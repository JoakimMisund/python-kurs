import argparse

def streng_func(s):
    print("Lengden på strengen er ", len(s))
    for i in range(1,len(s),2):
        print("Ny streng ", s[i])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', type=int,required=False, help='Input ett tall')
    parser.add_argument('-s', type=str,required=False, help='Input en streng')
    args = parser.parse_args()
    if args.c:
         print([*range(0,int(args.c)+1)])  
    elif args.s:
        streng_func(args.s)
if __name__ == '__main__':
    main()