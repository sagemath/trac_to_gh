# Issue 5061: Steenrod algebras report additive order of 0 is p

archive/issues_005061.json:
```json
{
    "body": "Assignee: tbd\n\nThis is wrong:\n\n\n```\nsage: S2 = SteenrodAlgebra(2)\nsage: z = S2(0)\nsage: z.additive_order()\n2\n```\n\n\nlooking at the code, it's easy to see why this happens...\n\n\n```\n    def additive_order(self):\n        \"\"\"\n        The additive order of any element of the mod p Steenrod algebra is p.\n\n        OUTPUT:\n            order -- positive prime number\n\n        EXAMPLES:\n            sage: z = Sq(4) + Sq(6) + Sq(0)\n            sage: z.additive_order()\n            2\n        \"\"\"\n        return self._prime\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5061\n\n",
    "created_at": "2009-01-23T00:28:53Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Steenrod algebras report additive order of 0 is p",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5061",
    "user": "boothby"
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

archive/issue_comments_038553.json:
```json
{
    "body": "Changing assignee from tbd to boothby.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38553",
    "user": "boothby"
}
```

Changing assignee from tbd to boothby.



---

archive/issue_comments_038554.json:
```json
{
    "body": "Changing priority from major to trivial.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38554",
    "user": "boothby"
}
```

Changing priority from major to trivial.



---

archive/issue_comments_038555.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38555",
    "user": "boothby"
}
```

Changing status from new to assigned.



---

archive/issue_comments_038556.json:
```json
{
    "body": "Changing component from algebra to commutative algebra.",
    "created_at": "2009-01-23T01:43:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38556",
    "user": "boothby"
}
```

Changing component from algebra to commutative algebra.



---

archive/issue_comments_038557.json:
```json
{
    "body": "Changing component from commutative algebra to algebra.",
    "created_at": "2009-01-23T02:18:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38557",
    "user": "boothby"
}
```

Changing component from commutative algebra to algebra.



---

archive/issue_comments_038558.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-23T09:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38558",
    "user": "boothby"
}
```

Attachment



---

archive/issue_comments_038559.json:
```json
{
    "body": "Looks good. The documentation should probably be fixed as well though, and you need a doctest.",
    "created_at": "2009-01-23T22:16:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38559",
    "user": "robertwb"
}
```

Looks good. The documentation should probably be fixed as well though, and you need a doctest.



---

archive/issue_comments_038560.json:
```json
{
    "body": "Attachment\n\napply on top of other patch",
    "created_at": "2009-02-26T18:49:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38560",
    "user": "jhpalmieri"
}
```

Attachment

apply on top of other patch



---

archive/issue_comments_038561.json:
```json
{
    "body": "Here's a documentation/doctest patch to go on top of the other one.",
    "created_at": "2009-02-26T18:50:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38561",
    "user": "jhpalmieri"
}
```

Here's a documentation/doctest patch to go on top of the other one.



---

archive/issue_comments_038562.json:
```json
{
    "body": "I'm happy with it.",
    "created_at": "2009-02-26T20:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38562",
    "user": "robertwb"
}
```

I'm happy with it.



---

archive/issue_comments_038563.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T17:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38563",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_038564.json:
```json
{
    "body": "Merged both patches in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T17:08:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5061",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5061#issuecomment-38564",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.4.rc0.

Cheers,

Michael
