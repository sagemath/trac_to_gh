# Issue 6183: Quaternion algebra latexification

Issue created by migration from https://trac.sagemath.org/ticket/6183

Original creator: robertwb

Original creation time: 2009-06-02 07:28:18

Assignee: tbd

Quaternion algebra elements don't have a nice latexification. This should be easy for someone to add. 


---

Comment by AlexGhitza created at 2009-07-11 13:12:02

Changing assignee from tbd to AlexGhitza.


---

Comment by AlexGhitza created at 2009-07-11 13:12:02

Changing keywords from "" to "quaternion latex".


---

Comment by AlexGhitza created at 2009-07-11 13:12:02

Changing type from defect to enhancement.


---

Comment by AlexGhitza created at 2009-07-11 13:12:02

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-07-11 13:12:02

See attached patch.


---

Attachment


---

Comment by davidloeffler created at 2009-07-13 19:16:53


```
sage: B.<i, j, k> = QuaternionAlgebra(RR, -1, -1) 
sage: latex(i + 1 - k) 
1.00000000000000 + i - k
```


With all due respect, this is hideous :-) I know you only did it for consistency with the `repr` method, of course; but what would you say to the suggestion that we change `repr`, and `latex`, so they return something like `1.00000000000000 + 1.00000000000000*i - 1.00000000000000*k`? This is consistent with our conventions for other algebras over inexact rings (e.g. polynomials and power series).


---

Comment by AlexGhitza created at 2009-07-14 07:05:59

Point taken.

I'm changing this to "needs work".  I'll try to find an elegant way of using the printing code for polynomials so that things are consistent (and stay that way).


---

Comment by AlexGhitza created at 2009-07-14 07:41:11

Actually, note that printing of polynomials is *not* consistent, in that multivariable polynomials have "hideous" printing, whereas univariate ones have "pretty" printing:


```
sage: R.<i, j, k> = RR[]
sage: i + 1 - k
i - k + 1.00000000000000
sage: R.<i> = RR[[]]
sage: i+1
1.00000000000000 + 1.00000000000000*i
```


So this needs fixing.
