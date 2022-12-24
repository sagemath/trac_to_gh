# Issue 5622: complex double fast callable interpreter

archive/issues_005622.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  cwitty\n\nAfter RDF and RR, CDF would be very handy to have too. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5622\n\n",
    "created_at": "2009-03-28T10:02:35Z",
    "labels": [
        "basic arithmetic",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "complex double fast callable interpreter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5622",
    "user": "@robertwb"
}
```
Assignee: somebody

CC:  cwitty

After RDF and RR, CDF would be very handy to have too. 

Issue created by migration from https://trac.sagemath.org/ticket/5622





---

archive/issue_comments_043901.json:
```json
{
    "body": "I started thinking about this as I was refereeing the original ticket, trying to make sure I understood how it all worked.",
    "created_at": "2009-03-28T10:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43901",
    "user": "@robertwb"
}
```

I started thinking about this as I was refereeing the original ticket, trying to make sure I understood how it all worked.



---

archive/issue_comments_043902.json:
```json
{
    "body": "Attachment [5622-fast-callable-cdf.patch](tarball://root/attachments/some-uuid/ticket5622/5622-fast-callable-cdf.patch) by cwitty created at 2009-03-28 16:56:24\n\nCode looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.\n\nMichael, I see two potential portability issues with the code:\n\n1) it uses C99 complex numbers\n\n2) it adds the compiler argument -std=c99\n\nI'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?",
    "created_at": "2009-03-28T16:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43902",
    "user": "cwitty"
}
```

Attachment [5622-fast-callable-cdf.patch](tarball://root/attachments/some-uuid/ticket5622/5622-fast-callable-cdf.patch) by cwitty created at 2009-03-28 16:56:24

Code looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.

Michael, I see two potential portability issues with the code:

1) it uses C99 complex numbers

2) it adds the compiler argument -std=c99

I'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?



---

archive/issue_comments_043903.json:
```json
{
    "body": "Replying to [comment:2 cwitty]:\n> Code looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.\n> \n> Michael, I see two potential portability issues with the code:\n> \n> 1) it uses C99 complex numbers\n\nThat is not a problem. FLINT mandates that we use C99 anyway.\n\n> 2) it adds the compiler argument -std=c99\n\nWe can work around that.\n\n> I'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?\n\nNot at the moment, but there is work under way to support the pathscale compiler for SiCortex. \n\nCheers,\n\nMichael",
    "created_at": "2009-03-28T17:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43903",
    "user": "mabshoff"
}
```

Replying to [comment:2 cwitty]:
> Code looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.
> 
> Michael, I see two potential portability issues with the code:
> 
> 1) it uses C99 complex numbers

That is not a problem. FLINT mandates that we use C99 anyway.

> 2) it adds the compiler argument -std=c99

We can work around that.

> I'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?

Not at the moment, but there is work under way to support the pathscale compiler for SiCortex. 

Cheers,

Michael



---

archive/issue_comments_043904.json:
```json
{
    "body": "Thanks. \n\nBTW, It compiles fine with gcc without the c99 flag, but I figured I'd put it there to be explicit. (I actually only knew about that flag because of flint.)",
    "created_at": "2009-03-28T18:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43904",
    "user": "@robertwb"
}
```

Thanks. 

BTW, It compiles fine with gcc without the c99 flag, but I figured I'd put it there to be explicit. (I actually only knew about that flag because of flint.)



---

archive/issue_comments_043905.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T06:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43905",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043906.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T06:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43906",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_043907.json:
```json
{
    "body": "The work around for the bug in Cython < 0.11 can be removed because we upgraded to Cython 0.11 in this release of Sage, right?\n\nfrom patch above:\n\n```\n# This is to work around a header ordering bug in Cython < 0.11 \n# (Pari is included from sage.rings.complex_double.) \n```\n",
    "created_at": "2009-04-11T11:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43907",
    "user": "@jasongrout"
}
```

The work around for the bug in Cython < 0.11 can be removed because we upgraded to Cython 0.11 in this release of Sage, right?

from patch above:

```
# This is to work around a header ordering bug in Cython < 0.11 
# (Pari is included from sage.rings.complex_double.) 
```

