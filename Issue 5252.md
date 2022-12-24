# Issue 5252: elliptic curves: P.height() lies about its precision

archive/issues_005252.json:
```json
{
    "body": "Assignee: @williamstein\n\nThis is a bit weird because it seems to only happen with some elliptic curves.\n\nAnyway, here's the example:\n\n```\nsage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])\nsage: P = E([-30987785091199, 258909576181697016447])\nsage: P.height()               # default precision: 53 bits\nsage: P.height(precision=100)  # new precision: 100 bits\n25.860317067546190744967149477\nsage: P.height(precision=250)  # new precision: 250 bits\n25.860317067546190744967149477417933667311444878578186035156250000000000000\n```\n\n\nI don't believe for a second that all the zeroes in the last example are correct.  In fact, if you increase the precision to 1000 bits you only get more zeroes.\n\nThere must be \"simpler\" elliptic curves for which this happens, and I'll try to find some.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5252\n\n",
    "created_at": "2009-02-13T04:05:11Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "elliptic curves: P.height() lies about its precision",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5252",
    "user": "@aghitza"
}
```
Assignee: @williamstein

This is a bit weird because it seems to only happen with some elliptic curves.

Anyway, here's the example:

```
sage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])
sage: P = E([-30987785091199, 258909576181697016447])
sage: P.height()               # default precision: 53 bits
sage: P.height(precision=100)  # new precision: 100 bits
25.860317067546190744967149477
sage: P.height(precision=250)  # new precision: 250 bits
25.860317067546190744967149477417933667311444878578186035156250000000000000
```


I don't believe for a second that all the zeroes in the last example are correct.  In fact, if you increase the precision to 1000 bits you only get more zeroes.

There must be "simpler" elliptic curves for which this happens, and I'll try to find some.


Issue created by migration from https://trac.sagemath.org/ticket/5252





---

archive/issue_comments_040302.json:
```json
{
    "body": "Running this example in a native GP session works fine, so the problem is either in Sage or in the way Sage communicates with the Pari library.",
    "created_at": "2009-02-13T05:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5252#issuecomment-40302",
    "user": "@aghitza"
}
```

Running this example in a native GP session works fine, so the problem is either in Sage or in the way Sage communicates with the Pari library.



---

archive/issue_comments_040303.json:
```json
{
    "body": "Attachment [trac_5252.patch](tarball://root/attachments/some-uuid/ticket5252/trac_5252.patch) by @JohnCremona created at 2009-02-15 17:29:49\n\nAlex, I think that the ellheight() function needs to be given the precision parameter, despite what it says in the docstring for that function:\n\n```\nsage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])\nsage: P = E([-30987785091199, 258909576181697016447])\nsage: PE = E.pari_curve(prec=500)\nsage: PE.ellheight([P[0],P[1],P[2]]).python()\n25.8603170675461907\nsage: PE.ellheight([P[0],P[1],P[2]],precision=500).python()\n25.8603170675461907438688407407351103230988729038444162155771710417835725129551130570889813281792157278507639909972112856019190236125362914195452321719909\n```\n\n(Here I output the .python() conversion since otherwise it uses the gp default precision for output so you cannot see what is going on).\n\nAfter my patch, your example works fine:\n\n```\nsage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])\nsage: P = E([-30987785091199, 258909576181697016447])\nsage: P.height()\n25.8603170675462\nsage: P.height(precision=100)\n25.860317067546190743868840741\nsage: P.height(precision=250)\n25.860317067546190743868840740735110323098872903844416215577171041783572513\nsage: P.height(precision=500)\n25.8603170675461907438688407407351103230988729038444162155771710417835725129551130570889813281792157278507639909972112856019190236125362914195452321720\n```\n\n\nThe patch (based on 3.3.rc0) corrects height(), adds a doctest, and corrects the docstring in gen.pyx.  I also had to correct a doctest output in ell_rational_field.py.\n\nNB The output at precision 500 for the new doctest looks odd on trac but is ok in the source file.",
    "created_at": "2009-02-15T17:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5252#issuecomment-40303",
    "user": "@JohnCremona"
}
```

Attachment [trac_5252.patch](tarball://root/attachments/some-uuid/ticket5252/trac_5252.patch) by @JohnCremona created at 2009-02-15 17:29:49

Alex, I think that the ellheight() function needs to be given the precision parameter, despite what it says in the docstring for that function:

```
sage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])
sage: P = E([-30987785091199, 258909576181697016447])
sage: PE = E.pari_curve(prec=500)
sage: PE.ellheight([P[0],P[1],P[2]]).python()
25.8603170675461907
sage: PE.ellheight([P[0],P[1],P[2]],precision=500).python()
25.8603170675461907438688407407351103230988729038444162155771710417835725129551130570889813281792157278507639909972112856019190236125362914195452321719909
```

(Here I output the .python() conversion since otherwise it uses the gp default precision for output so you cannot see what is going on).

After my patch, your example works fine:

```
sage: E = EllipticCurve([1, -1, 1, -2063758701246626370773726978, 32838647793306133075103747085833809114881])
sage: P = E([-30987785091199, 258909576181697016447])
sage: P.height()
25.8603170675462
sage: P.height(precision=100)
25.860317067546190743868840741
sage: P.height(precision=250)
25.860317067546190743868840740735110323098872903844416215577171041783572513
sage: P.height(precision=500)
25.8603170675461907438688407407351103230988729038444162155771710417835725129551130570889813281792157278507639909972112856019190236125362914195452321720
```


The patch (based on 3.3.rc0) corrects height(), adds a doctest, and corrects the docstring in gen.pyx.  I also had to correct a doctest output in ell_rational_field.py.

NB The output at precision 500 for the new doctest looks odd on trac but is ok in the source file.



---

archive/issue_comments_040304.json:
```json
{
    "body": "Excellent work, John!",
    "created_at": "2009-02-16T08:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5252#issuecomment-40304",
    "user": "@aghitza"
}
```

Excellent work, John!



---

archive/issue_comments_040305.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-16T08:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5252#issuecomment-40305",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040306.json:
```json
{
    "body": "Merged in Sage 3.3.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-16T08:30:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5252",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5252#issuecomment-40306",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.rc1.

Cheers,

Michael
