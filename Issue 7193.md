# Issue 7193: os x 10.6 -- print warning about Sage being broken, so we can release

archive/issues_007193.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @jasongrout\n\nSince *everybody* is totally stumped about how to fix Sage on OS X 10.6, let's release but print a big warning message about the one remaining bug. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7193\n\n",
    "created_at": "2009-10-12T05:10:01Z",
    "labels": [
        "component: algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "os x 10.6 -- print warning about Sage being broken, so we can release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7193",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @jasongrout

Since *everybody* is totally stumped about how to fix Sage on OS X 10.6, let's release but print a big warning message about the one remaining bug. 

Issue created by migration from https://trac.sagemath.org/ticket/7193





---

archive/issue_comments_059518.json:
```json
{
    "body": "Attachment [trac_7193.patch](tarball://root/attachments/some-uuid/ticket7193/trac_7193.patch) by @williamstein created at 2009-10-12 05:11:26",
    "created_at": "2009-10-12T05:11:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59518",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7193.patch](tarball://root/attachments/some-uuid/ticket7193/trac_7193.patch) by @williamstein created at 2009-10-12 05:11:26



---

archive/issue_comments_059519.json:
```json
{
    "body": "I'd love to referee this, but I don't have access to a 10.6 machine, so I can't verify that it works.",
    "created_at": "2009-10-12T23:09:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59519",
    "user": "https://github.com/jasongrout"
}
```

I'd love to referee this, but I don't have access to a 10.6 machine, so I can't verify that it works.



---

archive/issue_comments_059520.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-12T23:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59520",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059521.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-10-13T03:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59521",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059522.json:
```json
{
    "body": "Shouldn't this use the python platform module, rather than os.uname?\n\nhttp://docs.python.org/library/platform.html",
    "created_at": "2009-10-13T03:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59522",
    "user": "https://github.com/jasongrout"
}
```

Shouldn't this use the python platform module, rather than os.uname?

http://docs.python.org/library/platform.html



---

archive/issue_comments_059523.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2009-10-13T03:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59523",
    "user": "https://github.com/jasongrout"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_059524.json:
```json
{
    "body": "if you use the python platform module, you can check specifically for 10.6:\n\n\n```\n>>> platform.mac_ver()\n('10.6.1', ('', '', ''), 'i386')\n```\n\n\nHowever, it might be nice to warn people on 10.5 that 10.6 will not work to prevent people from upgrading.  What do you think?",
    "created_at": "2009-10-13T03:46:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59524",
    "user": "https://github.com/jasongrout"
}
```

if you use the python platform module, you can check specifically for 10.6:


```
>>> platform.mac_ver()
('10.6.1', ('', '', ''), 'i386')
```


However, it might be nice to warn people on 10.5 that 10.6 will not work to prevent people from upgrading.  What do you think?



---

archive/issue_comments_059525.json:
```json
{
    "body": "Replying to [comment:5 jason]:\n> if you use the python platform module, you can check specifically for 10.6:\n\nI think the test `if os.uname()[2] == \"10.0.0\"` does check specifically for 10.6.  If you're running OS X 10.5, then os.uname()[2] returns \"9.8.0\" (at least on my machine.  (On the other hand, `platform.mac_ver()` doesn't return anything with 10.5: I get `(*, (*, *, *), '')` as output.)\n\nAs for the warning, in addition or instead, should we put a notice up on sagemath.org, on the Mac download page?",
    "created_at": "2009-10-13T04:49:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59525",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:5 jason]:
> if you use the python platform module, you can check specifically for 10.6:

I think the test `if os.uname()[2] == "10.0.0"` does check specifically for 10.6.  If you're running OS X 10.5, then os.uname()[2] returns "9.8.0" (at least on my machine.  (On the other hand, `platform.mac_ver()` doesn't return anything with 10.5: I get `(*, (*, *, *), '')` as output.)

As for the warning, in addition or instead, should we put a notice up on sagemath.org, on the Mac download page?



---

archive/issue_comments_059526.json:
```json
{
    "body": "I'm changing this back to needs review, in light of John's comments.",
    "created_at": "2009-10-13T05:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59526",
    "user": "https://github.com/williamstein"
}
```

I'm changing this back to needs review, in light of John's comments.



---

archive/issue_comments_059527.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-10-13T05:49:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59527",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_059528.json:
```json
{
    "body": "Changing component from algebra to distribution.",
    "created_at": "2009-10-19T04:12:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59528",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to distribution.



---

archive/issue_comments_059529.json:
```json
{
    "body": "In light of the recent message [here](http://groups.google.com/group/sage-support/browse_thread/thread/eaf6f141dab9ae54/90f42dab4f2884ac?show_docid=90f42dab4f2884ac), has enough testing been done to close this?",
    "created_at": "2009-10-20T05:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59529",
    "user": "https://github.com/kcrisman"
}
```

In light of the recent message [here](http://groups.google.com/group/sage-support/browse_thread/thread/eaf6f141dab9ae54/90f42dab4f2884ac?show_docid=90f42dab4f2884ac), has enough testing been done to close this?



---

archive/issue_comments_059530.json:
```json
{
    "body": ">  In light of the recent message  here, has enough testing been done to close this?\n\nNo, that is orthogonal.",
    "created_at": "2009-11-11T19:03:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59530",
    "user": "https://github.com/williamstein"
}
```

>  In light of the recent message  here, has enough testing been done to close this?

No, that is orthogonal.



---

archive/issue_comments_059531.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-11T19:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59531",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_059532.json:
```json
{
    "body": "The line\n`if os.uname()[2] == \"10.0.0\"`\nmust be changed, since in new versions of 10.6 we have\n\n```\nsage: os.uname()[2]\n'10.2.0'\n```\n",
    "created_at": "2009-11-11T19:04:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59532",
    "user": "https://github.com/williamstein"
}
```

The line
`if os.uname()[2] == "10.0.0"`
must be changed, since in new versions of 10.6 we have

```
sage: os.uname()[2]
'10.2.0'
```




---

archive/issue_comments_059533.json:
```json
{
    "body": "Attachment [trac_7193-part2.patch](tarball://root/attachments/some-uuid/ticket7193/trac_7193-part2.patch) by @williamstein created at 2009-11-11 19:08:51",
    "created_at": "2009-11-11T19:08:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59533",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_7193-part2.patch](tarball://root/attachments/some-uuid/ticket7193/trac_7193-part2.patch) by @williamstein created at 2009-11-11 19:08:51



---

archive/issue_comments_059534.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-11T19:09:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59534",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_059535.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-11T20:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59535",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059536.json:
```json
{
    "body": "In verifying this, I cheated a bit.\n\n(I've only got OS X 10.4, so I had to replace one \"10\" with an \"8\", just for the sake of the test of course.)",
    "created_at": "2009-11-11T20:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59536",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

In verifying this, I cheated a bit.

(I've only got OS X 10.4, so I had to replace one "10" with an "8", just for the sake of the test of course.)



---

archive/issue_comments_059537.json:
```json
{
    "body": "BTW: One has to apply both patches, first the original one, then the \"part2\" one.",
    "created_at": "2009-11-11T20:53:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59537",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

BTW: One has to apply both patches, first the original one, then the "part2" one.



---

archive/issue_comments_059538.json:
```json
{
    "body": "(For what it's worth, I checked on the machines I have easy access to: on 10.5, `os.uname()[2]` returns \"9.8.0\", on 10.6, it returns \"10.0.0\", and on 10.6.2, it returns \"10.2.0\".)",
    "created_at": "2009-11-11T20:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59538",
    "user": "https://github.com/jhpalmieri"
}
```

(For what it's worth, I checked on the machines I have easy access to: on 10.5, `os.uname()[2]` returns "9.8.0", on 10.6, it returns "10.0.0", and on 10.6.2, it returns "10.2.0".)



---

archive/issue_comments_059539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:05:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7193#issuecomment-59539",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007412.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-11-12T06:05:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7193",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7193#event-7412"
}
```
