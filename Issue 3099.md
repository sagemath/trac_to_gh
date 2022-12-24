# Issue 3099: Singular crashes

archive/issues_003099.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  polybori @dimpase\n\nSingular crashes at degree 13 on intel core duo machine (mac os 10.5.2) when running \"fano7.sage\" with user command \"run2(1,20)\".  See attached files (fano7.sage, crash.txt}.  You may want to try \"run(12,20)\" to get to the crash more quickly.  Also, \"run2(19,40)\" crashed a quad core ppc machine with 8 gigs of memory.  The crash occurred before there was any significant output.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3099\n\n",
    "created_at": "2008-05-03T21:00:46Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Singular crashes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3099",
    "user": "jxxcarlson"
}
```
Assignee: @malb

CC:  polybori @dimpase

Singular crashes at degree 13 on intel core duo machine (mac os 10.5.2) when running "fano7.sage" with user command "run2(1,20)".  See attached files (fano7.sage, crash.txt}.  You may want to try "run(12,20)" to get to the crash more quickly.  Also, "run2(19,40)" crashed a quad core ppc machine with 8 gigs of memory.  The crash occurred before there was any significant output.

Issue created by migration from https://trac.sagemath.org/ticket/3099





---

archive/issue_comments_021398.json:
```json
{
    "body": "Sage source file",
    "created_at": "2008-05-03T21:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21398",
    "user": "jxxcarlson"
}
```

Sage source file



---

archive/issue_comments_021399.json:
```json
{
    "body": "Attachment [crash.txt](tarball://root/attachments/some-uuid/ticket3099/crash.txt) by jxxcarlson created at 2008-05-03 21:03:16\n\nCrash log",
    "created_at": "2008-05-03T21:03:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21399",
    "user": "jxxcarlson"
}
```

Attachment [crash.txt](tarball://root/attachments/some-uuid/ticket3099/crash.txt) by jxxcarlson created at 2008-05-03 21:03:16

Crash log



---

archive/issue_comments_021400.json:
```json
{
    "body": "Hi Jim,\n\nthis looks related to #3098. Since we have a fix for that issue which will be part of 3.0.1 can you try with it and check if the issue has been fixed? William is trying on a similar setup that also shows #3098, so hopefully he can give us some info here, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-04T03:32:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21400",
    "user": "mabshoff"
}
```

Hi Jim,

this looks related to #3098. Since we have a fix for that issue which will be part of 3.0.1 can you try with it and check if the issue has been fixed? William is trying on a similar setup that also shows #3098, so hopefully he can give us some info here, too.

Cheers,

Michael



---

archive/issue_comments_021401.json:
```json
{
    "body": "FYI:\n\n```\nme: ok. I just commented on the ticket that it likely would.\nSo you might want to clue us in that it is not that issue, but a similar problem\n William: Good.\n me: I also think that the \"huge\" problem he posted might just be that he ran out of RAM.\n William: Line 803 in singular.py would be fixed in a similar way to the fix in my other patch.\nWe'll find out in a while.\n me: After all: we are running Singular in 32 bit mode on OSX for now.\nNow if that mabshoff guy got moving on that issue .... [wink]\n William: Yes, what's holding up the 64-bit port?\n me: Nothing. Just spending my \"free\" time with lisp, Itanium and other fun stuff.\n```\n\n\nThe 64 bit OSX port is a high priority item for us and most problems have been already solved. William and I will likely spend some good time this Sunday and try to get everything merged back into 3.0.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-04T04:17:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21401",
    "user": "mabshoff"
}
```

FYI:

```
me: ok. I just commented on the ticket that it likely would.
So you might want to clue us in that it is not that issue, but a similar problem
 William: Good.
 me: I also think that the "huge" problem he posted might just be that he ran out of RAM.
 William: Line 803 in singular.py would be fixed in a similar way to the fix in my other patch.
We'll find out in a while.
 me: After all: we are running Singular in 32 bit mode on OSX for now.
Now if that mabshoff guy got moving on that issue .... [wink]
 William: Yes, what's holding up the 64-bit port?
 me: Nothing. Just spending my "free" time with lisp, Itanium and other fun stuff.
```


The 64 bit OSX port is a high priority item for us and most problems have been already solved. William and I will likely spend some good time this Sunday and try to get everything merged back into 3.0.2.

Cheers,

Michael



---

archive/issue_comments_021402.json:
```json
{
    "body": "I had some off list communication with Michael Brickenstein and he recommended using \n\n```\nHi Michael!\n\nI also use\n-with-valloc=system\nadditionally to\n--with-malloc=system\n\non Mac OS X  (32bit). I had issues with Singular not being able to\nallocate much memory (under certain circumstances) a few years ago\nand this configuration has proven to be useful.\n\nBest regards,\nMichael \n```\n\nI am not sure how Singular normally reacts when running out of memory, but it should obviously never crash.\n\nI am CCing PolyBoRi since Michael B. might enlighten us about this specific problem.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-29T01:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21402",
    "user": "mabshoff"
}
```

I had some off list communication with Michael Brickenstein and he recommended using 

```
Hi Michael!

I also use
-with-valloc=system
additionally to
--with-malloc=system

on Mac OS X  (32bit). I had issues with Singular not being able to
allocate much memory (under certain circumstances) a few years ago
and this configuration has proven to be useful.

Best regards,
Michael 
```

I am not sure how Singular normally reacts when running out of memory, but it should obviously never crash.

I am CCing PolyBoRi since Michael B. might enlighten us about this specific problem.

Cheers,

Michael



---

archive/issue_comments_021403.json:
```json
{
    "body": "Changing assignee from @malb to mabshoff.",
    "created_at": "2008-05-29T01:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21403",
    "user": "mabshoff"
}
```

Changing assignee from @malb to mabshoff.



---

archive/issue_comments_021404.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-29T01:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21404",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021405.json:
```json
{
    "body": "usually I got a clear error message about not being able to allocate more virtual memory (sometimes having only 100MB of memory consumed).\nI would recommend to export the actual commands sent to Singular somehow and to reproduce them with the Singular version in fink (and on other platforms).",
    "created_at": "2008-05-29T06:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21405",
    "user": "PolyBoRi"
}
```

usually I got a clear error message about not being able to allocate more virtual memory (sometimes having only 100MB of memory consumed).
I would recommend to export the actual commands sent to Singular somehow and to reproduce them with the Singular version in fink (and on other platforms).



---

archive/issue_comments_021406.json:
```json
{
    "body": "By the way: In Singular it is never checked, if an allocation is successful.\nIn this case, it usually crashes...\nIn fact, I was explicitely asked not to check the results of malloc calls...",
    "created_at": "2008-05-29T07:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21406",
    "user": "PolyBoRi"
}
```

By the way: In Singular it is never checked, if an allocation is successful.
In this case, it usually crashes...
In fact, I was explicitely asked not to check the results of malloc calls...



---

archive/issue_comments_021407.json:
```json
{
    "body": "On a new Mac,\n\n```\ndegree = 13\nTime: CPU 171.29 s, Wall: 171.90 s\n5107 [3, 4, 5, 7, 17, 22, 71, 104, 162, 189]\nTime: CPU 216.02 s, Wall: 218.62 s\n54323 [1, 3, 3, 7, 8, 11, 90, 109, 352]\n----------------------------------------------\n```\n\nbut this is presumably 64-bit.   It would be useful to know if this is still an issue with much larger input on a generic machine. Or is it so old it's wontfix?",
    "created_at": "2016-08-08T19:21:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21407",
    "user": "@kcrisman"
}
```

On a new Mac,

```
degree = 13
Time: CPU 171.29 s, Wall: 171.90 s
5107 [3, 4, 5, 7, 17, 22, 71, 104, 162, 189]
Time: CPU 216.02 s, Wall: 218.62 s
54323 [1, 3, 3, 7, 8, 11, 90, 109, 352]
----------------------------------------------
```

but this is presumably 64-bit.   It would be useful to know if this is still an issue with much larger input on a generic machine. Or is it so old it's wontfix?



---

archive/issue_comments_021408.json:
```json
{
    "body": "Outdated, should be closed",
    "created_at": "2020-04-18T06:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21408",
    "user": "@mkoeppe"
}
```

Outdated, should be closed



---

archive/issue_comments_021409.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-04-18T11:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21409",
    "user": "@dimpase"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_021410.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2020-04-18T11:09:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21410",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_021411.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-04-18T12:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3099",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3099#issuecomment-21411",
    "user": "@fchapoton"
}
```

Resolution: invalid
