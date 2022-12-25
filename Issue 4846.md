# Issue 4846: Doctesting should create an empty init.sage if it doesn't exist

archive/issues_004846.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @craigcitro\n\nOften when we do fix IPython related problems things break when init.sage is present. So make doctesting create an empty init.sage so that this is potentially caught.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4846\n\n",
    "created_at": "2008-12-21T09:25:01Z",
    "labels": [
        "component: doctest coverage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.3",
    "title": "Doctesting should create an empty init.sage if it doesn't exist",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @craigcitro

Often when we do fix IPython related problems things break when init.sage is present. So make doctesting create an empty init.sage so that this is potentially caught.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4846





---

archive/issue_comments_036674.json:
```json
{
    "body": "There are doctests in 3.2.2 that fail with an init.sage, so all we need to do is to add the check if it is missing in sage-sage when running doctests and then create an empty one to detect this particular bug.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-21T11:42:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36674",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

There are doctests in 3.2.2 that fail with an init.sage, so all we need to do is to add the check if it is missing in sage-sage when running doctests and then create an empty one to detect this particular bug.

Cheers,

Michael



---

archive/issue_comments_036675.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-26T23:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36675",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036676.json:
```json
{
    "body": "Attachment [trac_4846.patch](tarball://root/attachments/some-uuid/ticket4846/trac_4846.patch) by mabshoff created at 2008-12-26 23:21:26",
    "created_at": "2008-12-26T23:21:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36676",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4846.patch](tarball://root/attachments/some-uuid/ticket4846/trac_4846.patch) by mabshoff created at 2008-12-26 23:21:26



---

archive/issue_comments_036677.json:
```json
{
    "body": "After pestering mabshoff on IRC about this a little, I am convinced this is a good quick solution to avoid most init.sage problems we missed during some of the recent releases. Positive review. :)",
    "created_at": "2008-12-26T23:50:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36677",
    "user": "https://github.com/burcin"
}
```

After pestering mabshoff on IRC about this a little, I am convinced this is a good quick solution to avoid most init.sage problems we missed during some of the recent releases. Positive review. :)



---

archive/issue_comments_036678.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-26T23:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36678",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005091.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-12-26T23:53:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4846#event-5091"
}
```



---

archive/issue_comments_036679.json:
```json
{
    "body": "Merged in Sage 3.2.3.final",
    "created_at": "2008-12-26T23:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4846#issuecomment-36679",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.3.final
