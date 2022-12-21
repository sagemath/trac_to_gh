# Issue 5768: improve coverage of generators.pyx

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-12 01:50:32

Assignee: mabshoff

CC:  mvngu




---

Comment by was created at 2009-04-12 02:02:13

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
user:        David Roe <roed`@`math.harvard.edu>
date:        Tue Jul 29 01:24:30 2008 -0700
summary:     generators object
```


I rue the day I ever allowed a single non-doctested function into Sage.


---

Comment by kcrisman created at 2010-05-26 20:36:07

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

Comment by tscrim created at 2013-02-09 19:07:45

Quick note, it seems this file is currently in `5.7.beta3` referenced only in `structure/category_object.pyx` to handle the to-be-deprecated<sup>(tm)</sup> `ParentWithGens`. So this file might be obsolete...


---

Comment by jdemeyer created at 2016-09-01 07:07:11

This module will be completely removed in #21382.


---

Comment by jdemeyer created at 2016-09-01 07:07:11

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-09-01 07:07:27

Resolution: invalid
