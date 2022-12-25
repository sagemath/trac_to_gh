# Issue 2532: [with-patch] padic bugfix

archive/issues_002532.json:
```json
{
    "body": "Assignee: @roed314\n\nFixes a number of bugs in p-adic extensions.\n\n1. changes many object creation functions to pass on exceptions if necessary.\n2. fixes a bug in precision_absolute for capped relative extension elements that causes it to return the wrong answer if the element is not normalized.\n3. Fixes object creation functions so that they do not fail when asked to create an element of precision zero.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2532\n\n",
    "created_at": "2008-03-15T19:05:56Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with-patch] padic bugfix",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2532",
    "user": "https://github.com/roed314"
}
```
Assignee: @roed314

Fixes a number of bugs in p-adic extensions.

1. changes many object creation functions to pass on exceptions if necessary.
2. fixes a bug in precision_absolute for capped relative extension elements that causes it to return the wrong answer if the element is not normalized.
3. Fixes object creation functions so that they do not fail when asked to create an element of precision zero.

Issue created by migration from https://trac.sagemath.org/ticket/2532





---

archive/issue_comments_017227.json:
```json
{
    "body": "Attachment [padic_restore_context_zero_bugfix.patch](tarball://root/attachments/some-uuid/ticket2532/padic_restore_context_zero_bugfix.patch) by @mwhansen created at 2008-03-15 21:49:01",
    "created_at": "2008-03-15T21:49:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2532#issuecomment-17227",
    "user": "https://github.com/mwhansen"
}
```

Attachment [padic_restore_context_zero_bugfix.patch](tarball://root/attachments/some-uuid/ticket2532/padic_restore_context_zero_bugfix.patch) by @mwhansen created at 2008-03-15 21:49:01



---

archive/issue_comments_017228.json:
```json
{
    "body": "The patch applies, builds, and passes all tests.  However, a follow-up patch should be added which adds doctests to show that the bugs are indeed fixed.",
    "created_at": "2008-03-15T22:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2532#issuecomment-17228",
    "user": "https://github.com/mwhansen"
}
```

The patch applies, builds, and passes all tests.  However, a follow-up patch should be added which adds doctests to show that the bugs are indeed fixed.



---

archive/issue_comments_017229.json:
```json
{
    "body": "Doctests also pass for me when applying the patch to 2.10.4.final. After talking to roed about the missing doctest in IRC yesterday I tend to want to merge this and hope that doctests are forthcomings since these fixes have been tested and reviewed by several people \"back east.\"\n\nCheers,\n\nMichael",
    "created_at": "2008-03-17T00:35:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2532#issuecomment-17229",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Doctests also pass for me when applying the patch to 2.10.4.final. After talking to roed about the missing doctest in IRC yesterday I tend to want to merge this and hope that doctests are forthcomings since these fixes have been tested and reviewed by several people "back east."

Cheers,

Michael



---

archive/issue_comments_017230.json:
```json
{
    "body": "I agree. Given the current doctest coverage and code complexity of the p-adics code, I think we should just merge this and wait for the real doctesting work to catch up.",
    "created_at": "2008-03-17T00:52:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2532#issuecomment-17230",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```

I agree. Given the current doctest coverage and code complexity of the p-adics code, I think we should just merge this and wait for the real doctesting work to catch up.



---

archive/issue_comments_017231.json:
```json
{
    "body": "I agree with dmharvey. #610 covers the need to increase doctest coverage. Maybe somebody else besides roed can help out here?\n\nCheers,\n\nMichael",
    "created_at": "2008-03-17T01:05:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2532#issuecomment-17231",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I agree with dmharvey. #610 covers the need to increase doctest coverage. Maybe somebody else besides roed can help out here?

Cheers,

Michael



---

archive/issue_comments_017232.json:
```json
{
    "body": "Merged in Sage 2.10.4.final - note that the patch is a GNU patch. I did commit it in roed's name.",
    "created_at": "2008-03-17T01:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2532#issuecomment-17232",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.final - note that the patch is a GNU patch. I did commit it in roed's name.



---

archive/issue_comments_017233.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-17T01:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2532#issuecomment-17233",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_002713.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-17T01:09:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2532",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2532#event-2713"
}
```
