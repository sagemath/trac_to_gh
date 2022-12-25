# Issue 4670: prime_pi for input ~ 10^10 causes PariError

archive/issues_004670.json:
```json
{
    "body": "Assignee: @williamstein\n\nCalling the primepi function on a large pari integer (10^10) causes an error.  The issue is that in sage/libs/pari/gen.pyx the function init_primes casts the input to an unsigned long.  If we don't want to allow initialization with input bigger than this, we should give a better error.\n\n\nsage: prime_pi(10^10)\n\n---\nPariError                                 Traceback (most recent call last)\n\n/Users/Roed/Math/sage-3.2/<ipython console> in <module>()\n\n/Users/Roed/Math/sage-3.2/local/lib/python2.5/site-packages/sage/functions/transcendental.pyc in __call__(self, x)\n    363             from sage.rings.integer import Integer\n    364             pari.init_primes(pari(x)+Integer(1))\n--> 365             return ZZ(pari(x).primepi())\n    366 \n    367     def plot(self, xmin=0, xmax=100, *args, **kwds):\n\n/Users/Roed/Math/sage-3.2/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:37972)()\n\nPariError: impossible assignment I-->S (23)\n\nIssue created by migration from https://trac.sagemath.org/ticket/4670\n\n",
    "created_at": "2008-12-01T16:55:44Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "prime_pi for input ~ 10^10 causes PariError",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4670",
    "user": "https://github.com/roed314"
}
```
Assignee: @williamstein

Calling the primepi function on a large pari integer (10^10) causes an error.  The issue is that in sage/libs/pari/gen.pyx the function init_primes casts the input to an unsigned long.  If we don't want to allow initialization with input bigger than this, we should give a better error.


sage: prime_pi(10^10)

---
PariError                                 Traceback (most recent call last)

/Users/Roed/Math/sage-3.2/<ipython console> in <module>()

/Users/Roed/Math/sage-3.2/local/lib/python2.5/site-packages/sage/functions/transcendental.pyc in __call__(self, x)
    363             from sage.rings.integer import Integer
    364             pari.init_primes(pari(x)+Integer(1))
--> 365             return ZZ(pari(x).primepi())
    366 
    367     def plot(self, xmin=0, xmax=100, *args, **kwds):

/Users/Roed/Math/sage-3.2/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:37972)()

PariError: impossible assignment I-->S (23)

Issue created by migration from https://trac.sagemath.org/ticket/4670





---

archive/issue_events_010695.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-02T01:40:02Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4670#event-10695"
}
```



---

archive/issue_comments_035106.json:
```json
{
    "body": "Note also #3658.",
    "created_at": "2008-12-02T20:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35106",
    "user": "https://trac.sagemath.org/admin/accounts/users/fwclarke"
}
```

Note also #3658.



---

archive/issue_comments_035107.json:
```json
{
    "body": "ohanar is fixing this!",
    "created_at": "2009-01-15T22:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35107",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

ohanar is fixing this!



---

archive/issue_comments_035108.json:
```json
{
    "body": "Andrew Ohana's optimized Legendre prime_pi fixes this error.  The attached patch adds prime_pi(10**10) to the doctests of Andrew's code.  It may still be desired to give a better error in the PARI implementation.\n\n\nKevin Stueve",
    "created_at": "2010-01-18T00:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35108",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Andrew Ohana's optimized Legendre prime_pi fixes this error.  The attached patch adds prime_pi(10**10) to the doctests of Andrew's code.  It may still be desired to give a better error in the PARI implementation.


Kevin Stueve



---

archive/issue_comments_035109.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-18T00:25:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35109",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_035110.json:
```json
{
    "body": "added prime_pi(10**10) doctest",
    "created_at": "2010-01-18T01:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35110",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

added prime_pi(10**10) doctest



---

archive/issue_comments_035111.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-18T03:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35111",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_035112.json:
```json
{
    "body": "Attachment [4670.patch](tarball://root/attachments/some-uuid/ticket4670/4670.patch) by spancratz created at 2010-01-18 03:55:52\n\nThe patch above includes left overs from another patch.  I'll upload a new one now.",
    "created_at": "2010-01-18T03:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35112",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [4670.patch](tarball://root/attachments/some-uuid/ticket4670/4670.patch) by spancratz created at 2010-01-18 03:55:52

The patch above includes left overs from another patch.  I'll upload a new one now.



---

archive/issue_comments_035113.json:
```json
{
    "body": "Attachment [trac4670.patch](tarball://root/attachments/some-uuid/ticket4670/trac4670.patch) by spancratz created at 2010-01-18 03:56:41\n\nOnly the relevant lines from Kevin's patch",
    "created_at": "2010-01-18T03:56:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35113",
    "user": "https://trac.sagemath.org/admin/accounts/users/spancratz"
}
```

Attachment [trac4670.patch](tarball://root/attachments/some-uuid/ticket4670/trac4670.patch) by spancratz created at 2010-01-18 03:56:41

Only the relevant lines from Kevin's patch



---

archive/issue_events_010696.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-19T01:15:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4670#event-10696"
}
```



---

archive/issue_comments_035114.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T01:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4670#issuecomment-35114",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
