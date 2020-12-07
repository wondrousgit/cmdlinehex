# cmdlinehex
a small cmdline hex tool wirtting in python for practice


A hex tool for modifying file.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  the input file name.
  -p POSITION, --position POSITION
                        the start address of writing postion. like 20, means
                        the 20th bit of this file.
  -v VALUE, --value VALUE
                        the hex data to write. like 504b0304
  -o OUTPUT, --output OUTPUT
                        the output file after modify.
                        
                        
to build a standalone executable with nuitka, please run:

  python -m nuitka --standalone cmdhex.py
  
keep the pythonXX.dll and cmdhex.exe in the folder cmdhex-dist.

Have Fun!
