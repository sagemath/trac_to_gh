# Issue 1210: Cannot create distinct polynomial rings over p-adic rings with different print_modes

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-11-19 21:54:44

Assignee: roed

Keywords: polynomial p-adic print mode cache caching

The issue is in the caching:


```
sage: R = Qp(7, print_mode='val-unit')
sage: S = Qp(7)
sage: R(7^2 + 1)
7^2 * 1 + O(7^22)
sage: S(7^2)
7^2 + O(7^22)
sage: R(7^2 + 1)
50 + O(7^20)
sage: S(7^2 + 1)
1 + 7^2 + O(7^20)
sage: R is S
False
sage: R['x'] is S['x']
True
```

The issue manifests itself in polynomial_ring_constructor, which fails because the cache is keyed by ==, not identity, and

```
sage: R == S
True
```



---

Attachment


---

Attachment

Use this one instead


---

Comment by ncalexan created at 2009-01-24 22:04:40

I have lots of doctest failures... wrong versions?  The argument "print_pos" does not appear anywhere in my sage/rings/padics directory, btw.


```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: nca
sage: import sage_emacs as emacs
sage: R = Qp(7, print_mode='digits', print_pos=True)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 3.3.alpha0, Release Date: 2009-01-19                  |
| Type notebook() for the GUI, and license() for information.        |
/home/ncalexan/.sage/temp/sage.math.washington.edu/16970/_home_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:579)()
    106 
    107 
--> 108 
    109 
    110 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.create_key_and_extra_args (sage/structure/factory.c:1373)()
    193 
    194 
--> 195 
    196 
    197 

TypeError: create_key() got an unexpected keyword argument 'print_pos'
sage: S = Qp(7, print_mode='digits', print_pos=False)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/ncalexan/.sage/temp/sage.math.washington.edu/16970/_home_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.__call__ (sage/structure/factory.c:579)()
    106 
    107 
--> 108 
    109 
    110 

/scratch/nca/sage-3.3.alpha1-sage.math-only-x86_64-Linux/local/lib/python2.5/site-packages/sage/structure/factory.so in sage.structure.factory.UniqueFactory.create_key_and_extra_args (sage/structure/factory.c:1373)()
    193 
    194 
--> 195 
    196 
    197 

TypeError: create_key() got an unexpected keyword argument 'print_pos'
sage: 
```



---

Comment by mabshoff created at 2009-04-15 03:21:38

David, Nick: Has this problem been fixed due to the work by David merged in 3.4.1.rc3?

Cheers,

Michael


---

Comment by kedlaya created at 2009-05-20 21:42:11

Replying to [comment:3 mabshoff]:
> David, Nick: Has this problem been fixed due to the work by David merged in 3.4.1.rc3?
> 
> Cheers,
> 
> Michael

It would appear so. Consider:

```
sage: R = Qp(7, print_mode='val-unit')
sage: S = Qp(7)
sage: R(7^2 + 1)
7^2 * 1 + O(7^22)
sage: S(7^2)
7^2 + O(7^22)
sage: R(7^2 + 1)
50 + O(7^20)
sage: S(7^2 + 1)
1 + 7^2 + O(7^20)
sage: R is S
False
sage: R['x'] is S['x']
False # this is now fixed
sage: R['x'](7^2)
(7^2 * 1 + O(7^22))
sage: S['x'](7^2)
(7^2 + O(7^22))
sage: R['x'](7^2+1)
(50 + O(7^20))
sage: S['x'](7^2+1)
(1 + 7^2 + O(7^20))
```

However, this is still puzzling:

```
sage: R['x'] == S['x']
False
```



---

Comment by tscrim created at 2013-04-10 23:09:47

I get with `5.9.beta1`:

```
sage: sage: R = Qp(7, print_mode='val-unit')
sage: sage: S = Qp(7)
sage: R is S
False
sage: R == S
False
sage: R['x'] == S['x']
False
sage: R['x'] is S['x']
False
```

which is the expected behavior due to `UniqueRepresentation` parents.


---

Comment by tscrim created at 2013-04-10 23:09:47

Changing status from needs_work to needs_review.


---

Comment by aapitzsch created at 2014-03-09 22:43:55

Replying to [comment:5 tscrim]:
> I get with `5.9.beta1`:
> {{{
> sage: sage: R = Qp(7, print_mode='val-unit')
> sage: sage: S = Qp(7)
> sage: R is S
> False
> sage: R == S
> False
> sage: R['x'] == S['x']
> False
> sage: R['x'] is S['x']
> False
> }}}
> which is the expected behavior due to `UniqueRepresentation` parents.

It should be due to `UniqueFactory` (in `6.2.beta3`). But anyway, documentation of `Qp` says 

```
PRINTING:

    There are many different ways to print `p`-adic elements.
    ...
    Note that the printing options affect whether different
    `p`-adic fields are considered equal.
```



---

Comment by aapitzsch created at 2014-03-09 22:43:55

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-03-11 14:04:15

Resolution: fixed
