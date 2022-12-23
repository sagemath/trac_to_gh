# Issue 199: ling long sent some congruence subgroup code -- put in sage.

Issue created by migration from https://trac.sagemath.org/ticket/199

Original creator: was

Original creation time: 2007-01-19 11:35:14

Assignee: was




---

Comment by was created at 2007-01-19 11:36:10

cong group code


---

Attachment


```
To run:

cd \cygdrive\c\
cd (directory where the file is)
load "conggroups.sage"

To calculate a list of generators:
generators("Gamma",2,0)               (The third parameter is for inputing
generators("GammaBar0",11,0)           a list of coset representatives.
generators("GammaBar",3,0)             Putting 0 tells it to calculate the list)

To calculate a list of cusps:
cusps(cosetreps("Gamma",2))

Groups:
"Gamma"
"GammaBar"      Gamma(N)/(I,-I)
"Gamma1"        Gamma^1
"Gamma1Bar"
"Gamma0"        Gamma^0
"Gamma0Bar"
```



---

Comment by craigcitro created at 2008-02-08 07:03:47

Resolution: invalid


---

Comment by craigcitro created at 2008-02-08 07:03:47

Apparently this code is buggy.
