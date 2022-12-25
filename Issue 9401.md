# Issue 9401: pari(n).isprime(1) does not give the primality certificate to the user

archive/issues_009401.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @JohnCremona @orlitzky wstein @robertwb\n\nKeywords: prime number\n\nThe Pari `isprime` function is able to return a primality\ncertificate:\n\n```\ngp: isprime(2^31-1,1)\n\n[2 3 1]\n\n[3 5 1]\n\n[7 3 1]\n\n[11 3 1]\n\n[31 2 1]\n\n[151 3 1]\n\n[331 3 1]\n```\n\nHowever when calling this function from Sage, the certificate is\nlost:\n\n```\nsage: pari(2^31-1).isprime(1)\nTrue\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9401\n\n",
    "created_at": "2010-07-01T08:12:38Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "pari(n).isprime(1) does not give the primality certificate to the user",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9401",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @aghitza

CC:  @JohnCremona @orlitzky wstein @robertwb

Keywords: prime number

The Pari `isprime` function is able to return a primality
certificate:

```
gp: isprime(2^31-1,1)

[2 3 1]

[3 5 1]

[7 3 1]

[11 3 1]

[31 2 1]

[151 3 1]

[331 3 1]
```

However when calling this function from Sage, the certificate is
lost:

```
sage: pari(2^31-1).isprime(1)
True
```


Issue created by migration from https://trac.sagemath.org/ticket/9401





---

archive/issue_comments_089428.json:
```json
{
    "body": "\n```\nsage: pari(3).isprime()\nTrue\nsage: pari(3).isprime(1)\nFalse\nsage: pari(3).isprime(2)\nTrue\n```\n\n\n...what?",
    "created_at": "2012-01-16T04:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89428",
    "user": "https://github.com/orlitzky"
}
```


```
sage: pari(3).isprime()
True
sage: pari(3).isprime(1)
False
sage: pari(3).isprime(2)
True
```


...what?



---

archive/issue_comments_089429.json:
```json
{
    "body": "apparently something changed (in worse) since I reported this, since indeed we now get:\n\n```\nsage: pari(2^31-1).isprime(1)\nFalse\n```\n\nI change the priority to \"major\".\n\nPaul",
    "created_at": "2012-01-16T07:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89429",
    "user": "https://github.com/zimmermann6"
}
```

apparently something changed (in worse) since I reported this, since indeed we now get:

```
sage: pari(2^31-1).isprime(1)
False
```

I change the priority to "major".

Paul



---

archive/issue_comments_089430.json:
```json
{
    "body": "by the way I notice there is no indication on how to access or change the \"arithmetic proof flag\" mentioned in the documentation of `n.is_prime`.\n\nAnd the documentation of `get_flag` is ill-formed in the terminal version.\n\nPaul",
    "created_at": "2013-08-24T13:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89430",
    "user": "https://github.com/zimmermann6"
}
```

by the way I notice there is no indication on how to access or change the "arithmetic proof flag" mentioned in the documentation of `n.is_prime`.

And the documentation of `get_flag` is ill-formed in the terminal version.

Paul



---

archive/issue_comments_089431.json:
```json
{
    "body": "for the ill-formed documentation of `get_flag`, see #15096.",
    "created_at": "2013-08-25T10:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89431",
    "user": "https://github.com/zimmermann6"
}
```

for the ill-formed documentation of `get_flag`, see #15096.



---

archive/issue_comments_089432.json:
```json
{
    "body": "Attachment [trac_9401.patch](tarball://root/attachments/some-uuid/ticket9401/trac_9401.patch) by @zimmermann6 created at 2013-08-25 12:45:08\n\nthe attached patch does several things:\n\n1) it fixes two typos in `gen.pyx`\n\n2) it corrects the behaviour of `pari(n).isprime(1)` which incorrectly was returning `False` for prime n\n\n3) for prime n, now `pari(n).isprime(1)` returns a tuple `(True, cert)` where `cert` is the primality certificate (currently as Pari object, I didn't figure out how to convert it to a Python object)\n\nComments are welcome.\n\nPaul",
    "created_at": "2013-08-25T12:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89432",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_9401.patch](tarball://root/attachments/some-uuid/ticket9401/trac_9401.patch) by @zimmermann6 created at 2013-08-25 12:45:08

the attached patch does several things:

1) it fixes two typos in `gen.pyx`

2) it corrects the behaviour of `pari(n).isprime(1)` which incorrectly was returning `False` for prime n

3) for prime n, now `pari(n).isprime(1)` returns a tuple `(True, cert)` where `cert` is the primality certificate (currently as Pari object, I didn't figure out how to convert it to a Python object)

Comments are welcome.

Paul



---

archive/issue_comments_089433.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-08-25T12:45:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89433",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089434.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-10-02T20:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89434",
    "user": "https://github.com/pjbruin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089435.json:
```json
{
    "body": "In principle OK, but needs to be rebased on #15124.\n\nAlso, it would be much cleaner to call `new_gen()` instead of initialising the `gen` and resetting the stack by hand:\n\n```python\ncdef GEN x\npari_catch_sig_on()\nx = gisprime(self.g, flag)\nif typ(x) != t_INT:\n    # case flag=1 with prime input: x is the certificate\n    return True, P.new_gen(x)\nelse:\n    pari_catch_sig_off()\n    return bool(signe(x))\n```\n",
    "created_at": "2013-10-02T20:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89435",
    "user": "https://github.com/pjbruin"
}
```

In principle OK, but needs to be rebased on #15124.

Also, it would be much cleaner to call `new_gen()` instead of initialising the `gen` and resetting the stack by hand:

```python
cdef GEN x
pari_catch_sig_on()
x = gisprime(self.g, flag)
if typ(x) != t_INT:
    # case flag=1 with prime input: x is the certificate
    return True, P.new_gen(x)
else:
    pari_catch_sig_off()
    return bool(signe(x))
```




---

archive/issue_comments_089436.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-03-01T16:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89436",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089437.json:
```json
{
    "body": "Rebased on 6.2.base2, applied comment:7 by pbruin\n----\nNew commits:",
    "created_at": "2014-03-01T16:37:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89437",
    "user": "https://github.com/rwst"
}
```

Rebased on 6.2.base2, applied comment:7 by pbruin
----
New commits:



---

archive/issue_comments_089438.json:
```json
{
    "body": "Only the last two commits apply. If I create a new branch without the first stray commits, will trac handle this?",
    "created_at": "2014-03-01T16:39:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89438",
    "user": "https://github.com/rwst"
}
```

Only the last two commits apply. If I create a new branch without the first stray commits, will trac handle this?



---

archive/issue_comments_089439.json:
```json
{
    "body": "Yes, this is no problem.  I did this (using `git rebase -i`) in the branch I just pushed, and made one trivial additional change (in Cython, `s != 0` turns out to be faster than `bool(s)`).  You can set this to `positive_review` if you are happy with this branch.",
    "created_at": "2014-03-01T17:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89439",
    "user": "https://github.com/pjbruin"
}
```

Yes, this is no problem.  I did this (using `git rebase -i`) in the branch I just pushed, and made one trivial additional change (in Cython, `s != 0` turns out to be faster than `bool(s)`).  You can set this to `positive_review` if you are happy with this branch.



---

archive/issue_comments_089440.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-03-02T07:17:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89440",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-03-05T09:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9401#issuecomment-89441",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_009558.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-03-05T09:36:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9401",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9401#event-9558"
}
```
