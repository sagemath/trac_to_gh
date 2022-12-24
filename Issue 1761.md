# Issue 1761: Graphviz output for graphs

archive/issues_001761.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @ncalexan\n\nAdd functionality to use graphviz for graph display.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1761\n\n",
    "created_at": "2008-01-12T04:16:39Z",
    "labels": [
        "graph theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Graphviz output for graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1761",
    "user": "boothby"
}
```
Assignee: @rlmill

CC:  @ncalexan

Add functionality to use graphviz for graph display.

Issue created by migration from https://trac.sagemath.org/ticket/1761





---

archive/issue_comments_011111.json:
```json
{
    "body": "Attachment [graphviz.hg](tarball://root/attachments/some-uuid/ticket1761/graphviz.hg) by @mwhansen created at 2008-01-13 13:31:51",
    "created_at": "2008-01-13T13:31:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11111",
    "user": "@mwhansen"
}
```

Attachment [graphviz.hg](tarball://root/attachments/some-uuid/ticket1761/graphviz.hg) by @mwhansen created at 2008-01-13 13:31:51



---

archive/issue_comments_011112.json:
```json
{
    "body": "This is useful and should be applied.  I would have liked to see the actual function abstracted to a Graph class higher in the hierarchy, if there is one, because it seems like the actual code is the same, just the edge identifier symbols for dot are different.  Also, is '# not tested' the correct tag for doctests to not get run?",
    "created_at": "2008-01-22T07:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11112",
    "user": "@ncalexan"
}
```

This is useful and should be applied.  I would have liked to see the actual function abstracted to a Graph class higher in the hierarchy, if there is one, because it seems like the actual code is the same, just the edge identifier symbols for dot are different.  Also, is '# not tested' the correct tag for doctests to not get run?



---

archive/issue_comments_011113.json:
```json
{
    "body": "I agree with ncalexan:\n\n1. The string functions should be abstracted to the GenericGraph class with the string changing depending on whether the graph is directed or not.  In general, we are trying to consolidate functionality to the GenericGraph class when possible these days.\n\n2. The graphviz function documentation should clearly state that graphviz (and in particular, dot) needs to be installed in the system path.  It would be nice were the option to run the other graphviz programs, like neato, etc.",
    "created_at": "2008-02-16T11:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11113",
    "user": "@jasongrout"
}
```

I agree with ncalexan:

1. The string functions should be abstracted to the GenericGraph class with the string changing depending on whether the graph is directed or not.  In general, we are trying to consolidate functionality to the GenericGraph class when possible these days.

2. The graphviz function documentation should clearly state that graphviz (and in particular, dot) needs to be installed in the system path.  It would be nice were the option to run the other graphviz programs, like neato, etc.



---

archive/issue_comments_011114.json:
```json
{
    "body": "Changing keywords from \"\" to \"graph visualization dot graphviz\".",
    "created_at": "2008-04-06T19:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11114",
    "user": "@ncalexan"
}
```

Changing keywords from "" to "graph visualization dot graphviz".



---

archive/issue_comments_011115.json:
```json
{
    "body": "The attached patch addresses the referee's comments.\n\nIt also removes references to the actual graphviz/dot application.  I don't see how this can be made cross-platform and I'm worried about licensing issues, so I'm just ducking the issue.  Open a new ticket if you'd like this functionality.",
    "created_at": "2008-04-06T19:36:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11115",
    "user": "@ncalexan"
}
```

The attached patch addresses the referee's comments.

It also removes references to the actual graphviz/dot application.  I don't see how this can be made cross-platform and I'm worried about licensing issues, so I'm just ducking the issue.  Open a new ticket if you'd like this functionality.



---

archive/issue_comments_011116.json:
```json
{
    "body": "Attachment [1761-ncalexan-graphviz-1.patch](tarball://root/attachments/some-uuid/ticket1761/1761-ncalexan-graphviz-1.patch) by @ncalexan created at 2008-04-06 19:37:11\n\nThe original bundle is not needed; apply only the patch.",
    "created_at": "2008-04-06T19:37:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11116",
    "user": "@ncalexan"
}
```

Attachment [1761-ncalexan-graphviz-1.patch](tarball://root/attachments/some-uuid/ticket1761/1761-ncalexan-graphviz-1.patch) by @ncalexan created at 2008-04-06 19:37:11

The original bundle is not needed; apply only the patch.



---

archive/issue_comments_011117.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-06T20:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11117",
    "user": "boothby"
}
```

Looks good to me.



---

archive/issue_comments_011118.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-08T15:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11118",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_011119.json:
```json
{
    "body": "Merged in Sage 3.0.alpha3",
    "created_at": "2008-04-08T15:28:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11119",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha3



---

archive/issue_comments_011120.json:
```json
{
    "body": "doctest fix due to bitrot",
    "created_at": "2008-04-08T16:58:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11120",
    "user": "mabshoff"
}
```

doctest fix due to bitrot



---

archive/issue_comments_011121.json:
```json
{
    "body": "Attachment [trac_1761-tmp-file-dir-fix.patch](tarball://root/attachments/some-uuid/ticket1761/trac_1761-tmp-file-dir-fix.patch) by mabshoff created at 2008-04-08 17:50:53\n\ncreate doctest files in SAGE_TESTDIR",
    "created_at": "2008-04-08T17:50:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1761",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1761#issuecomment-11121",
    "user": "mabshoff"
}
```

Attachment [trac_1761-tmp-file-dir-fix.patch](tarball://root/attachments/some-uuid/ticket1761/trac_1761-tmp-file-dir-fix.patch) by mabshoff created at 2008-04-08 17:50:53

create doctest files in SAGE_TESTDIR
