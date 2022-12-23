# Issue 7693: the lrs SPKG.txt is not very useful.

Issue created by migration from https://trac.sagemath.org/ticket/7693

Original creator: was

Original creation time: 2009-12-15 23:07:40

Assignee: tbd

CC:  wstein

The lrs SPKG.txt is just:

```
wstein@boxen:/tmp/wstein/lrs-4.2b.p0$ more SPKG.txt
* 2008-05-15 (Marshall Hampton)
*initial build
1. Deleted McGill-specific build stuff from makefile
2. Added SAGE_LOCAL gmp build locations
```

Fix this.  I was trying to figure out what the heck lrs is, and this wasn't helfpul. 


---

Comment by mhampton created at 2009-12-16 03:35:53

Well, that's strange, I had a much better package that was supposedly included about a year ago:

http://trac.sagemath.org/sage_trac/ticket/5018

I hadn't noticed since the actual program hadn't changed from p0 to p1.  I did all the work on that to prepare this for being a standard package, which I think it should be.


---

Comment by mhampton created at 2009-12-16 03:35:53

Changing status from new to needs_review.


---

Comment by was created at 2009-12-16 08:19:07

IU fixed that #5018 was never actually uploaded.


---

Comment by was created at 2009-12-16 08:19:07

Resolution: fixed
