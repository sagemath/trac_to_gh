# Issue 5004: bug in latexing of powers of negative numbers

archive/issues_005004.json:
```json
{
    "body": "Assignee: @burcin\n\n\n```\n>\n> Hello all\n>\n> The command latex(7-(-1)^(1/3))   produces 7 - {-1}^{\\frac{1}{3}}\n> Is it possible to change it into 7 - \\left(-1\\right)^{\\frac{1}{3}}\n>\n> Which function should be redefined to gain this behavior?\n>\n> I think that two minus sign, one following the other, could be\n> confusing (for students of economics, for example :) )\n>\n> Thank you\n> Robert\n\nI would start by doing:\n\nsage: a = (-1)^(1/3)\nsage: a._latex_??\n[... source code in calculus.py...]\n\nThen I would look at the code, and be confused for about an hour, finally probably figure out what is going on, and maybe with luck be able to fix this.\nIIRC the code to get the latex for symbolic expressions is complicated.  I think it was written by Bobby Moretti (and undergrad who used to be a sage developer).\n\nI think this sort of behavior, e.g.,\n\nsage: a = (-1)^(1/4)\nsage: latex(a)\n{-1}^{\\frac{1}{4}} \n\nshould officially be considered a bug in fact.  It's not just confusing, it's wrong. \n\nBy the way, one trick you can use is to convert the expression to maxima first and use its latex.  For some things, e.g., your example above, this works better:\n\nsage: a = 7-(-1)^(1/3)\nsage: latex(a._maxima_())\n7-\\left(-1\\right)^`1}\\over{3`\n\nDon't use maxima(a), since then you'll get a in a session of maxima that has different defaults than the calculus module uses, in particular, roots are always assumed real, which may be bad (though maybe ok for economists):\n\nsage: a = 7-(-1)^(1/3)\nsage: latex(maxima(a))\n8\n\n -- William\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5004\n\n",
    "created_at": "2009-01-17T21:29:04Z",
    "labels": [
        "component: calculus",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "bug in latexing of powers of negative numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5004",
    "user": "https://github.com/williamstein"
}
```
Assignee: @burcin


```
>
> Hello all
>
> The command latex(7-(-1)^(1/3))   produces 7 - {-1}^{\frac{1}{3}}
> Is it possible to change it into 7 - \left(-1\right)^{\frac{1}{3}}
>
> Which function should be redefined to gain this behavior?
>
> I think that two minus sign, one following the other, could be
> confusing (for students of economics, for example :) )
>
> Thank you
> Robert

I would start by doing:

sage: a = (-1)^(1/3)
sage: a._latex_??
[... source code in calculus.py...]

Then I would look at the code, and be confused for about an hour, finally probably figure out what is going on, and maybe with luck be able to fix this.
IIRC the code to get the latex for symbolic expressions is complicated.  I think it was written by Bobby Moretti (and undergrad who used to be a sage developer).

I think this sort of behavior, e.g.,

sage: a = (-1)^(1/4)
sage: latex(a)
{-1}^{\frac{1}{4}} 

should officially be considered a bug in fact.  It's not just confusing, it's wrong. 

By the way, one trick you can use is to convert the expression to maxima first and use its latex.  For some things, e.g., your example above, this works better:

sage: a = 7-(-1)^(1/3)
sage: latex(a._maxima_())
7-\left(-1\right)^`1}\over{3`

Don't use maxima(a), since then you'll get a in a session of maxima that has different defaults than the calculus module uses, in particular, roots are always assumed real, which may be bad (though maybe ok for economists):

sage: a = 7-(-1)^(1/3)
sage: latex(maxima(a))
8

 -- William
```


Issue created by migration from https://trac.sagemath.org/ticket/5004





---

archive/issue_comments_038097.json:
```json
{
    "body": "Attachment [trac_5004.patch](tarball://root/attachments/some-uuid/ticket5004/trac_5004.patch) by @mwhansen created at 2009-01-17 21:58:51",
    "created_at": "2009-01-17T21:58:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5004#issuecomment-38097",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_5004.patch](tarball://root/attachments/some-uuid/ticket5004/trac_5004.patch) by @mwhansen created at 2009-01-17 21:58:51



---

archive/issue_comments_038098.json:
```json
{
    "body": "Looks great !  I'm glad you untangled the code.  \n\nI doctested the whole tree and nothing breaks:\n\n\n```\nAll tests passed!\nTimings have been updated.\nTotal time for all tests: 145.9 seconds    \nwstein@sage:/space/sage-3.2.3$ \n```\n\n\nYep, 145 seconds on the new hardware on a ram disk :-)\n\nWilliam",
    "created_at": "2009-01-17T22:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5004#issuecomment-38098",
    "user": "https://github.com/williamstein"
}
```

Looks great !  I'm glad you untangled the code.  

I doctested the whole tree and nothing breaks:


```
All tests passed!
Timings have been updated.
Total time for all tests: 145.9 seconds    
wstein@sage:/space/sage-3.2.3$ 
```


Yep, 145 seconds on the new hardware on a ram disk :-)

William



---

archive/issue_comments_038099.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T15:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5004#issuecomment-38099",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005248.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-01-18T15:57:22Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5004",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5004#event-5248"
}
```



---

archive/issue_comments_038100.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T15:57:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5004",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5004#issuecomment-38100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.3.alpha0
