# Issue 5673: [with patch, needs review] Enhanced handling of elliptic curve twists

Issue created by migration from https://trac.sagemath.org/ticket/5673

Original creator: cremona

Original creation time: 2009-04-03 11:07:49

Assignee: was

CC:  wuthrich

Keywords: elliptic curve twist

The patch does the following related things:

    1. Implements in ell_generic functions is_quadratic_twist(), is_quartic_twist(), is_sextic_twist(), which detect twists between curves (returning the appropriate twisting paramenter)
    2. Deprecates the EllipticCurve(j) constructor, replacing it with EllipticCurve_from_j(j).  Over Q this gives the minimal twist, i.e. a curve with the correct j and minimal conductor.
    3. Rewrites the function minimal_quadratic_twist() introduced in #4667 to use the previous function, with extra work in case j=0, 1728 since we need the minimal __quadratic__ twist, not the minimal twist.

There is likely to be a necessary change to documentation (pages 38 and 39 of the tutorial) which have not yet been made.

The patch is based on 3.4.1.alpha0 + patches at #4667.
I have tested all files in sage/schemes/elliptic_curves.  There are two failures in sha_tate which I do not understand, so I am posting the patch anyway.



---

Attachment

apply to 3.4.1.alpha0 + #4667 patches


---

Attachment

apply after last patch


---

Attachment

replaces previous (fixes typo)


---

Comment by cremona created at 2009-04-06 10:42:09

robertwb,  Thanks for your patch (which needs a typo fixing: change 3 to 2 in line 113 or the test does not pass! -- I have attached a fixed patch).  I am happy to give your patch a positive review, but did you review mine?


---

Comment by robertwb created at 2009-04-12 09:44:41

It looks good (and works) for me.


---

Comment by robertwb created at 2009-04-12 09:48:28

The only suggestion I have is that it might be better to return `False` rather than `0` for non-twists.


---

Comment by cremona created at 2009-04-12 09:55:19

Replying to [comment:3 robertwb]:
> The only suggestion I have is that it might be better to return `False` rather than `0` for non-twists. 

I did that since I wanted the return type to be the same whatever.  But that stopped me doing the right thing in char. 2 when twists are additive (so a twist parameter of 0 means isomorphic).

It's the usual thing:  ideally I would want to return either (True, param) or False, but that is not allowed in Sage.  We could go for a more complicated function which by default just returns True/False, or if an optional parameter "return_parameter" is set to True returns a tuple either (True, param) or (False,).

One advantage of the current setup is that if you do not need the parameter you can use the output as if it were a bool with 0 converting to False.  I think.


---

Comment by robertwb created at 2009-04-12 10:20:33

Replying to [comment:4 cremona]:
> 
> I did that since I wanted the return type to be the same whatever.  But that stopped me doing the right thing in char. 2 when twists are additive (so a twist parameter of 0 means isomorphic).
> 
> It's the usual thing:  ideally I would want to return either (True, param) or False, but that is not allowed in Sage.  We could go for a more complicated function which by default just returns True/False, or if an optional parameter "return_parameter" is set to True returns a tuple either (True, param) or (False,).

One could do this, but then it gets really messy to use. 
 
> One advantage of the current setup is that if you do not need the parameter you can use the output as if it were a bool with 0 converting to False.  I think.

Yes, that will work. Actually, I think the most Pythonic thing to do here would perhaps be to return None, but I think the current behavior is fine as well.


---

Comment by mabshoff created at 2009-04-13 07:30:34

Unfortunately there are a few doctest failures in 

```
sage -t -long devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 1 doctests failed
sage -t -long devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 2 doctests failed
sage -t -long devel/sage/doc/en/tutorial/tour_advanced.rst # 2 doctests failed
sage -t -long devel/sage/doc/fr/tutorial/tour_advanced.rst # 2 doctests failed
```

One issue here is certainly that *make check* does not doctest the ReST documentation - see #5702 for the ticket for that problem which I intend to fix before 3.4.1 is done. 

To test *everything* run 

```
sage -tp 1 devel/sage
```

which is what I use :)

Cheers,

Michael


---

Comment by cremona created at 2009-04-13 16:50:44

I am about to start fixing the rst failures which should not take long.

NB the sha_tate failures were there when I posted this, and (via a message to sage-nt) I had hoped that Chris Wuthrich might have helped track that down.  I'll have a go myself now anyway.


---

Comment by cremona created at 2009-04-13 17:19:16

Apply after previous:  fixes rst doc failures in tutorial etc.


---

Attachment

Patch trac_5763_rst.patch fixes the rst failures.  Now for sha_tate....


---

Comment by cremona created at 2009-04-13 17:59:47

Apply after previous (fixes sha_tate doctest failure)


---

Attachment

OK, the problem was that Chris's original minimal_quadratic_twist() function gave back the same curve it it already had minimal conductor, while mine did not, since my function takes the curve with smallest label.  But the padic code could not cope with a non-trivial twist of the same conductor!  (The bad example was '300b2' for which "my" minimal twist is '300a2' which is its 5-twist.)

Solution:  if the minimal twist has the same conductor,  I just throw it away and use the original curve, as Chris's code used to do.

The patch trac_5673_review.patch fixes this.

Sorry I made two separate patches to fix the failures -- I was not sure I would succeed with both problems.


---

Comment by robertwb created at 2009-04-15 08:32:37

Looks good to me.


---

Comment by mabshoff created at 2009-04-16 12:06:09

Merged 

 * trac_5673_part_1_twist.patch
 * trac_5673_part_2-j-keyword.2.patch
 * trac_5673_part_3_rst.patch
 * trac_5673_part_4_review.patch

in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-16 12:06:09

Resolution: fixed
