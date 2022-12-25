# Issue 4299: sha bound totally busted for rank 0 curves

archive/issues_004299.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: E = EllipticCurve('11a1')\nsage: Sha = E.sha()\nsage: Sha.bound()\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/wstein/sage/devel/sage-main/sage/schemes/elliptic_curves/<ipython console> in <module>()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in bound(self)\n    698         B of primes such that any divisor of Sha is in this list.\n    699         \"\"\"\n--> 700         if self.L1_vanishes():\n    701             B = self.bound_kolyvagin()\n    702         else:\n\nAttributeError: 'Sha' object has no attribute 'L1_vanishes'\nsage:\n                                        \n```\n\n\nThis is likely easy to fix and was caused by refactoring without enough doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4299\n\n",
    "created_at": "2008-10-15T15:09:34Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.3",
    "title": "sha bound totally busted for rank 0 curves",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4299",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein


```
sage: E = EllipticCurve('11a1')
sage: Sha = E.sha()
sage: Sha.bound()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/wstein/sage/devel/sage-main/sage/schemes/elliptic_curves/<ipython console> in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/sha.py in bound(self)
    698         B of primes such that any divisor of Sha is in this list.
    699         """
--> 700         if self.L1_vanishes():
    701             B = self.bound_kolyvagin()
    702         else:

AttributeError: 'Sha' object has no attribute 'L1_vanishes'
sage:
                                        
```


This is likely easy to fix and was caused by refactoring without enough doctests.

Issue created by migration from https://trac.sagemath.org/ticket/4299





---

archive/issue_comments_031379.json:
```json
{
    "body": "note -- this is against 3.1.2 and sha.py, but sha.py was renamed for 3.1.3, so this patch will need a manual REBASE!  but it's better than nothing.",
    "created_at": "2008-10-15T15:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4299#issuecomment-31379",
    "user": "https://github.com/williamstein"
}
```

note -- this is against 3.1.2 and sha.py, but sha.py was renamed for 3.1.3, so this patch will need a manual REBASE!  but it's better than nothing.



---

archive/issue_comments_031380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-15T15:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4299#issuecomment-31380",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_031381.json:
```json
{
    "body": "Attachment [sage-4299.patch](tarball://root/attachments/some-uuid/ticket4299/sage-4299.patch) by @williamstein created at 2008-10-15 15:22:01\n\nthis is fixed in 3.1.3  yeah!",
    "created_at": "2008-10-15T15:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4299",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4299#issuecomment-31381",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-4299.patch](tarball://root/attachments/some-uuid/ticket4299/sage-4299.patch) by @williamstein created at 2008-10-15 15:22:01

this is fixed in 3.1.3  yeah!
