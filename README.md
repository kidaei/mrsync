
nom et prenom : KIdaei rawia
                GHARZOUZI Maria

# mrsync:
We decided to put the code on 2 versions because we could not make the code work at step 2 completely 
mrsync_version1:  the code for step 1 that works well 
mrsync_version2:  the code for step 1+2 that does not work 
(small remark)  in the code there is some part are code in French other one in English because one of us are comfy in language more than another

# STEP1

to test you can run this :   
-----with shebang----(#!/user/bin/python3)(#!/bin/python)
./mrsync.py --list-only . DST  
./mrsync.py src  
./mrsync.py -r  
./mrsync.py -r SRC/ DST/
-----without shebang------  
python3 ./mrsync.py --list-only . DST/  
python3 ./mrsync.py -r .  


## step 1 : done.  
--> 
The pathTolist(arg) function lists all the files that are in source with the os.path if recursive and os.listdir otherwise and The CopyFile function copies files from one source to a destination 


-->
```py
if "*" == args.SRC:

        args.SRC = "."

```
We added this code to arrive is execute this command 
./mrsync.py --list-only * DST
--> 

# STEP2 
to test you can run this  
./mrsync.py -r SRC/ DST/
./mrsync.py * DST/

## step 2 :unreachable code(it worke if we comment the line 15 , 16,25, 26, 30, 31 in serveur.py but in this case we have communication by one pipe )
-->
We tried to implement the tubes between client and server to copy the files from a source to a destination but But we could not solve the probleme
it could worke if 

# STEP3
To be done 
