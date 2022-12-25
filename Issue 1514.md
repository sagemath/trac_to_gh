# Issue 1514: fix breakage and lameness in foo? and foo?? especially in the notebook.

archive/issues_001514.json:
```json
{
    "body": "Assignee: boothby\n\nI'm sick of foo? or foo?? failing with tracebacks.  They should never do that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1514\n\n",
    "created_at": "2007-12-15T00:17:52Z",
    "labels": [
        "component: notebook",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "fix breakage and lameness in foo? and foo?? especially in the notebook.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1514",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

I'm sick of foo? or foo?? failing with tracebacks.  They should never do that.

Issue created by migration from https://trac.sagemath.org/ticket/1514





---

archive/issue_comments_009679.json:
```json
{
    "body": "Attachment [trac-1514.patch](tarball://root/attachments/some-uuid/ticket1514/trac-1514.patch) by @williamstein created at 2007-12-15 01:45:04",
    "created_at": "2007-12-15T01:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1514#issuecomment-9679",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac-1514.patch](tarball://root/attachments/some-uuid/ticket1514/trac-1514.patch) by @williamstein created at 2007-12-15 01:45:04



---

archive/issue_comments_009680.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-12-15T05:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1514#issuecomment-9680",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_009681.json:
```json
{
    "body": "\n```\n[9:43pm] cwitty-rvw-1514: wstein-rvw-1119, it looks like #1514 does not have any doctests for whatever bugs you are fixing?\n[9:43pm] craigcitro: gmp comes before pari in the build order for libcsage\n[9:44pm] wstein-rvw-1119: cwitty-1514 -- the buginess is that nothing works at all.\n[9:44pm] wstein-rvw-1119: it's hard to have a doctest for that.\n[9:44pm] wstein-rvw-1119: However, notice the first line of the patch, which turns *on* doctesting for the sageinspect.py file\n[9:44pm] wstein-rvw-1119: So there are many new doctests as a result.\n[9:45pm] wstein-rvw-1119: It's really a design change anyway -- to use the files in SAGE_ROOT/devel/sage/sage instead of SAGE_ROOT/local/lib/python/site-packages/sage/,\n[9:45pm] wstein-rvw-1119: since for some reason often some .pyx files or other files that are relevant don't get copied over there.\n[9:45pm] wstein-rvw-1119: But SAGE_ROOT/devel/sage/sage does.\n```\n",
    "created_at": "2007-12-15T05:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1514#issuecomment-9681",
    "user": "https://github.com/williamstein"
}
```


```
[9:43pm] cwitty-rvw-1514: wstein-rvw-1119, it looks like #1514 does not have any doctests for whatever bugs you are fixing?
[9:43pm] craigcitro: gmp comes before pari in the build order for libcsage
[9:44pm] wstein-rvw-1119: cwitty-1514 -- the buginess is that nothing works at all.
[9:44pm] wstein-rvw-1119: it's hard to have a doctest for that.
[9:44pm] wstein-rvw-1119: However, notice the first line of the patch, which turns *on* doctesting for the sageinspect.py file
[9:44pm] wstein-rvw-1119: So there are many new doctests as a result.
[9:45pm] wstein-rvw-1119: It's really a design change anyway -- to use the files in SAGE_ROOT/devel/sage/sage instead of SAGE_ROOT/local/lib/python/site-packages/sage/,
[9:45pm] wstein-rvw-1119: since for some reason often some .pyx files or other files that are relevant don't get copied over there.
[9:45pm] wstein-rvw-1119: But SAGE_ROOT/devel/sage/sage does.
```




---

archive/issue_comments_009682.json:
```json
{
    "body": "Attachment [trac-1514-fixdoctest.patch](tarball://root/attachments/some-uuid/ticket1514/trac-1514-fixdoctest.patch) by cwitty created at 2007-12-15 06:07:56",
    "created_at": "2007-12-15T06:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1514#issuecomment-9682",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac-1514-fixdoctest.patch](tarball://root/attachments/some-uuid/ticket1514/trac-1514-fixdoctest.patch) by cwitty created at 2007-12-15 06:07:56



---

archive/issue_comments_009683.json:
```json
{
    "body": "Looks good to me; fixes doctests.\n\nApply both patches.",
    "created_at": "2007-12-15T06:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1514#issuecomment-9683",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good to me; fixes doctests.

Apply both patches.



---

archive/issue_comments_009684.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-15T07:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1514#issuecomment-9684",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_009685.json:
```json
{
    "body": "Merged in 2.9.rc0.",
    "created_at": "2007-12-15T07:21:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1514",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1514#issuecomment-9685",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc0.
