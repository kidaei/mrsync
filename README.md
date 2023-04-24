# STEP1

to test you can run this :   
-----with shebang----(#!/user/bin/python3)(#!/bin/python)
./mrsync.py --list-only . DST  
./mrsync.py src  
./mrsync.py -r  
-----without shebang------  
python3 ./mrsync.py --list-only . DST/  
python3 ./mrsync.py -r .  


## step 1 : done.  
To be checked:   
1. ./mrsync *.py --list-only  
2. add the permession whit os.stat   
```py
print()
```

# STEP2  
  to test you can run this  
./mrsync.py -r SRC/ DST/

