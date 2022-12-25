# Issue 2614: [with patch, needs review] MPolynomial coefficient/polynomial_coefficient merging

archive/issues_002614.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: multivariate coefficient\n\nThis ticket is a continuation and final aim of #2385.  I was hoping to generate a bit of discussion with that patch, but it got merged before the discussion was generated.\n\nThe end result is this (illustrated with ZZ, but applying equally to QQ):\n\n```\nsage: R.<x,y,z> = ZZ[]\nsage: f=(-x^2-x+3)*(y-1)\nsage: f\n-1*x^2*y + x^2 - x*y + x + 3*y - 3\nsage: f.coefficient(x^1)\n-1*y + 1\nsage: f.coefficient(x^0)\n-1*x^2*y + x^2 - x*y + x + 3*y - 3\nsage: f.coefficient({x:0})\n3*y - 3\nsage: f.coefficient([0,None,None])\n3*y - 3\n```\n\n\nNote that the \"f.coefficient(x^0)\" is possibly mis-leading and this motivated both #2385 and this ticket.  Note that for ZZ \"f.coefficient(x^0)\" actually returned the constant coefficient as a special case -- I think that was dead wrong.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2614\n\n",
    "created_at": "2008-03-20T14:46:25Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "[with patch, needs review] MPolynomial coefficient/polynomial_coefficient merging",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2614",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```
Assignee: @williamstein

Keywords: multivariate coefficient

This ticket is a continuation and final aim of #2385.  I was hoping to generate a bit of discussion with that patch, but it got merged before the discussion was generated.

The end result is this (illustrated with ZZ, but applying equally to QQ):

```
sage: R.<x,y,z> = ZZ[]
sage: f=(-x^2-x+3)*(y-1)
sage: f
-1*x^2*y + x^2 - x*y + x + 3*y - 3
sage: f.coefficient(x^1)
-1*y + 1
sage: f.coefficient(x^0)
-1*x^2*y + x^2 - x*y + x + 3*y - 3
sage: f.coefficient({x:0})
3*y - 3
sage: f.coefficient([0,None,None])
3*y - 3
```


Note that the "f.coefficient(x^0)" is possibly mis-leading and this motivated both #2385 and this ticket.  Note that for ZZ "f.coefficient(x^0)" actually returned the constant coefficient as a special case -- I think that was dead wrong.

Issue created by migration from https://trac.sagemath.org/ticket/2614





---

archive/issue_comments_017900.json:
```json
{
    "body": "Changing component from algebraic geometry to commutative algebra.",
    "created_at": "2008-03-20T14:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17900",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Changing component from algebraic geometry to commutative algebra.



---

archive/issue_comments_017901.json:
```json
{
    "body": "Changing assignee from @williamstein to @malb.",
    "created_at": "2008-03-20T14:50:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17901",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Changing assignee from @williamstein to @malb.



---

archive/issue_comments_017902.json:
```json
{
    "body": "I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?",
    "created_at": "2008-03-20T18:13:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17902",
    "user": "https://github.com/dfdeshom"
}
```

I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?



---

archive/issue_comments_017903.json:
```json
{
    "body": "Replying to [comment:3 dfdeshom]:\n> I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?\n>  \n\nWhat do you mean by \"restriction on a constant\"?  Is this bit what you are talking about:\n\n>Note that for ZZ \"f.coefficient(x0)\" actually returned the constant coefficient as a special case -- I think that was dead wrong.\n\nPerhaps I should have said:  In the current 2.10.4 code \"f.coefficient(x<sup>0</sup>)\" returns the constant coefficient -- I think this is dead wrong.\n\nI feel like I might be missing the point of your question.  If so, please clarify!",
    "created_at": "2008-03-20T19:00:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17903",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Replying to [comment:3 dfdeshom]:
> I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?
>  

What do you mean by "restriction on a constant"?  Is this bit what you are talking about:

>Note that for ZZ "f.coefficient(x0)" actually returned the constant coefficient as a special case -- I think that was dead wrong.

Perhaps I should have said:  In the current 2.10.4 code "f.coefficient(x<sup>0</sup>)" returns the constant coefficient -- I think this is dead wrong.

I feel like I might be missing the point of your question.  If so, please clarify!



---

archive/issue_comments_017904.json:
```json
{
    "body": "Replying to [comment:4 jbmohler]:\n> Replying to [comment:3 dfdeshom]:\n> > I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?\n> >  \n> \n> What do you mean by \"restriction on a constant\"?  Is this bit what you are talking about:\n> \n> >Note that for ZZ \"f.coefficient(x0)\" actually returned the constant coefficient as a special case -- I think that was dead wrong.\n\nActually, you were crystal clear. I was confused: I thought f was a mpoly in x and y only and was asking why you were doing `f.coefficient([0,None,None])`.",
    "created_at": "2008-03-20T19:37:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17904",
    "user": "https://github.com/dfdeshom"
}
```

Replying to [comment:4 jbmohler]:
> Replying to [comment:3 dfdeshom]:
> > I like the list of degree restrictions, but I'm confused: why give a restriction on a constant? Is  there a case where anything other than None will not give the same result?
> >  
> 
> What do you mean by "restriction on a constant"?  Is this bit what you are talking about:
> 
> >Note that for ZZ "f.coefficient(x0)" actually returned the constant coefficient as a special case -- I think that was dead wrong.

Actually, you were crystal clear. I was confused: I thought f was a mpoly in x and y only and was asking why you were doing `f.coefficient([0,None,None])`.



---

archive/issue_comments_017905.json:
```json
{
    "body": "Looks good.  I think it makes things much clearer than before, and the doctests are good.",
    "created_at": "2008-03-28T14:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17905",
    "user": "https://github.com/aghitza"
}
```

Looks good.  I think it makes things much clearer than before, and the doctests are good.



---

archive/issue_comments_017906.json:
```json
{
    "body": "Sorry, the patch no longer applies cleanly. Please rebase against 2.11.alpha2 out shortly:\n\n```\nsage-2.11.alpha2/devel/sage$ patch -p1 --dry-run < trac_2614_mpoly-coeff.patch\npatching file sage/rings/polynomial/multi_polynomial_element.py\nHunk #1 succeeded at 428 (offset -2 lines).\nHunk #2 succeeded at 439 with fuzz 1 (offset -2 lines).\nHunk #3 succeeded at 538 (offset -1 lines).\nHunk #4 succeeded at 550 (offset -1 lines).\nHunk #5 FAILED at 564.\nHunk #6 succeeded at 600 (offset -1 lines).\nHunk #7 succeeded at 612 (offset -1 lines).\n1 out of 7 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej\npatching file sage/rings/polynomial/multi_polynomial_libsingular.pyx\nHunk #1 succeeded at 2175 (offset 4 lines).\nHunk #2 succeeded at 2187 (offset 4 lines).\nHunk #3 succeeded at 2201 (offset 4 lines).\nHunk #4 succeeded at 2226 (offset 4 lines).\nHunk #5 succeeded at 2238 (offset 4 lines).\nHunk #6 succeeded at 2288 (offset 4 lines).\nHunk #7 succeeded at 2299 (offset 4 lines).\nHunk #8 succeeded at 2495 (offset 4 lines).\n```\n",
    "created_at": "2008-03-28T15:20:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17906",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Sorry, the patch no longer applies cleanly. Please rebase against 2.11.alpha2 out shortly:

```
sage-2.11.alpha2/devel/sage$ patch -p1 --dry-run < trac_2614_mpoly-coeff.patch
patching file sage/rings/polynomial/multi_polynomial_element.py
Hunk #1 succeeded at 428 (offset -2 lines).
Hunk #2 succeeded at 439 with fuzz 1 (offset -2 lines).
Hunk #3 succeeded at 538 (offset -1 lines).
Hunk #4 succeeded at 550 (offset -1 lines).
Hunk #5 FAILED at 564.
Hunk #6 succeeded at 600 (offset -1 lines).
Hunk #7 succeeded at 612 (offset -1 lines).
1 out of 7 hunks FAILED -- saving rejects to file sage/rings/polynomial/multi_polynomial_element.py.rej
patching file sage/rings/polynomial/multi_polynomial_libsingular.pyx
Hunk #1 succeeded at 2175 (offset 4 lines).
Hunk #2 succeeded at 2187 (offset 4 lines).
Hunk #3 succeeded at 2201 (offset 4 lines).
Hunk #4 succeeded at 2226 (offset 4 lines).
Hunk #5 succeeded at 2238 (offset 4 lines).
Hunk #6 succeeded at 2288 (offset 4 lines).
Hunk #7 succeeded at 2299 (offset 4 lines).
Hunk #8 succeeded at 2495 (offset 4 lines).
```




---

archive/issue_comments_017907.json:
```json
{
    "body": "rebased against 2.11.alpha2 (or some approximation there-of)",
    "created_at": "2008-03-28T18:11:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17907",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

rebased against 2.11.alpha2 (or some approximation there-of)



---

archive/issue_comments_017908.json:
```json
{
    "body": "Attachment [mpoly-coeff.patch](tarball://root/attachments/some-uuid/ticket2614/mpoly-coeff.patch) by jbmohler created at 2008-03-28 18:12:57\n\nThe current patch is re-based against 2.11.alpha1 augmented with patches from mabshoff's alpha2 release cycle directory.  I don't have a build of this to really test, but I believe doc-tests should pass.\n\nIf this is not integrated by the time alpha2 is released, I'll probably double-check some things with a built alpha2.",
    "created_at": "2008-03-28T18:12:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17908",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

Attachment [mpoly-coeff.patch](tarball://root/attachments/some-uuid/ticket2614/mpoly-coeff.patch) by jbmohler created at 2008-03-28 18:12:57

The current patch is re-based against 2.11.alpha1 augmented with patches from mabshoff's alpha2 release cycle directory.  I don't have a build of this to really test, but I believe doc-tests should pass.

If this is not integrated by the time alpha2 is released, I'll probably double-check some things with a built alpha2.



---

archive/issue_comments_017909.json:
```json
{
    "body": "The patch applies cleanly now. Merged in Sage 2.11.alpha2",
    "created_at": "2008-03-28T18:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17909",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The patch applies cleanly now. Merged in Sage 2.11.alpha2



---

archive/issue_comments_017910.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-28T18:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2614",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2614#issuecomment-17910",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
