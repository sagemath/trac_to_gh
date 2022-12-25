# Issue 1691: [with patch] old bug in pari.gen __setitem__ code

archive/issues_001691.json:
```json
{
    "body": "Assignee: @craigcitro\n\nCC:  craigcitro@gmail.com carl.witty@gmail.com\n\nThere's an old bug in the __setitem__ code for pari gen objects:\n\n```\nx = pari(\"[[1,2],3]\") ; x[0][0] = 500 ; x\n```\n\nwould give you back a list with nonsense where the 500 should go. The issue was a memory management one. In general, whenever a pari GEN is allocated, if we want it to be preserved, there ultimately has to be *some* python object pointing to it somewhere. What would happen in this case is that x[0][0] = 500 became x.__getitem__(0).__setitem__(0,500), and the return value from x.__getitem__(0) would store a pointer to the GEN containing 500. However, after the __setitem__ was finished, the object returned by __getitem__ was deallocated, and thus our GEN no longer had any python object pointing to it, and it was itself deallocated. \n\nSo, ultimately, we need to do a bit more memory management. Here's the fix I implemented (which came out of some conversation with Carl Witty during Bug Day ... 7?), and which is really just a more complete version of something already in place. Namely, pari gens sometimes have a _refers_to dictionary, which in the case of a t_VEC or t_MAT, stores references to the gens pointing to the GENs stored there. I've mostly just beefed up this system. \n\nI added two new fields, _GEN_owner and _owner_set. The idea is this: any time you create a gen that's not the only gen pointing to its GEN, we need to make sure that everyone knows when that GEN gets updated. So when we create a gen that's not the unique one pointing to its GEN, we set its _owner_set to 1, and _GEN_owner to the other gen pointing to its GEN. \n\nSince that reads like something out of \"Who's on First,\" let's give an example: we'll pretend for a moment that _owner_set, _GEN_owner, and _refers_to are def'd instead of cdef'd, and give a mock sage session explaining an example:\n\n```\nsage: x = pari([0,1,2])\nsage: x._owner_set\n0\nsage: x._refers_to\n{0: 0, 1: 1, 2: 2}\nsage: y = pari([3,4])\nsage: y._owner_set \n0\nsage: x[0] = y ; x\n[[3, 4], 1, 2]\nsage: x[0]._owner_set\n1\nsage: x[0] is y\nFalse\nsage: x[0]._GEN_owner is y\nTrue\nsage: x[0][0] = 123 ; x\n[[123, 4], 1, 2]\nsage: y\n[123, 4]\n```\n\nSo this does what we want. There's one somewhat frustrating thing that can happen, though. In the above example, we're allocating each element of the list, so our _refers_to gets set just as we'd like. However, it's possible that not every GEN has a gen pointing to it. That is:\n\n```\nsage: x = pari(\"[[1,2],3,4]\") ; x._refers_to\n{}\n```\n\nThis is annoying for us -- it means that we don't have our reference tracking working with such an object until the user tries to refer to a piece of it. So, when you try to create a new_ref to an object, and it's never been referenced before, we first make and store a reference to it as we would have done at allocation.\n\nWhile I was doing this, I sped up pari coercion a bit here and there ... here's two examples:\n\nBefore:\n\n```\nsage: ls = [2,3]\n\nsage: time for _ in range(100000): x = pari(ls)\nCPU times: user 4.84 s, sys: 1.05 s, total: 5.89 s\nWall time: 6.40\n\nsage: foo = True\n\nsage: time for _ in range(100000): x = pari(foo)\nCPU times: user 1.25 s, sys: 0.01 s, total: 1.26 s\nWall time: 1.35\n```\n\nAfter:\n\n```\nsage: ls = [2,3]\n\nsage: time for _ in range(100000): x = pari(ls)\nCPU times: user 2.56 s, sys: 0.89 s, total: 3.45 s\nWall time: 3.90\n\nsage: foo = True\n\nsage: time for _ in range(100000): x = pari(foo)\nCPU times: user 0.73 s, sys: 0.01 s, total: 0.73 s\nWall time: 0.80\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1691\n\n",
    "created_at": "2008-01-05T08:53:04Z",
    "labels": [
        "component: interfaces",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "[with patch] old bug in pari.gen __setitem__ code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1691",
    "user": "https://github.com/craigcitro"
}
```
Assignee: @craigcitro

CC:  craigcitro@gmail.com carl.witty@gmail.com

There's an old bug in the __setitem__ code for pari gen objects:

```
x = pari("[[1,2],3]") ; x[0][0] = 500 ; x
```

would give you back a list with nonsense where the 500 should go. The issue was a memory management one. In general, whenever a pari GEN is allocated, if we want it to be preserved, there ultimately has to be *some* python object pointing to it somewhere. What would happen in this case is that x[0][0] = 500 became x.__getitem__(0).__setitem__(0,500), and the return value from x.__getitem__(0) would store a pointer to the GEN containing 500. However, after the __setitem__ was finished, the object returned by __getitem__ was deallocated, and thus our GEN no longer had any python object pointing to it, and it was itself deallocated. 

So, ultimately, we need to do a bit more memory management. Here's the fix I implemented (which came out of some conversation with Carl Witty during Bug Day ... 7?), and which is really just a more complete version of something already in place. Namely, pari gens sometimes have a _refers_to dictionary, which in the case of a t_VEC or t_MAT, stores references to the gens pointing to the GENs stored there. I've mostly just beefed up this system. 

I added two new fields, _GEN_owner and _owner_set. The idea is this: any time you create a gen that's not the only gen pointing to its GEN, we need to make sure that everyone knows when that GEN gets updated. So when we create a gen that's not the unique one pointing to its GEN, we set its _owner_set to 1, and _GEN_owner to the other gen pointing to its GEN. 

Since that reads like something out of "Who's on First," let's give an example: we'll pretend for a moment that _owner_set, _GEN_owner, and _refers_to are def'd instead of cdef'd, and give a mock sage session explaining an example:

```
sage: x = pari([0,1,2])
sage: x._owner_set
0
sage: x._refers_to
{0: 0, 1: 1, 2: 2}
sage: y = pari([3,4])
sage: y._owner_set 
0
sage: x[0] = y ; x
[[3, 4], 1, 2]
sage: x[0]._owner_set
1
sage: x[0] is y
False
sage: x[0]._GEN_owner is y
True
sage: x[0][0] = 123 ; x
[[123, 4], 1, 2]
sage: y
[123, 4]
```

So this does what we want. There's one somewhat frustrating thing that can happen, though. In the above example, we're allocating each element of the list, so our _refers_to gets set just as we'd like. However, it's possible that not every GEN has a gen pointing to it. That is:

```
sage: x = pari("[[1,2],3,4]") ; x._refers_to
{}
```

This is annoying for us -- it means that we don't have our reference tracking working with such an object until the user tries to refer to a piece of it. So, when you try to create a new_ref to an object, and it's never been referenced before, we first make and store a reference to it as we would have done at allocation.

While I was doing this, I sped up pari coercion a bit here and there ... here's two examples:

Before:

```
sage: ls = [2,3]

sage: time for _ in range(100000): x = pari(ls)
CPU times: user 4.84 s, sys: 1.05 s, total: 5.89 s
Wall time: 6.40

sage: foo = True

sage: time for _ in range(100000): x = pari(foo)
CPU times: user 1.25 s, sys: 0.01 s, total: 1.26 s
Wall time: 1.35
```

After:

```
sage: ls = [2,3]

sage: time for _ in range(100000): x = pari(ls)
CPU times: user 2.56 s, sys: 0.89 s, total: 3.45 s
Wall time: 3.90

sage: foo = True

sage: time for _ in range(100000): x = pari(foo)
CPU times: user 0.73 s, sys: 0.01 s, total: 0.73 s
Wall time: 0.80
```



Issue created by migration from https://trac.sagemath.org/ticket/1691





---

archive/issue_comments_010713.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-01-05T09:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10713",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_010714.json:
```json
{
    "body": "Attachment [trac_1691.patch](tarball://root/attachments/some-uuid/ticket1691/trac_1691.patch) by @craigcitro created at 2008-01-05 09:00:40",
    "created_at": "2008-01-05T09:00:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10714",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac_1691.patch](tarball://root/attachments/some-uuid/ticket1691/trac_1691.patch) by @craigcitro created at 2008-01-05 09:00:40



---

archive/issue_comments_010715.json:
```json
{
    "body": "I think I understand what this patch is doing.  It seems excessively complicated and possibly broken.\n\n1) Sometimes _GEN_owner refers to another gen with the same value as self; sometimes it refers to another gen (a matrix or vector) such that self is an element of _GEN_owner.  This is quite confusing.\n\nI think the latter case is the only important case; then _GEN_owner should be renamed to _GEN_parent.\n\nIn the former case, instead of creating multiple gen elements with the same value, and setting _GEN_owner, it should just use the original gen.  So:\n\n```\n                    return P.new_ref((<gen>x).g,x)\n```\nwould become\n\n```\n                    return x\n```\n\n2) There need to be more comments describing these fields.\n\n3) (less important): It seems that ._owner_set is true iff ._GEN_owner is not None; I recommend removing this field and just checking ._GEN_owner (or, in the rewritten patch, ._GEN_parent), to save memory at a (probably) negligible cost in time.",
    "created_at": "2008-01-06T05:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10715",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I think I understand what this patch is doing.  It seems excessively complicated and possibly broken.

1) Sometimes _GEN_owner refers to another gen with the same value as self; sometimes it refers to another gen (a matrix or vector) such that self is an element of _GEN_owner.  This is quite confusing.

I think the latter case is the only important case; then _GEN_owner should be renamed to _GEN_parent.

In the former case, instead of creating multiple gen elements with the same value, and setting _GEN_owner, it should just use the original gen.  So:

```
                    return P.new_ref((<gen>x).g,x)
```
would become

```
                    return x
```

2) There need to be more comments describing these fields.

3) (less important): It seems that ._owner_set is true iff ._GEN_owner is not None; I recommend removing this field and just checking ._GEN_owner (or, in the rewritten patch, ._GEN_parent), to save memory at a (probably) negligible cost in time.



---

archive/issue_comments_010716.json:
```json
{
    "body": "I've completely thrown out the old patch and written a new fix for this. I was talking this through with Robert Bradshaw, and he pointed out that since so much of the trouble comes from lots of references to the same GEN, why not get rid of that? That is, we now demand that the following general rule is true: there is at most one sage gen pointing to any given Pari GEN. There are still multiple gens pointing to the parts of a single GEN (i.e. x[0], x[1], etc), but never to the same GEN. This greatly simplifies things, and the code seems to work well. All the timings above are still valid with the new patch.\n\nI also changed forcecopy to gcopy in gen.pyx, and commented out forcecopy in decl.pxi. It turns out that forcecopy is deprecated, and isn't even mentioned in the Pari manual anymore, and gcopy replaces it. In fact, looking at the Pari sources we ship with 2.9.3, forcecopy is declared by #define forcecopy gcopy, so there's no reason to have it around anyway, since it will likely disappear completely from Pari at some point.\n\nI am running a -testall overnight, so I can't guarantee there are no doctest failures, but the rings/ directory and libs/pari/ both doctest clean, which is a good start. I'll fix any doctest failures I find tomorrow.",
    "created_at": "2008-01-14T12:46:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10716",
    "user": "https://github.com/craigcitro"
}
```

I've completely thrown out the old patch and written a new fix for this. I was talking this through with Robert Bradshaw, and he pointed out that since so much of the trouble comes from lots of references to the same GEN, why not get rid of that? That is, we now demand that the following general rule is true: there is at most one sage gen pointing to any given Pari GEN. There are still multiple gens pointing to the parts of a single GEN (i.e. x[0], x[1], etc), but never to the same GEN. This greatly simplifies things, and the code seems to work well. All the timings above are still valid with the new patch.

I also changed forcecopy to gcopy in gen.pyx, and commented out forcecopy in decl.pxi. It turns out that forcecopy is deprecated, and isn't even mentioned in the Pari manual anymore, and gcopy replaces it. In fact, looking at the Pari sources we ship with 2.9.3, forcecopy is declared by #define forcecopy gcopy, so there's no reason to have it around anyway, since it will likely disappear completely from Pari at some point.

I am running a -testall overnight, so I can't guarantee there are no doctest failures, but the rings/ directory and libs/pari/ both doctest clean, which is a good start. I'll fix any doctest failures I find tomorrow.



---

archive/issue_comments_010717.json:
```json
{
    "body": "Attachment [1691v2.patch](tarball://root/attachments/some-uuid/ticket1691/1691v2.patch) by @craigcitro created at 2008-01-14 12:47:46",
    "created_at": "2008-01-14T12:47:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10717",
    "user": "https://github.com/craigcitro"
}
```

Attachment [1691v2.patch](tarball://root/attachments/some-uuid/ticket1691/1691v2.patch) by @craigcitro created at 2008-01-14 12:47:46



---

archive/issue_comments_010718.json:
```json
{
    "body": "Looks good to me!  (patch looks good, testall passes)\n\nApply only 1691v2.patch.",
    "created_at": "2008-01-15T03:14:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10718",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Looks good to me!  (patch looks good, testall passes)

Apply only 1691v2.patch.



---

archive/issue_events_004144.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-01-15T03:19:44Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1691#event-4144"
}
```



---

archive/issue_comments_010719.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T03:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10719",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_010720.json:
```json
{
    "body": "1691v2.patch only merged in Sage 2.10.alpha3",
    "created_at": "2008-01-15T03:19:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1691#issuecomment-10720",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

1691v2.patch only merged in Sage 2.10.alpha3
