# Issue 6867: [with SPKG, needs review] GLPK ( compatible with the symbolics from MIP )

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-09-02 17:33:12

Assignee: tbd

Hello everybody !!!

As I wrote a new numerical.MIP class using symbolics, which will be waaaaaayyyyy easier to use, here is the necessary update of GLPK which can stand all those news !

To install it :


```
sage -f http://www-sop.inria.fr/members/Nathann.Cohen/glpk-4.38.p1.spkg
```



---

Comment by mvngu created at 2009-09-02 17:47:44

ncohen --- Can you also provide a local copy of the spkg under your sage.math home dir?


---

Comment by ncohen created at 2009-09-02 19:38:05

Done : /home/ncohen/glpk-4.38.p1.spkg


---

Comment by mvngu created at 2009-09-08 14:56:36

Updated package at

http://sage.math.washington.edu/home/mvngu/release/spkg/optional/glpk-4.38.p1.spkg

It incorporates ncohen's original spkg, but with some general clean up.


---

Comment by mvngu created at 2009-09-10 12:17:59

Resolution: fixed


---

Comment by mvngu created at 2009-09-10 12:17:59

Merged in the optional packages repository at

http://www.sagemath.org/packages/optional/

You can get the spkg at

http://www.sagemath.org/packages/optional/glpk-4.38.p1.spkg
