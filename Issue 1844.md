# Issue 1844: [with bundle] Get doctest coverage in sage/modular/modform up to 100%

archive/issues_001844.json:
```json
{
    "body": "Assignee: craigcitro\n\nThis patch brings doctest coverage up to 100% for every file in sage/modular/modform except for find_generators.py, which isn't imported into sage by default anyway. Needless to say, there are lots of small fixes and whatnot. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1844\n\n",
    "created_at": "2008-01-19T01:50:38Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "[with bundle] Get doctest coverage in sage/modular/modform up to 100%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1844",
    "user": "craigcitro"
}
```
Assignee: craigcitro

This patch brings doctest coverage up to 100% for every file in sage/modular/modform except for find_generators.py, which isn't imported into sage by default anyway. Needless to say, there are lots of small fixes and whatnot. 

Issue created by migration from https://trac.sagemath.org/ticket/1844





---

archive/issue_comments_011673.json:
```json
{
    "body": "Attachment [modform-doctest.hg](tarball://root/attachments/some-uuid/ticket1844/modform-doctest.hg) by mhansen created at 2008-01-19 02:46:45",
    "created_at": "2008-01-19T02:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11673",
    "user": "mhansen"
}
```

Attachment [modform-doctest.hg](tarball://root/attachments/some-uuid/ticket1844/modform-doctest.hg) by mhansen created at 2008-01-19 02:46:45



---

archive/issue_comments_011674.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-19T06:24:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11674",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011675.json:
```json
{
    "body": "I'm adding a patch that one should use *instead* of the .hg bundle above. (It's a patch with *just* the modular form changes, as opposed to a lot of the junk that made it into my bundle.)",
    "created_at": "2008-01-19T06:27:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11675",
    "user": "craigcitro"
}
```

I'm adding a patch that one should use *instead* of the .hg bundle above. (It's a patch with *just* the modular form changes, as opposed to a lot of the junk that made it into my bundle.)



---

archive/issue_comments_011676.json:
```json
{
    "body": "Attachment [1844.patch](tarball://root/attachments/some-uuid/ticket1844/1844.patch) by craigcitro created at 2008-01-19 06:27:39",
    "created_at": "2008-01-19T06:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11676",
    "user": "craigcitro"
}
```

Attachment [1844.patch](tarball://root/attachments/some-uuid/ticket1844/1844.patch) by craigcitro created at 2008-01-19 06:27:39



---

archive/issue_comments_011677.json:
```json
{
    "body": "Attachment [1844-2.patch](tarball://root/attachments/some-uuid/ticket1844/1844-2.patch) by mhansen created at 2008-01-19 07:55:29",
    "created_at": "2008-01-19T07:55:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11677",
    "user": "mhansen"
}
```

Attachment [1844-2.patch](tarball://root/attachments/some-uuid/ticket1844/1844-2.patch) by mhansen created at 2008-01-19 07:55:29



---

archive/issue_comments_011678.json:
```json
{
    "body": "I added a new patch which should apply cleanly against 2.10.",
    "created_at": "2008-01-19T07:55:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11678",
    "user": "mhansen"
}
```

I added a new patch which should apply cleanly against 2.10.



---

archive/issue_comments_011679.json:
```json
{
    "body": "Attachment [1844-2a.patch](tarball://root/attachments/some-uuid/ticket1844/1844-2a.patch) by craigcitro created at 2008-01-19 09:53:41",
    "created_at": "2008-01-19T09:53:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11679",
    "user": "craigcitro"
}
```

Attachment [1844-2a.patch](tarball://root/attachments/some-uuid/ticket1844/1844-2a.patch) by craigcitro created at 2008-01-19 09:53:41



---

archive/issue_comments_011680.json:
```json
{
    "body": "One should apply 1844-2.patch and then 1844-2a.patch from a clean 2.10 install. (The 2a is a very small patch.)\n\nThis should be ready to go. *crosses fingers*",
    "created_at": "2008-01-19T09:55:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11680",
    "user": "craigcitro"
}
```

One should apply 1844-2.patch and then 1844-2a.patch from a clean 2.10 install. (The 2a is a very small patch.)

This should be ready to go. *crosses fingers*



---

archive/issue_comments_011681.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-21T04:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11681",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011682.json:
```json
{
    "body": "Merged 1844-2.patch and 1844-2a.patch in Sage 2.10.1.alpha1 - finally :)",
    "created_at": "2008-01-21T04:26:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1844",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1844#issuecomment-11682",
    "user": "mabshoff"
}
```

Merged 1844-2.patch and 1844-2a.patch in Sage 2.10.1.alpha1 - finally :)
