# Issue 6084: Improved p-adic polynomials

Issue created by migration from https://trac.sagemath.org/ticket/6084

Original creator: roed

Original creation time: 2009-05-19 08:23:45

Assignee: tbd

CC:  niles kedlaya jpflori

A reimplementation of p-adic polynomials in Cython with many different ways for handling precision.  Needed for more generic p-adic rings and fields and factoring of p-adic polynomials


---

Comment by roed created at 2009-05-19 08:26:04

Changing component from algebra to padics.


---

Comment by roed created at 2009-05-19 08:26:04

Changing assignee from tbd to roed.


---

Comment by roed created at 2009-05-19 08:26:04

Changing type from defect to enhancement.


---

Comment by roed created at 2009-05-19 09:42:24

A patch of Craig that's applied before padicpoly.


---

Attachment


---

Attachment

A patch of Craig's needed for the rest to apply cleanly


---

Attachment

Fixes aimed at ticket 5075


---

Attachment

Changes outside sage.rings.padics and sage.rings.polynomial.padics


---

Attachment

Changes in sage.rings.padics


---

Attachment

New files in sage.rings.polynomial.padics


---

Comment by roed created at 2009-06-08 18:34:10

Apply after other patches


---

Attachment


---

Comment by AlexGhitza created at 2009-10-24 11:24:44

David, is this ready for review now?


---

Comment by mhansen created at 2009-12-07 08:22:33

Ping.  Any updates on this?


---

Comment by roed created at 2009-12-07 19:25:57

Yep.  I started working on this again a week and a half ago.  I'm currently fixing bugs and bringing it up to 100% doctests.  I hope to have a version ready to review soon.


---

Attachment

Should apply against 4.3.2 and build; there are still doctest failures.


---

Comment by wuthrich created at 2010-07-28 12:42:12

Any news on this ? (Iam asking becasue of #8198 and #4656.)


---

Comment by niles created at 2010-08-04 01:58:24

I eventually found this ticket after a bug hunt related to #9457.  That patch changes power series comparison to use `padded_list` instead of `list`; I noticed that this patch (6084_ALL.patch) also makes changes to power series comparison, so maybe it makes sense to incorporate #9457 into this patch?


---

Comment by wuthrich created at 2011-01-27 13:25:43

It is such a shame that this has frozen a year ago. There is a lot of good work here and I am sure it would solve quite a few problems in other tickets.


---

Comment by roed created at 2011-01-27 13:43:19

I know.  I was just thinking the same thing after seeing the discussion at #10698.  It's nice to know that p-adic polynomials are getting used, but also sad that this bug is causing so much problems.

Unfortunately, my thesis is due in a little over a month, so I cannot work on this right now.  I know it's difficult to pick up someone else's work, but the code is mostly done; it mainly needs doctests and fixes to any problems that they reveal.  If someone wants to take this on, let me know: I can make sure you have the latest patches and let you know what needs doing.


---

Comment by roed created at 2011-04-07 14:49:18

I'm getting started on this.  Let me know if you want to help review it once I get it back in shape.


---

Comment by niles created at 2011-04-07 15:00:39

Replying to [comment:11 roed]:
> I'm getting started on this.  

Great!

> Let me know if you want to help review it once I get it back in shape.

Indeed, I'd be happy to help :)


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Attachment


---

Comment by roed created at 2011-06-10 15:11:07

Alright.  Let's try this again.

Apply 6084_1.patch, 6084_2.patch, 6084_3.patch, 6084_4.patch, 6084_5.patch, 6084_6.patch, 6084_7.patch, 6084_8.patch, 6084_9.patch, 6084_10.patch.  I'm happy to merge them, but I wanted them to be viewable on trac.  

Not all doctests work yet, but I wanted to get this posted so that people could play with it and give me feedback.  I'd like to succeed this time in getting it into Sage.


---

Comment by niles created at 2011-06-10 20:21:29

Replying to [comment:13 roed]:

Great!  The patches do all apply and build on 4.7, but there are errors when starting sage:


```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/niles/sage/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

...

/home/niles/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial._repr_ (sage/rings/polynomial/polynomial_element.c:14010)()

/home/niles/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial._repr (sage/rings/polynomial/polynomial_element.c:13276)()

/home/niles/sage/local/lib/python2.6/site-packages/sage/rings/polynomial/polynomial_element.so in sage.rings.polynomial.polynomial_element.Polynomial._top_nonzero_power (sage/rings/polynomial/polynomial_element.c:17586)()

TypeError: degree() takes no arguments (1 given)
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
sage:
```


Also, there are a number of failures on 4.7.1.alpha2 so this will have to be rebased.


---

Comment by niles created at 2011-06-10 20:25:08

Changing status from new to needs_info.


---

Comment by niles created at 2011-06-10 20:25:08

I think to get this reviewed, some additional organization will be useful -- here's what I would suggest:

 * Give us an introductory description of what this patch accomplishes: What are the "many different ways of handling precision"?  Why was this needed?  What had to be done?  What are the main ideas of your implementation?

 * Presumably the patch has been broken into some conceptual pieces -- it would be useful if you could explain what these are, so that they can be reviewed somewhat independently if possible.

 * I would suggest versioning each separate patch piece (since they will surely need to be updated), so a naming scheme like `6084_1.n.patch`.

 * An always-up-to-date `6084_ALL.patch` will make for easy downloading and applying (but viewing the separate pieces on trac is very useful for me)

 * Any other ways you can think to break the review down into distinct pieces will be much appreciated


---

Comment by roed created at 2011-06-10 22:12:30

I will build a copy of 4.7.1.alpha2 overnight and port the patches to there.

The key idea of this patch is that a polynomial over Zp should not be stored as a list of coefficients, but instead as an element of ZZ[x], together with some sort of precision object that records the precision to which each coefficient is known.  There are two main benefits of this approach:
1. One can use fast algorithms for things like polynomial multiplication, rather than being forced back on naive multiplication due to a desire to preserve precision.  For example, Karatsuba multiplication uses the identity

(f<sub>0</sub> + x<sup>n</sup> f<sub>1</sub>) (g<sub>0</sub> + x<sup>n</sup> g<sub>1</sub>) = (f<sub>0</sub> g<sub>0</sub>) + (f<sub>1</sub> g<sub>1</sub>) x<sup>2n</sup> + ((f<sub>0</sub> + f<sub>1</sub>)(g<sub>0</sub> + g<sub>1</sub>) - f<sub>0</sub> g<sub>0</sub> - f<sub>1</sub> g<sub>1</sub>)x<sup>n</sup>

This can lose precision over the naive definition since there are more additions than needed.  But if one computes an approximation over ZZ and then determines precision separately, one can use Karatsuba or FFT algorithms at will.
1. If one wants to use different methods for tracking precision (see below), the separation makes the implementation more modular and thus easier to implement and maintain.

These patches implement two kinds of polynomials: an anchored polynomial type which stores an approximation (in ZZ[x] for example) and a precision object, and a floating polynomial type which stores a common power of p for all the coefficients together with an anchored polynomial (thus allowing polynomials over Qp).  

There are three kinds of precision defined so far:
* Flat precision.  The precision of every entry is just a constant value n.  This is certainly the fastest option, and frequently is perfectly adequate.
* Jagged precision.  Each coefficient has its own precision, subject only to the precision cap of the base ring.  This is mainly for backward compatibility, but might also be useful in generating functions (maybe?).
* Newton precision.  The Newton polygon of the polynomial and of the precision are stored.  This is the default precision type, since it provides a compromise between the previous two types, and having precision above the Newton polygon is useless for evaluating the polynomial anyway.

I'll write more about the contents of the individual patches and some more of the contents tomorrow morning.


---

Attachment

Replaces 6084_1.patch


---

Attachment

Replaces 6084_2.patch


---

Comment by roed created at 2011-06-12 20:29:06

Replaces 6084_5.patch


---

Attachment

Replaces 6084_6.patch


---

Attachment

Replaces 6084_7.patch


---

Attachment

Replaces 6084_8.patch


---

Comment by roed created at 2011-06-12 20:30:46

Replaces 6084_9.patch


---

Attachment

Replaces 6084_10.patch


---

Attachment

Collects all patches in the .2 revision.  Only apply this patch


---

Attachment

Should apply against 4.7.1.alpha4.  One can apply only 6084_ALL.2.patch, with the rest existing so that one can view code on trac.

The breakdown into patches is not the best, but here's a description.
Patch 1: Some changes to polynomials and power series to allow leading terms that are indistinguishable from 0.
Patch 2: Original changes outside both sage.rings.padics and sage.rings.polynomial.
Patch 3: Changes to sage.rings.padics
Patch 4: The new code in sage.rings.polynomial
Patch 5: A small change to polynomial_ring_constructor to allow arbitrary kwds to be passed on to polynomial ring __init__ methods.
Patch 6: First update, bugfixes
Patch 7: Second update, bugfixes
Patch 8: Third update, bugfixes
Patch 9: Fourth update, bugfixes
Patch 10: Removing an ill-advised attempt to use fmpz_montgomery types to speed up computations for polynomials over Zp with p odd.

If reviewers would like, I can split up the ALL patch into more reasonable chunks.  Suggestions are welcome.  Bugs still remain, which I will continue to hunt down.


---

Comment by kedlaya created at 2011-06-18 17:22:38

It would be even better to split the patch over several tickets, which could then be reviewed, merged, and closed separately (this may also help with bug tracking). For instance, Patch 1 could perhaps go in independently, and would probably resolve a number of other outstanding tickets which point back here (e.g., with polynomials over power series rings).


---

Comment by saraedum created at 2012-07-10 11:00:46

What is the status of these patches? The ticket still says "needs work" but it seems you split the patch up as requested. So should it be "needs review"?

Can this be made into several tickets somehow? It's quite frightening to see a patch that says "HTML preview not available, since the file size exceeds 262144 bytes." ;) Anyway, I could try to split it up, just give me some hints where to start.

Is this independent of #12555? Which one should be reviewed/merged first?


---

Comment by roed created at 2012-07-10 19:37:41

I've kinda given up on this ticket and am attempting to make the changes in smaller pieces elsewhere.  Feel free to raid it for changes.  #12555 is a much higher priority for me: help on that would be much appreciated!  Once the templating code there gets in, I think the changes in this ticket will be easier to make.


---

Comment by saraedum created at 2015-08-13 18:24:28

Changing status from needs_info to positive_review.


---

Comment by saraedum created at 2015-08-13 18:24:28

I believe this ticket can be closed. Some of the patches here are still useful but it is clear that this can never be merged as is.


---

Comment by vbraun created at 2015-08-14 07:34:21

Resolution: invalid
