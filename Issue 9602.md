# Issue 9602: Fix gap on FreeBSD

archive/issues_009602.json:
```json
{
    "body": "Assignee: @peterjeremy\n\ngap sysfiles.c is very host-dependent.  Current code includes a mixture of SYS_xxx and HAVE_xxx_H tests.  Whilst SYS_BSD might appear logical for FreeBSD, there is no testing for this, and recent FreeBSD variants support termios.h.\n\nThe attached patches (mostly taken from the FreeBSD port) add tests for HAVE_TERMIOS_H to make gap compile on FreeBSD 8.x.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9602\n\n",
    "created_at": "2010-07-26T11:22:14Z",
    "labels": [
        "component: porting: bsd",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix gap on FreeBSD",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9602",
    "user": "https://github.com/peterjeremy"
}
```
Assignee: @peterjeremy

gap sysfiles.c is very host-dependent.  Current code includes a mixture of SYS_xxx and HAVE_xxx_H tests.  Whilst SYS_BSD might appear logical for FreeBSD, there is no testing for this, and recent FreeBSD variants support termios.h.

The attached patches (mostly taken from the FreeBSD port) add tests for HAVE_TERMIOS_H to make gap compile on FreeBSD 8.x.

Issue created by migration from https://trac.sagemath.org/ticket/9602





---

archive/issue_comments_092784.json:
```json
{
    "body": "Attachment [gap-4.4.12.p4.patch](tarball://root/attachments/some-uuid/ticket9602/gap-4.4.12.p4.patch) by @kcrisman created at 2012-01-31 01:48:26\n\nStephen Montgomery-Smith has successfully compiled with a very similar (identical?) patch, attached.",
    "created_at": "2012-01-31T01:48:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92784",
    "user": "https://github.com/kcrisman"
}
```

Attachment [gap-4.4.12.p4.patch](tarball://root/attachments/some-uuid/ticket9602/gap-4.4.12.p4.patch) by @kcrisman created at 2012-01-31 01:48:26

Stephen Montgomery-Smith has successfully compiled with a very similar (identical?) patch, attached.



---

archive/issue_comments_092785.json:
```json
{
    "body": "Attachment [spkg-patch-gap-4.4.12.p6](tarball://root/attachments/some-uuid/ticket9602/spkg-patch-gap-4.4.12.p6) by @kcrisman created at 2012-01-31 01:48:41",
    "created_at": "2012-01-31T01:48:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92785",
    "user": "https://github.com/kcrisman"
}
```

Attachment [spkg-patch-gap-4.4.12.p6](tarball://root/attachments/some-uuid/ticket9602/spkg-patch-gap-4.4.12.p6) by @kcrisman created at 2012-01-31 01:48:41



---

archive/issue_comments_092786.json:
```json
{
    "body": "I can confirm that this patch is needed to build sage-5.0.beta12.  It would be great if this patch could get put into sage.  It should be harmless to the builds under all other OS.",
    "created_at": "2012-04-08T14:47:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92786",
    "user": "https://trac.sagemath.org/admin/accounts/users/stephen"
}
```

I can confirm that this patch is needed to build sage-5.0.beta12.  It would be great if this patch could get put into sage.  It should be harmless to the builds under all other OS.



---

archive/issue_comments_092787.json:
```json
{
    "body": "Just for the record:\n\nThere's also a new GAP spkg at #7041; one should perhaps base a new one here on the latter, although it currently doesn't yet use `patch`.  (I've added a couple of TODOs, some of which I'll probably address at #7041 as well, if I find the time...)",
    "created_at": "2012-04-19T21:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92787",
    "user": "https://github.com/nexttime"
}
```

Just for the record:

There's also a new GAP spkg at #7041; one should perhaps base a new one here on the latter, although it currently doesn't yet use `patch`.  (I've added a couple of TODOs, some of which I'll probably address at #7041 as well, if I find the time...)



---

archive/issue_comments_092788.json:
```json
{
    "body": "Since #7041 didn't use patch, I don't think we need to do this either.\n\nSo we need a new spkg with this patch.",
    "created_at": "2012-06-20T19:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92788",
    "user": "https://github.com/kcrisman"
}
```

Since #7041 didn't use patch, I don't think we need to do this either.

So we need a new spkg with this patch.



---

archive/issue_comments_092789.json:
```json
{
    "body": "Just FYI to all reading this, there is an even newer GAP with a number of things fixed in spkg-install in Sage 5.6.rc0.  So it's possible that this would have to be rebased ... or maybe even unnecessary?  (We can hope!)",
    "created_at": "2013-01-16T01:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92789",
    "user": "https://github.com/kcrisman"
}
```

Just FYI to all reading this, there is an even newer GAP with a number of things fixed in spkg-install in Sage 5.6.rc0.  So it's possible that this would have to be rebased ... or maybe even unnecessary?  (We can hope!)



---

archive/issue_comments_092790.json:
```json
{
    "body": "The current `GAP-4.[5.6].x` doesn't have a `SYS_BSD` macro any more. This suggests that the issue has been fixed by upstream. I'm proposing to close this ticket as invalid/wontfix.",
    "created_at": "2013-03-12T13:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92790",
    "user": "https://github.com/vbraun"
}
```

The current `GAP-4.[5.6].x` doesn't have a `SYS_BSD` macro any more. This suggests that the issue has been fixed by upstream. I'm proposing to close this ticket as invalid/wontfix.



---

archive/issue_comments_092791.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-03-12T13:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92791",
    "user": "https://github.com/vbraun"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092792.json:
```json
{
    "body": "Stephen, what do you think?  [Your port](http://www.freebsd.org/cgi/cvsweb.cgi/ports/math/sage/files/) doesn't seem to have the GAP-specific patch I attached any more.",
    "created_at": "2013-03-12T14:11:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92792",
    "user": "https://github.com/kcrisman"
}
```

Stephen, what do you think?  [Your port](http://www.freebsd.org/cgi/cvsweb.cgi/ports/math/sage/files/) doesn't seem to have the GAP-specific patch I attached any more.



---

archive/issue_comments_092793.json:
```json
{
    "body": "Yes, at some point I seem to have removed the patch.  So it must be unnecessary now.",
    "created_at": "2013-03-13T01:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92793",
    "user": "https://trac.sagemath.org/admin/accounts/users/stephen"
}
```

Yes, at some point I seem to have removed the patch.  So it must be unnecessary now.



---

archive/issue_comments_092794.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-03-13T01:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92794",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092795.json:
```json
{
    "body": "I'll take that as a \"positive review\"",
    "created_at": "2013-03-13T01:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92795",
    "user": "https://github.com/vbraun"
}
```

I'll take that as a "positive review"



---

archive/issue_events_009746.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-03-15T13:02:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9602#event-9746"
}
```



---

archive/issue_comments_092796.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-03-15T13:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9602",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9602#issuecomment-92796",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
