# Issue 4835: pari starts up without inititializing enough primes?

archive/issues_004835.json:
```json
{
    "body": "Assignee: tbd\n\nIn 3.2.2, this looks ok:\n\n```\nsage: pari.default(\"primelimit\")\n500000\n```\n\nbut nevertheless,\n\n```\nsage: K.<zeta>=CyclotomicField(23)\nsage: K.ideal(2).factor()\n...\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n...\nPariError: not enough precomputed primes, need primelimit ~  (35)\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4835\n\n",
    "created_at": "2008-12-20T12:05:51Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "pari starts up without inititializing enough primes?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4835",
    "user": "cremona"
}
```
Assignee: tbd

In 3.2.2, this looks ok:

```
sage: pari.default("primelimit")
500000
```

but nevertheless,

```
sage: K.<zeta>=CyclotomicField(23)
sage: K.ideal(2).factor()
...
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)
...
PariError: not enough precomputed primes, need primelimit ~  (35)
```



Issue created by migration from https://trac.sagemath.org/ticket/4835





---

archive/issue_comments_036641.json:
```json
{
    "body": "I have narrowed it down to here:\n\n```\nsage: K.<z> = CyclotomicField(23)\nsage: pK = K.pari_bnf(certify=False, units=True)\nsage: pK.bnfcertify()\n\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n---------------------------------------------------------------------------\nPariError                                 Traceback (most recent call last)\n\n/home/john/sage-3.2.2.rc1/<ipython console> in <module>()\n\n/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38663)()\n\nPariError: not enough precomputed primes, need primelimit ~  (35)\n\nsage: pari.default(\"primelimit\")\n500000\n```\n\nI uncommented line 6903 in sage/libs/pari/gen.pyx so I know that pari_init() was called with maxprime=500000 (the default) exactly once on startup and not again.  So the question in the ticket description seems to have a negative answer.\n\nHowever in a gp session (\"pari -gp\", so the same version) I get:\n\n```\n? bnfcertify(bnfinit(polcyclo(23),1))\n  *** bnfcertify: Warning: large Minkowski bound: certification will be VERY long.\n  *** bnfcertify: not enough precomputed primes, need primelimit ~ 9324407.\n```\n\nso perhaps pari really cannot certify this field with having all primes up to 9.3 million, and the problem is that the error message report the wrong value for some reason when called from within Sage.  This is confirmed by continuing the above Sage session like this:\n\n```\nsage: pari.init_primes(10^7)\nsage: pK.bnfcertify()\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n```\n\nfollowed by a long wait but no error message.",
    "created_at": "2008-12-20T12:52:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4835#issuecomment-36641",
    "user": "cremona"
}
```

I have narrowed it down to here:

```
sage: K.<z> = CyclotomicField(23)
sage: pK = K.pari_bnf(certify=False, units=True)
sage: pK.bnfcertify()

  ***   Warning: large Minkowski bound: certification will be VERY long.
---------------------------------------------------------------------------
PariError                                 Traceback (most recent call last)

/home/john/sage-3.2.2.rc1/<ipython console> in <module>()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/libs/pari/gen.so in sage.libs.pari.gen._pari_trap (sage/libs/pari/gen.c:38663)()

PariError: not enough precomputed primes, need primelimit ~  (35)

sage: pari.default("primelimit")
500000
```

I uncommented line 6903 in sage/libs/pari/gen.pyx so I know that pari_init() was called with maxprime=500000 (the default) exactly once on startup and not again.  So the question in the ticket description seems to have a negative answer.

However in a gp session ("pari -gp", so the same version) I get:

```
? bnfcertify(bnfinit(polcyclo(23),1))
  *** bnfcertify: Warning: large Minkowski bound: certification will be VERY long.
  *** bnfcertify: not enough precomputed primes, need primelimit ~ 9324407.
```

so perhaps pari really cannot certify this field with having all primes up to 9.3 million, and the problem is that the error message report the wrong value for some reason when called from within Sage.  This is confirmed by continuing the above Sage session like this:

```
sage: pari.init_primes(10^7)
sage: pK.bnfcertify()
  ***   Warning: large Minkowski bound: certification will be VERY long.
```

followed by a long wait but no error message.



---

archive/issue_comments_036642.json:
```json
{
    "body": "\n```\nsage: pari.init_primes(10^7)\nsage: pK.bnfcertify()\n  ***   Warning: large Minkowski bound: certification will be VERY long.\n```\n\n> followed by a long wait(*) but no error message.\n\n3h 20m later:\n\n```\n1\n```\n",
    "created_at": "2008-12-20T16:35:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4835#issuecomment-36642",
    "user": "cremona"
}
```


```
sage: pari.init_primes(10^7)
sage: pK.bnfcertify()
  ***   Warning: large Minkowski bound: certification will be VERY long.
```

> followed by a long wait(*) but no error message.

3h 20m later:

```
1
```




---

archive/issue_comments_036643.json:
```json
{
    "body": "Changing component from algebra to interfaces.",
    "created_at": "2009-07-11T11:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4835#issuecomment-36643",
    "user": "AlexGhitza"
}
```

Changing component from algebra to interfaces.



---

archive/issue_comments_036644.json:
```json
{
    "body": "Changing assignee from tbd to was.",
    "created_at": "2009-07-11T11:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4835#issuecomment-36644",
    "user": "AlexGhitza"
}
```

Changing assignee from tbd to was.



---

archive/issue_comments_036645.json:
```json
{
    "body": "This issue does not appear anymore after upgrading PARI (ticket #9343), so I'm marking this invalid/duplicate/wontfix.",
    "created_at": "2010-08-02T07:38:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4835#issuecomment-36645",
    "user": "jdemeyer"
}
```

This issue does not appear anymore after upgrading PARI (ticket #9343), so I'm marking this invalid/duplicate/wontfix.



---

archive/issue_comments_036646.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-09-08T08:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4835#issuecomment-36646",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036647.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-09-10T10:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4835",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4835#issuecomment-36647",
    "user": "mpatel"
}
```

Resolution: duplicate
