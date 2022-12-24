# Issue 2586: latex products need to be space separated

archive/issues_002586.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @ncalexan\n\nKeywords: latex product polynomial\n\nI'm sure this is a dupe, but couldn't find a ticket.  It might need fixing at an awful lot of places... but polynomials are a start:\n\n\n```\nsage: ZZ['a']['b']([0, ZZ['a'].0])\na*b\nsage: latex(ZZ['a']['b']([0, ZZ['a'].0]))\nab\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2586\n\n",
    "created_at": "2008-03-18T17:01:07Z",
    "labels": [
        "user interface",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "latex products need to be space separated",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2586",
    "user": "@ncalexan"
}
```
Assignee: @williamstein

CC:  @ncalexan

Keywords: latex product polynomial

I'm sure this is a dupe, but couldn't find a ticket.  It might need fixing at an awful lot of places... but polynomials are a start:


```
sage: ZZ['a']['b']([0, ZZ['a'].0])
a*b
sage: latex(ZZ['a']['b']([0, ZZ['a'].0]))
ab
```


Issue created by migration from https://trac.sagemath.org/ticket/2586





---

archive/issue_comments_017699.json:
```json
{
    "body": "Some people might not think this is a problem.  This definitely is:\n\n\n```\nsage: latex(ZZ['alpha']['b']([0, ZZ['alpha'].0]))\n\\alphab\n```\n",
    "created_at": "2008-03-18T17:01:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17699",
    "user": "@ncalexan"
}
```

Some people might not think this is a problem.  This definitely is:


```
sage: latex(ZZ['alpha']['b']([0, ZZ['alpha'].0]))
\alphab
```




---

archive/issue_comments_017700.json:
```json
{
    "body": "I agree that this is a bug and I think the ticket you are referring to is the one where we discussed removing `\\cdot`. \n\nCheers,\n\nMichael",
    "created_at": "2008-03-18T20:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17700",
    "user": "mabshoff"
}
```

I agree that this is a bug and I think the ticket you are referring to is the one where we discussed removing `\cdot`. 

Cheers,

Michael



---

archive/issue_comments_017701.json:
```json
{
    "body": "Attachment [2586_latex_polynomials.patch](tarball://root/attachments/some-uuid/ticket2586/2586_latex_polynomials.patch) by @aghitza created at 2008-03-19 23:31:17",
    "created_at": "2008-03-19T23:31:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17701",
    "user": "@aghitza"
}
```

Attachment [2586_latex_polynomials.patch](tarball://root/attachments/some-uuid/ticket2586/2586_latex_polynomials.patch) by @aghitza created at 2008-03-19 23:31:17



---

archive/issue_comments_017702.json:
```json
{
    "body": "Attachment [2586_doc_const.patch](tarball://root/attachments/some-uuid/ticket2586/2586_doc_const.patch) by @aghitza created at 2008-03-19 23:32:35",
    "created_at": "2008-03-19T23:32:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17702",
    "user": "@aghitza"
}
```

Attachment [2586_doc_const.patch](tarball://root/attachments/some-uuid/ticket2586/2586_doc_const.patch) by @aghitza created at 2008-03-19 23:32:35



---

archive/issue_comments_017703.json:
```json
{
    "body": "Actually, it's not due to #384: that only touched the symbolic expressions, and you can check that the code puts spaces where \\cdot's used to be.\n\nBut it does happen in a few places in the polynomials code.  I believe the patch fixes all of them.  In particular, Nick's examples now work properly.\n\nThis (un)broke a bunch of doctests, so I've fixed them as well.  See also the doc patch with a small fix to const.tex due to these changes.",
    "created_at": "2008-03-19T23:33:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17703",
    "user": "@aghitza"
}
```

Actually, it's not due to #384: that only touched the symbolic expressions, and you can check that the code puts spaces where \cdot's used to be.

But it does happen in a few places in the polynomials code.  I believe the patch fixes all of them.  In particular, Nick's examples now work properly.

This (un)broke a bunch of doctests, so I've fixed them as well.  See also the doc patch with a small fix to const.tex due to these changes.



---

archive/issue_comments_017704.json:
```json
{
    "body": "Both patches look good to me. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T03:36:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17704",
    "user": "mabshoff"
}
```

Both patches look good to me. Positive review.

Cheers,

Michael



---

archive/issue_comments_017705.json:
```json
{
    "body": "referee's patch to fix some more doctest failures",
    "created_at": "2008-03-21T04:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17705",
    "user": "mabshoff"
}
```

referee's patch to fix some more doctest failures



---

archive/issue_comments_017706.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T04:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17706",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017707.json:
```json
{
    "body": "Attachment [trac_2586-further-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket2586/trac_2586-further-doctest-fixes.patch) by mabshoff created at 2008-03-21 04:17:19\n\nMerged all three patches in Sage 2.11.alpha1",
    "created_at": "2008-03-21T04:17:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2586",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2586#issuecomment-17707",
    "user": "mabshoff"
}
```

Attachment [trac_2586-further-doctest-fixes.patch](tarball://root/attachments/some-uuid/ticket2586/trac_2586-further-doctest-fixes.patch) by mabshoff created at 2008-03-21 04:17:19

Merged all three patches in Sage 2.11.alpha1
