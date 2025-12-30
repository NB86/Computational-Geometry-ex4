@echo off
setlocal enabledelayedexpansion

set TEST_DIR=.\tests\input_files

FOR %%f IN ("%TEST_DIR%\*.in") DO (
    set BASE_NAME=%%~nf
    
    :: Run the algorithm (Mode 1)
    python ./main.py %%f > .\tests\output_files\%%~nf.res
    
    :: Generate the expected output (Mode 2)
    python ./main.py %%f -m 2 > .\tests\expected_files\%%~nf.out 
    
    :: Compare the files
    FC ".\tests\output_files\%%~nf.res" ".\tests\expected_files\%%~nf.out" /N /L > nul
    
    :: CRITICAL: Use ! instead of % to get the updated ErrorLevel
    IF !ERRORLEVEL! EQU 0 (
        echo [%%~nf] - Passed
    ) ELSE (
        echo [%%~nf] - Failed
    )
)

pause