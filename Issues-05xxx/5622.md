# Issue 5622: [with patch, positive review] complex double fast callable interpreter

archive/issues_005622.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  cwitty\n\nAfter RDF and RR, CDF would be very handy to have too. \n\nIssue created by migration from https://trac.sagemath.org/ticket/5622\n\n",
    "closed_at": "2009-03-31T06:18:46Z",
    "created_at": "2009-03-28T10:02:35Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] complex double fast callable interpreter",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5622",
    "user": "https://github.com/robertwb"
}
```
Assignee: somebody

CC:  cwitty

After RDF and RR, CDF would be very handy to have too. 

Issue created by migration from https://trac.sagemath.org/ticket/5622





---

archive/issue_comments_043816.json:
```json
{
    "body": "I started thinking about this as I was refereeing the original ticket, trying to make sure I understood how it all worked.",
    "created_at": "2009-03-28T10:05:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43816",
    "user": "https://github.com/robertwb"
}
```

I started thinking about this as I was refereeing the original ticket, trying to make sure I understood how it all worked.



---

archive/issue_comments_043817.json:
```json
{
    "body": "Attachment [5622-fast-callable-cdf.patch](tarball://root/attachments/some-uuid/ticket5622/5622-fast-callable-cdf.patch) by cwitty created at 2009-03-28 16:56:24\n\nCode looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.\n\nMichael, I see two potential portability issues with the code:\n\n1) it uses C99 complex numbers\n\n2) it adds the compiler argument -std=c99\n\nI'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?",
    "created_at": "2009-03-28T16:56:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43817",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [5622-fast-callable-cdf.patch](tarball://root/attachments/some-uuid/ticket5622/5622-fast-callable-cdf.patch) by cwitty created at 2009-03-28 16:56:24

Code looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.

Michael, I see two potential portability issues with the code:

1) it uses C99 complex numbers

2) it adds the compiler argument -std=c99

I'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?



---

archive/issue_comments_043818.json:
```json
{
    "body": "Replying to [comment:2 cwitty]:\n> Code looks good, doctests pass.  Positive review, unless Michael complains about the portability issues.\n> \n> Michael, I see two potential portability issues with the code:\n> \n> 1) it uses C99 complex numbers\n\n\nThat is not a problem. FLINT mandates that we use C99 anyway.\n\n> 2) it adds the compiler argument -std=c99\n\n\nWe can work around that.\n\n> I'm guessing the latter will only work with gcc (unless other compilers specifically copy gcc command-line arguments).  Does Sage currently build with non-gcc compilers?\n\n\nNot at the moment, but there is work under way to support the pathscale compiler for SiCortex. \n\nCheers,\n\nMichael",
    "created_at": "2009-03-28T17:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43818",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
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

archive/issue_comments_043819.json:
```json
{
    "body": "Thanks. \n\nBTW, It compiles fine with gcc without the c99 flag, but I figured I'd put it there to be explicit. (I actually only knew about that flag because of flint.)",
    "created_at": "2009-03-28T18:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43819",
    "user": "https://github.com/robertwb"
}
```

Thanks. 

BTW, It compiles fine with gcc without the c99 flag, but I figured I'd put it there to be explicit. (I actually only knew about that flag because of flint.)



---

archive/issue_events_013229.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-31T06:18:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5622#event-13229"
}
```



---

archive/issue_comments_043820.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T06:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43820",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_013230.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-31T06:18:46Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5622#event-13230"
}
```



---

archive/issue_comments_043821.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T06:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_043822.json:
```json
{
    "body": "The work around for the bug in Cython < 0.11 can be removed because we upgraded to Cython 0.11 in this release of Sage, right?\n\nfrom patch above:\n\n```\n# This is to work around a header ordering bug in Cython < 0.11 \n# (Pari is included from sage.rings.complex_double.) \n```",
    "created_at": "2009-04-11T11:36:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5622",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5622#issuecomment-43822",
    "user": "https://github.com/jasongrout"
}
```

The work around for the bug in Cython < 0.11 can be removed because we upgraded to Cython 0.11 in this release of Sage, right?

from patch above:

```
# This is to work around a header ordering bug in Cython < 0.11 
# (Pari is included from sage.rings.complex_double.) 
```
