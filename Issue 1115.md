# Issue 1115: Sha_an either fails or lies when prec isn't the default 53

Issue created by migration from https://trac.sagemath.org/ticket/1115

Original creator: was

Original creation time: 2007-11-06 21:54:49

Assignee: was

This example illustrates the problem:

```
sage: E = EllipticCurve('389a')
sage: sha = E.sha()
sage: sha.an_numerical(200)
Traceback (most recent call last):
...
TypeError: unsupported operand parent(s) for '/': 'Complex Field with 200 bits of precision' and 'Real Field with 53 bits of precision'
sage: sha.an_numerical()
0.999999999999998
sage: sha.an_numerical(200)
0.999999999999998
sage: sha.an_numerical(300)
0.999999999999998
```



---

Comment by robertwb created at 2008-01-04 21:58:45

I am unable to reproduce the TypeError. Is the lie just in the precision? 

The docstring states that only the L-series is calculated with the given precision. This could be passed onto Omega as well, but letting mwrank run at precision 200 would probably take a long, long time. 

Once the generators are known, the regulator could be computed directly (rather than asking mwrank) to high precision, but this would be more an enhancement than a bug fix.


---

Comment by cremona created at 2008-08-31 17:15:17

The reported bug seems to have gone away, but the suggested enhancement is easy to do and I will do it.  We are using mwrank to get the gens and also the regulator;  but once we have the gens it is better to compute the regulator ourselves (using the height_pairing_matrix() function I put in as part of the integral points patch, which allows for arbitrary precision).

I'll do this, and have accordingly changed the trac Type to "enhancement".  The milestone should probably not be 3.1.2 though.


---

Comment by cremona created at 2008-08-31 17:15:17

Changing type from defect to enhancement.


---

Attachment

The patch sage-trac1115.patch implements the following:

In ell_point.py: arbitrary precision for canonical heights (over Q)

In ell_rational_field.py: improved use of database for gens() (e.g. if the curve is not in the database but an isomorphic curve is);  no longer gets regulator from db but computes it from gens;  regulator_of_points() function to find the regulators (i.e. det of height pairing matrix) for any list of points, to arbitrary precision;  revised regulator() function handles arbitrary precision with caching.

In ell_sha.py:  full precision setting for an_numerical(), which amongst other things deals with the original posting.


---

Comment by cremona created at 2008-09-01 11:36:45

PS Patch should apply to 3.1.2.alpha3+, but note that there are some intersecting changes in the patch at #3377 and it is possible that applying one after the other will need some attention.  Since I don't know which will get reviewed first, I am leaving things like this.


---

Comment by mabshoff created at 2008-09-01 11:37:12

:)


---

Comment by AlexGhitza created at 2008-09-02 09:43:00

I'm in the process of looking at this.  Here are two things:

1. I get a doctest failure in ell_point.py.  Not sure what's going on, but it's basically the following:

```
sage: e = EllipticCurve([0,0,1,-1,0])  
sage: dumps(e);
sage: g = e.gens()                                                             
sage: dumps(e);
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/opt/sage-3.1.2.alpha3/devel/sage-main/sage/<ipython console> in <module>()

/opt/sage-3.1.2.alpha3/devel/sage-main/sage/sage_object.pyx in sage.structure.sage_object.dumps (sage/structure/sage_object.c:5132)()

RuntimeError: maximum recursion depth exceeded
```


So somehow the new gens or regulator code breaks dumps(e).


2. a few minor typos:
- line 657 of ell_point.py: "precision of None" should be "precision if None"
- line 1473 of ell_rational_field.py: "int or Noene" should be "int or None"
- line 1588 of ell_rational_field.py: "number of bit" should be "number of bits"

Everything else seems to work as advertised.


---

Comment by cremona created at 2008-09-02 09:50:52

Thanks -- I can easily fix the typos of course.  But I have no idea about the dumps() problem -- I don't think I have ever called the dumps function and I have no idea what it does.  Can you enlighten me a bit?

This works for me:

```
john@ubuntu%./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: sha
sage: e = EllipticCurve([0,0,1,-1,0])  
sage: dumps(e);                        
sage: g = e.gens()                    
sage: dumps(e);   
sage: e == loads(dumps(e))
True
```



---

Attachment

Correction of docstring typos in previous patch


---

Attachment

The second patch corrects the typos (and makes the description of the precision parameter consistent in those three places). [I think I may have attached it twice: if so ignore one of the files sage-trac1115a.patch .  Sorry.]

I tried the dumps() thing again on a 64-bit machine and got the same error as you.

Michael A, any chance you can help determine what makes this dumps() call work ok in 32-bit but not in 64-bit?


---

Comment by AlexGhitza created at 2008-09-03 06:39:14

After an inordinate amount of staring at this, I managed to figure out what's going on.  The new code in gens() introduces an unwanted recursion that goes on and on and makes dumps() complain as we have seen.  The culprit is on line 1340 of the first patch John posted, where there is a call to E.gens(), which will come back to this very point and get another call to E.gens() etc.

The fix is to replace E.gens() with E.gens(use_database=False), since E is already a database curve.

I'll have a new patch up soon.


---

Attachment

apply only this patch, after #3377


---

Comment by AlexGhitza created at 2008-09-03 06:56:18

There is nontrivial intersection with the patch at #3377, and trying to keep the two separate seems not fun.  Since #3377 has a positive review and will therefore be merged soon, I am posting a new patch here that depends on #3377.

So: apply the patch 1115-sha_prec.patch instead of the others, and after merging #3377.

Credit goes of course to John Cremona.


---

Comment by cremona created at 2008-09-03 08:44:14

Replying to [comment:11 AlexGhitza]:
> There is nontrivial intersection with the patch at #3377, and trying to keep the two separate seems not fun.  Since #3377 has a positive review and will therefore be merged soon, I am posting a new patch here that depends on #3377.
> 
> So: apply the patch 1115-sha_prec.patch instead of the others, and after merging #3377.
> 
> Credit goes of course to John Cremona.

 -- including the credit for introducing the infinite recursion!

Thanks, Alex, for your work tracking this down.  I think that in the end it was not a 32/64-bit thing at all, but rather that my 32-bit system had the optional database which *does* include the gens for database curves, while the 64-bit test I did was with a Sage which did not have the large database and hence had no gens.

I will need to change Alex's fix though:  it has the effect that even when the large database is installed so the database curve's gens are known, they are not used!  The trick will be to test if the database curve's field `__gens` is set and extract the gens from there directly instead of calling the gens() function again.

I'll do this and test it after sorting out #3377.


---

Attachment


---

Comment by cremona created at 2008-09-03 10:53:16

The new small patch  1115-sha_prec-1.patch fixes the issue raised above:  without the recursive call to gens(), it gets the database curve's gens if they are there and maps them to this curve.

I have tested this on 3.1.2.alpha4 + 3377 patches, both on 32- and 64-bit machines, bothe before and after installing the optional database (the one with the gens).

I hope that does it!


---

Comment by AlexGhitza created at 2008-09-03 12:17:27

I'm getting paranoid so I've tried out John's mini-patch (although he didn't ask for it :).

Verdict: good.

After #3377 is closed, apply 1115-sha_prec.patch followed by 1115-sha_prec-1.patch.


---

Comment by mabshoff created at 2008-09-03 16:16:24

Merged 1115-sha_prec.patch and 1115-sha_prec-1.patch in Sage 3.1.2.rc0.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-03 16:16:24

Resolution: fixed
