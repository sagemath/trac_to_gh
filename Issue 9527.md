# Issue 9527: improve "sage -sh" prompt so it doesn't confuse everybody

archive/issues_009527.json:
```json
{
    "body": "Assignee: jason\n\nCC:  malb\n\nWhen doing `sage -sh`, the result is very, very confusing, since it has the SAGE_ROOT path displayed unlabeled, which causes confusion, and does not show the current path, which also causes confusion.  This patch adds a label and the current path, to help reduce confusion some.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9527\n\n",
    "created_at": "2010-07-17T11:55:26Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "improve \"sage -sh\" prompt so it doesn't confuse everybody",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9527",
    "user": "was"
}
```
Assignee: jason

CC:  malb

When doing `sage -sh`, the result is very, very confusing, since it has the SAGE_ROOT path displayed unlabeled, which causes confusion, and does not show the current path, which also causes confusion.  This patch adds a label and the current path, to help reduce confusion some.

Issue created by migration from https://trac.sagemath.org/ticket/9527





---

archive/issue_comments_091649.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-17T12:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9527#issuecomment-91649",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091650.json:
```json
{
    "body": "Attachment [trac_9527.patch](tarball://root/attachments/some-uuid/ticket9527/trac_9527.patch) by was created at 2010-07-17 13:03:03\n\nfix SAGE_ROOT (a separate bug, I guess)",
    "created_at": "2010-07-17T13:03:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9527#issuecomment-91650",
    "user": "was"
}
```

Attachment [trac_9527.patch](tarball://root/attachments/some-uuid/ticket9527/trac_9527.patch) by was created at 2010-07-17 13:03:03

fix SAGE_ROOT (a separate bug, I guess)



---

archive/issue_comments_091651.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-17T13:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9527#issuecomment-91651",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091652.json:
```json
{
    "body": "The patch looks fine. I'd have preferred to have my PS1 to be embedded in the new PS1, i.e. something like this:\n\n\n```\nthis_is_my_prompt$ sage -sh\nSAGE_ROOT=/usr/local/sage-4.3\n(sage subshell) this_is_my_prompt$\n\n\n```\n\nBut it seems this just doesn't work (I tried). This new one is definitely an improvement thus I'll give it a positive review.",
    "created_at": "2010-07-17T13:09:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9527#issuecomment-91652",
    "user": "malb"
}
```

The patch looks fine. I'd have preferred to have my PS1 to be embedded in the new PS1, i.e. something like this:


```
this_is_my_prompt$ sage -sh
SAGE_ROOT=/usr/local/sage-4.3
(sage subshell) this_is_my_prompt$


```

But it seems this just doesn't work (I tried). This new one is definitely an improvement thus I'll give it a positive review.



---

archive/issue_comments_091653.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n> The patch looks fine. I'd have preferred to have my PS1 to be embedded in the new PS1, i.e. something like this:\n> \n> {{{\n> this_is_my_prompt$ sage -sh\n> SAGE_ROOT=/usr/local/sage-4.3\n> (sage subshell) this_is_my_prompt$\n> \n> \n> }}}\n> But it seems this just doesn't work (I tried). \n\nI tried too, but couldn't figure it out. This patch is meant to be a big improvement, that's all.",
    "created_at": "2010-07-17T13:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9527#issuecomment-91653",
    "user": "was"
}
```

Replying to [comment:2 malb]:
> The patch looks fine. I'd have preferred to have my PS1 to be embedded in the new PS1, i.e. something like this:
> 
> {{{
> this_is_my_prompt$ sage -sh
> SAGE_ROOT=/usr/local/sage-4.3
> (sage subshell) this_is_my_prompt$
> 
> 
> }}}
> But it seems this just doesn't work (I tried). 

I tried too, but couldn't figure it out. This patch is meant to be a big improvement, that's all.



---

archive/issue_comments_091654.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T23:42:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9527",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9527#issuecomment-91654",
    "user": "ddrake"
}
```

Resolution: fixed
