@echo off
echo Assembling...
nasm -f win64 project.asm -o hello.obj
if errorlevel 1 goto :error

echo Linking...
gcc -nostartfiles -nostdlib -o hello.exe hello.obj -lkernel32
if errorlevel 1 goto :error

echo Build successful!
goto :eof

:error
echo Build failed.
pause
