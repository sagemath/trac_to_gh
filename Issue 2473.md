# Issue 2473: [with patch, needs review] BipartiteGraph.__init__ does not properly initialize for some inputs

archive/issues_002473.json:
```json
{
    "body": "Assignee: rlm\n\nBipartiteGraph.__init__ does not call the base class __init__ for some inputs, leaving the object unusable.  For example, \n\n```\nsage: B = BipartiteGraph(None)\nsage: B\n```\n\nwill throw an exception because the base class attributes have not been initialized.  The attached patch ensures the base class __init__ is called.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2473\n\n",
    "created_at": "2008-03-11T22:03:53Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] BipartiteGraph.__init__ does not properly initialize for some inputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2473",
    "user": "rhinton"
}
```
Assignee: rlm

BipartiteGraph.__init__ does not call the base class __init__ for some inputs, leaving the object unusable.  For example, 

```
sage: B = BipartiteGraph(None)
sage: B
```

will throw an exception because the base class attributes have not been initialized.  The attached patch ensures the base class __init__ is called.

Issue created by migration from https://trac.sagemath.org/ticket/2473





---

archive/issue_comments_016745.json:
```json
{
    "body": "The problem with this approach is it allows one to construct graphs which are not bipartite, but they will be instances of BipartiteGraph. What should be done instead is to raise a NotImplementedError, so that the user knows that the initialization failed. This problem is a small part of the much bigger task in ticket #1941, which is one of the next things I'll be doing. Watch for a patch in the next few days, perhaps...",
    "created_at": "2008-03-12T00:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16745",
    "user": "rlm"
}
```

The problem with this approach is it allows one to construct graphs which are not bipartite, but they will be instances of BipartiteGraph. What should be done instead is to raise a NotImplementedError, so that the user knows that the initialization failed. This problem is a small part of the much bigger task in ticket #1941, which is one of the next things I'll be doing. Watch for a patch in the next few days, perhaps...



---

archive/issue_comments_016746.json:
```json
{
    "body": "Attachment\n\ntry #2",
    "created_at": "2008-03-12T18:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16746",
    "user": "rhinton"
}
```

Attachment

try #2



---

archive/issue_comments_016747.json:
```json
{
    "body": "Attachment\n\nThe updated patch, I believe, addresses your concerns.  It also fixes several more bugs.",
    "created_at": "2008-03-12T18:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16747",
    "user": "rhinton"
}
```

Attachment

The updated patch, I believe, addresses your concerns.  It also fixes several more bugs.



---

archive/issue_comments_016748.json:
```json
{
    "body": "Is patch 2 supposed to replace patch 1?",
    "created_at": "2008-03-12T19:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16748",
    "user": "rlm"
}
```

Is patch 2 supposed to replace patch 1?



---

archive/issue_comments_016749.json:
```json
{
    "body": "Some notes:\n\n1. \"TESTS\" should actually be labeled \"EXAMPLE\" or \"EXAMPLES\". This is just the convention.\n\n2. Comments in the examples don't need \"#\"; see many other doctests for examples of the formatting.\n\n3. I've moved the networkx import further down so it only happens if it needs to. This import, if it hasn't been done before, takes several seconds... (I know this doesn't seem to make much sense now, but soon we won't be importing networkx by default whenever we have a graph, so it will make sense eventually.)",
    "created_at": "2008-03-13T02:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16749",
    "user": "rlm"
}
```

Some notes:

1. "TESTS" should actually be labeled "EXAMPLE" or "EXAMPLES". This is just the convention.

2. Comments in the examples don't need "#"; see many other doctests for examples of the formatting.

3. I've moved the networkx import further down so it only happens if it needs to. This import, if it hasn't been done before, takes several seconds... (I know this doesn't seem to make much sense now, but soon we won't be importing networkx by default whenever we have a graph, so it will make sense eventually.)



---

archive/issue_comments_016750.json:
```json
{
    "body": "Attachment\n\nApply bipartite_graph_input.2.patch, then this.",
    "created_at": "2008-03-13T02:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16750",
    "user": "rlm"
}
```

Attachment

Apply bipartite_graph_input.2.patch, then this.



---

archive/issue_comments_016751.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-13T12:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16751",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016752.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-13T12:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16752",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
