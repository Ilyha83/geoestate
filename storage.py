# -*- coding: utf-8 -*-
"""
Database storage & JSON export for AI Developer Rankings.
"""

import json
import sqlite3
from datetime import datetime
from typing import List, Dict, Any
from config import DB_PATH, LATEST_JSON_PATH, TRACKED_DEVELOPERS, DEFAULT_COUNTRY


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS audit_runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_date TEXT NOT NULL,
        country TEXT NOT NULL,
        platforms TEXT NOT NULL,
        notes TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS raw_responses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id INTEGER,
        platform TEXT NOT NULL,
        prompt_id TEXT NOT NULL,
        response_text TEXT NOT NULL,
        created_at TEXT NOT NULL,
        FOREIGN KEY(run_id) REFERENCES audit_runs(id)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS developer_scores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        run_id INTEGER,
        run_date TEXT NOT NULL,
        developer_id TEXT NOT NULL,
        developer_name TEXT NOT NULL,
        region TEXT NOT NULL,
        mentions_count INTEGER DEFAULT 0,
        recommendations_count INTEGER DEFAULT 0,
        risks_count INTEGER DEFAULT 0,
        sov_percent REAL DEFAULT 0.0,
        recommendation_rate REAL DEFAULT 0.0,
        final_score REAL DEFAULT 0.0,
        rank INTEGER DEFAULT 0,
        delta_rank INTEGER DEFAULT 0,
        summary_pros TEXT,
        summary_risks TEXT,
        FOREIGN KEY(run_id) REFERENCES audit_runs(id)
    )
    """)

    conn.commit()
    conn.close()


def save_audit_run(run_date: str, country: str, platforms: List[str], responses: List[Dict[str, Any]], scored_developers: List[Dict[str, Any]]) -> int:
    init_db()
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO audit_runs (run_date, country, platforms) VALUES (?, ?, ?)",
        (run_date, country, ",".join(platforms))
    )
    run_id = cur.lastrowid

    for r in responses:
        cur.execute(
            "INSERT INTO raw_responses (run_id, platform, prompt_id, response_text, created_at) VALUES (?, ?, ?, ?, ?)",
            (run_id, r.get("platform"), r.get("prompt_id"), r.get("response_text", ""), run_date)
        )

    # Get previous run_id for delta calculations
    cur.execute("SELECT id FROM audit_runs WHERE id < ? ORDER BY id DESC LIMIT 1", (run_id,))
    prev_row = cur.fetchone()
    prev_ranks = {}
    if prev_row:
        prev_run_id = prev_row[0]
        cur.execute("SELECT developer_id, rank, final_score FROM developer_scores WHERE run_id = ?", (prev_run_id,))
        for row in cur.fetchall():
            prev_ranks[row[0]] = {"rank": row[1], "score": row[2]}

    for dev in scored_developers:
        dev_id = dev["id"]
        current_rank = dev["rank"]
        delta_rank = 0
        if dev_id in prev_ranks:
            # If rank went from 5 to 3, delta is +2 (improved)
            delta_rank = prev_ranks[dev_id]["rank"] - current_rank

        cur.execute("""
        INSERT INTO developer_scores (
            run_id, run_date, developer_id, developer_name, region,
            mentions_count, recommendations_count, risks_count,
            sov_percent, recommendation_rate, final_score,
            rank, delta_rank, summary_pros, summary_risks
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            run_id, run_date, dev_id, dev["name"], dev.get("region", ""),
            dev.get("mentions_count", 0), dev.get("recommendations_count", 0), dev.get("risks_count", 0),
            dev.get("sov_percent", 0.0), dev.get("recommendation_rate", 0.0), dev.get("final_score", 0.0),
            current_rank, delta_rank, dev.get("pros", ""), dev.get("risks", "")
        ))

    conn.commit()
    conn.close()

    export_latest_json(run_id)
    return run_id


def export_latest_json(run_id: int = None):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    if not run_id:
        cur.execute("SELECT id, run_date, country, platforms FROM audit_runs ORDER BY id DESC LIMIT 1")
        run_row = cur.fetchone()
        if not run_row:
            conn.close()
            return
        run_id = run_row["id"]
    else:
        cur.execute("SELECT id, run_date, country, platforms FROM audit_runs WHERE id = ?", (run_id,))
        run_row = cur.fetchone()

    cur.execute("""
    SELECT * FROM developer_scores WHERE run_id = ? ORDER BY rank ASC
    """, (run_id,))
    rows = cur.fetchall()

    items = []
    for r in rows:
        items.append({
            "rank": r["rank"],
            "delta_rank": r["delta_rank"],
            "id": r["developer_id"],
            "name": r["developer_name"],
            "region": r["region"],
            "score": round(r["final_score"], 1),
            "sov_percent": round(r["sov_percent"], 1),
            "recommendation_rate": round(r["recommendation_rate"], 1),
            "mentions": r["mentions_count"],
            "recommendations": r["recommendations_count"],
            "risks_count": r["risks_count"],
            "summary_pros": r["summary_pros"],
            "summary_risks": r["summary_risks"]
        })

    payload = {
        "updated_at": run_row["run_date"],
        "country": run_row["country"],
        "platforms": run_row["platforms"].split(","),
        "total_developers": len(items),
        "rankings": items
    }

    with open(LATEST_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    # Also save as JS variable for direct file:// browser support without CORS issues
    js_path = LATEST_JSON_PATH.parent / "rankings_data.js"
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(f"window.RANKINGS_DATA = {json.dumps(payload, ensure_ascii=False, indent=2)};\n")

    conn.close()
    return payload
