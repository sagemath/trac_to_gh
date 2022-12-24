# Issue 6617: remove stale SageTeX files from latex_embed

archive/issues_006617.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: sagetex latex_embed\n\nThe directory `$SAGE_ROOT/examples/latex_embed` contains an old version of SageTeX, which is now a full-fledged Sage package. We should delete these old files. The attached patch does this, leaving behind just a pointer to the current SageTeX stuff.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6617\n\n",
    "created_at": "2009-07-25T12:30:24Z",
    "labels": [
        "distribution",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "remove stale SageTeX files from latex_embed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6617",
    "user": "ddrake"
}
```
Assignee: tbd

Keywords: sagetex latex_embed

The directory `$SAGE_ROOT/examples/latex_embed` contains an old version of SageTeX, which is now a full-fledged Sage package. We should delete these old files. The attached patch does this, leaving behind just a pointer to the current SageTeX stuff.

Issue created by migration from https://trac.sagemath.org/ticket/6617





---

archive/issue_comments_054214.json:
```json
{
    "body": "Attachment [trac_6617.patch](tarball://root/attachments/some-uuid/ticket6617/trac_6617.patch) by ddrake created at 2009-07-25 12:42:28",
    "created_at": "2009-07-25T12:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54214",
    "user": "ddrake"
}
```

Attachment [trac_6617.patch](tarball://root/attachments/some-uuid/ticket6617/trac_6617.patch) by ddrake created at 2009-07-25 12:42:28



---

archive/issue_comments_054215.json:
```json
{
    "body": "I don't know if the attached patch will do this, but be sure that the PDF files in that directory are also deleted. There should only be a README file remaining.",
    "created_at": "2009-07-25T13:03:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54215",
    "user": "ddrake"
}
```

I don't know if the attached patch will do this, but be sure that the PDF files in that directory are also deleted. There should only be a README file remaining.



---

archive/issue_comments_054216.json:
```json
{
    "body": "Changing assignee from tbd to ddrake.",
    "created_at": "2009-07-25T13:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54216",
    "user": "ddrake"
}
```

Changing assignee from tbd to ddrake.



---

archive/issue_comments_054217.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-25T13:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54217",
    "user": "ddrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054218.json:
```json
{
    "body": "Patch works and cleans directory up. Just one thing: in my installation there is a hidden `.example.sage.py` file left in latex_embed. Is it just here in my installation? If yes, positive review, otherwise we have to investigate where it is coming from ;)",
    "created_at": "2009-07-25T17:04:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54218",
    "user": "schilly"
}
```

Patch works and cleans directory up. Just one thing: in my installation there is a hidden `.example.sage.py` file left in latex_embed. Is it just here in my installation? If yes, positive review, otherwise we have to investigate where it is coming from ;)



---

archive/issue_comments_054219.json:
```json
{
    "body": "I see the hidden file too. I'll update the patch to remove it too.",
    "created_at": "2009-07-25T17:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54219",
    "user": "ddrake"
}
```

I see the hidden file too. I'll update the patch to remove it too.



---

archive/issue_comments_054220.json:
```json
{
    "body": "Oops, I just checked and that file is not tracked. So whoever merges this patch will need to delete that file manually, and perhaps run a \"hg status\" to see if there's any other cruft around.",
    "created_at": "2009-07-25T17:20:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54220",
    "user": "ddrake"
}
```

Oops, I just checked and that file is not tracked. So whoever merges this patch will need to delete that file manually, and perhaps run a "hg status" to see if there's any other cruft around.



---

archive/issue_comments_054221.json:
```json
{
    "body": "Yes, same for me, otherwise i would have updated the patch myself ;)\n\nI confirmed this with the hg.sagemath.org tracker, too. .* files seem to be ignored by hg anyways.\n\nGood, apart from that positive review. So, whoever merges this: **you have to delete a hidden file by hand**!!!",
    "created_at": "2009-07-25T17:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54221",
    "user": "schilly"
}
```

Yes, same for me, otherwise i would have updated the patch myself ;)

I confirmed this with the hg.sagemath.org tracker, too. .* files seem to be ignored by hg anyways.

Good, apart from that positive review. So, whoever merges this: **you have to delete a hidden file by hand**!!!



---

archive/issue_comments_054222.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-25T20:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54222",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054223.json:
```json
{
    "body": "Deleted `SAGE_ROOT/examples/latex_embed/.example.sage.py` by hand, not using\n\n```\nhg remove\n```\n",
    "created_at": "2009-07-25T20:56:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6617#issuecomment-54223",
    "user": "mvngu"
}
```

Deleted `SAGE_ROOT/examples/latex_embed/.example.sage.py` by hand, not using

```
hg remove
```

