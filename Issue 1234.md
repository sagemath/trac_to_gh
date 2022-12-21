# Issue 1234: analytic_rank crashes

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2007-11-21 14:04:25

Assignee: was

Maybe the following is not feasible, but analytic_rank could crash smoothly.


```
sage: d=100032426715415089/251987961355200625
sage: E = EllipticCurve([0, -d^3+5*d^2, 0, -8*d^5+8*d^4, 4*d^8-8*d^7+4*d^6])
sage: F = E.minimal_model()
sage: F.analytic_rank(algorithm='cremona')
<type 'exceptions.RuntimeError'>: Error: '  *** elltors: precision too low in torsell.

sage: F.analytic_rank(algorithm='rubinstein')
<type 'exceptions.TypeError'>: unable to convert x (= 6.90579e+20 and is too large) to an integer

sage: F.analytic_rank(algorithm='sympow')
sympow 1.018 RELEASE  (c) Mark Watkins --- see README and COPYING for details
**ERROR** c4 invariant is too large
```


From John Cremona: the "cremona" version just wraps a gp script, which
needs to have sufficient precision even for ellinit() to work ok here.
Unfortunately this call will run in its own gp session, and it is not
possible for the user to set the precision.  (I found the same while
running a lot of examples through Denis Simon's gp scripts).  The
solution is to change the wrapper to have a precision parameter, with
some reasonable default for backwards compatibility, which gets passes
through to gp.



---

Comment by cremona created at 2007-11-21 14:18:23

NB I think that all functions which wrap gp scripts should have the ability to set various gp defaults before the scripts are run.  Notably the real precision (which is the culprit above), but also in other cases.

This should be easy but tedious -- is there anywhere a list of which functions operate by running a gp script?

jec


---

Comment by mabshoff created at 2008-02-15 22:58:31

Still an issue with Sage 2.10.2.alpha0.

Cheers,

Michael


---

Comment by cremona created at 2008-02-16 10:36:50

I can only speak for the first of these, begin responsible for the gp script which computes analytic rank.

This curve has conductor N=690579402364042119390 which is vastly too big for the analytic rank algorithm anyway (it requires the computation of O(sqrt(N)) terms of the L-series).

Also relevant here is that my analytic rank gp code is *old*.  When Magma adopted it, it was vastly improved (by Mark Watkins), which means that for several years I have not used my own gp program at all, let alone developed it.  For this curve, I don't think even Magma would succeed in computing its analytic rank.


---

Comment by mabshoff created at 2008-06-26 06:56:16

What shall we do about this ticket?

Thoughts?

Cheers,

Michael


---

Comment by cremona created at 2008-06-26 08:19:15

Replying to [comment:5 mabshoff]:
> What shall we do about this ticket?
> 
> Thoughts?
> 
> Cheers,
> 
> Michael

Given the fundamental problem that computing the analytic rank increases rapidly with the conductor N (I think it is sqrt(N)), one solution would be to impose a (carefully-chosen but necessarily somewhat arbitrary) cutoff N_max, so that asking for the analytic rank of a curve of conductor>N_max would result in an error.

One way to implement this would be to have N_max a parameter to the analytic rank function, with a default value of (say) `10^6` or `10^7`.  (I would have to do some experiments to decide on a sensible value).  The docstring could explain that the user is allowed to increase this but warn that it may take (effectively) for ever.


---

Comment by cremona created at 2008-06-26 08:23:04

PS The vale of N_max would presumably be different for the different algorithms supported (sympow, lcalc, etc).  I was only thing of the "cremona" algorithm.  I also note that the docstring claims that lcalc is the most efficient, but cremona is the default -- that was not my decision!


---

Attachment


---

Comment by was created at 2009-01-22 08:26:33

The attached patch cleans up the exceptions raised, as requested.  Also, in the (default) case where Cremona's gp script is used, the precision is automatically doubled until it doesn't fail.  I also start the precision at 16 rather than the default, since it will get automatically double if necessary, and it's about 3 times faster usually by using this smaller precision to start:


```
BEFORE:
sage: E = EllipticCurve('5077a')
sage: time E.analytic_rank()
CPU times: user 0.01 s, sys: 0.01 s, total: 0.02 s
Wall time: 0.21 s


AFTER:
sage: E = EllipticCurve('5077a')
sage: time E.analytic_rank()
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.06 s


and another

BEFORE:
sage: time elliptic_curves.rank(4)[0].analytic_rank()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.50 s
4

AFTER:
sage: time elliptic_curves.rank(4)[0].analytic_rank()
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.33 s
4
```



---

Comment by cremona created at 2009-01-22 09:40:18

Review:  excellent and well done.  Applies cleanly to 3.3.alpha0 and all tests in elliptic_curves pass.

Suggestion:  I see that for EllipticCurve([1234567,89101112]) which has conductor 61928339435779485920, sympow and rubinstein know they are beaten and quit, while cremona just takes a long time (I did not wait).  It might be a good idea to work out a sensible conductor limit for my gp script and have sage only call the script if under that (perhaps with a parameter to allow users to override it).  But that would depend on many factors (speed of machine etc), and this patch should not be delayed because of that.

Pass!


---

Comment by zimmerma created at 2009-01-22 09:46:25

I also was testing the patch, but John was faster than me. Just a comment: it would be better to capitalize
people names (rubinstein -> Rubinstein, weierstrass -> Weierstrass), at least in the documentation
(for the options, it might involve too much work).


---

Comment by cremona created at 2009-01-22 10:09:16

Replying to [comment:10 zimmerma]:
> I also was testing the patch, but John was faster than me. Just a comment: it would be better to capitalize
> people names (rubinstein -> Rubinstein, weierstrass -> Weierstrass), at least in the documentation
> (for the options, it might involve too much work).

I agree with capitalization in documentation;  for parameters it would probably be best to allow either.


---

Comment by mabshoff created at 2009-01-23 10:26:07

Merged in Sage 3.3.alpha1

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-23 10:26:07

Resolution: fixed
