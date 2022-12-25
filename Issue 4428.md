# Issue 4428: [with patch, needs review] Forgot to close open files in sage/rings/number_field/totallyreal_phc.py

archive/issues_004428.json:
```json
{
    "body": "Assignee: @craigcitro\n\nI forgot to close the file handles opened by `popen2` in my fix for #4386. The attached patch cleans this up.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4428\n\n",
    "created_at": "2008-11-02T22:35:53Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "[with patch, needs review] Forgot to close open files in sage/rings/number_field/totallyreal_phc.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4428",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

I forgot to close the file handles opened by `popen2` in my fix for #4386. The attached patch cleans this up.

Issue created by migration from https://trac.sagemath.org/ticket/4428





---

archive/issue_comments_032483.json:
```json
{
    "body": "Attachment [trac-4428.patch](tarball://root/attachments/some-uuid/ticket4428/trac-4428.patch) by mabshoff created at 2008-11-04 00:41:53\n\nLooks good to me. Nice catch, sorry I did not catch it during the review of the previous ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-04T00:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4428#issuecomment-32483",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac-4428.patch](tarball://root/attachments/some-uuid/ticket4428/trac-4428.patch) by mabshoff created at 2008-11-04 00:41:53

Looks good to me. Nice catch, sorry I did not catch it during the review of the previous ticket.

Cheers,

Michael



---

archive/issue_comments_032484.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-04T21:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4428#issuecomment-32484",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_comments_032485.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-04T21:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4428#issuecomment-32485",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010015.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-04T21:33:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4428",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4428#event-10015"
}
```
