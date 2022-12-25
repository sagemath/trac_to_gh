# Issue 4607: double backslash not properly handled in latex mode

archive/issues_004607.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  p.a.rombouts@home.nl\n\nfrom [public bug collection](http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA):\n\nNormally a double backslash '\\\\' forces a new line in LaTeX. However, when I type the following in a notebook input cell:\n\n```\n%latex\nFirst line.\\\\\nSecond line.\n```\n\nthe output looks like this:\n\n```\n      First line.line.\n```\n\n\n----\n\nAfter a little fiddling, I discovered this effect can be achieved using three backslashes instead of two, but this is not correct behavior.\nI first discovered this problem when I tried to render something like this in a sage notebook:\n\n```\n%latex\n\\[\\theta(x)=\\begin{cases}\n0 & (x<0) \\\\\n1 & (x\\ge 0)\n\\end{cases}\\]\n```\n\nThe '1' is missing in the rendered output. The desired output can be obtained by using triple backslashes, but as I noted before, the is not correct behavior.\n\n----\n\nprobably just needs proper escaping.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4607\n\n",
    "created_at": "2008-11-25T00:05:55Z",
    "labels": [
        "component: notebook",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "double backslash not properly handled in latex mode",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4607",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: boothby

CC:  p.a.rombouts@home.nl

from [public bug collection](http://spreadsheets.google.com/pub?key=pCwvGVwSMxTzT6E2xNdo5fA):

Normally a double backslash '\\' forces a new line in LaTeX. However, when I type the following in a notebook input cell:

```
%latex
First line.\\
Second line.
```

the output looks like this:

```
      First line.line.
```


----

After a little fiddling, I discovered this effect can be achieved using three backslashes instead of two, but this is not correct behavior.
I first discovered this problem when I tried to render something like this in a sage notebook:

```
%latex
\[\theta(x)=\begin{cases}
0 & (x<0) \\
1 & (x\ge 0)
\end{cases}\]
```

The '1' is missing in the rendered output. The desired output can be obtained by using triple backslashes, but as I noted before, the is not correct behavior.

----

probably just needs proper escaping.


Issue created by migration from https://trac.sagemath.org/ticket/4607





---

archive/issue_comments_034520.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-01-20T10:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4607#issuecomment-34520",
    "user": "https://github.com/mwhansen"
}
```

Resolution: duplicate



---

archive/issue_events_010474.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-20T10:23:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4607",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4607#event-10474"
}
```



---

archive/issue_events_010475.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-01-20T10:23:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4607",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4607#event-10475"
}
```



---

archive/issue_comments_034521.json:
```json
{
    "body": "This is a duplicate of #3201.  I'll try to have the fix here in the next few days.",
    "created_at": "2009-01-20T10:23:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4607",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4607#issuecomment-34521",
    "user": "https://github.com/mwhansen"
}
```

This is a duplicate of #3201.  I'll try to have the fix here in the next few days.
