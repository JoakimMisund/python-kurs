#!/usr/bin/env python3
import sys

def sum(tall1=0, tall2=0, tall3=0):
    print("Summen er:", tall1 + tall2 + tall3)

def main():
    if len(sys.argv) == 2:                                        # Sjekk om antall argumenter er 2
        sum(sys.argv[1])                                          # Kjør sum med 1 argument
        
    elif len(sys.argv) == 3:                                      # Sjekk om antall argumenter er 3
        sum(int(sys.argv[1]), int(sys.argv[2]))                   # Kjør sum med 2 argumenter
        
    elif len(sys.argv) == 4:                                      # Sjekk om antall argumenter er 4
        sum(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])) # Kjør sum med 3 argumenter
        
    else:
        sum()                                                     # Kjør sum med 0 argumenter
    
if __name__ == '__main__':
    main()