# Issue 8569: Standardize the title in the categories

archive/issues_008569.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  documentation\n\nRight now there are various choices of title format in the categories files: for examples you have \"FiniteSemigroups\" but\n\"Finite Weyl Groups\". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely \"Monoids\". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link \"Monoids\" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. \n\nI think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,\nfile `finite_monoids.py` which defines category `FiniteMonoids()` should have title \"Finite Monoids\"\n\nFlorent\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8569\n\n",
    "created_at": "2010-03-21T11:11:55Z",
    "labels": [
        "component: categories",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Standardize the title in the categories",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8569",
    "user": "https://github.com/hivert"
}
```
Assignee: @nthiery

CC:  documentation

Right now there are various choices of title format in the categories files: for examples you have "FiniteSemigroups" but
"Finite Weyl Groups". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely "Monoids". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link "Monoids" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. 

I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,
file `finite_monoids.py` which defines category `FiniteMonoids()` should have title "Finite Monoids"

Florent



Issue created by migration from https://trac.sagemath.org/ticket/8569





---

archive/issue_comments_077494.json:
```json
{
    "body": "Replying to [ticket:8569 hivert]:\n> Right now there are various choices of title format in the categories files: for examples you have \"FiniteSemigroups\" but\n> \"Finite Weyl Groups\". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely \"Monoids\". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link \"Monoids\" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. \n> \n> I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,\n> file `finite_monoids.py` which defines category `FiniteMonoids()` should have title \"Finite Monoids\"\n\n\n+1.\n\nThe only issue is for how to do handle it while minimizing the conflicts with other patches.",
    "created_at": "2010-03-21T20:58:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8569#issuecomment-77494",
    "user": "https://github.com/nthiery"
}
```

Replying to [ticket:8569 hivert]:
> Right now there are various choices of title format in the categories files: for examples you have "FiniteSemigroups" but
> "Finite Weyl Groups". Even worse, files `finite_monoids.py` and `monoids.py` have the same title, namely "Monoids". As a results, in the front page http://www.sagemath.org/doc/reference/categories.html the link "Monoids" points to `finite_monoids.html` and `monoids.html` is compiled but not linked there. 
> 
> I think we should all standardize so that the title of the file is the same as the name of the category with space in it. For example,
> file `finite_monoids.py` which defines category `FiniteMonoids()` should have title "Finite Monoids"


+1.

The only issue is for how to do handle it while minimizing the conflicts with other patches.



---

archive/issue_events_020673.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8569#event-20673"
}
```



---

archive/issue_events_020674.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8569#event-20674"
}
```



---

archive/issue_events_020675.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8569#event-20675"
}
```



---

archive/issue_events_020676.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8569#event-20676"
}
```



---

archive/issue_events_020677.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8569#event-20677"
}
```



---

archive/issue_events_020678.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8569#event-20678"
}
```



---

archive/issue_events_020679.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8569",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8569#event-20679"
}
```
