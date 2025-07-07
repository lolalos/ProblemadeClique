@echo off
echo ==========================================
echo   Análisis de Cliques DBLP - Versión Simplificada
echo ==========================================
echo.

cd /d "%~dp0backend"

echo 🔍 Ejecutando análisis completo de cliques...
echo 📊 Esta versión NO requiere instalación de paquetes
echo ⏱️  El análisis puede tomar unos minutos
echo.

python clique_simple.py

echo.
echo ==========================================
echo   Análisis Completado
echo ==========================================
echo.
echo 💡 Si quieres la versión con interfaz web:
echo    1. Ejecuta: install_venv.bat
echo    2. Luego: run_venv.bat
echo.
pause
