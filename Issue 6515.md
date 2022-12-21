# Issue 6515: assume doesn't interact well with solve

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2009-07-12 04:22:28

Assignee: burcin

This has been brought up several times on the mailing lists. As a specific example 


```
sage: assume(x>0)
sage: solve([x^2-1],x)
[x == -1, x == 1]
```


At the very least, we could probably filter out the "solutions" that violate the assumptions. 



```
sage: [all(a.subs(s) for a in assumptions()) for s in solve(x^2-1==0, x)]
[False, True]
```



---

Comment by kcrisman created at 2009-09-30 18:40:20

It sounds like Maxima (intentionally?) doesn't use assumptions in solve, see for instance [http://www.math.utexas.edu/pipermail/maxima/2008/013152.html](http://www.math.utexas.edu/pipermail/maxima/2008/013152.html) and other similar threads.  The above solution seems reasonable.


---

Comment by kcrisman created at 2009-11-17 22:12:46

Update:  the solution above works well for single equations in one variable, but is tricky to implement for multiple equations (you can't subs x+y==3, for instance).  Also, one has to keep in mind how to check assumptions like 'x is Integer', which can't be subs'ed in.


---

Attachment


---

Comment by robertwb created at 2010-01-19 21:26:25

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-01-19 21:26:48

It doesn't catch everything, but is better than what we have now.


---

Attachment

minor documentation fixes


---

Comment by burcin created at 2010-02-03 16:53:44

The patch looks good and doctests pass. There is one minor problem, the line


```
sage: GenericDeclaration(x, 'rational').contradicts(y==pi)
```


is repeated several times in the doctest for `sage.symbolic.assumptions.GenericDeclaration.contradicts()`.

I attached a patch to change these lines and add an `INPUT` field to the docstring. Can you look over my patch and change the status to positive_review if you agree with the changes?


---

Comment by robertwb created at 2010-02-03 20:58:26

Thanks for looking at this. Nice catches, I approve of your changes.


---

Comment by robertwb created at 2010-02-03 20:58:26

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 15:54:22

For the record: Applying the patch to 4.3.2 + [a long queue](http://trac.sagemath.org/sage_trac/ticket/8186#comment:6) gives


```
applying 6515-solve-assume.patch
patching file sage/symbolic/expression.pyx
Hunk #2 succeeded at 5952 with fuzz 2 (offset 40 lines).
Hunk #3 succeeded at 6037 with fuzz 1 (offset 83 lines).
```


Please let us know (via sage-devel) about the best order in which to apply the symbolics and calculus patches.


---

Comment by mpatel created at 2010-02-10 19:33:17

The first patch is missing a Mercurial header and the ticket number.  I've applied a refreshed patch to 4.3.3.alpha0.


---

Comment by mpatel created at 2010-02-11 15:02:41

Resolution: fixed
