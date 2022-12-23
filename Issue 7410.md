# Issue 7410: Strings sometimes truncated in notebook mode.

archive/issues_007410.json:
```json
{
    "body": "Assignee: boothby\n\nNoticed that some strings are truncated when viewed by print. Example:\n\n```\nG=graphs.Grid2dGraph(2,9)\nS=G.graph6_string()\nprint S\nprint G.graph6_string()\n```\n\nWe expect this to print the same string two times, but when this code is evaluated in the notebook, this is what is printed:\n\n```\nQhCGGC@_A?c@C@A?__GC@?OC?_G\nQhCGGC@_A?c@C@A?__GC@?OC?\n```\n\nThe former is the correct answer, the latter removes the last two characters for some reason.\n\nThis only happens in the notebook(tested on alpha.sagenb.org for Ubuntu, Debian and Windows XP, with browsers Firefox and IE). When the code above is run in the terminal without a notebook, it works as expected. Running './sage -notebook' also displays the error. This is all tested with Sage 4.2.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7410\n\n",
    "created_at": "2009-11-08T10:41:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Strings sometimes truncated in notebook mode.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7410",
    "user": "AJonsson"
}
```
Assignee: boothby

Noticed that some strings are truncated when viewed by print. Example:

```
G=graphs.Grid2dGraph(2,9)
S=G.graph6_string()
print S
print G.graph6_string()
```

We expect this to print the same string two times, but when this code is evaluated in the notebook, this is what is printed:

```
QhCGGC@_A?c@C@A?__GC@?OC?_G
QhCGGC@_A?c@C@A?__GC@?OC?
```

The former is the correct answer, the latter removes the last two characters for some reason.

This only happens in the notebook(tested on alpha.sagenb.org for Ubuntu, Debian and Windows XP, with browsers Firefox and IE). When the code above is run in the terminal without a notebook, it works as expected. Running './sage -notebook' also displays the error. This is all tested with Sage 4.2.

Issue created by migration from https://trac.sagemath.org/ticket/7410





---

archive/issue_comments_062357.json:
```json
{
    "body": "This may be fixed by #7666.",
    "created_at": "2009-12-14T17:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7410#issuecomment-62357",
    "user": "mpatel"
}
```

This may be fixed by #7666.



---

archive/issue_comments_062358.json:
```json
{
    "body": "Possibly related: #7663.",
    "created_at": "2009-12-14T17:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7410#issuecomment-62358",
    "user": "mpatel"
}
```

Possibly related: #7663.



---

archive/issue_comments_062359.json:
```json
{
    "body": "#7648's patch (alone!) gives the correct answer.  If I'm right, please close this ticket when #7648 and #7663 merge.",
    "created_at": "2010-01-18T04:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7410#issuecomment-62359",
    "user": "mpatel"
}
```

#7648's patch (alone!) gives the correct answer.  If I'm right, please close this ticket when #7648 and #7663 merge.



---

archive/issue_comments_062360.json:
```json
{
    "body": "#7648's patch (alone!?) gives the correct answer.  If I'm right, please close this ticket when #7648 and #7663 merge.",
    "created_at": "2010-01-18T04:33:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7410#issuecomment-62360",
    "user": "mpatel"
}
```

#7648's patch (alone!?) gives the correct answer.  If I'm right, please close this ticket when #7648 and #7663 merge.



---

archive/issue_comments_062361.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7410#issuecomment-62361",
    "user": "timdumol"
}
```

Resolution: duplicate



---

archive/issue_comments_062362.json:
```json
{
    "body": "Works with sagenb-0.6.",
    "created_at": "2010-01-19T03:12:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7410",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7410#issuecomment-62362",
    "user": "timdumol"
}
```

Works with sagenb-0.6.
