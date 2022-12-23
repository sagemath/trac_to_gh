# Issue 9133: sage-4.4.3.alpha2: pynac build failure on an itanium box (easy autoconf issue)

Issue created by migration from https://trac.sagemath.org/ticket/9133

Original creator: was

Original creation time: 2010-06-03 16:08:35

Assignee: GeorgSWeber


```

cd . && /bin/sh /home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src/missing --run autoconf
/home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src/missing: line 54: autoconf: command not found
WARNING: `autoconf' is missing on your system.  You should only need it if
         you modified `configure.ac'.  You might want to install the
         `Autoconf' and `GNU m4' packages.  Grab them from any GNU
         archive site.
/bin/sh ./config.status --recheck
running CONFIG_SHELL=/bin/sh /bin/sh ./configure --disable-static --prefix=/home/wstein/screen/iras/sage-4.4.3.alpha2/local CC=gcc LDFL
AGS= CXX=g++ --no-create --no-recursion
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... configure: error: newly created file is older than distributed files!
Check your system clock
make[2]: *** [config.status] Error 1
make[2]: Leaving directory `/home/wstein/screen/iras/sage-4.4.3.alpha2/spkg/build/pynac-0.2.0.p1/src'
Error building pynac.

real    0m13.248s
user    0m5.660s
sys     0m2.400s
sage: An error occurred while installing pynac-0.2.0.p1
```



---

Comment by was created at 2010-06-03 16:13:42

Changing status from new to needs_review.


---

Comment by was created at 2010-06-03 16:13:42

The new spkg here works fine:

   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p2.spkg

All I did was type "autoreconf" in src, and also update the SPKG.txt.


---

Comment by was created at 2010-06-03 16:20:57

The above package builds fine on iras:

```
Done installing pynac.

real    7m5.748s
user    6m28.244s
sys     0m9.272s
Successfully installed pynac-0.2.0.p2
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing pynac-0.2.0.p2.spkg
wstein@iras:~/screen/iras/sage-4.4.3.alpha2>  
```



---

Comment by mhansen created at 2010-06-03 18:19:53

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-03 18:19:53

Looks good to to me.  This builds on both Cygwin and my linux box.


---

Comment by was created at 2010-06-04 15:18:47

Resolution: fixed
