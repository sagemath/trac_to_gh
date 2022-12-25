# Issue 3576: stupid bug in RDF

archive/issues_003576.json:
```json
{
    "body": "Assignee: somebody\n\nThis is sad:\n\n\n```\nsage: RDF(-1).nth_root(2)\n```\n\n\nLook at the dumb code in real_double.pyx:\n\n```\n    def nth_root(self, int n):\n        \"\"\"\n        Returns the $n^{th}$ root of self.\n        EXAMPLES:\n            sage: r = RDF(-125.0); r.nth_root(3)\n            -5.0\n            sage: r.nth_root(5)\n            -2.6265278044\n        \"\"\"\n        if n == 0:\n            return RealDoubleElement(float('nan'))\n        if self._value < 0 and GSL_IS_EVEN(n):\n            pass #return self._complex_double_().pow(1.0/n)\n        else:\n            return RealDoubleElement(self.__nth_root(n))\n```\n\n\nAmazingly this was introduced in the very first patch by Tom Boothby in 2006 and nobody ever noticed!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/3576\n\n",
    "created_at": "2008-07-06T22:22:32Z",
    "labels": [
        "component: basic arithmetic",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "stupid bug in RDF",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3576",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody

This is sad:


```
sage: RDF(-1).nth_root(2)
```


Look at the dumb code in real_double.pyx:

```
    def nth_root(self, int n):
        """
        Returns the $n^{th}$ root of self.
        EXAMPLES:
            sage: r = RDF(-125.0); r.nth_root(3)
            -5.0
            sage: r.nth_root(5)
            -2.6265278044
        """
        if n == 0:
            return RealDoubleElement(float('nan'))
        if self._value < 0 and GSL_IS_EVEN(n):
            pass #return self._complex_double_().pow(1.0/n)
        else:
            return RealDoubleElement(self.__nth_root(n))
```


Amazingly this was introduced in the very first patch by Tom Boothby in 2006 and nobody ever noticed!!

Issue created by migration from https://trac.sagemath.org/ticket/3576





---

archive/issue_comments_025205.json:
```json
{
    "body": "This is also bad, bad, bad:\n\n```\nsage: RDF(-1).nth_root(5)^(5)\n-1.35861063971\n```\n",
    "created_at": "2008-07-06T23:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3576#issuecomment-25205",
    "user": "https://github.com/williamstein"
}
```

This is also bad, bad, bad:

```
sage: RDF(-1).nth_root(5)^(5)
-1.35861063971
```




---

archive/issue_comments_025206.json:
```json
{
    "body": "Attachment [sage-3576.patch](tarball://root/attachments/some-uuid/ticket3576/sage-3576.patch) by @williamstein created at 2008-07-06 23:13:07",
    "created_at": "2008-07-06T23:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3576#issuecomment-25206",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3576.patch](tarball://root/attachments/some-uuid/ticket3576/sage-3576.patch) by @williamstein created at 2008-07-06 23:13:07



---

archive/issue_comments_025207.json:
```json
{
    "body": "The code is definitely much better style and correctness-wise after the patch.\n\n+1",
    "created_at": "2008-07-06T23:20:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3576#issuecomment-25207",
    "user": "https://github.com/mwhansen"
}
```

The code is definitely much better style and correctness-wise after the patch.

+1



---

archive/issue_events_008191.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-07-07T02:03:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3576",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3576#event-8191"
}
```



---

archive/issue_comments_025208.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha2",
    "created_at": "2008-07-07T02:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3576#issuecomment-25208",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.4.alpha2



---

archive/issue_comments_025209.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T02:03:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3576#issuecomment-25209",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_025210.json:
```json
{
    "body": "wow I'm dumb!",
    "created_at": "2008-07-07T03:21:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3576",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3576#issuecomment-25210",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

wow I'm dumb!
