# Issue 9146: cygwin: gd doesn't correctly link in libpng with sage-4.4.3.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-05 04:53:49

Assignee: tbd

The fix involves copying over $SAGE_LOCAL/bin/cygpng12-0.dll to $SAGE_LOCAL/lib/


---

Comment by mhansen created at 2010-06-05 04:58:55

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-06-05 04:58:55

There is an spkg at http://sage.math.washington.edu/home/mhansen/libpng-1.2.35.p2.spkg


---

Comment by was created at 2010-06-05 05:05:19

I tried installing on linux and:


```

make[2]: Leaving directory `/mnt/usb1/scratch/wstein/build/sage-4.4.3.rc0/spkg/build/libpng-1.2.35.p2/src'
make[1]: Leaving directory `/mnt/usb1/scratch/wstein/build/sage-4.4.3.rc0/spkg/build/libpng-1.2.35.p2/src'
./spkg-install: line 55: syntax error near unexpected token `fi'
./spkg-install: line 55: `fi'

```



---

Comment by was created at 2010-06-05 05:06:38

Fixed version:
   http://sage.math.washington.edu/home/wstein/patches/libpng-1.2.35.p2.spkg


---

Comment by was created at 2010-06-05 05:26:01

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-06-05 05:59:51

It doesn't work yet on Cygwin itself (on a clean install):

```

make[2]: Leaving directory `/home/wstein/sage-4.4.3/spkg/build/libpng-1.2.35.p2/src'
cp: cannot stat `/home/wstein/sage-4.4.3/local/bin/cygpng12-0.dll': No such file or directory
Error installing libpng

real    6m25.233s
user    1m28.601s
sys     4m59.953s
```



---

Comment by was created at 2010-06-05 05:59:51

Changing status from positive_review to needs_work.


---

Comment by was created at 2010-06-05 06:01:56

The above failure report is on cygwin upgraded to the latest version as of june 4, 2010.


---

Comment by mhansen created at 2010-06-05 08:24:38

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2010-06-05 08:24:38

The build completes successfully once "file" is installed in winxp3.  If "file" is not installed, then Cygwin has a difficult time making shared libraries.  This is why this wasn't an issue initially with my sage-4.3.5 install in winxp2.

We need to make "file" a preqreq.


---

Comment by was created at 2010-06-05 14:13:10

Yes, winxp3 is missing a lot of prerequisites.  MPIR also fails to build there.


---

Comment by was created at 2010-06-05 14:13:10

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-06 00:53:14

Resolution: fixed
