@echo off

set TEST_DIR=.\tests\input_files

FOR %%f IN ("%TEST_DIR%\t*.in") DO (
    echo %%f
    set BASE_NAME=%%~nf
    python ./main.py %%f > .\tests\output_files\t1.res
    FC ".\tests\output_files\t1.res" ".\tests\expected_files\t1.out" /N /L > nul
    IF %ERRORLEVEL% EQU 0 (
        echo [Test #1] - Passed
    ) ELSE (
        echo [Test #1] - Failed
    )
)