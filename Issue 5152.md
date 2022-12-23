# Issue 5152: order of abelian group element is a rational number, but should be an integer

archive/issues_005152.json:
```json
{
    "body": "Assignee: somebody\n\nThe line commented with \"error here???\" below is frightening:\n\n```\nFile: /sage/groups/abelian_gps/abelian_group_element.py\nSource Code (starting at line 268):\n    def order(self):\n        \"\"\"\n        Returns the (finite) order of this element or Infinity if this element\n        does not have finite order.\n \n        EXAMPLES:\n            sage: F = AbelianGroup(3,[7,8,9]); F\n            Multiplicative Abelian Group isomorphic to C7 x C8 x C9\n            sage: F.gens()[2].order()\n            9\n            sage: a,b,c = F.gens()\n            sage: (b*c).order()\n            72\n        \"\"\"\n        M = self.parent()\n        if self == M(1):\n            return Integer(1)\n        invs = M.invariants()\n        if self in M.gens():\n            o = invs[list(M.gens()).index(self)]\n            if o == 0:\n                return infinity\n            return o\n        L = list(self.list())\n        N = LCM([invs[i]/GCD(invs[i],L[i]) for i in range(len(invs)) if L[i]!=0])   ####### error here????\n        if N == 0:\n            return infinity\n        else:\n            return N\n```\n\n\n\nBut what bugs me about it is:\n\n```\nsage: G = AbelianGroup(3,[7,8,9])\nsage: type((G.0 * G.1).order())\n<type 'sage.rings.rational.Rational'>\n```\n\n\na simple coercion to Integer at the end of the function would fix this, or using // instead of /.   And add a doctest that has a type check so this doesn't get re-introduced. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5152\n\n",
    "created_at": "2009-02-01T22:02:43Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "title": "order of abelian group element is a rational number, but should be an integer",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5152",
    "user": "was"
}
```
Assignee: somebody

The line commented with "error here???" below is frightening:

```
File: /sage/groups/abelian_gps/abelian_group_element.py
Source Code (starting at line 268):
    def order(self):
        """
        Returns the (finite) order of this element or Infinity if this element
        does not have finite order.
 
        EXAMPLES:
            sage: F = AbelianGroup(3,[7,8,9]); F
            Multiplicative Abelian Group isomorphic to C7 x C8 x C9
            sage: F.gens()[2].order()
            9
            sage: a,b,c = F.gens()
            sage: (b*c).order()
            72
        """
        M = self.parent()
        if self == M(1):
            return Integer(1)
        invs = M.invariants()
        if self in M.gens():
            o = invs[list(M.gens()).index(self)]
            if o == 0:
                return infinity
            return o
        L = list(self.list())
        N = LCM([invs[i]/GCD(invs[i],L[i]) for i in range(len(invs)) if L[i]!=0])   ####### error here????
        if N == 0:
            return infinity
        else:
            return N
```



But what bugs me about it is:

```
sage: G = AbelianGroup(3,[7,8,9])
sage: type((G.0 * G.1).order())
<type 'sage.rings.rational.Rational'>
```


a simple coercion to Integer at the end of the function would fix this, or using // instead of /.   And add a doctest that has a type check so this doesn't get re-introduced. 



Issue created by migration from https://trac.sagemath.org/ticket/5152





---

archive/issue_comments_039419.json:
```json
{
    "body": "to be applied to 3.3.alpha3",
    "created_at": "2009-02-01T23:09:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5152#issuecomment-39419",
    "user": "wdj"
}
```

to be applied to 3.3.alpha3



---

archive/issue_comments_039420.json:
```json
{
    "body": "Attachment\n\nPlease *ignore* trac-5152-abelian-gp-order.2.patch (2.8 kB). I don't know how that got there; hg_sage.export was not working the way I expected.",
    "created_at": "2009-02-01T23:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5152#issuecomment-39420",
    "user": "wdj"
}
```

Attachment

Please *ignore* trac-5152-abelian-gp-order.2.patch (2.8 kB). I don't know how that got there; hg_sage.export was not working the way I expected.



---

archive/issue_comments_039421.json:
```json
{
    "body": "The patch trac-5152-abelian-gp-order.patch (1.6 kB) does exactly as instructed.",
    "created_at": "2009-02-01T23:13:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5152#issuecomment-39421",
    "user": "wdj"
}
```

The patch trac-5152-abelian-gp-order.patch (1.6 kB) does exactly as instructed.



---

archive/issue_comments_039422.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T18:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5152#issuecomment-39422",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039423.json:
```json
{
    "body": "Merged in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T18:20:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5152#issuecomment-39423",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha4.

Cheers,

Michael
