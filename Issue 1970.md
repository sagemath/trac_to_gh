# Issue 1970: [with tiny patch; needs easy review] notebook -- gnutls should not be needed if you're running the notebook insecurely, so don't require it

archive/issues_001970.json:
```json
{
    "body": "Assignee: boothby\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1970\n\n",
    "created_at": "2008-01-29T11:56:32Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with tiny patch; needs easy review] notebook -- gnutls should not be needed if you're running the notebook insecurely, so don't require it",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1970",
    "user": "@williamstein"
}
```
Assignee: boothby



Issue created by migration from https://trac.sagemath.org/ticket/1970





---

archive/issue_comments_012749.json:
```json
{
    "body": "Attachment [trac-1970-notebook-gnutls.patch](tarball://root/attachments/some-uuid/ticket1970/trac-1970-notebook-gnutls.patch) by @williamstein created at 2008-01-29 11:57:58",
    "created_at": "2008-01-29T11:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1970#issuecomment-12749",
    "user": "@williamstein"
}
```

Attachment [trac-1970-notebook-gnutls.patch](tarball://root/attachments/some-uuid/ticket1970/trac-1970-notebook-gnutls.patch) by @williamstein created at 2008-01-29 11:57:58



---

archive/issue_comments_012750.json:
```json
{
    "body": "updated patch use this instead",
    "created_at": "2008-01-29T16:08:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1970#issuecomment-12750",
    "user": "@malb"
}
```

updated patch use this instead



---

archive/issue_comments_012751.json:
```json
{
    "body": "Attachment [trac-1970-notebook-gnutls.2.patch](tarball://root/attachments/some-uuid/ticket1970/trac-1970-notebook-gnutls.2.patch) by @malb created at 2008-01-29 16:13:13\n\nI've uploaded a new patch which replaces the old patch. This version checks for an OSError rather than any exception. It is better to check for a specific error only because this way we can spot errors and fix them. I've applied this patch against rc2 but the insecure notebook worked for me before and after the patch (I have GnuTLS installed system wide)",
    "created_at": "2008-01-29T16:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1970#issuecomment-12751",
    "user": "@malb"
}
```

Attachment [trac-1970-notebook-gnutls.2.patch](tarball://root/attachments/some-uuid/ticket1970/trac-1970-notebook-gnutls.2.patch) by @malb created at 2008-01-29 16:13:13

I've uploaded a new patch which replaces the old patch. This version checks for an OSError rather than any exception. It is better to check for a specific error only because this way we can spot errors and fix them. I've applied this patch against rc2 but the insecure notebook worked for me before and after the patch (I have GnuTLS installed system wide)



---

archive/issue_comments_012752.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-29T16:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1970#issuecomment-12752",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012753.json:
```json
{
    "body": "Merged trac-1970-notebook-gnutls.2.patch in Sage 2.10.1.rc3",
    "created_at": "2008-01-29T16:19:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1970",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1970#issuecomment-12753",
    "user": "mabshoff"
}
```

Merged trac-1970-notebook-gnutls.2.patch in Sage 2.10.1.rc3
