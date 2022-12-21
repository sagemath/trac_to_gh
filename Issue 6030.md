# Issue 6030: Bring plot/circle.py to 100% coverage

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-05-12 16:06:29

Assignee: tba

Bring plot/circle.py to 100% coverage.


---

Attachment


---

Comment by kcrisman created at 2009-05-12 16:11:26

Brings plot/circle.py to 100% coverage and improves 3D plotting potential. 

See [http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43](http://groups.google.com/group/sage-devel/browse_thread/thread/1adac4035031b140/c36f1f8a7c8a9b43#c36f1f8a7c8a9b43) for why there is no loads(dumps()) test.


---

Comment by kcrisman created at 2009-05-12 16:11:36

Changing status from new to assigned.


---

Comment by kcrisman created at 2009-05-12 16:11:36

Changing assignee from tba to kcrisman.


---

Comment by mvngu created at 2009-05-13 03:59:00

Some doctest failures:

```
[mvngu`@`sage sage-3.4.2]$ ./sage -t -long devel/sage-6030/sage/plot/circle.py 
sage -t -long "devel/sage-6030/sage/plot/circle.py"         
**********************************************************************
File "/scratch/mvngu/sage-3.4.2/devel/sage-6030/sage/plot/circle.py", line 150:
    sage: d = c.plot3d(z=2)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sage-3.4.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sage-3.4.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sage-3.4.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[6]>", line 1, in <module>
        d = c.plot3d(z=Integer(2))###line 150:
    sage: d = c.plot3d(z=2)
      File "/scratch/mvngu/sage-3.4.2/local/lib/python2.5/site-packages/sage/plot/circle.py", line 176, in plot3d
        return Polygon(xdata, ydata, options).plot3d(z)
    TypeError: plot3d() takes exactly 1 argument (2 given)
**********************************************************************
File "/scratch/mvngu/sage-3.4.2/devel/sage-6030/sage/plot/circle.py", line 151:
    sage: d.texture.opacity
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/sage-3.4.2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/sage-3.4.2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/sage-3.4.2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[7]>", line 1, in <module>
        d.texture.opacity###line 151:
    sage: d.texture.opacity
    NameError: name 'd' is not defined
**********************************************************************
1 items had failures:
   2 of  12 in __main__.example_6
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/mvngu/sage-3.4.2/tmp/.doctest_circle.py
         [5.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage-6030/sage/plot/circle.py"
Total time for all tests: 5.3 seconds
```



---

Comment by kcrisman created at 2009-05-13 13:31:26

I should have pointed out that this patch depends on # 6023, which I mistakenly thought had been merged.  I believe that will fix both doctest failures above.

Also, I assume the same comment applies as did with # 6006 and # 6023 regarding Sphinx.


---

Comment by mabshoff created at 2009-05-13 17:19:43

No, the issue with `__init__` not showing up in the documentation will be fixed in the future, i.e. sphinx 0.6.

Cheer,s

Michael


---

Comment by mabshoff created at 2009-05-14 05:36:07

No review, no milestone 4.0 ;)

Cheers,

Michael


---

Attachment

Both depend on #6023


---

Comment by mvngu created at 2009-05-15 07:04:25

Positive review! Apply patches in the following order:
 1. `trac_6023.patch` at #6023
 1. `trac_6023-fix.patch` at #6023
 1. `trac_6030.patch`
 1. `trac_6030-fix.patch`


---

Comment by mabshoff created at 2009-05-15 07:55:23

Resolution: fixed


---

Comment by mabshoff created at 2009-05-15 07:55:23

Merged both patches in Sage 4.0.alpha0.

Cheers,

Michael
