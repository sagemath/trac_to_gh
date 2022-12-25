# Issue 9248: docstring for factorial doesn't say that it accepts non-integer, non-symbolic input

archive/issues_009248.json:
```json
{
    "body": "Assignee: mvngu\n\nAt comment:2:ticket:9240, we see someone get confused about the docstring for `factorial`, which claims it takes as input an integer or symbolic expression. However, it takes non-integer, non-SR inputs:\n\n```\nsage: x = 1.5; parent(x)\nReal Field with 53 bits of precision\nsage: factorial(x)\n1.32934038817914\nsage: x = 3/2; parent(x)\nRational Field\nsage: factorial(x)      \n3/4*sqrt(pi)\nsage: x = CC(1+I); parent(x)\nComplex Field with 53 bits of precision\nsage: factorial(x)\n0.652965496420167 + 0.343065839816545*I\n```\n\nI understand that there is coercion going on, but we should specify that the function takes pretty much any complex number (except of course negative integers) and evaluates (something akin to) gamma(1+x).\n\nHowever, it doesn't exactly do gamma(1+x):\n\n```\nsage: x = I; parent(x)  \nSymbolic Ring\nsage: factorial(x)    \n0.498015668118356 - 0.154949828301811*I\nsage: gamma(x+1)      \ngamma(I + 1)\nsage: parent(factorial(x))  \nSymbolic Ring\nsage: gamma(x+1).n() \n0.498015668118356 - 0.154949828301811*I\nsage: parent(gamma(x+1).n())\nComplex Field with 53 bits of precision\n```\n\nThe factorial function clearly is not simply calling gamma(x+1) when x is not an integer.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9248\n\n",
    "created_at": "2010-06-16T01:55:29Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "docstring for factorial doesn't say that it accepts non-integer, non-symbolic input",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9248",
    "user": "https://github.com/dandrake"
}
```
Assignee: mvngu

At comment:2:ticket:9240, we see someone get confused about the docstring for `factorial`, which claims it takes as input an integer or symbolic expression. However, it takes non-integer, non-SR inputs:

```
sage: x = 1.5; parent(x)
Real Field with 53 bits of precision
sage: factorial(x)
1.32934038817914
sage: x = 3/2; parent(x)
Rational Field
sage: factorial(x)      
3/4*sqrt(pi)
sage: x = CC(1+I); parent(x)
Complex Field with 53 bits of precision
sage: factorial(x)
0.652965496420167 + 0.343065839816545*I
```

I understand that there is coercion going on, but we should specify that the function takes pretty much any complex number (except of course negative integers) and evaluates (something akin to) gamma(1+x).

However, it doesn't exactly do gamma(1+x):

```
sage: x = I; parent(x)  
Symbolic Ring
sage: factorial(x)    
0.498015668118356 - 0.154949828301811*I
sage: gamma(x+1)      
gamma(I + 1)
sage: parent(factorial(x))  
Symbolic Ring
sage: gamma(x+1).n() 
0.498015668118356 - 0.154949828301811*I
sage: parent(gamma(x+1).n())
Complex Field with 53 bits of precision
```

The factorial function clearly is not simply calling gamma(x+1) when x is not an integer.

Issue created by migration from https://trac.sagemath.org/ticket/9248





---

archive/issue_comments_086891.json:
```json
{
    "body": "Changing assignee from mvngu to @dandrake.",
    "created_at": "2010-06-16T05:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86891",
    "user": "https://github.com/dandrake"
}
```

Changing assignee from mvngu to @dandrake.



---

archive/issue_comments_086892.json:
```json
{
    "body": "Also, factorial doesn't seem to accept the algorithm keyword anymore, even though the docstring says it does! I see that factorial() is just a wrapper around GiNaC's factorial; how does GiNaC compute factorials?",
    "created_at": "2010-06-16T05:13:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86892",
    "user": "https://github.com/dandrake"
}
```

Also, factorial doesn't seem to accept the algorithm keyword anymore, even though the docstring says it does! I see that factorial() is just a wrapper around GiNaC's factorial; how does GiNaC compute factorials?



---

archive/issue_comments_086893.json:
```json
{
    "body": "Notice also that factorial does not accept all sorts of input, which leads to problems in [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/119eafbfe3b69500).",
    "created_at": "2010-12-02T02:27:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86893",
    "user": "https://github.com/kcrisman"
}
```

Notice also that factorial does not accept all sorts of input, which leads to problems in [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/119eafbfe3b69500).



---

archive/issue_comments_086894.json:
```json
{
    "body": "Replying to [comment:2 kcrisman]:\n> Notice also that factorial does not accept all sorts of input, which leads to problems in [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/119eafbfe3b69500).  \nWhich for some reason I still posted even after realizing this is just #9240. Sorry for the noise.",
    "created_at": "2010-12-02T02:28:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86894",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:2 kcrisman]:
> Notice also that factorial does not accept all sorts of input, which leads to problems in [this thread](http://groups.google.com/group/sage-support/browse_thread/thread/119eafbfe3b69500).  
Which for some reason I still posted even after realizing this is just #9240. Sorry for the noise.



---

archive/issue_comments_086895.json:
```json
{
    "body": "Replying to [comment:1 ddrake]:\n> Also, factorial doesn't seem to accept the algorithm keyword anymore, even though the docstring says it does!\nWrong doc read. The problem is fixed in #17489.",
    "created_at": "2014-12-13T08:16:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86895",
    "user": "https://github.com/rwst"
}
```

Replying to [comment:1 ddrake]:
> Also, factorial doesn't seem to accept the algorithm keyword anymore, even though the docstring says it does!
Wrong doc read. The problem is fixed in #17489.



---

archive/issue_comments_086896.json:
```json
{
    "body": "It appears the originally described issue was fixed in #12286 (misleading title).",
    "created_at": "2014-12-13T08:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86896",
    "user": "https://github.com/rwst"
}
```

It appears the originally described issue was fixed in #12286 (misleading title).



---

archive/issue_comments_086897.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-12-13T08:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86897",
    "user": "https://github.com/rwst"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086898.json:
```json
{
    "body": "please change the status of a ticket to 'positive review' when you flag it as wontfix.",
    "created_at": "2014-12-31T10:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86898",
    "user": "https://github.com/nathanncohen"
}
```

please change the status of a ticket to 'positive review' when you flag it as wontfix.



---

archive/issue_comments_086899.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-12-31T10:46:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86899",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086900.json:
```json
{
    "body": "The same person should not both set it to wontfix and give it a positive review as it skips the review process.",
    "created_at": "2015-01-01T02:38:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86900",
    "user": "https://github.com/tscrim"
}
```

The same person should not both set it to wontfix and give it a positive review as it skips the review process.



---

archive/issue_comments_086901.json:
```json
{
    "body": "On the other hand, closing a ticket without review is much less bad than merging a branch without review. And essentially *nobody* reviews sage-duplicate/invalid/wontfix tickets.",
    "created_at": "2015-01-02T09:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86901",
    "user": "https://github.com/jdemeyer"
}
```

On the other hand, closing a ticket without review is much less bad than merging a branch without review. And essentially *nobody* reviews sage-duplicate/invalid/wontfix tickets.



---

archive/issue_comments_086902.json:
```json
{
    "body": "> The same person should not both set it to wontfix and give it a positive review as it skips the review process.\nBut the invalid and duplicate I think this is okay for.  I often give a positive review to dups or obviously now-functioning tickets.\n> And essentially nobody reviews sage-duplicate/invalid/wontfix tickets.\nYeah, probably also true.\n\nI do have to say that perhaps we should have a separate wontfix that would require *two* reviewers, maybe?  I have occasionally set some notebook tickets to wontfix but that is a fairly unusual situation.",
    "created_at": "2015-01-03T21:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86902",
    "user": "https://github.com/kcrisman"
}
```

> The same person should not both set it to wontfix and give it a positive review as it skips the review process.
But the invalid and duplicate I think this is okay for.  I often give a positive review to dups or obviously now-functioning tickets.
> And essentially nobody reviews sage-duplicate/invalid/wontfix tickets.
Yeah, probably also true.

I do have to say that perhaps we should have a separate wontfix that would require *two* reviewers, maybe?  I have occasionally set some notebook tickets to wontfix but that is a fairly unusual situation.



---

archive/issue_comments_086903.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-01-13T01:16:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9248#issuecomment-86903",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_009409.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-01-13T01:16:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9248",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9248#event-9409"
}
```
