# Issue 4368: Create a function which gets an attributed from an object and calls it with specified arguments and keywords

archive/issues_004368.json:
```json
{
    "body": "Assignee: cwitty\n\nExample:\n\n\n```\nsage: f = attrcall('r_core', 3); f\n*.r_core(3)\nsage: [f(p) for p in Partitions(5)]\n[[2], [1, 1], [1, 1], [3, 1, 1], [2], [2], [1, 1]]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4368\n\n",
    "created_at": "2008-10-25T21:33:46Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "title": "Create a function which gets an attributed from an object and calls it with specified arguments and keywords",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4368",
    "user": "mhansen"
}
```
Assignee: cwitty

Example:


```
sage: f = attrcall('r_core', 3); f
*.r_core(3)
sage: [f(p) for p in Partitions(5)]
[[2], [1, 1], [1, 1], [3, 1, 1], [2], [2], [1, 1]]
```



Issue created by migration from https://trac.sagemath.org/ticket/4368





---

archive/issue_comments_032096.json:
```json
{
    "body": "Changing assignee from cwitty to mhansen.",
    "created_at": "2008-10-25T21:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32096",
    "user": "mhansen"
}
```

Changing assignee from cwitty to mhansen.



---

archive/issue_comments_032097.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-25T21:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32097",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032098.json:
```json
{
    "body": "Reply to [comment:2 mhansen]\n\n\n\nThe following snippet is from the attached patch **trac_4368.patch**:\n\n```\n+def attrcall(name, *args, **kwds):\n+    \"\"\"\n+    Returns a callable which takes in an object, gets the method\n+    named name from that objects, and calls it with the specified\n+    arguments and keywords.\n```\n\nWhy \"named name from that _objects_\"? (my emphasis) My understanding is that I can pass in an object (not more than one) to the proposed class `AttrCallObject`. If you mean that I can pass in only one object in order to get a returned callable, then you might want to consider the following documentation change:\n\n```\n-named name from that objects, and calls it with the specified\n+named name from that object, and calls it with the specified\n```\n",
    "created_at": "2008-10-26T11:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32098",
    "user": "mvngu"
}
```

Reply to [comment:2 mhansen]



The following snippet is from the attached patch **trac_4368.patch**:

```
+def attrcall(name, *args, **kwds):
+    """
+    Returns a callable which takes in an object, gets the method
+    named name from that objects, and calls it with the specified
+    arguments and keywords.
```

Why "named name from that _objects_"? (my emphasis) My understanding is that I can pass in an object (not more than one) to the proposed class `AttrCallObject`. If you mean that I can pass in only one object in order to get a returned callable, then you might want to consider the following documentation change:

```
-named name from that objects, and calls it with the specified
+named name from that object, and calls it with the specified
```




---

archive/issue_comments_032099.json:
```json
{
    "body": "Any reason you're not using functools http://www.python.org/doc/2.5.2/lib/module-functools.html ?",
    "created_at": "2008-10-30T21:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32099",
    "user": "robertwb"
}
```

Any reason you're not using functools http://www.python.org/doc/2.5.2/lib/module-functools.html ?



---

archive/issue_comments_032100.json:
```json
{
    "body": "OK, looking into this more, I see that functools won't help much (as the callable isn't specified ahead of time). It looks good and works well. \n\nPositive review, pending the (presumably just a typo) fix from mvngu above. BTW, I like the \"*.foo(x)\" string representation.",
    "created_at": "2008-10-30T22:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32100",
    "user": "robertwb"
}
```

OK, looking into this more, I see that functools won't help much (as the callable isn't specified ahead of time). It looks good and works well. 

Positive review, pending the (presumably just a typo) fix from mvngu above. BTW, I like the "*.foo(x)" string representation.



---

archive/issue_comments_032101.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-30T22:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32101",
    "user": "mhansen"
}
```

Attachment



---

archive/issue_comments_032102.json:
```json
{
    "body": "I've updated the patch to fix the typo.",
    "created_at": "2008-10-30T22:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32102",
    "user": "mhansen"
}
```

I've updated the patch to fix the typo.



---

archive/issue_comments_032103.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T00:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32103",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032104.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T00:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32104",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2
