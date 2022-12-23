# Issue 4412: [with patch, needs review] extend the local information function for elliptic curves over number fields

Issue created by migration from https://trac.sagemath.org/ticket/4412

Original creator: cremona

Original creation time: 2008-10-31 16:46:51

Assignee: was

CC:  alexghitza

Keywords: elliptic curve local data

This is essentially a continuation of #3897.  I have added functionality to  ell_local_data.py so that for elliptic curves over number fields (and over Q) you can (1) ask about additive vs. split vs. non-split multiplicative reduction at a prime; (2) Ask for the Tamagawa index (which is not always equal to the T. number) and also (3) added some better documentation to the kodaira_symbol code.

The motivation is that this is used i computing p-adic elliptic logs which in turn in used in the S-integral points code which is coming along nicely.  But this stuff is independent of that so I thought it could be posted separately.

The patch should apply to 3.2.alpha1.


---

Attachment


---

Comment by mvngu created at 2008-11-01 07:34:26

fix typos found after applying cremona's patch


---

Attachment

The patch *4412-typo-localdata.patch* was produced under sage-3.1.4. It fixes various typos that were found after applying cremona's patch *sage-localdata.patch*. That is, *4412-typo-localdata.patch* should be applied on top of *sage-localdata.patch*.


---

Comment by cremona created at 2008-11-01 10:14:29

Replying to [comment:1 mvngu]:
> The patch *4412-typo-localdata.patch* was produced under sage-3.1.4. It fixes various typos that were found after applying cremona's patch *sage-localdata.patch*. That is, *4412-typo-localdata.patch* should be applied on top of *sage-localdata.patch*.

Many thanks!  I was relieved to see that most of those typos are pre-existing ones and not new ones introduced by me.  In the place where you give two alternatives I prefer the first one (and that one is my fault).  John


---

Comment by was created at 2008-11-28 23:07:02

REFEREEing:

Applies and all elliptic_curve tests pass.  I had to slightly rebase the typo fix patch, and fix the "which do you mean" issue.  

```
All tests passed!
Total time for all tests: 67.1 seconds
was@sage:~/build/sage-3.2.1.alpha1$ 
```


I've attached the rebased patch.


---

Attachment

REFEREE REPORT:

This is an extremely good patch, with about a 10:1 ratio of documentation to code, and it really really needs to get in.  Here are a few minor issues that need to get fixed.  When they are all fixed, I'll give this a positive review.

1. Please add a doctest to illustrate the algorithm= option to EllipticCurveLocalData, since all the doctests look like this, and none illustrate that new parameter. 

```
EllipticCurveLocalData(E,7)
```


2. Once you do 1, you'll find it doesn't work, at least in the only example I tried:

```
sage: E = EllipticCurve('14a1') 
sage: from sage.schemes.elliptic_curves.ell_local_data import EllipticCurveLocalData 
sage: EllipticCurveLocalData(E,2, algorithm='generic')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/was/build/sage-3.2.1.alpha1/<ipython console> in <module>()

/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_local_data.pyc in __init__(self, E, P, proof, algorithm)
    110             self._Emin, ch, self._val_disc, self._fp, self._KS, self._cp, self._split = self._tate(proof)
    111             if self._fp>0:
--> 112                 if self._Emin.c4().valuation(p)>0:
    113                     self._reduction_type = 0
    114                 elif self._split:    

/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/rational.so in sage.rings.rational.Rational.valuation (sage/rings/rational.c:6338)()

/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.valuation (sage/rings/integer.c:14944)()

/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__init__ (sage/rings/integer.c:6054)()

TypeError: unable to coerce <class 'sage.rings.ideal.Ideal_pid'> to an integer
```


3. Giving a meaningless algorithm option should raise a ValueError:

```
sage: EllipticCurveLocalData(E,2, algorithm='foo bar')
```


4. This line (line 240)

```
if not cp==4: 
```

looks silly.  How about "if cp != 4:"?

5. For consistency in your docstrings in the assignments could you put spaces
around =?  For example, you have

```
        476	            sage: K.<a>=NumberField(x^3-2) 
 	477	            sage: P17a, P17b = [P for P,e in K.factor(17)] 
 	478	            sage: E = EllipticCurve([0,0,0,0,2*a+1]) 
```

so sometimes there is space (which I really like!) and sometimes there isn't.


---

Attachment

Thanks for the detailed review.  The latest patch addresses all of those:
    1. Extra tests added
    2. Fixed (really a logic error)
    3. A ValueError is now raised (see extra doctest)
    4. Changed
    5. Changed (I agree with the convention but some always slip through!)

Tested on 3.2.1.rc0, all tests in elliptic_curves/ pass.


---

Comment by mabshoff created at 2008-11-30 07:15:04

Merged sage-localdata.patch, trac_sage-4412_typos-rebased.patch and trac_sage-4412_post-review.patch in Sage 3.2.1.rc1

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 07:15:04

Resolution: fixed
