# Issue 5890: clean up schemes/elliptic_curves/ell_generic.py

Issue created by migration from https://trac.sagemath.org/ticket/5890

Original creator: AlexGhitza

Original creation time: 2009-04-24 23:43:37

Assignee: was

CC:  was cremona

Keywords: elliptic curve field

As noted at #5765, `ell_generic.py` has some functions that do not make sense over a general ring and should rather be moved down to `ell_field.py` or one of its descendants.

Note also William's comment from #5765: I think it would be nice to be able to implement the elliptic curve factorization method (ECM) without having to use this hack:


```
R = Zmod(N)
R.is_field = lambda: True
E = EllipticCurve(R, [-1,0])
```




---

Comment by AlexGhitza created at 2009-04-25 05:07:29

For the record, to understand William's comment have a look at line 572 of `tests/book_stein_ent.py`, where he implements ECM and uses this hack.

However, his function works for me in 3.4.1, so I think it's already been fixed.


---

Comment by AlexGhitza created at 2009-04-25 05:08:18

Replying to [comment:1 AlexGhitza]:
> For the record, to understand William's comment have a look at line 572 of `tests/book_stein_ent.py`, where he implements ECM and uses this hack.
> 
> However, his function works for me in 3.4.1, so I think it's already been fixed.
> 
 I mean of course that it works for me in 3.4.1 without the hackish line that fools Sage into thinking that R is a field.


---

Comment by AlexGhitza created at 2009-04-25 05:15:46

The attached patch does some cleaning up, and it depends on #5765.

It moves all the twists-related methods from `ell_generic.py` to `ell_field.py`, as well as the alias `base_field = base_ring`.

It also makes `change_ring` into an alias for `base_extend`, since the two have the exact same functionality and equivalent code.

Lastly, the standalone function `Hasse_bounds` is moved from `ell_generic.py` to `schemes/plane_curves/projective_curve.py`, which is a more natural place for it.

There are more things to do, but they are issues with the generic code for curves rather than the code for elliptic curves, so I think they should be fixed in `schemes/plane_curves` instead.  I'll be looking into that soon.


---

Comment by AlexGhitza created at 2009-04-25 05:15:46

Changing assignee from was to AlexGhitza.


---

Comment by AlexGhitza created at 2009-04-25 05:15:46

Changing status from new to assigned.


---

Comment by AlexGhitza created at 2009-04-25 05:16:24

depends on the latest patch at #5765


---

Attachment


---

Comment by cremona created at 2009-04-29 11:39:46

Review: first of all, this is just moving code around, all perfectly sensible (lots of stuff moved down from ell_generic to ell_field, and Hasse_bound function moved off to plane curves (where I should have put it in the first place).

I applied first 12097.patch (from #5919) then trac_5765-rebased.patch (from #5765) and then trac_5890.patch (from here), all successfully.

Doctests in schemes/plane_curves and schemes/elliptic_curves pass.  I will give this a positive review, despite the following, which will make it harder to do EC factoring (but the fault lies not in the patch here, rather in moving the test for a point lying on a curve which is now more sophisticated to harder to fool.... but that is not for this ticket to sort out.

The example

```
N = 1001
R = Zmod(N)
R.is_field = lambda: True
E = EllipticCurve(R, [-1,0])
```

works but you cannot construct a point in the curve (e.g. E(0,0)) since this happens:

```
sage: P = E(0,0)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/masgaj/.sage/temp/host_56_150/32116/_home_masgaj__sage_init_sage_0.py in <module>()

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_generic.pyc in __call__(self, *args, **kwds)
    609                 args = tuple(args[0])
    610
--> 611         return plane_curve.ProjectiveCurve_generic.__call__(self, *args, **kwds)
    612
    613     def _reduce_point(self, R, p):

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in __call__(self, *args)
    196                 else:
    197                     return self.point(S)
--> 198         return self.point(args)
    199
    200     def point_homset(self, S = None):

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/scheme.pyc in point(self, v, check)
    230
    231     def point(self, v, check=True):
--> 232         return self._point_class(self, v, check=check)
    233
    234     def _point_class(self):

/local/jec/sage-3.4.2.alpha0/local/lib/python2.5/site-packages/sage/schemes/generic/morphism.pyc in __init__(self, X, v, check)
    415     """
    416     def __init__(self, X, v, check=True):
--> 417         raise NotImplementedError
    418
    419

NotImplementedError:
```



---

Comment by mabshoff created at 2009-04-30 00:54:18

Merged in Sage 3.4.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-30 00:54:18

Resolution: fixed
