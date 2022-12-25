# Issue 5346: Sage 3.3: schemes/elliptic_curves/ell_rational_field.py fails to doctest with optional database installed

archive/issues_005346.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @JohnCremona\n\nReported by Jan Groenewald in http://groups.google.com/group/sage-devel/browse_thread/thread/d5db5c25fbce1e99\n\n```\nsage -t  \"devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\"\n**********************************************************************\nFile \"/usr/local/src/sage-3.3/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py\", line 2675:\n    sage: E.cremona_label()\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field.\nGot:\n    '10351a1'\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5346\n\n",
    "created_at": "2009-02-23T07:34:07Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "Sage 3.3: schemes/elliptic_curves/ell_rational_field.py fails to doctest with optional database installed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5346",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: @williamstein

CC:  @JohnCremona

Reported by Jan Groenewald in http://groups.google.com/group/sage-devel/browse_thread/thread/d5db5c25fbce1e99

```
sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"
**********************************************************************
File "/usr/local/src/sage-3.3/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py", line 2675:
    sage: E.cremona_label()
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y + 3*y = x^3 + 2*x^2 + 4*x + 5 over Rational Field.
Got:
    '10351a1'
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/5346





---

archive/issue_comments_041111.json:
```json
{
    "body": "This problem is ironically introduced by having database_cremona_ellcurve-20071019.spkg installed :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-23T08:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41111",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This problem is ironically introduced by having database_cremona_ellcurve-20071019.spkg installed :)

Cheers,

Michael



---

archive/issue_comments_041112.json:
```json
{
    "body": "For the record:\n\nThe optional database covers conductor ranges from 10000 to 130000 AFAIK. So an obviously working patch (to be tested ...) already discussed elsewhere (I don't remember exactly who had this idea first, it wasn't me) would be to exchange the curve with conductor 10351 in the doctest, with a curve having conductor bigger than 130000.\n\nCheers,\ngsw",
    "created_at": "2009-03-26T23:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41112",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

For the record:

The optional database covers conductor ranges from 10000 to 130000 AFAIK. So an obviously working patch (to be tested ...) already discussed elsewhere (I don't remember exactly who had this idea first, it wasn't me) would be to exchange the curve with conductor 10351 in the doctest, with a curve having conductor bigger than 130000.

Cheers,
gsw



---

archive/issue_comments_041113.json:
```json
{
    "body": "Replying to [comment:2 GeorgSWeber]:\n> For the record:\n> \n> The optional database covers conductor ranges from 10000 to 130000 AFAIK. So an obviously working patch (to be tested ...) already discussed elsewhere (I don't remember exactly who had this idea first, it wasn't me) would be to exchange the curve with conductor 10351 in the doctest, with a curve having conductor bigger than 130000.\n\nI agree, and suggest\n\n```\nsage: E = EllipticCurve([1, -1, 0, -79, 289]) \nsage: E.cremona_label()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/home/john/.sage/temp/ubuntu/1126/_home_john__sage_init_sage_0.py in <module>()\n\n/home/john/sage-3.4/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in cremona_label(self, space)\n   3034                 X = self.database_curve()\n   3035             except RuntimeError:\n-> 3036                 raise RuntimeError, \"Cremona label not known for %s.\"%self\n   3037             self.__cremona_label = X.__cremona_label\n   3038             return self.cremona_label(space)\n\nRuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 79*x + 289 over Rational Field.\n```\n\nas that curve will one day have label 234446a1 (or b1 or c1, I forget).\n\n\n> \n> Cheers,\n> gsw",
    "created_at": "2009-03-27T08:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41113",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 GeorgSWeber]:
> For the record:
> 
> The optional database covers conductor ranges from 10000 to 130000 AFAIK. So an obviously working patch (to be tested ...) already discussed elsewhere (I don't remember exactly who had this idea first, it wasn't me) would be to exchange the curve with conductor 10351 in the doctest, with a curve having conductor bigger than 130000.

I agree, and suggest

```
sage: E = EllipticCurve([1, -1, 0, -79, 289]) 
sage: E.cremona_label()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/john/.sage/temp/ubuntu/1126/_home_john__sage_init_sage_0.py in <module>()

/home/john/sage-3.4/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/ell_rational_field.pyc in cremona_label(self, space)
   3034                 X = self.database_curve()
   3035             except RuntimeError:
-> 3036                 raise RuntimeError, "Cremona label not known for %s."%self
   3037             self.__cremona_label = X.__cremona_label
   3038             return self.cremona_label(space)

RuntimeError: Cremona label not known for Elliptic Curve defined by y^2 + x*y = x^3 - x^2 - 79*x + 289 over Rational Field.
```

as that curve will one day have label 234446a1 (or b1 or c1, I forget).


> 
> Cheers,
> gsw



---

archive/issue_comments_041114.json:
```json
{
    "body": "Apply to 3.4.1",
    "created_at": "2009-04-23T09:19:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41114",
    "user": "https://github.com/JohnCremona"
}
```

Apply to 3.4.1



---

archive/issue_comments_041115.json:
```json
{
    "body": "Attachment [trac_5346.patch](tarball://root/attachments/some-uuid/ticket5346/trac_5346.patch) by @JohnCremona created at 2009-04-23 09:22:06\n\nThe patch cahnges taht example to the one with condictor 234446 as I suggested.\n\nIt also make another doctest work ok with & without the database (at line 4941) by hard-wiring in some points instead of getting the gens.\n\nI tested this on sage-3.4.1 with & without the database installed.",
    "created_at": "2009-04-23T09:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41115",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_5346.patch](tarball://root/attachments/some-uuid/ticket5346/trac_5346.patch) by @JohnCremona created at 2009-04-23 09:22:06

The patch cahnges taht example to the one with condictor 234446 as I suggested.

It also make another doctest work ok with & without the database (at line 4941) by hard-wiring in some points instead of getting the gens.

I tested this on sage-3.4.1 with & without the database installed.



---

archive/issue_comments_041116.json:
```json
{
    "body": "Thanks for taking care of this John. Doctests pass, pass reads good and fixes the problem. Positve review.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41116",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Thanks for taking care of this John. Doctests pass, pass reads good and fixes the problem. Positve review.

Cheers,

Michael



---

archive/issue_comments_041117.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T08:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41117",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012472.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-24T08:27:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5346#event-12472"
}
```



---

archive/issue_events_012473.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-24T08:27:50Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5346#event-12473"
}
```



---

archive/issue_comments_041118.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5346",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5346#issuecomment-41118",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael
