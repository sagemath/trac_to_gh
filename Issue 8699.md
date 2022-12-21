# Issue 8699: allow doctest coverage script to handle triple single quotes

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-17 05:37:54

Assignee: tbd

CC:  jhpalmieri was

As the subject says. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/54de5b70bc7b18e3) thread for some background information.


---

Attachment


---

Comment by mvngu created at 2010-04-17 10:53:17

Changing status from new to needs_review.


---

Attachment

The two patches on this ticket provide documentation for the doctest coverage script, in addition to allowing that script to handle docstrings that are delimited by triple single quotes. Incidentally, using those patches I found that throughout the whole Sage library, only one method uses triple single quotes. The method in question is `BubbleSortGraph()` of the module `sage.graphs.graph_generators.py`. This means that for the 90% doctest coverage goal of Sage 5.0, we have one less method to document because it's already documented. See the following command line transcript:


```sh
[mvngu`@`sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverageall > coverage-before.log
[mvngu`@`sage sage-4.4.alpha0-8699-quotes]$ cd local/bin/
[mvngu`@`sage bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8699/trac_8699-documentation.patch && hg qpush 
adding trac_8699-documentation.patch to series file
applying trac_8699-documentation.patch
now at: trac_8699-documentation.patch
[mvngu`@`sage bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8699/trac_8699-single-quotes.patch && hg qpush 
adding trac_8699-single-quotes.patch to series file
applying trac_8699-single-quotes.patch
now at: trac_8699-single-quotes.patch
[mvngu`@`sage bin]$ cd ../..
[mvngu`@`sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverageall > coverage-after.log
[mvngu`@`sage sage-4.4.alpha0-8699-quotes]$ diff -Naur coverage-before.log coverage-after.log 
--- coverage-before.log	2010-04-17 03:37:50.663727239 -0700
+++ coverage-after.log	2010-04-17 03:38:45.181442502 -0700
`@``@` -381,7 +381,7 `@``@`
 geometry/polytope.py: 27% (6 of 22)
 geometry/polyhedra.py: 100% (186 of 186)
 graphs/graph_bundle.py: 100% (5 of 5)
-graphs/graph_generators.py: 98% (73 of 74)
+graphs/graph_generators.py: 100% (74 of 74)
 graphs/planarity.pyx: 100% (1 of 1)
 graphs/graph_latex.py: 100% (10 of 10)
 graphs/schnyder.py: 100% (8 of 8)
`@``@` -1185,6 +1185,6 `@``@`
 
 Overall weighted coverage score:  81.6%
 Total number of functions:  25377
-We need  852 more function to get to 85% coverage.
-We need 2121 more function to get to 90% coverage.
-We need 3390 more function to get to 95% coverage.
+We need  851 more function to get to 85% coverage.
+We need 2120 more function to get to 90% coverage.
+We need 3388 more function to get to 95% coverage.
```



---

Comment by timdumol created at 2010-04-18 08:07:15

attachment:trac_8699-documentation.patch works as advertised, but I believe attachment:trac_8699-single-quotes.patch will choke on something like this:


```
def foo():
   '''
   foobarbaz
   """

   """
   [..]
   bar baz
   '''
   pass
```



---

Comment by timdumol created at 2010-04-18 08:10:00

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-04-18 09:10:41

Replying to [comment:6 timdumol]:
> attachment:trac_8699-documentation.patch works as advertised, but I believe attachment:trac_8699-single-quotes.patch will choke on something like this:

I don't think I understand your test case. Say I put your test case in a module, e.g. devel/sage-main/sage/graphs/graph_generators.py:

```diff
[mvngu`@`sage sage-main]$ hg diff
diff --git a/sage/graphs/graph_generators.py b/sage/graphs/graph_generators.py
--- a/sage/graphs/graph_generators.py
+++ b/sage/graphs/graph_generators.py
`@``@` -168,6 +168,17 `@``@`
 from   math import sin, cos, pi
 from sage.misc.randstate import current_randstate
 
+def foo():
+   '''
+   foobarbaz
+   """
+
+   """
+   [..]
+   bar baz
+   '''
+   pass
+
 class GraphGenerators():
     r"""
     A class consisting of constructors for several common graphs, as
```


Running the doctest coverage script over this modified module reported the following:


```sh
[mvngu`@`sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverage devel/sage-main/sage/graphs/graph_generators.py 
----------------------------------------------------------------------
devel/sage-main/sage/graphs/graph_generators.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-main/sage/graphs/graph_generators.py: 98% (74 of 75)

Missing doctests:
	 * foo():

----------------------------------------------------------------------
```


So we have added another function, which is missing doctests. Or do you mean that the coverage script needs to ensure a balance of triple single/double quotes? In that case, I think a decent text editor that supports Python/Cython syntax would do a better job to highlight if we have, say, a triple single quotes for starting a docstring but triple double quotes to end the docstring.


---

Comment by timdumol created at 2010-04-18 09:34:23

I realize that test case is wrong. Here's what I meant:

Inserting this:


```python

def foo():
   '''
   foobarbaz
   """

   """
   [..]
   
   EXAMPLES::

      sage: print 5
      5
   '''
   pass
```


into a file will result in a missing doctests warning, despite the fact that it does have a doctest. This is because the first triple single quote is matched with the first triple double quote, instead of the second triple single quote. It may be an extremely unlikely test case, but it is probably better to get this right now rather than puzzle over it in the far future.


---

Comment by mhansen created at 2010-04-19 07:28:47

Also, isn't there an issue if qd1 and qs1 are both != -1, but qd1 comes before qs1.  I think you need to use the minimum of them.


---

Attachment


---

Comment by mhansen created at 2012-04-11 05:03:55

Minh, I think your documentation changes are fine, but I've gone ahead and updated the second patch to work in situations where there are both double and single triple quotes.  Can you look at my patch?


---

Comment by mhansen created at 2012-04-11 05:03:55

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2012-05-28 07:22:04

Changing keywords from "" to "7 years".


---

Comment by tscrim created at 2013-02-06 12:55:17

This seems to be fixed by #14061:

```
travis`@`travis-virtualbox:~/sage-5.7.beta3/devel/sage-reviews/sage$ sage -coverage test_8699.py 
----------------------------------------------------------------------
test_8699.py
SCORE test_8699.py: 0% (0 of 4)

Missing documentation:
	 * foo():
	 * bar():
	 * baz():
	 * correct():

----------------------------------------------------------------------
```

with #14061 applied:

```
------------------------------------------------------------------------
SCORE test_8699.py: 50.0% (2 of 4)

Missing doctests:
     * line 1: def foo()
     * line 12: def bar()

Possibly wrong (function name doesn't occur in doctests):
     * line 18: def baz()
------------------------------------------------------------------------
```

My test file:

```
def foo():
    '''
    foobarbaz
    """

    """
    [..]
    bar baz
    '''
    pass

def bar():
    '''
    Fixme
    '''
    pass

def baz():
    '''
    Still working?
    """

    """
    [..]

    EXAMPLES::

        sage: print 5
        5
    '''
    pass

def correct():
    '''
    Although abit strange.
    """

    """
    [..]

    EXAMPLES::

        sage: correct()
    '''
    pass
```


Best,

Travis


---

Comment by jdemeyer created at 2013-02-28 16:02:36

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-07 08:13:44

Resolution: duplicate
