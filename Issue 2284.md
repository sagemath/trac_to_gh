# Issue 2284: CallableSymbolicExpression._latex_() has some odd behavior

archive/issues_002284.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: f(x,y,z) = 2*x + 3*z^3 - sin(y)\nsage: f._latex_()\n'\\\\left((x, y, z) \\\\right)\\\\ {\\\\mapsto}\\\\ {3 {z}^{3} } - \\\\sin \\\\left( y\n\\\\right) + {2 x}'\n```\n\n(note the extra parens on the left of the arrow)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2284\n\n",
    "created_at": "2008-02-24T00:01:19Z",
    "labels": [
        "calculus",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.3",
    "title": "CallableSymbolicExpression._latex_() has some odd behavior",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2284",
    "user": "moretti"
}
```
Assignee: was


```
sage: f(x,y,z) = 2*x + 3*z^3 - sin(y)
sage: f._latex_()
'\\left((x, y, z) \\right)\\ {\\mapsto}\\ {3 {z}^{3} } - \\sin \\left( y
\\right) + {2 x}'
```

(note the extra parens on the left of the arrow)

Issue created by migration from https://trac.sagemath.org/ticket/2284





---

archive/issue_comments_015154.json:
```json
{
    "body": "Also note that _latex_() does not TeX the variable names on the left:\n\n``` \t\nsage: f(omega) = omega\nsage: f._latex_()\n'omega \\\\ {\\\\mapsto}\\\\ {2 \\\\omega}'\n```\n\n\n'omega' should be '\\\\omega'.",
    "created_at": "2008-02-24T00:07:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2284#issuecomment-15154",
    "user": "moretti"
}
```

Also note that _latex_() does not TeX the variable names on the left:

``` 	
sage: f(omega) = omega
sage: f._latex_()
'omega \\ {\\mapsto}\\ {2 \\omega}'
```


'omega' should be '\\omega'.



---

archive/issue_comments_015155.json:
```json
{
    "body": "latex fix",
    "created_at": "2008-02-24T00:35:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2284#issuecomment-15155",
    "user": "moretti"
}
```

latex fix



---

archive/issue_comments_015156.json:
```json
{
    "body": "Attachment [latex.hg](tarball://root/attachments/some-uuid/ticket2284/latex.hg) by moretti created at 2008-02-24 00:36:40\n\nOkay, submitted a fix; need a review.",
    "created_at": "2008-02-24T00:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2284#issuecomment-15156",
    "user": "moretti"
}
```

Attachment [latex.hg](tarball://root/attachments/some-uuid/ticket2284/latex.hg) by moretti created at 2008-02-24 00:36:40

Okay, submitted a fix; need a review.



---

archive/issue_comments_015157.json:
```json
{
    "body": "Applies cleanly to 2.10.3.alpha0 and passes tests for me.",
    "created_at": "2008-02-27T23:06:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2284#issuecomment-15157",
    "user": "mhansen"
}
```

Applies cleanly to 2.10.3.alpha0 and passes tests for me.



---

archive/issue_comments_015158.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-28T06:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2284#issuecomment-15158",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015159.json:
```json
{
    "body": "Merged in Sage 2.10.3.rc0",
    "created_at": "2008-02-28T06:50:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2284#issuecomment-15159",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.3.rc0
