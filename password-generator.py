#!/usr/bin/python3
# -*- coding: utf-8 -*-

import random                                    #import random

word=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','(',')','-','_','+','=','~','`','[',']','{','}','|',':',';','"',"'",'<','>',',','.','?','/']     #character allowed in password



length = int(input('length of password: '))      #ask for length of password
login = input('this password for :')             #ask for login name to save
print("Generating your password ")               #print a banner


pswd=[]                                          #list to make random password in
for i in range(length):
   pswd.append(random.choice(word))

fin=pswd                                         #set finish password as string not list

print ('[✔] Your password is ')

f=open("saved-passwords.txt","a")                #create file to save passwords in
f.write("\n")
f.write(login)                                   #set login name
f.write(' : ')


for n in fin:                                   #for-loop to extract ' from list
    print(n,end='')                             #print final password
    f.write(n)                                  #write password to file

f.close()                                       #close and save the file




