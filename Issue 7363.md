# Issue 7363: print symbolic fractions more naturally: print 2/(x+2) instead of 2 (1/(x+2))

Issue created by migration from https://trac.sagemath.org/ticket/7363

Original creator: jason

Original creation time: 2009-10-31 14:44:49

Assignee: burcin

CC:  burcin

See http://groups.google.com/group/sage-devel/browse_frm/thread/9d58693356e11947


---

Comment by jason created at 2009-10-31 14:45:24

Changing priority from major to minor.


---

Comment by burcin created at 2010-01-17 07:20:27

add doctests


---

Attachment

Next pynac release will have a patch for this. attachment:trac_7363-mul_coeff.patch fixes some doctests and adds a couple more.


---

Comment by burcin created at 2010-01-17 07:22:12

Changing keywords from "" to "pynac".


---

Comment by burcin created at 2010-01-17 07:22:12

Changing status from new to needs_work.


---

Comment by burcin created at 2010-01-19 22:50:03

New pynac package available here:

http://sage.math.washington.edu/home/burcin/pynac/pynac-0.1.11.spkg

The package contains fixes for #7822, #6961, #7876, #7363, #6465 and #6559. Apart from this ticket, #7876 contains printing changes. Doctests should be run with the patch from that ticket applied as well.


---

Comment by burcin created at 2010-01-19 22:50:03

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2010-01-28 21:17:03

This seems to work well, but I do not know enough C++ to review http://pynac.sagemath.org/hg/rev/5ea74f619c01, unfortunately.  Partial positive review?


---

Comment by rossk created at 2010-02-15 14:06:14

Changing status from needs_review to positive_review.


---

Comment by rossk created at 2010-02-15 14:06:14

Changing keywords from "pynac" to "pynac, symbolic, print".


---

Comment by rossk created at 2010-02-15 14:06:14

Im also not qualified to review the C++ code but the (representative) examples below indicate the code satisfies the objectives so Im giving it a positive review (which someone can reverse if they discover a counterexample)



```
# Note: division is left associative: 12/3/4 = (12/3)/4
sage: 12/3/4 
1

sage: var('x y z')
(x, y, z)

sage: 2/(x+1) # the motivating example
2/(x + 1)

sage: 1/(2*y)
1/2/y

sage: 1/(1/2*y)
2/y

sage: x/2/y
1/2*x/y

sage: .5*x/y
0.500000000000000*x/y

sage: .5/x/y
0.500000000000000/(x*y)

sage: 1/2/x/y
1/2/(x*y)

sage: 1/x/2
1/2/x
```



---

Comment by mvngu created at 2010-02-18 21:43:31

Resolution: fixed
