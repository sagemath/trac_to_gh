# Issue 4290: stopgap function to turn plane curves of genus one into elliptic curves

archive/issues_004290.json:
```json
{
    "body": "Assignee: was\n\nThis is a function to turn plane curves of genus 1 with a known point into objects of type EllipticCurve. It relies on MAGMA (as does EllipticCurve_from_cubic) but will add a little functionality. Here is an example of how it works:\n\n\n```\nsage: x,y,z=MPolynomialRing(QQ,Integer(3),'xyz').gens() # optional\nsage: C=Curve(x^4+x^2*y^2-z^4) \nsage: P=C(1,0,1) \nsage: E=EllipticCurve_from_plane_curve(C,P) \nsage: E \nElliptic Curve defined by y^2  = x^3 + 4*x over Rational Field\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4290\n\n",
    "created_at": "2008-10-14T22:39:08Z",
    "labels": [
        "algebraic geometry",
        "minor",
        "bug"
    ],
    "title": "stopgap function to turn plane curves of genus one into elliptic curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4290",
    "user": "ljpk"
}
```
Assignee: was

This is a function to turn plane curves of genus 1 with a known point into objects of type EllipticCurve. It relies on MAGMA (as does EllipticCurve_from_cubic) but will add a little functionality. Here is an example of how it works:


```
sage: x,y,z=MPolynomialRing(QQ,Integer(3),'xyz').gens() # optional
sage: C=Curve(x^4+x^2*y^2-z^4) 
sage: P=C(1,0,1) 
sage: E=EllipticCurve_from_plane_curve(C,P) 
sage: E 
Elliptic Curve defined by y^2  = x^3 + 4*x over Rational Field
```



Issue created by migration from https://trac.sagemath.org/ticket/4290





---

archive/issue_comments_031399.json:
```json
{
    "body": "Attachment [EllipticCurve_from_plane_curve.sage](tarball://root/attachments/some-uuid/ticket4290/EllipticCurve_from_plane_curve.sage) by ljpk created at 2008-10-14 22:39:46\n\nimplementation of EllipticCurve_from_plane_curve",
    "created_at": "2008-10-14T22:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31399",
    "user": "ljpk"
}
```

Attachment [EllipticCurve_from_plane_curve.sage](tarball://root/attachments/some-uuid/ticket4290/EllipticCurve_from_plane_curve.sage) by ljpk created at 2008-10-14 22:39:46

implementation of EllipticCurve_from_plane_curve



---

archive/issue_comments_031400.json:
```json
{
    "body": "Changing assignee from was to craigcitro.",
    "created_at": "2008-10-14T22:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31400",
    "user": "ljpk"
}
```

Changing assignee from was to craigcitro.



---

archive/issue_comments_031401.json:
```json
{
    "body": "The \"patch\" isn't a patch, it's just a function defined in Sage. Secondly, there is already a function that does almost the same as this in sage/schemes/elliptic_curves/constructor.py .\n\nSo what needs to be done (Lloyd!) is to (1) Explain briefly how this function differs from the existing one, and why it is better, and also (2) actually make a patch.\n\nIf Lloyd convinces me of  (1) then I'll happily do (2).",
    "created_at": "2008-11-04T17:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31401",
    "user": "cremona"
}
```

The "patch" isn't a patch, it's just a function defined in Sage. Secondly, there is already a function that does almost the same as this in sage/schemes/elliptic_curves/constructor.py .

So what needs to be done (Lloyd!) is to (1) Explain briefly how this function differs from the existing one, and why it is better, and also (2) actually make a patch.

If Lloyd convinces me of  (1) then I'll happily do (2).



---

archive/issue_comments_031402.json:
```json
{
    "body": "The current Sage function only converts cubics into elliptic curves, but MAGMA can do quite a bit more than that. My function can also cope with other genus one curves such as x<sup>4+x</sup>2*y<sup>2-z</sup>4 which is not cubic. Possibly the current function should be tweaked slightly so that it can do both cubic and non-cubic examples.",
    "created_at": "2008-11-24T11:20:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31402",
    "user": "ljpk"
}
```

The current Sage function only converts cubics into elliptic curves, but MAGMA can do quite a bit more than that. My function can also cope with other genus one curves such as x<sup>4+x</sup>2*y<sup>2-z</sup>4 which is not cubic. Possibly the current function should be tweaked slightly so that it can do both cubic and non-cubic examples.



---

archive/issue_comments_031403.json:
```json
{
    "body": "Anything going on with this patch? It has been sitting around for 4 months :(.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-06T06:01:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31403",
    "user": "mabshoff"
}
```

Anything going on with this patch? It has been sitting around for 4 months :(.

Cheers,

Michael



---

archive/issue_comments_031404.json:
```json
{
    "body": "Patch based on the above, based on 3.4.1.rc0",
    "created_at": "2009-04-06T10:07:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31404",
    "user": "cremona"
}
```

Patch based on the above, based on 3.4.1.rc0



---

archive/issue_comments_031405.json:
```json
{
    "body": "Attachment [trac_4290.patch](tarball://root/attachments/some-uuid/ticket4290/trac_4290.patch) by cremona created at 2009-04-06 10:14:49\n\nI have made a proper patch based on Lloyd's function (based on 3.4.1.rc0), which also fixes his function so that it works when the variable names are something other than 'x','y','z' (which it did not before).\n\nYou might think that this function makes the existing EllipicCurve_from_cubic redundant;  it nearly does, but that function takes a homogeneous polynomial while this one takes an actual curve.  It would probably be better to combine these when all this is rewritten in Sage.\n\nI added the new function to all.py so that it is in the global namespace.  I am not sure what the convention is here, given that it is an optional-only function requiring magma!  Also I have nto tested my patch o na machine without magma since I don't have one handy :)",
    "created_at": "2009-04-06T10:14:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31405",
    "user": "cremona"
}
```

Attachment [trac_4290.patch](tarball://root/attachments/some-uuid/ticket4290/trac_4290.patch) by cremona created at 2009-04-06 10:14:49

I have made a proper patch based on Lloyd's function (based on 3.4.1.rc0), which also fixes his function so that it works when the variable names are something other than 'x','y','z' (which it did not before).

You might think that this function makes the existing EllipicCurve_from_cubic redundant;  it nearly does, but that function takes a homogeneous polynomial while this one takes an actual curve.  It would probably be better to combine these when all this is rewritten in Sage.

I added the new function to all.py so that it is in the global namespace.  I am not sure what the convention is here, given that it is an optional-only function requiring magma!  Also I have nto tested my patch o na machine without magma since I don't have one handy :)



---

archive/issue_comments_031406.json:
```json
{
    "body": "The doctests should be marked:\n\n```\n   # optional - magma\n```\n\nso when one does\n\n```\n  sage -t -only_optional=magma\n```\n\nthey get run.",
    "created_at": "2009-04-12T02:56:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31406",
    "user": "was"
}
```

The doctests should be marked:

```
   # optional - magma
```

so when one does

```
  sage -t -only_optional=magma
```

they get run.



---

archive/issue_comments_031407.json:
```json
{
    "body": "Replaces previous; rebased to 4.0.1",
    "created_at": "2009-06-11T20:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31407",
    "user": "cremona"
}
```

Replaces previous; rebased to 4.0.1



---

archive/issue_comments_031408.json:
```json
{
    "body": "Attachment [trac_4290-rebase.patch](tarball://root/attachments/some-uuid/ticket4290/trac_4290-rebase.patch) by cremona created at 2009-06-11 20:39:20\n\nThe new patch replaces previous ones.  It marks the doctests as William asked;  testing then revealed bugs which have been fixed.  Also rebased to 4.0.1 and the docstrings properly ReSTified to the reference manual page looks good.",
    "created_at": "2009-06-11T20:39:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31408",
    "user": "cremona"
}
```

Attachment [trac_4290-rebase.patch](tarball://root/attachments/some-uuid/ticket4290/trac_4290-rebase.patch) by cremona created at 2009-06-11 20:39:20

The new patch replaces previous ones.  It marks the doctests as William asked;  testing then revealed bugs which have been fixed.  Also rebased to 4.0.1 and the docstrings properly ReSTified to the reference manual page looks good.



---

archive/issue_comments_031409.json:
```json
{
    "body": "Works well for me.  Pity it requires magma :(",
    "created_at": "2009-06-15T19:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31409",
    "user": "ncalexan"
}
```

Works well for me.  Pity it requires magma :(



---

archive/issue_comments_031410.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-24T10:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4290#issuecomment-31410",
    "user": "rlm"
}
```

Resolution: fixed
