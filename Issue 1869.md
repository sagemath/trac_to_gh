# Issue 1869: Implement show(list(graphs(n))) et al

archive/issues_001869.json:
```json
{
    "body": "Assignee: @rlmill\n\n`show` is in `sage/misc/functional.py`. It should be easy to get graphs_list functionality in there, if it applies.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1869\n\n",
    "created_at": "2008-01-20T20:35:34Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.1",
    "title": "Implement show(list(graphs(n))) et al",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1869",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

`show` is in `sage/misc/functional.py`. It should be easy to get graphs_list functionality in there, if it applies.

Issue created by migration from https://trac.sagemath.org/ticket/1869





---

archive/issue_comments_011806.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-20T20:35:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11806",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_011807.json:
```json
{
    "body": "Attachment [show_graphs.patch](tarball://root/attachments/some-uuid/ticket1869/show_graphs.patch) by @rlmill created at 2008-01-23 22:25:12",
    "created_at": "2008-01-23T22:25:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11807",
    "user": "https://github.com/rlmill"
}
```

Attachment [show_graphs.patch](tarball://root/attachments/some-uuid/ticket1869/show_graphs.patch) by @rlmill created at 2008-01-23 22:25:12



---

archive/issue_comments_011808.json:
```json
{
    "body": "Very nice functionality!\n\nThree things:\n\n* Could we pass the width and height of the grid as parameters?  something like {{{\nsage: show(graphs(5),width=3,height=3)\n# Displays 3x3 pages of the graphs\n}}}\n* Why limit this to graphs?  Why not have a list trigger a default rendering as a rectangular array, where each item is drawn with \"show(list[i])\"  Hmmm...then nested lists would even work and display nicely.\n* `show(graphs(1))` gives an image with space for 4 graphs, but only the one result is displayed.  Can we make the image narrower?\n\nI think this patch is a great start.",
    "created_at": "2008-01-23T23:05:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11808",
    "user": "https://github.com/jasongrout"
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

archive/issue_comments_011809.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T00:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11809",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011810.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T00:08:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1869#issuecomment-11810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
