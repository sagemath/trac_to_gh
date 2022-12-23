# Issue 2196: Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0

archive/issues_002196.json:
```json
{
    "body": "Assignee: was\n\nThe code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.\n\nNote that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.\n\nThe patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).\n\nIssue created by migration from https://trac.sagemath.org/ticket/2196\n\n",
    "created_at": "2008-02-17T19:09:35Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "Elliptic Curve quadratic/quartic/sextic twists: unhelpful error message when D=0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2196",
    "user": "cremona"
}
```
Assignee: was

The code for quadratic, quartic and sextic twists of elliptic curves does not check that the twisting parameter is nonzero, and hence fail when a singular curve tries to be constructed.  Instead we output a helpful message.

Note that in characteristic 2, the quadratic twist by 0 is allowed (but gives back the same curve), just as twisting by 1 in odd characteristic.

The patch provided also enhances the Hasse_bounds function (which should probably be put somewhere other than ell_generic.py).

Issue created by migration from https://trac.sagemath.org/ticket/2196





---

archive/issue_comments_014424.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-17T19:11:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14424",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_014425.json:
```json
{
    "body": "There are some typos.  Lines 964 and 965 don't line up, and line 968 should say \"Sextic twist\".\n\n\n```\n\t963\t \n956\t964\t        if self.j_invariant() !=K(0): \n957\t965\t            raise ValueError, \"Sextic twist not defined when j!=1728\" \n \t966\t \n \t967\t        if D.is_zero(): \n \t968\t            raise ValueError, \"quartic twist requires a nonzero argument\" \n```\n",
    "created_at": "2008-02-17T19:24:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14425",
    "user": "ncalexan"
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

archive/issue_comments_014426.json:
```json
{
    "body": "Attachment\n\nto be applied after 8313.patch",
    "created_at": "2008-02-17T20:21:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14426",
    "user": "cremona"
}
```

Attachment

to be applied after 8313.patch



---

archive/issue_comments_014427.json:
```json
{
    "body": "Patch 8314.patch fixes the typo and improved docstrings, but I could not see the non-lining up of lines.",
    "created_at": "2008-02-17T20:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14427",
    "user": "cremona"
}
```

Patch 8314.patch fixes the typo and improved docstrings, but I could not see the non-lining up of lines.



---

archive/issue_comments_014428.json:
```json
{
    "body": "This should be applied.  What I meant by 'not line up' was that they are incongruous:\n\n```\nif self.j_invariant() !=K(0): raise ValueError, \"Sextic twist not defined when j!=1728\"\n```\n\nThe test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix?",
    "created_at": "2008-02-17T20:29:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14428",
    "user": "ncalexan"
}
```

This should be applied.  What I meant by 'not line up' was that they are incongruous:

```
if self.j_invariant() !=K(0): raise ValueError, "Sextic twist not defined when j!=1728"
```

The test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix?



---

archive/issue_comments_014429.json:
```json
{
    "body": "Attachment\n\nand finally....",
    "created_at": "2008-02-17T20:35:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14429",
    "user": "cremona"
}
```

Attachment

and finally....



---

archive/issue_comments_014430.json:
```json
{
    "body": "Replying to [comment:4 ncalexan]:\n> This should be applied.  What I meant by 'not line up' was that they are incongruous:\n> {{{\n> if self.j_invariant() !=K(0): raise ValueError, \"Sextic twist not defined when j!=1728\"\n> }}}\n> The test is for $K(0)$ but the message reads $j != 1728$.  What is the correct fix? \n\n You are quite right, the error message should have had 0 instead of 1728.  Patch 8315.patch fizes that.  Sorry.",
    "created_at": "2008-02-17T20:36:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14430",
    "user": "cremona"
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

archive/issue_comments_014431.json:
```json
{
    "body": "Apply every patch.",
    "created_at": "2008-02-17T20:54:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14431",
    "user": "ncalexan"
}
```

Apply every patch.



---

archive/issue_comments_014432.json:
```json
{
    "body": "Merged 8313.patch, 8314.patch and 8315.patch in Sage 2.10.2.alpha1",
    "created_at": "2008-02-17T20:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14432",
    "user": "mabshoff"
}
```

Merged 8313.patch, 8314.patch and 8315.patch in Sage 2.10.2.alpha1



---

archive/issue_comments_014433.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-17T20:59:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2196",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2196#issuecomment-14433",
    "user": "mabshoff"
}
```

Resolution: fixed
