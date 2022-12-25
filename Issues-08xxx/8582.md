# Issue 8582: sum(1/(1+k^2), k, -oo, oo) returns 0

archive/issues_008582.json:
```json
{
    "body": "Assignee: @burcin\n\nFrom [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/658b0fe8413b86f8):\n\n```\nBut I want to make a comment, also from this documentation. It says\nsum(1/(1+k^2), k, -oo, oo, algorithm = 'mathematica')     # optional\n-- requires mathematica\n\nOK, I understand that sage do not kown how to evaluate\nsum(1/(1+k^2), k, -oo, oo)\n\nBut it answer     0      , that is wrong!!!\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/8582\n\n",
    "closed_at": "2010-12-06T11:56:39Z",
    "created_at": "2010-03-23T04:13:54Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "sum(1/(1+k^2), k, -oo, oo) returns 0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8582",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: @burcin

From [sage-support](http://groups.google.com/group/sage-support/browse_thread/thread/658b0fe8413b86f8):

```
But I want to make a comment, also from this documentation. It says
sum(1/(1+k^2), k, -oo, oo, algorithm = 'mathematica')     # optional
-- requires mathematica

OK, I understand that sage do not kown how to evaluate
sum(1/(1+k^2), k, -oo, oo)

But it answer     0      , that is wrong!!!
```

Issue created by migration from https://trac.sagemath.org/ticket/8582





---

archive/issue_comments_077598.json:
```json
{
    "body": "This seems to be fixed in Maxima 5.21.1 or so:\n\n```\n\n(%i2) load(simplify_sum);\n(%o2) /Users/.../maxima/share/contrib/solve_rec/simplif\\\ny_sum.mac\n(%i5) display2d:false;\n\n(%o5) false\n(%i6) simplify_sum(sum(1/(1+k^2),k,-inf,inf));\n\n(%o6) -%i*(psi[0](%i+1)+%gamma)/2-%i*(psi[0](%i)+%gamma)/2\n                                 +%i*(psi[0](-%i)+%gamma)/2\n                                 +%i*(psi[0](1-%i)+%gamma)/2\n```\nWhich uses the digamma function quite a bit.  We don't get the (perhaps) simpler answer `pi coth(pi)`.",
    "created_at": "2010-09-22T14:43:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8582#issuecomment-77598",
    "user": "https://github.com/kcrisman"
}
```

This seems to be fixed in Maxima 5.21.1 or so:

```

(%i2) load(simplify_sum);
(%o2) /Users/.../maxima/share/contrib/solve_rec/simplif\
y_sum.mac
(%i5) display2d:false;

(%o5) false
(%i6) simplify_sum(sum(1/(1+k^2),k,-inf,inf));

(%o6) -%i*(psi[0](%i+1)+%gamma)/2-%i*(psi[0](%i)+%gamma)/2
                                 +%i*(psi[0](-%i)+%gamma)/2
                                 +%i*(psi[0](1-%i)+%gamma)/2
```
Which uses the digamma function quite a bit.  We don't get the (perhaps) simpler answer `pi coth(pi)`.



---

archive/issue_comments_077599.json:
```json
{
    "body": "This should hopefully be resolved by #8731.",
    "created_at": "2010-09-22T14:45:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8582#issuecomment-77599",
    "user": "https://github.com/kcrisman"
}
```

This should hopefully be resolved by #8731.



---

archive/issue_comments_077600.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-12-06T11:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8582#issuecomment-77600",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_020723.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-12-06T11:56:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8582#event-20723"
}
```



---

archive/issue_comments_077601.json:
```json
{
    "body": "This is fixed at ticket #10187 by upgrading to Maxima 5.22.1:\n\n```\n[mvngu@sage sage-4.6.1.alpha3]$ ./sage \n----------------------------------------------------------------------\n----------------------------------------------------------------------\n**********************************************************************\n*                                                                    *\n* Warning: this is a prerelease version, and it may be unstable.     *\n*                                                                    *\n**********************************************************************\nsage: k = var(\"k\") \nsage: sum(1/(1+k^2), k, -oo, oo)\n1/2*I*psi(-I) - 1/2*I*psi(I) + 1/2*I*psi(-I + 1) - 1/2*I*psi(I + 1)\nsage: %maxima\n| Sage Version 4.6.1.alpha3, Release Date: 2010-12-05                |\n| Type notebook() for the GUI, and license() for information.        |\n  --> Switching to Maxima <-- \n\n''\nmaxima: load(simplify_sum);\n\"/dev/shm/mvngu/sage-4.6.1.alpha3/local/share/maxima/5.22.1/share/contrib/solve_rec/simplify_sum.mac\"\nmaxima: display2d:false;\nfalse\nmaxima: \nmaxima: simplify_sum(sum(1/(1+k^2),k,-inf,inf));\n-%i*(psi[0](%i+1)+%gamma)/2-%i*(psi[0](%i)+%gamma)/2+%i*(psi[0](-%i)+%gamma)/2+%i*(psi[0](1-%i)+%gamma)/2\n```\n\nSo I'm closing this ticket as fixed.",
    "created_at": "2010-12-06T11:56:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8582#issuecomment-77601",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

This is fixed at ticket #10187 by upgrading to Maxima 5.22.1:

```
[mvngu@sage sage-4.6.1.alpha3]$ ./sage 
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
sage: k = var("k") 
sage: sum(1/(1+k^2), k, -oo, oo)
1/2*I*psi(-I) - 1/2*I*psi(I) + 1/2*I*psi(-I + 1) - 1/2*I*psi(I + 1)
sage: %maxima
| Sage Version 4.6.1.alpha3, Release Date: 2010-12-05                |
| Type notebook() for the GUI, and license() for information.        |
  --> Switching to Maxima <-- 

''
maxima: load(simplify_sum);
"/dev/shm/mvngu/sage-4.6.1.alpha3/local/share/maxima/5.22.1/share/contrib/solve_rec/simplify_sum.mac"
maxima: display2d:false;
false
maxima: 
maxima: simplify_sum(sum(1/(1+k^2),k,-inf,inf));
-%i*(psi[0](%i+1)+%gamma)/2-%i*(psi[0](%i)+%gamma)/2+%i*(psi[0](-%i)+%gamma)/2+%i*(psi[0](1-%i)+%gamma)/2
```

So I'm closing this ticket as fixed.



---

archive/issue_comments_077602.json:
```json
{
    "body": "Is that doctested in the patches for #10187?",
    "created_at": "2010-12-06T13:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8582#issuecomment-77602",
    "user": "https://github.com/kcrisman"
}
```

Is that doctested in the patches for #10187?



---

archive/issue_comments_077603.json:
```json
{
    "body": "Replying to [comment:4 kcrisman]:\n> Is that doctested in the patches for #10187?\n\n\nNo. But it shouldn't be difficult to write a documentation patch with doctests in the current ticket. The Sage 4.6.1 release cycle is now in feature freeze, but I think documentation patches are OK for merging in the upcoming release candidates.",
    "created_at": "2010-12-06T13:34:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8582#issuecomment-77603",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:4 kcrisman]:
> Is that doctested in the patches for #10187?


No. But it shouldn't be difficult to write a documentation patch with doctests in the current ticket. The Sage 4.6.1 release cycle is now in feature freeze, but I think documentation patches are OK for merging in the upcoming release candidates.



---

archive/issue_comments_077604.json:
```json
{
    "body": "See #10434 for a follow-up documentation ticket.",
    "created_at": "2010-12-06T13:40:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8582",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8582#issuecomment-77604",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

See #10434 for a follow-up documentation ticket.
