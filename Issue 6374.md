# Issue 6374: [with patch, needs review] Fix race condition in sage build process

archive/issues_006374.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  ncalexan georgsweber\n\nSo on #6234, there was a second patch to fix a race condition that Nick saw during the 4.0.2 release cycle. Someone else just ran into this, and I noticed that the second patch from that ticket somehow didn't make it into Sage. (Oops.)\n\nI'm attaching the patch here, with the same filename -- see #6234 (at the bottom) for an example of the bad behavior and an explanation for the fix. It's already been reviewed at least once, but a second review wouldn't hurt. ;)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6374\n\n",
    "created_at": "2009-06-20T20:41:41Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "title": "[with patch, needs review] Fix race condition in sage build process",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6374",
    "user": "craigcitro"
}
```
Assignee: tbd

CC:  ncalexan georgsweber

So on #6234, there was a second patch to fix a race condition that Nick saw during the 4.0.2 release cycle. Someone else just ran into this, and I noticed that the second patch from that ticket somehow didn't make it into Sage. (Oops.)

I'm attaching the patch here, with the same filename -- see #6234 (at the bottom) for an example of the bad behavior and an explanation for the fix. It's already been reviewed at least once, but a second review wouldn't hurt. ;)

Issue created by migration from https://trac.sagemath.org/ticket/6374





---

archive/issue_comments_051016.json:
```json
{
    "body": "Attachment\n\nAt least twice, I ran into the failure (hopefully) fixed by this ticket. I already volunteered to review it (in a note on sage-release), but if somebody else is faster, OK.",
    "created_at": "2009-07-16T22:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6374#issuecomment-51016",
    "user": "GeorgSWeber"
}
```

Attachment

At least twice, I ran into the failure (hopefully) fixed by this ticket. I already volunteered to review it (in a note on sage-release), but if somebody else is faster, OK.



---

archive/issue_comments_051017.json:
```json
{
    "body": "Works fine for/with Sage-4.1.1.alpha0. It's hard to \"prove\" that a certain sporadic failures has been fixed, but the patch at least doesn't hurt. And it is plausible that it does help indeed.",
    "created_at": "2009-07-22T19:59:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6374#issuecomment-51017",
    "user": "GeorgSWeber"
}
```

Works fine for/with Sage-4.1.1.alpha0. It's hard to "prove" that a certain sporadic failures has been fixed, but the patch at least doesn't hurt. And it is plausible that it does help indeed.



---

archive/issue_comments_051018.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T01:43:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6374",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6374#issuecomment-51018",
    "user": "mvngu"
}
```

Resolution: fixed
