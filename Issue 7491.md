# Issue 7491: solve(x==x,x) fails

Issue created by migration from https://trac.sagemath.org/ticket/7491

Original creator: robert.marik

Original creation time: 2009-11-19 07:36:11

Assignee: burcin


```
sage: solve([x==x],x)
```

gives an exception.

Maxima says this:

```
$ maxima -q
(%i1) solve([x=x],x);
(%o1)                                 all
(%i2) 
```


There is a short [discussion](http://groups.google.cz/group/sage-devel/browse_thread/thread/ce3a256a9102c7fc) about this topic. 


---

Comment by robert.marik created at 2009-11-19 08:00:39

Changing status from new to needs_review.


---

Attachment

attached patch does the following

```
[marik@um-bc107 /opt/sage]$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: solve
sage: y=var('y');solve(SR(0),y,solution_dict=True)
{y: r1}
sage: y=var('y');solve(SR(0),y,solution_dict=True,multiplicities=True)
({y: r1}, [])
sage: solve(x==x,x,multiplicities=True)
([x == r1], [])
| Sage Version 4.2.1, Release Date: 2009-11-14                       |
| Type notebook() for the GUI, and license() for information.        |
```


All tests in symbolic and calculus passed.


---

Comment by kcrisman created at 2009-12-04 17:02:39

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-12-04 17:02:39

Positive review.  I'm not sure what the changes in relation.py bring to the game, but they don't hurt either.


---

Comment by mhansen created at 2009-12-14 16:45:44

Resolution: fixed
