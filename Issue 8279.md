# Issue 8279: cygwin: cliquer names the library incorrectly for cygwin

Issue created by migration from https://trac.sagemath.org/ticket/8279

Original creator: was

Original creation time: 2010-02-16 01:26:20

Assignee: tbd

Building the sage library fails because the cliquer shared object library is named incorrectly on cygwin.  It should be named with .dll but is named with .so.


```
   [ ] fails not finding cliquer:
gcc -shared -Wl,--enable-auto-image-base build/temp.cygwin-1.7.1-i686-2.6/sage/graphs/cliquer.o -L/home/wstein/build/sage-\
4.3.3.alpha0/local//lib -L/home/wstein/build/sage-4.3.3.alpha0/local/lib/python2.6/config -lcsage -lcliquer -lstdc++ -lntl\
 -lpython2.6 -o build/lib.cygwin-1.7.1-i686-2.6/sage/graphs/cliquer.dll
/usr/lib/gcc/i686-pc-cygwin/4.3.4/../../../../i686-pc-cygwin/bin/ld: cannot find -lcliquer
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1

  The problem is due to a misnamed library:

$ cd local/lib/
$ ls -lh *cliq*
-rwxr-xr-x 1 wstein None 167K 2010-02-12 22:40 libcliquer.so
$ ln -s libcliquer.so libcliquer.dll

That works.
```



---

Comment by mhansen created at 2010-02-16 04:29:29

I've put the spkg that fixes this at http://sage.math.washington.edu/home/mhansen/cygwin_port/cliquer-1.2.p5.spkg


---

Comment by mhansen created at 2010-02-16 04:29:29

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-02-16 05:22:21

This also includes David Kirkby's suggestions at #7308.


---

Comment by mvngu created at 2010-02-17 00:22:54

Sage 4.3.3.alpha0 rebuilt OK with this updated spkg. All doctests passed. The Cygwin build of Sage 4.3.3alpha0 also got pass the compilation process of cliquer.


---

Comment by mvngu created at 2010-02-17 00:22:54

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-02-17 00:23:26

Resolution: fixed


---

Comment by mhansen created at 2010-02-17 00:24:37

Could you check that libcliquer.dll is in your Cygwin build?
