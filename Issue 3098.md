# Issue 3098: doctest failure in devel/sage/sage/rings/ring.pyx

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2008-05-03 19:08:14

Assignee: was


```
File "/data2/wpalenst/sage-3.0.1.rc0/tmp/ring.py", line 879:
    sage: S.<a,b> = R.quotient_ring((x^2, y))
Exception raised:
    Traceback (most recent call last):
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_39[6]>", line 1, in <module>
        S = R.quotient_ring((x**Integer(2), y),names=('a', 'b')); (a, b,) = S._first_ngens(Integer(2))###line 879:
    sage: S.<a,b> = R.quotient_ring((x^2, y))
      File "parent_gens.pyx", line 200, in sage.structure.parent_gens.ParentWithGens._first_ngens (devel/sage/sage/structure/parent_gens.c:1377)
      File "parent_gens.pyx", line 283, in sage.structure.parent_gens.ParentWithGens.gens (devel/sage/sage/structure/parent_gens.c:1916)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py", line 496, in gen
        return self(self.__R.gen(i))
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring.py", line 404, in __call__
        return quotient_ring_element.QuotientRingElement(self, x)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py", line 74, in __init__
        self._reduce_()
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/quotient_ring_element.py", line 78, in _reduce_
        self.__rep = I.reduce(self.__rep)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1919, in reduce
        gb = self.groebner_basis()
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1835, in groebner_basis
        gb = self._groebner_basis_using_singular("groebner", *args, **kwds)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 326, in wrapper
        return func(*args, **kwds)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 312, in __exit__
        self.singular.option("set",self.o)
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 803, in option
        self.eval("option(set,%s)"%val.name())
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 423, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? unknown option `set`
       ? unknown option `sage33`
       ? error occurred in STDIN line 3: `option(set,sage33);`
**********************************************************************
File "/data2/wpalenst/sage-3.0.1.rc0/tmp/ring.py", line 884:
    sage: a == b
Exception raised:
    Traceback (most recent call last):
      File "/data2/wpalenst/sage-3.0.1.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_39[9]>", line 1, in <module>
        a == b###line 884:
    sage: a == b
    NameError: name 'a' is not defined
**********************************************************************
1 items had failures:
   2 of  10 in __main__.example_39
***Test Failed*** 2 failures.
```


Since this might be strangeness in the singular pexpect interface, I'm attaching a log file of that.


---

Attachment

Some further debugging shows that the problem here is caused by `expect._synchronize` being called while _another_ `expect._synchronize` is running. This caused the outer `_synchronize` to miss its trigger and time-out.

The inner one was called through the garbage collector calling `ExpectElement.__del__`  calling `clear()` calling `eval()` calling `_synchronize()`.


---

Attachment


---

Comment by wjp created at 2008-05-03 22:40:44

After applying this patch the doctest of `sage/schemes/generic/divisor.py` hangs with the following in the singular pexpect log:


```
> intvec sage241=. if(defined(sage220)>0){kill sage220;}
intvec sage241=. if(defined(sage220)>0){kill sage220;}
   ? error occurred in STDIN line 1059: `intvec sage241=. if(defined(sage220)>0){kill sage220;}`
   ? expected intvec-expression. type 'help intvec;'
   ? last reserved name was `intvec`
   skipping text from ` `. 
quit

Auf Wiedersehen.
```



---

Comment by wjp created at 2008-05-03 23:01:52

It looks like it just needed an extra semicolon at the end, actually. I don't have time to finish a -testall now, but pending that, positive review.


---

Attachment

With both patches applied I get four doctest failures:

```
sage -t -long devel/sage/sage/schemes/generic/algebraic_scheme.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/algebraic_scheme.py", line 374:
    sage: loads(S.dumps()) == S
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_10
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_algebraic_scheme.py
         [3.8 s]
exit code: 1024
```

And:

```
sage -t -long devel/sage/sage/rings/polynomial/polynomial_singular_interface.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/polynomial_singular_interface.py", line 330:
    sage: R(h^20) == f^20
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[11]>", line 1, in <module>
        R(h**Integer(20)) == f**Integer(20)###line 330:
    sage: R(h^20) == f^20
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 1056, in __call__
        raise TypeError, "Unable to coerce singular object"
    TypeError: Unable to coerce singular object
**********************************************************************
1 items had failures:
   1 of  12 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_polynomial_singular_interface.py
         [3.4 s]
exit code: 1024
```

And:

```
sage -t -long devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/multi_polynomial_ideal.py", line 502:
    sage: reduce(lambda Qi,Qj: Qi.intersection(Qj), [Qi for (Qi,radQi) in pd]) == I
Expected:
    True
Got:
    False
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/multi_polynomial_ideal.py", line 1886:
    sage: J.groebner_basis()
Expected:
    [x + y + z, y^2 + y*z + z^2, z^3 - 1]
Got:
    [x + y + z, x*y + x*z + y*z, y^2 + y*z + z^2, x*y*z - 1, z^3 - 1]
**********************************************************************
2 items had failures:
   1 of   8 in __main__.example_14
   1 of   9 in __main__.example_44
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_multi_polynomial_ideal.py
         [6.1 s]
exit code: 1024
```

And:

```
sage -t -long devel/sage/sage/interfaces/singular.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/singular.py", line 238:
    sage: a = singular('2')*3; a
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[59]>", line 1, in <module>
        a = singular('2')*Integer(3); a###line 238:
    sage: a = singular('2')*3; a
      File "element.pyx", line 1374, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:8544)
      File "coerce.pyx", line 265, in sage.structure.coerce.CoercionModel_cache_maps.bin_op_c (sage/structure/coerce.c:5005)
      File "coerce.pyx", line 455, in sage.structure.coerce.CoercionModel_cache_maps.get_action_c (sage/structure/coerce.c:7010)
      File "coerce.pyx", line 511, in sage.structure.coerce.CoercionModel_cache_maps.discover_action_c (sage/structure/coerce.c:7489)
      File "parent.pyx", line 213, in sage.structure.parent.Parent.get_action_c (sage/structure/parent.c:1829)
      File "parent.pyx", line 282, in sage.structure.parent.Parent.get_action_c_impl (sage/structure/parent.c:2641)
      File "parent.pyx", line 696, in sage.structure.parent._register_pair (sage/structure/parent.c:6199)
      File "parent.pyx", line 689, in sage.structure.parent.EltPair.__eq__ (sage/structure/parent.c:6049)
      File "element.pyx", line 623, in sage.structure.element.Element.__richcmp__ (sage/structure/element.c:4551)
      File "element.pyx", line 595, in sage.structure.element.Element._richcmp (sage/structure/element.c:4446)
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1257, in __cmp__
        if P.eval("%s %s %s"%(self.name(), P._lessthan_symbol(), other.name())) == P._true_symbol():
      File "/scratch/mabshoff/release-cycle/sage-3.0.1.final/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 423, in eval
        raise RuntimeError, 'Singular error:\n%s'%s
    RuntimeError: Singular error:
       ? `sage60` is not defined
       ? error occurred in STDIN line 52: `sage60 < sage60;`
**********************************************************************
1 items had failures:
   1 of  61 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mabshoff/release-cycle/sage-3.0.1.final/tmp/.doctest_singular.pyException exceptions.RuntimeError: RuntimeError('Singular error:\n   ? `sage60` is not defined\n   ? error occurred in STDIN line 36: `sage60 < sage60;`',) in 'sage.structure.parent._unregister_pair' ignored
Exception exceptions.RuntimeError: RuntimeError('Singular error:\n   ? `sage60` is not defined\n   ? error occurred in STDIN line 38: `sage60 < sage60;`',) in 'sage.structure.parent._unregister_pair' ignored

         [3.3 s]
exit code: 1024
```


Without the second semicolon patch I get hangs for some of the above tests.

This is on sage.math where the ring.pyx issue never hit me.

Cheers,

Michael


---

Attachment

apply this *after* the other patches


---

Comment by mabshoff created at 2008-05-04 17:36:56

With all three patches applied:

```
All tests passed!
Total time for all tests: 944.7 seconds
```

w00t - 3.0.1 - here we come.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-04 17:40:23

Merged in Sage 3.0.1.final. William did also test on boxen affected by the ring.pyx failure.


---

Comment by mabshoff created at 2008-05-04 17:40:23

Resolution: fixed
