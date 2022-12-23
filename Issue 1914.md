# Issue 1914: incorrect string escaping in preparser

archive/issues_001914.json:
```json
{
    "body": "Assignee: was\n\nThis works in python:\n\n```\n>>> print \"abc \\\"def\\\"\"\nabc \"def\"\n```\n\n\nbut it's broken in sage:\n\n```\nsage: print \"abc \\\"def\\\"\"\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     print \"abc \\\"def._backslash_()\"\"\n                                    ^\n<type 'exceptions.SyntaxError'>: EOL while scanning single-quoted string\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1914\n\n",
    "created_at": "2008-01-24T16:55:08Z",
    "labels": [
        "user interface",
        "major",
        "bug"
    ],
    "title": "incorrect string escaping in preparser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1914",
    "user": "dmharvey"
}
```
Assignee: was

This works in python:

```
>>> print "abc \"def\""
abc "def"
```


but it's broken in sage:

```
sage: print "abc \"def\""
------------------------------------------------------------
   File "<ipython console>", line 1
     print "abc \"def._backslash_()""
                                    ^
<type 'exceptions.SyntaxError'>: EOL while scanning single-quoted string
```



Issue created by migration from https://trac.sagemath.org/ticket/1914





---

archive/issue_comments_012127.json:
```json
{
    "body": "This might be related to #1781.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-24T20:37:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1914#issuecomment-12127",
    "user": "mabshoff"
}
```

This might be related to #1781.

Cheers,

Michael



---

archive/issue_comments_012128.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-24T09:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1914#issuecomment-12128",
    "user": "burcin"
}
```

Resolution: fixed



---

archive/issue_comments_012129.json:
```json
{
    "body": "This works for me on 3.0.2-rc2. There is also the following doctest in sage/misc/preparser.py around line 40 to cover this:\n\n\n```\nA string with escaped quotes in it (the point here is that the\npreparser doesn't get confused by the internal quotes):\n    sage: \"\\\"Yes,\\\" he said.\"\n    '\"Yes,\" he said.'\n    sage: s = \"\\\\\"; s\n    '\\\\'\n```\n\n\nI think this bug can safely be resolved as worksforme.",
    "created_at": "2008-05-24T09:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1914",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1914#issuecomment-12129",
    "user": "burcin"
}
```

This works for me on 3.0.2-rc2. There is also the following doctest in sage/misc/preparser.py around line 40 to cover this:


```
A string with escaped quotes in it (the point here is that the
preparser doesn't get confused by the internal quotes):
    sage: "\"Yes,\" he said."
    '"Yes," he said.'
    sage: s = "\\"; s
    '\\'
```


I think this bug can safely be resolved as worksforme.
