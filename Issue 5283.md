# Issue 5283: problem with posets: iterating the subposet construction

archive/issues_005283.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  sage-combinat\n\nIf I try to create a subposet of a subposet of something, I have problems:\n\n```\nsage: P = BooleanLattice(2)\nsage: above = P.principal_order_filter(0)\nsage: Q = P.subposet(above)\nsage: above_new = Q.principal_order_filter(Q.list()[0])\nsage: Q.subposet(above_new)\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/Users/palmieri/.sage/temp/Macintosh.local/16679/_Users_palmieri__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/posets.pyc in subposet(self, elements)\n   1036             raise ValueError, \"not a list.\"\n   1037         for element in elements:\n-> 1038             if element not in self:\n   1039                 raise ValueError, \"element not in self\"\n   1040         relations = []\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/posets.pyc in __contains__(self, x)\n    272         else:\n    273             y = x\n--> 274         return y in self._elements\n    275 \n    276     def __call__(self,element):\n\n/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/elements.pyc in __eq__(self, other)\n     50             False\n     51         \"\"\"\n---> 52         return self.parent() == other.parent() \\\n     53                 and self.element == other.element \\\n     54                 and self.vertex == other.vertex\n\nAttributeError: 'int' object has no attribute 'parent'\n```\n\nI think that the problem is in the `__contains__` method for posets, where the argument x is converted to x.element, which might be an int.  I'm not sure why I have to iterate the subposet construction twice to get this to happen...\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5283\n\n",
    "created_at": "2009-02-16T07:01:52Z",
    "labels": [
        "component: combinatorics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "problem with posets: iterating the subposet construction",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5283",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

CC:  sage-combinat

If I try to create a subposet of a subposet of something, I have problems:

```
sage: P = BooleanLattice(2)
sage: above = P.principal_order_filter(0)
sage: Q = P.subposet(above)
sage: above_new = Q.principal_order_filter(Q.list()[0])
sage: Q.subposet(above_new)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/Users/palmieri/.sage/temp/Macintosh.local/16679/_Users_palmieri__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/posets.pyc in subposet(self, elements)
   1036             raise ValueError, "not a list."
   1037         for element in elements:
-> 1038             if element not in self:
   1039                 raise ValueError, "element not in self"
   1040         relations = []

/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/posets.pyc in __contains__(self, x)
    272         else:
    273             y = x
--> 274         return y in self._elements
    275 
    276     def __call__(self,element):

/Applications/sage/local/lib/python2.5/site-packages/sage/combinat/posets/elements.pyc in __eq__(self, other)
     50             False
     51         """
---> 52         return self.parent() == other.parent() \
     53                 and self.element == other.element \
     54                 and self.vertex == other.vertex

AttributeError: 'int' object has no attribute 'parent'
```

I think that the problem is in the `__contains__` method for posets, where the argument x is converted to x.element, which might be an int.  I'm not sure why I have to iterate the subposet construction twice to get this to happen...



Issue created by migration from https://trac.sagemath.org/ticket/5283





---

archive/issue_comments_040524.json:
```json
{
    "body": "Attachment [trac_5283.patch](tarball://root/attachments/some-uuid/ticket5283/trac_5283.patch) by @saliola created at 2009-04-30 09:56:11\n\nThe poset elements are just wrapping elements, so I modified the subposet constructor to unwrap before constructing the subposet (it was wrapping a wrapped element).\n\nNote that you can still create a poset of poset elements, this is just for the subposet constructor.",
    "created_at": "2009-04-30T09:56:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5283#issuecomment-40524",
    "user": "https://github.com/saliola"
}
```

Attachment [trac_5283.patch](tarball://root/attachments/some-uuid/ticket5283/trac_5283.patch) by @saliola created at 2009-04-30 09:56:11

The poset elements are just wrapping elements, so I modified the subposet constructor to unwrap before constructing the subposet (it was wrapping a wrapped element).

Note that you can still create a poset of poset elements, this is just for the subposet constructor.



---

archive/issue_comments_040525.json:
```json
{
    "body": "This fixes the problem, and all tests pass.  Simple change to the code, good addition to the doctests.",
    "created_at": "2009-05-03T04:36:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5283#issuecomment-40525",
    "user": "https://github.com/jhpalmieri"
}
```

This fixes the problem, and all tests pass.  Simple change to the code, good addition to the doctests.



---

archive/issue_comments_040526.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-11T10:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5283#issuecomment-40526",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_040527.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-11T10:00:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5283#issuecomment-40527",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005538.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-05-11T10:00:45Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5283",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5283#event-5538"
}
```
