# Issue 8699: allow doctest coverage script to handle triple single quotes

archive/issues_008699.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  jhpalmieri was\n\nAs the subject says. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/54de5b70bc7b18e3) thread for some background information.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8699\n\n",
    "created_at": "2010-04-17T05:37:54Z",
    "labels": [
        "doctest coverage",
        "minor",
        "enhancement"
    ],
    "title": "allow doctest coverage script to handle triple single quotes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8699",
    "user": "mvngu"
}
```
Assignee: tbd

CC:  jhpalmieri was

As the subject says. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/54de5b70bc7b18e3) thread for some background information.

Issue created by migration from https://trac.sagemath.org/ticket/8699





---

archive/issue_comments_079253.json:
```json
{
    "body": "Attachment [trac_8699-documentation.patch](tarball://root/attachments/some-uuid/ticket8699/trac_8699-documentation.patch) by mvngu created at 2010-04-17 10:06:06",
    "created_at": "2010-04-17T10:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79253",
    "user": "mvngu"
}
```

Attachment [trac_8699-documentation.patch](tarball://root/attachments/some-uuid/ticket8699/trac_8699-documentation.patch) by mvngu created at 2010-04-17 10:06:06



---

archive/issue_comments_079254.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-17T10:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79254",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079255.json:
```json
{
    "body": "Attachment [trac_8699-single-quotes.patch](tarball://root/attachments/some-uuid/ticket8699/trac_8699-single-quotes.patch) by mvngu created at 2010-04-17 10:53:17\n\nThe two patches on this ticket provide documentation for the doctest coverage script, in addition to allowing that script to handle docstrings that are delimited by triple single quotes. Incidentally, using those patches I found that throughout the whole Sage library, only one method uses triple single quotes. The method in question is `BubbleSortGraph()` of the module `sage.graphs.graph_generators.py`. This means that for the 90% doctest coverage goal of Sage 5.0, we have one less method to document because it's already documented. See the following command line transcript:\n\n\n```sh\n[mvngu@sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverageall > coverage-before.log\n[mvngu@sage sage-4.4.alpha0-8699-quotes]$ cd local/bin/\n[mvngu@sage bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8699/trac_8699-documentation.patch && hg qpush \nadding trac_8699-documentation.patch to series file\napplying trac_8699-documentation.patch\nnow at: trac_8699-documentation.patch\n[mvngu@sage bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8699/trac_8699-single-quotes.patch && hg qpush \nadding trac_8699-single-quotes.patch to series file\napplying trac_8699-single-quotes.patch\nnow at: trac_8699-single-quotes.patch\n[mvngu@sage bin]$ cd ../..\n[mvngu@sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverageall > coverage-after.log\n[mvngu@sage sage-4.4.alpha0-8699-quotes]$ diff -Naur coverage-before.log coverage-after.log \n--- coverage-before.log\t2010-04-17 03:37:50.663727239 -0700\n+++ coverage-after.log\t2010-04-17 03:38:45.181442502 -0700\n@@ -381,7 +381,7 @@\n geometry/polytope.py: 27% (6 of 22)\n geometry/polyhedra.py: 100% (186 of 186)\n graphs/graph_bundle.py: 100% (5 of 5)\n-graphs/graph_generators.py: 98% (73 of 74)\n+graphs/graph_generators.py: 100% (74 of 74)\n graphs/planarity.pyx: 100% (1 of 1)\n graphs/graph_latex.py: 100% (10 of 10)\n graphs/schnyder.py: 100% (8 of 8)\n@@ -1185,6 +1185,6 @@\n \n Overall weighted coverage score:  81.6%\n Total number of functions:  25377\n-We need  852 more function to get to 85% coverage.\n-We need 2121 more function to get to 90% coverage.\n-We need 3390 more function to get to 95% coverage.\n+We need  851 more function to get to 85% coverage.\n+We need 2120 more function to get to 90% coverage.\n+We need 3388 more function to get to 95% coverage.\n```\n",
    "created_at": "2010-04-17T10:53:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79255",
    "user": "mvngu"
}
```

Attachment [trac_8699-single-quotes.patch](tarball://root/attachments/some-uuid/ticket8699/trac_8699-single-quotes.patch) by mvngu created at 2010-04-17 10:53:17

The two patches on this ticket provide documentation for the doctest coverage script, in addition to allowing that script to handle docstrings that are delimited by triple single quotes. Incidentally, using those patches I found that throughout the whole Sage library, only one method uses triple single quotes. The method in question is `BubbleSortGraph()` of the module `sage.graphs.graph_generators.py`. This means that for the 90% doctest coverage goal of Sage 5.0, we have one less method to document because it's already documented. See the following command line transcript:


```sh
[mvngu@sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverageall > coverage-before.log
[mvngu@sage sage-4.4.alpha0-8699-quotes]$ cd local/bin/
[mvngu@sage bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8699/trac_8699-documentation.patch && hg qpush 
adding trac_8699-documentation.patch to series file
applying trac_8699-documentation.patch
now at: trac_8699-documentation.patch
[mvngu@sage bin]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8699/trac_8699-single-quotes.patch && hg qpush 
adding trac_8699-single-quotes.patch to series file
applying trac_8699-single-quotes.patch
now at: trac_8699-single-quotes.patch
[mvngu@sage bin]$ cd ../..
[mvngu@sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverageall > coverage-after.log
[mvngu@sage sage-4.4.alpha0-8699-quotes]$ diff -Naur coverage-before.log coverage-after.log 
--- coverage-before.log	2010-04-17 03:37:50.663727239 -0700
+++ coverage-after.log	2010-04-17 03:38:45.181442502 -0700
@@ -381,7 +381,7 @@
 geometry/polytope.py: 27% (6 of 22)
 geometry/polyhedra.py: 100% (186 of 186)
 graphs/graph_bundle.py: 100% (5 of 5)
-graphs/graph_generators.py: 98% (73 of 74)
+graphs/graph_generators.py: 100% (74 of 74)
 graphs/planarity.pyx: 100% (1 of 1)
 graphs/graph_latex.py: 100% (10 of 10)
 graphs/schnyder.py: 100% (8 of 8)
@@ -1185,6 +1185,6 @@
 
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

archive/issue_comments_079256.json:
```json
{
    "body": "attachment:trac_8699-documentation.patch works as advertised, but I believe attachment:trac_8699-single-quotes.patch will choke on something like this:\n\n\n```\ndef foo():\n   '''\n   foobarbaz\n   \"\"\"\n\n   \"\"\"\n   [..]\n   bar baz\n   '''\n   pass\n```\n",
    "created_at": "2010-04-18T08:07:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79256",
    "user": "timdumol"
}
```

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

archive/issue_comments_079257.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-18T08:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79257",
    "user": "timdumol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079258.json:
```json
{
    "body": "Replying to [comment:6 timdumol]:\n> attachment:trac_8699-documentation.patch works as advertised, but I believe attachment:trac_8699-single-quotes.patch will choke on something like this:\n\nI don't think I understand your test case. Say I put your test case in a module, e.g. devel/sage-main/sage/graphs/graph_generators.py:\n\n```diff\n[mvngu@sage sage-main]$ hg diff\ndiff --git a/sage/graphs/graph_generators.py b/sage/graphs/graph_generators.py\n--- a/sage/graphs/graph_generators.py\n+++ b/sage/graphs/graph_generators.py\n@@ -168,6 +168,17 @@\n from   math import sin, cos, pi\n from sage.misc.randstate import current_randstate\n \n+def foo():\n+   '''\n+   foobarbaz\n+   \"\"\"\n+\n+   \"\"\"\n+   [..]\n+   bar baz\n+   '''\n+   pass\n+\n class GraphGenerators():\n     r\"\"\"\n     A class consisting of constructors for several common graphs, as\n```\n\n\nRunning the doctest coverage script over this modified module reported the following:\n\n\n```sh\n[mvngu@sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverage devel/sage-main/sage/graphs/graph_generators.py \n----------------------------------------------------------------------\ndevel/sage-main/sage/graphs/graph_generators.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE devel/sage-main/sage/graphs/graph_generators.py: 98% (74 of 75)\n\nMissing doctests:\n\t * foo():\n\n----------------------------------------------------------------------\n```\n\n\nSo we have added another function, which is missing doctests. Or do you mean that the coverage script needs to ensure a balance of triple single/double quotes? In that case, I think a decent text editor that supports Python/Cython syntax would do a better job to highlight if we have, say, a triple single quotes for starting a docstring but triple double quotes to end the docstring.",
    "created_at": "2010-04-18T09:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79258",
    "user": "mvngu"
}
```

Replying to [comment:6 timdumol]:
> attachment:trac_8699-documentation.patch works as advertised, but I believe attachment:trac_8699-single-quotes.patch will choke on something like this:

I don't think I understand your test case. Say I put your test case in a module, e.g. devel/sage-main/sage/graphs/graph_generators.py:

```diff
[mvngu@sage sage-main]$ hg diff
diff --git a/sage/graphs/graph_generators.py b/sage/graphs/graph_generators.py
--- a/sage/graphs/graph_generators.py
+++ b/sage/graphs/graph_generators.py
@@ -168,6 +168,17 @@
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
[mvngu@sage sage-4.4.alpha0-8699-quotes]$ ./sage -coverage devel/sage-main/sage/graphs/graph_generators.py 
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

archive/issue_comments_079259.json:
```json
{
    "body": "I realize that test case is wrong. Here's what I meant:\n\nInserting this:\n\n\n```python\n\ndef foo():\n   '''\n   foobarbaz\n   \"\"\"\n\n   \"\"\"\n   [..]\n   \n   EXAMPLES::\n\n      sage: print 5\n      5\n   '''\n   pass\n```\n\n\ninto a file will result in a missing doctests warning, despite the fact that it does have a doctest. This is because the first triple single quote is matched with the first triple double quote, instead of the second triple single quote. It may be an extremely unlikely test case, but it is probably better to get this right now rather than puzzle over it in the far future.",
    "created_at": "2010-04-18T09:34:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79259",
    "user": "timdumol"
}
```

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

archive/issue_comments_079260.json:
```json
{
    "body": "Also, isn't there an issue if qd1 and qs1 are both != -1, but qd1 comes before qs1.  I think you need to use the minimum of them.",
    "created_at": "2010-04-19T07:28:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79260",
    "user": "mhansen"
}
```

Also, isn't there an issue if qd1 and qs1 are both != -1, but qd1 comes before qs1.  I think you need to use the minimum of them.



---

archive/issue_comments_079261.json:
```json
{
    "body": "Attachment [trac_8699.patch](tarball://root/attachments/some-uuid/ticket8699/trac_8699.patch) by mhansen created at 2012-04-11 05:02:10",
    "created_at": "2012-04-11T05:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79261",
    "user": "mhansen"
}
```

Attachment [trac_8699.patch](tarball://root/attachments/some-uuid/ticket8699/trac_8699.patch) by mhansen created at 2012-04-11 05:02:10



---

archive/issue_comments_079262.json:
```json
{
    "body": "Minh, I think your documentation changes are fine, but I've gone ahead and updated the second patch to work in situations where there are both double and single triple quotes.  Can you look at my patch?",
    "created_at": "2012-04-11T05:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79262",
    "user": "mhansen"
}
```

Minh, I think your documentation changes are fine, but I've gone ahead and updated the second patch to work in situations where there are both double and single triple quotes.  Can you look at my patch?



---

archive/issue_comments_079263.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2012-04-11T05:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79263",
    "user": "mhansen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079264.json:
```json
{
    "body": "Changing keywords from \"\" to \"7 years\".",
    "created_at": "2012-05-28T07:22:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79264",
    "user": "mhansen"
}
```

Changing keywords from "" to "7 years".



---

archive/issue_comments_079265.json:
```json
{
    "body": "This seems to be fixed by #14061:\n\n```\ntravis@travis-virtualbox:~/sage-5.7.beta3/devel/sage-reviews/sage$ sage -coverage test_8699.py \n----------------------------------------------------------------------\ntest_8699.py\nSCORE test_8699.py: 0% (0 of 4)\n\nMissing documentation:\n\t * foo():\n\t * bar():\n\t * baz():\n\t * correct():\n\n----------------------------------------------------------------------\n```\n\nwith #14061 applied:\n\n```\n------------------------------------------------------------------------\nSCORE test_8699.py: 50.0% (2 of 4)\n\nMissing doctests:\n     * line 1: def foo()\n     * line 12: def bar()\n\nPossibly wrong (function name doesn't occur in doctests):\n     * line 18: def baz()\n------------------------------------------------------------------------\n```\n\nMy test file:\n\n```\ndef foo():\n    '''\n    foobarbaz\n    \"\"\"\n\n    \"\"\"\n    [..]\n    bar baz\n    '''\n    pass\n\ndef bar():\n    '''\n    Fixme\n    '''\n    pass\n\ndef baz():\n    '''\n    Still working?\n    \"\"\"\n\n    \"\"\"\n    [..]\n\n    EXAMPLES::\n\n        sage: print 5\n        5\n    '''\n    pass\n\ndef correct():\n    '''\n    Although abit strange.\n    \"\"\"\n\n    \"\"\"\n    [..]\n\n    EXAMPLES::\n\n        sage: correct()\n    '''\n    pass\n```\n\n\nBest,\n\nTravis",
    "created_at": "2013-02-06T12:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79265",
    "user": "tscrim"
}
```

This seems to be fixed by #14061:

```
travis@travis-virtualbox:~/sage-5.7.beta3/devel/sage-reviews/sage$ sage -coverage test_8699.py 
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

archive/issue_comments_079266.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-28T16:02:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79266",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079267.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-03-07T08:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8699#issuecomment-79267",
    "user": "jdemeyer"
}
```

Resolution: duplicate
