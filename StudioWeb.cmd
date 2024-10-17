chcp 866
cd /d "%~dp0"
taskkill /F /IM jupyter-lab.exe
call ..\Resources\WConfigure\Init.cmd orpa-std.exe orpa-std.exe -m pyOpenRPA.Studio "config.py"
start /B orpa-std.exe -m pyOpenRPA.Studio "config.py" --mode=web
call ..\Resources\WConfigure\CreateExe.cmd orpa-lab.exe orpa-lab.exe
set PYTHONIOENCODING=utf-8
orpa-lab.exe -m jupyter lab --config="%~dp0..\Resources\WConfigure\Orpa_lab_config.py
pause>nul
