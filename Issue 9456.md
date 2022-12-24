# Issue 9456: zlib should be a prerequisite for libpng

archive/issues_009456.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby\n\nFrom the libpng INSTALL file:\n\n```\nBefore installing libpng, you must first install zlib\n```\n\nSo fix the file \"deps\" accordingly.  (This issue arose when building spkg's in parallel: the build failed when it reached libpng because zlib wasn't installed yet.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/9456\n\n",
    "created_at": "2010-07-08T15:21:45Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "zlib should be a prerequisite for libpng",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9456",
    "user": "@jhpalmieri"
}
```
Assignee: tbd

CC:  drkirkby

From the libpng INSTALL file:

```
Before installing libpng, you must first install zlib
```

So fix the file "deps" accordingly.  (This issue arose when building spkg's in parallel: the build failed when it reached libpng because zlib wasn't installed yet.)

Issue created by migration from https://trac.sagemath.org/ticket/9456





---

archive/issue_comments_090621.json:
```json
{
    "body": "That's perfectly logical. Positive review.",
    "created_at": "2010-07-08T15:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90621",
    "user": "drkirkby"
}
```

That's perfectly logical. Positive review.



---

archive/issue_comments_090622.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-08T15:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90622",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090623.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-08T15:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90623",
    "user": "drkirkby"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090624.json:
```json
{
    "body": "I'm upgrading this to a blocker because there is a patch and I hit it every time I try to build sage on the skynet machine iras with parallel spkg building: the build fails on libpng, then I have to restart it.  (Usually libpng and zlib are built at the same time on this machine, so after libpng fails, zlib builds successfully, so running \"make\" again works fine.)",
    "created_at": "2010-07-22T23:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90624",
    "user": "@jhpalmieri"
}
```

I'm upgrading this to a blocker because there is a patch and I hit it every time I try to build sage on the skynet machine iras with parallel spkg building: the build fails on libpng, then I have to restart it.  (Usually libpng and zlib are built at the same time on this machine, so after libpng fails, zlib builds successfully, so running "make" again works fine.)



---

archive/issue_comments_090625.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-07-22T23:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90625",
    "user": "@jhpalmieri"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_090626.json:
```json
{
    "body": "I've put the deps file here in SAGE_ROOT/spkg/standard for 4.5.2.alpha1.",
    "created_at": "2010-07-23T00:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90626",
    "user": "@dandrake"
}
```

I've put the deps file here in SAGE_ROOT/spkg/standard for 4.5.2.alpha1.



---

archive/issue_comments_090627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-23T00:00:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90627",
    "user": "@dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_090628.json:
```json
{
    "body": "I'm sorry, I have screwed up here, and attached these files to the wrong ticket! Instead of attaching them to #9598, I've attached them here. \n\nSince this has not been merged, it's probably not a fatal screw up. Sorry. \n\nI will attempt to put the files back as they should be.",
    "created_at": "2010-07-26T09:50:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90628",
    "user": "drkirkby"
}
```

I'm sorry, I have screwed up here, and attached these files to the wrong ticket! Instead of attaching them to #9598, I've attached them here. 

Since this has not been merged, it's probably not a fatal screw up. Sorry. 

I will attempt to put the files back as they should be.



---

archive/issue_comments_090629.json:
```json
{
    "body": "Replying to [comment:5 drkirkby]:\n\n> Since this has not been merged, it's probably not a fatal screw up. Sorry. \n\nI mean it has been merged, so it should not be a big deal. But I will attempt to put the files back as they should be.",
    "created_at": "2010-07-26T09:51:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90629",
    "user": "drkirkby"
}
```

Replying to [comment:5 drkirkby]:

> Since this has not been merged, it's probably not a fatal screw up. Sorry. 

I mean it has been merged, so it should not be a big deal. But I will attempt to put the files back as they should be.



---

archive/issue_comments_090630.json:
```json
{
    "body": "I've tried to correct this, but have failed. I'm going to delete this, and raise it on sage-devel. \n\nDave",
    "created_at": "2010-07-26T10:04:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90630",
    "user": "drkirkby"
}
```

I've tried to correct this, but have failed. I'm going to delete this, and raise it on sage-devel. 

Dave



---

archive/issue_comments_090631.json:
```json
{
    "body": "Attachment [deps](tarball://root/attachments/some-uuid/ticket9456/deps) by drkirkby created at 2010-07-26 10:20:07\n\nspkg/standard/deps file, written by John and merged into sage-4.5.2.alpha1 which I overwrote by mistake. I'm 99% sure this is right.",
    "created_at": "2010-07-26T10:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90631",
    "user": "drkirkby"
}
```

Attachment [deps](tarball://root/attachments/some-uuid/ticket9456/deps) by drkirkby created at 2010-07-26 10:20:07

spkg/standard/deps file, written by John and merged into sage-4.5.2.alpha1 which I overwrote by mistake. I'm 99% sure this is right.



---

archive/issue_comments_090632.json:
```json
{
    "body": "Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9456/deps.diff) by drkirkby created at 2010-07-26 10:21:07\n\ndiff of spkg/standard/deps written by john which I overwrote by mistake. I'm 99% sure this is right.",
    "created_at": "2010-07-26T10:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90632",
    "user": "drkirkby"
}
```

Attachment [deps.diff](tarball://root/attachments/some-uuid/ticket9456/deps.diff) by drkirkby created at 2010-07-26 10:21:07

diff of spkg/standard/deps written by john which I overwrote by mistake. I'm 99% sure this is right.



---

archive/issue_comments_090633.json:
```json
{
    "body": "I believe these are correct. Perhaps someone else can check. \n\nDave",
    "created_at": "2010-07-26T10:42:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9456",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9456#issuecomment-90633",
    "user": "drkirkby"
}
```

I believe these are correct. Perhaps someone else can check. 

Dave
