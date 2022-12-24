# Issue 2660: copy work around stdint.h on Solaris 9

archive/issues_002660.json:
```json
{
    "body": "Assignee: mabshoff\n\nSolaris 9 only supports a draft standard of the C99 spec, so it is missing stdint.h. This patch adds a workaround fix that for now is 32 bits only.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2660\n\n",
    "created_at": "2008-03-24T12:40:10Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "copy work around stdint.h on Solaris 9",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2660",
    "user": "mabshoff"
}
```
Assignee: mabshoff

Solaris 9 only supports a draft standard of the C99 spec, so it is missing stdint.h. This patch adds a workaround fix that for now is 32 bits only.


Issue created by migration from https://trac.sagemath.org/ticket/2660





---

archive/issue_comments_018314.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-24T12:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2660#issuecomment-18314",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_018315.json:
```json
{
    "body": "Attachment [trac_2660.patch](tarball://root/attachments/some-uuid/ticket2660/trac_2660.patch) by mabshoff created at 2008-03-24 12:42:39",
    "created_at": "2008-03-24T12:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2660#issuecomment-18315",
    "user": "mabshoff"
}
```

Attachment [trac_2660.patch](tarball://root/attachments/some-uuid/ticket2660/trac_2660.patch) by mabshoff created at 2008-03-24 12:42:39



---

archive/issue_comments_018316.json:
```json
{
    "body": "Patch applies cleanly. Looked at the changes, seems good. Not tested since it is sun only.",
    "created_at": "2008-03-24T12:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2660#issuecomment-18316",
    "user": "jkantor"
}
```

Patch applies cleanly. Looked at the changes, seems good. Not tested since it is sun only.



---

archive/issue_comments_018317.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-24T12:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2660#issuecomment-18317",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018318.json:
```json
{
    "body": "Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-24T12:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2660",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2660#issuecomment-18318",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha2
