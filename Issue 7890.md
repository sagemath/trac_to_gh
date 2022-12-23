# Issue 7890: [new] Improve conversion of GAP objects into sage objects.

Issue created by migration from https://trac.sagemath.org/ticket/7890

Original creator: jlopez

Original creation time: 2010-01-10 10:45:46

Assignee: was

As of now, certain kinds of sage objects can be converted into GAP objects, but the resulting GAP objects cannot be converted back to sage objects.

Examples of this are matrices over finite fields:


```
sage: g = matrix(GF(5),2,[1,2, -1, 1])
sage: gg = g._gap_()
sage: gg.sage()
---------------------------------------------------------------------------
NotImplementedError
```



```
sage: a = gap('E(9)')
sage: a
-E(9)^4-E(9)^7
sage: a.sage()
---------------------------------------------------------------------------
NotImplementedError  
```


Being able to translate gap field elements into sage ones would help accesing GAP character tables, and a good conversion of matrices would allow many methods to be available for matrix groups.

See this thread at sage devel for more details:
http://groups.google.com/group/sage-devel/browse_thread/thread/a04006e5da578bd


---

Comment by jlopez created at 2010-01-10 15:51:19

Added a _sage_ method in GapElement class (gap.py) that tries to convert matrices into sage matrices. This only work if the coefficient ring can be converted into a sage ring. Also, modified _matrix_ in the same class so that it tries to find a ring if none is given.


---

Comment by jlopez created at 2010-01-10 15:55:11

Changing status from new to needs_work.


---

Attachment


---

Comment by jlopez created at 2010-01-12 00:01:00

Conversion for finite and cyclotomic fields and their elements.


---

Comment by jlopez created at 2010-01-12 00:13:29

Changing status from needs_work to needs_review.


---

Attachment

The patches should be applied in order.
This provides conversion of finite fields, cyclotomic fields and their elements, as well as gap matrices.


---

Comment by jlopez created at 2010-01-12 00:26:16

Simplification of one of the previous functions


---

Attachment

Further simplifications and merging. Apply only this patch.


---

Comment by wdj created at 2010-01-12 03:06:28

Changing status from needs_review to needs_work.


---

Attachment

Last patch applied fine to sage-4.3.a0 on a 64bit ubuntu machine, but the following tests failed:


```
The following tests failed:


        sage -t  "devel/sage/sage/groups/perm_gps/permgroup.py"
        sage -t  "devel/sage/sage/structure/parent.pyx"
        sage -t  "devel/sage/sage/structure/parent_old.pyx"
        sage -t  "devel/sage/sage/misc/sagedoc.py"
        sage -t  "devel/sage/sage/misc/sage_eval.py"

```



---

Comment by was created at 2012-03-19 20:28:19

Hi Javier,

What are your intentions regarding http://trac.sagemath.org/sage_trac/ticket/7890
It seems to have got dropped over two years ago.  Now none of the patches apply to recent
versions of Sage.  I wonder if you're planning to clean this up and finish it?

 -- William


---

Comment by jlopez created at 2012-06-15 07:10:36

Hi William,

yeah, sorry about that. I changed jobs in 2010 and my whole work plan went south.
I would like to get this thing working eventually, but I don't believe the approach I was trying is a good one. The lack of types in GAP creates some ambiguity in gap elements that can have different parents and where a choice needs to be made.

Probably a better approach would be to provide an optional argument `sage_parent` to the `_sage_` function in GapElement, and then put the heavy lift into the sage parent where an ad-hoc gap-to-sage function can be defined, something like this:


```
def _sage_(self, sage_parent = None):
    if sage_parent is not None:
        return sage_parent._call_from_gap(self)
    else:
        .... # The function as it used to work

```


In this way, anyone creating a sage structure could implement their own "take an element from gap here" function rather than mess up with the interface. How does that sound?

In any case it might make sense to wait a little bit and get GAP 4.5 working first, as it seems [the representation of some objects has changed](http://www.gap-system.org/Manuals/doc/changes/chap2.html).


---

Comment by vdelecroix created at 2015-04-09 22:15:40

Hello,

With #18152, it works fine for cyclotomic elements (because I introduced a function `E` in the global namespace)

```
sage: a = gap('E(9)')
sage: a.sage()
-E(9)^4 - E(9)^7
```


Vincent


---

Comment by vdelecroix created at 2015-04-11 22:28:57

Note that with the new `libgap` the conversion works almost fine for matrices (it is converted into a list of lists instead of a matrix)

```
sage: m = matrix(GF(5), 2, [1,2,-1,1])
sage: a = m._libgap_().sage()
sage: a
[[1, 2], [4, 1]]
sage: matrix(a) == m
True
```

