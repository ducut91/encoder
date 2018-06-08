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
                print str.encode('base64','strict')
            elif(sys.argv[2]) == 'hex':
                print str.encode('hex','strict')
            elif(sys.argv[2]) == 'url':
                print urllib.quote(str)
            else:
                help.help()
        elif sys.argv[1] == 'decode':
            if(sys.argv[2]) == 'base64':
                str += '==='
                print str.decode('base64','strict')
            elif(sys.argv[2]) == 'hex':
                str = hextranslate(str)
                print str
            elif(sys.argv[2]) == 'url':
                print urllib.unquote(str)
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
