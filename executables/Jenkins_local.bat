
@ECHO ON

"C:\Program Files\Python35\Scripts\pip3.5.exe" install virtualenv

set working_folder=%cd%


if exist %working_folder%\pythonenvironment\ (
  cd %working_folder%\pythonenvironment\
  dir
) else (
mkdir %working_folder%\pythonenvironment\
)

if exist %working_folder%\test_results\result\ (
  cd %working_folder%\test_results\result\
  del . /F /Q
)

cd %working_folder%

"c:\Program Files\Python35\python.exe" -m venv %working_folder%\pythonenvironment

%working_folder%\pythonenvironment\Scripts\python.exe -m pip install --upgrade pip

%working_folder%\pythonenvironment\Scripts\pip3.5.exe install -r %working_folder%\requirements.txt

setx path "%path%;%working_folder%\shared_resources"

cd %working_folder%

REM execute features
%working_folder%\pythonenvironment\Scripts\behave.exe -f allure_behave.formatter:AllureFormatter -o %working_folder%\test_results\result\ %working_folder%\features\try.feature

REM generate reports
call %working_folder%\shared_resources\allure-2.5.0\bin\allure.bat generate %working_folder%\test_results\result --clean -o %working_folder%\test_results\report\
call %working_folder%\shared_resources\allure-2.5.0\bin\allure.bat serve %working_folder%\test_results\result
@echo off