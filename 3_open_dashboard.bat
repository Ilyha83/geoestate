@echo off
chcp 65001 > nul
echo Открытие сайта-дашборда в браузере...
start "" "%~dp0index.html"
