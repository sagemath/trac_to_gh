# Issue 5759: bug in divides

Issue created by migration from https://trac.sagemath.org/ticket/5759

Original creator: was

Original creation time: 2009-04-11 18:37:49

Assignee: somebody


```
sage: Zmod(2)(0).divides(Zmod(2)(1))
---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/50691/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/structure/element.so in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:12423)()

/Users/wstein/build/sage-3.4.1.rc2/local/lib/python2.5/site-packages/sage/rings/integer_mod.so in sage.rings.integer_mod.IntegerMod_int.__mod__ (sage/rings/integer_mod.c:17834)()
   1867     def __mod__(IntegerMod_int self, right):
   1868         right = int(right)
-> 1869         if self.__modulus.int32 % right != 0:
   1870             raise ZeroDivisionError, "reduction modulo right not defined."
   1871         return integer_mod_ring.IntegerModRing(right)(self)

ZeroDivisionError: integer division or modulo by zero

Found by  kilian__ on irc.
```



---

Comment by kkilger created at 2009-04-11 22:10:28

Changing priority from minor to major.


---

Attachment


---

Comment by kkilger created at 2009-04-11 22:20:32

Changing assignee from somebody to was.


---

Attachment


---

Comment by was created at 2009-04-12 04:43:21

This breaks a doctest somewhere else:


```
wstein@sage:~/build/sage-3.4.1.rc2$ ./sage -t  devel/sage/sage/coding/code_constructions.py
sage -t  "devel/sage/sage/coding/code_constructions.py"
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage/sage/coding/code_constructions.py", line 530:
    sage: g.divides(f)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[6]>", line 1, in <module>
        g.divides(f)###line 530:
    sage: g.divides(f)
      File "element.pyx", line 1380, in sage.structure.element.CommutativeRingElement.divides (sage/structure/element.c:12436)
      File "parent_old.pyx", line 334, in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:5417)
      File "parent_old.pyx", line 336, in sage.structure.parent_old.Parent._coerce_c (sage/structure/parent_old.c:5186)
      File "parent.pyx", line 374, in sage.structure.parent.Parent.coerce (sage/structure/parent.c:4994)
    TypeError: no canonical coercion from Univariate Polynomial Ring in x over Finite Field in a of size 3^2 to Univariate Polynomial Ring in x over Finite Field of size 3
**********************************************************************
1 items had failures:
   1 of  14 in __main__.example_7
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_code_constructions.py
         [4.2 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/coding/code_constructions.py"
Total time for all tests: 4.2 seconds
```



---

Comment by kkilger created at 2009-04-12 14:17:28

The whole divides function is broken (nearly irreparable) with the effect that "divides" failes or gives *wrong* answers if and only if the ring is no polynomial ring or ZZ (which have their own (buggy) implementation). 

The reason is that not all commutative rings are euclidean domains and "modulo" operation does not do what it is supposed to do in general commutative rings, for example in finite integer rings: Zmod(12)(3) % Zmod(12)(4) gives Zmod(3)(0) (which is also broken, by the way). 

The only correct behaviour would be:

1. to raise a NotImplementedError in element.py and let all subclasses implemenent their own divides. 
     or:
2. define divides as "inclusion of ideals" and give errors if the subclasses can't check the inclusion of ideals. 

Also: all doctests in element.py and other files are for polynomial rings only, with the effect that many functions in SAGE fail or give *wrong* answers if the ring is no polynomial ring.  

Greetings,
Kilian.


---

Comment by cremona created at 2009-08-18 20:34:04

I would have thought that even in this generality (element of a commutative ring) it would be worth adding the following special cases:

   1. if self=1 return True
   1. if x =0 return True; else if self =0 return False
   1. if self.is_unit() return True

where in each case the test is wrapped in a try/except block so that if (for example) self.is_unit() is not implemented then it just passes.  Finally, if none of the above works then default to code as it is now.

Any individual ring where the x%self computation will not work but where there is an easy alternative direct test (such as in Integers(n)) can have their own specific implementations.
   
If there is any support for this I'm willing to try to do it.


---

Comment by cremona created at 2009-10-05 13:44:24

Note that #5347 (merged in 4.1.2.alpha2) fixes the easy cases I listed above.  We still have

```
sage: Zmod(5)(1).divides(Zmod(2)(1))
True
```

but this looks fine to me:

```

sage: Zmod(2).zero_ideal() == Zmod(2).zero_ideal()
True
sage: Zmod(2).zero_ideal() == Zmod(2).unit_ideal()
False
```


Hence the patches here need to be rebased and simplified to cater for the first one.


---

Comment by cremona created at 2009-10-05 13:48:37

In fact the original patches can be discarded since they only fixed things that have been fixed anyway in #5347.  What we do not have is a check the self and other are in "the same ring", which is not so obvious -- the simplest would be to throw an error if the parents were not identical, but that seems to harsh (it would cause 1.divides(1/2) to fail).  Better would be to coerce into a common parent first -- the sort of thing which is done for `__add___()`.


---

Comment by lftabera created at 2010-09-14 09:02:22

I add a patch to solve this problem. This patch is applied alone. Previous patches are discarded due to changes in the function during these months. See #5347

The algorithm first checks if parents coincide. If so, it runs the existing code. In other case, coerces both element to a common parent using the coercion model an runs the existing code on the coerced elements.

The patch works on 4.5.3


---

Comment by lftabera created at 2010-09-14 09:02:22

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by cremona created at 2010-10-03 15:48:44

Changing status from needs_review to positive_review.


---

Comment by cremona created at 2010-10-03 15:48:44

The patch applies fine to 4.6.alpha1, and all test pass (I tested the whole sage library on account of earlier difficulties).  No generic function can deliver everything, but this deals with simple generic cases, as the new doctests show.


---

Comment by mpatel created at 2010-10-04 02:48:22

Resolution: fixed
