# Issue 1869: Implement show(list(graphs(n))) et al

archive/issues_001869.json:
```json
{
    "body": "Assignee: rlm\n\n`show` is in `sage/misc/functional.py`. It should be easy to get graphs_list functionality in there, if it applies.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1869\n\n",
    "created_at": "2008-01-20T20:35:34Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Implement show(list(graphs(n))) et al",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1869",
    "user": "rlm"
}
```
Assignee: rlm

`show` is in `sage/misc/functional.py`. It should be easy to get graphs_list functionality in there, if it applies.

Issue created by migration from https://trac.sagemath.org/ticket/1869





---

archive/issue_comments_011835.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T20:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11835",
    "user": "rlm"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011836.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-01-23T22:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11836",
    "user": "rlm"
}
```

Attachment



---

archive/issue_comments_011837.json:
```json
{
    "body": "Very nice functionality!\n\nThree things:\n\n* Could we pass the width and height of the grid as parameters?  something like {{{\nsage: show(graphs(5),width=3,height=3)\n# Displays 3x3 pages of the graphs\n}}}\n* Why limit this to graphs?  Why not have a list trigger a default rendering as a rectangular array, where each item is drawn with \"show(list[i])\"  Hmmm...then nested lists would even work and display nicely.\n* `show(graphs(1))` gives an image with space for 4 graphs, but only the one result is displayed.  Can we make the image narrower?\n\nI think this patch is a great start.",
    "created_at": "2008-01-23T23:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11837",
    "user": "jason"
}
```

Very nice functionality!

Three things:

* Could we pass the width and height of the grid as parameters?  something like {{{
sage: show(graphs(5),width=3,height=3)
# Displays 3x3 pages of the graphs
}}}
* Why limit this to graphs?  Why not have a list trigger a default rendering as a rectangular array, where each item is drawn with "show(list[i])"  Hmmm...then nested lists would even work and display nicely.
* `show(graphs(1))` gives an image with space for 4 graphs, but only the one result is displayed.  Can we make the image narrower?

I think this patch is a great start.



---

archive/issue_comments_011838.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T00:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11838",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011839.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T00:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11839",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
