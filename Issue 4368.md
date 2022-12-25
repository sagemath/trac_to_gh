# Issue 4368: Create a function which gets an attributed from an object and calls it with specified arguments and keywords

archive/issues_004368.json:
```json
{
    "body": "Assignee: cwitty\n\nExample:\n\n\n```\nsage: f = attrcall('r_core', 3); f\n*.r_core(3)\nsage: [f(p) for p in Partitions(5)]\n[[2], [1, 1], [1, 1], [3, 1, 1], [2], [2], [1, 1]]\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4368\n\n",
    "created_at": "2008-10-25T21:33:46Z",
    "labels": [
        "component: misc",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Create a function which gets an attributed from an object and calls it with specified arguments and keywords",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4368",
    "user": "https://github.com/mwhansen"
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

archive/issue_comments_032033.json:
```json
{
    "body": "Changing assignee from cwitty to @mwhansen.",
    "created_at": "2008-10-25T21:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32033",
    "user": "https://github.com/mwhansen"
}
```

Changing assignee from cwitty to @mwhansen.



---

archive/issue_comments_032034.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-25T21:34:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32034",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032035.json:
```json
{
    "body": "Reply to [comment:2 mhansen]\n\n\n\nThe following snippet is from the attached patch **trac_4368.patch**:\n\n```\n+def attrcall(name, *args, **kwds):\n+    \"\"\"\n+    Returns a callable which takes in an object, gets the method\n+    named name from that objects, and calls it with the specified\n+    arguments and keywords.\n```\n\nWhy \"named name from that _objects_\"? (my emphasis) My understanding is that I can pass in an object (not more than one) to the proposed class `AttrCallObject`. If you mean that I can pass in only one object in order to get a returned callable, then you might want to consider the following documentation change:\n\n```\n-named name from that objects, and calls it with the specified\n+named name from that object, and calls it with the specified\n```\n",
    "created_at": "2008-10-26T11:17:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32035",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
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

archive/issue_comments_032036.json:
```json
{
    "body": "Any reason you're not using functools http://www.python.org/doc/2.5.2/lib/module-functools.html ?",
    "created_at": "2008-10-30T21:44:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32036",
    "user": "https://github.com/robertwb"
}
```

Any reason you're not using functools http://www.python.org/doc/2.5.2/lib/module-functools.html ?



---

archive/issue_comments_032037.json:
```json
{
    "body": "OK, looking into this more, I see that functools won't help much (as the callable isn't specified ahead of time). It looks good and works well. \n\nPositive review, pending the (presumably just a typo) fix from mvngu above. BTW, I like the \"*.foo(x)\" string representation.",
    "created_at": "2008-10-30T22:24:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32037",
    "user": "https://github.com/robertwb"
}
```

OK, looking into this more, I see that functools won't help much (as the callable isn't specified ahead of time). It looks good and works well. 

Positive review, pending the (presumably just a typo) fix from mvngu above. BTW, I like the "*.foo(x)" string representation.



---

archive/issue_comments_032038.json:
```json
{
    "body": "Attachment [trac_4368.patch](tarball://root/attachments/some-uuid/ticket4368/trac_4368.patch) by @mwhansen created at 2008-10-30 22:32:43",
    "created_at": "2008-10-30T22:32:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32038",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_4368.patch](tarball://root/attachments/some-uuid/ticket4368/trac_4368.patch) by @mwhansen created at 2008-10-30 22:32:43



---

archive/issue_comments_032039.json:
```json
{
    "body": "I've updated the patch to fix the typo.",
    "created_at": "2008-10-30T22:33:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32039",
    "user": "https://github.com/mwhansen"
}
```

I've updated the patch to fix the typo.



---

archive/issue_comments_032040.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-31T00:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32040",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032041.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-31T00:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4368#issuecomment-32041",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha2



---

archive/issue_events_009879.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T00:24:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4368#event-9879"
}
```



---

archive/issue_events_009880.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-31T00:24:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4368",
    "milestone": "sage-3.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4368#event-9880"
}
```
