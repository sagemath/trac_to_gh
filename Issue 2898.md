# Issue 2898: Coerce float and RDF to Integers

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-12 16:08:08

Assignee: somebody


```
>  That said, William, is there a reason why this doesn't work?  This is
> >  what is necessitating the two type conversions above.
> >
> >  sage: Integer(float(2))
> >
> > ---------------------------------------------------------------------------
> >  <type 'exceptions.TypeError'>             Traceback (most recent call last)
> >
> >  /home/grout/<ipython console> in <module>()
> >
> >  /home/grout/integer.pyx in sage.rings.integer.Integer.__init__()
> >
> >  <type 'exceptions.TypeError'>: unable to coerce element to an integer
> >
> >
> >  sage: Integer(RDF(2))
> >
> > ---------------------------------------------------------------------------
> >  <type 'exceptions.TypeError'>             Traceback (most recent call last)
> >
> >  /home/grout/<ipython console> in <module>()
> >
> >  /home/grout/integer.pyx in sage.rings.integer.Integer.__init__()
> >
> >  <type 'exceptions.TypeError'>: unable to coerce element to an integer
> >
> >
> >  I guess I would think it was a design decision to not convert floating
> >  points to ints automatically.  However, the following does work:
> >
> >  sage: Integer(RR(2))
> >  2
> >
> >
> >  This seems inconsistent.

Yep.  I think it's just a NotImplementedError.  Please implement it
and post a patch.  Make sure that it only succeeds if

   Integer(k(a)) == a

and otherwise fails.  I.e., Integer(k(a)) should *not* truncate k(a).

William
```




---

Comment by jason created at 2008-04-12 16:09:44

Changing component from basic arithmetic to coercion.


---

Comment by jason created at 2008-04-12 16:09:44

Changing assignee from somebody to robertwb.


---

Comment by jason created at 2008-04-13 04:40:32

I've put up a preliminary patch at:

http://sage.math.washington.edu/home/jason/trac-2898-coerce-to-Int.patch

This is undergoing doctesting in alpha3 right now.


---

Comment by mabshoff created at 2008-06-09 07:01:21

Jason, 

any update on this patch? I corrected the subject to be a little clearer.

Cheers,

Michael


---

Comment by craigcitro created at 2008-06-20 04:47:46

Changing keywords from "" to "editor_mhansen".


---

Comment by jason created at 2008-06-24 00:27:50

I believe the patch is ready to be doctested (which is where my time gave out before).


---

Comment by jason created at 2008-06-24 00:29:39

This is supposed to fix #2899, so it would be good to check if the other issue is resolved as well.


---

Attachment


---

Comment by ncalexan created at 2008-08-14 00:34:51

The patch I posted is basically the same as jgrout's; it sat in my tree for a long time without any problems.

It looks good to me, but let's get a second opinion.


---

Comment by cwitty created at 2008-08-23 21:15:13

Unfortunately, this patch gives:

```
sage: 1.0r/8
1/8
```

which is IMHO unacceptable.

I think that the bug is actually in the coercion framework, rather than in this patch; so I've opened a new issue for that bug at #3938.  Once it is fixed, then we can revisit this patch.


---

Comment by robertwb created at 2008-08-23 22:36:43

I agree with cwitty, I'll be taking a look at #3938.


---

Comment by robertwb created at 2008-08-30 19:39:10

#3938 has been resolved.


---

Comment by mabshoff created at 2008-08-30 23:03:54

Replying to [comment:11 robertwb]:
> #3938 has been resolved. 

Hi Robert,

so if I understand you correctly this patch here should not be merged since it fixes a symptom and not the root cause.

Cheers,

Michael


---

Comment by robertwb created at 2008-08-31 03:27:46

This patch should be applied. The problem is that it exposed a bug that was worse than what it fixed. Now the bug has been resolved, they both should be applied.


---

Comment by mhansen created at 2008-09-19 00:36:21

Looks good to me.  This depends on #3938.


---

Comment by mabshoff created at 2008-09-19 02:56:21

The patch no longer applies cleanly and also causes a doctest failure (sorry, forgot the details and no longer have the logs ;)). The rebase should be easy since hunk 2 of integer.pyx is affected and it is only a doctest issue.

Cheers,

Michael


---

Attachment


---

Comment by cwitty created at 2009-01-25 20:22:59

I've attached two patches, 2898-jgrout-coerce-to-integer-3.3.alpha2.patch and trac2898-fixups.patch.  With #3938 plus these two patches over 3.3.alpha2, all doctests pass (except those that were broken in base 3.3.alpha2).

I'm giving a positive review for 2898-jgrout-coerce-to-integer-3.3.alpha2.patch; somebody else should review trac2898-fixups.patch.


---

Comment by jason created at 2009-01-28 18:09:23

I get an error applying the fixups patch:


```
applying trac2898-fixups.patch?format=raw
patching file sage/rings/real_mpfr.pyx
Hunk #1 FAILED at 396
1 out of 1 hunks FAILED -- saving rejects to file sage/rings/real_mpfr.pyx.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
Errors during apply, please fix and refresh trac2898-fixups.patch?format=raw
```



---

Comment by jason created at 2009-01-28 18:13:09

I'm confused by the real_mpfr.pyx part of the fixups patch.  I can't find the misspelling "cannonical" anywhere in that directory in sage-3.3alpha2.


---

Comment by jason created at 2009-01-28 19:10:17

The real_mpfr.pyx part of the fixups patch should be deleted-mabshoff corrected the typo when merging #3938.

Doctests pass in all files touched by the fixups patch.  I'd like someone else to look at the code it touches in free_modules.pyx and verify the changes there.  Other than that, this looks good to me.


---

Attachment

We didn't get this in quite soon enough; in alpha5, this gives failing doctests in symbolic/expression.pyx.  (The following is hand-edited to remove boring bits of the backtraces.)

```
sage -t  "devel/sage-mqtmp/sage/symbolic/expression.pyx"    
**********************************************************************
File "/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx", line 2169:
    sage: S(10.0r).gamma()
Expected:
    362880.000000000
Got:
    362880
**********************************************************************
File "/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx", line 2180:
    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)
Exception raised:
    Traceback (most recent call last):
...
      File "<doctest __main__.example_73[9]>", line 1, in <module>
        set_verbose(-Integer(1)); plot(lambda x: S(x).gamma(), -Integer(6),Integer(4)).show(ymin=-Integer(3),ymax=Integer(3))###line 2180:
    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)
      File "/home/cwitty/sage-3.3.alpha5/local/lib/python2.5/site-packages/sage/plot/misc.py", line 428, in wrapper
        return func(*args, **kwds)
...
      File "<doctest __main__.example_73[9]>", line 1, in <lambda>
        set_verbose(-Integer(1)); plot(lambda x: S(x).gamma(), -Integer(6),Integer(4)).show(ymin=-Integer(3),ymax=Integer(3))###line 2180:
    sage: set_verbose(-1); plot(lambda x: S(x).gamma(), -6,4).show(ymin=-3,ymax=3)
      File "expression.pyx", line 2183, in sage.symbolic.expression.Expression.gamma (sage/symbolic/expression.cpp:8410)
    RuntimeError: tgamma_eval(): simple pole
**********************************************************************
File "/home/cwitty/sage-3.3.alpha5/devel/sage-mqtmp/sage/symbolic/expression.pyx", line 2204:
    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()
Exception raised:
    Traceback (most recent call last):
...
      File "<doctest __main__.example_74[7]>", line 1, in <module>
        set_verbose(-Integer(1)); plot(lambda x: S(x).lgamma(), -Integer(7),Integer(8), plot_points=Integer(1000)).show()###line 2204:
    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()
...
      File "<doctest __main__.example_74[7]>", line 1, in <lambda>
        set_verbose(-Integer(1)); plot(lambda x: S(x).lgamma(), -Integer(7),Integer(8), plot_points=Integer(1000)).show()###line 2204:
    sage: set_verbose(-1); plot(lambda x: S(x).lgamma(), -7,8, plot_points=1000).show()
      File "expression.pyx", line 2210, in sage.symbolic.expression.Expression.lgamma (sage/symbolic/expression.cpp:8476)
    RuntimeError: lgamma_eval(): logarithmic pole
**********************************************************************
2 items had failures:
   2 of  10 in __main__.example_73
   1 of  10 in __main__.example_74
***Test Failed*** 3 failures.
```



---

Comment by cwitty created at 2009-02-07 05:20:17

I've placed a proposed patch for the above doctest failure at #5199.  So I'm now saying that this is "ready for review" again; but the patch now depends on #5199 (and #3938, if the reviewer is using a version of Sage older than 3.3.alpha3).


---

Comment by mhansen created at 2009-02-09 08:01:25

The fixups patch looks good to me except for the following two failures:


```
**********************************************************************
File "/home/mhansen/sage-coxeter/devel/sage-main/sage/rings/number_field/totallyreal_data.pyx", line 74:
    sage: hermite_constant(1) # trivial one-dimensional lattice
Expected:
    1.0
Got:
    1
**********************************************************************
File "/home/mhansen/sage-coxeter/devel/sage-main/sage/rings/number_field/totallyreal_data.pyx", line 80:
    sage: hermite_constant(8) # E_8
Expected:
    2.0
Got:
    2
**********************************************************************
```



---

Comment by mabshoff created at 2009-02-09 08:52:12

I cannot reproduce the failures Mike saw and I assume #5199 fixed that.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 08:53:42

Merged 2898-jgrout-coerce-to-integer-3.3.alpha2.patch and trac2898-fixups.patch in Sage 3.3.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-09 08:53:42

Resolution: fixed
