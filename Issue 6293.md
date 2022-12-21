# Issue 6293: conjugacy_classes_representatives is missing in AbelianGroup

Issue created by migration from Trac.

Original creator: jlefebvre

Original creation time: 2009-06-15 04:14:19

Assignee: joyner

Keywords: AbelianGroup

The function conjugacy_classes_representatives isn't defined for AbelianGroup. It's possible to simply use the list of elements when G is finite, but it probably be preferable to make sure the order of the conjugacy classes is the same as in gap. Which seems to be the case, but not totally sure. This might be easier to deal with if we can more easily convert between AbelianGroup elements and gap elements, I've opened trac 6292 for this separate issue.


```
sage: G = AbelianGroup([2,2])
sage: H = gap(G)
sage: H.ConjugacyClasses()
[ ConjugacyClass( Group( [ f1, f2 ] ), <identity> of ... ), 
  ConjugacyClass( Group( [ f1, f2 ] ), f1 ), 
  ConjugacyClass( Group( [ f1, f2 ] ), f2 ), 
  ConjugacyClass( Group( [ f1, f2 ] ), f1*f2 ) ]
sage: G.list()
[1, f1, f0, f0*f1]
```

