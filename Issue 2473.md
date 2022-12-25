# Issue 2473: [with patch, needs review] BipartiteGraph.__init__ does not properly initialize for some inputs

archive/issues_002473.json:
```json
{
    "body": "Assignee: @rlmill\n\nBipartiteGraph.__init__ does not call the base class __init__ for some inputs, leaving the object unusable.  For example, \n\n```\nsage: B = BipartiteGraph(None)\nsage: B\n```\n\nwill throw an exception because the base class attributes have not been initialized.  The attached patch ensures the base class __init__ is called.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2473\n\n",
    "created_at": "2008-03-11T22:03:53Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10.4",
    "title": "[with patch, needs review] BipartiteGraph.__init__ does not properly initialize for some inputs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2473",
    "user": "https://github.com/rhinton"
}
```
Assignee: @rlmill

BipartiteGraph.__init__ does not call the base class __init__ for some inputs, leaving the object unusable.  For example, 

```
sage: B = BipartiteGraph(None)
sage: B
```

will throw an exception because the base class attributes have not been initialized.  The attached patch ensures the base class __init__ is called.

Issue created by migration from https://trac.sagemath.org/ticket/2473





---

archive/issue_comments_016709.json:
```json
{
    "body": "The problem with this approach is it allows one to construct graphs which are not bipartite, but they will be instances of BipartiteGraph. What should be done instead is to raise a NotImplementedError, so that the user knows that the initialization failed. This problem is a small part of the much bigger task in ticket #1941, which is one of the next things I'll be doing. Watch for a patch in the next few days, perhaps...",
    "created_at": "2008-03-12T00:23:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16709",
    "user": "https://github.com/rlmill"
}
```

The problem with this approach is it allows one to construct graphs which are not bipartite, but they will be instances of BipartiteGraph. What should be done instead is to raise a NotImplementedError, so that the user knows that the initialization failed. This problem is a small part of the much bigger task in ticket #1941, which is one of the next things I'll be doing. Watch for a patch in the next few days, perhaps...



---

archive/issue_comments_016710.json:
```json
{
    "body": "Attachment [bipartite_graph_input.patch](tarball://root/attachments/some-uuid/ticket2473/bipartite_graph_input.patch) by @rhinton created at 2008-03-12 18:57:52\n\ntry #2",
    "created_at": "2008-03-12T18:57:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16710",
    "user": "https://github.com/rhinton"
}
```

Attachment [bipartite_graph_input.patch](tarball://root/attachments/some-uuid/ticket2473/bipartite_graph_input.patch) by @rhinton created at 2008-03-12 18:57:52

try #2



---

archive/issue_comments_016711.json:
```json
{
    "body": "Attachment [bipartite_graph_input.2.patch](tarball://root/attachments/some-uuid/ticket2473/bipartite_graph_input.2.patch) by @rhinton created at 2008-03-12 18:59:27\n\nThe updated patch, I believe, addresses your concerns.  It also fixes several more bugs.",
    "created_at": "2008-03-12T18:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16711",
    "user": "https://github.com/rhinton"
}
```

Attachment [bipartite_graph_input.2.patch](tarball://root/attachments/some-uuid/ticket2473/bipartite_graph_input.2.patch) by @rhinton created at 2008-03-12 18:59:27

The updated patch, I believe, addresses your concerns.  It also fixes several more bugs.



---

archive/issue_comments_016712.json:
```json
{
    "body": "Is patch 2 supposed to replace patch 1?",
    "created_at": "2008-03-12T19:40:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16712",
    "user": "https://github.com/rlmill"
}
```

Is patch 2 supposed to replace patch 1?



---

archive/issue_comments_016713.json:
```json
{
    "body": "Some notes:\n\n1. \"TESTS\" should actually be labeled \"EXAMPLE\" or \"EXAMPLES\". This is just the convention.\n\n2. Comments in the examples don't need \"#\"; see many other doctests for examples of the formatting.\n\n3. I've moved the networkx import further down so it only happens if it needs to. This import, if it hasn't been done before, takes several seconds... (I know this doesn't seem to make much sense now, but soon we won't be importing networkx by default whenever we have a graph, so it will make sense eventually.)",
    "created_at": "2008-03-13T02:23:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16713",
    "user": "https://github.com/rlmill"
}
```

Some notes:

1. "TESTS" should actually be labeled "EXAMPLE" or "EXAMPLES". This is just the convention.

2. Comments in the examples don't need "#"; see many other doctests for examples of the formatting.

3. I've moved the networkx import further down so it only happens if it needs to. This import, if it hasn't been done before, takes several seconds... (I know this doesn't seem to make much sense now, but soon we won't be importing networkx by default whenever we have a graph, so it will make sense eventually.)



---

archive/issue_comments_016714.json:
```json
{
    "body": "Attachment [2473-ref.patch](tarball://root/attachments/some-uuid/ticket2473/2473-ref.patch) by @rlmill created at 2008-03-13 02:24:50\n\nApply bipartite_graph_input.2.patch, then this.",
    "created_at": "2008-03-13T02:24:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16714",
    "user": "https://github.com/rlmill"
}
```

Attachment [2473-ref.patch](tarball://root/attachments/some-uuid/ticket2473/2473-ref.patch) by @rlmill created at 2008-03-13 02:24:50

Apply bipartite_graph_input.2.patch, then this.



---

archive/issue_comments_016715.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-13T12:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_016716.json:
```json
{
    "body": "Merged in Sage 2.10.4.alpha0",
    "created_at": "2008-03-13T12:45:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2473",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2473#issuecomment-16716",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.10.4.alpha0
