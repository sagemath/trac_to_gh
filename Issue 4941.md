# Issue 4941: pari list slicing is extremely slow -- make it much faster

archive/issues_004941.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe following illustrates that list slicing in Pari is ridiculously slow.\n\n\n```\nsage: time p=pari.prime_list(10^6)\nCPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s\nWall time: 0.09 s\nsage: len(p)\n1000000\nsage: time c=p[0:]\nCPU times: user 45.05 s, sys: 0.54 s, total: 45.59 s\nWall time: 46.20 s\n```\n\n\nThe code responsible for this is in pari/gen.pyx (line 825 in sage-3.2.3) in __getitem__:\n\n```\n        elif PyObject_TypeCheck(n, slice):\n            l = glength(self.g)\n            inds = _normalize_slice(n, l)\n            k = len(inds)\n            v = P.vector(k)\n            for i in range(k):\n                v[i] = self[inds[i]]\n            return v\n```\n\n\nThere must be dramatically faster ways to do a list slice in pari than the above.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4941\n\n",
    "created_at": "2009-01-05T17:10:35Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "pari list slicing is extremely slow -- make it much faster",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4941",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The following illustrates that list slicing in Pari is ridiculously slow.


```
sage: time p=pari.prime_list(10^6)
CPU times: user 0.06 s, sys: 0.02 s, total: 0.08 s
Wall time: 0.09 s
sage: len(p)
1000000
sage: time c=p[0:]
CPU times: user 45.05 s, sys: 0.54 s, total: 45.59 s
Wall time: 46.20 s
```


The code responsible for this is in pari/gen.pyx (line 825 in sage-3.2.3) in __getitem__:

```
        elif PyObject_TypeCheck(n, slice):
            l = glength(self.g)
            inds = _normalize_slice(n, l)
            k = len(inds)
            v = P.vector(k)
            for i in range(k):
                v[i] = self[inds[i]]
            return v
```


There must be dramatically faster ways to do a list slice in pari than the above.



Issue created by migration from https://trac.sagemath.org/ticket/4941





---

archive/issue_comments_037424.json:
```json
{
    "body": "in GP I would do something like\n\n```\nu=start-step; v=vector(k,unused,p[u+=step])\n```\n\n\nbut I don't know how to translate this...\n\notherwise for big blocks,\n\n```\np.vecextract('\"150..10000\"')\n```\n\nmight be faster",
    "created_at": "2009-01-19T20:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37424",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

in GP I would do something like

```
u=start-step; v=vector(k,unused,p[u+=step])
```


but I don't know how to translate this...

otherwise for big blocks,

```
p.vecextract('"150..10000"')
```

might be faster



---

archive/issue_comments_037425.json:
```json
{
    "body": "This patch solves only the easy part of the problem, for slices of type [::1] or [::-1], still better than nothing.",
    "created_at": "2009-01-20T18:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37425",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

This patch solves only the easy part of the problem, for slices of type [::1] or [::-1], still better than nothing.



---

archive/issue_comments_037426.json:
```json
{
    "body": "oh, and it needs to be applied after patching #4974",
    "created_at": "2009-01-20T18:47:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37426",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

oh, and it needs to be applied after patching #4974



---

archive/issue_comments_037427.json:
```json
{
    "body": "I removed my broken patch",
    "created_at": "2009-01-20T20:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37427",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

I removed my broken patch



---

archive/issue_comments_037428.json:
```json
{
    "body": "corrected patch, sorry for the spam...\n\nit uses vecextract when possible.\n\nall tests pass",
    "created_at": "2009-01-21T08:50:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37428",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

corrected patch, sorry for the spam...

it uses vecextract when possible.

all tests pass



---

archive/issue_comments_037429.json:
```json
{
    "body": "Attachment [trac-4941.patch](tarball://root/attachments/some-uuid/ticket4941/trac-4941.patch) by ylchapuy created at 2009-01-21 12:54:33\n\nfor polynomials, slicing for generic polynomials returns a polynomial, whereas with pari it returns a vector. I think we should change this behavior.",
    "created_at": "2009-01-21T12:54:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37429",
    "user": "https://trac.sagemath.org/admin/accounts/users/ylchapuy"
}
```

Attachment [trac-4941.patch](tarball://root/attachments/some-uuid/ticket4941/trac-4941.patch) by ylchapuy created at 2009-01-21 12:54:33

for polynomials, slicing for generic polynomials returns a polynomial, whereas with pari it returns a vector. I think we should change this behavior.



---

archive/issue_comments_037430.json:
```json
{
    "body": "Looks good to me. If we want to change the behavior, then I would make that a seperate ticket.",
    "created_at": "2009-10-05T18:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37430",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me. If we want to change the behavior, then I would make that a seperate ticket.



---

archive/issue_comments_037431.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T05:25:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4941#issuecomment-37431",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_005183.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T05:25:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4941",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4941#event-5183"
}
```
