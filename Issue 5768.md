# Issue 5768: improve coverage of generators.pyx

archive/issues_005768.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mvngu\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5768\n\n",
    "created_at": "2009-04-12T01:50:32Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "improve coverage of generators.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5768",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  mvngu



Issue created by migration from https://trac.sagemath.org/ticket/5768





---

archive/issue_comments_045036.json:
```json
{
    "body": "This file is just scary.   The second function I tried to document is:\n\n```\n    cpdef get_from_index(self, i):\n        return self._obj._gen_(i)\n```\n\nI couldn't find any object in all of Sage with a `_gen_` method -- I see now way this could ever work.    Hence I can't see any way `Generators_naturals` would ever work.  This whole file just scares me.  I don't get it at all. \n\nI give up.\n\nThis file was evidently 100% part of this changeset:\n\n```\nchangeset:   10231:8dea97c4b4f0\nparent:      10067:717c10d9cd4a\nuser:        David Roe <roed@math.harvard.edu>\ndate:        Tue Jul 29 01:24:30 2008 -0700\nsummary:     generators object\n```\n\n\nI rue the day I ever allowed a single non-doctested function into Sage.",
    "created_at": "2009-04-12T02:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5768#issuecomment-45036",
    "user": "https://github.com/williamstein"
}
```

This file is just scary.   The second function I tried to document is:

```
    cpdef get_from_index(self, i):
        return self._obj._gen_(i)
```

I couldn't find any object in all of Sage with a `_gen_` method -- I see now way this could ever work.    Hence I can't see any way `Generators_naturals` would ever work.  This whole file just scares me.  I don't get it at all. 

I give up.

This file was evidently 100% part of this changeset:

```
changeset:   10231:8dea97c4b4f0
parent:      10067:717c10d9cd4a
user:        David Roe <roed@math.harvard.edu>
date:        Tue Jul 29 01:24:30 2008 -0700
summary:     generators object
```


I rue the day I ever allowed a single non-doctested function into Sage.



---

archive/issue_comments_045037.json:
```json
{
    "body": "Current status of that function:\n\n```\n    cpdef get_from_index(self, i):\n        \"\"\"\n        EXAMPLES:\n            sage: from sage.structure.generators import Generators_list\n            sage: gens = Generators_list(ZZ, [5,9], Rings)\n            sage: gens.get_from_index(0)\n            5\n        \"\"\"\n```\n\n\nThough still\n\n```\nSCORE /Users/.../sage-4.4.2/devel/sage/sage/structure/generators.pyx: 11% (5 of 45)\n\nMissing documentation:\n\t * __init__(self, Generators gens):\n\t * next(self):\n\t * __iter__(self):\n\t * __init__(self, obj, index_set, category):\n\t * get_from_index(self, i):\n\t * __contains__(self, x):\n\t * __call__(self, i):\n\t * __getitem__(self, i):\n\t * __iter__(self):\n\t * __len__(self):\n\t * index_set(self):\n\t * category(self):\n\t * obj(self):\n\t * count(self):\n\t * list(self):\n\t * _repr_(self):\n\t * count(self):\n\t * __cmp__(self, other_unty):\n\t * _repr_(self):\n\t * __reduce__(self):\n\t * make_finite_gens(obj, n, index_set, category):\n\t * __reduce__(self):\n\t * __cmp__(left, _right):\n\t * _repr_(self):\n\t * __init__(self, obj, category):\n\t * count(self):\n\t * __getitem__(self, i):\n\t * __init__(self, obj, category = None):\n\t * get_from_index(self, i):\n\t * __contains__(self, x):\n\t * __iter__(self):\n\t * index_set(self):\n\t * count(self):\n\t * list(self):\n\t * __init__(self, G, index_set, category, computing_function):\n\t * get_from_index(self, i):\n\t * count(self):\n\t * list(self):\n\t * _repr_(self):\n\n\nMissing doctests:\n\t * __init__(self, obj, n, index_set, category):\n\n\nPossibly wrong (function name doesn't occur in doctests):\n\t * make_list_gens(*args):\n```\n\nSo there is yet work to be done.",
    "created_at": "2010-05-26T20:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5768#issuecomment-45037",
    "user": "https://github.com/kcrisman"
}
```

Current status of that function:

```
    cpdef get_from_index(self, i):
        """
        EXAMPLES:
            sage: from sage.structure.generators import Generators_list
            sage: gens = Generators_list(ZZ, [5,9], Rings)
            sage: gens.get_from_index(0)
            5
        """
```


Though still

```
SCORE /Users/.../sage-4.4.2/devel/sage/sage/structure/generators.pyx: 11% (5 of 45)

Missing documentation:
	 * __init__(self, Generators gens):
	 * next(self):
	 * __iter__(self):
	 * __init__(self, obj, index_set, category):
	 * get_from_index(self, i):
	 * __contains__(self, x):
	 * __call__(self, i):
	 * __getitem__(self, i):
	 * __iter__(self):
	 * __len__(self):
	 * index_set(self):
	 * category(self):
	 * obj(self):
	 * count(self):
	 * list(self):
	 * _repr_(self):
	 * count(self):
	 * __cmp__(self, other_unty):
	 * _repr_(self):
	 * __reduce__(self):
	 * make_finite_gens(obj, n, index_set, category):
	 * __reduce__(self):
	 * __cmp__(left, _right):
	 * _repr_(self):
	 * __init__(self, obj, category):
	 * count(self):
	 * __getitem__(self, i):
	 * __init__(self, obj, category = None):
	 * get_from_index(self, i):
	 * __contains__(self, x):
	 * __iter__(self):
	 * index_set(self):
	 * count(self):
	 * list(self):
	 * __init__(self, G, index_set, category, computing_function):
	 * get_from_index(self, i):
	 * count(self):
	 * list(self):
	 * _repr_(self):


Missing doctests:
	 * __init__(self, obj, n, index_set, category):


Possibly wrong (function name doesn't occur in doctests):
	 * make_list_gens(*args):
```

So there is yet work to be done.



---

archive/issue_comments_045038.json:
```json
{
    "body": "Quick note, it seems this file is currently in `5.7.beta3` referenced only in `structure/category_object.pyx` to handle the to-be-deprecated<sup>(tm)</sup> `ParentWithGens`. So this file might be obsolete...",
    "created_at": "2013-02-09T19:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5768#issuecomment-45038",
    "user": "https://github.com/tscrim"
}
```

Quick note, it seems this file is currently in `5.7.beta3` referenced only in `structure/category_object.pyx` to handle the to-be-deprecated<sup>(tm)</sup> `ParentWithGens`. So this file might be obsolete...



---

archive/issue_comments_045039.json:
```json
{
    "body": "This module will be completely removed in #21382.",
    "created_at": "2016-09-01T07:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5768#issuecomment-45039",
    "user": "https://github.com/jdemeyer"
}
```

This module will be completely removed in #21382.



---

archive/issue_comments_045040.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-09-01T07:07:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5768#issuecomment-45040",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_045041.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2016-09-01T07:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5768",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5768#issuecomment-45041",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
