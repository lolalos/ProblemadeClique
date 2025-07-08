@echo off
echo ==========================================
echo   Analisis de Cliques DBLP - Version Simplificada
echo ==========================================
echo.

cd /d "%~dp0backend"

echo Ejecutando analisis completo de cliques...
echo Esta version NO requiere instalacion de paquetes
echo El analisis puede tomar unos minutos
echo.

python -m pip show matplotlib >nul 2>&1
if errorlevel 1 (
	echo El paquete matplotlib no esta instalado. Instalando...
	python -m pip install matplotlib
)

python clique_simple.py

echo.
echo ==========================================
echo   Analisis Completado
echo ==========================================
echo.
echo Si quieres la version con interfaz web:
echo    1. Ejecuta: install_venv.bat
echo    2. Luego: run_venv.bat
echo.
pause
