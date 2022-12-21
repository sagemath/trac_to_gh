# Issue 3597: building sage on opensuse x86_64 fails with readline detection error

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-07 23:30:37

Assignee: mabshoff

This is on menas on skynet:


```

Configure findings:
  FFI:        no (user requested: default)
  readline:   no (user requested: /home/wstein/menas/build/sage-3.0.4.alpha2/local)
  libsigsegv: no, consider installing GNU libsigsegv
As you requested, we will proceed without libsigsegv...
./makemake  --with-readline=/home/wstein/menas/build/sage-3.0.4.alpha2/local --prefix=/home/wstein/menas/build/sage-3.0.4.alpha2/local --without-libintl    > Makefile
makemake: configure failed to detect readline
Error configuring clisp

real    0m35.648s
user    0m10.957s
sys     0m10.445s
sage: An error occurred while installing clisp-2.46.p1

```



---

Comment by was created at 2008-07-07 23:47:39

Here it is:

  http://sage.math.washington.edu/home/was/patches/clisp-2.46.p2.spkg


---

Comment by mabshoff created at 2008-07-08 00:16:56

Positive review, it builds for me, but cripples Maxima for now. Oh well, Maxima without readline is better than no Maxima at all.

Cheers,

Michael


---

Comment by was created at 2008-07-08 00:18:45

Resolution: fixed


---

Comment by mabshoff created at 2008-07-08 00:40:54

Merged in Sage 3.0.4.rc0
