# Issue 9579: Raise an exception when arguments to add_constraint are not admissible

archive/issues_009579.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nBecause of the error reported on :\n\nhttp://groups.google.com/group/sage-support/browse_thread/thread/b953192f3554337f\n\nIt may be good to save an user several hours of trouble because a wrong argument is silently accepted.\n\nDone in this patch ! :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9579\n\n",
    "created_at": "2010-07-23T02:37:16Z",
    "labels": [
        "component: numerical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "Raise an exception when arguments to add_constraint are not admissible",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9579",
    "user": "https://github.com/nathanncohen"
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

archive/issue_comments_092362.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-23T02:38:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92362",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092363.json:
```json
{
    "body": "I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.",
    "created_at": "2010-07-23T09:00:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92363",
    "user": "https://github.com/haraldschilly"
}
```

I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.



---

archive/issue_comments_092364.json:
```json
{
    "body": "test both arguments, not only one of them",
    "created_at": "2010-07-23T09:01:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92364",
    "user": "https://github.com/haraldschilly"
}
```

test both arguments, not only one of them



---

archive/issue_comments_092365.json:
```json
{
    "body": "Attachment [trac_9579_review.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579_review.patch) by @nathanncohen created at 2010-07-23 09:02:46\n\nReplying to [comment:2 schilly]:\n> I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.\n\nYou do not begin to know how I *HATE* this RR... Is there any way to check whether a value is numerical without having to import RINGS ? :-D\n\nEven a Python method is fine !!! The most esoteric thing that could be found there is a rational number !\n\nNathann",
    "created_at": "2010-07-23T09:02:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92365",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9579_review.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579_review.patch) by @nathanncohen created at 2010-07-23 09:02:46

Replying to [comment:2 schilly]:
> I don't know if testing with RR is the best way to do this, but should work. What's missing is a test for max b/c you only tested for min.

You do not begin to know how I *HATE* this RR... Is there any way to check whether a value is numerical without having to import RINGS ? :-D

Even a Python method is fine !!! The most esoteric thing that could be found there is a rational number !

Nathann



---

archive/issue_comments_092366.json:
```json
{
    "body": "Attachment [trac_9579.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579.patch) by @nathanncohen created at 2010-07-23 09:18:17\n\nI just updated my patch so that instead of ugly \"try/except\", a \"if\" is enough, thanks to Harald's suggestion. By the way, your patch still applies on top of mine, so if you are ok with these changes, let's say this ticket is positively reviewed :-)\n\nNathann",
    "created_at": "2010-07-23T09:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92366",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_9579.patch](tarball://root/attachments/some-uuid/ticket9579/trac_9579.patch) by @nathanncohen created at 2010-07-23 09:18:17

I just updated my patch so that instead of ugly "try/except", a "if" is enough, thanks to Harald's suggestion. By the way, your patch still applies on top of mine, so if you are ok with these changes, let's say this ticket is positively reviewed :-)

Nathann



---

archive/issue_comments_092367.json:
```json
{
    "body": "there is still this hurdle to run all tests, i'll start them right now.",
    "created_at": "2010-07-23T09:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92367",
    "user": "https://github.com/haraldschilly"
}
```

there is still this hurdle to run all tests, i'll start them right now.



---

archive/issue_comments_092368.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-23T10:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92368",
    "user": "https://github.com/haraldschilly"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092369.json:
```json
{
    "body": "dear release manager, first merge trac_9579.patch and then trac_9579_review.patch",
    "created_at": "2010-07-23T10:17:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92369",
    "user": "https://github.com/haraldschilly"
}
```

dear release manager, first merge trac_9579.patch and then trac_9579_review.patch



---

archive/issue_comments_092370.json:
```json
{
    "body": "Replying to [comment:6 schilly]:\n> dear release manager, first merge trac_9579.patch and then trac_9579_review.patch\n\nMerged in 4.5.2.alpha1.",
    "created_at": "2010-07-26T02:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92370",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:6 schilly]:
> dear release manager, first merge trac_9579.patch and then trac_9579_review.patch

Merged in 4.5.2.alpha1.



---

archive/issue_comments_092371.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-26T02:37:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92371",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_comments_092372.json:
```json
{
    "body": "My 'n' !! I hadn't noticed it !! Thank you :-)\n\nNathann",
    "created_at": "2010-08-06T02:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9579",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9579#issuecomment-92372",
    "user": "https://github.com/nathanncohen"
}
```

My 'n' !! I hadn't noticed it !! Thank you :-)

Nathann
