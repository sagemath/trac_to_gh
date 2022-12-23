# Issue 7777: Implement SymmetricFunctions(QQ).inject_shorthands()

archive/issues_007777.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  sage-combinat jbandlow\n\nKeywords: symmetric functions, inject\n\nThe title says it all. Depends on #7776\n\nIssue created by migration from https://trac.sagemath.org/ticket/7777\n\n",
    "created_at": "2009-12-27T22:29:20Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Implement SymmetricFunctions(QQ).inject_shorthands()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7777",
    "user": "nthiery"
}
```
Assignee: sage-combinat

CC:  sage-combinat jbandlow

Keywords: symmetric functions, inject

The title says it all. Depends on #7776

Issue created by migration from https://trac.sagemath.org/ticket/7777





---

archive/issue_comments_067052.json:
```json
{
    "body": "Beware: patch written and tested on Sage 4.2, not 4.3.",
    "created_at": "2009-12-27T22:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67052",
    "user": "nthiery"
}
```

Beware: patch written and tested on Sage 4.2, not 4.3.



---

archive/issue_comments_067053.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T22:36:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67053",
    "user": "nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067054.json:
```json
{
    "body": "Although I haven't tested it yet, I'm in principle very happy with the 'green' part of the patch.  Could you say a little about the 'red' part?  What's being deleted from the 'introspect' files and why?",
    "created_at": "2010-01-07T15:11:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67054",
    "user": "jbandlow"
}
```

Although I haven't tested it yet, I'm in principle very happy with the 'green' part of the patch.  Could you say a little about the 'red' part?  What's being deleted from the 'introspect' files and why?



---

archive/issue_comments_067055.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-01-07T19:48:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67055",
    "user": "nthiery"
}
```

Attachment



---

archive/issue_comments_067056.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-09T02:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67056",
    "user": "jbandlow"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067057.json:
```json
{
    "body": "Looks good to me (on top of 7776). Thanks for this, Nicolas!",
    "created_at": "2010-01-09T02:42:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67057",
    "user": "jbandlow"
}
```

Looks good to me (on top of 7776). Thanks for this, Nicolas!



---

archive/issue_comments_067058.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-01-13T09:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67058",
    "user": "rlm"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_067059.json:
```json
{
    "body": "\n```\nThe following tests failed:\n\n        sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed\n```\n",
    "created_at": "2010-01-13T09:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67059",
    "user": "rlm"
}
```


```
The following tests failed:

        sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed
```




---

archive/issue_comments_067060.json:
```json
{
    "body": "Replying to [comment:4 rlm]:\n> {{{\n> The following tests failed:\n> \n>         sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed\n> }}}\n\nThanks for the report. I did not manage yet to reproduce yet (I am downloading 4.3.1.alpha).\nCould you send me a copy of the log? Was 7776 applied?\n\nCheers",
    "created_at": "2010-01-13T11:57:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67060",
    "user": "nthiery"
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

archive/issue_comments_067061.json:
```json
{
    "body": "I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...",
    "created_at": "2010-01-13T12:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67061",
    "user": "rlm"
}
```

I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...



---

archive/issue_comments_067062.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-13T12:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67062",
    "user": "rlm"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_067063.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T12:01:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67063",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067064.json:
```json
{
    "body": "Replying to [comment:6 rlm]:\n> I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...\n\n:-)\n\nWe really should be using a ticket dependency plugin like:\nhttp://trac-hacks.org/wiki/MasterTicketsPlugin.\n\nHave a good night!",
    "created_at": "2010-01-13T12:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67064",
    "user": "nthiery"
}
```

Replying to [comment:6 rlm]:
> I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...

:-)

We really should be using a ticket dependency plugin like:
http://trac-hacks.org/wiki/MasterTicketsPlugin.

Have a good night!



---

archive/issue_comments_067065.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T01:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7777#issuecomment-67065",
    "user": "rlm"
}
```

Resolution: fixed
