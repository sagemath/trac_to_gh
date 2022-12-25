# Issue 6285: Wrong description of arcsin function

archive/issues_006285.json:
```json
{
    "body": "Description for \"arcsin\" wrongly says it is \"The inverse of the hyperbolic sine function\" !!\n\n```\narcsin?\n\nFile:        /home/golam/foo/sage-4.0.1/local/lib/python2.5/site-packages/sage/functions/trig.py\nType:        <class 'sage.functions.trig.Function_arcsin'>\nDefinition:  arcsin(x, hold='False')\nDocstring: \n\n        The inverse of the hyperbolic sine function.\n\n        EXAMPLES::\n\n            sage: arcsinh(0.5)\n            0.481211825059603\n            sage: arcsinh(1/2)\n            arcsinh(1/2)\n            sage: arcsinh(1 + 1.0*I)\n\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6285\n\n",
    "created_at": "2009-06-14T11:43:56Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "Wrong description of arcsin function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6285",
    "user": "https://github.com/golam-m-hossain"
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

archive/issue_comments_050089.json:
```json
{
    "body": "Changing keywords from \"\" to \"arcsin, wrong description\".",
    "created_at": "2009-06-14T12:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50089",
    "user": "https://github.com/golam-m-hossain"
}
```

Changing keywords from "" to "arcsin, wrong description".



---

archive/issue_comments_050090.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-14T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50090",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050091.json:
```json
{
    "body": "I fixed these as a part of #6244. This bug can be closed once #6244 is merged.",
    "created_at": "2009-06-14T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50091",
    "user": "https://github.com/burcin"
}
```

I fixed these as a part of #6244. This bug can be closed once #6244 is merged.



---

archive/issue_comments_050092.json:
```json
{
    "body": "Set assignee to @burcin.",
    "created_at": "2009-06-14T13:02:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50092",
    "user": "https://github.com/burcin"
}
```

Set assignee to @burcin.



---

archive/issue_events_014696.json:
```json
{
    "actor": "https://github.com/burcin",
    "created_at": "2009-06-14T13:02:20Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "milestone": "sage-4.0.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6285#event-14696"
}
```



---

archive/issue_events_014697.json:
```json
{
    "actor": "https://github.com/ncalexan",
    "created_at": "2009-06-14T22:20:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6285#event-14697"
}
```



---

archive/issue_comments_050093.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-14T22:20:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6285",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6285#issuecomment-50093",
    "user": "https://github.com/ncalexan"
}
```

Resolution: fixed
