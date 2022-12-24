# Issue 2271: Include Antti Ajanki's DLX library

archive/issues_002271.json:
```json
{
    "body": "Assignee: @mwhansen\n\nThe Dancing Links algorithm (DLX) is sweet.  It solves the Exact Cover problem with the quickness.\n\nArguments for including Ajanki's code:\n    1) It's the only Python implementation of DLX I've seen.\n    2) I emailed the author, who happily added the \"or later\" bit after the GPL2\n    3) With my Sage Matrix -> DLXMatrix code (plus docstrings to everything I\nadded), the file dlx.py is only 8kB!\n    4) It will resolve tickets #1311 and #1313\n\nIssue created by migration from https://trac.sagemath.org/ticket/2271\n\n",
    "created_at": "2008-02-22T23:27:49Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "Include Antti Ajanki's DLX library",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2271",
    "user": "boothby"
}
```
Assignee: @mwhansen

The Dancing Links algorithm (DLX) is sweet.  It solves the Exact Cover problem with the quickness.

Arguments for including Ajanki's code:
    1) It's the only Python implementation of DLX I've seen.
    2) I emailed the author, who happily added the "or later" bit after the GPL2
    3) With my Sage Matrix -> DLXMatrix code (plus docstrings to everything I
added), the file dlx.py is only 8kB!
    4) It will resolve tickets #1311 and #1313

Issue created by migration from https://trac.sagemath.org/ticket/2271





---

archive/issue_comments_015055.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-02-22T23:27:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15055",
    "user": "boothby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_015056.json:
```json
{
    "body": "Attachment [2271_adds_DLX.hg](tarball://root/attachments/some-uuid/ticket2271/2271_adds_DLX.hg) by boothby created at 2008-02-22 23:32:33",
    "created_at": "2008-02-22T23:32:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15056",
    "user": "boothby"
}
```

Attachment [2271_adds_DLX.hg](tarball://root/attachments/some-uuid/ticket2271/2271_adds_DLX.hg) by boothby created at 2008-02-22 23:32:33



---

archive/issue_comments_015057.json:
```json
{
    "body": "+1 to include this in Sage.\n\nI haven't formally refereed it.\n\nYou should just attach a single plain text patch instead of an hg bundle.",
    "created_at": "2008-02-22T23:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15057",
    "user": "@williamstein"
}
```

+1 to include this in Sage.

I haven't formally refereed it.

You should just attach a single plain text patch instead of an hg bundle.



---

archive/issue_comments_015058.json:
```json
{
    "body": "Oops, I forgot to add the functions to all.py, so the tests fail.  New patch up in a few.",
    "created_at": "2008-02-23T20:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15058",
    "user": "boothby"
}
```

Oops, I forgot to add the functions to all.py, so the tests fail.  New patch up in a few.



---

archive/issue_comments_015059.json:
```json
{
    "body": "Attachment [2271_adds_DLX.patch](tarball://root/attachments/some-uuid/ticket2271/2271_adds_DLX.patch) by @rlmill created at 2008-02-24 19:32:29\n\nThis patch (although awesome) doesn't quite obey the new doctest-for-every-function rule, since the following functions do not have doctests:\n\n1. `walknodes`\n2. `constructmatrix`\n3. `covercolumn`\n4. `uncovercolumn`\n5. `dosearch`\n6. `solve`",
    "created_at": "2008-02-24T19:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15059",
    "user": "@rlmill"
}
```

Attachment [2271_adds_DLX.patch](tarball://root/attachments/some-uuid/ticket2271/2271_adds_DLX.patch) by @rlmill created at 2008-02-24 19:32:29

This patch (although awesome) doesn't quite obey the new doctest-for-every-function rule, since the following functions do not have doctests:

1. `walknodes`
2. `constructmatrix`
3. `covercolumn`
4. `uncovercolumn`
5. `dosearch`
6. `solve`



---

archive/issue_comments_015060.json:
```json
{
    "body": "Attachment [2271_doctests.patch](tarball://root/attachments/some-uuid/ticket2271/2271_doctests.patch) by boothby created at 2008-02-25 19:59:52",
    "created_at": "2008-02-25T19:59:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15060",
    "user": "boothby"
}
```

Attachment [2271_doctests.patch](tarball://root/attachments/some-uuid/ticket2271/2271_doctests.patch) by boothby created at 2008-02-25 19:59:52



---

archive/issue_comments_015061.json:
```json
{
    "body": "2271_doctests.patch implements world peace, washes your dishes, and makes coffee before your alarm goes off in the morning.  It's truly amazing.  Also, it contains doctests for everything in sight, reworks the DLXMatrix class to be a real python generator class, and implements an iterative formulation of DLX.\n\nIn the creation of these doctests, I have discovered a wondrous resolution of P vs. NP, but the proof was too long to justify appending to the patch.",
    "created_at": "2008-02-25T20:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15061",
    "user": "boothby"
}
```

2271_doctests.patch implements world peace, washes your dishes, and makes coffee before your alarm goes off in the morning.  It's truly amazing.  Also, it contains doctests for everything in sight, reworks the DLXMatrix class to be a real python generator class, and implements an iterative formulation of DLX.

In the creation of these doctests, I have discovered a wondrous resolution of P vs. NP, but the proof was too long to justify appending to the patch.



---

archive/issue_comments_015062.json:
```json
{
    "body": "As well as a round of applause.",
    "created_at": "2008-02-25T20:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15062",
    "user": "@rlmill"
}
```

As well as a round of applause.



---

archive/issue_comments_015063.json:
```json
{
    "body": "Replying to [comment:7 boothby]:\n> 2271_doctests.patch implements world peace, washes your dishes, and makes coffee before your alarm goes off in the morning.  It's truly amazing.  Also, it contains doctests for everything in sight, reworks the DLXMatrix class to be a real python generator class, and implements an iterative formulation of DLX.\n> \n> In the creation of these doctests, I have discovered a wondrous resolution of P vs. NP, but the proof was too long to justify appending to the patch.\n> \n\nI guess you should have written it in the margins :)\n\nCheers,\n\nMichael",
    "created_at": "2008-02-25T20:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15063",
    "user": "mabshoff"
}
```

Replying to [comment:7 boothby]:
> 2271_doctests.patch implements world peace, washes your dishes, and makes coffee before your alarm goes off in the morning.  It's truly amazing.  Also, it contains doctests for everything in sight, reworks the DLXMatrix class to be a real python generator class, and implements an iterative formulation of DLX.
> 
> In the creation of these doctests, I have discovered a wondrous resolution of P vs. NP, but the proof was too long to justify appending to the patch.
> 

I guess you should have written it in the margins :)

Cheers,

Michael



---

archive/issue_comments_015064.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-25T20:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15064",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015065.json:
```json
{
    "body": "Merged 2271_adds_DLX.patch and 2271_doctests.patch in Sage 2.10.3.alpha0 - w00t",
    "created_at": "2008-02-25T20:35:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2271#issuecomment-15065",
    "user": "mabshoff"
}
```

Merged 2271_adds_DLX.patch and 2271_doctests.patch in Sage 2.10.3.alpha0 - w00t
