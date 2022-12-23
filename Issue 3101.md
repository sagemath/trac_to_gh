# Issue 3101: pbuild: mwrank.so needs to be build as a C++ extension

Issue created by migration from https://trac.sagemath.org/ticket/3101

Original creator: mabshoff

Original creation time: 2008-05-04 04:12:24

Assignee: gfurnish

Some people have reported mwrank.so missing some symbols at startup when compiled with pbuild, but the old build system is fine.

Working:

```
g++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/mwrank/mwrank.o 
build/temp.linux-x86_64-2.5/sage/libs/mwrank/wrap.o -L/scratch/mabshoff/
release-cycle/sage-3.0.1.final/local//lib -lcsage -lcurvesntl -lg0nntl 
-ljcntl -lrankntl -lntl -lgmp -lgmpxx -lstdc++ -lm -lpari -lstdc++ -lntl 
-o build/lib.linux-x86_64-2.5/sage/libs/mwrank/mwrank.so
```


Non-working:

```
gcc -O3 -g -fwrapv -shared -fno-strict-aliasing /mnt/drive_hda1/sagefiles/
sage-3.0.1.rc0/devel/sage/build/temp/sage/libs/mwrank/mwrank.o -L/home/wdj/
wdj/sagefiles/sage-3.0.1.rc0/local/lib  -lcsage  -lcurvesntl  -lg0nntl  
-ljcntl  -lrankntl  -lntl -lgmp  -lgmpxx  -lstdc++  -lm  -lpari  -lstdc++  
-lntl  -o /mnt/drive_hda1/sagefiles/sage-3.0.1.rc0/devel/sage-main/build/
sage/libs/mwrank/mwrank.so
```


mwrank.so is a C wrapper around a C++ extension, so on some systems the linker ends up either being stupid or clever depending on your perspective. 

Cheers,

Michael


---

Comment by gfurnish created at 2008-05-04 07:45:51

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-05-04 08:08:11

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-04 08:08:23

Resolution: fixed


---

Comment by mabshoff created at 2008-05-04 08:08:23

Merged in Sage 3.0.1.final
