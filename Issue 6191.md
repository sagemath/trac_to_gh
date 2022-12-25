# Issue 6191: atlas -- make it so SAGE_FAT_BINARY only used on x86

archive/issues_006191.json:
```json
{
    "body": "Assignee: tbd\n\nI couldn't build atlas on itanium and was puzzled why.  It turns out I had the SAGE_FAT_BINARY environ variable set.    This update to the atlas spkg fixes it so that environ variable has no impact on itanium.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6191\n\n",
    "created_at": "2009-06-02T21:31:27Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "atlas -- make it so SAGE_FAT_BINARY only used on x86",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6191",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

I couldn't build atlas on itanium and was puzzled why.  It turns out I had the SAGE_FAT_BINARY environ variable set.    This update to the atlas spkg fixes it so that environ variable has no impact on itanium.



Issue created by migration from https://trac.sagemath.org/ticket/6191





---

archive/issue_comments_049357.json:
```json
{
    "body": "The spkg is here: http://sage.math.washington.edu/home/wstein/release/4.0.1/alpha0/stuff/atlas-3.8.3.p3.spkg",
    "created_at": "2009-06-02T21:31:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6191#issuecomment-49357",
    "user": "https://github.com/williamstein"
}
```

The spkg is here: http://sage.math.washington.edu/home/wstein/release/4.0.1/alpha0/stuff/atlas-3.8.3.p3.spkg



---

archive/issue_comments_049358.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-06-02T21:32:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6191#issuecomment-49358",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_049359.json:
```json
{
    "body": "Changes look good to me.\n\nMerged in 4.0.1.rc0.",
    "created_at": "2009-06-04T06:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6191#issuecomment-49359",
    "user": "https://github.com/mwhansen"
}
```

Changes look good to me.

Merged in 4.0.1.rc0.



---

archive/issue_events_006439.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T06:39:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6191",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6191#event-6439"
}
```



---

archive/issue_comments_049360.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T06:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6191#issuecomment-49360",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
