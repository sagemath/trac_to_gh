# Issue 3479: [with patch, needs review] update dsage portion of tut.tex

archive/issues_003479.json:
```json
{
    "body": "Assignee: tba\n\nThis patch provides 2 more examples on how to use the distributed map() function in dsage as well as the `@`parallel decorator.\n\nTo get the tutorial to build correctly I needed to remove all the temporary files and run the 'build_pdf' script twice to generate the index. \n\nThis patch depends on #3467 and the `@`parallel decorator patches going in.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3479\n\n",
    "created_at": "2008-06-19T22:29:22Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "[with patch, needs review] update dsage portion of tut.tex",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3479",
    "user": "https://github.com/yqiang"
}
```
Assignee: tba

This patch provides 2 more examples on how to use the distributed map() function in dsage as well as the `@`parallel decorator.

To get the tutorial to build correctly I needed to remove all the temporary files and run the 'build_pdf' script twice to generate the index. 

This patch depends on #3467 and the `@`parallel decorator patches going in.

Issue created by migration from https://trac.sagemath.org/ticket/3479





---

archive/issue_comments_024465.json:
```json
{
    "body": "Patch for doc/tut/tut.tex",
    "created_at": "2008-06-19T22:30:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24465",
    "user": "https://github.com/yqiang"
}
```

Patch for doc/tut/tut.tex



---

archive/issue_comments_024466.json:
```json
{
    "body": "Attachment [3479_dsage_tut.patch](tarball://root/attachments/some-uuid/ticket3479/3479_dsage_tut.patch) by @mwhansen created at 2008-06-19 22:31:35\n\nYi, does your patch apply with #3347 applied?",
    "created_at": "2008-06-19T22:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24466",
    "user": "https://github.com/mwhansen"
}
```

Attachment [3479_dsage_tut.patch](tarball://root/attachments/some-uuid/ticket3479/3479_dsage_tut.patch) by @mwhansen created at 2008-06-19 22:31:35

Yi, does your patch apply with #3347 applied?



---

archive/issue_comments_024467.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mhansen\".",
    "created_at": "2008-06-19T22:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24467",
    "user": "https://github.com/mwhansen"
}
```

Changing keywords from "" to "editor_mhansen".



---

archive/issue_comments_024468.json:
```json
{
    "body": "The patch fails against the current version of the tutorial.\n\nWhen applied manually, the patch seems okay, and passes all doctests. A few comments:\n\nIn example 3, item 5, I would suggest changing `$f$` to `\\code{f`}, for the sake of better latex to html conversion.\n\nIn example 4, the verbatim block looks odd, especially in the live version of the tutorial.\n\nIf you fix at least example 3, and produce a patch against the current tutorial, I'll give it a positive review.\n\n(In general, I find the style of using numbered instructions, as in all of the dsage examples, at odds with the style of the rest of the tutorial.  It would be nice if this were rewritten, but that can wait for a separate trac item and patch.)",
    "created_at": "2008-08-13T19:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24468",
    "user": "https://github.com/jhpalmieri"
}
```

The patch fails against the current version of the tutorial.

When applied manually, the patch seems okay, and passes all doctests. A few comments:

In example 3, item 5, I would suggest changing `$f$` to `\code{f`}, for the sake of better latex to html conversion.

In example 4, the verbatim block looks odd, especially in the live version of the tutorial.

If you fix at least example 3, and produce a patch against the current tutorial, I'll give it a positive review.

(In general, I find the style of using numbered instructions, as in all of the dsage examples, at odds with the style of the rest of the tutorial.  It would be nice if this were rewritten, but that can wait for a separate trac item and patch.)



---

archive/issue_comments_024469.json:
```json
{
    "body": "By the way, what does \"% (fold)\" mean?  This only appears in the dsage part of the tutorial, and I don't know what role it plays.",
    "created_at": "2008-08-13T21:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24469",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, what does "% (fold)" mean?  This only appears in the dsage part of the tutorial, and I don't know what role it plays.



---

archive/issue_comments_024470.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-24T09:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24470",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_024471.json:
```json
{
    "body": "Changing assignee from tba to @mwhansen.",
    "created_at": "2009-01-24T09:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24471",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from tba to @mwhansen.



---

archive/issue_comments_024472.json:
```json
{
    "body": "I addressed the referee's comment and added this to the Sphinx version of the tutorial.",
    "created_at": "2009-01-24T09:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24472",
    "user": "https://github.com/mwhansen"
}
```

I addressed the referee's comment and added this to the Sphinx version of the tutorial.



---

archive/issue_comments_024473.json:
```json
{
    "body": "Merged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T17:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24473",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.alpha0.

Cheers,

Michael



---

archive/issue_comments_024474.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T17:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3479",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3479#issuecomment-24474",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
