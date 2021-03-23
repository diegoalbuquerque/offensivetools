# offensivetools
My little tools created to study and practice offensive thinking

## Byte Array Generator
Generate partial or full bytearray to help at binary exploitation

[+] use: ./bytearraygen [-i From_Value] [-l To_Value] [-b Badchars_to_exclude>] [-f file_name]

This script will generate two files of chars in hexadecimal format and binary format to use with mona.py or another similar script to find bad chars in memory, from Initial Value (-i) to last value (-l), excluding Badchars (-b)

*Parameters:*

All parameters are optional.  
-i -> Initial value   
-l -> last value   
-b -> String of hexadecimal values separate by comma  
-f -> file name  
  
*Output:* 
  
<file_name>.txt -> array of hexadecimal values  
<file_name>.bin -> binary file of chars. 
  
*Example*
```
$./bytearraygen.py -i 75 -l 100 -b "0x5c,0x5e"    
╔╗ ┬ ┬┌┬┐┌─┐╔═╗┬─┐┬─┐┌─┐┬ ┬
╠╩╗└┬┘ │ ├┤ ╠═╣├┬┘├┬┘├─┤└┬┘
╚═╝ ┴  ┴ └─┘╩ ╩┴└─┴└─┴ ┴ ┴ 
┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
│ ┬├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
└─┘└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─
v0.1 -           19.03.2021
            by joaninhaDark
 
[+] Generating bytearray from 75 to 100 to files: bytearray.txt/.bin
[-] Excluded 0x5c,0x5e, bytes: 
[+] line to copy paste: 

buf="\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5d\x5f\x60\x61\x62\x63"

$ xxd bytearray.bin                                
00000000: 4b4c 4d4e 4f50 5152 5354 5556 5758 595a  KLMNOPQRSTUVWXYZ
00000010: 5b5d 5f60 6162 63                        []_`abc

$ cat bytearray.txt
\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5d\x5f\x60\x61\x62\x63%                                                                              

```


## getenviroment
Print the enviroment variable address and its content in hexadecimal

```
 [+] use:  getenviroment <variable-name> <length-of-memory>
    <variable-name> : enviroment variable name to get the address
    <length-of-memory> : length, in bytes, of memory that will be leaked beginning 
                          at address of the variable 

     caution! Big length can cause Segmentation Fault if the application try to read
              not allowed memory!

 [+] Example: 
      $ export binsh="/bin/sh"  (\x2f\x62\x69\x6e\x2f\x73\x68)
      $ getenviroment binsh 20
        [+] The variable binsh is at: 0xffffdfb5
        [+] Memory content at 0xffffdfb5
            \x2F\x62\x69\x6E\x2F\x73\x68\x0\x5F\x3D\x2F\x68\x6F\x6D\x65\x2F\x6B\x61\x6C\x69%   
```
