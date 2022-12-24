# Issue 2816: unify eigen* functions for different matrix classes

archive/issues_002816.json:
```json
{
    "body": "Assignee: was\n\nSee the conclusions from the discussion: \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/c8d2001f2b19a9bc#\n\nIssue created by migration from https://trac.sagemath.org/ticket/2816\n\n",
    "created_at": "2008-04-05T22:17:44Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "unify eigen* functions for different matrix classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2816",
    "user": "jason"
}
```
Assignee: was

See the conclusions from the discussion: 

http://groups.google.com/group/sage-devel/browse_thread/thread/c8d2001f2b19a9bc#

Issue created by migration from https://trac.sagemath.org/ticket/2816





---

archive/issue_comments_019334.json:
```json
{
    "body": "Attachment [linear-algebra-interface.patch](tarball://root/attachments/some-uuid/ticket2816/linear-algebra-interface.patch) by jason created at 2008-07-19 18:48:32",
    "created_at": "2008-07-19T18:48:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19334",
    "user": "jason"
}
```

Attachment [linear-algebra-interface.patch](tarball://root/attachments/some-uuid/ticket2816/linear-algebra-interface.patch) by jason created at 2008-07-19 18:48:32



---

archive/issue_comments_019335.json:
```json
{
    "body": "The documentation isn't all there, but you can see the functions.",
    "created_at": "2008-07-19T18:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19335",
    "user": "jason"
}
```

The documentation isn't all there, but you can see the functions.



---

archive/issue_comments_019336.json:
```json
{
    "body": "This depends on #3654",
    "created_at": "2008-07-19T18:49:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19336",
    "user": "jason"
}
```

This depends on #3654



---

archive/issue_comments_019337.json:
```json
{
    "body": "See http://groups.google.com/group/sage-devel/browse_thread/thread/3ef6da9c8fa7db36 for \"documentation\" on the functions.",
    "created_at": "2008-07-19T18:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19337",
    "user": "jason"
}
```

See http://groups.google.com/group/sage-devel/browse_thread/thread/3ef6da9c8fa7db36 for "documentation" on the functions.



---

archive/issue_comments_019338.json:
```json
{
    "body": "I know this is preliminary but just wanted to report for others testers that this has a boat-load of doctest failures:\n\n\n```\n...\n        sage -t  devel/sage/sage/calculus/wester.py\n        sage -t  devel/sage/sage/matrix/matrix2.pyx\n        sage -t  devel/sage/sage/matrix/tests.py\n        sage -t  devel/sage/sage/modular/modform/half_integral.py\n        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx\n        sage -t  devel/sage/sage/misc/functional.py\n```\n\nI ran testall twice and it seems that I did not pick up the failure of sage -t  devel/sage/sage/calculus/wester.py or of devel/sage/sage/modular/modform/half_integral.py the first time. These aside, looks like it will eventually be a valuable contribution to SAGE.",
    "created_at": "2008-07-20T02:39:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19338",
    "user": "wdj"
}
```

I know this is preliminary but just wanted to report for others testers that this has a boat-load of doctest failures:


```
...
        sage -t  devel/sage/sage/calculus/wester.py
        sage -t  devel/sage/sage/matrix/matrix2.pyx
        sage -t  devel/sage/sage/matrix/tests.py
        sage -t  devel/sage/sage/modular/modform/half_integral.py
        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
        sage -t  devel/sage/sage/misc/functional.py
```

I ran testall twice and it seems that I did not pick up the failure of sage -t  devel/sage/sage/calculus/wester.py or of devel/sage/sage/modular/modform/half_integral.py the first time. These aside, looks like it will eventually be a valuable contribution to SAGE.



---

archive/issue_comments_019339.json:
```json
{
    "body": "Thanks for running testall.  Some doctests are fixed in the current patch; I'll fix the other doctests in an updated patch.",
    "created_at": "2008-07-20T03:32:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19339",
    "user": "jason"
}
```

Thanks for running testall.  Some doctests are fixed in the current patch; I'll fix the other doctests in an updated patch.



---

archive/issue_comments_019340.json:
```json
{
    "body": "This is part of the linear algebra SEP: http://wiki.sagemath.org/LinearAlgebraSEP",
    "created_at": "2009-01-22T01:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19340",
    "user": "jason"
}
```

This is part of the linear algebra SEP: http://wiki.sagemath.org/LinearAlgebraSEP



---

archive/issue_comments_019341.json:
```json
{
    "body": "What is going on here?\n\nCheers,\n\nMichael",
    "created_at": "2009-04-18T22:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19341",
    "user": "mabshoff"
}
```

What is going on here?

Cheers,

Michael



---

archive/issue_comments_019342.json:
```json
{
    "body": "Well, it probably needs massive rebasing because of the rest transition, for one.  It's on my back burner; I'll probably get to it before June, since I'm teaching linear algebra for the first part of the summer.  However, if someone else is interested in working on this, don't hesitate to post a message here and start working!",
    "created_at": "2009-04-19T00:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2816",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2816#issuecomment-19342",
    "user": "jason"
}
```

Well, it probably needs massive rebasing because of the rest transition, for one.  It's on my back burner; I'll probably get to it before June, since I'm teaching linear algebra for the first part of the summer.  However, if someone else is interested in working on this, don't hesitate to post a message here and start working!
