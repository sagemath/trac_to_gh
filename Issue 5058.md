# Issue 5058: sage -f and sage -i is broken for local files

Issue created by migration from https://trac.sagemath.org/ticket/5058

Original creator: rlm

Original creation time: 2009-01-22 19:23:44

Assignee: mabshoff


```
[minime sage-3.3.alpha0.spkg_check]$ ./sage -i boehm_gc-7.1.p1.spkg 
Installing boehm_gc-7.1.p1.spkg
Calling sage-spkg on boehm_gc-7.1.p1.spkg
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
boehm_gc-7.1.p1.spkg
Machine:
Darwin minime.local 9.6.0 Darwin Kernel Version 9.6.0: Mon Nov 24 17:37:00 PST 2008; root:xnu-1228.9.59~1/RELEASE_I386 i386 i386 MacBook4,1 Darwin
Deleting directories from past builds of previous/current versions of boehm_gc-7.1.p1.spkg
Extracting package /Users/rlmill/sage-3.3.alpha0.spkg_check/boehm_gc-7.1.p1.spkg ...
-rw-r--r-- 1 rlmill staff 870192 2009-01-22 10:25 /Users/rlmill/sage-3.3.alpha0.spkg_check/boehm_gc-7.1.p1.spkg
./._boehm_gc-7.1.p1



...verbose untar...



Finished extraction
sage: After decompressing the directory boehm_gc-7.1.p1.spkg does not exist
etc... FAIL
```


The directory does not have .spkg on the end of it.


---

Attachment


---

Comment by boothby created at 2009-01-23 10:12:30

Looks good to me.


---

Comment by mabshoff created at 2009-01-23 10:35:09

Merged in Sage 3.3.alpha1


---

Comment by mabshoff created at 2009-01-23 10:35:09

Resolution: fixed
