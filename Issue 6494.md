# Issue 6494: sage should *never* ever import numpy by default on startup.  Yet again it does!

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-09 04:20:56

Assignee: mabshoff

CC:  was jason robertwb


```
.bash-3.2$ ./sage -startuptime |grep numpy
           decorators_numpy: 0.000 (IPython.testing)
             numpy: 0.073 (complex_plot)
              numpy.__config__: 0.000 (numpy)
              version: 0.000 (numpy)
              _import_tools: 0.000 (numpy)
              add_newdocs: 0.047 (numpy)
                numpy.version: 0.000 (lib)
                 numpy.core.numeric: 0.018 (type_check)
                  multiarray: 0.002 (numpy.core.numeric)
                  umath: 0.001 (numpy.core.numeric)
                   numpy.core.multiarray: 0.000 (umath)
                  _internal: 0.001 (numpy.core.numeric)
                  numerictypes: 0.002 (numpy.core.numeric)
                  _sort: 0.000 (numpy.core.numeric)
                  numeric: 0.004 (numpy.core.numeric)
                  defmatrix: 0.001 (numpy.core.numeric)
                  defchararray: 0.000 (numpy.core.numeric)
                  records: 0.001 (numpy.core.numeric)
                  memmap: 0.000 (numpy.core.numeric)
                  scalarmath: 0.001 (numpy.core.numeric)
                   numpy.core.umath: 0.000 (scalarmath)
                  numpy.testing: 0.004 (numpy.core.numeric)
                   decorators: 0.000 (numpy.testing)
                   utils: 0.003 (numpy.testing)
                   numpytest: 0.000 (numpy.testing)
                 numpy.core.numerictypes: 0.000 (index_tricks)
                  numpy.core.fromnumeric: 0.000 (function_base)
                  numpy.lib.shape_base: 0.000 (function_base)
                  numpy.lib.twodim_base: 0.000 (function_base)
                 numpy.core.defmatrix: 0.000 (index_tricks)
                 numpy.lib.type_check: 0.000 (scimath)
                 numpy.core: 0.000 (polynomial)
                 numpy.lib.getlimits: 0.001 (polynomial)
                  machar: 0.000 (numpy.lib.getlimits)
                 numpy.lib.function_base: 0.000 (polynomial)
                 numpy.linalg: 0.002 (polynomial)
                  linalg: 0.001 (numpy.linalg)
                   numpy.lib: 0.000 (linalg)
                  numpy.lib.utils: 0.000 (format)
               numpy.lib._compiled_base: 0.000 (add_newdocs)
               numpy.lib.index_tricks: 0.000 (add_newdocs)
              testing: 0.000 (numpy)
              core: 0.000 (numpy)
              fft: 0.002 (numpy)
              mtrand: 0.015 (numpy)
              ctypeslib: 0.001 (numpy)
               numpy.core._internal: 0.000 (ctypeslib)
              ma: 0.006 (numpy)
0.073 numpy (complex_plot)
```


I think this is because of the new complex_plot module, which I think I positively reviewed, so this is my fault.  To resolve this ticket, make that import sufficiently lazy.  Also, make a doctest that verifies that numpy is not imported when Sage starts up.


---

Attachment


---

Comment by mhansen created at 2010-08-26 19:35:16

Changing status from new to needs_review.


---

Comment by mhansen created at 2010-08-26 19:35:16

I don't think you can cimport numpy without causing an import in the module.  Thus, a number of things have to be lazily imported.  This will cause a problem if people do


```
sage: from sage.finance.all import TimeSeries
sage: isinstance(foo, TimeSeries)
```


since TimeSeries will be a LazyImport object rather than a class.  I'm not sure the best thing to do, but I've posted a patch anyway.


---

Comment by jason created at 2010-10-02 20:10:31

numpy recently has made great improvements in its import speed, so maybe this isn't quite the issue it used to be?


---

Comment by jdemeyer created at 2011-10-15 12:54:49

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2011-10-15 12:54:49

I'm not going to judge whether numpy imports are still an issue or not, but in any case the patch needs to be rebased:

```
patching file sage/calculus/all.py
Hunk #2 succeeded at 16 (offset 1 line).
patching file sage/finance/all.py
patching file sage/interfaces/gnuplot.py
patching file sage/plot/all.py
Hunk #2 FAILED at 21.
1 out of 2 hunks FAILED -- saving rejects to file sage/plot/all.py.rej
patching file sage/plot/plot3d/implicit_plot3d.py
Hunk #2 succeeded at 255 (offset 10 lines).
patching file sage/stats/all.py
patching file sage/stats/hmm/all.py
```



---

Comment by mhansen created at 2012-03-28 21:09:33

This ticket is invalid now as all of the changes appearing in it are already in the Sage library.


---

Comment by mhansen created at 2012-03-28 21:09:33

Resolution: invalid


---

Comment by jdemeyer created at 2012-03-28 22:44:11

You shouldn't just close tickets, leave that to the release manager.
