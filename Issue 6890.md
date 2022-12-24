# Issue 6890: No help for is_SymbolicVariable ?

archive/issues_006890.json:
```json
{
    "body": "Assignee: tba\n\nKeywords: partial, help, doc\n\nHelp for is_SymbolicVariable and is_SymbolicExpressionRing is nonexistent, for Python reasons, apparently:\n\n```\nsage: is_SymbolicExpressionRing??\nError getting source: could not find class definition\nType: partial\n...\npartial(func, *args, **keywords) - new function with partial application of the given arguments and keywords.\n```\n\nNotice that these functions do have useful docstrings, they just aren't showing up.  This was originally reported in #2562.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6890\n\n",
    "created_at": "2009-09-04T18:55:24Z",
    "labels": [
        "documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "No help for is_SymbolicVariable ?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6890",
    "user": "@kcrisman"
}
```
Assignee: tba

Keywords: partial, help, doc

Help for is_SymbolicVariable and is_SymbolicExpressionRing is nonexistent, for Python reasons, apparently:

```
sage: is_SymbolicExpressionRing??
Error getting source: could not find class definition
Type: partial
...
partial(func, *args, **keywords) - new function with partial application of the given arguments and keywords.
```

Notice that these functions do have useful docstrings, they just aren't showing up.  This was originally reported in #2562.

Issue created by migration from https://trac.sagemath.org/ticket/6890





---

archive/issue_comments_056935.json:
```json
{
    "body": "This works fine now after an explicit import:\n\n\n```\nsage: is_SymbolicExpressionRing??\nType:       builtin_function_or_method\nString Form:<built-in function is_SymbolicExpressionRing>\nDefinition: is_SymbolicExpressionRing(R)\nSource:\ndef is_SymbolicExpressionRing(R):\n    \"\"\"\n    Returns True if *R* is the symbolic expression ring.\n\n    EXAMPLES::\n\n        sage: from sage.symbolic.ring import is_SymbolicExpressionRing\n        sage: is_SymbolicExpressionRing(ZZ)\n        False\n        sage: is_SymbolicExpressionRing(SR)\n        True\n    \"\"\"\n    return R is SR\n```\n",
    "created_at": "2013-07-23T15:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6890#issuecomment-56935",
    "user": "@mwhansen"
}
```

This works fine now after an explicit import:


```
sage: is_SymbolicExpressionRing??
Type:       builtin_function_or_method
String Form:<built-in function is_SymbolicExpressionRing>
Definition: is_SymbolicExpressionRing(R)
Source:
def is_SymbolicExpressionRing(R):
    """
    Returns True if *R* is the symbolic expression ring.

    EXAMPLES::

        sage: from sage.symbolic.ring import is_SymbolicExpressionRing
        sage: is_SymbolicExpressionRing(ZZ)
        False
        sage: is_SymbolicExpressionRing(SR)
        True
    """
    return R is SR
```




---

archive/issue_comments_056936.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-07-23T15:31:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6890",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6890#issuecomment-56936",
    "user": "@mwhansen"
}
```

Resolution: invalid
