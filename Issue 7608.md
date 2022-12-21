# Issue 7608: update Networkx to version 1.0rc1

Issue created by migration from Trac.

Original creator: ylchapuy

Original creation time: 2009-12-05 23:01:18

Assignee: rlm

CC:  ncohen rbeezer

This implies a lot of modifications in graph_backends.py to respect the new API.


---

Comment by ylchapuy created at 2009-12-05 23:12:44

Changing status from new to needs_work.


---

Comment by ylchapuy created at 2009-12-05 23:12:44

With the provided patch, all doctests in the graph/ directory pass.
I didn't tested more yet.

There is probably room for improvements, but it's a good starting point.
I leave it as needs work because it probably conflicts with many other patches...

(It also corrects a few bugs)


---

Comment by ylchapuy created at 2009-12-05 23:16:07

and the corresponding spkg con be found there:

http://yann.laiglechapuy.net/spkg/networkx-1.0rc1.p1.spkg


---

Comment by mvngu created at 2009-12-05 23:30:50

Ticket #6041 is a duplicate of this ticket.


---

Comment by wdj created at 2009-12-05 23:50:28

I installed the spkg then created a clone and applied the patch and got this:


```
jeeves:sage-4.3.alpha1 wdj$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
**********************************************************************
*                                                                    *
* Warning: this is a prerelease version, and it may be unstable.     *
*                                                                    *
**********************************************************************
WARNING: There is one major unsolved bug in some versions of
Sage on OS X 10.6 that causes an 'Abort trap' crash when
doing certain symbolic computations.
See http://trac.sagemath.org/sage_trac/ticket/7095/.
Loading Sage library. Current Mercurial branch is: 7308_networkx
sage: hg_sage.apply("/Users/wdj/sagefiles/trac_7608-Networkx_1.0rc1.patch")
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg status
/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg status
cd "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage" && hg import   "/Users/wdj/sagefiles/trac_7608-Networkx_1.0rc1.patch"
applying /Users/wdj/sagefiles/trac_7608-Networkx_1.0rc1.patch
patching file sage/graphs/graph.py
Hunk #4 FAILED at 1585
1 out of 49 hunks FAILED -- saving rejects to file sage/graphs/graph.py.rej
abort: patch failed to apply
sage: 
Exiting SAGE (CPU time 0m0.05s, Wall time 0m7.67s).
```

| Sage Version 4.3.alpha1, Release Date: 2009-12-03                  |
| Type notebook() for the GUI, and license() for information.        |
This is on an imac running 10.6.1 and sage 4.3.a1. 


Do you see the problem?


---

Comment by ylchapuy created at 2009-12-05 23:57:25

as I said, the patch is based on 4.3alpha0, on many patches on graphs have been merged since...


---

Comment by wdj created at 2009-12-06 01:44:50

Replying to [comment:5 ylchapuy]:
> as I said, the patch is based on 4.3alpha0, on many patches on graphs have been merged since...

Okay. Maybe the patch needs to be "rebased"?  I am not an expert though...


---

Comment by ylchapuy created at 2009-12-06 01:46:36

If you wait 5 minutes, you'll have the new patch.

Replying to [comment:6 wdj]:
> Replying to [comment:5 ylchapuy]:
> > as I said, the patch is based on 4.3alpha0, on many patches on graphs have been merged since...
> 
> Okay. Maybe the patch needs to be "rebased"?  I am not an expert though...


---

Comment by ylchapuy created at 2009-12-06 01:54:15

based on 4.3.alpha1


---

Attachment

patch updated, now based on 4.3alpha1.


---

Comment by ylchapuy created at 2009-12-06 01:54:58

Changing status from needs_work to needs_review.


---

Comment by ylchapuy created at 2009-12-06 01:58:40

(N.B.: the two failures in graph_generators.py are not related. They come from a missing file for patch #6813 )


---

Comment by wdj created at 2009-12-06 08:49:33

I tested this on an imac running 10.6.1, which has these failures before adding the spkg and the patch from this ticket:


```
	sage -t  "devel/sage/sage/calculus/tests.py"
	sage -t  "devel/sage/sage/calculus/wester.py"
	sage -t  "devel/sage/sage/functions/hyperbolic.py"
	sage -t  "devel/sage/sage/functions/log.py"
	sage -t  "devel/sage/sage/functions/other.py"
	sage -t  "devel/sage/sage/functions/trig.py"
	sage -t  "devel/sage/sage/graphs/graph_generators.py"
	sage -t  "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
	sage -t  "devel/sage/sage/plot/text.py"
	sage -t  "devel/sage/sage/rings/arith.py"
	sage -t  "devel/sage/sage/rings/complex_double.pyx"
	sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"
	sage -t  "devel/sage/sage/symbolic/expression.pyx"
	sage -t  "devel/sage/sage/symbolic/function.pyx"
```


Afterwards, there were these failures:


```
        sage -t  "devel/sage/sage/calculus/tests.py"
        sage -t  "devel/sage/sage/calculus/wester.py"
        sage -t  "devel/sage/sage/combinat/species/species.py"
        sage -t  "devel/sage/sage/combinat/symmetric_group_representations.py"
        sage -t  "devel/sage/sage/functions/hyperbolic.py"
        sage -t  "devel/sage/sage/functions/log.py"
        sage -t  "devel/sage/sage/functions/other.py"
        sage -t  "devel/sage/sage/functions/trig.py"
        sage -t  "devel/sage/sage/graphs/graph_generators.py"
        sage -t  "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
        sage -t  "devel/sage/sage/plot/text.py"
        sage -t  "devel/sage/sage/rings/arith.py"
        sage -t  "devel/sage/sage/rings/complex_double.pyx"
        sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"
        sage -t  "devel/sage/sage/structure/sage_object.pyx"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
        sage -t  "devel/sage/sage/symbolic/function.pyx"
```


For example,


```
jeeves:sage-4.3.alpha1 wdj$ ./sage -t  "devel/sage/sage/combinat/species/species.py"
sage -t  "devel/sage/sage/combinat/species/species.py"      
WARNING: There is one major unsolved bug in some versions of
Sage on OS X 10.6 that causes an 'Abort trap' crash when
doing certain symbolic computations.
See http://trac.sagemath.org/sage_trac/ticket/7095/.
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/species/species.py", line 667:
    sage: list(sorted(labels.items()))
Expected:
    [(Combinatorial species, 0),
     (Product of (Combinatorial species) and (Combinatorial species), 2),
     (Singleton species, 1),
     (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), 3)]
Got:
    [(Combinatorial species, 0), (Combinatorial species, Combinatorial species), (Product of (Combinatorial species) and (Combinatorial species), 2), (Product of (Combinatorial species) and (Combinatorial species), Product of (Combinatorial species) and (Combinatorial species)), (Singleton species, 1), (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), 3), (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)))]
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/species/species.py", line 672:
    sage: g.edges()
Expected:
    [(0, 3, None), (2, 0, None), (2, 0, None), (3, 1, None), (3, 2, None)]
Got:
    [(Combinatorial species, Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), None), (Product of (Combinatorial species) and (Combinatorial species), Combinatorial species, None), (Product of (Combinatorial species) and (Combinatorial species), Combinatorial species, None), (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), 1, None), (Sum of (Singleton species) and (Product of (Combinatorial species) and (Combinatorial species)), Product of (Combinatorial species) and (Combinatorial species), None)]
**********************************************************************
1 items had failures:
   2 of   9 in __main__.example_27
***Test Failed*** 2 failures.
For whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_species.py
         [3.4 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/combinat/species/species.py"
Total time for all tests: 3.5 seconds
```


and


```
jeeves:sage-4.3.alpha1 wdj$ ./sage -t  "devel/sage/sage/combinat/symmetric_group_representations.py"
sage -t  "devel/sage/sage/combinat/symmetric_group_representations.py"
WARNING: There is one major unsolved bug in some versions of
Sage on OS X 10.6 that causes an 'Abort trap' crash when
doing certain symbolic computations.
See http://trac.sagemath.org/sage_trac/ticket/7095/.
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 80:
    sage: orth([2,1,3,4,5])
Exception raised:
    Traceback (most recent call last):
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        orth([Integer(2),Integer(1),Integer(3),Integer(4),Integer(5)])###line 80:
    sage: orth([2,1,3,4,5])
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 343, in __call__
        return self.representation_matrix(Permutation(permutation))
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/misc/cachefunc.py", line 251, in __call__
        cache[key] = self.f(self._instance, *args, **kwds)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 672, in representation_matrix
        return self._representation_matrix_uncached(permutation)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 642, in _representation_matrix_uncached
        M *= self.representation_matrix_for_simple_transposition(i)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/misc/cachefunc.py", line 251, in __call__
        cache[key] = self.f(self._instance, *args, **kwds)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 606, in representation_matrix_for_simple_transposition
        [(u,v,(j,beta))] = g.edges()
    ValueError: too many values to unpack
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 86:
    sage: orth([1,3,2,4,5])
Exception raised:
    Traceback (most recent call last):
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        orth([Integer(1),Integer(3),Integer(2),Integer(4),Integer(5)])###line 86:
    sage: orth([1,3,2,4,5])
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 343, in __call__
        return self.representation_matrix(Permutation(permutation))
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/misc/cachefunc.py", line 251, in __call__
        cache[key] = self.f(self._instance, *args, **kwds)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 672, in representation_matrix
        return self._representation_matrix_uncached(permutation)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 642, in _representation_matrix_uncached
        M *= self.representation_matrix_for_simple_transposition(i)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/misc/cachefunc.py", line 251, in __call__
        cache[key] = self.f(self._instance, *args, **kwds)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 606, in representation_matrix_for_simple_transposition
        [(u,v,(j,beta))] = g.edges()
    ValueError: too many values to unpack
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 92:
    sage: orth([1,2,4,3,5])
Exception raised:
    Traceback (most recent call last):
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[7]>", line 1, in <module>
        orth([Integer(1),Integer(2),Integer(4),Integer(3),Integer(5)])###line 92:
    sage: orth([1,2,4,3,5])
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 343, in __call__
        return self.representation_matrix(Permutation(permutation))
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/misc/cachefunc.py", line 251, in __call__
        cache[key] = self.f(self._instance, *args, **kwds)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 672, in representation_matrix
        return self._representation_matrix_uncached(permutation)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 642, in _representation_matrix_uncached
        M *= self.representation_matrix_for_simple_transposition(i)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/misc/cachefunc.py", line 251, in __call__
        cache[key] = self.f(self._instance, *args, **kwds)
      File "/Users/wdj/sagefiles/sage-4.3.alpha1/local/lib/python/site-packages/sage/combinat/symmetric_group_representations.py", line 606, in representation_matrix_for_simple_transposition
        [(u,v,(j,beta))] = g.edges()
    ValueError: too many values to unpack
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 568:
    sage: orth.representation_matrix_for_simple_transposition(1)
Expected:
    [ 1  0]
    [ 0 -1]
Got:
    [       -1/2 1/2*sqrt(3)]
    [1/2*sqrt(3)         1/2]
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 576:
    sage: norm.representation_matrix_for_simple_transposition(1)
Expected:
    [ 1  0]
    [ 0 -1]
Got:
    [-1/2  3/2]
    [ 1/2  1/2]
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 620:
    sage: orth._representation_matrix_uncached(Permutation([2,1,3]))
Expected:
    [ 1  0]
    [ 0 -1]
Got:
    [       -1/2 1/2*sqrt(3)]
    [1/2*sqrt(3)         1/2]
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 631:
    sage: norm._representation_matrix_uncached(p)
Expected:
    [ 1  0]
    [ 0 -1]
Got:
    [-1/2  3/2]
    [ 1/2  1/2]
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 653:
    sage: orth.representation_matrix(Permutation([2,1,3]))
Expected:
    [ 1  0]
    [ 0 -1]
Got:
    [       -1/2 1/2*sqrt(3)]
    [1/2*sqrt(3)         1/2]
**********************************************************************
File "/Users/wdj/sagefiles/sage-4.3.alpha1/devel/sage/sage/combinat/symmetric_group_representations.py", line 664:
    sage: norm.representation_matrix(p)
Expected:
    [ 1  0]
    [ 0 -1]
Got:
    [-1/2  3/2]
    [ 1/2  1/2]
**********************************************************************
4 items had failures:
   3 of  19 in __main__.example_1
   2 of   8 in __main__.example_18
   2 of  10 in __main__.example_19
   2 of  10 in __main__.example_20
***Test Failed*** 9 failures.
For whitespace errors, see the file /Users/wdj/.sage//tmp/.doctest_symmetric_group_representations.py
         [3.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/combinat/symmetric_group_representations.py"
Total time for all tests: 4.0 seconds
```


It seems as though the edges method now has a different form of output?


---

Comment by wdj created at 2009-12-06 08:49:58

Changing status from needs_review to needs_work.


---

Comment by ylchapuy created at 2009-12-06 11:34:51

the problem is in the relabel method, I must have made a mistake... investigating


---

Comment by ylchapuy created at 2009-12-06 14:19:16

Changing status from needs_work to needs_review.


---

Attachment

Small patch to remove the failure in species.py and symmetric_group_representations.py.

I'm not sure about copy vs deepcopy though (see http://groups.google.com/group/sage-devel/browse_thread/thread/a7d9f2e0138c5757)


---

Comment by wdj created at 2009-12-06 16:31:11

With the new patch, I get these errors using sage -testall on an 
imac running 10.6.1 and sage-4.3.a1:


```
        sage -t  "devel/sage/sage/calculus/tests.py"
        sage -t  "devel/sage/sage/calculus/wester.py"
        sage -t  "devel/sage/sage/combinat/posets/posets.py"
        sage -t  "devel/sage/sage/functions/hyperbolic.py"
        sage -t  "devel/sage/sage/functions/log.py"
        sage -t  "devel/sage/sage/functions/other.py"
        sage -t  "devel/sage/sage/functions/trig.py"
        sage -t  "devel/sage/sage/graphs/base/dense_graph.pyx"
        sage -t  "devel/sage/sage/graphs/graph.py"
        sage -t  "devel/sage/sage/graphs/graph_generators.py"
        sage -t  "devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx"
        sage -t  "devel/sage/sage/homology/simplicial_complex.py"
        sage -t  "devel/sage/sage/matrix/matrix_symbolic_dense.pyx"
        sage -t  "devel/sage/sage/plot/text.py"
        sage -t  "devel/sage/sage/rings/arith.py"
        sage -t  "devel/sage/sage/rings/complex_double.pyx"
        sage -t  "devel/sage/sage/rings/polynomial/pbori.pyx"
        sage -t  "devel/sage/sage/structure/sage_object.pyx"
        sage -t  "devel/sage/sage/symbolic/expression.pyx"
        sage -t  "devel/sage/sage/symbolic/function.pyx"
Total time for all tests: 5342.8 seconds
```


In particular, there are possibly these new errors:



```
        sage -t  "devel/sage/sage/graphs/base/dense_graph.pyx"
        sage -t  "devel/sage/sage/graphs/graph.py"
        sage -t  "devel/sage/sage/graphs/graph_generators.py"
        sage -t  "devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx"
        sage -t  "devel/sage/sage/homology/simplicial_complex.py"
        sage -t  "devel/sage/sage/structure/sage_object.pyx"
```

I did not check of the output from the graph_generators.py test was the same before and after the patch. So some of these failures might be unrelated. It does seem as though the test for refinement_graphs.pyx hangs. That alone seems to be a problem, doesn't it?


---

Comment by wdj created at 2009-12-06 16:31:11

Changing status from needs_review to needs_work.


---

Attachment

The tree patches must be applied.

The only doctest failure remaining for me is

```
sage -t  "devel/sage/sage/structure/sage_object.pyx"
```

It's  a backward compatibility problem: we can't unpickle graphs pickled in the old format as the NetworkX format changed. I must admit I don't really know how to deal with this.


---

Comment by ylchapuy created at 2009-12-07 10:28:03

Replying to [comment:16 wdj]:

> It does seem as though the test for refinement_graphs.pyx hangs. That alone seems to be a problem, doesn't it?
> 

The timeout for refinement_graphs.pyx is unrelated, it's ticket #7461


---

Comment by rlm created at 2009-12-07 17:30:04

Replying to [comment:18 ylchapuy]:
> Replying to [comment:16 wdj]:
> 
> > It does seem as though the test for refinement_graphs.pyx hangs. That alone seems to be a problem, doesn't it?
> > 
> 
> The timeout for refinement_graphs.pyx is unrelated, it's ticket #7461

This seems a little glib to me. I've never seen problems with refinement_graphs.pyx timing out, #7461 was supposed to fix a timeout in refinement_matrices.pyx, which only happened on systems where the clock was seriously messed up.

David-- Can you apply the patch at #7461 and see if refinement_graphs.pyx is still hanging?

There is some code in there which converts to and from NetworkX graphs, if I'm not mistaken. There might actually be something going on there.


---

Comment by rlm created at 2009-12-07 17:36:54

Replying to [comment:17 ylchapuy]:
> The tree patches must be applied.
> 
> The only doctest failure remaining for me is
> {{{
> sage -t  "devel/sage/sage/structure/sage_object.pyx"
> }}}
> It's  a backward compatibility problem: we can't unpickle graphs pickled in the old format as the NetworkX format changed. I must admit I don't really know how to deal with this.

This is tricky, but not impossible to deal with. Usually, Python objects don't need to be told explicitly how to pickle themselves, but, for example, if you make a Cython object, you need to define a `__reduce__` method (see http://www.sagemath.org/doc/reference/sage/structure/unique_representation.html). What that does is returns information to tell Sage how to recreate the object, basically by calling the first object returned on the rest of them. What needs to be done is to trace back through what is happening when we unpickle old Sage graphs, and see if there isn't an `__init__` function that gets called somewhere that we can modify to account for this case. Then we could probably just reach in and grab the adjacency dict from the old NetworkX object.


---

Comment by ylchapuy created at 2009-12-07 17:45:22

I sort of know that this is the thing to do, but I don't know how to do it, and I'm not able to spend enough time to learn by now...

If anyone want to do it, I'd be very pleased!


---

Comment by wdj created at 2009-12-08 01:55:34

Replying to [comment:19 rlm]:
> Replying to [comment:18 ylchapuy]:
> > Replying to [comment:16 wdj]:
> > 
> > > It does seem as though the test for refinement_graphs.pyx hangs. That alone seems to be a problem, doesn't it?
> > > 
> > 
> > The timeout for refinement_graphs.pyx is unrelated, it's ticket #7461
> 
> This seems a little glib to me. I've never seen problems with refinement_graphs.pyx timing out, #7461 was supposed to fix a timeout in refinement_matrices.pyx, which only happened on systems where the clock was seriously messed up.
> 
> David-- Can you apply the patch at #7461 and see if refinement_graphs.pyx is 
> still hanging?


The problem is that, for me, #7461 will not apply after applying the tickets from 
this patch. I guess they are conflicting?

I only got the hanging problem with refinement_graphs.pyx after applying these
patches.


> 
> There is some code in there which converts to and from NetworkX graphs, if I'm not mistaken. There might actually be something going on there.


---

Comment by was created at 2009-12-08 06:02:48

I care a lot more about pickling being designed for graphs so it works in the future and is immune to future upgrades.   That's more important than possibly breaking old pickles.   E.g., all the matrix code is *designed* so that old pickles always work yet new formats can be introduced.   You should look at that matrix code to see how this works.


---

Comment by mvngu created at 2010-01-18 02:31:31

NetworkX 1.0 is now out. See original announcement on [networkx-discuss](http://groups.google.com/group/networkx-discuss/browse_thread/thread/f7b9060d0e2bc1fb).


---

Comment by gsmcwhirter created at 2010-01-29 04:49:00

Networkx 1.0.1 is latest. 

Put together an spkg of 1.0.1 here: http://webfiles.uci.edu/gmcwhirt/www/networkx-1.0.1.spkg

Also attaching a patch that almost passes all the tests (with some slight corrections to doctest answers on account of altered networkx internal representations). The patch also incorporates many of the changes from the already-attached patches, but should not depend on them. It is patched off of the 4.3.1 release. The patch does not solve the unpickling problems cited above. See http://groups.google.com/group/sage-devel/browse_thread/thread/1f0d3fe3897646d0 for a mailing list thread.


---

Attachment


---

Attachment

Added second patch on top of the previous one that should resolve unpickling issues in a correct way.


---

Attachment


---

Comment by gsmcwhirter created at 2010-01-30 05:50:19

Added the documentation strings for the unpickling classes and methods. Should be ready for review.


---

Comment by gsmcwhirter created at 2010-01-30 05:50:19

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-02-02 20:40:56

Thanks.  Just today, I had someone ask to see networkx.  I felt embarrassed about showing them networkx 0.36, so I pulled these patches and applied them to 4.3.1 without a problem.  I'll probably try to referee this sometime in the next week, unless someone (hopefully! :) beats me to it.


---

Comment by jason created at 2010-02-02 20:40:56

Changing assignee from rlm to jason.


---

Comment by mvngu created at 2010-02-28 20:53:27

The patch [trac_7608_networkx-1.0.1_fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.patch) is actually many patches put into one file, as evident by the following snippet:

```
-#        from networkx import XGraph                                           
+#        from networkx import MultiGraph                                       
 #        G = Graph(self.vertices)                                              
 #        cdef object XG = G._backend._nxg                                      
 #                                                                              
# HG changeset patch
# User Gregory McWhirter <gmcwhirt`@`uci.edu>
# Date 1264709924 28800
# Node ID 69b48b5bff7c07dfa3013a1572cd7926d17a601c
# Parent  6a8cf386950323e52babe883811d4bffddb54a74
Applying -bugs patch                                                            
                                                                                
diff -r 6a8cf3869503 -r 69b48b5bff7c sage/graphs/base/graph_backends.py         
--- a/sage/graphs/base/graph_backends.py        Thu Jan 28 12:14:56 2010 -0800  
+++ b/sage/graphs/base/graph_backends.py        Thu Jan 28 12:18:44 2010 -0800  
`@``@` -603,7 +603,7 `@``@`
                         self._nxg.remove_edge(u,v,k)                           
                         break                                                  
             else:                                                              
-                if self._nxg.edge[u][v].get('weight',None) == l:               
+                if l is None or self._nxg.edge[u][v].get('weight',None) == l:  
                     self._nxg.remove_edge(u,v)                                 
         except KeyError:                                                       
             pass                                                               
# HG changeset patch
# User Gregory McWhirter <gmcwhirt`@`uci.edu>
# Date 1264739634 28800
# Node ID 6216ab27b8110fad4803f298cafb60535b9ff273
# Parent  69b48b5bff7c07dfa3013a1572cd7926d17a601c
Trac 7608 accomodate upgrade to networkx-1.0.1                                  
                                                                                
diff -r 69b48b5bff7c -r 6216ab27b811 sage/graphs/base/graph_backends.py         
--- a/sage/graphs/base/graph_backends.py        Thu Jan 28 12:18:44 2010 -0800  
+++ b/sage/graphs/base/graph_backends.py        Thu Jan 28 20:33:54 2010 -0800  
`@``@` -32,12 +32,12 `@``@`
         """                                                                    
         Add an edge (u,v) to self, with label l.  If directed is True, this is
         interpreted as an arc from u to v.                                     
-                                                                               
+
```

Also, try to put all changes into one patch. In this case, the following three patches could be rolled into one:

 * [trac_7608_networkx-1.0.1_fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.patch)
 * [trac_7608_networkx-1.0.1_fixes.p1.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.p1.patch)
 * [trac_7608_networkx-1.0.1_fixes.p2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.p2.patch)

Doing so would make it easier to review.



Applying [trac_7608_networkx-1.0.1_fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.patch) to Sage 4.3.3 results in a hunk failure:

```
[mvngu`@`sage sage-main]$ hg qimport http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.patch && hg qpush
adding trac_7608_networkx-1.0.1_fixes.patch to series file
applying trac_7608_networkx-1.0.1_fixes.patch
patching file sage/graphs/generic_graph.py
Hunk #250 succeeded at 6694 with fuzz 2 (offset 0 lines).
Hunk #313 FAILED at 8757
Hunk #346 succeeded at 10231 with fuzz 1 (offset -1 lines).
1 out of 364 hunks FAILED -- saving rejects to file sage/graphs/generic_graph.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
errors during apply, please fix and refresh trac_7608_networkx-1.0.1_fixes.patch
[mvngu`@`sage sage-main]$ cat sage/graphs/generic_graph.py.rej
--- generic_graph.py
+++ generic_graph.py
`@``@` -8750,9 +8758,9 `@``@`
         """
         Logic for coloring by label (factored out from plot() for use in 3d
         plots, etc)
-        
-        EXAMPLES::
-        
+
+        EXAMPLES::
+
             sage: G = AlternatingGroup(5).cayley_graph()
             sage: G.num_edges()
             120
```

I have attached [trac_7608-networkx-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608-networkx-folded.patch) which folds the following three patches into one patch:

 * [trac_7608_networkx-1.0.1_fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.patch)
 * [trac_7608_networkx-1.0.1_fixes.p1.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.p1.patch)
 * [trac_7608_networkx-1.0.1_fixes.p2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.p2.patch)
 
Only apply [trac_7608-networkx-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608-networkx-folded.patch). This folded patch is based on Sage 4.3.3 because [trac_7608_networkx-1.0.1_fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608_networkx-1.0.1_fixes.patch) results in a hunk failure as reported above.


---

Comment by mvngu created at 2010-03-01 03:51:42

The reason why gsmcwhirter's patch [trac_7608-networkx-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608-networkx-folded.patch) is so large is that most of it is about removing trailing white spaces. Maybe I don't understand pickling enough to see why gsmcwhirter doesn't provide any (valid) examples in the following code:

```
+class NetworkXGraphDeprecated(SageObject):
+    """
+    Class for unpickling old networkx.XGraph formats
+
+    DOCTEST:
+        sage: import sage.graphs.base.graph_backends
+    """
+
+    def __init__(self):
+        """
+        Issue deprecation warnings for the old networkx XGraph formats
+        """
+        import warnings
+        from sage.misc.misc import deprecation
+        warnings.warn("Your graph object is saved in an old format since networkx\
+                    was updated to 1.0.1. You can re-save your graph by typing\
+                    graph.save(filename) to make this warning go away.",
+                    DeprecationWarning, stacklevel=2)
+        deprecation("Your graph object is saved in an old format since networkx\
+                    was updated to 1.0.1. You can re-save your graph by typing\
+                    graph.save(filename) to make this warning go away.")
+
+    def mutate(self):
+        """
+        Change the old networkx XGraph format into the new one.
+
+        OUTPUT:
+
+        - The networkx.Graph or networkx.MultiGraph corresponding to the
+          unpickled data.
+        """
+        import networkx
+        new_adj = {}
+
+        for node1, edges in self.adj.iteritems():
+            new_adj[node1] = {}
+            for node2, weights in edges.iteritems():
+                new_adj[node1][node2] = {}
+                if weights is not None:
+                    try:
+                        for weight in weights:
+                            new_adj[node1][node2][weight] = {}
+                    except TypeError:
+                        new_adj[node1][node2]['weight'] = weight
+
+        if self.multiedges:
+            G = networkx.MultiGraph(new_adj)
+        else:
+            G = networkx.Graph(new_adj)
+
+        return G
+
+class NetworkXDiGraphDeprecated(SageObject):
+    """
+    Class for unpickling old networkx.XDiGraph formats
+
+    DOCTEST:
+        sage: import sage.graphs.base.graph_backends
+    """
+
+    def __init__(self):
+        """
+        Issue deprecation warnings for the old networkx XDiGraph formats
+        """
+        import warnings
+        from sage.misc.misc import deprecation
+        warnings.warn("Your digraph object is saved in an old format since networkx\
+                    was updated to 1.0.1. You can re-save your digraph by typing\
+                    digraph.save(filename) to make this warning go away.",
+                    DeprecationWarning, stacklevel=2)
+        deprecation("Your digraph object is saved in an old format since networkx\
+                    was updated to 1.0.1. You can re-save your digraph by typing\
+                    digraph.save(filename) to make this warning go away.")
+
+    def mutate(self):
+        """
+        Change the old networkx XDiGraph format into the new one.
+
+        OUTPUT:
+
+        - The networkx.DiGraph or networkx.MultiDiGraph corresponding to the
+          unpickled data.
+        """
+        import networkx
+        new_adj = {}
+
+        for node1, edges in self.adj.iteritems():
+            new_adj[node1] = {}
+            for node2, weights in edges.iteritems():
+                new_adj[node1][node2] = {}
+                if weights is not None:
+                    try:
+                        for weight in weights:
+                            new_adj[node1][node2][weight] = {}
+                    except TypeError:
+                        new_adj[node1][node2]['weight'] = weight
+
+        if self.multiedges:
+            G = networkx.MultiDiGraph(new_adj)
+        else:
+            G = networkx.DiGraph(new_adj)
+
+        return G
+
+from sage.structure.sage_object import register_unpickle_override
+register_unpickle_override('networkx.xgraph','XGraph', NetworkXGraphDeprecated)
+register_unpickle_override('networkx.xdigraph','XDiGraph', NetworkXDiGraphDeprecated)
```

[This section](http://www.sagemath.org/doc/developer/conventions.html) of the Developer's Guide explains the policy regarding doctests and examples. See also [these guidelines](http://www.sagemath.org/doc/developer/trac.html). You need to explain why the following functions don't have doctests/examples:

```
+    def _iterator_in_edges_with_labels(self, vertices):
+        """
+        Iterate over the incoming edges incident to a sequence of vertices.
+        Special case, only for internal use.
+        """
+        try:
+            assert(not isinstance(self._nxg, (NetworkXGraphDeprecated, NetworkXDiGraphDeprecated)))
+        except AssertionError:
+            self._nxg = self._nxg.mutate()
+
+        for u,v,d in self._nxg.in_edges_iter(vertices,data=True):
+            yield (u,v,d.get('weight',None))
```

and

```
+    def _iterator_out_edges_with_labels(self, vertices):
+        """
+        Iterate over the outbound edges incident to a sequence of vertices.
+        Special case, only for internal use.
+        """
+        try:
+            assert(not isinstance(self._nxg, (NetworkXGraphDeprecated, NetworkXDiGraphDeprecated)))
+        except AssertionError:
+            self._nxg = self._nxg.mutate()
+
+        for u,v,d in self._nxg.out_edges_iter(vertices,data=True):
+            yield (u,v,d.get('weight',None))
```

Nevertheless, the proposed changes to upgrade NetworkX to 1.0.1 have been in demand for a long time. I'm happy with the changes, but you need to address the issues I listed above.


---

Comment by gsmcwhirter created at 2010-03-01 04:27:37

Sorry about the white space stuff. Editor automatically trims it and I couldn't figure out an efficient way to roll it back before patching.

I'll see about some examples for the unpickling stuff and the other two functions soon.


---

Comment by rbeezer created at 2010-03-01 05:30:53

Changing assignee from jason to rbeezer.


---

Comment by rbeezer created at 2010-03-02 04:57:47

Never meant to become owner on this one.


---

Comment by rbeezer created at 2010-03-02 04:57:47

Changing assignee from rbeezer to jason.


---

Comment by jason created at 2010-03-02 05:32:35

Replying to [comment:34 rbeezer]:
> Never meant to become owner on this one.

Bummer!


---

Comment by wdj created at 2010-03-03 11:05:55

the networkx spkg and the last patch apply fine and pass sage -testall on a 10.6.2 mac.


---

Comment by GeorgSWeber created at 2010-03-10 20:54:27

I guess, that in order to have some non-trivial doctests for the above code snippets, (the next one to incorporate nNetworkx 1.0.1 and all) further versions of Sage need to incorporate some pickles of graphs, pickled with former versions of Sage (and Networkx 0.36).

The right place to store these (they're in binary format, of course), would be in "$SAGE_ROOT/data/extcode/pickle_jar/", i.e. in the extcode spkg, wouldn't it?

(I just wanted to use graphs for the first time, and immediately wondered, why my nice and carefully named labels for the edges of my new graph were not printed. Networkx 0.36 misses the respective function "networkx.draw_networkx_edge_labels", which is in Networkx 1.0.1 however ...)


---

Attachment

folding the previous three patches into one; rebased vs. Sage 4.3.4.alpha1; only apply this one


---

Comment by mvngu created at 2010-03-10 22:58:01

The rebased patch [trac_7608-networkx-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608-networkx-folded.patch) should hopefully only contain changes to get NetworkX upgraded to version 1.0.1. I have not included any of the "remove trailing white spaces" changes. Anyone but me can review it.


---

Comment by wdj created at 2010-03-11 03:07:46

Using 4.3.4.a1 on a 10.6.2 mac, I had a large number of failures, eg


```
        sage -t  "devel/sage/sage/graphs/base/c_graph.pyx"
        sage -t  "devel/sage/sage/graphs/base/dense_graph.pyx"
        sage -t  "devel/sage/sage/graphs/base/graph_backends.py"
        sage -t  "devel/sage/sage/graphs/base/sparse_graph.pyx"
        sage -t  "devel/sage/sage/graphs/bipartite_graph.py"
        sage -t  "devel/sage/sage/graphs/chrompoly.pyx"
        sage -t  "devel/sage/sage/graphs/digraph.py"
        sage -t  "devel/sage/sage/graphs/digraph_generators.py"
        sage -t  "devel/sage/sage/graphs/generic_graph.py"
        sage -t  "devel/sage/sage/graphs/generic_graph_pyx.pyx"
        sage -t  "devel/sage/sage/graphs/graph.py"
        sage -t  "devel/sage/sage/graphs/graph_bundle.py"
        sage -t  "devel/sage/sage/graphs/graph_coloring.py"
        sage -t  "devel/sage/sage/graphs/graph_editor.py"
        sage -t  "devel/sage/sage/graphs/graph_generators.py"
        sage -t  "devel/sage/sage/graphs/graph_latex.py"
        sage -t  "devel/sage/sage/graphs/graph_list.py"
        sage -t  "devel/sage/sage/graphs/graph_plot.py"
        sage -t  "devel/sage/sage/graphs/linearextensions.py"
        sage -t  "devel/sage/sage/graphs/planarity.pyx"
        sage -t  "devel/sage/sage/graphs/schnyder.py"
        sage -t  "devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx"
```


Can anyone else confirm this?

Strange, since I think for the previous patch I had no failures.


---

Comment by rbeezer created at 2010-03-11 04:50:23

Replying to [comment:39 wdj]:
> Using 4.3.4.a1 on a 10.6.2 mac, I had a large number of failures, eg

This ticket keeps trying to make me the owner.  Jason?

This is on 4.3.3.final, I will upgrade right now and try again.  Just a few errors:


```
        sage -t  devel/sage-networkx/sage/graphs/graph_generators.py # 4 doctests failed
        sage -t  devel/sage-networkx/sage/graphs/graph_plot.py # 1 doctests failed
        sage -t  devel/sage-networkx/sage/graphs/generic_graph.py # 2 doctests failed
```


Some are ordering problems, mostly on what appear to be random graphs.  Some look obviously fixable.  The `graph_plot.py` is an exception and looks unintelligible to me.

More in a little bit.

Rob


---

Comment by jason created at 2010-03-11 05:34:20

Replying to [comment:40 rbeezer]:

> Replying to [comment:39 wdj]:
> This ticket keeps trying to make me the owner.  Jason? 

Yeah, I vote for you too :).

There appears to be some problem with trac; I've accidentally taken ownership of a tickets myself.  The problem is the radio button default sometimes seems to be "assign to" instead of "leave as...".


---

Comment by rbeezer created at 2010-03-11 06:11:10

On 4.3.4.alpha1 just 6 failed doctests.  Four seem to involve random graphs, one is numerical noise (`clustering_coeff()`), and one seems related to changes for edges that are not labeled (None versus and empty dictionary).


```
        sage -t  devel/sage-networkx/sage/graphs/graph_generators.py # 4 doctests failed
        sage -t  devel/sage-networkx/sage/graphs/generic_graph.py # 2 doctests failed
```


I'll continue testing...


---

Comment by GeorgSWeber created at 2010-03-14 17:01:14

Hi, I agree that five of the doctest failures are trivial, but I find that one is at least a bit suspicious:

```
File "/Users/Shared/sage/test/sage-4.3.4.alpha1/devel/sage/sage/graphs/generic_graph.py", line 6700:
    sage: (graphs.FruchtGraph()).clustering_coeff(nbunch=[0,1,2],with_labels=True,weights=True)
Expected:
    ({0: 0.33333333333333331, 1: 0.33333333333333331, 2: 0.0}, {0: 0.083333333333333329, 1: 0.083333333333333329, 2: 0.083333333333333329})
Got:
    ({0: 0.33333333333333331, 1: 0.33333333333333331, 2: 0.0}, {0: 0.33333333333333331, 1: 0.33333333333333331, 2: 0.33333333333333331})
```

because the last three numerical values "switched" from 1/12 to 1/3, that is not "numerical noise". It might just be a functional change in the networkx core (maybe even a bugfix), but I didn't dig deeper.

If this change is seen by everybody else, I would vote for just adapting the doctest according to the new behaviour. The good news is that I did a complete "make test" on sage-4.3.4.alpha1 (with the new spkg, and the last patch from this ticket attached), and there were no other doctest failures outside the graphs subdirectory.


---

Comment by rbeezer created at 2010-03-14 19:37:52

Replying to [comment:43 GeorgSWeber]:
> Hi, I agree that five of the doctest failures are trivial, but I find that one is at least a bit suspicious:

Yep, I was only looking carefully at the low-order bits.  ;-)

This doctest is addressed in one of the previous patches (trac_7608_networkx-1.0.1_fixes.patch).

Minh did an excellent service in cleaning-up the monster version of this patch, but I'd guess maybe a couple of necessary parts didn't make the cut into the latest version.  Perhaps the other five could also be located in the "fixes" series.


---

Comment by rbeezer created at 2010-03-14 19:37:52

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-03-14 20:10:53

I've tested this with a 700-line script I used last August to generate graphics for a graph theory talk.  While not comprehensive, it will certainly give the basic graph theory routines quite a workout.  Output looks correct, no errors raised, and just one (legitimate) deprecation warning about the `cliques()` method.  So I'm even more confident that these changes should be (fairly) backward-compatible.

I don't have any patches on this ticket, so I could give a positive review once the six doctests are fixed.  Or if no one rises to the bait, I'll fix the doctests in a day or two......

Rob


---

Attachment


---

Comment by rbeezer created at 2010-03-16 06:12:35

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-03-16 06:12:35

Latest attachment fixes five doctests (and a sixth seems to fix itself as it is in a chain of random events where two were deleted).  This has been kept separate from the "folded" patch so it can be easy to review.

All of the new doctest results in this patch are straight out of the original "fixes" patch, so I believe they were simply omitted in creating the "folded" patch.

With this patch, all tests pass on sage.math except for some `sage/combinat/words/morphism.py` pickling/save/category stuff.  My own setup seems a bit messed up, so with `-testall` I get lots of failures, but all tests pass in `sage/graphs`.


---

Comment by jason created at 2010-04-09 02:36:05

Replying to [comment:45 rbeezer]:

> I don't have any patches on this ticket, so I could give a positive review once the six doctests are fixed.  Or if no one rises to the bait, I'll fix the doctests in a day or two......

What is left to review this?  Just reviewing your doctest fixes?


---

Comment by jason created at 2010-04-15 04:14:12

After applying the patches and installing the spkg, sage -t for files in the graphs/ directory works fine for me.  `sage -t sage/combinat/words/*.py` also works (which includes the morphism.py mentioned above).


---

Comment by jason created at 2010-04-15 04:17:28

Looking at your doctest code, it seems that some user code could break since the output format of the edge function has changed (i.e., edge labels are not None, but a dictionary).  However, this might be "unavoidable".  Definitely we should upgrade networkx!


---

Comment by rbeezer created at 2010-04-15 06:01:13

Replying to [comment:49 jason]:
> Looking at your doctest code, it seems that some user code could break since the output format of the edge function has changed (i.e., edge labels are not None, but a dictionary).  However, this might be "unavoidable".  Definitely we should upgrade networkx!

Hi Jason,

Sorry I missed your ping on IRC.  Yes, all I did was copy six missing doctests.  One big patch had many spurious changes (line endings, blank lines, whatever).  Minh did a great service to clean it up, but I think he simply missed a few tests.  I just copied them out of the old patch and ran tests.  And I also ran it against a big script I used to build my Hoffman-Singleton Graph talk.

Yes, I think the possible break in user code is somewhat out of our hands, given it was a change in NetworkX.  But not bad, given how long its been since an upgrade.

Short answer - I think it just needs somebody fresh to run tests (on the whole Sage library?) and call it good.  That'd be you.  ;-)

Rob


---

Comment by jason created at 2010-04-15 18:03:45

Changing status from needs_review to needs_work.


---

Comment by jason created at 2010-04-15 18:03:45

I get a number of failures for "make ptestlong" on sage 4.3.5.  It seems that there are maybe 5-6 real issues.  The files that don't pass doctests are:


```
The following tests failed:

        sage -t  -long 4.3.5/devel/sage/doc/en/bordeaux_2008/elliptic_curves.rst # 8 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/combinat/graph_path.py # 59 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/combinat/posets/lattices.py # 67 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/combinat/posets/elements.py # 57 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/combinat/posets/hasse_diagram.py # 79 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/combinat/posets/poset_examples.py # 44 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/linearextensions.py # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/chrompoly.pyx # 10 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/planarity.pyx # 2 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph_coloring.py # 11 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph_list.py # 25 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph_editor.py # 5 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/bipartite_graph.py # 22 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph_bundle.py # 2 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/digraph_generators.py # 9 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph_latex.py # 17 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph.py # 109 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/schnyder.py # 23 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/generic_graph_pyx.pyx # 6 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph_plot.py # 11 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/base/dense_graph.pyx # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/base/c_graph.pyx # 3 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/base/sparse_graph.pyx # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/base/graph_backends.py # 58 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/digraph.py # 44 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/graph_generators.py # 230 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/graphs/generic_graph.py # 566 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/categories/finite_coxeter_groups.py # 18 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/categories/category.py # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/geometry/polyhedra.py # 4 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/categories/coxeter_groups.py # 7 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/groups/perm_gps/partn_ref/refinement_graphs.pyx # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/homology/simplicial_complex.py # 9 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/homology/delta_complex.py # 2 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/homology/cell_complex.py # 3 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/descent_two_isogeny.pyx # 1 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/lseries_ell.py # 10 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py # 66 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/heegner.py # 10 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/padics.py # 25 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/BSD.py # 9 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/sha_tate.py # 48 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/padic_lseries.py # 102 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py # 21 doctests failed
        sage -t  -long 4.3.5/devel/sage/sage/combinat/posets/posets.py # 240 doctests failed
```


Here is a sampling of the issues:


```
**********************************************************************
File "/home/grout/sage-4.3.5/devel/sage-main/sage/categories/category.py", line 518:
    sage: G.is_directed_acyclic()
Expected:
    True
Got:
    False
**********************************************************************
1 items had failures:
   1 of   6 in __main__.example_12
***Test Failed*** 1 failures.

**********************************************************************
File "/home/grout/sage-4.3.5/devel/sage-main/sage/graphs/generic_graph.py", line 5453:
    sage: G = graphs.TetrahedralGraph()
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_98[5]>", line 1, in <module>
        G = graphs.TetrahedralGraph()###line 5453:
    sage: G = graphs.TetrahedralGraph()
      File "/home/grout/sage/local/lib/python/site-packages/sage/graphs/graph_generators.py", line 1651, in TetrahedralGraph
        return graph.Graph(G, name="Tetrahedron")
      File "/home/grout/sage/local/lib/python/site-packages/sage/graphs/graph.py", line 832, in __init__
        if isinstance(data, (networkx.DiGraph, networkx.classes.MultiDiGraph)):
    AttributeError: 'module' object has no attribute 'classes'
**********************************************************************


**********************************************************************
File "/home/grout/sage-4.3.5/devel/sage-main/sage/graphs/generic_graph.py", line 10036:
    sage: G.get_vertices()
Expected:
    {0: 'before', 1: 'after', 2: None, 3: None}
Got:
    {0: 'before', 1: 'after', 2: None, 3: None, 4: None, 5: None, 6: None}
**********************************************************************


**********************************************************************
File "/home/grout/sage-4.3.5/devel/sage-main/sage/graphs/generic_graph.py", line 481:
    sage: h._pos is g._pos
Expected:
    False
Got:
    True
**********************************************************************


**********************************************************************
File "/home/grout/sage-4.3.5/devel/sage-main/sage/graphs/generic_graph.py", line 7664:
    sage: G.shortest_path_lengths(0, by_weight=True)
Exception raised:
    Traceback (most recent call last):
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/grout/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_139[6]>", line 1, in <module>
        G.shortest_path_lengths(Integer(0), by_weight=True)###line 7664:
    sage: G.shortest_path_lengths(0, by_weight=True)
      File "/home/grout/sage/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 7669, in shortest_path_lengths
        paths = self.shortest_paths(u, by_weight)
      File "/home/grout/sage/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 7632, in shortest_paths
        return networkx.single_source_dijkstra_path(self.networkx_graph(copy=False), u)
      File "/home/grout/sage/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 569, in networkx_graph
        name=self.name())
    TypeError: __init__() got an unexpected keyword argument 'selfloops'
**********************************************************************


```



---

Attachment

apply on top of previous patches


---

Comment by jason created at 2010-04-20 15:17:01

With the last patch, "make ptestlong" now passes all doctests!

Rob, can you review my last patch to make sure nothing bad is changed?  I'm particularly worried about taking out the selfloops option---does it break anything?


---

Comment by jason created at 2010-04-20 15:17:01

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-04-21 04:48:30

Replying to [comment:52 jason]:
> Rob, can you review my last patch to make sure nothing bad is changed?  I'm particularly worried about taking out the selfloops option---does it break anything?

Hi Jason,

Had to rebase the mega-patch and it looks like there are some new (trivial) failures with the edge labels being None/empty-dictionaries.

I'll try to get some full tests done and new patches up before the evening is out.

Rob


---

Comment by rbeezer created at 2010-04-21 04:48:30

Changing status from needs_review to needs_work.


---

Attachment

For information only, to be folded into rebased patch


---

Comment by rbeezer created at 2010-04-21 06:48:45

trac_7608-networkx-mega.patch is a rolled-up patch, rebased on 4.4.alpha1, folding three previous patches together, plus includes fourth patch that fixes some edge-label output in doctests new to the 4.4 series.

Builds, passes long tests.  Documentation builds without warnings.

Jason - can you just check the few places where a `None` is replaced by an empty dictionary in new bipartite graph doctests that output edges?  Small information patch is available so you can quickly see the changes.

Rob


---

Comment by rbeezer created at 2010-04-21 06:48:45

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-04-21 06:56:47

Great job!  Your last changes look reasonable to me, given the new format of the edges with the new networkx.


---

Comment by rbeezer created at 2010-04-22 03:42:13

I meant to suggest that this could have a positive review once Jason was done.  So it sounds like Jason is satisfied with the final details, and so am I.

I'm going to change this to "positive review" and if anybody feels different they can flip it back.

Minh - keep that 1.0.1 spkg available!

Rob


---

Comment by rbeezer created at 2010-04-22 03:42:13

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-04-23 06:06:01

Rebased, folded


---

Attachment

Authorship credit goes to Gregory McWhirter, so I have updated rbeezer's mega patch to set the username to Gregory McWhirter.


---

Attachment


---

Attachment


---

Comment by mvngu created at 2010-04-25 09:02:13

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-04-25 09:02:13

Replying to [comment:57 rbeezer]:
> I'm going to change this to "positive review" and if anybody feels different they can flip it back.

I took Sage 4.4.rc0, replaced its NetworkX spkg with the upgraded one on this ticket, and applied the patch [trac_7608-networkx-mega.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608-networkx-mega.patch) to the package sage-4.4.rc0.spkg. I then rebuilt Sage 4.4.rc0 from scratch with these modifications. The build went fine, but doctesting resulted in the following failures:


```
sage -t  -long devel/sage/sage/graphs/generic_graph.py
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.rc0-7608-networkx/devel/sage-main/sage/graphs/generic_graph.py", line 6828:
    sage: (graphs.FruchtGraph()).clustering_coeff(nbunch=[0,1,2],with_labels=True,weights=True)
Expected:
    ({0: 0.33333333333333331, 1: 0.33333333333333331, 2: 0.0}, {0: 0.083333333333333329, 1: 0.083333333333333329, 2: 0.083333333333333329})
Got:
    ({0: 0.33333333333333331, 1: 0.33333333333333331, 2: 0.0}, {0: 0.33333333333333331, 1: 0.33333333333333331, 2: 0.33333333333333331})
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.4.rc0-7608-networkx/devel/sage-main/sage/graphs/generic_graph.py", line 5469:
    sage: graphs.DodecahedralGraph().edges()
Expected:
    [(0, 1, None), (0, 10, None), (0, 19, None), (1, 2, None), (1, 8, None), (2, 3, None), (2, 6, None), (3, 4, None), (3, 19, None), (4, 5, None), (4, 17, None), (5, 6, None), (5, 15, None), (6, 7, None), (7, 8, None), (7, 14, None), (8, 9, None), (9, 10, None), (9, 13, None), (10, 11, None), (11, 12, None), (11, 18, None), (12, 13, None), (12, 16, None), (13, 14, None), (14, 15, None), (15, 16, None), (16, 17, None), (17, 18, None), (18, 19, None)]
Got:
    [(0, 1, {}), (0, 10, {}), (0, 19, {}), (1, 2, {}), (1, 8, {}), (2, 3, {}), (2, 6, {}), (3, 4, {}), (3, 19, {}), (4, 5, {}), (4, 17, {}), (5, 6, {}), (5, 15, {}), (6, 7, {}), (7, 8, {}), (7, 14, {}), (8, 9, {}), (9, 10, {}), (9, 13, {}), (10, 11, {}), (11, 12, {}), (11, 18, {}), (12, 13, {}), (12, 16, {}), (13, 14, {}), (14, 15, {}), (15, 16, {}), (16, 17, {}), (17, 18, {}), (18, 19, {})]
**********************************************************************
2 items had failures:
```


I have patched this failure, as contained in [trac_7608-more-doctest-fixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608-more-doctest-fixes.patch). This patch is folded into the original mega patch to get the new mega patch [trac_7608-networkx-mega.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7608/trac_7608-networkx-mega.2.patch). Anyone up for a further trivial review of this new mega patch?


---

Comment by mvngu created at 2010-04-25 09:02:43

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-04-28 22:52:15

Changing status from needs_review to positive_review.


---

Comment by rbeezer created at 2010-04-28 22:52:15

The latest fix-ups by Minh, the rolled-up mega patch, the upgraded spkg all build and past tests on 4.4rc0, specifically,

`sage -t -long  devel/sage/sage`

so I'm flipping this back to positive review.  Hopefully it'll get merged before any new graph theory tickets.

Rob


---

Comment by was created at 2010-04-29 00:35:25

Merged! (into 4.4.1.alpha1)


---

Comment by was created at 2010-04-29 00:35:25

Resolution: fixed
