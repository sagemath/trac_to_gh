# Issue 7623: Name OS X distributions automatically for PPC or Intel

archive/issues_007623.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  iandrus georgsweber\n\nThis was first requested in #5261, but no one is quite sure how to do it yet.   This would be the last thing to make OSX stuff more or less automatic.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7623\n\n",
    "created_at": "2009-12-08T15:29:09Z",
    "labels": [
        "distribution",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Name OS X distributions automatically for PPC or Intel",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7623",
    "user": "kcrisman"
}
```
Assignee: tbd

CC:  iandrus georgsweber

This was first requested in #5261, but no one is quite sure how to do it yet.   This would be the last thing to make OSX stuff more or less automatic.

Issue created by migration from https://trac.sagemath.org/ticket/7623





---

archive/issue_comments_065137.json:
```json
{
    "body": "On can do:\n\n```\nprompt$ /usr/sbin/system_profiler SPHardwareDataType\nHardware:\n\n    Hardware Overview:\n\n      Model Name: MacBook\n      Model Identifier: MacBook2,1\n      Processor Name: Intel Core 2 Duo\n      Processor Speed: 2 GHz\n      Number Of Processors: 1\n      Total Number Of Cores: 2\n      L2 Cache (per processor): 4 MB\n      Memory: 2 GB\n      Bus Speed: 667 MHz\n      Boot ROM Version: MB21.00A5.B07\n      SMC Version: 1.13f3\n      Serial Number: 4H7074T5WGL\n      Sudden Motion Sensor:\n          State: Enabled\n```\n\nThe only thing one should extract is the CPU type (\"G4\", \"G5\", or neither).\n\nBut since \"uname -m\" already gives you either \"i386\" or \"PowerMacintosh\", I fear that the ticket title is misleading. As far as I remember, we wanted to check whether a binary build tries to run on a system it is not made for ...",
    "created_at": "2010-02-08T22:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7623#issuecomment-65137",
    "user": "GeorgSWeber"
}
```

On can do:

```
prompt$ /usr/sbin/system_profiler SPHardwareDataType
Hardware:

    Hardware Overview:

      Model Name: MacBook
      Model Identifier: MacBook2,1
      Processor Name: Intel Core 2 Duo
      Processor Speed: 2 GHz
      Number Of Processors: 1
      Total Number Of Cores: 2
      L2 Cache (per processor): 4 MB
      Memory: 2 GB
      Bus Speed: 667 MHz
      Boot ROM Version: MB21.00A5.B07
      SMC Version: 1.13f3
      Serial Number: 4H7074T5WGL
      Sudden Motion Sensor:
          State: Enabled
```

The only thing one should extract is the CPU type ("G4", "G5", or neither).

But since "uname -m" already gives you either "i386" or "PowerMacintosh", I fear that the ticket title is misleading. As far as I remember, we wanted to check whether a binary build tries to run on a system it is not made for ...



---

archive/issue_comments_065138.json:
```json
{
    "body": "I doubt that we still support old OS X PPC.",
    "created_at": "2016-04-11T09:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7623#issuecomment-65138",
    "user": "jdemeyer"
}
```

I doubt that we still support old OS X PPC.



---

archive/issue_comments_065139.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-04-11T09:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7623#issuecomment-65139",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065140.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-11T09:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7623#issuecomment-65140",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065141.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-06-12T12:02:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7623",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7623#issuecomment-65141",
    "user": "vbraun"
}
```

Resolution: fixed
