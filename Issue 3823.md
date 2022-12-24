# Issue 3823: Interact - get rid of default height

archive/issues_003823.json:
```json
{
    "body": "Assignee: itolkov\n\nInteractions have a minimum height of 400px, which consumes space when only part of it is used.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3823\n\n",
    "created_at": "2008-08-12T20:38:42Z",
    "labels": [
        "notebook",
        "minor",
        "bug"
    ],
    "title": "Interact - get rid of default height",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3823",
    "user": "itolkov"
}
```
Assignee: itolkov

Interactions have a minimum height of 400px, which consumes space when only part of it is used.

Issue created by migration from https://trac.sagemath.org/ticket/3823





---

archive/issue_comments_027194.json:
```json
{
    "body": "Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3823/sage.patch) by itolkov created at 2008-08-12 20:51:21\n\nI changed the default height to 20px, since it's probably good to have one.",
    "created_at": "2008-08-12T20:51:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3823#issuecomment-27194",
    "user": "itolkov"
}
```

Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3823/sage.patch) by itolkov created at 2008-08-12 20:51:21

I changed the default height to 20px, since it's probably good to have one.



---

archive/issue_comments_027195.json:
```json
{
    "body": "Changing component from notebook to interact.",
    "created_at": "2008-08-13T06:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3823#issuecomment-27195",
    "user": "mabshoff"
}
```

Changing component from notebook to interact.



---

archive/issue_comments_027196.json:
```json
{
    "body": "Looks good to me.  Positive review.",
    "created_at": "2008-08-27T14:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3823#issuecomment-27196",
    "user": "jason"
}
```

Looks good to me.  Positive review.



---

archive/issue_comments_027197.json:
```json
{
    "body": "This does not apply cleanly any more, but should be trivial to rebase:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/devel/sage$ patch -p1 < trac_3823_sage.patch \npatching file sage/server/notebook/interact.py\nHunk #1 FAILED at 1397.\n1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/interact.py.rej\n```\n\n\nIgor: In the future please name the patches you post trac_XXXX_description.patch.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-27T21:39:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3823#issuecomment-27197",
    "user": "mabshoff"
}
```

This does not apply cleanly any more, but should be trivial to rebase:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.1.2.alpha2/devel/sage$ patch -p1 < trac_3823_sage.patch 
patching file sage/server/notebook/interact.py
Hunk #1 FAILED at 1397.
1 out of 1 hunk FAILED -- saving rejects to file sage/server/notebook/interact.py.rej
```


Igor: In the future please name the patches you post trac_XXXX_description.patch.

Cheers,

Michael



---

archive/issue_comments_027198.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-29T00:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3823#issuecomment-27198",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_027199.json:
```json
{
    "body": "Attachment [trac_3823_sage.patch](tarball://root/attachments/some-uuid/ticket3823/trac_3823_sage.patch) by mabshoff created at 2008-08-29 00:58:22\n\nMerged trac_3823_sage.patch in Sage 3.1.2.alpha2",
    "created_at": "2008-08-29T00:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3823#issuecomment-27199",
    "user": "mabshoff"
}
```

Attachment [trac_3823_sage.patch](tarball://root/attachments/some-uuid/ticket3823/trac_3823_sage.patch) by mabshoff created at 2008-08-29 00:58:22

Merged trac_3823_sage.patch in Sage 3.1.2.alpha2
