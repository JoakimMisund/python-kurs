import sys

def main():
    if "-h" in sys.argv:
        print("Bruk -c n hvor n er ett tall.")
        print("Bruk -s str hvor str er en string.")
    elif "-c" in sys.argv:
       print(list(range(0,int(sys.argv[2])+1)))
    elif "-s" in sys.argv:                                # Kjør sum med 0 argumenter
        streng = sys.argv[2]
        print("Lengden på strengen er ", len(streng))
        for i in range(1,len(streng),2):
            print("Ny streng ", streng[i])
    
if __name__ == '__main__':
    main()