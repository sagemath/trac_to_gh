# Issue 7610: `readline-6.0` causes "undefined symbol: PC" errors on Arch Linux

archive/issues_007610.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  drkirkby alexghitza\n\nOn running Sage or the next build, readline fails with:\n\n\n```\nbash: symbol lookup error: /opt/sage-bin/local/lib/libreadline.so.6: undefined symbol: PC\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7610\n\n",
    "created_at": "2009-12-06T02:43:36Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "`readline-6.0` causes \"undefined symbol: PC\" errors on Arch Linux",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7610",
    "user": "https://github.com/TimDumol"
}
```
Assignee: tbd

CC:  drkirkby alexghitza

On running Sage or the next build, readline fails with:


```
bash: symbol lookup error: /opt/sage-bin/local/lib/libreadline.so.6: undefined symbol: PC
```


Issue created by migration from https://trac.sagemath.org/ticket/7610





---

archive/issue_comments_064880.json:
```json
{
    "body": "Attachment [trac_7610-readline-arch-workaround.patch](tarball://root/attachments/some-uuid/ticket7610/trac_7610-readline-arch-workaround.patch) by @TimDumol created at 2009-12-06 02:54:38\n\nAdds Arch Linux workaround (copies over system library)",
    "created_at": "2009-12-06T02:54:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7610#issuecomment-64880",
    "user": "https://github.com/TimDumol"
}
```

Attachment [trac_7610-readline-arch-workaround.patch](tarball://root/attachments/some-uuid/ticket7610/trac_7610-readline-arch-workaround.patch) by @TimDumol created at 2009-12-06 02:54:38

Adds Arch Linux workaround (copies over system library)



---

archive/issue_comments_064881.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-06T02:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7610#issuecomment-64881",
    "user": "https://github.com/TimDumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064882.json:
```json
{
    "body": "This patch adds the standard workaround (copying over the system package to $SAGE_LOCAL/lib). This should not ever fail since `readline` is in the `base` repository, and so should be installed in all systems.\n\nOriginally I thought it was because readline linked to termcap, which is disabled in Arch, but linking to curses did not help.",
    "created_at": "2009-12-06T02:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7610#issuecomment-64882",
    "user": "https://github.com/TimDumol"
}
```

This patch adds the standard workaround (copying over the system package to $SAGE_LOCAL/lib). This should not ever fail since `readline` is in the `base` repository, and so should be installed in all systems.

Originally I thought it was because readline linked to termcap, which is disabled in Arch, but linking to curses did not help.



---

archive/issue_comments_064883.json:
```json
{
    "body": "I've also added double quotes around almost all variable references (otherwise, there will be issues if there are spaces in the path to $SAGE_LOCAL, etc.)",
    "created_at": "2009-12-06T02:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7610#issuecomment-64883",
    "user": "https://github.com/TimDumol"
}
```

I've also added double quotes around almost all variable references (otherwise, there will be issues if there are spaces in the path to $SAGE_LOCAL, etc.)



---

archive/issue_comments_064884.json:
```json
{
    "body": "I've merge http://sage.math.washington.edu/home/mhansen/readline-6.0.p1.spkg which has these changes applied on top of the ones at #7164.",
    "created_at": "2009-12-09T02:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7610#issuecomment-64884",
    "user": "https://github.com/mwhansen"
}
```

I've merge http://sage.math.washington.edu/home/mhansen/readline-6.0.p1.spkg which has these changes applied on top of the ones at #7164.



---

archive/issue_comments_064885.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-09T02:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7610#issuecomment-64885",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_007836.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-12-09T02:34:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7610#event-7836"
}
```



---

archive/issue_comments_064886.json:
```json
{
    "body": "Replying to [ticket:7610 timdumol]:\n> On running Sage or the next build, readline fails with:\n> \n\n```\nbash: symbol lookup error: /opt/sage-bin/local/lib/libreadline.so.6: undefined symbol: PC\n```\n\n\nThis is because our shared libreadline lacks a `DT_NEEDED` tag for libtermcap, libncurses, libtinfo or whichever library provides these symbols (depends on the OS / distro).\n\nI have a readline 6.2.p2 spkg which fixes this, but haven't yet opened a ticket for it...\n\n(Just in case someone searches for this error and ends up here.)",
    "created_at": "2011-10-29T22:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7610#issuecomment-64886",
    "user": "https://github.com/nexttime"
}
```

Replying to [ticket:7610 timdumol]:
> On running Sage or the next build, readline fails with:
> 

```
bash: symbol lookup error: /opt/sage-bin/local/lib/libreadline.so.6: undefined symbol: PC
```


This is because our shared libreadline lacks a `DT_NEEDED` tag for libtermcap, libncurses, libtinfo or whichever library provides these symbols (depends on the OS / distro).

I have a readline 6.2.p2 spkg which fixes this, but haven't yet opened a ticket for it...

(Just in case someone searches for this error and ends up here.)
