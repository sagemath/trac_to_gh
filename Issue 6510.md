# Issue 6510: Adds __nonzero__ method to abelian groups

archive/issues_006510.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: abelian groups\n\n\n```\n sage: E=EllipticCurve([0,82])\n sage: tor=E.torsion_subgroup()\n sage: if tor:\n ...       print tor.order()\n 1\n```\n\n\nWe'd like to have tor evaluate to false in boolean context.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6510\n\n",
    "created_at": "2009-07-10T21:57:38Z",
    "labels": [
        "algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "Adds __nonzero__ method to abelian groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6510",
    "user": "tsutton"
}
```
Assignee: tbd

Keywords: abelian groups


```
 sage: E=EllipticCurve([0,82])
 sage: tor=E.torsion_subgroup()
 sage: if tor:
 ...       print tor.order()
 1
```


We'd like to have tor evaluate to false in boolean context.

Issue created by migration from https://trac.sagemath.org/ticket/6510





---

archive/issue_comments_053037.json:
```json
{
    "body": "Attachment [trac_6510.patch](tarball://root/attachments/some-uuid/ticket6510/trac_6510.patch) by tsutton created at 2009-07-10 22:11:00",
    "created_at": "2009-07-10T22:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53037",
    "user": "tsutton"
}
```

Attachment [trac_6510.patch](tarball://root/attachments/some-uuid/ticket6510/trac_6510.patch) by tsutton created at 2009-07-10 22:11:00



---

archive/issue_comments_053038.json:
```json
{
    "body": "Needs a doctest.",
    "created_at": "2009-07-10T22:12:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53038",
    "user": "@roed314"
}
```

Needs a doctest.



---

archive/issue_comments_053039.json:
```json
{
    "body": "Attachment [trac_6510.2.patch](tarball://root/attachments/some-uuid/ticket6510/trac_6510.2.patch) by tsutton created at 2009-07-10 22:19:55",
    "created_at": "2009-07-10T22:19:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53039",
    "user": "tsutton"
}
```

Attachment [trac_6510.2.patch](tarball://root/attachments/some-uuid/ticket6510/trac_6510.2.patch) by tsutton created at 2009-07-10 22:19:55



---

archive/issue_comments_053040.json:
```json
{
    "body": "Looks good.  All tests pass for me.",
    "created_at": "2009-07-11T00:02:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53040",
    "user": "@roed314"
}
```

Looks good.  All tests pass for me.



---

archive/issue_comments_053041.json:
```json
{
    "body": "Still needs a doctest!",
    "created_at": "2009-07-11T12:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53041",
    "user": "ylchapuy"
}
```

Still needs a doctest!



---

archive/issue_comments_053042.json:
```json
{
    "body": "Now includes #indirect doctest",
    "created_at": "2009-07-12T08:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53042",
    "user": "@roed314"
}
```

Now includes #indirect doctest



---

archive/issue_comments_053043.json:
```json
{
    "body": "What's the real name of tsutton? The real name should be used so we can give proper credit to contributors.",
    "created_at": "2009-07-16T14:39:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53043",
    "user": "mvngu"
}
```

What's the real name of tsutton? The real name should be used so we can give proper credit to contributors.



---

archive/issue_comments_053044.json:
```json
{
    "body": "I assume that I only need to apply the patch `trac_6510.3.patch`. But why are there three functions `__nonzero__(self)` all of which are the same and reside in the same module, but each block of definition contains different stuff? For example, after applying `trac_6510.3.patch`, I get the following in `sage/groups/abelian_gps/abelian_group.py`:\n\n```\n    def __nonzero__(self):\n        return len(self.invariants()) != 0\n\n    def __nonzero__(self):\n        \"\"\"                                                                     \n        Returns True if this group is nontrivial.                               \n                                                                                \n        EXAMPLES::                                                              \n                                                                                \n            sage: E = EllipticCurve([0,82])                                     \n            sage: T = E.torsion_subgroup()                                      \n            sage: bool(T)                                                       \n            False                                                               \n        \"\"\"\n        return len(self.invariants()) != 0\n\n    def __nonzero__(self):\n        \"\"\"                                                                     \n        Returns True if this group is nontrivial.                               \n                                                                                \n        EXAMPLES::                                                              \n                                                                                \n            sage: E = EllipticCurve([0,82])                                     \n            sage: T = E.torsion_subgroup()                                      \n            sage: bool(T) # indirect doctest                                    \n            False                                                               \n        \"\"\"\n        return len(self.invariants()) != 0\n```\n\nChoose which block of function definition you want, and upload a new patch. Preferrably, you should replace `trac_6510.3.patch` with your new patch. I'm marking this as needs work. After a new patch is uploaded, positive review can be reinstated.",
    "created_at": "2009-07-16T14:53:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53044",
    "user": "mvngu"
}
```

I assume that I only need to apply the patch `trac_6510.3.patch`. But why are there three functions `__nonzero__(self)` all of which are the same and reside in the same module, but each block of definition contains different stuff? For example, after applying `trac_6510.3.patch`, I get the following in `sage/groups/abelian_gps/abelian_group.py`:

```
    def __nonzero__(self):
        return len(self.invariants()) != 0

    def __nonzero__(self):
        """                                                                     
        Returns True if this group is nontrivial.                               
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: E = EllipticCurve([0,82])                                     
            sage: T = E.torsion_subgroup()                                      
            sage: bool(T)                                                       
            False                                                               
        """
        return len(self.invariants()) != 0

    def __nonzero__(self):
        """                                                                     
        Returns True if this group is nontrivial.                               
                                                                                
        EXAMPLES::                                                              
                                                                                
            sage: E = EllipticCurve([0,82])                                     
            sage: T = E.torsion_subgroup()                                      
            sage: bool(T) # indirect doctest                                    
            False                                                               
        """
        return len(self.invariants()) != 0
```

Choose which block of function definition you want, and upload a new patch. Preferrably, you should replace `trac_6510.3.patch` with your new patch. I'm marking this as needs work. After a new patch is uploaded, positive review can be reinstated.



---

archive/issue_comments_053045.json:
```json
{
    "body": "Attachment [trac_6510.3.patch](tarball://root/attachments/some-uuid/ticket6510/trac_6510.3.patch) by @roed314 created at 2009-07-16 18:21:10",
    "created_at": "2009-07-16T18:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53045",
    "user": "@roed314"
}
```

Attachment [trac_6510.3.patch](tarball://root/attachments/some-uuid/ticket6510/trac_6510.3.patch) by @roed314 created at 2009-07-16 18:21:10



---

archive/issue_comments_053046.json:
```json
{
    "body": "Fixed.  tsutton's real name is Taylor Sutton.",
    "created_at": "2009-07-16T18:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53046",
    "user": "@roed314"
}
```

Fixed.  tsutton's real name is Taylor Sutton.



---

archive/issue_comments_053047.json:
```json
{
    "body": "Merged the patch `trac_6510.3.patch` in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T19:12:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53047",
    "user": "mvngu"
}
```

Merged the patch `trac_6510.3.patch` in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_053048.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6510",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6510#issuecomment-53048",
    "user": "mvngu"
}
```

Resolution: fixed
