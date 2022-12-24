# Issue 9579: Raise an exception when arguments to add_constraint are not admissible

archive/issues_009579.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nBecause of the error reported on :\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/b953192f3554337f\n\nIt may be good to save an user several hours of trouble because a wrong argument is silently accepted.\n\nDone in this patch ! :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9579\n\n",
    "created_at": "2010-07-23T02:37:16Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Raise an exception when arguments to add_constraint are not admissible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9579",
    "user": "ncohen"
}
```
Assignee: jason, jkantor

Because of the error reported on :

http://groups.google.com/group/sage-support/browse_thread/thread/b953192f3554337f

It may be good to save an user several hours of trouble because a wrong argument is silently accepted.

Done in this patch ! :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9579





---

archive/issue_comments_092516.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T02:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92516",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092517.json:
```json
{
    "body": "I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.",
    "created_at": "2010-07-23T09:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92517",
    "user": "schilly"
}
```

I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.



---

archive/issue_comments_092518.json:
```json
{
    "body": "test both arguments, not only one of them",
    "created_at": "2010-07-23T09:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92518",
    "user": "schilly"
}
```

test both arguments, not only one of them



---

archive/issue_comments_092519.json:
```json
{
    "body": "Attachment [trac_9579_review.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579_review.patch) by ncohen created at 2010-07-23 09:02:46\n\nReplying to [comment:2 schilly]:\n> I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.\n\nYou do not begin to know how I *HATE* this RR... Is there any way to check whether a value is numerical without having to import RINGS ? :-D\n\nEven a Python method is fine !!! The most esoteric thing that could be found there is a rational number !\n\nNathann",
    "created_at": "2010-07-23T09:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92519",
    "user": "ncohen"
}
```

Attachment [trac_9579_review.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579_review.patch) by ncohen created at 2010-07-23 09:02:46

Replying to [comment:2 schilly]:
> I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.

You do not begin to know how I *HATE* this RR... Is there any way to check whether a value is numerical without having to import RINGS ? :-D

Even a Python method is fine !!! The most esoteric thing that could be found there is a rational number !

Nathann



---

archive/issue_comments_092520.json:
```json
{
    "body": "Attachment [trac_9579.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579.patch) by ncohen created at 2010-07-23 09:18:17\n\nI just updated my patch so that instead of ugly \"try/except\", a \"if\" is enough, thanks to Harald's suggestion. By the way, your patch still applies on top of mine, so if you are ok with these changes, let's say this ticket is positively reviewed :-)\n\nNathann",
    "created_at": "2010-07-23T09:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92520",
    "user": "ncohen"
}
```

Attachment [trac_9579.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579.patch) by ncohen created at 2010-07-23 09:18:17

I just updated my patch so that instead of ugly "try/except", a "if" is enough, thanks to Harald's suggestion. By the way, your patch still applies on top of mine, so if you are ok with these changes, let's say this ticket is positively reviewed :-)

Nathann



---

archive/issue_comments_092521.json:
```json
{
    "body": "there is still this hurdle to run all tests, i'll start them right now.",
    "created_at": "2010-07-23T09:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92521",
    "user": "schilly"
}
```

there is still this hurdle to run all tests, i'll start them right now.



---

archive/issue_comments_092522.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T10:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92522",
    "user": "schilly"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092523.json:
```json
{
    "body": "dear release manager, first merge trac_9579.patch and then trac_9579_review.patch",
    "created_at": "2010-07-23T10:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92523",
    "user": "schilly"
}
```

dear release manager, first merge trac_9579.patch and then trac_9579_review.patch



---

archive/issue_comments_092524.json:
```json
{
    "body": "Replying to [comment:6 schilly]:\n> dear release manager, first merge trac_9579.patch and then trac_9579_review.patch\n\nMerged in 4.5.2.alpha1.",
    "created_at": "2010-07-26T02:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92524",
    "user": "ddrake"
}
```

Replying to [comment:6 schilly]:
> dear release manager, first merge trac_9579.patch and then trac_9579_review.patch

Merged in 4.5.2.alpha1.



---

archive/issue_comments_092525.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92525",
    "user": "ddrake"
}
```

Resolution: fixed



---

archive/issue_comments_092526.json:
```json
{
    "body": "My 'n' !! I hadn't noticed it !! Thank you :-)\n\nNathann",
    "created_at": "2010-08-06T02:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92526",
    "user": "ncohen"
}
```

My 'n' !! I hadn't noticed it !! Thank you :-)

Nathann
