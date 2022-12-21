# Issue 6736: spell-check all modules under sage/symbolic

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-08-11 10:54:05

Assignee: tba

As the subject says.


---

Attachment

based on Sage 4.1.1.rc2


---

Comment by mhampton created at 2009-08-11 19:30:47

Only touches documentation, and all changes seem correct.


---

Comment by mvngu created at 2009-08-12 06:40:23

Resolution: fixed


---

Comment by mvngu created at 2009-08-12 06:40:23

I had the following one-time doctest failure. It's not repeatable.

```
sage -t -long devel/sage-main/sage/graphs/graph_bundle.py
libpng error: Image width or height is zero in IHDR
**********************************************************************
File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/devel/sage-main/sage/graphs/graph_bundle.py", line 163:
    sage: B.plot()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_5[5]>", line 1, in <module>
        B.plot()###line 163:
    sage: B.plot()
      File "sage_object.pyx", line 101, in sage.structure.sage_object.SageObject.__repr__ (sage/structure/sage_object.c:1387)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py", line 873, in _repr_
        self.show()
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py", line 1360, in show
        self.save(DOCTEST_MODE_FILE, **options)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/sage/plot/plot.py", line 1683, in save
        canvas.print_figure(filename, dpi=dpi)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/matplotlib/backend_bases.py", line 1453, in print_figure
        **kwargs)
      File "/scratch/mvngu/sandbox-1/sage-4.1.1.rc2/local/lib/python/site-packages/matplotlib/backends/backend_agg.py", line 334, in print_png
        filename_or_obj, self.figure.dpi)
    RuntimeError: Error building image
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_5
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/sandbox-1/sage-4.1.1.rc2/tmp/.doctest_graph_bundle.py
	 [2.8 s]
```

