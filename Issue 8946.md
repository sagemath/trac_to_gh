# Issue 8946: Sage 4.4.2.alpha0: doctest failures in calculus/riemann.pyx due to #8479

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-05-11 03:31:51

Assignee: tbd

CC:  whuss burcin

This was reported on [sage-devel](http://groups.google.com/group/sage-devel/msg/e4472856a6b8ec53) and is due to #8479:


```sh
sage -t  -long devel/sage/sage/calculus/riemann.pyx
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/devel/sage-main/sage/calculus/riemann.pyx", line 110:
    sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)  # long time (8 sec)
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[7]>", line 1, in <module>
        m = Riemann_Map([f, hf], [hf, hfprime], RealNumber('0.5') + RealNumber('0.5')*I)  # long time (8 sec)###line 110:
    sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)  # long time (8 sec)
      File "riemann.pyx", line 176, in sage.calculus.riemann.Riemann_Map.__init__ (sage/calculus/riemann.c:1757)
        self.cps[k, i] = np.complex(fs[k](self.tk[i]))
      File "expression.pyx", line 3398, in sage.symbolic.expression.Expression.__call__ (sage/symbolic/expression.cpp:15476)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/lib/python/site-packages/sage/symbolic/callable.py", line 447, in _call_element_
        raise NotImplementedError("Numpy arrays are not supported as arguments for symbolic expressions")
    NotImplementedError: Numpy arrays are not supported as arguments for symbolic expressions
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/devel/sage-main/sage/calculus/riemann.pyx", line 325:
    sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)  # long time (8 sec)
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[12]>", line 1, in <module>
        m = Riemann_Map([f, hf], [hf, hfprime], RealNumber('0.5') + RealNumber('0.5')*I)  # long time (8 sec)###line 325:
    sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)  # long time (8 sec)
      File "riemann.pyx", line 176, in sage.calculus.riemann.Riemann_Map.__init__ (sage/calculus/riemann.c:1757)
        self.cps[k, i] = np.complex(fs[k](self.tk[i]))
      File "expression.pyx", line 3398, in sage.symbolic.expression.Expression.__call__ (sage/symbolic/expression.cpp:15476)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/lib/python/site-packages/sage/symbolic/callable.py", line 447, in _call_element_
        raise NotImplementedError("Numpy arrays are not supported as arguments for symbolic expressions")
    NotImplementedError: Numpy arrays are not supported as arguments for symbolic expressions
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/devel/sage-main/sage/calculus/riemann.pyx", line 330:
    sage: sz1 = m.get_szego(boundary=1)  # long time
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[14]>", line 1, in <module>
        sz1 = m.get_szego(boundary=Integer(1))  # long time###line 330:
    sage: sz1 = m.get_szego(boundary=1)  # long time
      File "riemann.pyx", line 348, in sage.calculus.riemann.Riemann_Map.get_szego (sage/calculus/riemann.c:4222)
        [self.tk, self.szego[boundary]]).tolist()
    IndexError: index out of bounds
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/devel/sage-main/sage/calculus/riemann.pyx", line 392:
    sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)  # long time (8 sec)
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[11]>", line 1, in <module>
        m = Riemann_Map([f, hf], [hf, hfprime], RealNumber('0.5') + RealNumber('0.5')*I)  # long time (8 sec)###line 392:
    sage: m = Riemann_Map([f, hf], [hf, hfprime], 0.5 + 0.5*I)  # long time (8 sec)
      File "riemann.pyx", line 176, in sage.calculus.riemann.Riemann_Map.__init__ (sage/calculus/riemann.c:1757)
        self.cps[k, i] = np.complex(fs[k](self.tk[i]))
      File "expression.pyx", line 3398, in sage.symbolic.expression.Expression.__call__ (sage/symbolic/expression.cpp:15476)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/lib/python/site-packages/sage/symbolic/callable.py", line 447, in _call_element_
        raise NotImplementedError("Numpy arrays are not supported as arguments for symbolic expressions")
    NotImplementedError: Numpy arrays are not supported as arguments for symbolic expressions
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/devel/sage-main/sage/calculus/riemann.pyx", line 397:
    sage: tp1 = m.get_theta_points(boundary=1)  # long time
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/sandbox/sage-4.4.2.alpha0-7665r/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[13]>", line 1, in <module>
        tp1 = m.get_theta_points(boundary=Integer(1))  # long time###line 397:
    sage: tp1 = m.get_theta_points(boundary=1)  # long time
      File "riemann.pyx", line 407, in sage.calculus.riemann.Riemann_Map.get_theta_points (sage/calculus/riemann.c:4547)
        [self.tk2, self.theta_array[boundary]]).tolist()
    IndexError: index out of bounds
```



---

Attachment


---

Comment by whuss created at 2010-05-11 08:33:10

Changing status from new to needs_review.


---

Comment by whuss created at 2010-05-11 08:33:10

The attached patch should fix the problem.

But there is another problem when applying sumbolic functions to numpy types,
which is independent of #8479. See #8949.


---

Comment by mvngu created at 2010-05-12 22:51:39

Resolution: fixed
