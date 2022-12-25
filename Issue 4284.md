# Issue 4284: modular symbols -- applying Hecke operator on cuspidal subspace broken

archive/issues_004284.json:
```json
{
    "body": "Assignee: citro\n\nBug in sage-3.1.2:\n\n```\nsage: M = ModularSymbols(11).cuspidal_subspace(); M.hecke_operator(3)(M.0)\n\n---------------------------------------------------------------------------\nAttributeError                            Traceback (most recent call last)\n\n/home/wstein/<ipython console> in <module>()\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py in __call__(self, x)\n    127         \"\"\"\n    128         T = self.hecke_module_morphism()\n--> 129         return T(x)\n    130\n    131     def __rmul__(self, left):\n\n/home/wstein/sage/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py in __call__(self, x)\n    115             x = x.element()\n    116         else:\n--> 117             x = self.domain().coordinate_vector(x)\n    118         v = x*self.matrix()\n    119         C = self.codomain()\n\nAttributeError: 'ModularSymbolsSubspace' object has no attribute 'coordinate_vector'\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/4284\n\n",
    "created_at": "2008-10-14T14:38:35Z",
    "labels": [
        "component: modular forms",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "modular symbols -- applying Hecke operator on cuspidal subspace broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4284",
    "user": "https://github.com/williamstein"
}
```
Assignee: citro

Bug in sage-3.1.2:

```
sage: M = ModularSymbols(11).cuspidal_subspace(); M.hecke_operator(3)(M.0)

---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/wstein/<ipython console> in <module>()

/home/wstein/sage/local/lib/python2.5/site-packages/sage/modular/hecke/hecke_operator.py in __call__(self, x)
    127         """
    128         T = self.hecke_module_morphism()
--> 129         return T(x)
    130
    131     def __rmul__(self, left):

/home/wstein/sage/local/lib/python2.5/site-packages/sage/modules/matrix_morphism.py in __call__(self, x)
    115             x = x.element()
    116         else:
--> 117             x = self.domain().coordinate_vector(x)
    118         v = x*self.matrix()
    119         C = self.codomain()

AttributeError: 'ModularSymbolsSubspace' object has no attribute 'coordinate_vector'
```

Issue created by migration from https://trac.sagemath.org/ticket/4284





---

archive/issue_comments_031286.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-17T09:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4284#issuecomment-31286",
    "user": "https://github.com/craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_031287.json:
```json
{
    "body": "Attachment [trac-4284.patch](tarball://root/attachments/some-uuid/ticket4284/trac-4284.patch) by @craigcitro created at 2008-10-17 09:47:11\n\nYep, this just wasn't tested at all. Fixed it, added some doctests.",
    "created_at": "2008-10-17T09:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4284#issuecomment-31287",
    "user": "https://github.com/craigcitro"
}
```

Attachment [trac-4284.patch](tarball://root/attachments/some-uuid/ticket4284/trac-4284.patch) by @craigcitro created at 2008-10-17 09:47:11

Yep, this just wasn't tested at all. Fixed it, added some doctests.



---

archive/issue_comments_031288.json:
```json
{
    "body": "Changing assignee from citro to @craigcitro.",
    "created_at": "2008-10-17T09:47:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4284#issuecomment-31288",
    "user": "https://github.com/craigcitro"
}
```

Changing assignee from citro to @craigcitro.



---

archive/issue_comments_031289.json:
```json
{
    "body": "Looks good!",
    "created_at": "2008-10-17T13:10:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4284#issuecomment-31289",
    "user": "https://github.com/williamstein"
}
```

Looks good!



---

archive/issue_comments_031290.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T09:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4284#issuecomment-31290",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031291.json:
```json
{
    "body": "Merged in Sage 3.2.alpha0",
    "created_at": "2008-10-18T09:29:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4284",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4284#issuecomment-31291",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha0



---

archive/issue_events_009678.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-10-18T09:29:31Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4284",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4284#event-9678"
}
```
