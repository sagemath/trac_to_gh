# Issue 6209: fix flint

archive/issues_006209.json:
```json
{
    "body": "Assignee: tbd\n\n```\nin fmpz.c change\n\n#include \"zn_poly/zn_poly.h\"\n\nto\n\n#include \"zn_poly/src/zn_poly.h\"\n\nAlso, in the FLINT makefile\n\n-DNEBUG -> -DNDEBUG\n\nin a couple of places. David Harvey found these.\n\nThese will fix the issues you note. The next version of FLINT due at\nthe end of June will have these fixes.\n\n -- Bill Hart\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6209\n\n",
    "created_at": "2009-06-04T17:02:22Z",
    "labels": [
        "component: build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "fix flint",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6209",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

```
in fmpz.c change

#include "zn_poly/zn_poly.h"

to

#include "zn_poly/src/zn_poly.h"

Also, in the FLINT makefile

-DNEBUG -> -DNDEBUG

in a couple of places. David Harvey found these.

These will fix the issues you note. The next version of FLINT due at
the end of June will have these fixes.

 -- Bill Hart
```

Issue created by migration from https://trac.sagemath.org/ticket/6209





---

archive/issue_comments_049511.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T17:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49511",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049512.json:
```json
{
    "body": "I've made these changes and put them in http://sage.math.washington.edu/home/mhansen/flint-1.2.5.p0.spkg",
    "created_at": "2009-06-04T17:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49512",
    "user": "https://github.com/mwhansen"
}
```

I've made these changes and put them in http://sage.math.washington.edu/home/mhansen/flint-1.2.5.p0.spkg



---

archive/issue_comments_049513.json:
```json
{
    "body": "Changing assignee from tbd to @mwhansen.",
    "created_at": "2009-06-04T17:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49513",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tbd to @mwhansen.



---

archive/issue_comments_049514.json:
```json
{
    "body": "The fmpz.c file still has #include \"zn_poly/zn_poly.h\"",
    "created_at": "2009-06-04T19:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49514",
    "user": "https://trac.sagemath.org/admin/accounts/users/wbhart"
}
```

The fmpz.c file still has #include "zn_poly/zn_poly.h"



---

archive/issue_comments_049515.json:
```json
{
    "body": "Did you look in the fmpz.c file in the patches/directory?  That overwrites the one in the the src/ before the build.",
    "created_at": "2009-06-04T19:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49515",
    "user": "https://github.com/mwhansen"
}
```

Did you look in the fmpz.c file in the patches/directory?  That overwrites the one in the the src/ before the build.



---

archive/issue_comments_049516.json:
```json
{
    "body": "Sorry, my mistake. It's fixed in patches not src indeed!!",
    "created_at": "2009-06-04T19:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49516",
    "user": "https://trac.sagemath.org/admin/accounts/users/wbhart"
}
```

Sorry, my mistake. It's fixed in patches not src indeed!!



---

archive/issue_events_014564.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-06-04T19:39:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6209#event-14564"
}
```



---

archive/issue_comments_049517.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49517",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049518.json:
```json
{
    "body": "Merged in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49518",
    "user": "https://github.com/mwhansen"
}
```

Merged in 4.0.1.rc1.
