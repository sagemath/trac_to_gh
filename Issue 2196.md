# Issue 2196: Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0

archive/issues_002196.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.\n\nNote that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.\n\nThe patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2196\n\n",
    "created_at": "2008-02-17T19:09:35Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.2",
    "title": "Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2196",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @williamstein

The code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.

Note that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.

The patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).

Issue created by migration from https://trac.sagemath.org/ticket/2196





---

archive/issue_comments_014393.json:
```json
{
    "body": "Attachment [8313.patch](tarball://root/attachments/some-uuid/ticket2196/8313.patch) by mabshoff created at 2008-02-17 19:11:27",
    "created_at": "2008-02-17T19:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [8313.patch](tarball://root/attachments/some-uuid/ticket2196/8313.patch) by mabshoff created at 2008-02-17 19:11:27



---

archive/issue_comments_014394.json:
```json
{
    "body": "There are some typos.  Lines 964 and 965 don't line up, and line 968 should say \"Sextic twist\".\n\n\n```\n\t963\t \n956\t964\t        if self.j_invariant() !=K(0): \n957\t965\t            raise ValueError, \"Sextic twist not defined when j!=1728\" \n \t966\t \n \t967\t        if D.is_zero(): \n \t968\t            raise ValueError, \"quartic twist requires a nonzero argument\" \n```\n",
    "created_at": "2008-02-17T19:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14394",
    "user": "https://github.com/ncalexan"
}
```

There are some typos.  Lines 964 and 965 don't line up, and line 968 should say "Sextic twist".


```
	963	 
956	964	        if self.j_invariant() !=K(0): 
957	965	            raise ValueError, "Sextic twist not defined when j!=1728" 
 	966	 
 	967	        if D.is_zero(): 
 	968	            raise ValueError, "quartic twist requires a nonzero argument" 
```




---

archive/issue_comments_014395.json:
```json
{
    "body": "Attachment [8314.patch](tarball://root/attachments/some-uuid/ticket2196/8314.patch) by @JohnCremona created at 2008-02-17 20:21:21\n\nto be applied after 8313.patch",
    "created_at": "2008-02-17T20:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14395",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8314.patch](tarball://root/attachments/some-uuid/ticket2196/8314.patch) by @JohnCremona created at 2008-02-17 20:21:21

to be applied after 8313.patch



---

archive/issue_comments_014396.json:
```json
{
    "body": "Patch 8314.patch fixes the typo and improved docstrings, but I could not see the non-lining up of lines.",
    "created_at": "2008-02-17T20:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14396",
    "user": "https://github.com/JohnCremona"
}
```

Patch 8314.patch fixes the typo and improved docstrings, but I could not see the non-lining up of lines.



---

archive/issue_comments_014397.json:
```json
{
    "body": "This should be applied.  What I meant by 'not line up' was that they are incongruous:\n\n```\nif self.j_invariant() !=K(0): raise ValueError, \"Sextic twist not defined when j!=1728\"\n```\n\nThe test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix?",
    "created_at": "2008-02-17T20:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14397",
    "user": "https://github.com/ncalexan"
}
```

This should be applied.  What I meant by 'not line up' was that they are incongruous:

```
if self.j_invariant() !=K(0): raise ValueError, "Sextic twist not defined when j!=1728"
```

The test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix?



---

archive/issue_comments_014398.json:
```json
{
    "body": "Attachment [8315.patch](tarball://root/attachments/some-uuid/ticket2196/8315.patch) by @JohnCremona created at 2008-02-17 20:35:51\n\nand finally....",
    "created_at": "2008-02-17T20:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14398",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [8315.patch](tarball://root/attachments/some-uuid/ticket2196/8315.patch) by @JohnCremona created at 2008-02-17 20:35:51

and finally....



---

archive/issue_comments_014399.json:
```json
{
    "body": "Replying to [comment:4 ncalexan]:\n> This should be applied.  What I meant by 'not line up' was that they are incongruous:\n> {{{\n> if self.j_invariant() !=K(0): raise ValueError, \"Sextic twist not defined when j!=1728\"\n> }}}\n> The test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix? \n\n You are quite right, the error message should have had 0 instead of 1728.  Patch 8315.patch fizes that.  Sorry.",
    "created_at": "2008-02-17T20:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14399",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:4 ncalexan]:
> This should be applied.  What I meant by 'not line up' was that they are incongruous:
> {{{
> if self.j_invariant() !=K(0): raise ValueError, "Sextic twist not defined when j!=1728"
> }}}
> The test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix? 

 You are quite right, the error message should have had 0 instead of 1728.  Patch 8315.patch fizes that.  Sorry.



---

archive/issue_comments_014400.json:
```json
{
    "body": "Apply every patch.",
    "created_at": "2008-02-17T20:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14400",
    "user": "https://github.com/ncalexan"
}
```

Apply every patch.



---

archive/issue_comments_014401.json:
```json
{
    "body": "Merged 8313.patch, 8314.patch and 8315.patch in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T20:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14401",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 8313.patch, 8314.patch and 8315.patch in Sage 2.10.2.alpha1



---

archive/issue_comments_014402.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T20:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
