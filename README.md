# Convert Images From HEIC Format To JPG Format

## Python Package Dependencies

- Pillow
- pillow-heif

## Quick Start (on Windows)
Build the binary executable using `pyinstaller`. 

In the following commands, repalce the `demo`, `heic_s`, `jpg_s` with the actual file and directory names. Replace the number coming after `-q` with your desired saved image quality, which is between 1 (worst) and 95 (best, default).

### Convert single heic file 
```ps1
myheic2jpg.exe -i demo.heic -o demo.jpg -q 20
```

### Convert multiple heic files from a directory in batch mode
```ps1
myheic2jpg.exe -i heic_s -o jpg_s -q 20
```

## CLI Input Arguments

```ps1
Convert heic files to jpg files

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The input heic file name or the input directory name
  -o OUTPUT, --output OUTPUT
                        The output heic file name or the output directory name
  -q QUALITY, --quality QUALITY
                        The saved image quality between 1 (worst) and 95 (best, default)

The arguments for -i and -o must either both be file names or directory names
```