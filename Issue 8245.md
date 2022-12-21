# Issue 8245: tutorial: typo in section "Euler’s Method for Systems of Differential Equations"

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-02-12 03:51:50

Assignee: mvngu

CC:  kcrisman

From [sage-support](http://groups.google.com/group/sage-support/browse_frm/thread/437ae27f84e3a05):

```
In the section, "A Guided Tour"->"Basic Algebra and Calculus"-
>"Euler’s Method for Systems of Differential Equations", I found that

the answer of the example is z(1)≈0.75, which seems to be wrong.

The calculation is
------------------------------------------------------------------------
sage: t,x,y = PolynomialRing(RealField(10),3,"txy").gens()
sage: f = y; g = -x - y * t
sage: eulers_method_2x2(f,g, 0, 1, 0, 1/4, 1)
      t                x            h*f(t,x,y)                y
h*g(t,x,y)
      0                1                  0.00
0           -0.25
    1/4              1.0                -0.062
-0.25           -0.23
    1/2             0.94                 -0.12
-0.48           -0.17
    3/4             0.82                 -0.16
-0.66          -0.081
      1             0.65                 -0.18
-0.74           0.02
------------------------------------------------------------------------

So I think the right answer should be z(1)≈0.65 
```



---

Comment by jason created at 2010-05-26 15:19:39

Changing keywords from "" to "beginner".


---

Comment by ksmith created at 2012-01-11 21:27:38

Changing status from new to needs_review.


---

Attachment

I just made that one change making the 7 a 6.


---

Comment by ksmith created at 2012-01-11 22:04:31

Changing keywords from "beginner" to "beginner sd35.5".


---

Comment by kcrisman created at 2012-01-11 22:26:53

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2012-01-11 22:26:53

And the math turns out to be right.  The example itself is somewhat elliptically expressed, but this is fine.  

Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.


---

Comment by jdemeyer created at 2012-01-12 08:33:38

Replying to [comment:6 kcrisman]:
> Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.

Within Sage, ``foo`` is equivalent to `:math:`foo``.  In general ReST code, this is not true.


---

Comment by kcrisman created at 2012-01-12 14:16:21

> > Curious as to why we have both `:math:` and the backticks... but anyway, that would be a general overhaul of the tutorial.
> 
> Within Sage, ``foo`` is equivalent to `:math:`foo``.  In general ReST code, this is not true.
Ah, so it's historical in that sense.  Thanks for the clarification.


---

Comment by jdemeyer created at 2012-01-13 23:07:29

Resolution: fixed
