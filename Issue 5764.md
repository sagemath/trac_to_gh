# Issue 5764: [with patch, needs review] improve doctest coverage for sageinspect.py

Issue created by migration from https://trac.sagemath.org/ticket/5764

Original creator: jhpalmieri

Original creation time: 2009-04-11 22:23:22

Assignee: jhpalmieri

As the summary says...

Unfortunately, running 'sage -coverage' on this file doesn't yield 100% because it gets confused by, for example, a string containing 'def test1' -- it thinks this is a function without a doctest.


---

Attachment

I thought this already got dealt with.  Anyways, right now doctests fail on the sagedoc.py file (and no others).

```
sage -t  devel/sage/sage/misc/sagedoc.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/misc/sagedoc.py", line 366:
    sage: format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[2]>", line 1, in <module>
        format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')###line 366:
    sage: format_search_as_html('Source', 'algebras/steenrod_algebra_element.py:        an antihomomorphism: if we call the antipode `c`, then', 'antipode antihomomorphism')
    NameError: name 'format_search_as_html' is not defined
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2-ref2/devel/sage-main/sage/misc/sagedoc.py", line 368:
    sage: format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class="math">c</span>, then', 'antipode antihomomorphism')
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-3.4.1.rc2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class="math">c</span>, then', 'antipode antihomomorphism')###line 368:
    sage: format_search_as_html('Other', 'html/en/reference/sage/algebras/steenrod_algebra_element.html:an antihomomorphism: if we call the antipode <span class="math">c</span>, then', 'antipode antihomomorphism')
    NameError: name 'format_search_as_html' is not defined
html/en/tutorial/tour_polynomial.html:<p>This creates a polynomial ring and tells Sage to use (the string)

**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_7
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2-ref2/tmp/.doctest_sagedoc.py
         [24.9 s]
sage -t  devel/sage/sage/rings/tests.py
```



---

Comment by jhpalmieri created at 2009-04-12 17:16:30

I've tried, and I just can't reproduce this doctest failure.  Well, I can, but only by failing to apply one of the patches at #5754: if I apply either both of the patches there or neither of the patches there, I don't see a doctest failure for sagedoc.py.  If I only apply the first one, I see the failure here.


---

Comment by was created at 2009-04-12 19:02:46

The problem is 100% that I forgot to apply the patches at #5754.   Thanks.   Michael, keep in mind that this ticket depends on #5754.

I think this doctest failure is caused by this patch, since you got rid of a lot of strips.

```
sage -t  devel/sage/sage/server/notebook/cell.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/cell.py", line 406:
    sage: C
Expected:
    Cell 0; in=2+3, out=20
Got:
    Cell 0; in=2+3, out=
    20
**********************************************************************
1 items had failures:
   1 of  13 in __main__.example_25
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_cell.py
         [14.3 s]
```


Here are some similar failures:

```
sage -t  devel/sage/sage/server/notebook/worksheet.py
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 326:
    sage: W.__repr__()
Expected:
    '[Cell 0; in=2+3, out=5, Cell 10; in=2+8, out=10]'
Got:
    '[Cell 0; in=2+3, out=\n5, Cell 10; in=2+8, out=\n10]'
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 2088:
    sage: W
Expected:
    [Cell 0; in=2+3, out=5, Cell 1; in=2+8, out=10]
Got:
    [Cell 0; in=2+3, out=
    5, Cell 1; in=2+8, out=
    10]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 2509:
    sage: v = W.cell_list(); v
Expected:
    [Cell 0; in=2+3, out=5, Cell 1; in=2+8, out=10]
Got:
    [Cell 0; in=2+3, out=
    5, Cell 1; in=2+8, out=
    10]
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 2511:
    sage: v[0]
Expected:
    Cell 0; in=2+3, out=5
Got:
    Cell 0; in=2+3, out=
    5
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage-ref2/sage/server/notebook/worksheet.py", line 3863:
    sage: W.cell_list()
Expected:
    [Cell 0; in=2+3, out=5]
Got:
    [Cell 0; in=2+3, out=
    5]
**********************************************************************
4 items had failures:
   1 of   7 in __main__.example_7
   1 of   8 in __main__.example_70
   2 of   7 in __main__.example_79
   1 of  11 in __main__.example_99
***Test Failed*** 5 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_worksheet.py
```



---

Comment by jhpalmieri created at 2009-04-12 19:39:23

I don't think I actually changed any code in sageinspect -- just added doctests.  I think these errors are actually caused by the patch at #5379.  That certainly gets rid of some strips, and after applying the patch here, I don't get failures, but after applying the patch there, I do.  I'm changing this one back go "needs review" and I'll mark the other as "needs work".


---

Comment by mabshoff created at 2009-04-13 03:41:05

Hmm, unless this gets reviewed soon it will probably now make it into 3.4.1, even though it seems quite an important ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-13 22:57:11

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 22:57:11

Merged in Sage 3.4.1.rc3.

Cheers,

Michael
