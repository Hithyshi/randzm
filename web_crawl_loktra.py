import re
import sys
import urllib

def first_query(kw):
    firsturl = 'http://www.shopping.com/products?KW=' + kw 
    ufirst = urllib.urlopen(firsturl)
    text1 = ufirst.read()
    num_items = re.findall(r'NumItemsReturned:(\d+)', text1)
    print num_items	

def sec_query(kw, pn):
    firsturl = 'http://www.shopping.com/products?KW=' + kw 
    ufirst = urllib.urlopen(firsturl)
    text1 = ufirst.read()
    securl = 'http://www.shopping.com/products~PG-' + str(pn) + '?KW=' + kw
    usec = urllib.urlopen(securl)	
    text2 = usec.read()
    num_items2 = re.findall(r'NumItemsReturned:(\d+)', text1)
    	
    if num_items2 !=[]:	
        num_items_page = re.findall(r'id=\"nameQA.*title=\"(.*)\">', text2)
        print num_items_page	
		
			
    else: print "no items"	
	
def main():
    if len(sys.argv) == 2:
        keyword = sys.argv[1]
        first_query(keyword)		
        
    elif len(sys.argv) == 3:
        keyword = sys.argv[1]
        page_num = int(sys.argv[2])
        sec_query(keyword, page_num)
		
    else: 
        sys.exit(1)	

if __name__ == '__main__':
    main()