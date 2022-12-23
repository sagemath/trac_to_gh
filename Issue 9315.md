# Issue 9315: Basic pickling bug in finite fields

Issue created by migration from https://trac.sagemath.org/ticket/9315

Original creator: was

Original creation time: 2010-06-22 18:58:02

Assignee: AlexGhitza

CC:  cremona


```

wstein@redhawk:~/db/modsym-2010$ sage modp.sage 
data/000000/gamma0-aplist-mod2-000002-0008-10000.sobj
data/000000/gamma0-aplist-mod2-000003-0004-10000.sobj
data/000000/gamma0-aplist-mod2-000077-0002-10000.sobj
Traceback (most recent call last):
  File "modp.py", line 57, in <module>
    go()
  File "modp.py", line 52, in go
    all(Integer(0),Integer(2))
  File "/usr/local/sage/local/lib/python2.6/site-packages/sage/parallel/decorate.py", line 101, in g
    return f(*args, **kwds)
  File "modp.py", line 48, in all
    modp(d + '/' + name, p)
  File "modp.py", line 27, in modp
    save(X, name)
  File "sage_object.pyx", line 763, in sage.structure.sage_object.save (sage/structure/sage_object.c:7999)
  File "finite_field_base.pyx", line 674, in sage.rings.finite_rings.finite_field_base.FiniteField.__reduce__ (sage/rings/finite_rings/finite_field_base.c:4937)
TypeError: 'NoneType' object is unsubscriptable
wstein@redhawk:~/db/modsym-2010$ 
```


More details to come!


---

Comment by was created at 2010-06-22 20:13:55

There is a function in finite_field_base.pyx that tries to pickle.  It has doctests but clearly can *never* actually work if run, i.e., it is never actually tested.  Here's the function:

```

    def __reduce__(self):
        """
        Used in pickling.

        EXAMPLES::

            sage: A = FiniteField(127)
            sage: A == loads(dumps(A)) # indirect doctest
            True
            sage: B = FiniteField(3^3,'b')
            sage: B == loads(dumps(B))
            True
            sage: C = FiniteField(2^16,'c')
            sage: C == loads(dumps(C))
            True
            sage: D = FiniteField(3^20,'d')
            sage: D == loads(dumps(D))
            True
        """
        return self._factory_data[0].reduce_data(self)
```


However, _factory_data is not defined anywhere else in the source code:

```
wstein@redhawk:~/build/sage-4.4.4.alpha1/devel/sage/sage/rings/finite_rings$ grep _factory_data *.pyx *.pxd
 *.py                                                                                                      
finite_field_base.pyx:        return self._factory_data[0].reduce_data(self)
```



---

Attachment


---

Comment by was created at 2010-06-23 03:04:46

Changing status from new to needs_review.


---

Comment by cremona created at 2010-07-07 12:12:43

I get this doctest failure (and no more in finite_rings):


```
sage -t  "sage/rings/finite_rings/element_ntl_gf2e.pyx"     
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1092:
    sage: f = loads(dumps(e))
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[4]>", line 1, in <module>
        f = loads(dumps(e))###line 1092:
    sage: f = loads(dumps(e))
      File "sage_object.pyx", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)
      File "element_ntl_gf2e.pyx", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)
    TypeError: __cinit__() takes at least 1 positional argument (0 given)
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1093:
    sage: e is f
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[5]>", line 1, in <module>
        e is f###line 1093:
    sage: e is f
    NameError: name 'f' is not defined
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1095:
    sage: e == f
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[6]>", line 1, in <module>
        e == f###line 1095:
    sage: e == f
    NameError: name 'f' is not defined
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1449:
    sage: loads(dumps(a)) == a
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_55[3]>", line 1, in <module>
        loads(dumps(a)) == a###line 1449:
    sage: loads(dumps(a)) == a
      File "sage_object.pyx", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)
      File "element_ntl_gf2e.pyx", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)
    TypeError: __cinit__() takes at least 1 positional argument (0 given)
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1499:
    sage: f = loads(dumps(e)) # indirect doctest
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_57[4]>", line 1, in <module>
        f = loads(dumps(e)) # indirect doctest###line 1499:
    sage: f = loads(dumps(e)) # indirect doctest
      File "sage_object.pyx", line 915, in sage.structure.sage_object.loads (sage/structure/sage_object.c:9175)
      File "element_ntl_gf2e.pyx", line 200, in sage.rings.finite_rings.element_ntl_gf2e.FiniteField_ntl_gf2e.__cinit__ (sage/rings/finite_rings/element_ntl_gf2e.cpp:3159)
    TypeError: __cinit__() takes at least 1 positional argument (0 given)
**********************************************************************
File "/home/john/sage-4.5.alpha4/devel/sage-tests/sage/rings/finite_rings/element_ntl_gf2e.pyx", line 1500:
    sage: e == f
Exception raised:
    Traceback (most recent call last):
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/john/sage-current/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_57[5]>", line 1, in <module>
        e == f###line 1500:
    sage: e == f
    NameError: name 'f' is not defined
**********************************************************************
3 items had failures:
   3 of   8 in __main__.example_40
   1 of   4 in __main__.example_55
   2 of   6 in __main__.example_57
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/john/.sage//tmp/.doctest_element_ntl_gf2e.py
	 [2.6 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  "sage/rings/finite_rings/element_ntl_gf2e.pyx"
Total time for all tests: 2.6 seconds
```



---

Comment by cremona created at 2010-07-07 12:12:43

Changing status from needs_review to needs_work.


---

Comment by cremona created at 2010-07-07 12:34:52

And a similar failure in sage/rings/polynomial/multi_polynomial_libsingular.pyx


---

Comment by was created at 2010-07-07 21:27:18

Doctesting the whole the tree: http://sage.math.washington.edu/home/wstein/build/sage-4.5.alpha4/doctest-9315.out


---

Comment by was created at 2010-08-14 02:04:28

apply only this; I updated the patch to address the issues John pointed out, and clearly document what the whole point of _factory_data is (I was confused before).


---

Comment by was created at 2010-08-14 02:04:58

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by cremona created at 2010-08-14 16:38:59

I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?

I guess that you considered this already, and that it is harder than I am suggesting.

On with the testing, anyway!


---

Comment by cremona created at 2010-08-14 16:42:46

#9409 may well be ok after this;  I will test that.


---

Comment by was created at 2010-08-14 16:45:13

Replying to [comment:8 cremona]:
> I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?
> 
> I guess that you considered this already, and that it is harder than I am suggesting.
> 

Yes, i tried for several hours to figure out how to do that and failed completely.  Obviously, if somrbody can find a way to do whatvyou propose that might be good.  But the fact is the currrent patch fixes a major bug, and nobody has suggested a better fix.

> On with the testing, anyway!


---

Comment by cremona created at 2010-08-14 17:18:29

Replying to [comment:10 was]:
> Replying to [comment:8 cremona]:
> > I am reviewing this now.   Question: is it not possible to avoid the code duplication?  Could we not have a `__reduce()__` function in the base class that could somehow detect whether or not that is appropriate to use?  Perhaps all finite fields should on creation be given a tag to say whether or not they fall under the factory framework?
> > 
> > I guess that you considered this already, and that it is harder than I am suggesting.
> > 
> 
> Yes, i tried for several hours to figure out how to do that and failed completely.  Obviously, if somrbody can find a way to do whatvyou propose that might be good.  But the fact is the currrent patch fixes a major bug, and nobody has suggested a better fix.
> 

I guessed you would have tried.


> > On with the testing, anyway!

All tests pass (sage -tp 10 -long).

Unfortunately,  this does not fix #9409.  But as it is not certain that pickling of residue fields is the issue there (though I reckon it must be) I will not delay this one on that account.


---

Comment by cremona created at 2010-08-14 17:18:29

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-08-15 17:53:37

> Unfortunately, this does not fix #9409. But as it is not certain
>  that pickling of residue fields is the issue there (though 
> I reckon it must be) I will not delay this one on that account. 

By "pickling" maybe you mean "caching"?   I didn't make any changes at all, whatsoever to caching.  The only actual change my patch makes is that the default __reduce__ method is now used when explicitly pickling residue fields.   Before pickling residue fields just resulted in a big error.   So what I do can't possibly fix any bug that wasn't very explicit before (i.e., "pickling doesn't work at all").


---

Comment by cremona created at 2010-08-15 19:18:07

Replying to [comment:12 was]:
> > Unfortunately, this does not fix #9409. But as it is not certain
> >  that pickling of residue fields is the issue there (though 
> > I reckon it must be) I will not delay this one on that account. 
> 
> By "pickling" maybe you mean "caching"?   I didn't make any changes at all, whatsoever to caching.  The only actual change my patch makes is that the default __reduce__ method is now used when explicitly pickling residue fields.   Before pickling residue fields just resulted in a big error.   So what I do can't possibly fix any bug that wasn't very explicit before (i.e., "pickling doesn't work at all").

OK, I just don't know what I am talking about.... 
>


---

Comment by mpatel created at 2010-09-15 11:13:50

Resolution: fixed
