# Issue 7696: zlib -- source spkg contains precompiled binary crap (.obj files)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-16 00:54:45

Assignee: tbd


```
zlib-1.2.3.p4/src/contrib/masmx86/inffas32.obj: 80386 COFF
zlib-1.2.3.p4/src/contrib/masmx86/gvmat32.obj: 80386 COFF
zlib-1.2.3.p4/src/contrib/masmx64/inffasx64.obj: ACB archive data
zlib-1.2.3.p4/src/contrib/masmx64/gvmat64.obj: ACB archive data
```


Delete the above and it builds fine.  Similar directories don't have obj files.

Note that the above is for Microsoft Windows anyways, so it's especially important we don't distribute their binary stuff!


---

Comment by was created at 2009-12-18 06:17:59

The following new spkg deletes the binary crap *and* also greatly improves the SPKG.txt:

    http://wstein.org/home/wstein/patches/zlib-1.2.3.p5.spkg


---

Comment by was created at 2009-12-18 06:17:59

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-27 16:09:22

Looks good to me.


---

Comment by mhansen created at 2009-12-27 16:09:22

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 22:23:23

Resolution: fixed
