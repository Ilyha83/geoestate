# -*- coding: utf-8 -*-
"""
Analyzer & Scorer for AI responses.
Extracts developer mentions, detects recommendations vs risk warnings,
and calculates the AI Visibility & Trust Index.
"""

import re
from typing import List, Dict, Any
from config import TRACKED_DEVELOPERS

POSITIVE_SIGNALS = [
    r"рекоменд", r"лидер", r"надежн", r"топ", r"высок(?:ое|ий|ая) качеств",
    r"чист(?:ый|ые) титул", r"сдан(?:о|ы) в срок", r"популярн", r"безупречн",
    r"премиум", r"хорош(?:ая|ий) репутац", r"высокий спрос", r"высок(?:ая|ий) roi",
    r"best", r"top", r"recommend", r"reliable", r"trusted", r"award"
]

RISK_SIGNALS = [
    r"осторожн", r"риск", r"суд(?:ебн|а|ом)", r"задержк", r"не рекоменд",
    r"проблем", r"жалоб", r"претензи", r"низк(?:ий|ая) рейтинг", r"пессимиз",
    r"caution", r"avoid", r"delay", r"lawsuit", r"court", r"complaint", r"warning",
    r"банкрот", r"негатив"
]


# Phrases that should NOT trigger a risk penalty because they are actually positive/neutral
NEGATIVE_EXCLUSIONS = [
    r"редк(?:ие|их)\s+жалоб",
    r"нет\s+жалоб",
    r"жалоб\s+нет",
    r"отсутств(?:ие|уют)\s+(?:суд|жалоб|претензи|проблем)",
    r"без\s+(?:суд|задержек|проблем)",
    r"жалобы\s+касаются\s+лишь\s+мелк",
    r"минимальн(?:ый|ые)\s+риск",
    r"жалобы\s+отсутствуют"
]


def score_responses(responses: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    responses: list of dicts with:
      - platform: 'Gemini' | 'ChatGPT' | 'Perplexity'
      - prompt_id: str
      - response_text: str
    """
    total_audits = len(responses)
    if total_audits == 0:
        return []

    results = []

    for dev in TRACKED_DEVELOPERS:
        dev_id = dev["id"]
        dev_name = dev["name"]
        aliases = dev["aliases"]
        
        # Build regex for matching developer name or aliases
        pattern = r"(?:\b|_)(?:" + "|".join(re.escape(a) for a in aliases) + r")(?:\b|_)"
        regex = re.compile(pattern, re.IGNORECASE)

        mentions_count = 0
        rec_count = 0
        risk_count = 0
        pros_snippets = []
        risks_snippets = []

        for resp in responses:
            text = resp.get("response_text", "")
            if not text:
                continue

            matches = list(regex.finditer(text))
            if not matches:
                continue

            mentions_count += 1

            for m in matches:
                start = max(0, m.start() - 150)
                end = min(len(text), m.end() + 250)
                snippet = text[start:end].strip()

                # Check if risk signal is just a false positive (e.g. "редкие жалобы")
                is_false_risk = any(re.search(exc, snippet, re.IGNORECASE) for exc in NEGATIVE_EXCLUSIONS)

                has_pos = any(re.search(sig, snippet, re.IGNORECASE) for sig in POSITIVE_SIGNALS)
                has_risk = not is_false_risk and any(re.search(sig, snippet, re.IGNORECASE) for sig in RISK_SIGNALS)

                if has_pos and not has_risk:
                    rec_count += 1
                    clean_snip = snippet.replace("\n", " ").strip()
                    if len(clean_snip) > 130:
                        clean_snip = clean_snip[:130] + "..."
                    if clean_snip not in pros_snippets and len(pros_snippets) < 2:
                        pros_snippets.append(clean_snip)

                elif has_risk:
                    risk_count += 1
                    clean_snip = snippet.replace("\n", " ").strip()
                    if len(clean_snip) > 130:
                        clean_snip = clean_snip[:130] + "..."
                    if clean_snip not in risks_snippets and len(risks_snippets) < 2:
                        risks_snippets.append(clean_snip)

        # 1. Share of Voice (0 to 100%)
        sov_percent = min(100.0, (mentions_count / total_audits) * 100.0)

        # 2. Raw recommendation rate
        raw_rec_rate = min(100.0, (rec_count / max(1, mentions_count)) * 100.0)

        # 3. Statistical Confidence Weight:
        # A developer with only 1 mention cannot get full 100% credibility score.
        # Confidence scales smoothly: 1 mention = 0.4x weight, 2 mentions = 0.7x weight, 3+ mentions = 1.0x weight
        confidence = min(1.0, mentions_count / max(1, min(3, total_audits)))
        weighted_rec_rate = raw_rec_rate * confidence

        # 4. Risk penalty: only penalize genuine confirmed risks
        risk_penalty = min(35.0, (risk_count / max(1, mentions_count)) * 30.0)

        # 5. Composite Final Score:
        # 55% Volume & Scale (SoV) + 40% Weighted Trust/Recommendation - Risk Penalty
        final_score = max(0.0, min(100.0, (sov_percent * 0.55) + (weighted_rec_rate * 0.40) - risk_penalty))

        results.append({
            "id": dev_id,
            "name": dev_name,
            "region": dev.get("region", ""),
            "website": dev.get("website", ""),
            "mentions_count": mentions_count,
            "recommendations_count": rec_count,
            "risks_count": risk_count,
            "sov_percent": sov_percent,
            "recommendation_rate": raw_rec_rate,
            "final_score": final_score,
            "pros": "; ".join(pros_snippets) if pros_snippets else "Стандартное присутствие в каталогах",
            "risks": "; ".join(risks_snippets) if risks_snippets else "Критических стоп-факторов не обнаружено"
        })

    # Sort by final score descending
    results.sort(key=lambda x: x["final_score"], reverse=True)

    # Assign ranks
    for idx, item in enumerate(results, 1):
        item["rank"] = idx

    return results
