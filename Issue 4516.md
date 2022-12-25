# Issue 4516: make check on binaries should smoothly 100% pass -- right now it fails on the docs and gives lots of verbosity at the start, and #4515

archive/issues_004516.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4516\n\n",
    "created_at": "2008-11-13T22:59:26Z",
    "labels": [
        "component: distribution",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "make check on binaries should smoothly 100% pass -- right now it fails on the docs and gives lots of verbosity at the start, and #4515",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4516",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff



Issue created by migration from https://trac.sagemath.org/ticket/4516





---

archive/issue_comments_033458.json:
```json
{
    "body": "The main bug is that the devel/doc directory isn't copied into the bdist.  This is because of a stupid bug in local/bin/sage-bdist, which is fixed by the attached 1-line patch. \n\nTo test this, apply the patch, do \"./sage -bdist\" then look in the SAGE_ROOT/dist directory and confirm that the resulting binary has a devel/doc directory.",
    "created_at": "2008-11-14T00:45:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4516#issuecomment-33458",
    "user": "https://github.com/williamstein"
}
```

The main bug is that the devel/doc directory isn't copied into the bdist.  This is because of a stupid bug in local/bin/sage-bdist, which is fixed by the attached 1-line patch. 

To test this, apply the patch, do "./sage -bdist" then look in the SAGE_ROOT/dist directory and confirm that the resulting binary has a devel/doc directory.



---

archive/issue_comments_033459.json:
```json
{
    "body": "Attachment [scripts-4516.patch](tarball://root/attachments/some-uuid/ticket4516/scripts-4516.patch) by GeorgSWeber created at 2008-11-14 22:39:43\n\nBy chance, I had experimented with \"sage -bdist\" on Sage 3.2.alpha2, so I could verify that indeed, without this patch the \"devel/doc-main\" directory is missing.\n\nWith this patch applied, it is there after \"sage-bdist\".",
    "created_at": "2008-11-14T22:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4516#issuecomment-33459",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Attachment [scripts-4516.patch](tarball://root/attachments/some-uuid/ticket4516/scripts-4516.patch) by GeorgSWeber created at 2008-11-14 22:39:43

By chance, I had experimented with "sage -bdist" on Sage 3.2.alpha2, so I could verify that indeed, without this patch the "devel/doc-main" directory is missing.

With this patch applied, it is there after "sage-bdist".



---

archive/issue_comments_033460.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T05:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4516#issuecomment-33460",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004761.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-11-15T05:04:50Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4516",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4516#event-4761"
}
```



---

archive/issue_comments_033461.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-15T05:04:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4516",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4516#issuecomment-33461",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc1
