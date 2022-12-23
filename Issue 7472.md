# Issue 7472: Taylor polynomial in two variables does not work

Issue created by migration from https://trac.sagemath.org/ticket/7472

Original creator: robert.marik

Original creation time: 2009-11-16 09:26:26

Assignee: burcin

Keywords: taylor polynomial, derivative

make taylor(x*y^3,[x,y],[1,-1],4) work


---

Comment by robert.marik created at 2009-11-16 09:32:09

Changing status from new to needs_review.


---

Comment by robert.marik created at 2009-11-16 09:32:09

I hope it has been fixed by the attached patch.


---

Attachment


---

Comment by robert.marik created at 2009-11-16 09:45:31

this patch should be installed on the top of previous patch and improves documentation


---

Attachment


---

Comment by kcrisman created at 2009-11-16 15:08:38

I'm waiting for a build of 4.2.1... but in the meantime, is the new syntax (list for variables, list for numbers) more or less equivalent to other Sage functionality, or Mathematica/Maple syntax?  I honestly don't know, just asking.  It would be good to have compatibility, though.  For instance, plotting has the variable and range together (x,-5,5), so maybe [x,4] and [y,1] would be more appropriate? Looks like Mma allows for different "distance" for different variables, see [here](http://reference.wolfram.com/mathematica/ref/SeriesCoefficient.html)...  Just thinking out loud here.


---

Comment by robert.marik created at 2009-11-16 19:34:17

Replying to [comment:3 kcrisman]:
> I'm waiting for a build of 4.2.1... but in the meantime, is the new syntax (list for variables, list for numbers) more or less equivalent to other Sage functionality, or Mathematica/Maple syntax?  I honestly don't know, just asking.  It would be good to have compatibility, though.  For instance, plotting has the variable and range together (x,-5,5), so maybe [x,4] and [y,1] would be more appropriate? Looks like Mma allows for different "distance" for different variables, see [here](http://reference.wolfram.com/mathematica/ref/SeriesCoefficient.html)...  Just thinking out loud here.

Can be done easily, the expression is passed to Maxima and Maxima allows many possibilities how to use [taylor command](http://maxima.sourceforge.net/docs/manual/en/maxima_30.html#Item_003a-taylor). I wanted to do as minotr change as possible. I was thinking for example also on the possibility to use different order for different variable, but I do not know if there is a demand for this.

I do not know to much about habits in Sage notation, but I think that we evaluate expansion about point in n-dimensional space, so the coordinates should be together.


---

Comment by burcin created at 2009-11-23 14:08:56

FWIW, I also like the MMA notation better. It is more consistent with the interface to `integrate`, `plot`, etc. as kcrisman mentioned.


---

Comment by robert.marik created at 2009-11-23 19:26:00

OK. what about this, is it acceptable? 

```
sage: y=var('y');taylor(sin(x)*exp(y),(x,y),(0,1),4)
1/6*(y - 1)^3*x*e - 1/6*(y - 1)*x^3*e + 1/2*(y - 1)^2*x*e - 1/6*x^3*e + (y - 1)*x*e + x*e
sage: y=var('y');taylor(sin(x)*exp(y),(x,0,4),(y,1,4))
-1/144*((y - 1)^4*e + 4*(y - 1)^3*e + 12*(y - 1)^2*e + 24*(y - 1)*e + 24*e)*x^3 + 1/24*((y - 1)^4*e + 4*(y - 1)^3*e + 12*(y - 1)^2*e + 24*(y - 1)*e + 24*e)*x
sage: y=var('y');taylor(sin(x)*exp(y),x,0,4)
-1/6*x^3*e^y + x*e^y
sage: y=var('y');taylor(sin(x)*exp(y),(x,0,4))
-1/6*x^3*e^y + x*e^y
```

Note that in the first example the degree of  polynomial is 4 and in the second example the degree of polynomial is 7.
(Not yet documented in the experimental patch)


---

Comment by robert.marik created at 2009-11-23 19:28:31

apply on the top of the two other patches


---

Comment by robert.marik created at 2009-11-23 19:31:08

Changing status from needs_review to needs_info.


---

Attachment


---

Comment by robert.marik created at 2009-11-23 19:36:54

btw: it seems that taylor command in Maxima may return not only Taylor polynomial as in calculus books, but also truncated power expansion truncated at given power. I think that this could be something different from Taylor polynomial, so the name of the command is misleading. How is it in Mathematica and Maple? What should be in Sage?


---

Comment by robert.marik created at 2010-01-05 20:19:04

New patch, replaces all previous patches. Notation is more Sage like.


---

Attachment


---

Comment by robert.marik created at 2010-01-05 20:19:53

Changing status from needs_info to needs_review.


---

Comment by kcrisman created at 2010-01-13 21:29:30

I assume the idea of different degrees for different variables was lost?  That really doesn't matter to me, though.

What about this one, from the documentation?

```
sage: x,y=var('x y'); taylor(x*y^3,(x,1),(y,-1),4)  
(y + 1)^3*(x - 1) + (y + 1)^3 - 3*(y + 1)^2*(x - 1) - 3*(y + 1)^2 + 3*(y + 1)*(x - 1) - x + 3*y + 3 
```

Why doesn't it end this way?

```
-(x-1)+3*(y+1) -1
```

Maybe this is documented in Maxima?  It does seem odd, though, if I'm understanding what a multivariable Taylor polynomial is supposed to look like.

But overall this looks fine, assuming the Maxima computations are correct.  I am waiting for 4.3.alpha2 to build to see if there needs to be a rebase, but surely it would be trivial if so.


---

Comment by robert.marik created at 2010-01-13 22:11:22

Replying to [comment:10 kcrisman]:
> I assume the idea of different degrees for different variables was lost?  That really doesn't matter to me, though.

Yes, different degrees for different variables seem odd to me (from the point of view of pure caculcus) and I do not know, if there is a demand to keep this functionality.

> 
> What about this one, from the documentation?
> {{{
> sage: x,y=var('x y'); taylor(x*y^3,(x,1),(y,-1),4)  
> (y + 1)^3*(x - 1) + (y + 1)^3 - 3*(y + 1)^2*(x - 1) - 3*(y + 1)^2 + 3*(y + 1)*(x - 1) - x + 3*y + 3 
> }}}
> Why doesn't it end this way?
> {{{
> -(x-1)+3*(y+1) -1
> }}}
> Maybe this is documented in Maxima?  It does seem odd, though, if I'm understanding what a multivariable Taylor polynomial is supposed to look like.


Very good question :). Maxima in fact returns 

```
-(x-1)+3*(y+1) -1
```

and Sage changes it somehow into 

```
-x+3y+.... 
```

I do not know why, perhaps I should ask on sage-devel. The same problem is also in current Sage. The linear Taylor polynomial hal always slope intercept form f'(a)*x+q, but should be (and Maxima returns) point slope form  f'(a)*(x-a)+f(a)



```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: maxima("taylor(x^3,x,2,1)")
8+12*(x-2)
sage: maxima("taylor(x^3,x,2,1)").sage()
12*x - 16
sage: taylor(x^3,x,2,1)
12*x - 16
sage:
```

| Sage Version 4.3, Release Date: 2009-12-24                         |
| Type notebook() for the GUI, and license() for information.        |
> 
> But overall this looks fine, assuming the Maxima computations are correct.  I am waiting for 4.3.alpha2 to build to see if there needs to be a rebase, but surely it would be trivial if so.


---

Comment by robert.marik created at 2010-01-13 22:18:29

Replying to [comment:11 robert.marik]:
> I do not know why, perhaps I should ask on sage-devel. 

The [question](http://groups.google.cz/group/sage-devel/browse_thread/thread/81a2e114559cac8a) at sage-devel.


---

Comment by kcrisman created at 2010-01-15 05:56:06

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-01-15 05:56:06

I have made some trivial changes.  The new thing is a bug in some ways, but shouldn't keep us from merging this valuable functionality.


---

Comment by kcrisman created at 2010-01-15 05:56:39

Apply only this.


---

Comment by rlm created at 2010-01-18 22:57:36

Resolution: fixed


---

Attachment
