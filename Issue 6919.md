# Issue 6919: basic arithmetic using FLINT is broken (very serious!)

archive/issues_006919.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  wbhart @burcin\n\nMariah Lenox reported:\n\n```\nR.<x> = PolynomialRing(ZZ)\nA = 2^(2^17+2^15)  # note the 2 rather than the \"s\"\na = A * x^31\nb = (A * x) * x^30\na == b   # prints \"False\" ???\n```\n\nBut\n\n```\nR.<x> = PolynomialRing(ZZ, implementation='NTL')\nA = 2^(2^17+2^15)  # note the 2 rather than the \"s\"\na = A * (x^31)\nb = A * x * (x^30)\na == b   \n```\ngives True.  So this is definitely either a bug in FLINT (highly likely), or a bug in our wrapper (much less likely, since our wrapper is so generic:\n\n```\ncpdef RingElement _mul_(self, RingElement right):\n    r\"\"\"\n    Returns self multiplied by right.\n\n    EXAMPLES::\n\n        sage: R.<x> = PolynomialRing(ZZ)\n        sage: (x - 2)*(x^2 - 8*x + 16)\n        x^3 - 10*x^2 + 32*x - 32\n    \"\"\"\n    cdef Polynomial_integer_dense_flint x = self._new()\n    _sig_on\n    fmpz_poly_mul(x.__poly, self.__poly,\n            (<Polynomial_integer_dense_flint>right).__poly)\n    _sig_off\n    return x\n```\n}}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/6919\n\n",
    "created_at": "2009-09-10T18:56:51Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "basic arithmetic using FLINT is broken (very serious!)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6919",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

CC:  wbhart @burcin

Mariah Lenox reported:

```
R.<x> = PolynomialRing(ZZ)
A = 2^(2^17+2^15)  # note the 2 rather than the "s"
a = A * x^31
b = (A * x) * x^30
a == b   # prints "False" ???
```

But

```
R.<x> = PolynomialRing(ZZ, implementation='NTL')
A = 2^(2^17+2^15)  # note the 2 rather than the "s"
a = A * (x^31)
b = A * x * (x^30)
a == b   
```
gives True.  So this is definitely either a bug in FLINT (highly likely), or a bug in our wrapper (much less likely, since our wrapper is so generic:

```
cpdef RingElement _mul_(self, RingElement right):
    r"""
    Returns self multiplied by right.

    EXAMPLES::

        sage: R.<x> = PolynomialRing(ZZ)
        sage: (x - 2)*(x^2 - 8*x + 16)
        x^3 - 10*x^2 + 32*x - 32
    """
    cdef Polynomial_integer_dense_flint x = self._new()
    _sig_on
    fmpz_poly_mul(x.__poly, self.__poly,
            (<Polynomial_integer_dense_flint>right).__poly)
    _sig_off
    return x
```
}}}

Issue created by migration from https://trac.sagemath.org/ticket/6919





---

archive/issue_comments_057011.json:
```json
{
    "body": "```\nBill Hart <goodwillhart@googlemail.com> wrote:\n<snip>\n> It was caused by a bug in the FLINT FFT (the first ever found). I\n> tracked the bug down to a specific piece of code and David Harvey has\n> supplied a fix. There will be a new version of FLINT to patch this\n> bug.\n```",
    "created_at": "2009-09-16T13:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57011",
    "user": "https://github.com/burcin"
}
```

```
Bill Hart <goodwillhart@googlemail.com> wrote:
<snip>
> It was caused by a bug in the FLINT FFT (the first ever found). I
> tracked the bug down to a specific piece of code and David Harvey has
> supplied a fix. There will be a new version of FLINT to patch this
> bug.
```



---

archive/issue_comments_057012.json:
```json
{
    "body": "Attachment [trac_6919.patch](tarball://root/attachments/some-uuid/ticket6919/trac_6919.patch) by @mwhansen created at 2009-09-25 04:10:07",
    "created_at": "2009-09-25T04:10:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57012",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6919.patch](tarball://root/attachments/some-uuid/ticket6919/trac_6919.patch) by @mwhansen created at 2009-09-25 04:10:07



---

archive/issue_comments_057013.json:
```json
{
    "body": "I've attached a patch which makes sure that this bug is indeed fixed by FLINT 1.5.0.  The spkg can be found at http://sage.math.washington.edu/home/mhansen/flint-1.5.0.p0.spkg .  This spkg is based of 1.3.0.p3 that Ondrej did.",
    "created_at": "2009-09-25T04:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57013",
    "user": "https://github.com/mwhansen"
}
```

I've attached a patch which makes sure that this bug is indeed fixed by FLINT 1.5.0.  The spkg can be found at http://sage.math.washington.edu/home/mhansen/flint-1.5.0.p0.spkg .  This spkg is based of 1.3.0.p3 that Ondrej did.



---

archive/issue_comments_057014.json:
```json
{
    "body": "I posted another spkg that adds one critical Cygwin fix, namely naming the library libflint.dll instead of libflint.so:\n\nhttp://sage.math.washington.edu/home/wstein/patches/flint-1.5.0.p1.spkg\n\nIt's based exactly on mhansen's spkg.",
    "created_at": "2009-09-26T01:21:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57014",
    "user": "https://github.com/williamstein"
}
```

I posted another spkg that adds one critical Cygwin fix, namely naming the library libflint.dll instead of libflint.so:

http://sage.math.washington.edu/home/wstein/patches/flint-1.5.0.p1.spkg

It's based exactly on mhansen's spkg.



---

archive/issue_comments_057015.json:
```json
{
    "body": "OS X 10.5, both 32-bit and 64-bit: first I applied the patch.  This produced the doctest failure described in the ticket for the file libs/flint/flint.pyx.  Then I did 'sage -f flint...' to install the new spkg .  Then this file passed doctests.",
    "created_at": "2009-09-26T04:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57015",
    "user": "https://github.com/jhpalmieri"
}
```

OS X 10.5, both 32-bit and 64-bit: first I applied the patch.  This produced the doctest failure described in the ticket for the file libs/flint/flint.pyx.  Then I did 'sage -f flint...' to install the new spkg .  Then this file passed doctests.



---

archive/issue_comments_057016.json:
```json
{
    "body": "New FLINT package up at\n\nhttp://sage.math.washington.edu/home/mvngu/release/spkg/standard/flint-1.5.0.p2.spkg\n\nThe only change from .p1 is:\n\n* Check in all changes in wstein's name.",
    "created_at": "2009-09-27T01:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57016",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

New FLINT package up at

http://sage.math.washington.edu/home/mvngu/release/spkg/standard/flint-1.5.0.p2.spkg

The only change from .p1 is:

* Check in all changes in wstein's name.



---

archive/issue_comments_057017.json:
```json
{
    "body": "See palmieri's and my reports at #6849.",
    "created_at": "2009-09-27T03:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See palmieri's and my reports at #6849.



---

archive/issue_events_016251.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-27T03:40:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6919#event-16251"
}
```



---

archive/issue_comments_057018.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-27T03:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57018",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_057019.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T11:03:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6919",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6919#issuecomment-57019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
