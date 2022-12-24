# Issue 9000: sage notebook: change default interact color selector

archive/issues_009000.json:
```json
{
    "body": "Assignee: jason, was\n\nPeople voted yes to the following:\n\n\n```\nWould anybody be opposed to me changing the default for \ncolor_select from 'farbtastic' to 'colorpicker'.  The \nfarbtastic color picker is *HUGE*, whereas the 'colorpicker' \none is much smaller and more usable.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9000\n\n",
    "created_at": "2010-05-20T19:37:34Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "sage notebook: change default interact color selector",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9000",
    "user": "was"
}
```
Assignee: jason, was

People voted yes to the following:


```
Would anybody be opposed to me changing the default for 
color_select from 'farbtastic' to 'colorpicker'.  The 
farbtastic color picker is *HUGE*, whereas the 'colorpicker' 
one is much smaller and more usable.
```


Issue created by migration from https://trac.sagemath.org/ticket/9000





---

archive/issue_comments_083221.json:
```json
{
    "body": "I ended up changing it to jpicker instead of colorpicker, since after trying it out, frankly colorpicker sucks, whereas jpicker is very nice.",
    "created_at": "2010-08-11T18:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83221",
    "user": "was"
}
```

I ended up changing it to jpicker instead of colorpicker, since after trying it out, frankly colorpicker sucks, whereas jpicker is very nice.



---

archive/issue_comments_083222.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-11T18:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83222",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083223.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-12T06:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83223",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_083224.json:
```json
{
    "body": "I think you may have accidentally changed the wrong function (`html_color_selector` instead of `color_selector`).",
    "created_at": "2010-08-12T06:01:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83224",
    "user": "timdumol"
}
```

I think you may have accidentally changed the wrong function (`html_color_selector` instead of `color_selector`).



---

archive/issue_comments_083225.json:
```json
{
    "body": "Attachment [trac_9000-interact_color.patch](tarball://root/attachments/some-uuid/ticket9000/trac_9000-interact_color.patch) by was created at 2010-08-14 02:22:56\n\nnew version that fixes the (valid) issue that tim pointed out.",
    "created_at": "2010-08-14T02:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83225",
    "user": "was"
}
```

Attachment [trac_9000-interact_color.patch](tarball://root/attachments/some-uuid/ticket9000/trac_9000-interact_color.patch) by was created at 2010-08-14 02:22:56

new version that fixes the (valid) issue that tim pointed out.



---

archive/issue_comments_083226.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-14T02:23:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83226",
    "user": "was"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_083227.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-08-14T03:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83227",
    "user": "timdumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_083228.json:
```json
{
    "body": "Looks good to me. Doctests pass. Positive review.",
    "created_at": "2010-08-14T03:19:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83228",
    "user": "timdumol"
}
```

Looks good to me. Doctests pass. Positive review.



---

archive/issue_comments_083229.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-10-04T01:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83229",
    "user": "mpatel"
}
```

Resolution: fixed



---

archive/issue_comments_083230.json:
```json
{
    "body": "Apparently this never quite got changed, or maybe it just was changed back or something.  See [this commit](https://github.com/sagemath/sagenb/commit/ece3ebf2c5a5e4389013988182609501d9332121), which I accidentally put in without review, sigh...",
    "created_at": "2014-10-01T15:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9000",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9000#issuecomment-83230",
    "user": "kcrisman"
}
```

Apparently this never quite got changed, or maybe it just was changed back or something.  See [this commit](https://github.com/sagemath/sagenb/commit/ece3ebf2c5a5e4389013988182609501d9332121), which I accidentally put in without review, sigh...
