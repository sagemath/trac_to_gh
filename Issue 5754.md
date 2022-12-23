# Issue 5754: docstrings for all the interactive_constructors functions are *all* now completely broken

Issue created by migration from https://trac.sagemath.org/ticket/5754

Original creator: was

Original creation time: 2009-04-11 17:13:58

Assignee: tba

Type

```
sage: inject_on()
sage: PolynomialRing?
```


You won't get a docstring at all, which sucks.  You *should* get 

```
    Construct a finite field and inject the variables of the
    finite field to the global interactive interpreter.  Use
    inject=False to not inject the variables.  This is a wrapper
    around the following function: <<<FiniteField>>>
```

but with <<<FiniteField>>> replaced by the docstring for FiniteField.  

The problem is probably that misc/sagedoc.py contains this line:

```
            t0 = sage.server.support.get_def(x, obj)
```

and there is no function sage.server.support.get_def.




---

Comment by jhpalmieri created at 2009-04-11 17:31:11

fix + new doctests


---

Attachment

REFEREE REPORT:

The code looks great.  But it fails doctests on a clean 3.4.1.rc2 install on sage.math:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: 
Exiting SAGE (CPU time 0m0.03s, Wall time 0m0.79s).
wstein@sage:~/build/sage-3.4.1.rc2$ ./sage -t devel/sage/sage/misc/sagedoc.py
sage -t  "devel/sage/sage/misc/sagedoc.py"                  
**********************************************************************
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage/sage/misc/sagedoc.py", line 366:
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
File "/scratch/wstein/build/sage-3.4.1.rc2/devel/sage/sage/misc/sagedoc.py", line 368:
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
| Sage Version 3.4.1.rc2, Release Date: 2009-04-10                   |
| Type notebook() for the GUI, and license() for information.        |
**********************************************************************
1 items had failures:
   2 of   4 in __main__.example_7
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-3.4.1.rc2/tmp/.doctest_sagedoc.py
         [16.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/misc/sagedoc.py"
Total time for all tests: 16.4 seconds
wstein@sage:~/build/sage-3.4.1.rc2$ 
```


The rest of the Sage library testsuite passes.


---

Comment by jhpalmieri created at 2009-04-11 22:43:43

apply this on top of the other patch


---

Attachment

Here's a patch: apply on top of the other one.


---

Comment by mabshoff created at 2009-04-13 06:33:40

Resolution: fixed


---

Comment by mabshoff created at 2009-04-13 06:33:40

Merged both patches in Sage 3.4.1.rc3.

Cheers,

Michael
