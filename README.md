# offensivetools
My little tools created to study and practice offensive thinking

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
