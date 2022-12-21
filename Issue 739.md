# Issue 739: hang doctesting const.tex

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-09-22 22:02:03

Assignee: failure

Many people (John Cremona and David Harvey at least) had the following problem:


```
I upgraded to 2.8.5 ok (kubuntu 7.04, kernel 2.6.20-16-generic, gcc
version 4.1.2).

sage --testall hangs at this point:
Testing SAGE constructions guide
sage -t  const.tex

and "ps -ux" shows that all the processes are in swap (S status).
Also Ctrl-C did not kill it, I am having to kill all the processes one
by one.

John
```



---

Comment by was created at 2007-09-23 21:41:56

It turns out that "hangs forever" means takes longer than 30 seconds for many people :-). 
This actually works fine -- it's just that const.tex is really long (nearly a minute!).


---

Comment by was created at 2007-09-23 21:41:56

Resolution: invalid
