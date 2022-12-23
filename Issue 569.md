# Issue 569: fix many broken --long doctests in functions/piecewise.py

Issue created by migration from https://trac.sagemath.org/ticket/569

Original creator: was

Original creation time: 2007-09-02 17:37:50

Assignee: wdjoyner

None of the following should fail:


```
sage -t --long functions/piecewise.py                       **********************************************************************
File "piecewise.py", line 954:
    sage: P = f.plot_fourier_series_partial_sum(3,pi,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_26[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 954:
    sage: P = f.plot_fourier_series_partial_sum(3,pi,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 972, in plot_fourier_series_partial_sum
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 958:
    sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_26[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 958:
    sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 972, in plot_fourier_series_partial_sum
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 992:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(3,pi,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_27[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_cesaro(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 992:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(3,pi,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1010, in plot_fourier_series_partial_sum_cesaro
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 996:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(15,pi,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_27[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_cesaro(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 996:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(15,pi,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1010, in plot_fourier_series_partial_sum_cesaro
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1030:
    sage: P = f.plot_fourier_series_partial_sum_hann(3,pi,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_hann(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 1030:
    sage: P = f.plot_fourier_series_partial_sum_hann(3,pi,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1048, in plot_fourier_series_partial_sum_hann
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1034:
    sage: P = f.plot_fourier_series_partial_sum_hann(15,pi,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_hann(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 1034:
    sage: P = f.plot_fourier_series_partial_sum_hann(15,pi,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1048, in plot_fourier_series_partial_sum_hann
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1070:
    sage: P = f.plot_fourier_series_partial_sum_filtered(3,pi,[1]*3,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_filtered(Integer(3),pi,[Integer(1)]*Integer(3),-Integer(5),Integer(5))    # long time###line 1070:
    sage: P = f.plot_fourier_series_partial_sum_filtered(3,pi,[1]*3,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1088, in plot_fourier_series_partial_sum_filtered
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1074:
    sage: P = f.plot_fourier_series_partial_sum_filtered(15,pi,[1]*15,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_filtered(Integer(15),pi,[Integer(1)]*Integer(15),-Integer(5),Integer(5))   # long time###line 1074:
    sage: P = f.plot_fourier_series_partial_sum_filtered(15,pi,[1]*15,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1088, in plot_fourier_series_partial_sum_filtered
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
4 items had failures:
   2 of  10 in __main__.example_26
   2 of  10 in __main__.example_27
   2 of  10 in __main__.example_28
   2 of  10 in __main__.example_29
***Test Failed*** 8 failures.
For whitespace errors, see the file .doctest_piecewise.py
         [53.6 s]
```



---

Comment by wdj created at 2007-09-06 00:33:29

hg patch to fix this report


---

Attachment

I had some comments here but adding the attachment deleted by remarks!
Hopefully the diff file will explain the idea. The fix was very easy.


---

Comment by was created at 2007-09-06 17:26:36

Resolution: fixed


---

Comment by was created at 2007-09-06 17:26:36

looks good
