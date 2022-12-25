# Issue 3791: ATLAS.spkg: add Altivec errata support for Linux PPC

archive/issues_003791.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @kiwifb jpflori\n\n\n```\nI was told that this line means that altivec was not detected.\nFor atlas on linux ppc with altivec, we should use the options\n--cflags='-mregnames' -D c -DATL_AVgcc\nfor configure ( http://math-atlas.sourceforge.net/errata.html#G4gcc ).\n\nWith these options, I had \"Vector ISA Extension configured as  AltiVec (1,2)\".\n\nBest regards,\nBin \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3791\n\n",
    "created_at": "2008-08-08T16:15:19Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "ATLAS.spkg: add Altivec errata support for Linux PPC",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3791",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @kiwifb jpflori


```
I was told that this line means that altivec was not detected.
For atlas on linux ppc with altivec, we should use the options
--cflags='-mregnames' -D c -DATL_AVgcc
for configure ( http://math-atlas.sourceforge.net/errata.html#G4gcc ).

With these options, I had "Vector ISA Extension configured as  AltiVec (1,2)".

Best regards,
Bin 
```


Issue created by migration from https://trac.sagemath.org/ticket/3791





---

archive/issue_comments_026896.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-08-08T16:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26896",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_026897.json:
```json
{
    "body": "What do you guys think - is this still valid?",
    "created_at": "2015-01-05T16:06:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26897",
    "user": "https://github.com/kcrisman"
}
```

What do you guys think - is this still valid?



---

archive/issue_comments_026898.json:
```json
{
    "body": "Frankly, I'd say we don't care about such systems...\nAnd from the ticket description it just seems that ATLAS won't be optimized on such systems but would still build.",
    "created_at": "2015-01-05T16:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26898",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Frankly, I'd say we don't care about such systems...
And from the ticket description it just seems that ATLAS won't be optimized on such systems but would still build.



---

archive/issue_comments_026899.json:
```json
{
    "body": "My own experience is that you need to let ATLAS set its own flags on power7 and probably other ppc(64) arch. It detects and adds altivec/vsx flags appropriately. If you touch CFLAGS you have to make sure to include flags that activate altivec (appropriate -mcpu and -mtune does the trick the CPPFLAGS should be included automatically and failure to include the right flags will result in a compilation failure at some point).\n\nIs this for your project of building a last tiger ppc binary?",
    "created_at": "2015-01-05T18:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26899",
    "user": "https://github.com/kiwifb"
}
```

My own experience is that you need to let ATLAS set its own flags on power7 and probably other ppc(64) arch. It detects and adds altivec/vsx flags appropriately. If you touch CFLAGS you have to make sure to include flags that activate altivec (appropriate -mcpu and -mtune does the trick the CPPFLAGS should be included automatically and failure to include the right flags will result in a compilation failure at some point).

Is this for your project of building a last tiger ppc binary?



---

archive/issue_comments_026900.json:
```json
{
    "body": ">Is this for your project of building a last tiger ppc binary?\n\nNo, although that is going fine.  This is just me seeing random tickets that possibly could be closed as wontfix/invalid... I can't say whether it would but if you both agree then I say you should do so :)",
    "created_at": "2015-01-05T20:37:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26900",
    "user": "https://github.com/kcrisman"
}
```

>Is this for your project of building a last tiger ppc binary?

No, although that is going fine.  This is just me seeing random tickets that possibly could be closed as wontfix/invalid... I can't say whether it would but if you both agree then I say you should do so :)



---

archive/issue_comments_026901.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-01-05T21:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26901",
    "user": "https://github.com/kiwifb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026902.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-01-05T21:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26902",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_026903.json:
```json
{
    "body": "I am putting it as \"invalid\".",
    "created_at": "2015-01-05T21:33:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26903",
    "user": "https://github.com/kiwifb"
}
```

I am putting it as "invalid".



---

archive/issue_comments_026904.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2015-01-13T01:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26904",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid



---

archive/issue_comments_026905.json:
```json
{
    "body": "You are supposed to change the milestone to \"duplicate/invalid/wontfix\" then...",
    "created_at": "2015-01-13T01:13:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3791#issuecomment-26905",
    "user": "https://github.com/vbraun"
}
```

You are supposed to change the milestone to "duplicate/invalid/wontfix" then...



---

archive/issue_events_004013.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-01-13T01:13:57Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3791",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3791#event-4013"
}
```
