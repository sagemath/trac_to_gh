# Issue 4483: Add coefficient_field() method to ModularSymbols/ModularForms

archive/issues_004483.json:
```json
{
    "body": "Assignee: @craigcitro\n\nDefine a newform (up to conjugation)\n\n```\ntime nf = ModularSymbols(100,2,1).cuspidal_subspace().new_subspace().decomposition()[0]\n```\n\n`nf.coefficient_field()` -- should return the field of definition of the newform.  (This appears to be accomplished with `nf.eigenvalue(1).parent()`.  It would be nice to know that this really does give the field of definition.)\n\n`nf.degree()` -- should return the degree of the coefficient field.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4483\n\n",
    "created_at": "2008-11-09T22:43:46Z",
    "labels": [
        "component: modular forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Add coefficient_field() method to ModularSymbols/ModularForms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4483",
    "user": "https://github.com/jonhanke"
}
```
Assignee: @craigcitro

Define a newform (up to conjugation)

```
time nf = ModularSymbols(100,2,1).cuspidal_subspace().new_subspace().decomposition()[0]
```

`nf.coefficient_field()` -- should return the field of definition of the newform.  (This appears to be accomplished with `nf.eigenvalue(1).parent()`.  It would be nice to know that this really does give the field of definition.)

`nf.degree()` -- should return the degree of the coefficient field.


Issue created by migration from https://trac.sagemath.org/ticket/4483





---

archive/issue_comments_033054.json:
```json
{
    "body": "There is something like this in Sage: look at the class `Newform` in modular/modform/element.py.  It has a method `hecke_eigenvalue_field()` which returns the field of definition of the newform.  There is no `degree()` method, although that's of course easy to get at this point as `nf.hecke_eigenvalue_field().degree()`.\n\nIt remains to add such a method to modular symbols (`nf.eigenvalue(1).parent()` is indeed correct), and maybe make `coefficient_field()` an alias for `hecke_eigenvalue_field()`.",
    "created_at": "2010-01-05T11:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4483#issuecomment-33054",
    "user": "https://github.com/aghitza"
}
```

There is something like this in Sage: look at the class `Newform` in modular/modform/element.py.  It has a method `hecke_eigenvalue_field()` which returns the field of definition of the newform.  There is no `degree()` method, although that's of course easy to get at this point as `nf.hecke_eigenvalue_field().degree()`.

It remains to add such a method to modular symbols (`nf.eigenvalue(1).parent()` is indeed correct), and maybe make `coefficient_field()` an alias for `hecke_eigenvalue_field()`.



---

archive/issue_events_010138.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4483#event-10138"
}
```



---

archive/issue_events_010139.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4483#event-10139"
}
```



---

archive/issue_events_010140.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4483#event-10140"
}
```



---

archive/issue_events_010141.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4483#event-10141"
}
```



---

archive/issue_events_010142.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4483#event-10142"
}
```



---

archive/issue_events_010143.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4483#event-10143"
}
```



---

archive/issue_events_010144.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4483",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4483#event-10144"
}
```
