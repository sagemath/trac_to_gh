# Issue 8475: Pickling of _python_object_alphabet is broken.

Issue created by migration from https://trac.sagemath.org/ticket/8475

Original creator: hivert

Original creation time: 2010-03-07 09:14:12

Assignee: hivert

Keywords: pickling nested classes

Thanks to #7448 and #8452, on can trace unpicklable class throughout sage. Here is one:

```
sage: sage: W = Words()
sage: sage: A = W._python_object_alphabet()
sage: TestSuite(A).run(verbose=True)
running ._test_pickling() . . . fail
Traceback (most recent call last):
  File "/mnt/usb1/scratch/hivert/sage-4.3.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/misc/sage_unittest.py", line 268, in run
    test_method(tester = tester)
  File "/mnt/usb1/scratch/hivert/sage-4.3.4.alpha0-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/misc/sage_unittest.py", line 484, in _test_pickling
    tester.assertEqual(loads(dumps(self._instance)), self._instance)
  File "sage_object.pyx", line 792, in sage.structure.sage_object.dumps (sage/structure/sage_object.c:8367)
PicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed
------------------------------------------------------------
The following tests failed: _test_pickling
```



---

Comment by hivert created at 2010-03-07 09:37:49

Again, this is the nested class problem. I uploaded a patch which fixes that.
I also added UniqueRepresentation to _python_object_alphabet (there seems to
be only one), hence inheriting missing equality.

Should be ready for review.


---

Comment by hivert created at 2010-03-07 09:37:49

Changing status from new to needs_review.


---

Comment by slabbe created at 2010-03-09 09:33:08

Changing status from needs_review to positive_review.


---

Comment by slabbe created at 2010-03-09 09:33:08

BEFORE:


```
sage: W = Words()
sage: A = W.alphabet()
sage: A
Python objects
sage: Z = loads(dumps(W))
sage: B = Z.alphabet()
sage: B
Python objects
sage: A is B
True
sage: W is Z
False
sage: W == Z
True
sage: loads(dumps(A))
Traceback (most recent call last):
...
PicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed
sage: loads(dumps(B))
Traceback (most recent call last):
...
PicklingError: Can't pickle <class 'sage.combinat.words.words._python_object_alphabet'>: attribute lookup sage.combinat.words.words._python_object_alphabet failed
```


AFTER with the patche applied:


```
sage: W = Words()
sage: A = W.alphabet()
sage: A
Python objects
sage: Z = loads(dumps(W))
sage: B = Z.alphabet()
sage: B
Python objects
sage: A is B
True
sage: W is Z
False
sage: W == Z
True
sage: loads(dumps(A))
Python objects
sage: loads(dumps(B))
Python objects
```



Hence, the problem described in this ticket is fixed by the patch. Moreover, all tests passed in the sage tree. Positive review.

Note to the release manager : this patch commutes with the one at #8429.


---

Comment by mvngu created at 2010-03-10 06:34:43

In the "TESTS:" section, you should saying something like:

```
TESTS:

Test that #8475 is fixed::

    <put-your-tests-here>
```

That way, you provide more context for why you are writing that test. Plus, it makes it easier to locate the relevant ticket number. I leave it up to you to modify the patch as appropriate.


---

Attachment

Replying to [comment:3 mvngu]:
> In the "TESTS:" section, you should saying something like:
> {{{
> TESTS:
> 
> Test that #8475 is fixed::
> 
>     <put-your-tests-here>
> }}}
> That way, you provide more context for why you are writing that test. Plus, it makes it easier to locate the relevant ticket number. I leave it up to you to modify the patch as appropriate.

Done. Please re-review.


---

Comment by hivert created at 2010-03-10 08:09:39

Changing status from positive_review to needs_work.


---

Comment by hivert created at 2010-03-10 08:09:49

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-03-10 10:33:57

Minh's suggestion is done. To me the patch is good for a positive review.


---

Comment by mvngu created at 2010-03-10 20:21:04

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-11 04:47:39

Resolution: fixed
