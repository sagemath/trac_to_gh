# Issue 9149: spelling error (trivial to fix)

archive/issues_009149.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nThe following message has a spelling error: `occured` should be\n`occurred`:\n\n```\nUnhandled SIGFPE: An unhandled floating point exception occured in Sage.\nThis probably occured because a *compiled* component\nof Sage has a bug in it (typically accessing invalid memory)\nor is not properly wrapped with _sig_on, _sig_off.\nYou might want to run Sage under gdb with 'sage -gdb' to debug this.\nSage will now terminate (sorry).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9149\n\n",
    "created_at": "2010-06-05T12:02:01Z",
    "labels": [
        "build",
        "trivial",
        "enhancement"
    ],
    "title": "spelling error (trivial to fix)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9149",
    "user": "zimmerma"
}
```
Assignee: GeorgSWeber

The following message has a spelling error: `occured` should be
`occurred`:

```
Unhandled SIGFPE: An unhandled floating point exception occured in Sage.
This probably occured because a *compiled* component
of Sage has a bug in it (typically accessing invalid memory)
or is not properly wrapped with _sig_on, _sig_off.
You might want to run Sage under gdb with 'sage -gdb' to debug this.
Sage will now terminate (sorry).
```


Issue created by migration from https://trac.sagemath.org/ticket/9149





---

archive/issue_comments_085425.json:
```json
{
    "body": "Attachment [trac_9149.patch](tarball://root/attachments/some-uuid/ticket9149/trac_9149.patch) by zimmerma created at 2010-06-05 12:24:12",
    "created_at": "2010-06-05T12:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9149#issuecomment-85425",
    "user": "zimmerma"
}
```

Attachment [trac_9149.patch](tarball://root/attachments/some-uuid/ticket9149/trac_9149.patch) by zimmerma created at 2010-06-05 12:24:12



---

archive/issue_comments_085426.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-05T12:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9149#issuecomment-85426",
    "user": "zimmerma"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_085427.json:
```json
{
    "body": "The attached patch fixes that spelling error. (Note there are other similar errors in the source\nfiles, but that one is directly visible to the user.)",
    "created_at": "2010-06-05T12:27:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9149#issuecomment-85427",
    "user": "zimmerma"
}
```

The attached patch fixes that spelling error. (Note there are other similar errors in the source
files, but that one is directly visible to the user.)



---

archive/issue_comments_085428.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-05T15:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9149#issuecomment-85428",
    "user": "mvngu"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_085429.json:
```json
{
    "body": "Thanks for this.",
    "created_at": "2010-06-05T15:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9149#issuecomment-85429",
    "user": "mvngu"
}
```

Thanks for this.



---

archive/issue_comments_085430.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T01:25:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9149#issuecomment-85430",
    "user": "mhansen"
}
```

Resolution: fixed
