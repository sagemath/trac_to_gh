# Issue 6868: [with SPKG, needs review] Coin-OR CBC ( compatible with the symbolics from MIP )

Issue created by migration from https://trac.sagemath.org/ticket/6868

Original creator: ncohen

Original creation time: 2009-09-02 17:34:38

Assignee: tbd

Hello everybody !!!

As I wrote a new numerical.MIP class using symbolics, which will be waaaaaayyyyy easier to use, here is the necessary update of GLPK which can stand all those news !

To install it :


```
sage -f http://www-sop.inria.fr/members/Nathann.Cohen/cbc-2.3.p0.spkg
```



---

Comment by mvngu created at 2009-09-02 17:49:00

ncohen --- Can you also provide a local copy of the spkg under your sage.math home dir?


---

Comment by ncohen created at 2009-09-02 19:37:44

Done : /home/ncohen/cbc-2.3.p0.spkg


---

Comment by mvngu created at 2009-09-08 14:57:46

Updated package at

http://sage.math.washington.edu/home/mvngu/release/spkg/optional/cbc-2.3.p0.spkg

It incorporates ncohen's original spkg, but with some general clean up.


---

Comment by mvngu created at 2009-09-10 12:19:51

Merged in the optional packages repository at

http://www.sagemath.org/packages/optional/

You can get the spkg at

http://www.sagemath.org/packages/optional/cbc-2.3.p0.spkg


---

Comment by mvngu created at 2009-09-10 12:19:51

Resolution: fixed
