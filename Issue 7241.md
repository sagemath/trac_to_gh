# Issue 7241: sage -upgrade will try to redownload spkg's that are already present

archive/issues_007241.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: upgrade\n\nThis causes a problem with flaky internet connections since all of the spkgs have to be able to be downloaded all successfully one right after the other.  It shouldn't try to redownload files that are already present.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7241\n\n",
    "created_at": "2009-10-18T17:41:26Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "sage -upgrade will try to redownload spkg's that are already present",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7241",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

Keywords: upgrade

This causes a problem with flaky internet connections since all of the spkgs have to be able to be downloaded all successfully one right after the other.  It shouldn't try to redownload files that are already present.

Issue created by migration from https://trac.sagemath.org/ticket/7241





---

archive/issue_comments_060014.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-18T17:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7241#issuecomment-60014",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060015.json:
```json
{
    "body": "Attachment [trac_7241.patch](tarball://root/attachments/some-uuid/ticket7241/trac_7241.patch) by @mwhansen created at 2009-10-18 17:44:06\n\nIt would also be nice to have it use a more robust downloader such as cURL or wget if it is present.  The current one doesn't resume downloads.",
    "created_at": "2009-10-18T17:44:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7241#issuecomment-60015",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7241.patch](tarball://root/attachments/some-uuid/ticket7241/trac_7241.patch) by @mwhansen created at 2009-10-18 17:44:06

It would also be nice to have it use a more robust downloader such as cURL or wget if it is present.  The current one doesn't resume downloads.



---

archive/issue_comments_060016.json:
```json
{
    "body": "Attachment [trac_7241-rebase.patch](tarball://root/attachments/some-uuid/ticket7241/trac_7241-rebase.patch) by @hivert created at 2009-11-07 08:56:52",
    "created_at": "2009-11-07T08:56:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7241#issuecomment-60016",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7241-rebase.patch](tarball://root/attachments/some-uuid/ticket7241/trac_7241-rebase.patch) by @hivert created at 2009-11-07 08:56:52



---

archive/issue_comments_060017.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-07T08:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7241#issuecomment-60017",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060018.json:
```json
{
    "body": "For some reason the patch needed a little rebase. I just uploaded a rebased patch which is ready to go. => positive review. \n\nCheers,\n\nFlorent",
    "created_at": "2009-11-07T08:58:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7241#issuecomment-60018",
    "user": "https://github.com/hivert"
}
```

For some reason the patch needed a little rebase. I just uploaded a rebased patch which is ready to go. => positive review. 

Cheers,

Florent



---

archive/issue_comments_060019.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-07T11:58:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7241#issuecomment-60019",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
