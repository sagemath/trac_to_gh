# Issue 9307: delete GHMM standard spkg from Sage

Issue created by migration from https://trac.sagemath.org/ticket/9307

Original creator: was

Original creation time: 2010-06-22 13:18:21

Assignee: GeorgSWeber

CC:  rlm




---

Comment by mpatel created at 2010-06-29 21:27:20

I think we can resolve this as "fixed."  For 4.4.4, 4.5.alpha0, and 4.5.alpha1, I get

```sh
$ cd SAGE_ROOT
$ grep -i ghmm spkg/install spkg/standard/deps
$ find | grep -i ghmm
$
```



---

Comment by rlm created at 2010-07-01 17:10:56

William did this a while ago without closing the ticket. We should figure out what the right milestone is.


---

Comment by rlm created at 2010-07-01 17:10:56

Resolution: fixed
