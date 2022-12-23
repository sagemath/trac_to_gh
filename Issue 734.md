# Issue 734: combinatorics problems on fedora core 7 with sage-2.8.5

Issue created by migration from https://trac.sagemath.org/ticket/734

Original creator: was

Original creation time: 2007-09-21 21:09:48

Assignee: was

CC:  sage-combinat


```
> >
> > NOTE: Since this is such a major release, there will likely be problems
> > and a 2.8.5.1 release shortly to fix them.  Please report!
> >
> 
> Builds on Fedora 7,
> 
> ----------------------------------------------------------------------
> The following tests failed:
> 
> 
>          sage -t  devel/sage-main/sage/combinat/skew_tableau.py
>          sage -t  devel/sage-main/sage/combinat/ribbon.py
> Total time for all tests: 1838.3 seconds
> [jaap@paix sage-2.8.5]$

This is from mike Hansen's new combinatorics code, I think.
I *am* able to replicate this on my Fedora Core machine,
and on none of my other 10 or so machines.  Mike, any
comments -- I can give you an account on the machine if
necessary.

 -- William
```



---

Comment by mhansen created at 2007-09-21 21:36:26

Changing assignee from was to mhansen.


---

Attachment


---

Comment by mhansen created at 2007-09-23 19:46:51

Changing status from new to assigned.


---

Comment by was created at 2007-09-23 21:32:28

Resolution: fixed


---

Comment by was created at 2007-09-23 21:32:28

The problem turned out to be comparing Integer and None. 

I had to fix another related problem: 
    http://sage.math.washington.edu/tmp/fc734.hg
