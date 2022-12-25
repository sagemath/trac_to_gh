# Issue 7504: Magma booleans don't evaluate correctly in boolean contexts

archive/issues_007504.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: magma, boolean context\n\nCompare the following results:\n\n```\nsage: bool(pari(False))\nFalse\nsage: bool(gap(False))\nFalse\nsage: bool(maxima(False))\nFalse\nsage: bool(maple(False))\nFalse\nsage: bool(mathematica(False))\nFalse\nsage: bool(magma(False))\nTrue\n```\n\nThis is in some sense the inverse problem to #845.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7504\n\n",
    "created_at": "2009-11-20T13:27:44Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Magma booleans don't evaluate correctly in boolean contexts",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7504",
    "user": "https://github.com/kedlaya"
}
```
Assignee: @williamstein

Keywords: magma, boolean context

Compare the following results:

```
sage: bool(pari(False))
False
sage: bool(gap(False))
False
sage: bool(maxima(False))
False
sage: bool(maple(False))
False
sage: bool(mathematica(False))
False
sage: bool(magma(False))
True
```

This is in some sense the inverse problem to #845.

Issue created by migration from https://trac.sagemath.org/ticket/7504





---

archive/issue_comments_063321.json:
```json
{
    "body": "In \"gap.py\", in the \"class GapElement(ExpectElement)\", there is (lines 1058 ff):\n\n```\n    def bool(self):\n        \"\"\"\n        EXAMPLES::\n        \n            sage: bool(gap(2))\n            True\n            sage: gap(0).bool()\n            False\n            sage: gap('false').bool()\n            False\n        \"\"\"\n        P = self._check_valid()\n        return self != P(0) and repr(self) != 'false'\n```\n\nI didn't check maxima.py, ... but in magma.py, I couldn't find a counterpart in the class MagmaElement. My first attempt to add this with the obvious minor modifications failed however (so I do not post the patch):\n\n```\nsage: magma(True).bool()\n---------------------------------------------------------------------------\nRuntimeError                              Traceback (most recent call last)\n\n/Users/georgweber/.sage/temp/susanne_webers_computer.local/15820/_Users_georgweber__sage_init_sage_0.py in <module>()\n\n/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in bool(self)\n   2111         \"\"\"\n   2112         P = self._check_valid()\n-> 2113         return self != P(0) and repr(self) != 'false'\n   2114 \n   2115     def __len__(self):\n\n/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:6484)()\n\n/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6363)()\n\n/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __cmp__(self, other)\n   1521         P = self.parent()\n   1522         if P.eval(\"%s %s %s\"%(self.name(), P._equality_symbol(),\n-> 1523                                  other.name())) == P._true_symbol():\n   1524             return 0\n   1525         elif P.eval(\"%s %s %s\"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():\n\n/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in eval(self, x, strip, **kwds)\n    478         ans = Expect.eval(self, x, **kwds).replace('\\\\\\n','')\n    479         if 'Runtime error' in ans or 'User error' in ans:\n--> 480             raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    481         return ans\n    482 \n\nRuntimeError: Error evaluating Magma code.\nIN:_sage_[3] eq _sage_[6];\nOUT:\n>> _sage_[3] eq _sage_[6];\n             ^\nRuntime error in 'eq': Bad argument types\nArgument types given: BoolElt, RngIntElt\n```\n",
    "created_at": "2009-11-20T23:24:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63321",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

In "gap.py", in the "class GapElement(ExpectElement)", there is (lines 1058 ff):

```
    def bool(self):
        """
        EXAMPLES::
        
            sage: bool(gap(2))
            True
            sage: gap(0).bool()
            False
            sage: gap('false').bool()
            False
        """
        P = self._check_valid()
        return self != P(0) and repr(self) != 'false'
```

I didn't check maxima.py, ... but in magma.py, I couldn't find a counterpart in the class MagmaElement. My first attempt to add this with the obvious minor modifications failed however (so I do not post the patch):

```
sage: magma(True).bool()
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/Users/georgweber/.sage/temp/susanne_webers_computer.local/15820/_Users_georgweber__sage_init_sage_0.py in <module>()

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in bool(self)
   2111         """
   2112         P = self._check_valid()
-> 2113         return self != P(0) and repr(self) != 'false'
   2114 
   2115     def __len__(self):

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:6484)()

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:6363)()

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __cmp__(self, other)
   1521         P = self.parent()
   1522         if P.eval("%s %s %s"%(self.name(), P._equality_symbol(),
-> 1523                                  other.name())) == P._true_symbol():
   1524             return 0
   1525         elif P.eval("%s %s %s"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():

/Users/Shared/sage/sage-4.2.1/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in eval(self, x, strip, **kwds)
    478         ans = Expect.eval(self, x, **kwds).replace('\\\n','')
    479         if 'Runtime error' in ans or 'User error' in ans:
--> 480             raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    481         return ans
    482 

RuntimeError: Error evaluating Magma code.
IN:_sage_[3] eq _sage_[6];
OUT:
>> _sage_[3] eq _sage_[6];
             ^
Runtime error in 'eq': Bad argument types
Argument types given: BoolElt, RngIntElt
```




---

archive/issue_comments_063322.json:
```json
{
    "body": "Ouch, I give up after experimenting further and getting (one and the same session!):\n\n```\nsage: magma(False).bool()\nFalse\nsage: bool(magma(False))\nTrue\n```\n",
    "created_at": "2009-11-20T23:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63322",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Ouch, I give up after experimenting further and getting (one and the same session!):

```
sage: magma(False).bool()
False
sage: bool(magma(False))
True
```




---

archive/issue_comments_063323.json:
```json
{
    "body": "` bool(f) ` calls ` f.__nonzero__() `",
    "created_at": "2009-11-21T15:27:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63323",
    "user": "https://github.com/mwhansen"
}
```

` bool(f) ` calls ` f.__nonzero__() `



---

archive/issue_comments_063324.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-22T22:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63324",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_063325.json:
```json
{
    "body": "In Magma we have:\n\n\n```\n> false ne 0;\n\n>> false ne 0;\n         ^\nRuntime error in 'ne': Bad argument types\nArgument types given: BoolElt, RngIntElt\n\n> 1 ne 0;    \ntrue\n```\n\n\nI.e., comparing false to 0 is not allowed in Magma.   So we need to add code to __nonzero__ that also tests bools.",
    "created_at": "2009-11-22T22:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63325",
    "user": "https://github.com/williamstein"
}
```

In Magma we have:


```
> false ne 0;

>> false ne 0;
         ^
Runtime error in 'ne': Bad argument types
Argument types given: BoolElt, RngIntElt

> 1 ne 0;    
true
```


I.e., comparing false to 0 is not allowed in Magma.   So we need to add code to __nonzero__ that also tests bools.



---

archive/issue_comments_063326.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-24T22:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63326",
    "user": "https://github.com/kedlaya"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_063327.json:
```json
{
    "body": "Attachment [trac_7504.patch](tarball://root/attachments/some-uuid/ticket7504/trac_7504.patch) by @kedlaya created at 2009-11-24 22:19:29\n\nThis applied against 4.2, fixed the issue for me, and doesn't appear to have caused any failures of optional doctests.",
    "created_at": "2009-11-24T22:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63327",
    "user": "https://github.com/kedlaya"
}
```

Attachment [trac_7504.patch](tarball://root/attachments/some-uuid/ticket7504/trac_7504.patch) by @kedlaya created at 2009-11-24 22:19:29

This applied against 4.2, fixed the issue for me, and doesn't appear to have caused any failures of optional doctests.



---

archive/issue_events_017790.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-29T05:43:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7504#event-17790"
}
```



---

archive/issue_comments_063328.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:43:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7504#issuecomment-63328",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017791.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-12-09T00:19:57Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7504",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7504#event-17791"
}
```
