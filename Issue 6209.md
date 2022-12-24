# Issue 6209: fix flint

archive/issues_006209.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nin fmpz.c change\n\n#include \"zn_poly/zn_poly.h\"\n\nto\n\n#include \"zn_poly/src/zn_poly.h\"\n\nAlso, in the FLINT makefile\n\n-DNEBUG -> -DNDEBUG\n\nin a couple of places. David Harvey found these.\n\nThese will fix the issues you note. The next version of FLINT due at\nthe end of June will have these fixes.\n\n -- Bill Hart\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6209\n\n",
    "created_at": "2009-06-04T17:02:22Z",
    "labels": [
        "build",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "fix flint",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6209",
    "user": "was"
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

archive/issue_comments_049606.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-04T17:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49606",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_049607.json:
```json
{
    "body": "I've made these changes and put them in http://sage.math.washington.edu/home/mhansen/flint-1.2.5.p0.spkg",
    "created_at": "2009-06-04T17:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49607",
    "user": "mhansen"
}
```

I've made these changes and put them in http://sage.math.washington.edu/home/mhansen/flint-1.2.5.p0.spkg



---

archive/issue_comments_049608.json:
```json
{
    "body": "Changing assignee from tbd to mhansen.",
    "created_at": "2009-06-04T17:53:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49608",
    "user": "mhansen"
}
```

Changing assignee from tbd to mhansen.



---

archive/issue_comments_049609.json:
```json
{
    "body": "The fmpz.c file still has #include \"zn_poly/zn_poly.h\"",
    "created_at": "2009-06-04T19:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49609",
    "user": "wbhart"
}
```

The fmpz.c file still has #include "zn_poly/zn_poly.h"



---

archive/issue_comments_049610.json:
```json
{
    "body": "Did you look in the fmpz.c file in the patches/directory?  That overwrites the one in the the src/ before the build.",
    "created_at": "2009-06-04T19:17:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49610",
    "user": "mhansen"
}
```

Did you look in the fmpz.c file in the patches/directory?  That overwrites the one in the the src/ before the build.



---

archive/issue_comments_049611.json:
```json
{
    "body": "Sorry, my mistake. It's fixed in patches not src indeed!!",
    "created_at": "2009-06-04T19:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49611",
    "user": "wbhart"
}
```

Sorry, my mistake. It's fixed in patches not src indeed!!



---

archive/issue_comments_049612.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T19:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49612",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_049613.json:
```json
{
    "body": "Merged in 4.0.1.rc1.",
    "created_at": "2009-06-04T19:39:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6209#issuecomment-49613",
    "user": "mhansen"
}
```

Merged in 4.0.1.rc1.
