# Issue 4828: [with patch, needs review] Sage 3.2.2.rc2: Fix documentation build issues

archive/issues_004828.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are two issues: \n\n* In sage/sage/combinat/ranker.py \"Thi\u00e9ry\" is used without the proper encoding, so change it to \"Thiery\" since that is consistent with the other spellings\n* in doc/ref/files we still include the old word.tex file which no longer exists, so delete that line. The new words documentation will be in 3.3.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4828\n\n",
    "created_at": "2008-12-19T06:34:10Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with patch, needs review] Sage 3.2.2.rc2: Fix documentation build issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4828",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

There are two issues: 

* In sage/sage/combinat/ranker.py "Thiéry" is used without the proper encoding, so change it to "Thiery" since that is consistent with the other spellings
* in doc/ref/files we still include the old word.tex file which no longer exists, so delete that line. The new words documentation will be in 3.3.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4828





---

archive/issue_comments_036530.json:
```json
{
    "body": "Attachment [trac_4828_doc.patch](tarball://root/attachments/some-uuid/ticket4828/trac_4828_doc.patch) by mabshoff created at 2008-12-19 06:37:01",
    "created_at": "2008-12-19T06:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4828#issuecomment-36530",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4828_doc.patch](tarball://root/attachments/some-uuid/ticket4828/trac_4828_doc.patch) by mabshoff created at 2008-12-19 06:37:01



---

archive/issue_comments_036531.json:
```json
{
    "body": "Attachment [trac_4828_sage.patch](tarball://root/attachments/some-uuid/ticket4828/trac_4828_sage.patch) by @dandrake created at 2008-12-19 07:06:53\n\nI had to delete the patchlevel.tex hunk to get the doc patch to apply, but otherwise looks good, positive review.",
    "created_at": "2008-12-19T07:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4828#issuecomment-36531",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_4828_sage.patch](tarball://root/attachments/some-uuid/ticket4828/trac_4828_sage.patch) by @dandrake created at 2008-12-19 07:06:53

I had to delete the patchlevel.tex hunk to get the doc patch to apply, but otherwise looks good, positive review.



---

archive/issue_comments_036532.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-19T07:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4828#issuecomment-36532",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_036533.json:
```json
{
    "body": "Merged both patches in Sage 3.2.2.rc2",
    "created_at": "2008-12-19T07:07:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4828",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4828#issuecomment-36533",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.2.2.rc2



---

archive/issue_events_005074.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-19T07:07:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4828",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4828#event-5074"
}
```
