# Issue 6316: optional doctest failure -- surf tests fail since surf isn't included in sage anymore

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-16 14:45:27

Assignee: tbd

I think these tests should be removed.  surf isn't in sage, and it isn't even an official "optional spkg". It used to be included as a binary.  It is mostly pointless now that we have implicit 3d plotting. 


```
sage -t -long --optional devel/sage/sage/rings/polynomial/multi_polynomial_ideal.py
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py", line 565:
    sage: I.plot()          # a cone         optional - surf
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[13]>", line 1, in <module>
        I.plot()          # a cone         optional - surf###line 565:
    sage: I.plot()          # a cone         optional - surf
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 2854, in plot
        MPolynomialIdeal_singular_repr.plot(self, kwds.get("singular",singular_default))
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 581, in plot
        I.plot()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1385, in __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in function_call
        return self.new(s)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1089, in new
        return self(code)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 660, in __call__
        return SingularElement(self, type, x, False)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1109, in __init__
        raise TypeError, x
    TypeError: Singular error:
    Press q to exit from 'surf'
       ? calling `surf` failed. (the shell return the error code 32512).
    probably the executable `surf` is not found.
       ? leaving surf.lib::plot
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py", line 567:
    sage: I.plot()          # same code, from a different angle  optional - surf
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[15]>", line 1, in <module>
        I.plot()          # same code, from a different angle  optional - surf###line 567:
    sage: I.plot()          # same code, from a different angle  optional - surf
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 2854, in plot
        MPolynomialIdeal_singular_repr.plot(self, kwds.get("singular",singular_default))
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 581, in plot
        I.plot()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1385, in __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in function_call
        return self.new(s)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1089, in new
        return self(code)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 660, in __call__
        return SingularElement(self, type, x, False)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1109, in __init__
        raise TypeError, x
    TypeError: Singular error:
    Press q to exit from 'surf'
       ? calling `surf` failed. (the shell return the error code 32512).
    probably the executable `surf` is not found.
       ? leaving surf.lib::plot
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/sage/rings/polynomial/multi_polynomial_ideal.py", line 569:
    sage: I.plot()          # Steiner surface   optional - surf
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_14[17]>", line 1, in <module>
        I.plot()          # Steiner surface   optional - surf###line 569:
    sage: I.plot()          # Steiner surface   optional - surf
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 2854, in plot
        MPolynomialIdeal_singular_repr.plot(self, kwds.get("singular",singular_default))
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 581, in plot
        I.plot()
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1385, in __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1293, in function_call
        return self.new(s)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 1089, in new
        return self(code)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 660, in __call__
        return SingularElement(self, type, x, False)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/singular.py", line 1109, in __init__
        raise TypeError, x
    TypeError: Singular error:
    Press q to exit from 'surf'
       ? calling `surf` failed. (the shell return the error code 32512).
    probably the executable `surf` is not found.
       ? leaving surf.lib::plot
**********************************************************************
```



---

Comment by kcrisman created at 2012-06-01 19:03:13

See also #8973.   For some reason getting Surf available was a "high-priority" bug at Sage Days 40.5.
