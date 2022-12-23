# Issue 6285: Wrong description of arcsin function

archive/issues_006285.json:
```json
{
    "body": "Description for \"arcsin\" wrongly says it is \"The inverse of the hyperbolic sine function\" !!\n\n\n```\narcsin?\n\nFile:        /home/golam/foo/sage-4.0.1/local/lib/python2.5/site-packages/sage/functions/trig.py\nType:        <class 'sage.functions.trig.Function_arcsin'>\nDefinition:  arcsin(x, hold='False')\nDocstring: \n\n        The inverse of the hyperbolic sine function.\n\n        EXAMPLES::\n\n            sage: arcsinh(0.5)\n            0.481211825059603\n            sage: arcsinh(1/2)\n            arcsinh(1/2)\n            sage: arcsinh(1 + 1.0*I)\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6285\n\n",
    "created_at": "2009-06-14T11:43:56Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "Wrong description of arcsin function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6285",
    "user": "gmhossain"
}
```
Description for "arcsin" wrongly says it is "The inverse of the hyperbolic sine function" !!


```
arcsin?

File:        /home/golam/foo/sage-4.0.1/local/lib/python2.5/site-packages/sage/functions/trig.py
Type:        <class 'sage.functions.trig.Function_arcsin'>
Definition:  arcsin(x, hold='False')
Docstring: 

        The inverse of the hyperbolic sine function.

        EXAMPLES::

            sage: arcsinh(0.5)
            0.481211825059603
            sage: arcsinh(1/2)
            arcsinh(1/2)
            sage: arcsinh(1 + 1.0*I)

```


Issue created by migration from https://trac.sagemath.org/ticket/6285





---

archive/issue_comments_050185.json:
```json
{
    "body": "Changing keywords from \"\" to \"arcsin, wrong description\".",
    "created_at": "2009-06-14T12:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50185",
    "user": "gmhossain"
}
```

Changing keywords from "" to "arcsin, wrong description".



---

archive/issue_comments_050186.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-14T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50186",
    "user": "burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050187.json:
```json
{
    "body": "I fixed these as a part of #6244. This bug can be closed once #6244 is merged.",
    "created_at": "2009-06-14T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50187",
    "user": "burcin"
}
```

I fixed these as a part of #6244. This bug can be closed once #6244 is merged.



---

archive/issue_comments_050188.json:
```json
{
    "body": "Set assignee to burcin.",
    "created_at": "2009-06-14T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50188",
    "user": "burcin"
}
```

Set assignee to burcin.



---

archive/issue_comments_050189.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50189",
    "user": "ncalexan"
}
```

Resolution: fixed
