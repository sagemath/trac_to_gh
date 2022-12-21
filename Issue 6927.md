# Issue 6927: extend CachedFunction to handle disk-cache

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2009-09-12 23:24:42

Assignee: cwitty

CC:  was craigcitro

Keywords: cache database

The CachedFunction class is a wonderful decorator that provides cacheing of computations, unique rings, etc.  However, for any number of databases, it would be useful if the computed data was to persist between sessions.  So, we should extend the CachedFunction class to enable disk caches, too.


---

Comment by boothby created at 2009-09-12 23:27:04

Changing assignee from cwitty to boothby.


---

Comment by was created at 2009-09-12 23:36:45

Comments on the first patch:

```
yo
[4:32pm] williamstein:
Do you break pickling?  I'm curious.
[4:32pm] williamstein:
that lambda scares me.
[4:32pm] williamstein:
You could do: "stringify = lambda k: arguments_to_string(f,k) "
[4:33pm] williamstein:
via a partial function evaluation object (which is also somewhere in Python -- see ref guide) and avoid the lambda whilst making sure to not break pickling.
[4:33pm] williamstein:
Pickling would of course only be an issue if you generalize this to methods of a class.
[4:33pm] williamstein:
Oh, it could also be a problem if you say combine this with `@`parallel and multiprocessing.
[4:33pm] williamstein:
Have you tried that?
[4:34pm] williamstein:
boothby_ -- ping
[4:34pm] williamstein:
I don't like this: "if isinstance(cache, FileCache) and clear_disk_cache_too != 'yes I mean it':"
[4:34pm] williamstein:
It needs to be broken down a little more so that one gets an error if clear_disk_cache_too is true but not that string.
[4:35pm] williamstein:
As is, it is undocumented and you would never know how to use it without reading the source.
[4:36pm] williamstein:
the empty line 560 should be deleted, I think.
```



---

Comment by was created at 2009-09-19 09:31:53

I tried to apply this to a clean 4.1.2.alpha1 and got nowhere:

```
wstein`@`sage:~/build/sage-4.1.2.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
Loading Sage library. Current Mercurial branch is: referee
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/6927/6927-disk-cache.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6927/6927-disk-cache.patch
Loading: [.....]
cd "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage" && hg status
/scratch/wstein/build/sage-4.1.2.alpha1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage" && hg status
cd "/scratch/wstein/build/sage-4.1.2.alpha1/devel/sage" && hg import   "/scratch/wstein/sage/temp/sage.math.washington.edu/22785/tmp_1.patch"
applying /scratch/wstein/sage/temp/sage.math.washington.edu/22785/tmp_1.patch
unable to find 'sage/misc/function_mangling.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file sage/misc/function_mangling.py.rej
patching file sage/misc/all.py
Hunk #1 succeeded at 154 with fuzz 2 (offset 2 lines).
patching file sage/misc/all.py
Hunk #1 FAILED at 149
1 out of 1 hunks FAILED -- saving rejects to file sage/misc/all.py.rej
patching file sage/misc/cachefunc.py
Hunk #1 FAILED at 3
Hunk #2 FAILED at 13
Hunk #3 succeeded at 219 with fuzz 2 (offset 20 lines).
2 out of 4 hunks FAILED -- saving rejects to file sage/misc/cachefunc.py.rej
sage/misc/function_mangling.py: No such file or directory
abort: patch failed to apply
```

| Sage Version 4.1.2.alpha1, Release Date: 2009-09-07                |
| Type notebook() for the GUI, and license() for information.        |

Your patch contains changes to function_mangling.py, but doesn't even contain that file in the first place.


---

Comment by boothby created at 2009-09-20 04:37:56

replaces previous patch, based on #6937


---

Attachment

I'm not sure if this problem is local to this patch, but running:


```
`@`cached_function
def oddprime_factors(n):
     l = [p for p,e in factor(n) if p != 2]
     return len(l)
oddprime_factors.precompute(range(1,100), 4)
```


, which is in the doctets of `cachefunc.py`, in the Notebook throws a `NameError`:


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/deadlyx/.sage/sage_notebook/worksheets/admin/0/code/1.py", line 13, in <module>
    oddprime_factors.precompute(range(_sage_const_1 ,_sage_const_100 ), _sage_const_4 )
  File "", line 1, in <module>
    
  File "/opt/sage-bin/local/lib/python2.6/site-packages/sage/misc/cachefunc.py", line 226, in precompute
    for ((args,kwargs), val) in P(arglist):
  File "/opt/sage-bin/local/lib/python2.6/site-packages/sage/parallel/multiprocessing.py", line 66, in parallel_iter
    for res in result:
  File "/opt/sage-bin/local/lib/python2.6/site-packages/processing/pool.py", line 470, in next
    raise value
NameError: global name '_sage_const_2' is not defined
```


Running it in the command line works perfectly.

 * The paths for `FileCache` are not OS agnostic: Windows uses backslashes, instead of slashes. Using `os.sep` instead should fix it.
 * The examples in the docstrings are not properly formatted. To display them as a code block, please use the ff. format:


```

EXAMPLES::

    sage: foo()
    bar
    sage: bar()
    baz

:: # Another code block

    sage: foo()
    foo

```


Everything else seems to work well. Oh, it may be worth hashing the function being cached and adding that to the key. It should prevent problems with using the same directory for the cache folder.


---

Comment by timdumol created at 2009-11-30 07:50:06

This patch should fix the issues regarding the docstrings. The NameError is due to the implementation of `@`parallel. I am not sure if it is feasible to fix the error. In any case, this is orthogonal to this patch. Positive review so far as I can do.

Can anyone review the referee patch?


---

Comment by timdumol created at 2009-11-30 07:50:06

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2009-11-30 09:05:50

Oh, I made `multiprocessing.py` import from stdlib's `multiprocessing` instead of `processing`. It may be worth considering removing the `processing` package, since its contents are now in stdlib with the name `multiprocessing`.


---

Attachment

Fixes docstrings and OS agnosticism issues. Also changes `processing` import to stdlib's `multiprocessing`


---

Attachment

Relocate an import.  Fixed doctest failure. Rebased vs. 4.3.2.alpha0. Combined patch replaces all previous.


---

Comment by mpatel created at 2010-01-31 04:24:38

I've attached a combined, rebased patch.  I've removed

```python
        return P(arglist) 
```

from the "ref" patch.  Otherwise, the precomputed values are not cached.  Or am I mistaken?

I've also relocated

```python
from sage.structure.sage_object import save, load
```

to avoid a circular import problem with `sage -docbuild reference html -j`:

```python
Traceback (most recent call last):
  File "/home/apps/sage/devel/sage/doc/common/builder.py", line 11, in <module>
    from sage.misc.cachefunc import cached_method
  File "/home/apps/sage/local/lib/python2.6/site-packages/sage/misc/cachefunc.py", line 20, in <module>
    from sage.structure.sage_object import save, load
  File "/home/apps/sage/local/lib/python2.6/site-packages/sage/structure/__init__.py", line 1, in <module>
    import dynamic_class # allows for sage.structure.dynamic_class?
  File "/home/apps/sage/local/lib/python2.6/site-packages/sage/structure/dynamic_class.py", line 119, in <module>
    from sage.misc.cachefunc import cached_method, cached_function
ImportError: cannot import name cached_method
```


To the extent it counts, my review is positive, but someone should check the combined patch.


---

Attachment

Avoid `sage -startuptime` error.  Replaces previous.


---

Comment by mpatel created at 2010-02-03 05:48:21

V2 of the combined patch is an attempt to work around an absolute import problem with `sage -startuptime`.  Diff of the diffs:

```diff
`@``@` -639,7 +639,7 `@``@` diff --git a/sage/parallel/multiprocessi
 -from processing import Pool
 +from __future__ import absolute_import
 +
-+from multiprocessing import Pool
++import multiprocessing
  from functools import partial
  from sage.misc.fpickle import pickle_function, call_pickled_function
 -import ncpus
`@``@` -647,8 +647,12 `@``@` diff --git a/sage/parallel/multiprocessi
  
  def pyprocessing(processes=0):
      """
-`@``@` -62,7 +64,7 `@``@` def parallel_iter(processes, f, inputs):
-     p = Pool(processes)
+`@``@` -59,10 +61,10 `@``@` def parallel_iter(processes, f, inputs):
+         [(((2,), {}), 4), (((3,), {}), 6)]
+     """
+     if processes == 0: processes = ncpus.ncpus()
+-    p = Pool(processes)
++    p = multiprocessing.Pool(processes)
      fp = pickle_function(f)
```



---

Comment by timdumol created at 2010-04-18 13:43:34

Changing status from needs_review to positive_review.


---

Comment by timdumol created at 2010-04-18 13:43:34

Nice catch on `P(arglist)`, which was for debugging only. Positive review for your changes. Here's a rebase on #6927, which consists on basically removing the multiprocessing.py part.


---

Attachment

Rebase on sage-4.4.alpha0. Apply this patch only.


---

Comment by jhpalmieri created at 2010-04-19 05:20:02

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-19 05:20:02

Merged "trac_6927-disk-cache-rebase.patch" into 4.4.alpha1.


---

Comment by boothby created at 2017-01-06 21:26:49

I'm changing the author name of this patch to re-establish trust with the patchbot.
