# Issue 6286: Inconsistence typesettings of PrimitiveFunctions

archive/issues_006286.json:
```json
{
    "body": "In sage-4.0.1, most of the primitive functions suffer from\ninconsistence typsettings. For example:\n\n\n```\nf = arcsin\nlatex( f ); latex( f(x) ); latex( f(x,1) )\n\n\\sin^{-1}\n\\arcsin\\left(x\\right)\n\\mbox{\\sin^{-1}}\\left(x\\right)\n```\n\n\nNote that the same function is being typeset differently. The additional \"\\mbox\" in third case (which has been reported in\n#6268) will get resolved by #5711. \n\nHowever, second case seems weird to me, given \"class Function_arcsin\" (sage.functions.trig) clearly defines its \nlatex expression to be \"\\sin^{-1}\". So it seems to be a pynac issue.\n\nOne can try following to see the issues for other functions\n\n\n```\n# Trigonometric functions\nlst = [sin, cos, tan, cot, sec, csc, arcsin, arccos, arctan, arccot, arcsec, arccsc]  \n\n# view\nfor fn in lst:\n    view( fn ); view( fn(x) ); view( fn(x,1) )\n    \n# latex\nfor fn in lst:\n    latex( fn ); latex( fn(x) ); latex( fn(x,1) )\n```\n\n \nand\n\n\n```\n# Hyperbolic functions\nlst = [sinh, cosh, tanh, coth, sech, csch, arcsinh, arccosh, arctanh, arccoth, arcsech, arccsch ] \n\n# view\nfor fn in lst:\n    view( fn ); view( fn(x) ); view( fn(x,1) )\n    \n# latex\nfor fn in lst:\n    latex( fn ); latex( fn(x) ); latex( fn(x,1) )\n```\n\n\nIt seems, out of these 24 functions, 18 functions suffer from inconsistence typesetting.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6286\n\n",
    "created_at": "2009-06-14T14:29:47Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Inconsistence typesettings of PrimitiveFunctions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6286",
    "user": "gmhossain"
}
```
In sage-4.0.1, most of the primitive functions suffer from
inconsistence typsettings. For example:


```
f = arcsin
latex( f ); latex( f(x) ); latex( f(x,1) )

\sin^{-1}
\arcsin\left(x\right)
\mbox{\sin^{-1}}\left(x\right)
```


Note that the same function is being typeset differently. The additional "\mbox" in third case (which has been reported in
#6268) will get resolved by #5711. 

However, second case seems weird to me, given "class Function_arcsin" (sage.functions.trig) clearly defines its 
latex expression to be "\sin^{-1}". So it seems to be a pynac issue.

One can try following to see the issues for other functions


```
# Trigonometric functions
lst = [sin, cos, tan, cot, sec, csc, arcsin, arccos, arctan, arccot, arcsec, arccsc]  

# view
for fn in lst:
    view( fn ); view( fn(x) ); view( fn(x,1) )
    
# latex
for fn in lst:
    latex( fn ); latex( fn(x) ); latex( fn(x,1) )
```

 
and


```
# Hyperbolic functions
lst = [sinh, cosh, tanh, coth, sech, csch, arcsinh, arccosh, arctanh, arccoth, arcsech, arccsch ] 

# view
for fn in lst:
    view( fn ); view( fn(x) ); view( fn(x,1) )
    
# latex
for fn in lst:
    latex( fn ); latex( fn(x) ); latex( fn(x,1) )
```


It seems, out of these 24 functions, 18 functions suffer from inconsistence typesetting.

Issue created by migration from https://trac.sagemath.org/ticket/6286





---

archive/issue_comments_050190.json:
```json
{
    "body": "I am working on this at the moment, as a part of the changes for #6211. Thanks for providing this comprehensive test data.\n\nI am not sure about using `sin^{-1}` as the latex form of `arcsin` though.",
    "created_at": "2009-06-14T15:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6286#issuecomment-50190",
    "user": "burcin"
}
```

I am working on this at the moment, as a part of the changes for #6211. Thanks for providing this comprehensive test data.

I am not sure about using `sin^{-1}` as the latex form of `arcsin` though.



---

archive/issue_comments_050191.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-14T15:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6286#issuecomment-50191",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050192.json:
```json
{
    "body": "Set assignee to burcin.",
    "created_at": "2009-06-14T15:47:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6286#issuecomment-50192",
    "user": "burcin"
}
```

Set assignee to burcin.



---

archive/issue_comments_050193.json:
```json
{
    "body": "The patch at #7490 fixes this. It also includes doctests to check latex typesetting of each of these functions.",
    "created_at": "2009-11-21T11:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6286#issuecomment-50193",
    "user": "burcin"
}
```

The patch at #7490 fixes this. It also includes doctests to check latex typesetting of each of these functions.



---

archive/issue_comments_050194.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-21T11:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6286#issuecomment-50194",
    "user": "burcin"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050195.json:
```json
{
    "body": "Fixed by #7490",
    "created_at": "2009-12-04T06:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6286#issuecomment-50195",
    "user": "mhansen"
}
```

Fixed by #7490



---

archive/issue_comments_050196.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-04T06:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6286",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6286#issuecomment-50196",
    "user": "mhansen"
}
```

Resolution: fixed
