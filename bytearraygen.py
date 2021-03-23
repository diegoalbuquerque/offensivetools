#!/usr/bin/env python3
import argparse

def main():
    
    ap = argparse.ArgumentParser("Generate bytearray")
    ap.add_argument("-i", "--initvalue", required=False, help="from value in decimal")
    ap.add_argument("-l", "--lastvalue", required=False, help="to value in decimal")
    ap.add_argument("-f", "--filename", required=False, help="destination filename")
    ap.add_argument("-b", "--badchars", required=False, help="string of badchars separated by coma like 0x0,0x0a,0x0d")
    args = vars(ap.parse_args())

    #badchars ="0x08,0x0a,0x10"
    badchars  = args["badchars"] if (args["badchars"] is not None ) else ""
    filename  = args["filename"] if (args["filename"] is not None ) else "bytearray"
    initvalue = int(args["initvalue"] if (args["initvalue"] is not None ) else 0)
    lastvalue = int(args["lastvalue"] if (args["lastvalue"] is not None ) else 256)

    #normalize badchars
    if len(badchars)>1: 
        temp = ""
        for byte in badchars.split(","): 
            if len(byte)<4:
                byte="0x{:02x}".format(int(byte,16))
            temp+=byte+","
        badchars = temp

    print ('╔╗ ┬ ┬┌┬┐┌─┐╔═╗┬─┐┬─┐┌─┐┬ ┬')
    print ('╠╩╗└┬┘ │ ├┤ ╠═╣├┬┘├┬┘├─┤└┬┘')
    print ('╚═╝ ┴  ┴ └─┘╩ ╩┴└─┴└─┴ ┴ ┴ ')
    print ('┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐')
    print ('│ ┬├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘')
    print ('└─┘└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─')  
    print ('v0.1 -           19.03.2021')
    print ("            by joaninhaDark")
    print (" ")
    print ("[+] Generating bytearray from {} to {} to files: {}.txt/.bin".format(initvalue,lastvalue,filename))
    print ("[-] Excluded {} bytes: ".format(badchars))
    print ("[+] line to copy paste: ")
    print ("")

    
    print('buf="',end="");
    fText = open(filename+".txt", "w")
    fBin  = open(filename+".bin", "wb")


    for i in range(initvalue, lastvalue):
        if ("0x{:02x}".format(i)) not in badchars:
            print("\\x{:02x}".format(i),end="")
            fText.write("\\x{:02x}".format(i))
            fBin.write(chr(i).encode('latin-1'))

    print('"')
    print("")

if __name__ == "__main__":
    main()
