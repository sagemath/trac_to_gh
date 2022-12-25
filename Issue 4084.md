# Issue 4084: plot(1/cos,-1,1) fails

archive/issues_004084.json:
```json
{
    "body": "Assignee: @jicama\n\nPlot works with symbolic functions, but not compositions or arithmetic involving them.\n\n```\nsage: plot(cos,-1,1) #works\n\nsage: plot(1/cos,-1,1)\nTraceback (most recent call last):\n...\nTypeError: float() argument must be a string or a number\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4084\n\n",
    "created_at": "2008-09-09T03:44:08Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "plot(1/cos,-1,1) fails",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4084",
    "user": "https://github.com/jicama"
}
```
Assignee: @jicama

Plot works with symbolic functions, but not compositions or arithmetic involving them.

```
sage: plot(cos,-1,1) #works

sage: plot(1/cos,-1,1)
Traceback (most recent call last):
...
TypeError: float() argument must be a string or a number
```

Issue created by migration from https://trac.sagemath.org/ticket/4084





---

archive/issue_comments_029407.json:
```json
{
    "body": "Attachment [4804.patch](tarball://root/attachments/some-uuid/ticket4084/4804.patch) by mabshoff created at 2008-09-09 03:50:13\n\nHi,\n\nthis is fixed in 3.1.2.rc1-ish:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.2.rc0, Release Date: 2008-09-06                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: plot(1/cos,-1,1)\n\nsage: \nExiting SAGE (CPU time 0m0.63s, Wall time 0m4.01s).\nExiting spawned Maxima process.\n```\nPlease post a patch that adds only the doctest. There are unrelated changes in the patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T03:50:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4084#issuecomment-29407",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [4804.patch](tarball://root/attachments/some-uuid/ticket4084/4804.patch) by mabshoff created at 2008-09-09 03:50:13

Hi,

this is fixed in 3.1.2.rc1-ish:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.rc1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.2.rc0, Release Date: 2008-09-06                   |
| Type notebook() for the GUI, and license() for information.        |
sage: plot(1/cos,-1,1)

sage: 
Exiting SAGE (CPU time 0m0.63s, Wall time 0m4.01s).
Exiting spawned Maxima process.
```
Please post a patch that adds only the doctest. There are unrelated changes in the patch.

Cheers,

Michael



---

archive/issue_comments_029408.json:
```json
{
    "body": "Attachment [4804_doctest_only.patch](tarball://root/attachments/some-uuid/ticket4084/4804_doctest_only.patch) by @jicama created at 2008-09-09 04:05:46\n\n4804_doctest_only.patch adds only doctests.  If accepted, only that patch should be applied.  This should not be accepted until the new doctests actually pass.\n\nThanks for the quick catch mhansen.  \"Unrelated\" might be a little strong, though I was bold in modifying implementation to make this work.  In any case, sounds like problem solved.\n\nCheers,\n\nJM",
    "created_at": "2008-09-09T04:05:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4084#issuecomment-29408",
    "user": "https://github.com/jicama"
}
```

Attachment [4804_doctest_only.patch](tarball://root/attachments/some-uuid/ticket4084/4804_doctest_only.patch) by @jicama created at 2008-09-09 04:05:46

4804_doctest_only.patch adds only doctests.  If accepted, only that patch should be applied.  This should not be accepted until the new doctests actually pass.

Thanks for the quick catch mhansen.  "Unrelated" might be a little strong, though I was bold in modifying implementation to make this work.  In any case, sounds like problem solved.

Cheers,

JM



---

archive/issue_comments_029409.json:
```json
{
    "body": "Replying to [comment:2 jwmerrill]:\n> 4804_doctest_only.patch adds only doctests.  If accepted, only that patch should be applied.  This should not be accepted until the new doctests actually pass.\n\n\nI rebased the patch against my current merge tree. \n\n> Thanks for the quick catch mhansen.  \"Unrelated\" might be a little strong, though I was bold in modifying implementation to make this work.  In any case, sounds like problem solved.\n\n\nIt wasn't mhansen ;). The changes in plot.py had *zero* to do with the ticket and the \"fix\" is canonically wrong since we just don't just wipe out low order bits preventatively.\n\n> Cheers,\n> \n> JM\n\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T04:21:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4084#issuecomment-29409",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:2 jwmerrill]:
> 4804_doctest_only.patch adds only doctests.  If accepted, only that patch should be applied.  This should not be accepted until the new doctests actually pass.


I rebased the patch against my current merge tree. 

> Thanks for the quick catch mhansen.  "Unrelated" might be a little strong, though I was bold in modifying implementation to make this work.  In any case, sounds like problem solved.


It wasn't mhansen ;). The changes in plot.py had *zero* to do with the ticket and the "fix" is canonically wrong since we just don't just wipe out low order bits preventatively.

> Cheers,
> 
> JM


Cheers,

Michael



---

archive/issue_comments_029410.json:
```json
{
    "body": "Both points well taken.\n\nCheers,\n\nJM",
    "created_at": "2008-09-09T04:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4084#issuecomment-29410",
    "user": "https://github.com/jicama"
}
```

Both points well taken.

Cheers,

JM



---

archive/issue_comments_029411.json:
```json
{
    "body": "With the patch applied doctests do pass. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-09T04:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4084#issuecomment-29411",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

With the patch applied doctests do pass. Positive review.

Cheers,

Michael



---

archive/issue_comments_029412.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-09T04:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4084#issuecomment-29412",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009319.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-09T04:45:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4084#event-9319"
}
```



---

archive/issue_comments_029413.json:
```json
{
    "body": "Merged rebased 4804_doctest_only.patch in Sage 3.1.2.rc1",
    "created_at": "2008-09-09T04:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4084",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4084#issuecomment-29413",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged rebased 4804_doctest_only.patch in Sage 3.1.2.rc1
