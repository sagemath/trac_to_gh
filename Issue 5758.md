# Issue 5758: weird "hello" bug in homset coerce!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-04-11 18:03:27

Assignee: robertwb

CC:  robertwb

With a 100% clean sage-3.4.1.rc2:


```
wstein`@`sage:~/build/sage-3.4.1.rc2$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: ref
sage: Zmod(8).lift() == 1
init_coerce() for  <class 'sage.categories.homset.Homset'>
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |
/scratch/wstein/sage/temp/sage.math.washington.edu/4833/_scratch_wstein_sage_init_sage_0.py in <module>()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/rings/integer.so in sage.rings.integer.Integer.__richcmp__ (sage/rings/integer.c:7457)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.Element._richcmp (sage/structure/element.c:5714)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.canonical_coercion (sage/structure/coerce.c:7434)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.coercion_maps (sage/structure/coerce.c:9262)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/coerce.so in sage.structure.coerce.CoercionModel_cache_maps.discover_coercion (sage/structure/coerce.c:11046)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.coerce_map_from (sage/structure/parent.c:9337)()

/scratch/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.init_coerce (sage/structure/parent.c:3085)()

ZeroDivisionError: hello
```




---

Comment by was created at 2009-04-11 18:07:41

NOTE: When this is fixed, be sure to add this test to rings/morphism.pyx:

```
sage: Zmod(8).lift() == 1
False
```


See #5756.


---

Comment by mabshoff created at 2009-04-13 03:39:53

Bouncing to 3.4.2.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-07-21 21:16:51

The cuplrit here is in parent.pyx, 

```
    cdef int init_coerce(self, bint warn=True) except -1:
        if self._coerce_from_hash is None:
            if warn:
                print "init_coerce() for ", type(self)
                raise ZeroDivisionError, "hello"
        ...
```

I'm attaching a patch which I think fixes the problem, but maybe someone familiar with the coercion code should take a look.  (It's a one-line patch, plus the doctest that William requested.)


---

Attachment

Looks good to me.


---

Comment by mvngu created at 2009-09-09 05:09:53

Resolution: fixed
