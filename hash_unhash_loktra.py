import sys

def unhash(key):

    mystr=''
    letters = "acdegilmnoprstuw"
    while key >= 37:	
		
        mystr=mystr+letters[key%37]
        key=key / 37		
    return mystr[::-1]

def main():
    try:	
        if len(sys.argv) != 2 :	
            print "Wrong input. Please provide a hash number (integer) after the program name" 
            sys.exit()	
        
        mykey=int(sys.argv[1])	
        print unhash(mykey)		

    except:
        print "Wrong input. Please provide a hash number (integer) after the program name" 	
	
if __name__ == '__main__':
    main()	
