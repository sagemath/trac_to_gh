# Issue 6386: [with patch, needs review] Implement elliptic exponential

archive/issues_006386.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @robertwb\n\nKeywords: elliptic curve\n\nThe elliptic exponential is the inverse to the elliptic log, i.e. it is the Weierstrass parametrization CC/L -> E(CC) for an elliptic curve.\n\nThe patch implements this as a member function of the PeriodLattice_ell class.  It works for all period lattices, real or not.  Currently it is accessible via a member function for elliptic curves over Q;  I'll make it work over number fields too, but ona separate ticket.  [At present it would already work for real embeddings;  shortly a rigorously justified elliptic log for non-real embeddings will also be ready.]\n\nThe hard work is done by pari's ellwp0() function, which was already wrapped, but to get the precision right that had to be slightly changed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6386\n\n",
    "created_at": "2009-06-22T18:09:09Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "[with patch, needs review] Implement elliptic exponential",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6386",
    "user": "@JohnCremona"
}
```
Assignee: @williamstein

CC:  @robertwb

Keywords: elliptic curve

The elliptic exponential is the inverse to the elliptic log, i.e. it is the Weierstrass parametrization CC/L -> E(CC) for an elliptic curve.

The patch implements this as a member function of the PeriodLattice_ell class.  It works for all period lattices, real or not.  Currently it is accessible via a member function for elliptic curves over Q;  I'll make it work over number fields too, but ona separate ticket.  [At present it would already work for real embeddings;  shortly a rigorously justified elliptic log for non-real embeddings will also be ready.]

The hard work is done by pari's ellwp0() function, which was already wrapped, but to get the precision right that had to be slightly changed.

Issue created by migration from https://trac.sagemath.org/ticket/6386





---

archive/issue_comments_051125.json:
```json
{
    "body": "Attachment [ellexp.patch](tarball://root/attachments/some-uuid/ticket6386/ellexp.patch) by @JohnCremona created at 2009-06-22 18:09:33\n\nApplies to 4.0.2",
    "created_at": "2009-06-22T18:09:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51125",
    "user": "@JohnCremona"
}
```

Attachment [ellexp.patch](tarball://root/attachments/some-uuid/ticket6386/ellexp.patch) by @JohnCremona created at 2009-06-22 18:09:33

Applies to 4.0.2



---

archive/issue_comments_051126.json:
```json
{
    "body": "For the most part this looks good, and specifically I wasn't able to find any precision issues. \n\n* I think the elliptic exponential should actually return a point on E(C), not just a tuple (x,y)\n\n* The docstring in elliptic exponential about to_Weierstrass is wrong. (Maybe it could be to_curve, default True to give something on E(C), false returning the raw `(wp(z), wp'(z))`.\n\n* The `antilogarithm` shouldn't simply discard the imaginary part: \n\n\n```\nsage: E = EllipticCurve('389a')\nsage: z0 = CC(1.76776906963, 0.303020775118)\nsage: E.elliptic_exponential(z0)\n(1.00012725137998 + 1.00002216580174*I,\n 0.000229106700941339 + 2.00010160734906*I)\nsage: E.antilogarithm(z0, 10)\n(1 : 0 : 1)\n```\n",
    "created_at": "2009-06-25T10:16:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51126",
    "user": "@robertwb"
}
```

For the most part this looks good, and specifically I wasn't able to find any precision issues. 

* I think the elliptic exponential should actually return a point on E(C), not just a tuple (x,y)

* The docstring in elliptic exponential about to_Weierstrass is wrong. (Maybe it could be to_curve, default True to give something on E(C), false returning the raw `(wp(z), wp'(z))`.

* The `antilogarithm` shouldn't simply discard the imaginary part: 


```
sage: E = EllipticCurve('389a')
sage: z0 = CC(1.76776906963, 0.303020775118)
sage: E.elliptic_exponential(z0)
(1.00012725137998 + 1.00002216580174*I,
 0.000229106700941339 + 2.00010160734906*I)
sage: E.antilogarithm(z0, 10)
(1 : 0 : 1)
```




---

archive/issue_comments_051127.json:
```json
{
    "body": "Replying to [comment:2 robertwb]:\n> For the most part this looks good, and specifically I wasn't able to find any precision issues. \n> \n> * I think the elliptic exponential should actually return a point on E(C), not just a tuple (x,y)\n\nOK, I'll do that.  I literally had not tried that!\n\n> \n> * The docstring in elliptic exponential about to_Weierstrass is wrong. (Maybe it could be to_curve, default True to give something on E(C), false returning the raw `(wp(z), wp'(z))`.\n\nI'll check that out.\n\n> \n> * The `antilogarithm` shouldn't simply discard the imaginary part: \n> \n> {{{\n> sage: E = EllipticCurve('389a')\n> sage: z0 = CC(1.76776906963, 0.303020775118)\n> sage: E.elliptic_exponential(z0)\n> (1.00012725137998 + 1.00002216580174*I,\n>  0.000229106700941339 + 2.00010160734906*I)\n> sage: E.antilogarithm(z0, 10)\n> (1 : 0 : 1)\n> }}}\n\nMy reasoning is that you only use this function when you have reason to believe that the result is actually a rational point, so in particular it is real.  Can I just clarify the docstring?  Note that this function is never going to be able to give a provable result, at best it will retrun a rational point whose elliptic log is close to the input value, but it is still a useful thing to have.",
    "created_at": "2009-06-25T12:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51127",
    "user": "@JohnCremona"
}
```

Replying to [comment:2 robertwb]:
> For the most part this looks good, and specifically I wasn't able to find any precision issues. 
> 
> * I think the elliptic exponential should actually return a point on E(C), not just a tuple (x,y)

OK, I'll do that.  I literally had not tried that!

> 
> * The docstring in elliptic exponential about to_Weierstrass is wrong. (Maybe it could be to_curve, default True to give something on E(C), false returning the raw `(wp(z), wp'(z))`.

I'll check that out.

> 
> * The `antilogarithm` shouldn't simply discard the imaginary part: 
> 
> {{{
> sage: E = EllipticCurve('389a')
> sage: z0 = CC(1.76776906963, 0.303020775118)
> sage: E.elliptic_exponential(z0)
> (1.00012725137998 + 1.00002216580174*I,
>  0.000229106700941339 + 2.00010160734906*I)
> sage: E.antilogarithm(z0, 10)
> (1 : 0 : 1)
> }}}

My reasoning is that you only use this function when you have reason to believe that the result is actually a rational point, so in particular it is real.  Can I just clarify the docstring?  Note that this function is never going to be able to give a provable result, at best it will retrun a rational point whose elliptic log is close to the input value, but it is still a useful thing to have.



---

archive/issue_comments_051128.json:
```json
{
    "body": "Apply after previous",
    "created_at": "2009-06-25T16:07:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51128",
    "user": "@JohnCremona"
}
```

Apply after previous



---

archive/issue_comments_051129.json:
```json
{
    "body": "Attachment [trac_6386-post-review.patch](tarball://root/attachments/some-uuid/ticket6386/trac_6386-post-review.patch) by @JohnCremona created at 2009-06-25 16:08:13\n\nI have done the first thing requested, delivering a point in E(CC) or E(RR) in cases where it is possible to tell that the point is real.  I had to use \"check=False\" since the returned x,y do not necessarily satisfy the equation to the given precision.  I'm not sure what the problem was in the second point, but I changed the name of the parameter to \"to_curve\" and fixed a typo in the docstring (it said True instead of False, or possibly the other way round, at one point -- this might have caused the confusion).\n\nI have left the third point, with the explanation given above!",
    "created_at": "2009-06-25T16:08:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51129",
    "user": "@JohnCremona"
}
```

Attachment [trac_6386-post-review.patch](tarball://root/attachments/some-uuid/ticket6386/trac_6386-post-review.patch) by @JohnCremona created at 2009-06-25 16:08:13

I have done the first thing requested, delivering a point in E(CC) or E(RR) in cases where it is possible to tell that the point is real.  I had to use "check=False" since the returned x,y do not necessarily satisfy the equation to the given precision.  I'm not sure what the problem was in the second point, but I changed the name of the parameter to "to_curve" and fixed a typo in the docstring (it said True instead of False, or possibly the other way round, at one point -- this might have caused the confusion).

I have left the third point, with the explanation given above!



---

archive/issue_comments_051130.json:
```json
{
    "body": "Looks good. Using check=False is fine, there's really no way around it. \n\nI understand your point, but I would be more comfortable if for antilogarithm you at least bounded the magnitude of the imaginary part as a function of the error in the real part. Also, it has undesirable behavior when x or y (or both) are supposed to be 0, but are off by machine epsilon. Neither of these are regressions to what was there before, and I like the doctests, so I'm not stuck on this. \n\nPositive review pending acceptance of the tiny patch above.",
    "created_at": "2009-06-26T04:47:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51130",
    "user": "@robertwb"
}
```

Looks good. Using check=False is fine, there's really no way around it. 

I understand your point, but I would be more comfortable if for antilogarithm you at least bounded the magnitude of the imaginary part as a function of the error in the real part. Also, it has undesirable behavior when x or y (or both) are supposed to be 0, but are off by machine epsilon. Neither of these are regressions to what was there before, and I like the doctests, so I'm not stuck on this. 

Positive review pending acceptance of the tiny patch above.



---

archive/issue_comments_051131.json:
```json
{
    "body": "Wait, I take that back. There's still some issues: \n\n* `E.elliptic_exponential(z)` gives a tuple while `E.period_lattice().elliptic_exponential()` gives a point. They should both at least be consistent, and I think the latter is better. \n\n* When you use check=False, you have to give projective coordinates because it doesn't check to add the 1 at the end.",
    "created_at": "2009-06-26T05:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51131",
    "user": "@robertwb"
}
```

Wait, I take that back. There's still some issues: 

* `E.elliptic_exponential(z)` gives a tuple while `E.period_lattice().elliptic_exponential()` gives a point. They should both at least be consistent, and I think the latter is better. 

* When you use check=False, you have to give projective coordinates because it doesn't check to add the 1 at the end.



---

archive/issue_comments_051132.json:
```json
{
    "body": "apply after other two",
    "created_at": "2009-06-26T05:52:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51132",
    "user": "@robertwb"
}
```

apply after other two



---

archive/issue_comments_051133.json:
```json
{
    "body": "Attachment [6386-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket6386/6386-referee-fixes.patch) by @robertwb created at 2009-06-26 05:55:31\n\nOK, I resolved the issues above, and while I was at it modified antilogarithm to look at the imaginary parts. Now I need a review from you.",
    "created_at": "2009-06-26T05:55:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51133",
    "user": "@robertwb"
}
```

Attachment [6386-referee-fixes.patch](tarball://root/attachments/some-uuid/ticket6386/6386-referee-fixes.patch) by @robertwb created at 2009-06-26 05:55:31

OK, I resolved the issues above, and while I was at it modified antilogarithm to look at the imaginary parts. Now I need a review from you.



---

archive/issue_comments_051134.json:
```json
{
    "body": "I agree with all the changes you made -- thanks for all the attention to detail!  the sequence of 3 patches applies fine to 4.0.2 and relevant tests pass on 32 and 64 bit, so I'll give this a positive review.  [Note to release manager: Robert positively reviewed my two patches modulo his and I approve of his!]",
    "created_at": "2009-06-26T08:41:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51134",
    "user": "@JohnCremona"
}
```

I agree with all the changes you made -- thanks for all the attention to detail!  the sequence of 3 patches applies fine to 4.0.2 and relevant tests pass on 32 and 64 bit, so I'll give this a positive review.  [Note to release manager: Robert positively reviewed my two patches modulo his and I approve of his!]



---

archive/issue_comments_051135.json:
```json
{
    "body": "Doctest failure when applied to 4.1.alpha1 -- this one looks pretty easy.\n\n\n```\nsage -t -long devel/sage/sage/symbolic/pynac.pyx\n**********************************************************************\nFile \"/space/boothby/sage-4.1.alpha1/devel/sage-main/sage/symbolic/pynac.pyx\", line 850:\n    sage: py_imag(RR(1))\nExpected:\n    0\nGot:\n    0.000000000000000\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_22\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /space/boothby/sage-4.1.alpha1/tmp/.doctest_pynac.py\n         [2.1 s]\n```\n",
    "created_at": "2009-06-27T02:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51135",
    "user": "boothby"
}
```

Doctest failure when applied to 4.1.alpha1 -- this one looks pretty easy.


```
sage -t -long devel/sage/sage/symbolic/pynac.pyx
**********************************************************************
File "/space/boothby/sage-4.1.alpha1/devel/sage-main/sage/symbolic/pynac.pyx", line 850:
    sage: py_imag(RR(1))
Expected:
    0
Got:
    0.000000000000000
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_22
***Test Failed*** 1 failures.
For whitespace errors, see the file /space/boothby/sage-4.1.alpha1/tmp/.doctest_pynac.py
         [2.1 s]
```




---

archive/issue_comments_051136.json:
```json
{
    "body": "Hmm... actually I didn't know that imag(z) worked before. Perhaps an exact zero is better to return here after all...",
    "created_at": "2009-06-27T02:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51136",
    "user": "@robertwb"
}
```

Hmm... actually I didn't know that imag(z) worked before. Perhaps an exact zero is better to return here after all...



---

archive/issue_comments_051137.json:
```json
{
    "body": "Robert, I think this was caused by something you added?  Namely, that x.imag() when x is a RealField element is now not an exact zero but 0 in that realfield.  I'm not at all sure what's best here -- perhaps consult on sage-devel?",
    "created_at": "2009-06-27T14:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51137",
    "user": "@JohnCremona"
}
```

Robert, I think this was caused by something you added?  Namely, that x.imag() when x is a RealField element is now not an exact zero but 0 in that realfield.  I'm not at all sure what's best here -- perhaps consult on sage-devel?



---

archive/issue_comments_051138.json:
```json
{
    "body": "Yep, this was due to the method I added. I'm changing it back to what it used to be.",
    "created_at": "2009-06-27T17:15:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51138",
    "user": "@robertwb"
}
```

Yep, this was due to the method I added. I'm changing it back to what it used to be.



---

archive/issue_comments_051139.json:
```json
{
    "body": "Attachment [6386-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6386/6386-doctest-fix.patch) by @robertwb created at 2009-06-27 17:15:57\n\napply after all others",
    "created_at": "2009-06-27T17:15:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51139",
    "user": "@robertwb"
}
```

Attachment [6386-doctest-fix.patch](tarball://root/attachments/some-uuid/ticket6386/6386-doctest-fix.patch) by @robertwb created at 2009-06-27 17:15:57

apply after all others



---

archive/issue_comments_051140.json:
```json
{
    "body": "I applied all four patches successfully to 4.1.alpha2, and all tests pass (even with testall I only got the same failures as with a vanilla 4.1.alpha2).  Let's go!",
    "created_at": "2009-06-28T11:26:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51140",
    "user": "@JohnCremona"
}
```

I applied all four patches successfully to 4.1.alpha2, and all tests pass (even with testall I only got the same failures as with a vanilla 4.1.alpha2).  Let's go!



---

archive/issue_comments_051141.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-03T18:14:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6386",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6386#issuecomment-51141",
    "user": "@rlmill"
}
```

Resolution: fixed
