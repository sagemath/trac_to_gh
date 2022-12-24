# Issue 594: Teach the MAGMA interface how to handle GF(q) conversions

archive/issues_000594.json:
```json
{
    "body": "Assignee: was\n\nThe attached patch implements conversion to/from MAGMA polynomials over non-prime finite fields.\n\nIssue created by migration from https://trac.sagemath.org/ticket/594\n\n",
    "created_at": "2007-09-05T16:27:33Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.4",
    "title": "Teach the MAGMA interface how to handle GF(q) conversions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/594",
    "user": "malb"
}
```
Assignee: was

The attached patch implements conversion to/from MAGMA polynomials over non-prime finite fields.

Issue created by migration from https://trac.sagemath.org/ticket/594





---

archive/issue_comments_003061.json:
```json
{
    "body": "Attachment [magma_gfq.patch](tarball://root/attachments/some-uuid/ticket594/magma_gfq.patch) by malb created at 2007-09-05 16:29:57\n\nForgot to mention:\n* please review carefully, this includes a change to SageObject and FiniteField\n* 'make test' passes (didn't try optional because I don't have all optional packages installed)",
    "created_at": "2007-09-05T16:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/594#issuecomment-3061",
    "user": "malb"
}
```

Attachment [magma_gfq.patch](tarball://root/attachments/some-uuid/ticket594/magma_gfq.patch) by malb created at 2007-09-05 16:29:57

Forgot to mention:
* please review carefully, this includes a change to SageObject and FiniteField
* 'make test' passes (didn't try optional because I don't have all optional packages installed)



---

archive/issue_comments_003062.json:
```json
{
    "body": "The patch adds a couple of debug print statements, e.g.,\n\n```\n  +        print \"INPUT\",x\n```\n",
    "created_at": "2007-09-05T21:34:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/594#issuecomment-3062",
    "user": "was"
}
```

The patch adds a couple of debug print statements, e.g.,

```
  +        print "INPUT",x
```




---

archive/issue_comments_003063.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> The patch adds a couple of debug print statements, e.g.,\n> {{{\n>   +        print \"INPUT\",x\n> }}}\n\nand removes them again in the second patch in the file. `sage -upgrade` committed my unfinished business.",
    "created_at": "2007-09-05T21:47:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/594#issuecomment-3063",
    "user": "malb"
}
```

Replying to [comment:2 was]:
> The patch adds a couple of debug print statements, e.g.,
> {{{
>   +        print "INPUT",x
> }}}

and removes them again in the second patch in the file. `sage -upgrade` committed my unfinished business.



---

archive/issue_comments_003064.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T17:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/594",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/594#issuecomment-3064",
    "user": "was"
}
```

Resolution: fixed
