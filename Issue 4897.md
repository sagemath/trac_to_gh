# Issue 4897: integral_points() misses some points

archive/issues_004897.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  tnagel mardaus\n\nKeywords: elliptic curve integral points\n\nFrancois Glineur reported to me that for the elliptic curve \"20160bg2\" not all integral points are found.\n\n```\nsage: E=EllipticCurve('20160bg2')\nsage: [P[0] for P in E.integral_points()]\n[-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 186, 1476, 2034, 67246]\n```\n\nwhile Magma gives\n\n```\n> E:=EllipticCurve([0, 0, 0, -468, 2592]);\n> Sort([P[1] : P in IntegralPoints(E)]);\n[ -24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 168, 186, 381, \n1476, 2034, 67246 ]\n```\n\nso we are missing x=168 and x=381.\n\nThe curve has rank 2 and full 2-torsion.\nThe point Q=(168,2160) is the unique integral point its coset modulo torsion and I think that is why it is being missed.  In fact it seems incredible that this has not been seen before in all the testing which was done!\n\nI therefore think that the function  integral_points_with_bounded_mw_coeffs() is at fault, and will fix it.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4897\n\n",
    "created_at": "2008-12-31T10:42:46Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "integral_points() misses some points",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4897",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

CC:  tnagel mardaus

Keywords: elliptic curve integral points

Francois Glineur reported to me that for the elliptic curve "20160bg2" not all integral points are found.

```
sage: E=EllipticCurve('20160bg2')
sage: [P[0] for P in E.integral_points()]
[-24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 186, 1476, 2034, 67246]
```

while Magma gives

```
> E:=EllipticCurve([0, 0, 0, -468, 2592]);
> Sort([P[1] : P in IntegralPoints(E)]);
[ -24, -18, -14, -6, -3, 4, 6, 18, 21, 24, 36, 46, 102, 168, 186, 381, 
1476, 2034, 67246 ]
```

so we are missing x=168 and x=381.

The curve has rank 2 and full 2-torsion.
The point Q=(168,2160) is the unique integral point its coset modulo torsion and I think that is why it is being missed.  In fact it seems incredible that this has not been seen before in all the testing which was done!

I therefore think that the function  integral_points_with_bounded_mw_coeffs() is at fault, and will fix it.



Issue created by migration from https://trac.sagemath.org/ticket/4897





---

archive/issue_comments_037059.json:
```json
{
    "body": "That's really incredible that we hadn't noticed this bug during our tests.\nPlease let me know if I can help with fixing this bug.\n\nGreetings Tobias",
    "created_at": "2008-12-31T11:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37059",
    "user": "https://trac.sagemath.org/admin/accounts/users/tnagel"
}
```

That's really incredible that we hadn't noticed this bug during our tests.
Please let me know if I can help with fixing this bug.

Greetings Tobias



---

archive/issue_comments_037060.json:
```json
{
    "body": "It was not that function in the end, but the point_preprocessing function.\n\n```\nHere's the problem (and it is not in the function I thought it was.\n\nThe curve 20160bg2 has two real components.  The generators in the database are\nP1=(-18,72) and P2=(-14,0) which are both on the non-identity\ncomponent.   Preprocessing replaces those by P1+P2, 2*P1 (which\ngenerate a subgroup H of index 2) and the LLL-reduction changes that\nto use Q1=P1+P2=(36,-180) and Q2=-P1+P2=(1476,-56700).\n\nThe missing point (168,2160) is 2*P1+P2+T where T is the torsion point\n(6,0).  This is not in H (even up to torsion).\n\nA better way to do the preprocessing here is to take a torsion point\non the egg (e.g. T=(6,0)) and add that to the generators.  Similarly,\nif there is a torsion point on the egg (necessarily of even order)\nthen we should add it to any of the generators which are on the egg.\nOnly if all torsion points are on the identity component should we do\nwhat we currently do.\n```\n\n\nI have implemented this change and am currently testing.  Patch up later today!",
    "created_at": "2008-12-31T11:45:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37060",
    "user": "https://github.com/JohnCremona"
}
```

It was not that function in the end, but the point_preprocessing function.

```
Here's the problem (and it is not in the function I thought it was.

The curve 20160bg2 has two real components.  The generators in the database are
P1=(-18,72) and P2=(-14,0) which are both on the non-identity
component.   Preprocessing replaces those by P1+P2, 2*P1 (which
generate a subgroup H of index 2) and the LLL-reduction changes that
to use Q1=P1+P2=(36,-180) and Q2=-P1+P2=(1476,-56700).

The missing point (168,2160) is 2*P1+P2+T where T is the torsion point
(6,0).  This is not in H (even up to torsion).

A better way to do the preprocessing here is to take a torsion point
on the egg (e.g. T=(6,0)) and add that to the generators.  Similarly,
if there is a torsion point on the egg (necessarily of even order)
then we should add it to any of the generators which are on the egg.
Only if all torsion points are on the identity component should we do
what we currently do.
```


I have implemented this change and am currently testing.  Patch up later today!



---

archive/issue_comments_037061.json:
```json
{
    "body": "Attachment [trac_4897.patch](tarball://root/attachments/some-uuid/ticket4897/trac_4897.patch) by @JohnCremona created at 2009-01-04 17:44:05\n\nThe patch is based on 3.2.2 + #4901 (which has a positive review but is not yet merged).\n\nIt does what was promised above, i.e. corrects the function  point_preprocessing().  A doctest is added with example from Francois Glineur.  In addition, I reran every single curve in the database (as reported to sage-nt) and have uploaded the revised files to my web page:  in about 1% of cases (over 8000 curves) there are more integral points than before.\n\nThe only file touched here is schemes/elliptic_curves/ell_rational_field.py, which is one of the ones which has already been sphinxified (see #4926) so this patch will need to be merged with that one at some point.",
    "created_at": "2009-01-04T17:44:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37061",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_4897.patch](tarball://root/attachments/some-uuid/ticket4897/trac_4897.patch) by @JohnCremona created at 2009-01-04 17:44:05

The patch is based on 3.2.2 + #4901 (which has a positive review but is not yet merged).

It does what was promised above, i.e. corrects the function  point_preprocessing().  A doctest is added with example from Francois Glineur.  In addition, I reran every single curve in the database (as reported to sage-nt) and have uploaded the revised files to my web page:  in about 1% of cases (over 8000 curves) there are more integral points than before.

The only file touched here is schemes/elliptic_curves/ell_rational_field.py, which is one of the ones which has already been sphinxified (see #4926) so this patch will need to be merged with that one at some point.



---

archive/issue_comments_037062.json:
```json
{
    "body": "Sorry, that should have said: based on 3.2.3.final + #4901.  Strictly, it does not depend on #4901, but it was in testing this patch extensively that the bug fixed in #4901 was found.",
    "created_at": "2009-01-04T17:46:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37062",
    "user": "https://github.com/JohnCremona"
}
```

Sorry, that should have said: based on 3.2.3.final + #4901.  Strictly, it does not depend on #4901, but it was in testing this patch extensively that the bug fixed in #4901 was found.



---

archive/issue_comments_037063.json:
```json
{
    "body": "This patch looks pretty good!\n\nThe patch apllies correctly and all doctest pass.\nAdditional tests didn't show any defects -> positive review.\n\nGreetings\nTobias",
    "created_at": "2009-01-11T10:17:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37063",
    "user": "https://trac.sagemath.org/admin/accounts/users/tnagel"
}
```

This patch looks pretty good!

The patch apllies correctly and all doctest pass.
Additional tests didn't show any defects -> positive review.

Greetings
Tobias



---

archive/issue_events_011310.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T00:57:17Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4897#event-11310"
}
```



---

archive/issue_comments_037064.json:
```json
{
    "body": "This patch causes a doctest failure without the database installed:\n\n```\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.3.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\", line 4305:\n    sage: [P[0] for P in EllipticCurve('20160bg2').integral_points()]\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_109[14]>\", line 1, in <module>\n        [P[Integer(0)] for P in EllipticCurve('20160bg2').integral_points()]###line 4305:\n    sage: [P[0] for P in EllipticCurve('20160bg2').integral_points()]\n      File \"/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py\", line 124, in EllipticCurve\n        return ell_rational_field.EllipticCurve_rational_field(x)\n      File \"/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py\", line 121, in __init__\n        X = sage.databases.cremona.CremonaDatabase()[label]\n      File \"/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/databases/cremona.py\", line 349, in __getitem__\n        return self.elliptic_curve(N)\n      File \"/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/databases/cremona.py\", line 487, in elliptic_curve\n        raise RuntimeError, \"No such elliptic curve in the database (note: use lower case letters!)\"\n    RuntimeError: No such elliptic curve in the database (note: use lower case letters!)\n**********************************************************************\n```\n\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-01-12T00:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37064",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch causes a doctest failure without the database installed:

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha0/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 4305:
    sage: [P[0] for P in EllipticCurve('20160bg2').integral_points()]
Exception raised:
    Traceback (most recent call last):
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mabshoff/build/sage-3.2.4-cycle/sage-3.2.4.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_109[14]>", line 1, in <module>
        [P[Integer(0)] for P in EllipticCurve('20160bg2').integral_points()]###line 4305:
    sage: [P[0] for P in EllipticCurve('20160bg2').integral_points()]
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/constructor.py", line 124, in EllipticCurve
        return ell_rational_field.EllipticCurve_rational_field(x)
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 121, in __init__
        X = sage.databases.cremona.CremonaDatabase()[label]
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/databases/cremona.py", line 349, in __getitem__
        return self.elliptic_curve(N)
      File "/scratch/mabshoff/sage-3.3.alpha0/local/lib/python2.5/site-packages/sage/databases/cremona.py", line 487, in elliptic_curve
        raise RuntimeError, "No such elliptic curve in the database (note: use lower case letters!)"
    RuntimeError: No such elliptic curve in the database (note: use lower case letters!)
**********************************************************************
```


Thoughts?

Cheers,

Michael



---

archive/issue_comments_037065.json:
```json
{
    "body": "Oops, just change `E=EllipticCurve('20160bg2')` to \n`E=EllipticCurve([0,0,0,-468,2592])`\nin that doctest.  It should suffice to edit the patch itself.",
    "created_at": "2009-01-12T09:23:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37065",
    "user": "https://github.com/JohnCremona"
}
```

Oops, just change `E=EllipticCurve('20160bg2')` to 
`E=EllipticCurve([0,0,0,-468,2592])`
in that doctest.  It should suffice to edit the patch itself.



---

archive/issue_comments_037066.json:
```json
{
    "body": "John's patch with his suggested fix integrated.",
    "created_at": "2009-01-12T11:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37066",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

John's patch with his suggested fix integrated.



---

archive/issue_comments_037067.json:
```json
{
    "body": "Attachment [trac_4897.2.patch](tarball://root/attachments/some-uuid/ticket4897/trac_4897.2.patch) by mabshoff created at 2009-01-12 11:07:26\n\nReplying to [comment:7 cremona]:\n> Oops, just change `E=EllipticCurve('20160bg2')` to \n> `E=EllipticCurve([0,0,0,-468,2592])`\n> in that doctest.  It should suffice to edit the patch itself.\n\nYep, I should have thought of that. trac_4897.2.patch does exactly that.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-12T11:07:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37067",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4897.2.patch](tarball://root/attachments/some-uuid/ticket4897/trac_4897.2.patch) by mabshoff created at 2009-01-12 11:07:26

Replying to [comment:7 cremona]:
> Oops, just change `E=EllipticCurve('20160bg2')` to 
> `E=EllipticCurve([0,0,0,-468,2592])`
> in that doctest.  It should suffice to edit the patch itself.

Yep, I should have thought of that. trac_4897.2.patch does exactly that.

Cheers,

Michael



---

archive/issue_comments_037068.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-12T11:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37068",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037069.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-12T11:08:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37069",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_events_011311.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-12T11:08:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4897#event-11311"
}
```



---

archive/issue_comments_037070.json:
```json
{
    "body": "Thanks for fixing that for me!  John",
    "created_at": "2009-01-12T11:25:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4897",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4897#issuecomment-37070",
    "user": "https://github.com/JohnCremona"
}
```

Thanks for fixing that for me!  John
