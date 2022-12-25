# Issue 4380: Memory Leak in libsingular

archive/issues_004380.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: memory leak libsingular\n\nAt http://groups.google.com/group/sage-support/browse_thread/thread/b997f95c1e2503e0/5db5f9e7d4c8faf2 was discussion about a memory leak. I found a reasonably short bit of code that triggers the leak.\n\nIn `test.pyx`:\n\n```\nfrom sage.all import copy\n\ndef Test(I):\n    R=I.ring()\n    p=R.random_element()\n    J0=list(I.reduced_basis())\n    while(1):\n        J = copy(J0)\n        for i in range(100):\n            q=p.reduce(J)\n            J.append(q)\n```\n\n\nApparently the memory consumption should not grow, since `J` returns to its original state after finishing the `for` loop. However, the following `Sage` session is leaking (i.e., the memory consumption grows rapidly, and after a few seconds 1GB are filled up):\n\n```\nsage: attach test.pyx\nCompiling /home/king/Projekte/f5/test.pyx...\nsage: from sage.rings.ideal import Cyclic\nsage: R=PolynomialRing(QQ,'x',5)\nsage: I=Cyclic(R).homogenize()\nsage: Test(I)\n```\n\n\nThe `while` loop comprises\n1. copying of a Sequence (`J0`) of `MPolynomial_libsingular`\n2. reduction of `MPolynomial_libsingular`\n3. appending to a Sequence.\n\nIn one of these three steps must be the leak. I suspect it is the reduction and will try to verify it.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4380\n\n",
    "created_at": "2008-10-29T09:27:48Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Memory Leak in libsingular",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4380",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @malb

Keywords: memory leak libsingular

At http://groups.google.com/group/sage-support/browse_thread/thread/b997f95c1e2503e0/5db5f9e7d4c8faf2 was discussion about a memory leak. I found a reasonably short bit of code that triggers the leak.

In `test.pyx`:

```
from sage.all import copy

def Test(I):
    R=I.ring()
    p=R.random_element()
    J0=list(I.reduced_basis())
    while(1):
        J = copy(J0)
        for i in range(100):
            q=p.reduce(J)
            J.append(q)
```


Apparently the memory consumption should not grow, since `J` returns to its original state after finishing the `for` loop. However, the following `Sage` session is leaking (i.e., the memory consumption grows rapidly, and after a few seconds 1GB are filled up):

```
sage: attach test.pyx
Compiling /home/king/Projekte/f5/test.pyx...
sage: from sage.rings.ideal import Cyclic
sage: R=PolynomialRing(QQ,'x',5)
sage: I=Cyclic(R).homogenize()
sage: Test(I)
```


The `while` loop comprises
1. copying of a Sequence (`J0`) of `MPolynomial_libsingular`
2. reduction of `MPolynomial_libsingular`
3. appending to a Sequence.

In one of these three steps must be the leak. I suspect it is the reduction and will try to verify it.


Issue created by migration from https://trac.sagemath.org/ticket/4380





---

archive/issue_comments_032158.json:
```json
{
    "body": "Sorry, it is not copying a *Sequence* but a *list*. But that shouldn't matter.",
    "created_at": "2008-10-29T09:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32158",
    "user": "https://github.com/simon-king-jena"
}
```

Sorry, it is not copying a *Sequence* but a *list*. But that shouldn't matter.



---

archive/issue_comments_032159.json:
```json
{
    "body": "... and the line `J.append(q)` (that would occur, e.g., in a Groebner basis computation) is not needed either. Replacing `Test(I)` by the following code triggers the leak as well:\n\n\n```\ndef Test(I):\n    R=I.ring()\n    p=R.random_element()\n    J=list(I.reduced_basis())\n    while(1):\n        q=p.reduce(J)\n```\n",
    "created_at": "2008-10-29T10:33:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32159",
    "user": "https://github.com/simon-king-jena"
}
```

... and the line `J.append(q)` (that would occur, e.g., in a Groebner basis computation) is not needed either. Replacing `Test(I)` by the following code triggers the leak as well:


```
def Test(I):
    R=I.ring()
    p=R.random_element()
    J=list(I.reduced_basis())
    while(1):
        q=p.reduce(J)
```




---

archive/issue_comments_032160.json:
```json
{
    "body": "The patch `libsingularLeak.patch` partially solves the problem.\n\nI observed that when a coercion error occurs an intermediately generated ideal `_I` is explicitly destroyed with `id_Delete(&_I,r)`. But when there is no error and the result is returned, then `_I` is not deleted. But I think it should.\n\nWith the patch, the above `Test(I)` still shows an increase of memory, but a rather moderate increase. So, it seems to be a partial solution of the problem, but more needs to be done.",
    "created_at": "2008-10-29T11:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32160",
    "user": "https://github.com/simon-king-jena"
}
```

The patch `libsingularLeak.patch` partially solves the problem.

I observed that when a coercion error occurs an intermediately generated ideal `_I` is explicitly destroyed with `id_Delete(&_I,r)`. But when there is no error and the result is returned, then `_I` is not deleted. But I think it should.

With the patch, the above `Test(I)` still shows an increase of memory, but a rather moderate increase. So, it seems to be a partial solution of the problem, but more needs to be done.



---

archive/issue_comments_032161.json:
```json
{
    "body": "Simon,\n\nnice work. If you find any more issues please open a new ticket, so that this patch can be merged. I will review this patch shortly.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-29T11:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32161",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Simon,

nice work. If you find any more issues please open a new ticket, so that this patch can be merged. I will review this patch shortly.

Cheers,

Michael



---

archive/issue_comments_032162.json:
```json
{
    "body": "Attachment [libsingularLeak.patch](tarball://root/attachments/some-uuid/ticket4380/libsingularLeak.patch) by @simon-king-jena created at 2008-10-29 12:15:20\n\nFixing the leak, after a suggestion of malb",
    "created_at": "2008-10-29T12:15:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32162",
    "user": "https://github.com/simon-king-jena"
}
```

Attachment [libsingularLeak.patch](tarball://root/attachments/some-uuid/ticket4380/libsingularLeak.patch) by @simon-king-jena created at 2008-10-29 12:15:20

Fixing the leak, after a suggestion of malb



---

archive/issue_comments_032163.json:
```json
{
    "body": "Since the announced review of Michael didn't come yet, I hope it is ok that I changed the patch according to a suggestion of malb, without opening a new ticket. \n\nThe new patch seems to fix it completely.",
    "created_at": "2008-10-29T12:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32163",
    "user": "https://github.com/simon-king-jena"
}
```

Since the announced review of Michael didn't come yet, I hope it is ok that I changed the patch according to a suggestion of malb, without opening a new ticket. 

The new patch seems to fix it completely.



---

archive/issue_comments_032164.json:
```json
{
    "body": "Replying to [comment:5 SimonKing]:\n> Since the announced review of Michael didn't come yet, I hope it is ok that I changed the patch according to a suggestion of malb, without opening a new ticket. \n\nYep, I am testing that patch now.\n\n> The new patch seems to fix it completely.\n\n:)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-29T12:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32164",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:5 SimonKing]:
> Since the announced review of Michael didn't come yet, I hope it is ok that I changed the patch according to a suggestion of malb, without opening a new ticket. 

Yep, I am testing that patch now.

> The new patch seems to fix it completely.

:)

Cheers,

Michael



---

archive/issue_comments_032165.json:
```json
{
    "body": "This patch also seems to fix the problem with sr.py consuming vast amounts of memory, but I will do some independent testing first.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-29T12:22:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32165",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch also seems to fix the problem with sr.py consuming vast amounts of memory, but I will do some independent testing first.

Cheers,

Michael



---

archive/issue_comments_032166.json:
```json
{
    "body": "Replying to [comment:7 mabshoff]:\n> This patch also seems to fix the problem with sr.py consuming vast amounts of memory, but I will do some independent testing first.\n\nUnfortunately it doesn't fix the segfault (see #3758), but the amount of memory allocated goes down significantly already.\n\n> Cheers,\n> \n> Michael\n\nCheers,\n\nMichael",
    "created_at": "2008-10-29T12:47:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32166",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:7 mabshoff]:
> This patch also seems to fix the problem with sr.py consuming vast amounts of memory, but I will do some independent testing first.

Unfortunately it doesn't fix the segfault (see #3758), but the amount of memory allocated goes down significantly already.

> Cheers,
> 
> Michael

Cheers,

Michael



---

archive/issue_comments_032167.json:
```json
{
    "body": "Valgrinds clean, passes doctests, positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-29T12:55:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32167",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Valgrinds clean, passes doctests, positive review.

Cheers,

Michael



---

archive/issue_comments_032168.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-29T12:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32168",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004625.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-29T12:56:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4380#event-4625"
}
```



---

archive/issue_comments_032169.json:
```json
{
    "body": "Merged in Sage 3.2alpha2",
    "created_at": "2008-10-29T12:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4380",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4380#issuecomment-32169",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2alpha2
