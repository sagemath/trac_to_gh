# Issue 7337: PolyBoRi fails to build on cygwin

archive/issues_007337.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @williamstein\n\nIt fails with \n\n```\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:70: undefined reference to `_png_get_error_ptr'\n  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngReadData':\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:85: undefined reference to `_png_get_io_ptr'\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:87: undefined reference to `_png_error'\n  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngWriteData':\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:94: undefined reference to `_png_get_io_ptr'\n  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdImageCreateFromPngCtx':\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:152: undefined reference to `_png_check_sig'\n```\n\nThis can be fixed by adding png12 and z to the list of libraries needed when gd is present.\n\nI'll post an spkg shortly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7337\n\n",
    "closed_at": "2010-05-26T23:08:12Z",
    "created_at": "2009-10-28T19:37:45Z",
    "labels": [
        "component: porting: cygwin",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.3",
    "title": "PolyBoRi fails to build on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7337",
    "user": "https://github.com/mwhansen"
}
```
Assignee: tbd

CC:  @williamstein

It fails with 

```
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:70: undefined reference to `_png_get_error_ptr'
  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngReadData':
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:85: undefined reference to `_png_get_io_ptr'
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:87: undefined reference to `_png_error'
  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngWriteData':
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:94: undefined reference to `_png_get_io_ptr'
  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdImageCreateFromPngCtx':
  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:152: undefined reference to `_png_check_sig'
```

This can be fixed by adding png12 and z to the list of libraries needed when gd is present.

I'll post an spkg shortly.


Issue created by migration from https://trac.sagemath.org/ticket/7337





---

archive/issue_comments_061283.json:
```json
{
    "body": "This no longer fails with Cygwin 1.7.",
    "created_at": "2010-02-17T08:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61283",
    "user": "https://github.com/mwhansen"
}
```

This no longer fails with Cygwin 1.7.



---

archive/issue_events_017361.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-02-17T08:12:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7337#event-17361"
}
```



---

archive/issue_events_017362.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-02-17T08:12:09Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7337#event-17362"
}
```



---

archive/issue_comments_061284.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-02-17T08:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61284",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid



---

archive/issue_comments_061285.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2010-05-26T20:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61285",
    "user": "https://github.com/mwhansen"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_061286.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-05-26T20:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61286",
    "user": "https://github.com/mwhansen"
}
```

Changing status from closed to new.



---

archive/issue_events_017363.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-05-26T20:20:36Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7337#event-17363"
}
```



---

archive/issue_comments_061287.json:
```json
{
    "body": "So, it turns out this is still an issue.",
    "created_at": "2010-05-26T20:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61287",
    "user": "https://github.com/mwhansen"
}
```

So, it turns out this is still an issue.



---

archive/issue_comments_061288.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-26T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61288",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061289.json:
```json
{
    "body": "There's an spkg which should fix this at http://sage.math.washington.edu/home/mhansen/polybori-0.6.4.p1.spkg",
    "created_at": "2010-05-26T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61289",
    "user": "https://github.com/mwhansen"
}
```

There's an spkg which should fix this at http://sage.math.washington.edu/home/mhansen/polybori-0.6.4.p1.spkg



---

archive/issue_comments_061290.json:
```json
{
    "body": "looks good",
    "created_at": "2010-05-26T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61290",
    "user": "https://github.com/williamstein"
}
```

looks good



---

archive/issue_events_017364.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2010-05-26T23:08:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7337#event-17364"
}
```



---

archive/issue_comments_061291.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61291",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_017365.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-27T04:22:55Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7337#event-17365"
}
```



---

archive/issue_events_017366.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-05-27T04:22:55Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "milestone": "sage-4.4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7337#event-17366"
}
```
