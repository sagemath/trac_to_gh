# Issue 6663: add new 4ti2 and glpk experimental packages

Issue created by migration from https://trac.sagemath.org/ticket/6663

Original creator: mhampton

Original creation time: 2009-07-31 20:14:51

Assignee: tbd

Keywords: 4ti2, glpk, sandpile

The 4ti2 and glpk packages in experimental are very out of date.  Since there seems to be some growing interest in having them available in sage they should be updated.  If they can be made to work on more platforms they should be moved to optional.


---

Comment by mhampton created at 2009-07-31 20:19:51

My current package attempts are at:

http://www.d.umn.edu/~mhampton/4ti2.p0.spkg
http://www.d.umn.edu/~mhampton/glpk.p0.spkg 

-Marshall


---

Comment by mhampton created at 2009-07-31 23:06:41

I was unaware of the glpk package at:
http://trac.sagemath.org/sage_trac/ticket/6602

which has a more recent version of glpk.  That spkg should be used instead of mine.


---

Comment by wdj created at 2009-08-01 04:08:41

This 4ti2 spkg installed fine with N Cohen's glpk (http://trac.sagemath.org/sage_trac/ticket/6602) on an amd64 ubuntu 9.04 machine.


---

Comment by wdj created at 2009-08-01 20:11:36

This installed fine and passed sage -testall (except for the known failures) on an intel macbook with 4.1.1.a0 running OS 10.4.11.

This gets a positive review from me. Are there more tests which should be run before "needs review" gets changed to "positive review"?


---

Comment by AlexGhitza created at 2009-08-16 05:52:54

Changing component from algebra to packages.


---

Comment by AlexGhitza created at 2009-08-16 05:52:54

Changing assignee from tbd to mabshoff.


---

Comment by mvngu created at 2009-09-02 08:11:40

I have downloaded the spkg to my home directory:



http://sage.math.washington.edu/home/mvngu/patch/4ti2.p0.spkg



Is there any special reason why the package is not under revision control?

```
[mvngu@mod mvngu]$ tar -jxf 4ti2.p0.spkg 
[mvngu@mod mvngu]$ cd 4ti2.p0/
[mvngu@mod 4ti2.p0]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
```



---

Comment by mvngu created at 2009-09-11 18:11:36

Merged in the experimental packages repository at

http://www.sagemath.org/packages/experimental/

The updated spkg is available at

http://www.sagemath.org/packages/experimental/4ti2.p0.spkg


---

Comment by mvngu created at 2009-09-11 18:11:36

Resolution: fixed


---

Comment by mvngu created at 2009-09-20 22:35:51

Changing component from packages to experimental package.
