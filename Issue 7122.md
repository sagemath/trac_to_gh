# Issue 7122: plot real part and imaginary part of function sqrt.

Issue created by migration from https://trac.sagemath.org/ticket/7122

Original creator: fmaltey

Original creation time: 2009-10-05 15:15:11

Assignee: was

I try to plot a half-circle with the 


```
var('m')
parametric_plot ([real(m+sqrt(1-m^2)), imaginary(m+sqrt(1-m^2))],m,-1,1)
}}} 

and get a severe error.

Theses plots are right :
{{{
plot([sqrt(m2+1)],m,0,6)
plot(real (sqrt(m2+1)),m,0,6)
}}}

But this one with AND real(...) or imaginary(...) AND list AND sqrt(...)  fails :

{{{
plot([real (sqrt(m2+1))],m,0,6)
}}}

On devel-support kcrisman proposes :


After looking at the traceback about an extra argument, I have a
sneaky suspicion this is because sqrt takes an extra keyword prec,
which perhaps is getting caught up in fast_float somehow.  What's
interesting is that the problem also only shows up for a list, so
again fast_float([]) is what's getting concerned.  Those who know how fast_float and the expression trees work will hopefully check this out as they get an opportunity.



---

Comment by mhansen created at 2009-10-05 17:27:30

I've attached a patch which fixes the error you get.  However, I don't think that's the right equation to draw a half circle since sqrt(1-m^2) is always going to be real for -1 <= m <= 1.


---

Attachment


---

Comment by kcrisman created at 2009-10-20 06:49:17

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-10-20 06:49:17

Looks good, passes all the tests I can think of. 

If it's significant enough that 

```
sage: plot([real (sqrt(m^2-1))],m,0,6)
```

now works, maybe there should be a doctest in plot/plot.py?

Otherwise positive review.


---

Comment by mhansen created at 2009-10-21 04:04:19

Resolution: fixed
