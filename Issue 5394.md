# Issue 5394: [with patch, needs review] Remove the remnants of the docs from sage-ptest and make it ignore the devel/sage/build directory

archive/issues_005394.json:
```json
{
    "body": "Assignee: cwitty\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5394\n\n",
    "created_at": "2009-02-27T17:14:13Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] Remove the remnants of the docs from sage-ptest and make it ignore the devel/sage/build directory",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5394",
    "user": "mhansen"
}
```
Assignee: cwitty



Issue created by migration from https://trac.sagemath.org/ticket/5394





---

archive/issue_comments_041541.json:
```json
{
    "body": "Attachment [trac_5394.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394.patch) by mabshoff created at 2009-02-27 21:03:32\n\nExcellent, couldn't have done it better myself :)\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T21:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41541",
    "user": "mabshoff"
}
```

Attachment [trac_5394.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394.patch) by mabshoff created at 2009-02-27 21:03:32

Excellent, couldn't have done it better myself :)

Cheers,

Michael



---

archive/issue_comments_041542.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T23:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41542",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-27T23:07:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41543",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_041544.json:
```json
{
    "body": "This patch actually does not ignore the bits in build and I am not quite sure why the patch doesn't work.\n\nMike: Thoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T12:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41544",
    "user": "mabshoff"
}
```

This patch actually does not ignore the bits in build and I am not quite sure why the patch doesn't work.

Mike: Thoughts?

Cheers,

Michael



---

archive/issue_comments_041545.json:
```json
{
    "body": "Ok, figured it out - reviewer patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T12:35:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41545",
    "user": "mabshoff"
}
```

Ok, figured it out - reviewer patch coming up.

Cheers,

Michael



---

archive/issue_comments_041546.json:
```json
{
    "body": "Attachment [trac_5394-reviewer.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394-reviewer.patch) by mabshoff created at 2009-02-28 15:50:50\n\nOops, the reviewer patch had some debug output in it. I removed that in the tree and did another checkin.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T15:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5394",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5394#issuecomment-41546",
    "user": "mabshoff"
}
```

Attachment [trac_5394-reviewer.patch](tarball://root/attachments/some-uuid/ticket5394/trac_5394-reviewer.patch) by mabshoff created at 2009-02-28 15:50:50

Oops, the reviewer patch had some debug output in it. I removed that in the tree and did another checkin.

Cheers,

Michael
