# Issue 4910: convert sage.functions.* docstrings to Sphinx

archive/issues_004910.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4910\n\n",
    "created_at": "2009-01-01T22:50:50Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.functions.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4910",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4910





---

archive/issue_comments_037189.json:
```json
{
    "body": "Attachment [trac_4910.patch](tarball://root/attachments/some-uuid/ticket4910/trac_4910.patch) by @mwhansen created at 2009-01-02 02:26:41",
    "created_at": "2009-01-02T02:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37189",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4910.patch](tarball://root/attachments/some-uuid/ticket4910/trac_4910.patch) by @mwhansen created at 2009-01-02 02:26:41



---

archive/issue_comments_037190.json:
```json
{
    "body": "Attachment [sage.functions-final.patch](tarball://root/attachments/some-uuid/ticket4910/sage.functions-final.patch) by @hivert created at 2009-02-24 15:21:11\n\nI've found some minor problem in the patch:\n\n```\n-  Each *Legendre polynomial* `P_n(x)` is an $n$-th degree polynomial. \n```\nShould be\n\n```\n-  Each *Legendre polynomial* `P_n(x)` is an `n`-th degree polynomial. \n```\n\nAnd a little bit lower:\n\n```\n The *Legendre function of the second kind* $Q_n(x)$ is another \n```\nShould be\n\n```\n The *Legendre function of the second kind* `Q_n(x)` is another \n```\n\nA whole section\n\n```\nImplemented methods: \n  9 latex outout \n  10 __call__ \n[...]\n  39 extend_by_zero_to \n  40 unextend \n```\nseems to have vanished.",
    "created_at": "2009-02-24T15:21:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37190",
    "user": "https://github.com/hivert"
}
```

Attachment [sage.functions-final.patch](tarball://root/attachments/some-uuid/ticket4910/sage.functions-final.patch) by @hivert created at 2009-02-24 15:21:11

I've found some minor problem in the patch:

```
-  Each *Legendre polynomial* `P_n(x)` is an $n$-th degree polynomial. 
```
Should be

```
-  Each *Legendre polynomial* `P_n(x)` is an `n`-th degree polynomial. 
```

And a little bit lower:

```
 The *Legendre function of the second kind* $Q_n(x)$ is another 
```
Should be

```
 The *Legendre function of the second kind* `Q_n(x)` is another 
```

A whole section

```
Implemented methods: 
  9 latex outout 
  10 __call__ 
[...]
  39 extend_by_zero_to 
  40 unextend 
```
seems to have vanished.



---

archive/issue_comments_037191.json:
```json
{
    "body": "I've manually edited the patch to fixes the two \"$\" vs \"`\" problems. The corrected patch should follow. \n\nThe section implemented methods is removed on purpose (it is redundent with the code). Otherwise it seems Ok.\n\nAs for combinat, my rereading was a fast rereading. In particular, There are a lot of formulas that needs time to be checked carfully.",
    "created_at": "2009-02-24T15:36:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37191",
    "user": "https://github.com/hivert"
}
```

I've manually edited the patch to fixes the two "$" vs "`" problems. The corrected patch should follow. 

The section implemented methods is removed on purpose (it is redundent with the code). Otherwise it seems Ok.

As for combinat, my rereading was a fast rereading. In particular, There are a lot of formulas that needs time to be checked carfully.



---

archive/issue_comments_037192.json:
```json
{
    "body": "Attachment [sage.functions-final-fixed.patch](tarball://root/attachments/some-uuid/ticket4910/sage.functions-final-fixed.patch) by @hivert created at 2009-02-24 15:37:56\n\nNew patch with hand fix.",
    "created_at": "2009-02-24T15:37:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37192",
    "user": "https://github.com/hivert"
}
```

Attachment [sage.functions-final-fixed.patch](tarball://root/attachments/some-uuid/ticket4910/sage.functions-final-fixed.patch) by @hivert created at 2009-02-24 15:37:56

New patch with hand fix.



---

archive/issue_comments_037193.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-02-24T18:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37193",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_037194.json:
```json
{
    "body": "I put these changes in the fixes.patch in #5330.",
    "created_at": "2009-02-24T18:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37194",
    "user": "https://github.com/mwhansen"
}
```

I put these changes in the fixes.patch in #5330.



---

archive/issue_comments_037195.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-24T18:07:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37195",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37196",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_011328.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-24T18:14:08Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4910#event-11328"
}
```



---

archive/issue_comments_037197.json:
```json
{
    "body": "Merged sage.functions-final-fixed.patch in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4910",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4910#issuecomment-37197",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged sage.functions-final-fixed.patch in Sage 3.4.alpha0.

Cheers,

Michael
