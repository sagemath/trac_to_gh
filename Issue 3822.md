# Issue 3822: Interact - slider breaks defaulting on too many values

archive/issues_003822.json:
```json
{
    "body": "Assignee: itolkov\n\n> Unfortunately, as soon as the range of values gets at all large --\n> e.g., a few thousand, -- this causes *major* problems,\n> which lead to the browser spitting out errors, etc.  Basically you\n> exceed hard limits.\n\nThe problem is that something like\n\n```\nslider(1, 10^6)\n```\n\ngenerates 10<sup>6</sup> values, which get sent back to the user. Now, there is no reason to use 10<sup>6</sup> values when the maximum number of accessible values (via manipulating the slider) is 500.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3822\n\n",
    "created_at": "2008-08-12T20:20:22Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Interact - slider breaks defaulting on too many values",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3822",
    "user": "itolkov"
}
```
Assignee: itolkov

> Unfortunately, as soon as the range of values gets at all large --
> e.g., a few thousand, -- this causes *major* problems,
> which lead to the browser spitting out errors, etc.  Basically you
> exceed hard limits.

The problem is that something like

```
slider(1, 10^6)
```

generates 10<sup>6</sup> values, which get sent back to the user. Now, there is no reason to use 10<sup>6</sup> values when the maximum number of accessible values (via manipulating the slider) is 500.


Issue created by migration from https://trac.sagemath.org/ticket/3822





---

archive/issue_comments_027184.json:
```json
{
    "body": "Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3822/sage.patch) by itolkov created at 2008-08-12 20:31:08\n\n1. Changed default step size from 1 to such that there are 500 steps\n   2. `(a, b)` is now equivalent to `slider(a, b)`",
    "created_at": "2008-08-12T20:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27184",
    "user": "itolkov"
}
```

Attachment [sage.patch](tarball://root/attachments/some-uuid/ticket3822/sage.patch) by itolkov created at 2008-08-12 20:31:08

1. Changed default step size from 1 to such that there are 500 steps
   2. `(a, b)` is now equivalent to `slider(a, b)`



---

archive/issue_comments_027185.json:
```json
{
    "body": "It is still broken since you didn't deal with the case when the input is a list of values.  \n\nE.g.,\n\n```\n@interact\ndef _(n=range_slider([1..10000])):\n    print n\n```\n\n\nbreaks it.",
    "created_at": "2008-08-12T21:52:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27185",
    "user": "was"
}
```

It is still broken since you didn't deal with the case when the input is a list of values.  

E.g.,

```
@interact
def _(n=range_slider([1..10000])):
    print n
```


breaks it.



---

archive/issue_comments_027186.json:
```json
{
    "body": "Changing component from notebook to interact.",
    "created_at": "2008-08-13T06:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27186",
    "user": "mabshoff"
}
```

Changing component from notebook to interact.



---

archive/issue_comments_027187.json:
```json
{
    "body": "Attachment [sage2.2.patch](tarball://root/attachments/some-uuid/ticket3822/sage2.2.patch) by itolkov created at 2008-08-14 19:06:58\n\nApply after sage.patch",
    "created_at": "2008-08-14T19:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27187",
    "user": "itolkov"
}
```

Attachment [sage2.2.patch](tarball://root/attachments/some-uuid/ticket3822/sage2.2.patch) by itolkov created at 2008-08-14 19:06:58

Apply after sage.patch



---

archive/issue_comments_027188.json:
```json
{
    "body": "3. `slider(a, b, c)` is equivalent to `slider([a,a+c..b])`\n   4. Improved performance for input like `slider(a, b, c)`",
    "created_at": "2008-08-14T19:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27188",
    "user": "itolkov"
}
```

3. `slider(a, b, c)` is equivalent to `slider([a,a+c..b])`
   4. Improved performance for input like `slider(a, b, c)`



---

archive/issue_comments_027189.json:
```json
{
    "body": "Good job.  Note that this still breaks things.  But still this patch needs to go in.\n\n\n```\n@interact\ndef _(n=[1..10^5]):\n    print n\n```\n",
    "created_at": "2008-08-15T10:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27189",
    "user": "was"
}
```

Good job.  Note that this still breaks things.  But still this patch needs to go in.


```
@interact
def _(n=[1..10^5]):
    print n
```




---

archive/issue_comments_027190.json:
```json
{
    "body": "Attachment [sage-3822.patch](tarball://root/attachments/some-uuid/ticket3822/sage-3822.patch) by was created at 2008-08-15 10:02:34",
    "created_at": "2008-08-15T10:02:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27190",
    "user": "was"
}
```

Attachment [sage-3822.patch](tarball://root/attachments/some-uuid/ticket3822/sage-3822.patch) by was created at 2008-08-15 10:02:34



---

archive/issue_comments_027191.json:
```json
{
    "body": "I fixed some failed doctests.",
    "created_at": "2008-08-15T10:02:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27191",
    "user": "was"
}
```

I fixed some failed doctests.



---

archive/issue_comments_027192.json:
```json
{
    "body": "Merged all three patches in Sage 3.1.rc0. William's patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-15T10:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27192",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.1.rc0. William's patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_027193.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-15T10:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3822",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3822#issuecomment-27193",
    "user": "mabshoff"
}
```

Resolution: fixed
