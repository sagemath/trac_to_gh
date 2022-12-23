# Issue 2109: the maxima interface doesn't recognize a syntax error (and then hangs)

Issue created by migration from https://trac.sagemath.org/ticket/2109

Original creator: mhansen

Original creation time: 2008-02-08 10:44:29

Assignee: was


```
sage: maxima.eval('sage0: x == x;')
display2d : false; 
(%o2) false

0; 
(%o4) 0
```


It hangs there.  If doing the same thing in Maxima, we get the following results:


```
(%i1) sage0: x==x;
Incorrect syntax: = is not a prefix operator
sage0: x==
        ^

```



---

Comment by AlexGhitza created at 2009-08-24 09:37:46

Here is what happens in sage-4.1.1:


```
sage: maxima.eval('sage0: x == x;')
'x'
```



---

Comment by kcrisman created at 2009-12-17 21:06:03

So at least it doesn't hang anymore.  I will change the summary.


---

Attachment


---

Comment by mhansen created at 2010-01-17 04:16:42

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-01-18 15:53:04

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-18 15:53:04

Passes relevant tests, catches several different types of incorrect input errors, and helped me learn a little more about pexpect.  Positive review, and thanks! 

Unfortunately, it doesn't catch when someone does something like this, but I'm not sure this is really an "error", as it's intended that Maxima can handle this sort of thing... yet it could easily come as a result of an error by the user.  Oh well.

```
integrate(f,
x,1,
2)
```



---

Comment by rlm created at 2010-01-19 00:41:20

Resolution: fixed
