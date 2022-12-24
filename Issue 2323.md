# Issue 2323: updated tutorial to include dsage section

archive/issues_002323.json:
```json
{
    "body": "Assignee: tba\n\nupdated the tutorial to add a section of distributed computing.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2323\n\n",
    "created_at": "2008-02-26T18:15:52Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "updated tutorial to include dsage section",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2323",
    "user": "yi"
}
```
Assignee: tba

updated the tutorial to add a section of distributed computing.

Issue created by migration from https://trac.sagemath.org/ticket/2323





---

archive/issue_comments_015454.json:
```json
{
    "body": "Attachment [dsage-tut.hg](tarball://root/attachments/some-uuid/ticket2323/dsage-tut.hg) by yi created at 2008-02-26 18:16:02",
    "created_at": "2008-02-26T18:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2323#issuecomment-15454",
    "user": "yi"
}
```

Attachment [dsage-tut.hg](tarball://root/attachments/some-uuid/ticket2323/dsage-tut.hg) by yi created at 2008-02-26 18:16:02



---

archive/issue_comments_015455.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-02-27T23:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2323#issuecomment-15455",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_015456.json:
```json
{
    "body": "No dice against my merge tree:\n\n```\nhg unbundle trac_2323_dsage-tut.hg\nadding changesets\ntransaction abort!\nrollback completed\nabort: unknown parent 2af41ec9da8d!\n```\n\nPlease post a flattened patch or tell me which patches to merge first.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-27T23:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2323#issuecomment-15456",
    "user": "mabshoff"
}
```

No dice against my merge tree:

```
hg unbundle trac_2323_dsage-tut.hg
adding changesets
transaction abort!
rollback completed
abort: unknown parent 2af41ec9da8d!
```

Please post a flattened patch or tell me which patches to merge first.

Cheers,

Michael



---

archive/issue_comments_015457.json:
```json
{
    "body": "Attachment [2323.patch](tarball://root/attachments/some-uuid/ticket2323/2323.patch) by mhansen created at 2008-02-27 23:59:41",
    "created_at": "2008-02-27T23:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2323#issuecomment-15457",
    "user": "mhansen"
}
```

Attachment [2323.patch](tarball://root/attachments/some-uuid/ticket2323/2323.patch) by mhansen created at 2008-02-27 23:59:41



---

archive/issue_comments_015458.json:
```json
{
    "body": "Attachment [2323.hg](tarball://root/attachments/some-uuid/ticket2323/2323.hg) by mabshoff created at 2008-02-28 00:13:27\n\nMerged in Sage 2.10.3.rc0. Please indicate clearly that this bundle is against the doc repo since it wasn't immediately clear and it cause some confusion.",
    "created_at": "2008-02-28T00:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2323#issuecomment-15458",
    "user": "mabshoff"
}
```

Attachment [2323.hg](tarball://root/attachments/some-uuid/ticket2323/2323.hg) by mabshoff created at 2008-02-28 00:13:27

Merged in Sage 2.10.3.rc0. Please indicate clearly that this bundle is against the doc repo since it wasn't immediately clear and it cause some confusion.



---

archive/issue_comments_015459.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T00:13:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2323#issuecomment-15459",
    "user": "mabshoff"
}
```

Resolution: fixed
