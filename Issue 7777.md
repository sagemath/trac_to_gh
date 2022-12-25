# Issue 7777: Implement SymmetricFunctions(QQ).inject_shorthands()

archive/issues_007777.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat @jbandlow\n\nKeywords: symmetric functions, inject\n\nThe title says it all. Depends on #7776\n\nIssue created by migration from https://trac.sagemath.org/ticket/7777\n\n",
    "created_at": "2009-12-27T22:29:20Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Implement SymmetricFunctions(QQ).inject_shorthands()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7777",
    "user": "https://github.com/nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat @jbandlow

Keywords: symmetric functions, inject

The title says it all. Depends on #7776

Issue created by migration from https://trac.sagemath.org/ticket/7777





---

archive/issue_comments_066935.json:
```json
{
    "body": "Beware: patch written and tested on Sage 4.2, not 4.3.",
    "created_at": "2009-12-27T22:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66935",
    "user": "https://github.com/nthiery"
}
```

Beware: patch written and tested on Sage 4.2, not 4.3.



---

archive/issue_comments_066936.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T22:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66936",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066937.json:
```json
{
    "body": "Although I haven't tested it yet, I'm in principle very happy with the 'green' part of the patch.  Could you say a little about the 'red' part?  What's being deleted from the 'introspect' files and why?",
    "created_at": "2010-01-07T15:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66937",
    "user": "https://github.com/jbandlow"
}
```

Although I haven't tested it yet, I'm in principle very happy with the 'green' part of the patch.  Could you say a little about the 'red' part?  What's being deleted from the 'introspect' files and why?



---

archive/issue_comments_066938.json:
```json
{
    "body": "Attachment [trac_7777_symmetric_functions-inject_shorthands-nt.patch](tarball://root/attachments/some-uuid/ticket7777/trac_7777_symmetric_functions-inject_shorthands-nt.patch) by @nthiery created at 2010-01-07 19:48:08",
    "created_at": "2010-01-07T19:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66938",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7777_symmetric_functions-inject_shorthands-nt.patch](tarball://root/attachments/some-uuid/ticket7777/trac_7777_symmetric_functions-inject_shorthands-nt.patch) by @nthiery created at 2010-01-07 19:48:08



---

archive/issue_comments_066939.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-09T02:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66939",
    "user": "https://github.com/jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066940.json:
```json
{
    "body": "Looks good to me (on top of 7776). Thanks for this, Nicolas!",
    "created_at": "2010-01-09T02:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66940",
    "user": "https://github.com/jbandlow"
}
```

Looks good to me (on top of 7776). Thanks for this, Nicolas!



---

archive/issue_comments_066941.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T09:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66941",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_066942.json:
```json
{
    "body": "\n```\nThe following tests failed:\n\n        sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed\n```\n",
    "created_at": "2010-01-13T09:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66942",
    "user": "https://github.com/rlmill"
}
```


```
The following tests failed:

        sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed
```




---

archive/issue_comments_066943.json:
```json
{
    "body": "Replying to [comment:4 rlm]:\n> {{{\n> The following tests failed:\n> \n>         sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed\n> }}}\n\nThanks for the report. I did not manage yet to reproduce yet (I am downloading 4.3.1.alpha).\nCould you send me a copy of the log? Was 7776 applied?\n\nCheers",
    "created_at": "2010-01-13T11:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66943",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:4 rlm]:
> {{{
> The following tests failed:
> 
>         sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed
> }}}

Thanks for the report. I did not manage yet to reproduce yet (I am downloading 4.3.1.alpha).
Could you send me a copy of the log? Was 7776 applied?

Cheers



---

archive/issue_comments_066944.json:
```json
{
    "body": "I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...",
    "created_at": "2010-01-13T12:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66944",
    "user": "https://github.com/rlmill"
}
```

I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...



---

archive/issue_comments_066945.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-13T12:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66945",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066946.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T12:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66946",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066947.json:
```json
{
    "body": "Replying to [comment:6 rlm]:\n> I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...\n\n:-)\n\nWe really should be using a ticket dependency plugin like:\nhttp://trac-hacks.org/wiki/MasterTicketsPlugin.\n\nHave a good night!",
    "created_at": "2010-01-13T12:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66947",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:6 rlm]:
> I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...

:-)

We really should be using a ticket dependency plugin like:
http://trac-hacks.org/wiki/MasterTicketsPlugin.

Have a good night!



---

archive/issue_comments_066948.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T01:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-66948",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_007991.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-14T01:45:05Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7777#event-7991"
}
```
