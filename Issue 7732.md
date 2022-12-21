# Issue 7732: remove binary files from ECL distribution

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-18 06:19:16

Assignee: tbd

Figure out what these binary files are and if we can remove them:

```
         ecl-9.10.2-20091105cvs.p0/src/contrib/encodings/
```



---

Comment by was created at 2009-12-18 06:20:02

The author of ECL remarks:

```
Dear William,

the encodings directory contains files which are needed by ECL to understand files in other formats -- windows encodings, japanese, russian, etc. It only works if you build ECL with support for Unicode (--enable-unicode)

Juanjo
```



---

Comment by was created at 2009-12-18 06:20:35

More readable version:

```
Dear William,

the encodings directory contains files which are needed by ECL to understand files in
 other formats -- windows encodings, japanese, russian, etc. It only works if you 
build ECL with support for Unicode (--enable-unicode)

Juanjo
```



---

Comment by was created at 2009-12-18 06:24:22

Changing status from new to needs_review.


---

Comment by was created at 2009-12-18 06:24:22

The new spkg is here:
 
    http://wstein.org/home/wstein/patches/ecl-9.10.2-20091105cvs.p1.spkg


---

Comment by drkirkby created at 2009-12-21 13:26:50

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2009-12-21 13:26:50

Looks safe and fine and works for me.


---

Comment by mhansen created at 2010-01-03 22:19:55

Resolution: fixed
