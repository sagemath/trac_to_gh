# Issue 8122: Sage patches added directly to symmetica source

archive/issues_008122.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @jaapspies mvngu\n\nThe symmerica package says in SPKG.txt\n\n```\n## Special Update/Build Instructions\n\nAgainst common policy the patches in the patches directory have been applied to \nthe src directory:\n\n * de.patch (Turn off banner)\n * macro.h.patch (Change some return types, this can be avoided)\n * makefile.patch (Fix compiler, inject CFLAGS)\n * sort_sum_rename.patch (rename sort tp sym_sort, sum to sym_sum) \n```\n\nIt would appear various patches have been made to the source code. \n\n\nhttp://boxen.math.washington.edu/home/kirkby/portability/symmetrica-2.0.p5/\n\nhas an updated version of symmetica, which will build with any compiler, and in 64-bit mode. However, it does not resolve the issue of patching the source directly. I modified the makefile, which had already been modified before. A patch was left, so I have tried to recreate the original makefile. But other files have been changed too. The packages is basically a bit of a mess\n\nIssue created by migration from https://trac.sagemath.org/ticket/8122\n\n",
    "created_at": "2010-01-29T18:51:48Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage patches added directly to symmetica source",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8122",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @jaapspies mvngu

The symmerica package says in SPKG.txt

```
## Special Update/Build Instructions

Against common policy the patches in the patches directory have been applied to 
the src directory:

 * de.patch (Turn off banner)
 * macro.h.patch (Change some return types, this can be avoided)
 * makefile.patch (Fix compiler, inject CFLAGS)
 * sort_sum_rename.patch (rename sort tp sym_sort, sum to sym_sum) 
```

It would appear various patches have been made to the source code. 


http://boxen.math.washington.edu/home/kirkby/portability/symmetrica-2.0.p5/

has an updated version of symmetica, which will build with any compiler, and in 64-bit mode. However, it does not resolve the issue of patching the source directly. I modified the makefile, which had already been modified before. A patch was left, so I have tried to recreate the original makefile. But other files have been changed too. The packages is basically a bit of a mess

Issue created by migration from https://trac.sagemath.org/ticket/8122





---

archive/issue_comments_071282.json:
```json
{
    "body": "Has this been fixed already? Looks like the text you quoted no longer exists in SPKG.txt in symmetrica-2.0.p7.spkg, which currently ships with Sage.",
    "created_at": "2012-10-02T22:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8122#issuecomment-71282",
    "user": "https://github.com/kini"
}
```

Has this been fixed already? Looks like the text you quoted no longer exists in SPKG.txt in symmetrica-2.0.p7.spkg, which currently ships with Sage.



---

archive/issue_comments_071283.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2012-10-02T22:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8122#issuecomment-71283",
    "user": "https://github.com/kini"
}
```

Changing status from new to needs_info.



---

archive/issue_events_019452.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8122#event-19452"
}
```



---

archive/issue_comments_071284.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2013-12-29T23:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8122#issuecomment-71284",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_071285.json:
```json
{
    "body": "Duplicate of #10719.",
    "created_at": "2013-12-29T23:33:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8122#issuecomment-71285",
    "user": "https://github.com/jdemeyer"
}
```

Duplicate of #10719.



---

archive/issue_events_019453.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-12-29T23:33:51Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8122#event-19453"
}
```



---

archive/issue_events_019454.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-12-29T23:33:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8122#event-19454"
}
```



---

archive/issue_comments_071286.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-04T04:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8122#issuecomment-71286",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_019455.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-01-04T04:18:20Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8122",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8122#event-19455"
}
```
