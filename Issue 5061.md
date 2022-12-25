# Issue 5061: Steenrod algebras report additive order of 0 is p

archive/issues_005061.json:
```json
{
    "body": "Assignee: tbd\n\nThis is wrong:\n\n\n```\nsage: S2 = SteenrodAlgebra(2)\nsage: z = S2(0)\nsage: z.additive_order()\n2\n```\n\n\nlooking at the code, it's easy to see why this happens...\n\n\n```\n    def additive_order(self):\n        \"\"\"\n        The additive order of any element of the mod p Steenrod algebra is p.\n\n        OUTPUT:\n            order -- positive prime number\n\n        EXAMPLES:\n            sage: z = Sq(4) + Sq(6) + Sq(0)\n            sage: z.additive_order()\n            2\n        \"\"\"\n        return self._prime\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5061\n\n",
    "created_at": "2009-01-23T00:28:53Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "Steenrod algebras report additive order of 0 is p",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5061",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```
Assignee: tbd

This is wrong:


```
sage: S2 = SteenrodAlgebra(2)
sage: z = S2(0)
sage: z.additive_order()
2
```


looking at the code, it's easy to see why this happens...


```
    def additive_order(self):
        """
        The additive order of any element of the mod p Steenrod algebra is p.

        OUTPUT:
            order -- positive prime number

        EXAMPLES:
            sage: z = Sq(4) + Sq(6) + Sq(0)
            sage: z.additive_order()
            2
        """
        return self._prime
```



Issue created by migration from https://trac.sagemath.org/ticket/5061





---

archive/issue_comments_038480.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38480",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_038481.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38481",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_038482.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38482",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038483.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38483",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_038484.json:
```json
{
    "body": "Changing component from commutative algebra to algebra.",
    "created_at": "2009-01-23T02:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38484",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Changing component from commutative algebra to algebra.



---

archive/issue_comments_038485.json:
```json
{
    "body": "Attachment [5061-steenrod-ao.patch](tarball://root/attachments/some-uuid/ticket5061/5061-steenrod-ao.patch) by boothby created at 2009-01-23 09:45:33",
    "created_at": "2009-01-23T09:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38485",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Attachment [5061-steenrod-ao.patch](tarball://root/attachments/some-uuid/ticket5061/5061-steenrod-ao.patch) by boothby created at 2009-01-23 09:45:33



---

archive/issue_comments_038486.json:
```json
{
    "body": "Looks good. The documentation should probably be fixed as well though, and you need a doctest.",
    "created_at": "2009-01-23T22:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38486",
    "user": "https://github.com/robertwb"
}
```

Looks good. The documentation should probably be fixed as well though, and you need a doctest.



---

archive/issue_comments_038487.json:
```json
{
    "body": "Attachment [5061-doc.patch](tarball://root/attachments/some-uuid/ticket5061/5061-doc.patch) by @jhpalmieri created at 2009-02-26 18:49:30\n\napply on top of other patch",
    "created_at": "2009-02-26T18:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38487",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [5061-doc.patch](tarball://root/attachments/some-uuid/ticket5061/5061-doc.patch) by @jhpalmieri created at 2009-02-26 18:49:30

apply on top of other patch



---

archive/issue_comments_038488.json:
```json
{
    "body": "Here's a documentation/doctest patch to go on top of the other one.",
    "created_at": "2009-02-26T18:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38488",
    "user": "https://github.com/jhpalmieri"
}
```

Here's a documentation/doctest patch to go on top of the other one.



---

archive/issue_comments_038489.json:
```json
{
    "body": "I'm happy with it.",
    "created_at": "2009-02-26T20:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38489",
    "user": "https://github.com/robertwb"
}
```

I'm happy with it.



---

archive/issue_comments_038490.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T17:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38490",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038491.json:
```json
{
    "body": "Merged both patches in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T17:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38491",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_events_005307.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-02-28T17:08:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5061#event-5307"
}
```
