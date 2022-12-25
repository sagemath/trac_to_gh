# Issue 1785: bug in creating points on elliptic curves over extension fields

archive/issues_001785.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  alexghitza\n\n\n```\n\n\nOn Jan 15, 2008 10:25 AM, John Cremona <john.cremona@gmail.com> wrote:\n> \n> I like Robert's suggestion.  If the user wants n independent generic\n> points, construct a large enough field (transcendence degree n) to\n> contain them.\n> \n> A useful change Magma made relatively recently (a couple of years or\n> so ago) was to aloow points on an elliptic curve to have coordinates\n> in an extension of the base field of the curve -- as one would when\n> working mathematically.  e.g. given a curve defined over QQ you can\n> define points on E(K) for e.g. K=a number field, or K=a function field\n> (such as the function field of E, to get a generic point).  Of course,\n> these points \"know\" what their curve is so you can do point arithmetic\n> on them and so on.\n> \n> I don't see why this should be workable in Sage too (maybe it is\n> already?  if so I will retire shame-faced from the discussion...)\n\nIt's sort of half-way there.  You can do:\n\nsage: K.<a> = NumberField(x^2 + x - (3^3-3))\nsage: E = EllipticCurve('37a')\nsage: X = E(K)\n\nbut stupidly X is wrong:\n\nsage: X\nAbelian group of points on Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field\n\nthough:\n\nsage: X.domain()\nSpectrum of Number Field in a with defining polynomial x^2 + x - 24\n\nHowever, \n\nsage: P = X([3,a]);\nboom with a TypeError\n\nSo this obviously needs work.  In fact, this counts as a bug.\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1785\n\n",
    "created_at": "2008-01-15T19:10:31Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "bug in creating points on elliptic curves over extension fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1785",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  alexghitza


```


On Jan 15, 2008 10:25 AM, John Cremona <john.cremona@gmail.com> wrote:
> 
> I like Robert's suggestion.  If the user wants n independent generic
> points, construct a large enough field (transcendence degree n) to
> contain them.
> 
> A useful change Magma made relatively recently (a couple of years or
> so ago) was to aloow points on an elliptic curve to have coordinates
> in an extension of the base field of the curve -- as one would when
> working mathematically.  e.g. given a curve defined over QQ you can
> define points on E(K) for e.g. K=a number field, or K=a function field
> (such as the function field of E, to get a generic point).  Of course,
> these points "know" what their curve is so you can do point arithmetic
> on them and so on.
> 
> I don't see why this should be workable in Sage too (maybe it is
> already?  if so I will retire shame-faced from the discussion...)

It's sort of half-way there.  You can do:

sage: K.<a> = NumberField(x^2 + x - (3^3-3))
sage: E = EllipticCurve('37a')
sage: X = E(K)

but stupidly X is wrong:

sage: X
Abelian group of points on Elliptic Curve defined by y^2 + y = x^3 - x over Rational Field

though:

sage: X.domain()
Spectrum of Number Field in a with defining polynomial x^2 + x - 24

However, 

sage: P = X([3,a]);
boom with a TypeError

So this obviously needs work.  In fact, this counts as a bug.

```


Issue created by migration from https://trac.sagemath.org/ticket/1785





---

archive/issue_comments_011271.json:
```json
{
    "body": "Attachment [1785-ell_point_ext.patch](tarball://root/attachments/some-uuid/ticket1785/1785-ell_point_ext.patch) by @aghitza created at 2008-09-07 07:29:44",
    "created_at": "2008-09-07T07:29:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1785#issuecomment-11271",
    "user": "https://github.com/aghitza"
}
```

Attachment [1785-ell_point_ext.patch](tarball://root/attachments/some-uuid/ticket1785/1785-ell_point_ext.patch) by @aghitza created at 2008-09-07 07:29:44



---

archive/issue_comments_011272.json:
```json
{
    "body": "See the patch (made against 3.1.2.rc0).",
    "created_at": "2008-09-07T07:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1785#issuecomment-11272",
    "user": "https://github.com/aghitza"
}
```

See the patch (made against 3.1.2.rc0).



---

archive/issue_comments_011273.json:
```json
{
    "body": "Review:  Amazing 2-line fix!  Patch applies fine and all doctests in sage.schemes.elliptic_curves pass.  This will be very useful.",
    "created_at": "2008-09-08T18:57:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1785#issuecomment-11273",
    "user": "https://github.com/JohnCremona"
}
```

Review:  Amazing 2-line fix!  Patch applies fine and all doctests in sage.schemes.elliptic_curves pass.  This will be very useful.



---

archive/issue_comments_011274.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-08T20:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1785#issuecomment-11274",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011275.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc1",
    "created_at": "2008-09-08T20:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1785#issuecomment-11275",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc1



---

archive/issue_events_001942.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-09-08T20:21:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1785",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1785#event-1942"
}
```
