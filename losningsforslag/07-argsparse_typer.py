import argparse
import typer
from typing import Optional

def streng_func(s):
    print("Lengden på strengen er ", len(s))
    for i in range(1,len(s),2):
        print("Ny streng ", s[i])

def argsparse_example():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int,required=False, help='Input ett tall')
    parser.add_argument('-s', type=str,required=False, help='Input en streng')
    args = parser.parse_args()
    if args.c:
         print([*range(0,int(args.c)+1)])  
    elif args.s:
        streng_func(args.s)

def typer_example(
          tall: Optional[int] = typer.Option(default=None, help="Input ett tall"),
          streng: Optional[str] = typer.Option(default=None,help="Input en streng"),
    ):
    if tall is not None:
        print([*range(0,int(tall)+1)]) 
    if streng is not None:
        streng_func(streng)

if __name__ == '__main__':
    #argsparse_example()
    typer.run(typer_example)