# Issue 6075: dsage is not yet entirely optional

archive/issues_006075.json:
```json
{
    "body": "Assignee: @yqiang\n\nCC:  @craigcitro\n\nKeywords: dsage optional spkg\n\nFor 4.0, dsage was made an optional spkg.  However, if I rm -rf build/ and sage -ba, the newly built tree has no dsage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6075\n\n",
    "created_at": "2009-05-18T21:02:20Z",
    "labels": [
        "component: dsage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "dsage is not yet entirely optional",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6075",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @yqiang

CC:  @craigcitro

Keywords: dsage optional spkg

For 4.0, dsage was made an optional spkg.  However, if I rm -rf build/ and sage -ba, the newly built tree has no dsage.

Issue created by migration from https://trac.sagemath.org/ticket/6075





---

archive/issue_comments_048264.json:
```json
{
    "body": "Changing assignee from @yqiang to @mwhansen.",
    "created_at": "2009-05-26T20:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48264",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from @yqiang to @mwhansen.



---

archive/issue_comments_048265.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-26T20:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48265",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_048266.json:
```json
{
    "body": "I've added a patch that makes things continue to work if dsage is not there.  However, we really should make it so that dsage does not install into sage.dsage.  This requires quite a few more changes within dsage itself.",
    "created_at": "2009-05-26T20:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48266",
    "user": "https://github.com/mwhansen"
}
```

I've added a patch that makes things continue to work if dsage is not there.  However, we really should make it so that dsage does not install into sage.dsage.  This requires quite a few more changes within dsage itself.



---

archive/issue_comments_048267.json:
```json
{
    "body": "Attachment [trac_6075.patch](tarball://root/attachments/some-uuid/ticket6075/trac_6075.patch) by @mwhansen created at 2009-05-28 02:44:46",
    "created_at": "2009-05-28T02:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48267",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_6075.patch](tarball://root/attachments/some-uuid/ticket6075/trac_6075.patch) by @mwhansen created at 2009-05-28 02:44:46



---

archive/issue_comments_048268.json:
```json
{
    "body": "I updated the patch and made http://sage.math.washington.edu/home/mhansen/dsage-1.0.1.spkg which moves DSage from sage.dsage to just dsage.",
    "created_at": "2009-05-28T02:47:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48268",
    "user": "https://github.com/mwhansen"
}
```

I updated the patch and made http://sage.math.washington.edu/home/mhansen/dsage-1.0.1.spkg which moves DSage from sage.dsage to just dsage.



---

archive/issue_comments_048269.json:
```json
{
    "body": "Yep, this looks good. You have to manually remove `$SAGE_ROOT/devel/sage/build/sage/dsage` to see that this completely works, but then, that's exactly what the patch at #5977 does for you ...",
    "created_at": "2009-05-28T04:57:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48269",
    "user": "https://github.com/craigcitro"
}
```

Yep, this looks good. You have to manually remove `$SAGE_ROOT/devel/sage/build/sage/dsage` to see that this completely works, but then, that's exactly what the patch at #5977 does for you ...



---

archive/issue_comments_048270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-28T05:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48270",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_006329.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-05-28T05:07:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6075#event-6329"
}
```



---

archive/issue_comments_048271.json:
```json
{
    "body": "Merged in 4.0.rc1.",
    "created_at": "2009-05-28T05:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6075",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6075#issuecomment-48271",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.rc1.
