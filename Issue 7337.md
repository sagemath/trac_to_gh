# Issue 7337: PolyBoRi fails to build on cygwin

archive/issues_007337.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  was\n\nIt fails with \n\n\n```\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:70: undefined reference to `_png_get_error_ptr'\n  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngReadData':\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:85: undefined reference to `_png_get_io_ptr'\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:87: undefined reference to `_png_error'\n  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdPngWriteData':\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:94: undefined reference to `_png_get_io_ptr'\n  /home/mhansen/sage-4.2/local/lib/libgd.a(gd_png.o): In function `gdImageCreateFromPngCtx':\n  /home/mhansen/sage-4.2/spkg/build/gd-2.0.35.p2/src/gd_png.c:152: undefined reference to `_png_check_sig'\n```\n\n\nThis can be fixed by adding png12 and z to the list of libraries needed when gd is present.\n\nI'll post an spkg shortly.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7337\n\n",
    "created_at": "2009-10-28T19:37:45Z",
    "labels": [
        "porting: Cygwin",
        "major",
        "bug"
    ],
    "title": "PolyBoRi fails to build on cygwin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7337",
    "user": "mhansen"
}
```
Assignee: tbd

CC:  was

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

archive/issue_comments_061396.json:
```json
{
    "body": "This no longer fails with Cygwin 1.7.",
    "created_at": "2010-02-17T08:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61396",
    "user": "mhansen"
}
```

This no longer fails with Cygwin 1.7.



---

archive/issue_comments_061397.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-02-17T08:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61397",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_061398.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2010-05-26T20:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61398",
    "user": "mhansen"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_061399.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2010-05-26T20:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61399",
    "user": "mhansen"
}
```

Changing status from closed to new.



---

archive/issue_comments_061400.json:
```json
{
    "body": "So, it turns out this is still an issue.",
    "created_at": "2010-05-26T20:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61400",
    "user": "mhansen"
}
```

So, it turns out this is still an issue.



---

archive/issue_comments_061401.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-26T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61401",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061402.json:
```json
{
    "body": "There's an spkg which should fix this at http://sage.math.washington.edu/home/mhansen/polybori-0.6.4.p1.spkg",
    "created_at": "2010-05-26T20:29:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61402",
    "user": "mhansen"
}
```

There's an spkg which should fix this at http://sage.math.washington.edu/home/mhansen/polybori-0.6.4.p1.spkg



---

archive/issue_comments_061403.json:
```json
{
    "body": "looks good",
    "created_at": "2010-05-26T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61403",
    "user": "was"
}
```

looks good



---

archive/issue_comments_061404.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-26T23:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7337",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7337#issuecomment-61404",
    "user": "was"
}
```

Resolution: fixed
