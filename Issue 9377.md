# Issue 9377: unable to coerce matrix over finite field into magma

Issue created by migration from https://trac.sagemath.org/ticket/9377

Original creator: mariah

Original creation time: 2010-06-29 18:16:05

Assignee: somebody


```
sage: F.<a>=GF(4)
sage: m=matrix(2,[F(1),2,3,4])
sage: magma(m) 
---------------------------------------------------------------------------
TypeError  
...
TypeError: unable to coerce element into magma
```



---

Comment by klee created at 2010-06-30 06:07:39

I investigated a little bit. 


sage: m._magma_init_(Magma()) 
  --------------------------------------------------------------------------- 
 AttributeError                            Traceback (most recent  call 
 last) 
 ... 
 AttributeError: 'FiniteField_givaro' object has no attribute 
 '_element_poly_repr' 


The version of Magma on my system is "V2.16-6".


---

Comment by klee created at 2010-06-30 06:07:39

Changing priority from major to minor.


---

Attachment


---

Comment by klee created at 2010-07-10 03:30:20

The problem was with the finite field givaro implementation.


---

Comment by klee created at 2010-07-10 03:30:20

Changing status from new to needs_review.


---

Comment by mariah created at 2010-07-12 19:25:00

Changing status from needs_review to needs_work.


---

Comment by mariah created at 2010-07-12 19:25:00


```
Using magma-2.16-11, I get the following with this patch

eno% ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: F.<a>=GF(4)
sage: m=matrix(2,[F(1),2,3,4])
sage: magma(m)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
| Sage Version 4.4.4.1, Release Date: 2010-06-28                     |
| Type notebook() for the GUI, and license() for information.        |
/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/<ipython console> in <module>()

/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/local/lib/python2.6/site-packages/sage/interfaces/magma.pyc in __call__(self, x, gens)
    735             pass
    736         
--> 737         A = Expect.__call__(self, x)
    738         if has_cache:
    739             x._magma_cache[self] = A
   1034             return self._coerce_from_special_method(x)

/home/mariah/sage/sage-4.4.4.1-x86_64-Linux-core2-fc-trac9377/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1449             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1450                 self._session_number = -1
-> 1451                 raise TypeError, x
   1452         self._session_number = parent._session_number
   1453 

TypeError: Error evaluating Magma code.
IN:_sage_[7]:=_sage_[3]![_sage_[4]!(1),_sage_[4]!(0),_sage_[4]!(1),_sage_[4]!(0)];
OUT:
>> _sage_[7]:=_sage_[3]![_sage_[4]!(1),_sage_[4]!(0),_sage_[4]!(1),_sage_[4]!(
                       ^
Runtime error in '!': Cannot coerce sequence element 1 into the coefficient ring

sage: 
```



---

Attachment

contains the previous patch and more


---

Comment by klee created at 2010-07-13 02:01:21

Sorry for the incomplete patch. The revised patch fixes another bug in Sage that caused the error.


---

Comment by klee created at 2010-07-13 02:01:21

Changing status from needs_work to needs_review.


---

Comment by mariah created at 2010-07-13 19:15:51

The revised patch fixes the reported problem.

sage-4.4.4.1 with the revised patch passes all tests when I do "make testlong"

sage-4.4.4.1 with the revised patch and using magma-2.16-11 has
fewer doctest failures when I do 

```
./sage -t -only_optional=magma devel/sage/sage 
```

than without the patch - and no new failures were introduced.

Positive review!


---

Comment by mariah created at 2010-07-13 19:15:51

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-22 08:21:35

Merged trac#9377_revised.patch in 4.5.2.alpha1.


---

Comment by ddrake created at 2010-07-22 08:21:35

Resolution: fixed
