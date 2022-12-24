# Issue 5264: [with patch, needs review] optimize small permgroup elements

archive/issues_005264.json:
```json
{
    "body": "Assignee: joyner\n\nAvoid allocation for very small permutation group elements (which can be a significant cost of element creation). \n\nIssue created by migration from https://trac.sagemath.org/ticket/5264\n\n",
    "created_at": "2009-02-14T06:49:24Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] optimize small permgroup elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5264",
    "user": "robertwb"
}
```
Assignee: joyner

Avoid allocation for very small permutation group elements (which can be a significant cost of element creation). 

Issue created by migration from https://trac.sagemath.org/ticket/5264





---

archive/issue_comments_040415.json:
```json
{
    "body": "Attachment [5264-perm-speed.patch](tarball://root/attachments/some-uuid/ticket5264/5264-perm-speed.patch) by robertwb created at 2009-02-14 06:50:11",
    "created_at": "2009-02-14T06:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5264#issuecomment-40415",
    "user": "robertwb"
}
```

Attachment [5264-perm-speed.patch](tarball://root/attachments/some-uuid/ticket5264/5264-perm-speed.patch) by robertwb created at 2009-02-14 06:50:11



---

archive/issue_comments_040416.json:
```json
{
    "body": "Before: \n\n\n```\nsage: G = SymmetricGroup(3)\nsage: L = [G.random_element() for _ in range(100)] * 17\nsage: timeit(\"prod(L)\")\n625 loops, best of 3: 651 \u00b5s per loop\n\nsage: G = SymmetricGroup(10)\nsage: L = [G.random_element() for _ in range(100)] * 17\nsage: timeit(\"prod(L)\")\n625 loops, best of 3: 766 \u00b5s per loop\n\nsage: G = SymmetricGroup(20)\nsage: L = [G.random_element() for _ in range(100)] * 17\nsage: timeit(\"prod(L)\")\n625 loops, best of 3: 854 \u00b5s per loop\n```\n\n\nAfter: \n\n```\nsage: sage: G = SymmetricGroup(3)\nsage: sage: L = [G.random_element() for _ in range(100)] * 17\nsage: sage: timeit(\"prod(L)\")\n625 loops, best of 3: 485 \u00b5s per loop\n\nsage: sage: G = SymmetricGroup(10)\nsage: sage: L = [G.random_element() for _ in range(100)] * 17\nsage: sage: timeit(\"prod(L)\")\n625 loops, best of 3: 564 \u00b5s per loop\n\nsage: sage: G = SymmetricGroup(20)\nsage: sage: L = [G.random_element() for _ in range(100)] * 17\nsage: sage: timeit(\"prod(L)\")\n625 loops, best of 3: 876 \u00b5s per loop\n```\n",
    "created_at": "2009-02-14T06:58:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5264#issuecomment-40416",
    "user": "robertwb"
}
```

Before: 


```
sage: G = SymmetricGroup(3)
sage: L = [G.random_element() for _ in range(100)] * 17
sage: timeit("prod(L)")
625 loops, best of 3: 651 µs per loop

sage: G = SymmetricGroup(10)
sage: L = [G.random_element() for _ in range(100)] * 17
sage: timeit("prod(L)")
625 loops, best of 3: 766 µs per loop

sage: G = SymmetricGroup(20)
sage: L = [G.random_element() for _ in range(100)] * 17
sage: timeit("prod(L)")
625 loops, best of 3: 854 µs per loop
```


After: 

```
sage: sage: G = SymmetricGroup(3)
sage: sage: L = [G.random_element() for _ in range(100)] * 17
sage: sage: timeit("prod(L)")
625 loops, best of 3: 485 µs per loop

sage: sage: G = SymmetricGroup(10)
sage: sage: L = [G.random_element() for _ in range(100)] * 17
sage: sage: timeit("prod(L)")
625 loops, best of 3: 564 µs per loop

sage: sage: G = SymmetricGroup(20)
sage: sage: L = [G.random_element() for _ in range(100)] * 17
sage: sage: timeit("prod(L)")
625 loops, best of 3: 876 µs per loop
```




---

archive/issue_comments_040417.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T11:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5264#issuecomment-40417",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_040418.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T11:35:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5264",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5264#issuecomment-40418",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
