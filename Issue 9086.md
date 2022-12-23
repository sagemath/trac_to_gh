# Issue 9086: LaTeX representation of negative symbolic fractions broken

Issue created by migration from https://trac.sagemath.org/ticket/9086

Original creator: leif

Original creation time: 2010-05-29 18:44:54

Assignee: burcin

Keywords: symbolic fraction, sign, minus, latex

When the numerator of a (negative) symbolic expression happens to be `1` (and only then), the sign is dropped in its LaTeX representation (but not its string representation):


```
sage: latex(-1/x)
\frac{1}{x}
sage: latex(1/-x) 
\frac{1}{x}
```


Origin of the new doctest failure in `sage/graphs/generic_graphy.py`, introduced with Sage 4.4.3.alpha0.


---

Comment by burcin created at 2010-05-29 18:59:56

Changing keywords from "symbolic fraction, sign, minus, latex" to "symbolic fraction, sign, minus, latex, pynac".


---

Comment by burcin created at 2010-05-29 18:59:56

Thanks for tracking this down. This patch is the culprit:

http://pynac.sagemath.org/hg/rev/cbd65a7dcf6a


I will only be able to look at this after next weekend.


---

Attachment

apply to sage library


---

Attachment

apply to src/ repo in pynac spkg


---

Comment by was created at 2010-06-03 01:26:19

The patch to the pynac spkg is long, but is logically nearly trivial.  I just copied some code for printing a sign, which Burcin forgot.

The patch to the sage library is merely to test that this is fixed. 

William


---

Comment by was created at 2010-06-03 01:26:19

Changing status from new to needs_review.


---

Comment by was created at 2010-06-03 01:26:19

Changing priority from critical to blocker.


---

Comment by was created at 2010-06-03 01:28:26

New spkg here:

   http://sage.math.washington.edu/home/wstein/patches/pynac-0.2.0.p1.spkg


---

Comment by mhansen created at 2010-06-03 01:43:59

This looks good to me and fixes the issue.  There was a change for #9037 that didn't get included in the spkg merged so far in 4.4.3 so I've included it at 

http://sage.math.washington.edu/home/mhansen/pynac-0.2.0.p1.spkg

which should be used instead of the above link.


---

Comment by mhansen created at 2010-06-03 01:43:59

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-06-03 04:11:48

Mike, Can you give #9037 a positive review?


---

Comment by mhansen created at 2010-06-03 04:19:19

Positive review up at #9037.


---

Comment by was created at 2010-06-03 16:01:17

Resolution: fixed


---

Comment by damm created at 2010-06-21 20:25:20

Resolution changed from fixed to 


---

Comment by damm created at 2010-06-21 20:25:20

Changing status from closed to new.


---

Comment by damm created at 2010-06-21 20:44:32

Replying to [comment:10 damm]:
Sorry, i've changed the description and couldn't revert the change.

I think the fix didn't solve all problems:


```
sage: var('x y')
sage: latex(-x/y) 
\frac{x}{y}
```



---

Comment by leif created at 2010-06-22 16:39:05

Replying to [comment:12 damm]:
> I think the fix didn't solve all problems

Indeed. Despite the ticket's name, I think this second case should be addressed on another ticket, since this one had already been merged.


---

Comment by damm created at 2010-06-22 18:22:19

Done. http://trac.sagemath.org/sage_trac/ticket/9314


---

Comment by leif created at 2010-06-22 18:50:05

Resolution: fixed
