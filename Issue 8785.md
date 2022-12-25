# Issue 8785: avoid subtle interaction between importing multiprocessing and twisted

archive/issues_008785.json:
```json
{
    "body": "Assignee: @jasongrout\n\nIt turns out that on some platforms, importing multiprocessing, then twisted, leads to an \"int object is not callable\" TypeError.  This breaks devel/sage/sage/all.py's quit_sage function, causing a big traceback at exit.   This could also cause great confusion for people writing a program that uses `@`parallel('multiprocessing') followed by anything involving twisted. \n\nA simple fix is to import the relevant part of twisted before using multiprocessing in `@`parallel.   The attached patch does this.\n\nNOTE: The system that exhibits this is in a corporate setting, and no devs have systems where this can be replicated at present, unfortunately.  So please do NOT revert this just because you don't see the problem on your laptop!\n\nIssue created by migration from https://trac.sagemath.org/ticket/8785\n\n",
    "closed_at": "2010-04-28T17:36:19Z",
    "created_at": "2010-04-27T20:54:37Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.1",
    "title": "avoid subtle interaction between importing multiprocessing and twisted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8785",
    "user": "https://github.com/williamstein"
}
```
Assignee: @jasongrout

It turns out that on some platforms, importing multiprocessing, then twisted, leads to an "int object is not callable" TypeError.  This breaks devel/sage/sage/all.py's quit_sage function, causing a big traceback at exit.   This could also cause great confusion for people writing a program that uses `@`parallel('multiprocessing') followed by anything involving twisted. 

A simple fix is to import the relevant part of twisted before using multiprocessing in `@`parallel.   The attached patch does this.

NOTE: The system that exhibits this is in a corporate setting, and no devs have systems where this can be replicated at present, unfortunately.  So please do NOT revert this just because you don't see the problem on your laptop!

Issue created by migration from https://trac.sagemath.org/ticket/8785





---

archive/issue_comments_080306.json:
```json
{
    "body": "Attachment [trac_8785.patch](tarball://root/attachments/some-uuid/ticket8785/trac_8785.patch) by @williamstein created at 2010-04-27 20:58:45",
    "created_at": "2010-04-27T20:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80306",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_8785.patch](tarball://root/attachments/some-uuid/ticket8785/trac_8785.patch) by @williamstein created at 2010-04-27 20:58:45



---

archive/issue_comments_080307.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-27T20:58:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80307",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080308.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-27T22:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80308",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080309.json:
```json
{
    "body": "I tried it and it works!",
    "created_at": "2010-04-27T22:27:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80309",
    "user": "https://trac.sagemath.org/admin/accounts/users/mariah"
}
```

I tried it and it works!



---

archive/issue_events_021419.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-04-28T17:36:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8785#event-21419"
}
```



---

archive/issue_comments_080310.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-28T17:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80310",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_080311.json:
```json
{
    "body": "Would be more informative to write explicitely on which hardware/OS it failed. \"corporate settings\" is more than vague. Was there any upstream report? This problem might have been solved since then!",
    "created_at": "2016-01-10T23:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8785",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8785#issuecomment-80311",
    "user": "https://github.com/videlec"
}
```

Would be more informative to write explicitely on which hardware/OS it failed. "corporate settings" is more than vague. Was there any upstream report? This problem might have been solved since then!
