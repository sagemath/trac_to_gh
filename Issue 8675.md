# Issue 8675: Remove AmbientSpace._constructor and fix consequences

archive/issues_008675.json:
```json
{
    "body": "Assignee: @aghitza\n\nCurrently in schemes/generic/ambient_space we see\n\n\n```\n...\n# Derived classes must overload all of the following functions\n...\ndef _constructor(self):\n    \"\"\"\n    TEST::\n\n        sage: from sage.schemes.generic.ambient_space import AmbientSpace\n        sage: A = AmbientSpace(5, ZZ)\n        sage: A._constructor()\n        Traceback (most recent call last):\n        ...\n        NotImplementedError\n    \"\"\"\n    raise NotImplementedError\n...\n# End overloads\n...\ndef base_extend(self, S, check=True):\n    \"\"\"\n\t...\n    \"\"\"\n    if is_CommutativeRing(S):\n        R = self.base_ring()\n        if S == R:\n            return self\n        if check:\n            if not S.has_coerce_map_from(R):\n                raise ValueError, \"No natural map from the base ring (=%s) to S (=%s)\"%(R, S)\n        return self._constructor(self.__n, S, self.variable_names())\n    else:\n        raise NotImplementedError\n...\n```\n\n\nI have the following problems with it:\n* _constructor function has no documentation and a very strange name (because !__init!__ IS a constructor, why do we need another one?)\n* Its usage in the same class calls it with arguments different from specified.\n* With these arguments _constructor still would not quite make sense for toric varieties, where dimension and base ring are not sufficient for creation (and if we do take extra information from self, why do we need to pass dimension explicitly?)\n* Digging further, I have found the following as a consequence of using _constructor:\n\n\n```\nsage: A = AffineSpace(2)\nsage: (A^2).variable_names()\n('x0', 'x1', 'x0', 'x1')\n```\n\n\nI propose the following solution, making AmbientSpace behave closer to FreeModule's like ZZ^n:\n* Remove _constructor\n* Make base_extend check if extension is possible and call change_ring\n* Make change_ring mandatory for overriding - it should create \"exactly the same\" ambient space but with a new ring, even if it is not a base extension.\n* Powers of affine ambient spaces use default indexed variables rather than trying to cook up something from variables of the base:\n\n\n```\nsage: A = AffineSpace(2)\nsage: (A^2).variable_names()\n('x0', 'x1', 'x2', 'x3')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8675\n\n",
    "created_at": "2010-04-11T23:31:02Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "Remove AmbientSpace._constructor and fix consequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8675",
    "user": "https://github.com/novoselt"
}
```
Assignee: @aghitza

Currently in schemes/generic/ambient_space we see


```
...
# Derived classes must overload all of the following functions
...
def _constructor(self):
    """
    TEST::

        sage: from sage.schemes.generic.ambient_space import AmbientSpace
        sage: A = AmbientSpace(5, ZZ)
        sage: A._constructor()
        Traceback (most recent call last):
        ...
        NotImplementedError
    """
    raise NotImplementedError
...
# End overloads
...
def base_extend(self, S, check=True):
    """
	...
    """
    if is_CommutativeRing(S):
        R = self.base_ring()
        if S == R:
            return self
        if check:
            if not S.has_coerce_map_from(R):
                raise ValueError, "No natural map from the base ring (=%s) to S (=%s)"%(R, S)
        return self._constructor(self.__n, S, self.variable_names())
    else:
        raise NotImplementedError
...
```


I have the following problems with it:
* _constructor function has no documentation and a very strange name (because !__init!__ IS a constructor, why do we need another one?)
* Its usage in the same class calls it with arguments different from specified.
* With these arguments _constructor still would not quite make sense for toric varieties, where dimension and base ring are not sufficient for creation (and if we do take extra information from self, why do we need to pass dimension explicitly?)
* Digging further, I have found the following as a consequence of using _constructor:


```
sage: A = AffineSpace(2)
sage: (A^2).variable_names()
('x0', 'x1', 'x0', 'x1')
```


I propose the following solution, making AmbientSpace behave closer to FreeModule's like ZZ^n:
* Remove _constructor
* Make base_extend check if extension is possible and call change_ring
* Make change_ring mandatory for overriding - it should create "exactly the same" ambient space but with a new ring, even if it is not a base extension.
* Powers of affine ambient spaces use default indexed variables rather than trying to cook up something from variables of the base:


```
sage: A = AffineSpace(2)
sage: (A^2).variable_names()
('x0', 'x1', 'x2', 'x3')
```


Issue created by migration from https://trac.sagemath.org/ticket/8675





---

archive/issue_comments_078818.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-11T23:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8675#issuecomment-78818",
    "user": "https://github.com/novoselt"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078819.json:
```json
{
    "body": "Attachment [trac_8675_remove_ambient_space_constructor.patch](tarball://root/attachments/some-uuid/ticket8675/trac_8675_remove_ambient_space_constructor.patch) by @novoselt created at 2010-04-11 23:36:55",
    "created_at": "2010-04-11T23:36:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8675#issuecomment-78819",
    "user": "https://github.com/novoselt"
}
```

Attachment [trac_8675_remove_ambient_space_constructor.patch](tarball://root/attachments/some-uuid/ticket8675/trac_8675_remove_ambient_space_constructor.patch) by @novoselt created at 2010-04-11 23:36:55



---

archive/issue_comments_078820.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-18T12:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8675#issuecomment-78820",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078821.json:
```json
{
    "body": "Looks good, passes tests, and fixes a number of inconsistencies.",
    "created_at": "2010-05-18T12:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8675#issuecomment-78821",
    "user": "https://github.com/aghitza"
}
```

Looks good, passes tests, and fixes a number of inconsistencies.



---

archive/issue_events_008849.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-06-06T07:48:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8675",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8675#event-8849"
}
```



---

archive/issue_comments_078822.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-06T07:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8675",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8675#issuecomment-78822",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
