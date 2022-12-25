# Issue 34: Bug in is_simple() for a space of ModularSymbols

archive/issues_000034.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n   sage: M = ModularSymbols(Gamma0(22),2,sign=1)\n   sage: M1 = M.decomposition()[1]\n   sage: M1\n   Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(22) of weight 2 with sign 1 over Rational Field\n   sage: M1.is_simple() ## throws a TypeError\n```\n\n\nIn fact, I can find lots of examples where this happens: levels 6, 7, 8, and 9 with weight 24 all have subspaces which crash is_simple.\n\nI don't really know if this qualifies as \"critical,\" but it seems more than just \"annoying.\" Maybe the page name should be clarified (at least to me)?\n\n-- Craig Citro\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/34\n\n",
    "created_at": "2006-09-12T23:28:51Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Bug in is_simple() for a space of ModularSymbols",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/34",
    "user": "https://github.com/williamstein"
}
```
Assignee: somebody


```
   sage: M = ModularSymbols(Gamma0(22),2,sign=1)
   sage: M1 = M.decomposition()[1]
   sage: M1
   Modular Symbols subspace of dimension 2 of Modular Symbols space of dimension 5 for Gamma_0(22) of weight 2 with sign 1 over Rational Field
   sage: M1.is_simple() ## throws a TypeError
```


In fact, I can find lots of examples where this happens: levels 6, 7, 8, and 9 with weight 24 all have subspaces which crash is_simple.

I don't really know if this qualifies as "critical," but it seems more than just "annoying." Maybe the page name should be clarified (at least to me)?

-- Craig Citro



Issue created by migration from https://trac.sagemath.org/ticket/34





---

archive/issue_comments_000220.json:
```json
{
    "body": "Added doctest to sage/modular/modsym/subspace.py exposing related bug.  As of 2.1.5, does not pass.",
    "created_at": "2007-02-19T22:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-220",
    "user": "https://github.com/ncalexan"
}
```

Added doctest to sage/modular/modsym/subspace.py exposing related bug.  As of 2.1.5, does not pass.



---

archive/issue_comments_000221.json:
```json
{
    "body": "Changing assignee from somebody to @williamstein.",
    "created_at": "2007-02-19T22:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-221",
    "user": "https://github.com/ncalexan"
}
```

Changing assignee from somebody to @williamstein.



---

archive/issue_comments_000222.json:
```json
{
    "body": "Changing component from basic arithmetic to modular forms.",
    "created_at": "2007-02-19T22:06:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-222",
    "user": "https://github.com/ncalexan"
}
```

Changing component from basic arithmetic to modular forms.



---

archive/issue_comments_000223.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2007-08-16T09:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-223",
    "user": "https://github.com/williamstein"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_000224.json:
```json
{
    "body": "This throws notimplemented error now.  The problem is that actually implementing this in general efficiently is hard.  Because it's now a not implemented error, I've changed this to an enhancement.",
    "created_at": "2007-08-16T09:45:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-224",
    "user": "https://github.com/williamstein"
}
```

This throws notimplemented error now.  The problem is that actually implementing this in general efficiently is hard.  Because it's now a not implemented error, I've changed this to an enhancement.



---

archive/issue_comments_000225.json:
```json
{
    "body": "This is still a problem with Sage 2.8.2:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.2, Release Date: 2007-08-22                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: M = ModularSymbols(Gamma0(22),2,sign=1)\nsage: M1 = M.decomposition()[1]\nsage: M1\nModular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(22) of weight 2 with sign 1 over Rational Field\nsage: M1.is_simple()\n---------------------------------------------------------------------------\n<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)\n\n/tmp/Work2/sage-2.8.2/<ipython console> in <module>()\n\n/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in is_simple(self)\n    234             return self._is_simple\n    235         except AttributeError:\n--> 236             D = self.factorization()\n    237             if len(D) == 0 or len(D) == 1 and D[0][1] == 1:\n    238                 self._is_simple = True\n\n/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py in factorization(self)\n    197         if r != s:\n    198             raise NotImplementedError, \"modular symbols factorization not fully implemented yet --  self has dimension %s, but sum of dimensions of factors is %s\"%(\n--> 199             r, s)\n    200         self._factorization = sage.structure.factorization.Factorization(D, cr=True)\n    201         return self._factorization\n\n<type 'exceptions.NotImplementedError'>: modular symbols factorization not fully implemented yet --  self has dimension 3, but sum of dimensions of factors is 2\nsage:    \n```\n\n\nMaybe something worth fixing during the next bug day.\n\nCheers,\n\nMichael",
    "created_at": "2007-08-28T11:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-225",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still a problem with Sage 2.8.2:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: M = ModularSymbols(Gamma0(22),2,sign=1)
sage: M1 = M.decomposition()[1]
sage: M1
Modular Symbols subspace of dimension 3 of Modular Symbols space of dimension 5 for Gamma_0(22) of weight 2 with sign 1 over Rational Field
sage: M1.is_simple()
---------------------------------------------------------------------------
<type 'exceptions.NotImplementedError'>   Traceback (most recent call last)

/tmp/Work2/sage-2.8.2/<ipython console> in <module>()

/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/modular/modsym/space.py in is_simple(self)
    234             return self._is_simple
    235         except AttributeError:
--> 236             D = self.factorization()
    237             if len(D) == 0 or len(D) == 1 and D[0][1] == 1:
    238                 self._is_simple = True

/tmp/Work2/sage-2.8.2/local/lib/python2.5/site-packages/sage/modular/modsym/subspace.py in factorization(self)
    197         if r != s:
    198             raise NotImplementedError, "modular symbols factorization not fully implemented yet --  self has dimension %s, but sum of dimensions of factors is %s"%(
--> 199             r, s)
    200         self._factorization = sage.structure.factorization.Factorization(D, cr=True)
    201         return self._factorization

<type 'exceptions.NotImplementedError'>: modular symbols factorization not fully implemented yet --  self has dimension 3, but sum of dimensions of factors is 2
sage:    
```


Maybe something worth fixing during the next bug day.

Cheers,

Michael



---

archive/issue_comments_000226.json:
```json
{
    "body": "This, as well as the other cases listed in Craig's post, work for me in sage-3.0.alpha5.\n\nI think this was fixed as a side effect of Craig's various fixes in the modular symbols code.",
    "created_at": "2008-04-19T01:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-226",
    "user": "https://github.com/aghitza"
}
```

This, as well as the other cases listed in Craig's post, work for me in sage-3.0.alpha5.

I think this was fixed as a side effect of Craig's various fixes in the modular symbols code.



---

archive/issue_comments_000227.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-19T21:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-227",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000033.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-19T21:20:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/34#event-33"
}
```



---

archive/issue_comments_000228.json:
```json
{
    "body": "Fixed in Sage 3.0.rc0 due to patches by Creg Citro merged earlier in the 3.0 alpha cycle.",
    "created_at": "2008-04-19T21:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/34",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/34#issuecomment-228",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed in Sage 3.0.rc0 due to patches by Creg Citro merged earlier in the 3.0 alpha cycle.
