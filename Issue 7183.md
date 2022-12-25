# Issue 7183: HP-UX issue: Evert package "date: bad format character - s

archive/issues_007183.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  david.kirkby@onetel.ne\n\nI assume this is in one of the files that gets called for every single .spkg. It appears 'date -s' is not portable\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7183\n\n",
    "created_at": "2009-10-10T10:32:35Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "HP-UX issue: Evert package \"date: bad format character - s",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7183",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  david.kirkby@onetel.ne

I assume this is in one of the files that gets called for every single .spkg. It appears 'date -s' is not portable



Issue created by migration from https://trac.sagemath.org/ticket/7183





---

archive/issue_comments_059371.json:
```json
{
    "body": "Changing component from build to porting: AIX or HP-UX.",
    "created_at": "2015-09-08T12:45:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7183#issuecomment-59371",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from build to porting: AIX or HP-UX.



---

archive/issue_comments_059372.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-08T14:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7183#issuecomment-59372",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059373.json:
```json
{
    "body": "I don't think that `date -s` is still used somewhere.",
    "created_at": "2015-09-08T14:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7183#issuecomment-59373",
    "user": "https://github.com/jdemeyer"
}
```

I don't think that `date -s` is still used somewhere.



---

archive/issue_comments_059374.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-08T14:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7183#issuecomment-59374",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_007402.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-09-12T14:05:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7183#event-7402"
}
```



---

archive/issue_comments_059375.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T14:05:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7183#issuecomment-59375",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_059376.json:
```json
{
    "body": "Where's the fix that received positive receive, and so allowed the ticket to be closed? \n\nIt seems a lot of tickets are now getting positive review and closed, where there is no actual fix.",
    "created_at": "2015-09-12T15:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7183#issuecomment-59376",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Where's the fix that received positive receive, and so allowed the ticket to be closed? 

It seems a lot of tickets are now getting positive review and closed, where there is no actual fix.



---

archive/issue_comments_059377.json:
```json
{
    "body": "Replying to [comment:6 drkirkby]:\n> Where's the fix that received positive receive, and so allowed the ticket to be closed? \n> \n> It seems a lot of tickets are now getting positive review and closed, where there is no actual fix. \n\n1. This ticket has seen no activity at all in years.\n2. I haven't seen any report of this problem in years (usually, when there is really a problem, it pops up on `sage-devel` now and then).\n3. I grepped the Sage sources and couldn't find anything like `date -s`.\n\nIf you really think there is still a problem, feel free to re-open the ticket but with more concrete info than just \"I assume this is in one of the files that gets called for every single .spkg\".",
    "created_at": "2015-09-12T22:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7183#issuecomment-59377",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:6 drkirkby]:
> Where's the fix that received positive receive, and so allowed the ticket to be closed? 
> 
> It seems a lot of tickets are now getting positive review and closed, where there is no actual fix. 

1. This ticket has seen no activity at all in years.
2. I haven't seen any report of this problem in years (usually, when there is really a problem, it pops up on `sage-devel` now and then).
3. I grepped the Sage sources and couldn't find anything like `date -s`.

If you really think there is still a problem, feel free to re-open the ticket but with more concrete info than just "I assume this is in one of the files that gets called for every single .spkg".
