# Issue 4241: magma -- memory is never freed in the interface when MagmaElement's are deleted

archive/issues_004241.json:
```json
{
    "body": "Assignee: @williamstein\n\nObserve:\n\n```\nsage: a = magma('10000')\nsage: a.name()\n'_sage_[1]'\nsage: del a\nsage: magma.eval('_sage_[1]')\n'10000'\n```\n\n\nWhenever anybody ever creates a MagmaElement via the Magma interface, it doesn't get deleted.  This is because possible (1) the clear method in magma.py is commented out, and/or (2) the _available_var list that gets appended to in (1) isn't actually used by magma.py, so e.g., _sage_[1] in the example above never gets re-used. \n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4241\n\n",
    "created_at": "2008-10-04T05:01:55Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "magma -- memory is never freed in the interface when MagmaElement's are deleted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4241",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

Observe:

```
sage: a = magma('10000')
sage: a.name()
'_sage_[1]'
sage: del a
sage: magma.eval('_sage_[1]')
'10000'
```


Whenever anybody ever creates a MagmaElement via the Magma interface, it doesn't get deleted.  This is because possible (1) the clear method in magma.py is commented out, and/or (2) the _available_var list that gets appended to in (1) isn't actually used by magma.py, so e.g., _sage_[1] in the example above never gets re-used. 


Issue created by migration from https://trac.sagemath.org/ticket/4241





---

archive/issue_comments_030763.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-04T05:02:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4241#issuecomment-30763",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030764.json:
```json
{
    "body": "Here's a vivid illustration of the memory leakage, which of course we know is there by reading the code:\n\n```\nsage: a = [magma('3^100000') for _ in range(1000)]\nsage: magma.GetMemoryUsage()\n42917912\nsage: del a\nsage: magma.GetMemoryUsage()\n42917912\nsage: a = [magma('3^100000') for _ in range(1000)]\nsage: magma.GetMemoryUsage()\n69103640\nsage: del a\nsage: magma.GetMemoryUsage()\n69103640\n```\n",
    "created_at": "2008-10-23T22:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4241#issuecomment-30764",
    "user": "https://github.com/williamstein"
}
```

Here's a vivid illustration of the memory leakage, which of course we know is there by reading the code:

```
sage: a = [magma('3^100000') for _ in range(1000)]
sage: magma.GetMemoryUsage()
42917912
sage: del a
sage: magma.GetMemoryUsage()
42917912
sage: a = [magma('3^100000') for _ in range(1000)]
sage: magma.GetMemoryUsage()
69103640
sage: del a
sage: magma.GetMemoryUsage()
69103640
```




---

archive/issue_comments_030765.json:
```json
{
    "body": "Without patch:\n\n```\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage() \n42917912\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage() \n94192176\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()\n121287216\n```\n\nWith patch:\n\n```\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()\n40817200\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()\n41820720\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()\n41820720\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()\n41820720\nsage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()\n41820720\n```\n\n}}}",
    "created_at": "2008-10-23T23:26:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4241#issuecomment-30765",
    "user": "https://github.com/williamstein"
}
```

Without patch:

```
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage() 
42917912
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage() 
94192176
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
121287216
```

With patch:

```
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
40817200
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
sage: a = [magma('3^100000') for _ in range(1000)]; del a;magma.GetMemoryUsage()
41820720
```

}}}



---

archive/issue_comments_030766.json:
```json
{
    "body": "Attachment [sage-4241.patch](tarball://root/attachments/some-uuid/ticket4241/sage-4241.patch) by @williamstein created at 2008-10-23 23:33:55",
    "created_at": "2008-10-23T23:33:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4241#issuecomment-30766",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4241.patch](tarball://root/attachments/some-uuid/ticket4241/sage-4241.patch) by @williamstein created at 2008-10-23 23:33:55



---

archive/issue_comments_030767.json:
```json
{
    "body": "Patch looks good to me. There is a spelling error in the new docstring: \"clearlying\" _ i will fix it in the patch I will apply.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T02:53:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4241#issuecomment-30767",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Patch looks good to me. There is a spelling error in the new docstring: "clearlying" _ i will fix it in the patch I will apply.

Cheers,

Michael



---

archive/issue_events_004478.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-27T04:19:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4241#event-4478"
}
```



---

archive/issue_comments_030768.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-27T04:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4241#issuecomment-30768",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha1



---

archive/issue_comments_030769.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-27T04:19:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4241",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4241#issuecomment-30769",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
