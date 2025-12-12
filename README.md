## Variations

### 1. Python

| Environment | File    |
| :---------: | :------ |
|    .venv    | main.py |

### 2. C++

| Compiler | File     |
| :------: | :------- |
|   g++    | main.cpp |

### 3. C

| Compiler | File   |
| :------: | :----- |
|   gcc    | main.c |

### 4. Assembly (Potential Future Development)

|   OS    |  Assembler  | Build Script |   File   |
| :-----: | :---------: | :----------: | :------: |
| Windows | NASM 64-bit |  build.bat   | main.asm |
| Windows | MASM 64-bit |  build.bat   | main.asm |
|  Linux  | NASM 64-bit |   build.sh   | main.asm |
|  Linux  | GAS 64-bit  |   build.sh   | main.asm |

## File Structure

This is the basic file structure I will stick to for each application, this is subject to change based on the number of scripts I use in each part.

```
.../
    assembly/
        windows/
            masm/
                build.bat
                main.asm
            nasm/
                build.bat
                main.asm
        linux/
            gas/
                build.sh
                main.asm
            nasm/
                build.sh
                main.asm
    c++/
        main.cpp
        build/
            windows/
                main.o
                app.exe
            linux/
                main.o
                app
    c/
        main.c
        build/
            windows/
                main.o
                app.exe
            linux/
                main.o
                app
    data/
            # Varies based on application
    python/
        venv/
        main.py
    README.MD
```
