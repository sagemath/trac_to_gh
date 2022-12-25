# Issue 9120: plot3d transformations don't respect variable names

archive/issues_009120.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  olazo wcauchois\n\nIf a transformation is applied to a plotting function, it may return a function with the wrong parameter names.  This wrecks havoc since there are assumptions about the variables being passed in being the variable names of the function.  This patch corrects and tests for this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9120\n\n",
    "closed_at": "2010-06-06T19:49:00Z",
    "created_at": "2010-06-03T02:55:23Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "plot3d transformations don't respect variable names",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9120",
    "user": "https://github.com/jasongrout"
}
```
Assignee: jason, was

CC:  olazo wcauchois

If a transformation is applied to a plotting function, it may return a function with the wrong parameter names.  This wrecks havoc since there are assumptions about the variables being passed in being the variable names of the function.  This patch corrects and tests for this.

Issue created by migration from https://trac.sagemath.org/ticket/9120





---

archive/issue_comments_084680.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-03T03:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84680",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084681.json:
```json
{
    "body": "Attachment [trac-9120-transformation-signature.patch](tarball://root/attachments/some-uuid/ticket9120/trac-9120-transformation-signature.patch) by @jasongrout created at 2010-06-03 03:01:23",
    "created_at": "2010-06-03T03:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84681",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9120-transformation-signature.patch](tarball://root/attachments/some-uuid/ticket9120/trac-9120-transformation-signature.patch) by @jasongrout created at 2010-06-03 03:01:23



---

archive/issue_comments_084682.json:
```json
{
    "body": "Hi Jason!\n\nThanks for your patch. However I'm having trouble understanding what this code does & what problem it fixes.\n\nSo basically, in the old code, if you passed in a lambda expression then the functions returned by to_cartesian() wouldn't have the correct parameter names? Can you give me some examples of when this would lead to incorrect behavior in Sage?",
    "created_at": "2010-06-03T05:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84682",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Hi Jason!

Thanks for your patch. However I'm having trouble understanding what this code does & what problem it fixes.

So basically, in the old code, if you passed in a lambda expression then the functions returned by to_cartesian() wouldn't have the correct parameter names? Can you give me some examples of when this would lead to incorrect behavior in Sage?



---

archive/issue_comments_084683.json:
```json
{
    "body": "The current implementation *will* lead to incorrect behavior in the fast_callable patch I'm working on...\n\nI don't know if they lead to incorrect behavior right now.\u00a0 The idea is that if you do plot(f, (x,0,1), (y,2,3), transformation=...), then the plotting code expects f to be called with f(x=.., y=...).\u00a0 However, if a transformation is applied first, then x and y may not be the right keyword arguments to use for f, since the parameters could be changed in the current implementation.",
    "created_at": "2010-06-03T05:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84683",
    "user": "https://github.com/jasongrout"
}
```

The current implementation *will* lead to incorrect behavior in the fast_callable patch I'm working on...

I don't know if they lead to incorrect behavior right now.  The idea is that if you do plot(f, (x,0,1), (y,2,3), transformation=...), then the plotting code expects f to be called with f(x=.., y=...).  However, if a transformation is applied first, then x and y may not be the right keyword arguments to use for f, since the parameters could be changed in the current implementation.



---

archive/issue_comments_084684.json:
```json
{
    "body": "Hmm, I see. Its too bad the only way to make this work is to call eval() on a string. I wish there were a more... static alternative.\n\n\nHave you been using plot3d transformations, in your class or otherwise?",
    "created_at": "2010-06-03T05:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84684",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Hmm, I see. Its too bad the only way to make this work is to call eval() on a string. I wish there were a more... static alternative.


Have you been using plot3d transformations, in your class or otherwise?



---

archive/issue_comments_084685.json:
```json
{
    "body": "Well, this all looks good and it seems to do what you're describing.\n\nDo you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake?",
    "created_at": "2010-06-03T05:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84685",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Well, this all looks good and it seems to do what you're describing.

Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake?



---

archive/issue_comments_084686.json:
```json
{
    "body": "Replying to [comment:5 wcauchois]:\n\n> Well, this all looks good and it seems to do what you're describing. Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake\n\n>\n\nCan we make that another ticket?",
    "created_at": "2010-06-03T15:02:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84686",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:5 wcauchois]:

> Well, this all looks good and it seems to do what you're describing. Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake

>

Can we make that another ticket?



---

archive/issue_comments_084687.json:
```json
{
    "body": "Replying to [comment:4 wcauchois]:\n\n\n> Have you been using plot3d transformations, in your class or otherwise?\n\n\nIt was merged too late to use in my class this last semester, but I do plan to use it in my class next semester.",
    "created_at": "2010-06-03T15:03:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84687",
    "user": "https://github.com/jasongrout"
}
```

Replying to [comment:4 wcauchois]:


> Have you been using plot3d transformations, in your class or otherwise?


It was merged too late to use in my class this last semester, but I do plan to use it in my class next semester.



---

archive/issue_comments_084688.json:
```json
{
    "body": "apply on top of previous patches",
    "created_at": "2010-06-03T15:32:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84688",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patches



---

archive/issue_comments_084689.json:
```json
{
    "body": "Attachment [trac-9120-refactoring.patch](tarball://root/attachments/some-uuid/ticket9120/trac-9120-refactoring.patch) by @jasongrout created at 2010-06-03 15:33:08\n\nReplying to [comment:5 wcauchois]:\n> Well, this all looks good and it seems to do what you're describing.\n> \n> Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake?\n\n\nOn second thought, that's a really good suggestion and relatively easy to do right now.  I've attached a second patch, to be applied on top of the first one.",
    "created_at": "2010-06-03T15:33:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84689",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-9120-refactoring.patch](tarball://root/attachments/some-uuid/ticket9120/trac-9120-refactoring.patch) by @jasongrout created at 2010-06-03 15:33:08

Replying to [comment:5 wcauchois]:
> Well, this all looks good and it seems to do what you're describing.
> 
> Do you think it would be good to factor the block of code from line 236 to line 259 into its own function (say, _find_arguments_for_callable) for readability's sake?


On second thought, that's a really good suggestion and relatively easy to do right now.  I've attached a second patch, to be applied on top of the first one.



---

archive/issue_comments_084690.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T22:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84690",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084691.json:
```json
{
    "body": "REFEREE REPORT\n\nWith this refactoring, I think this patch passes review. Applies fine to Sage 4.4.2, and fixes the (rather obscure :) bug it sets out to fix. plot3d.py passes all doctests.\n\nPositive review.",
    "created_at": "2010-06-05T22:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84691",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

REFEREE REPORT

With this refactoring, I think this patch passes review. Applies fine to Sage 4.4.2, and fixes the (rather obscure :) bug it sets out to fix. plot3d.py passes all doctests.

Positive review.



---

archive/issue_comments_084692.json:
```json
{
    "body": "Attachment [trac-9120-all.patch](tarball://root/attachments/some-uuid/ticket9120/trac-9120-all.patch) by wcauchois created at 2010-06-05 22:18:56\n\nincorporates all of the patches, based on sage 4.4.2",
    "created_at": "2010-06-05T22:18:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84692",
    "user": "https://trac.sagemath.org/admin/accounts/users/wcauchois"
}
```

Attachment [trac-9120-all.patch](tarball://root/attachments/some-uuid/ticket9120/trac-9120-all.patch) by wcauchois created at 2010-06-05 22:18:56

incorporates all of the patches, based on sage 4.4.2



---

archive/issue_events_022388.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-06T19:49:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9120#event-22388"
}
```



---

archive/issue_comments_084693.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T19:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9120",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9120#issuecomment-84693",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
