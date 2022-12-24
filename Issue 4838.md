# Issue 4838: implement plotting of complex numbers

archive/issues_004838.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plot complex number\n\nIt would be nice to be able to do:\n\n\n```\nsage: CC(3-2*I).plot()\n```\n\n\nwhich would return a plot object of the point 3-2*I.  I guess it just needs to wrap the normal plot of a point.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4838\n\n",
    "created_at": "2008-12-20T16:47:25Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "title": "implement plotting of complex numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4838",
    "user": "AlexGhitza"
}
```
Assignee: was

Keywords: plot complex number

It would be nice to be able to do:


```
sage: CC(3-2*I).plot()
```


which would return a plot object of the point 3-2*I.  I guess it just needs to wrap the normal plot of a point.

Issue created by migration from https://trac.sagemath.org/ticket/4838





---

archive/issue_comments_036682.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-29T22:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36682",
    "user": "vdelecroix"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_036683.json:
```json
{
    "body": "Attachment [patch_4838-vd.patch](tarball://root/attachments/some-uuid/ticket4838/patch_4838-vd.patch) by vdelecroix created at 2010-01-29 22:34:31",
    "created_at": "2010-01-29T22:34:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36683",
    "user": "vdelecroix"
}
```

Attachment [patch_4838-vd.patch](tarball://root/attachments/some-uuid/ticket4838/patch_4838-vd.patch) by vdelecroix created at 2010-01-29 22:34:31



---

archive/issue_comments_036684.json:
```json
{
    "body": "Attachment [trac_4838-vd.patch](tarball://root/attachments/some-uuid/ticket4838/trac_4838-vd.patch) by vdelecroix created at 2010-01-29 22:45:04\n\nuse only this one !",
    "created_at": "2010-01-29T22:45:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36684",
    "user": "vdelecroix"
}
```

Attachment [trac_4838-vd.patch](tarball://root/attachments/some-uuid/ticket4838/trac_4838-vd.patch) by vdelecroix created at 2010-01-29 22:45:04

use only this one !



---

archive/issue_comments_036685.json:
```json
{
    "body": "This works (so patch does its job as designed)\n\n```\nCC(1+I).plot() \n```\n\n\nThis currently doesnt work (because not part of this ticket) \n\n```\n[CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)].plot()\n```\n\n(its a natural extension of the idea in this ticket, but will have to be a new ticket if anyone thinks its worth implementing)",
    "created_at": "2010-01-31T10:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36685",
    "user": "rossk"
}
```

This works (so patch does its job as designed)

```
CC(1+I).plot() 
```


This currently doesnt work (because not part of this ticket) 

```
[CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)].plot()
```

(its a natural extension of the idea in this ticket, but will have to be a new ticket if anyone thinks its worth implementing)



---

archive/issue_comments_036686.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-31T10:47:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36686",
    "user": "rossk"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_036687.json:
```json
{
    "body": "> This currently doesnt work (because not part of this ticket) \n> {{{\n> [CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)].plot()\n> }}}\n> (its a natural extension of the idea in this ticket, but will have to be a new ticket if anyone thinks its worth implementing)  \n\nBEWARE: It's not a good idea to implement this (and not even possible). To be able to do this the .plot() method have to be coded inside the list object which is a python object.\n\nBut remains the question on how do the following work ?\n\n```\nsage: z0 = CC(2,3)\nsage: plot(z0)   # works with this patch\nsage: z1 = 2 + 3*I\nsage: plot(z1)  # does not work because z1 is in SR and not in CC\n```\n\n\nMost of the time users have to think about using `point` more than `plot` for complex numbers... and I'm not sure about the usefulness of this ticket...",
    "created_at": "2010-01-31T11:44:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36687",
    "user": "vdelecroix"
}
```

> This currently doesnt work (because not part of this ticket) 
> {{{
> [CC(cos(theta)+I*sin(theta)) for theta in srange(0, 2*pi, pi/4)].plot()
> }}}
> (its a natural extension of the idea in this ticket, but will have to be a new ticket if anyone thinks its worth implementing)  

BEWARE: It's not a good idea to implement this (and not even possible). To be able to do this the .plot() method have to be coded inside the list object which is a python object.

But remains the question on how do the following work ?

```
sage: z0 = CC(2,3)
sage: plot(z0)   # works with this patch
sage: z1 = 2 + 3*I
sage: plot(z1)  # does not work because z1 is in SR and not in CC
```


Most of the time users have to think about using `point` more than `plot` for complex numbers... and I'm not sure about the usefulness of this ticket...



---

archive/issue_comments_036688.json:
```json
{
    "body": "The patch commit string is insufficiently descriptive.  I've refreshed it to\n`#4838: Implement plotting of complex numbers` in the queue for 4.3.3.alpha0.",
    "created_at": "2010-02-10T15:24:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36688",
    "user": "mpatel"
}
```

The patch commit string is insufficiently descriptive.  I've refreshed it to
`#4838: Implement plotting of complex numbers` in the queue for 4.3.3.alpha0.



---

archive/issue_comments_036689.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:57:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4838",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4838#issuecomment-36689",
    "user": "mpatel"
}
```

Resolution: fixed
