# Issue 9321: Documentation for sum() function should indicate Python syntax *first*

archive/issues_009321.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @kcrisman\n\nWhen did we hijack the sum function? Based on the documentation there, I have (today alone) had four different people come up to me and ask why something like the following doesn't work:\n\n\n```\nsage: sum(Integer(x), x, 0, 9)\n```\n\n\nI know the reasons this shouldn't work, but newbies definitely don't. It should say something about how to do\n\n```\nsage: sum( Integer(x) for x in range(10) )\n```\n\nbefore \"getting all symbolic.\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/9321\n\n",
    "created_at": "2010-06-24T00:01:48Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "title": "Documentation for sum() function should indicate Python syntax *first*",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9321",
    "user": "https://github.com/rlmill"
}
```
Assignee: mvngu

CC:  @kcrisman

When did we hijack the sum function? Based on the documentation there, I have (today alone) had four different people come up to me and ask why something like the following doesn't work:


```
sage: sum(Integer(x), x, 0, 9)
```


I know the reasons this shouldn't work, but newbies definitely don't. It should say something about how to do

```
sage: sum( Integer(x) for x in range(10) )
```

before "getting all symbolic."

Issue created by migration from https://trac.sagemath.org/ticket/9321





---

archive/issue_comments_087731.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2014-03-18T14:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87731",
    "user": "https://github.com/rwst"
}
```

Changing priority from major to critical.



---

archive/issue_comments_087732.json:
```json
{
    "body": "The sagenb bug spreadsheet has several examples, too.",
    "created_at": "2014-03-18T14:51:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87732",
    "user": "https://github.com/rwst"
}
```

The sagenb bug spreadsheet has several examples, too.



---

archive/issue_comments_087733.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-03-18T15:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87733",
    "user": "https://github.com/rwst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_087734.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-03-18T15:59:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87734",
    "user": "https://github.com/rwst"
}
```

New commits:



---

archive/issue_comments_087735.json:
```json
{
    "body": "Nice first step.  I would also add some actual examples as the original reporter suggests - maybe with an explicit example showing what does and doesn't work along these lines.",
    "created_at": "2014-03-18T20:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87735",
    "user": "https://github.com/kcrisman"
}
```

Nice first step.  I would also add some actual examples as the original reporter suggests - maybe with an explicit example showing what does and doesn't work along these lines.



---

archive/issue_comments_087736.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-19T08:41:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87736",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087737.json:
```json
{
    "body": "How about this? Cannot make it any shorter than that.",
    "created_at": "2014-03-19T08:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87737",
    "user": "https://github.com/rwst"
}
```

How about this? Cannot make it any shorter than that.



---

archive/issue_comments_087738.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-19T08:51:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87738",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087739.json:
```json
{
    "body": "Your warning messages are indented one too many times.",
    "created_at": "2014-03-19T16:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87739",
    "user": "https://github.com/tscrim"
}
```

Your warning messages are indented one too many times.



---

archive/issue_comments_087740.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-03-19T16:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87740",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_087741.json:
```json
{
    "body": "Thanks for the review.",
    "created_at": "2014-03-19T17:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87741",
    "user": "https://github.com/rwst"
}
```

Thanks for the review.



---

archive/issue_comments_087742.json:
```json
{
    "body": "Okay, I'm going to ask for one final thing.  Probably it isn't appropriate to have this warning be before one even sees the INPUT block!  Can you put this after the first few examples, and then have some wording indicating \"now back to the examples\" in a not-informal way?  Otherwise we'll have the opposite problem of everyone avoiding this function :)\n\nAlso, another nit-pick - try to put the `sum()` in double back ticks so that it typesets properly as code.  And... is there any general reference for the Python sum, or are all of them version-dependent?  (I think the latter, just checking in case you know).\n\nThanks! Sorry this is an incremental review but it will be more awesomer soon.",
    "created_at": "2014-03-20T02:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87742",
    "user": "https://github.com/kcrisman"
}
```

Okay, I'm going to ask for one final thing.  Probably it isn't appropriate to have this warning be before one even sees the INPUT block!  Can you put this after the first few examples, and then have some wording indicating "now back to the examples" in a not-informal way?  Otherwise we'll have the opposite problem of everyone avoiding this function :)

Also, another nit-pick - try to put the `sum()` in double back ticks so that it typesets properly as code.  And... is there any general reference for the Python sum, or are all of them version-dependent?  (I think the latter, just checking in case you know).

Thanks! Sorry this is an incremental review but it will be more awesomer soon.



---

archive/issue_comments_087743.json:
```json
{
    "body": "I moved the warning a bit lower and added necessary backticks. I also removed the version string from the python link, although you will still arrive at the 2.x version. It's no longer hardcoded however. Finally, I had to change the branch path because `git amend`ed commits are not accepted by `sage -dev push`.\n----\nNew commits:",
    "created_at": "2014-03-20T09:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87743",
    "user": "https://github.com/rwst"
}
```

I moved the warning a bit lower and added necessary backticks. I also removed the version string from the python link, although you will still arrive at the 2.x version. It's no longer hardcoded however. Finally, I had to change the branch path because `git amend`ed commits are not accepted by `sage -dev push`.
----
New commits:



---

archive/issue_comments_087744.json:
```json
{
    "body": "Karl-Dieter, are you happy with the current version? (Really this is an elaborate **ping**.)",
    "created_at": "2014-06-22T04:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87744",
    "user": "https://github.com/tscrim"
}
```

Karl-Dieter, are you happy with the current version? (Really this is an elaborate **ping**.)



---

archive/issue_comments_087745.json:
```json
{
    "body": "> I also removed the version string from the python link, although you will still arrive at the 2.x version. It's no longer hardcoded however. \nhttps://docs.python.org/{2,3}/library/functions.html#sum is the link, technically.  I won't hold it up for that, though, since they can just click on \"sum\" from the big list at that location.  Doc looks good now.\n> Karl-Dieter, are you happy with the current version? (Really this is an elaborate ping.)\n:-)  Sorry for the delay; I definitely have been having to cut back even on review time the past few months.",
    "created_at": "2014-06-24T16:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87745",
    "user": "https://github.com/kcrisman"
}
```

> I also removed the version string from the python link, although you will still arrive at the 2.x version. It's no longer hardcoded however. 
https://docs.python.org/{2,3}/library/functions.html#sum is the link, technically.  I won't hold it up for that, though, since they can just click on "sum" from the big list at that location.  Doc looks good now.
> Karl-Dieter, are you happy with the current version? (Really this is an elaborate ping.)
:-)  Sorry for the delay; I definitely have been having to cut back even on review time the past few months.



---

archive/issue_comments_087746.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-24T16:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87746",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009477.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2014-06-26T01:50:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9321#event-9477"
}
```



---

archive/issue_comments_087747.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-26T01:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9321",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9321#issuecomment-87747",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
