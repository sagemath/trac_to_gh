# Issue 7819: RealInterval(+infinity,+infinity).is_int() blows up

archive/issues_007819.json:
```json
{
    "body": "Assignee: @aghitza\n\n```\nsage: RealInterval(+infinity,+infinity).is_int()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/rlmill/.sage/temp/rlm_book.local/9535/_Users_rlmill__sage_init_sage_0.py in <module>()\n\n/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/rings/real_mpfi.so in sage.rings.real_mpfi.RealIntervalFieldElement.is_int (sage/rings/real_mpfi.c:16689)()\n\n/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.ceil (sage/rings/real_mpfr.c:14488)()\n\nValueError: Calling ceil() on infinity or NaN\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7819\n\n",
    "created_at": "2010-01-02T15:02:56Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "RealInterval(+infinity,+infinity).is_int() blows up",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7819",
    "user": "https://github.com/rlmill"
}
```
Assignee: @aghitza

```
sage: RealInterval(+infinity,+infinity).is_int()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/9535/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/rings/real_mpfi.so in sage.rings.real_mpfi.RealIntervalFieldElement.is_int (sage/rings/real_mpfi.c:16689)()

/Users/rlmill/sage-4.3/local/lib/python2.6/site-packages/sage/rings/real_mpfr.so in sage.rings.real_mpfr.RealNumber.ceil (sage/rings/real_mpfr.c:14488)()

ValueError: Calling ceil() on infinity or NaN
```

Issue created by migration from https://trac.sagemath.org/ticket/7819





---

archive/issue_comments_067556.json:
```json
{
    "body": "Attachment [trac_7819.patch](tarball://root/attachments/some-uuid/ticket7819/trac_7819.patch) by @rlmill created at 2010-01-02 15:03:42",
    "created_at": "2010-01-02T15:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7819#issuecomment-67556",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_7819.patch](tarball://root/attachments/some-uuid/ticket7819/trac_7819.patch) by @rlmill created at 2010-01-02 15:03:42



---

archive/issue_comments_067557.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-02T15:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7819#issuecomment-67557",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067558.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-04T15:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7819#issuecomment-67558",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067559.json:
```json
{
    "body": "Positive review.  By the way,\n\n```\nsage: a = RIF(3.9999999999999999999999999999999999,5.000000000000000000000000000000000)\nsage: b = RIF(4.000000000000000000000000000000000,4.9999999999999999999999999999999999)\nsage: a.is_int()\n(False, None)\nsage: b.is_int()\n(False, None)\n```\nthough I don't know if that's a bug (except in user input), since\n\n```\nsage: a.str(style='brackets')\n'[3.9999999999999995 .. 5.0000000000000000]'\nsage: b.str(style='brackets')\n'[4.0000000000000000 .. 5.0000000000000000]'\n```\nbut anyway wanted to point it out in case this is considered something that should be documented in is_int(), not just in RIF().",
    "created_at": "2010-01-04T15:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7819#issuecomment-67559",
    "user": "https://github.com/kcrisman"
}
```

Positive review.  By the way,

```
sage: a = RIF(3.9999999999999999999999999999999999,5.000000000000000000000000000000000)
sage: b = RIF(4.000000000000000000000000000000000,4.9999999999999999999999999999999999)
sage: a.is_int()
(False, None)
sage: b.is_int()
(False, None)
```
though I don't know if that's a bug (except in user input), since

```
sage: a.str(style='brackets')
'[3.9999999999999995 .. 5.0000000000000000]'
sage: b.str(style='brackets')
'[4.0000000000000000 .. 5.0000000000000000]'
```
but anyway wanted to point it out in case this is considered something that should be documented in is_int(), not just in RIF().



---

archive/issue_events_018715.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-13T05:14:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7819",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7819#event-18715"
}
```



---

archive/issue_comments_067560.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-13T05:14:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7819#issuecomment-67560",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed
