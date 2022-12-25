# Issue 8847: pynac.pyx use double precision special functions instead of long double

archive/issues_008847.json:
```json
{
    "body": "Assignee: tbd\n\nMany systems such as cygwin don't have the long double version.  Plus, they are being applied to floats/doubles so the extra precision doesn't buy much.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8847\n\n",
    "created_at": "2010-05-03T12:18:24Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "pynac.pyx use double precision special functions instead of long double",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8847",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

Many systems such as cygwin don't have the long double version.  Plus, they are being applied to floats/doubles so the extra precision doesn't buy much.

Issue created by migration from https://trac.sagemath.org/ticket/8847





---

archive/issue_comments_081197.json:
```json
{
    "body": "Attachment [trac_8847.patch](tarball://root/attachments/some-uuid/ticket8847/trac_8847.patch) by @mwhansen created at 2010-05-03 13:22:06",
    "created_at": "2010-05-03T13:22:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81197",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8847.patch](tarball://root/attachments/some-uuid/ticket8847/trac_8847.patch) by @mwhansen created at 2010-05-03 13:22:06



---

archive/issue_comments_081198.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-03T13:22:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81198",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081199.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-05-05T02:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81199",
    "user": "https://github.com/burcin"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_081200.json:
```json
{
    "body": "This gives the following doctest failures on my 64-bit T9300 Core 2 Duo laptop, with `gcc (Gentoo 4.3.4 p1.0, pie-10.1.5) 4.3.4` and glibc-2.10.1. I have no idea what is relevant, so I give some random information. :)\n\n\n```\n**********************************************************************\nFile \"/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/functions/other.py\", line 428:\n    sage: gamma1(float(6))\nExpected:\n    120.0\nGot:\n    119.99999999999997\n**********************************************************************\n```\n\n\n```\n**********************************************************************\nFile \"/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/symbolic/expression.pyx\", line 5318:\n    sage: SR(10.0r).gamma()\nExpected:\n    362880.0\nGot:\n    362880.00000000047\n**********************************************************************\n```\n",
    "created_at": "2010-05-05T02:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81200",
    "user": "https://github.com/burcin"
}
```

This gives the following doctest failures on my 64-bit T9300 Core 2 Duo laptop, with `gcc (Gentoo 4.3.4 p1.0, pie-10.1.5) 4.3.4` and glibc-2.10.1. I have no idea what is relevant, so I give some random information. :)


```
**********************************************************************
File "/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/functions/other.py", line 428:
    sage: gamma1(float(6))
Expected:
    120.0
Got:
    119.99999999999997
**********************************************************************
```


```
**********************************************************************
File "/home/burcin/sage/sage-4.4.1.alpha2-patched/devel/sage-t/sage/symbolic/expression.pyx", line 5318:
    sage: SR(10.0r).gamma()
Expected:
    362880.0
Got:
    362880.00000000047
**********************************************************************
```




---

archive/issue_comments_081201.json:
```json
{
    "body": "Changing keywords from \"\" to \"pynac\".",
    "created_at": "2010-05-05T02:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81201",
    "user": "https://github.com/burcin"
}
```

Changing keywords from "" to "pynac".



---

archive/issue_comments_081202.json:
```json
{
    "body": "It'd be nice if we could just do like an ifdef in Cython.",
    "created_at": "2010-05-05T02:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81202",
    "user": "https://github.com/mwhansen"
}
```

It'd be nice if we could just do like an ifdef in Cython.



---

archive/issue_comments_081203.json:
```json
{
    "body": "We can put the ifdef in `c_lib/include/ginac_wrapper.h` to define the long double versions on Cygwin. Initially, they could just wrap the double precision functions.",
    "created_at": "2010-05-05T02:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81203",
    "user": "https://github.com/burcin"
}
```

We can put the ifdef in `c_lib/include/ginac_wrapper.h` to define the long double versions on Cygwin. Initially, they could just wrap the double precision functions.



---

archive/issue_comments_081204.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-26T01:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81204",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_081205.json:
```json
{
    "body": "I just did something at runtime using a bint.  It's very simple, and will have a very minimal performance hit.",
    "created_at": "2010-05-26T01:39:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81205",
    "user": "https://github.com/williamstein"
}
```

I just did something at runtime using a bint.  It's very simple, and will have a very minimal performance hit.



---

archive/issue_comments_081206.json:
```json
{
    "body": "apply only this (not the one below)",
    "created_at": "2010-05-26T01:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81206",
    "user": "https://github.com/williamstein"
}
```

apply only this (not the one below)



---

archive/issue_comments_081207.json:
```json
{
    "body": "Attachment [trac_8847-take3.patch](tarball://root/attachments/some-uuid/ticket8847/trac_8847-take3.patch) by @williamstein created at 2010-05-26 02:19:50",
    "created_at": "2010-05-26T02:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81207",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8847-take3.patch](tarball://root/attachments/some-uuid/ticket8847/trac_8847-take3.patch) by @williamstein created at 2010-05-26 02:19:50



---

archive/issue_comments_081208.json:
```json
{
    "body": "Attachment [trac_8847-take4.patch](tarball://root/attachments/some-uuid/ticket8847/trac_8847-take4.patch) by @mwhansen created at 2010-05-26 02:50:13",
    "created_at": "2010-05-26T02:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81208",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_8847-take4.patch](tarball://root/attachments/some-uuid/ticket8847/trac_8847-take4.patch) by @mwhansen created at 2010-05-26 02:50:13



---

archive/issue_events_009012.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-26T02:52:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8847#event-9012"
}
```



---

archive/issue_comments_081209.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T02:52:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8847",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8847#issuecomment-81209",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
