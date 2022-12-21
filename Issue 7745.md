# Issue 7745: Update Maxima to 5.20.1

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-12-21 02:07:46

Assignee: tbd

CC:  robert.marik burcin

Keywords: maxima

Maxima is now updated, and that will incorporate a number of our bugfixes as well as things we have reported, not to mention other improvements.   See [http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7](http://groups.google.com/group/sage-devel/browse_thread/thread/bbd2c801032392f7) for the announcement.


---

Comment by kcrisman created at 2009-12-22 04:40:19

Okay, I have a successful spkg.  BUT there are a number of things that will have to be fixed.  I have most of them (just doctests) but there are a couple bigger ones.  So this needs work (and a patch), but hopefully will be ready for 4.3.1, when that comes.

The spkg is at [http://sage.math.washington.edu/home/kcrisman/maxima-5.20.1.spkg](http://sage.math.washington.edu/home/kcrisman/maxima-5.20.1.spkg).

1. For some reason, a certain integration with infinity is not working properly.  Maybe Maxima regressed on it?  Or maybe we aren't parsing it properly?  

```
sage: integrate(t*cos(-theta*t),(t,-oo,oo))
```


2. Because of overall improvements to to_poly_solve/%solve, there are some annoying things we will have to fix.  Some are just in parsing the new %solve and some other things from its new capabilities, like

```
TypeError: unable to make sense of Maxima expression '[If(cos(pi*...!=0,[x=-...],union())]' in Sage
```

though this used to be nicely behaved from 

```
sage: solve(cos(x) * sin(x) == 1/2, x, to_poly_solve=True)
```

but unfortunately one of them is yet another hang in the algsys which doesn't automatically resolve (this is line 5948 in symbolic/expression.pyx):

```
sage: a = .004*(8*e^(-(300*t)) - 8*e^(-(1200*t)))*(720000*e^(-(300*t)) - 11520000*e^(-(1200*t))) +.004*(9600*e^(-(1200*t)) - 2400*e^(-(300*t)))^2
sage: a.solve(t, to_poly_solve=True)
<hang>
```

I'm contacting the author of that for info.


---

Comment by kcrisman created at 2009-12-22 04:40:19

Changing status from new to needs_work.


---

Comment by kcrisman created at 2009-12-22 16:32:58

> 1. For some reason, a certain integration with infinity is not working properly.  Maybe Maxima regressed on it?  Or maybe we aren't parsing it properly?  
> {{{
> sage: integrate(t*cos(-theta*t),(t,-oo,oo))
> }}}
> 

Update: this integral doesn't converge!  It was reported in #6816 but we never checked that it made sense, since Maxima did give an answer - zero, because the limit of the indefinite integral from -N to N is zero.  Maxima now (sensibly) doesn't give that any more, though it would be even better if it returned divergent; however, that would be a different ticket.

Still working on fixing the remaining doctest issues.


---

Comment by kcrisman created at 2009-12-22 21:16:07

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-12-22 21:16:07

Came up with fixes of one kind or another for all these things.  The real remaining issue is that there isn't a super-simple way to parse %if when it comes from to_poly_solve, so for now I am just leaving that alone.  As soon as anyone can think of a way to do this, please open a ticket and post a patch.   Otherwise this patch should make the new spkg work.


---

Comment by kcrisman created at 2009-12-22 21:16:34

Based on 4.3.alpha1


---

Attachment

See #6423 and #4142 for other bugs fixed by this spkg.


---

Comment by robert.marik created at 2009-12-23 00:35:51

Installs fine. Still running tests, but have the following (trivial) errors.

```
sage -t  "devel/sage/sage/interfaces/maxima.py"
**********************************************************************
File "/opt/sage-4.3.rc0/devel/sage/sage/interfaces/maxima.py", line 1204:
    sage: maxima.version()
Expected:
    '5.19.1'
Got:
    '5.20.1'
**********************************************************************
File "/opt/sage-4.3.rc0/devel/sage/sage/interfaces/maxima.py", line 2723:
    sage: maxima_version()
Expected:
    '5.19.1'
Got:
    '5.20.1'
**********************************************************************
```



---

Comment by kcrisman created at 2009-12-23 04:44:35

If those are the only ones you get, can you put a reviewer patch of those?  I always forget little things like that, and unfortunately the horsepower I have precludes running full tests if I ever want to get anything done.  I did get the one in rings/number_field, though.


---

Attachment

apply on the top of the previous patch and #6423 and #4142


---

Comment by robert.marik created at 2009-12-23 08:37:18

Changing status from needs_review to positive_review.


---

Comment by robert.marik created at 2009-12-23 08:37:18

Positive review! Tested on 4.3.rc0 and got only errors which have been reported on sage-devel and are not relevent to this ticket. Tested together with #6423 and #4142.

Positive review, thanks for upgrading.


---

Comment by kcrisman created at 2009-12-27 03:28:07

Note that if sage.math is still down, one can also get this at [http://boxen.math.washington.edu/home/kcrisman/maxima-5.20.1.spkg](http://boxen.math.washington.edu/home/kcrisman/maxima-5.20.1.spkg).


---

Comment by mhansen created at 2010-01-04 03:09:34

Resolution: fixed
