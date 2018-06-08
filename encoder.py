import sys
import clipboard

from modules import help
import urllib

def main():
    if len(sys.argv) < 4 or len(sys.argv) > 5:
        help.help()


    if len(sys.argv) == 4:
        str = sys.argv[3]
        if sys.argv[1] == 'encode':
            if(sys.argv[2]) == 'base64':
                str = str.encode('base64','strict')
                print str
            elif(sys.argv[2]) == 'hex':
                str =  str.encode('hex','strict')
                print str
            elif(sys.argv[2]) == 'url':
                str = urllib.quote(str)
                print str
            else:
                help.help()
        elif sys.argv[1] == 'decode':
            if(sys.argv[2]) == 'base64':
                str += '==='
                str = str.decode('base64','strict')
                print str
            elif(sys.argv[2]) == 'hex':
                str = str.decode('hex', 'strict')
                print str
            elif(sys.argv[2]) == 'url':
                str =  urllib.unquote(str)
                print str
            else:
                help.help()
        clipboard.copy(str)


def hextranslate(s):
        res = ""
        for i in range(len(s)/2):
                realIdx = i*2
                res = res + chr(int(s[realIdx:realIdx+2],16))
        return res

if __name__ == '__main__':
	main()
