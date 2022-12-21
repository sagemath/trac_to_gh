# Issue 6269: Coloring speed up

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2009-06-12 17:25:52

Assignee: was

It would be nice to have faster versions of things like hue() and rainbow(), and to have them in their own submodule of plot.


---

Attachment

This patch does several closely related things:

 1. Takes all coloring functions from plot.plot, plot.misc, and plot.tachyon and puts them in new file plot.colors
 1. Writes most of these in Cython, for anywhere between a 3 and 10 times speedup.  This is not so crucial, given that most are called only once or some number of times less than 100 in a given plot, but is still nice.
 1. Changes complex_plot.pyx in two ways:
    a. Makes the coloring conform with documentation, in that roygbiv goes from positive real axis counterclockwise (increasing argument) instead of the other way around
    a. Changes the function mag_to_lightness to use log(sqrt(r)+1) instead of log(r+1)

None of these need explanation except the last subpoint. Previous behavior was so dark as to obscure tick marks even on the doctest plots, and so light as to make plotting even z squared look pretty vague.  This only adds about .02 ms on average to plots, which means that complex_plot(sqrt) takes a little bit longer but complex_plot(zeta) is indistinguishable from before in timing.  One can quibble about it, but this makes zeros still recognizable for polynomials while not allowing them to drown out for zeta, and makes anything yielding high moduli easier to view, while incurring a very modest performance hit, which seems in line with the pedagogical point of complex_plot.


---

Comment by mhansen created at 2009-06-13 04:25:26

My main concern with this is that converting to something to Cython that is not time critical adds unnecessary build time to the Sage library.  Doing development on Cython files is a lot more annoying than with Python files.  But, I think the other changes are useful.


---

Comment by was created at 2009-06-13 09:55:28

Replying to [comment:2 mhansen]:
> My main concern with this is that converting to something to 
> Cython that is not time critical adds unnecessary build time 
> to the Sage library.  Doing development on Cython files is a 
> lot more annoying than with Python files. 

+1 -- I strongly agree with this.  One also can't trace through code
that is in Cython nearly so easily as with Python.  One should only
Cythonize code where there is a clear important benefit to doing so.

William


---

Comment by kcrisman created at 2009-06-13 23:51:19

Okay, these comments seem reasonable. It was still a good learning experience, and it was very impressive how much faster the commands became.  Perhaps there could be some suggestions added in developer guide as to when not to use Cython.

Anyway, I will try to put up a patch for 1 and 3ab above sometime in the near future!  Description and summary changed accordingly.


---

Comment by ncalexan created at 2009-06-15 20:30:32

I get doctest errors on sage.math and my laptop.  They seem to be to do with graph coloring rather than the valuable refactor of the Color stuff.  Could these be separated?


```
/Users/ncalexan/sage-4.0.1.alpha0/sage -tp 10 -long devel/sage/sage/plot/tachyon.py devel/sage/sage/plot/tri_plot.py devel/sage/sage/plot/circle.py devel/sage/sage/plot/text.py devel/sage/sage/plot/line.py devel/sage/sage/plot/complex_plot.pyx devel/sage/sage/server/notebook/interact.py devel/sage/sage/graphs/graph_coloring.py devel/sage/sage/plot/arrow.py devel/sage/sage/plot/contour_plot.py devel/sage/sage/plot/plot.py devel/sage/sage/plot/matrix_plot.py devel/sage/sage/plot/polygon.py devel/sage/sage/graphs/graph_plot.py devel/sage/sage/plot/bezier_path.py devel/sage/sage/graphs/graph.py devel/sage/sage/plot/plot_field.py devel/sage/sage/plot/plot3d/platonic.py devel/sage/sage/plot/point.py devel/sage/sage/plot/all.py devel/sage/sage/plot/plot3d/plot3d.py devel/sage/sage/plot/disk.py devel/sage/sage/plot/misc.py devel/sage/sage/plot/density_plot.py devel/sage/sage/plot/plot3d/texture.py devel/sage/sage/plot/colors.py devel/sage/sage/plot/primitive.py

Global iterations: 1
File iterations: 1
Using long cached timings to run longest doctests first.
Doctesting 26 files doing 10 jobs in parallel
sage -t -long devel/sage/sage/plot/bezier_path.py
         [34.9 s]
sage -t -long devel/sage/sage/graphs/graph_coloring.py
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py", line 152:
    sage: first_coloring(G,3)
Expected:
    {'#00ff00': [1, 3], '#ff0000': [0], '#0000ff': [2]}
Got:
    {'#ff0000': [0, 1, 2, 3]}
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py", line 248:
    sage: Test().random(1)
Exception raised:
    Traceback (most recent call last):
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_7[3]>", line 1, in <module>
        Test().random(Integer(1))###line 248:
    sage: Test().random(1)
      File "/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py", line 250, in random
        self.random_all_graph_colorings(tests)
      File "/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py", line 281, in random_all_graph_colorings
        raise RuntimeError, "Coloring Failed."
    RuntimeError: Coloring Failed.
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph_coloring.py", line 263:
    sage: Test().random_all_graph_colorings(1)
Exception raised:
    Traceback (most recent call last):
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/ncalexan/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_8[3]>", line 1, in <module>
        Test().random_all_graph_colorings(Integer(1))###line 263:
    sage: Test().random_all_graph_colorings(1)
      File "/Users/ncalexan/sage-4.0.1.alpha0/local/lib/python2.5/site-packages/sage/graphs/graph_coloring.py", line 281, in random_all_graph_colorings
        raise RuntimeError, "Coloring Failed."
    RuntimeError: Coloring Failed.
**********************************************************************
3 items had failures:
   1 of   5 in __main__.example_2
   1 of   4 in __main__.example_7
   1 of   4 in __main__.example_8
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/ncalexan/sage-4.0.1.alpha0/tmp/.doctest_graph_coloring.py
         [36.1 s]
sage -t -long devel/sage/sage/plot/colors.py
         [36.4 s]
sage -t -long devel/sage/sage/plot/density_plot.py
         [42.3 s]
sage -t -long devel/sage/sage/plot/arrow.py
         [43.8 s]
sage -t -long devel/sage/sage/plot/misc.py
         [11.4 s]
sage -t -long devel/sage/sage/plot/circle.py
         [58.4 s]
sage -t -long devel/sage/sage/plot/matrix_plot.py
         [23.4 s]
sage -t -long devel/sage/sage/plot/disk.py
         [25.7 s]
sage -t -long devel/sage/sage/plot/complex_plot.pyx
         [69.4 s]
sage -t -long devel/sage/sage/plot/plot3d/texture.py
         [11.6 s]
sage -t -long devel/sage/sage/plot/plot3d/platonic.py
         [18.7 s]
sage -t -long devel/sage/sage/graphs/graph_plot.py
         [79.5 s]
sage -t -long devel/sage/sage/plot/primitive.py
         [15.4 s]
sage -t -long devel/sage/sage/plot/plot_field.py
         [28.1 s]
sage -t -long devel/sage/sage/plot/plot3d/plot3d.py
         [32.2 s]
sage -t -long devel/sage/sage/plot/line.py
         [62.4 s]
sage -t -long devel/sage/sage/plot/tri_plot.py
         [10.4 s]
sage -t -long devel/sage/sage/server/notebook/interact.py
         [12.5 s]
sage -t -long devel/sage/sage/plot/contour_plot.py
         [103.6 s]
sage -t -long devel/sage/sage/plot/text.py
         [18.0 s]
sage -t -long devel/sage/sage/plot/point.py
         [36.7 s]
sage -t -long devel/sage/sage/plot/polygon.py
         [36.7 s]
sage -t -long devel/sage/sage/plot/tachyon.py
         [53.6 s]
sage -t -long devel/sage/sage/plot/plot.py
         [129.0 s]
sage -t -long devel/sage/sage/graphs/graph.py
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py", line 6160:
    sage: G._color_by_label()
Expected:
    {'#00ffff': [((1,4)(3,5), (1,5,4), (3,4,5)),
     ...],
     '#ff0000': [((1,4)(3,5), (1,5,4,2,3), (1,2,3,4,5)),
     ...]}
Got:
    {'#ff0000': [((1,4)(3,5), (1,5,4), (3,4,5)), ((1,3)(2,5), (1,4,5,2,3), (3,4,5)), ((2,3,5), (2,4,5), (3,4,5)), ((1,3,4,5,2), (1,4,3,5,2), (3,4,5)), ((1,4,3), (1,5,3), (3,4,5)), ((1,3,2,4,5), (1,4,3,2,5), (3,4,5)), ((1,3,5), (1,4,5), (3,4,5)), ((1,3,4,2,5), (1,4,2,3,5), (3,4,5)), ((1,5,3), (1,3)(4,5), (3,4,5)), ((1,4,5,2,3), (1,5,2,4,3), (3,4,5)), ((1,5,2,4,3), (1,3)(2,5), (3,4,5)), ((1,5,4,3,2), (1,3,2), (3,4,5)), ((2,5,4), (2,3,4), (3,4,5)), ((1,4,2,5,3), (1,5,4,2,3), (3,4,5)), ((1,3)(2,4), (1,4,2,5,3), (3,4,5)), ((1,5,3,4,2), (1,3,5,4,2), (3,4,5)), ((1,2,3,5,4), (1,2,4), (3,4,5)), ((1,4,5,3,2), (1,5,4,3,2), (3,4,5)), ((2,4)(3,5), (2,5,4), (3,4,5)), ((1,2,3,4,5), (1,2,4,3,5), (3,4,5)), ((1,4)(2,5), (1,5,2,3,4), (3,4,5)), ((2,4,3), (2,5,3), (3,4,5)), ((1,3,2,5,4), (1,4)(2,3), (3,4,5)), ((1,4,2), (1,5,3,4,2), (3,4,5)), ((3,4,5), (3,5,4), (3,4,5)), ((1,2)(3,5), (1,2)(4,5), (3,4,5)), ((1,3,4), (1,4)(3,5), (3,4,5)), ((3,5,4), (), (3,4,5)), ((1,2)(4,5), (1,2)(3,4), (3,4,5)), ((1,4,3,5,2), (1,5,2), (3,4,5)), ((), (3,4,5), (3,4,5)), ((1,5,3,2,4), (1,3,2,5,4), (3,4,5)), ((1,4,3,2,5), (1,5)(2,3), (3,4,5)), ((2,5,3), (2,3)(4,5), (3,4,5)), ((1,2,4,3,5), (1,2,5), (3,4,5)), ((2,3)(4,5), (2,4,3), (3,4,5)), ((2,3,4), (2,4)(3,5), (3,4,5)), ((1,2,4,5,3), (1,2,5,4,3), (3,4,5)), ((1,5,2), (1,3,4,5,2), (3,4,5)), ((1,3,5,4,2), (1,4,2), (3,4,5)), ((1,5,4), (1,3,4), (3,4,5)), ((1,3)(4,5), (1,4,3), (3,4,5)), ((1,2,3), (1,2,4,5,3), (3,4,5)), ((1,3,2), (1,4,5,3,2), (3,4,5)), ((1,2)(3,4), (1,2)(3,5), (3,4,5)), ((1,2,4), (1,2,5,3,4), (3,4,5)), ((1,4,2,3,5), (1,5)(2,4), (3,4,5)), ((1,2,5,3,4), (1,2,3,5,4), (3,4,5)), ((1,5,2,3,4), (1,3,5,2,4), (3,4,5)), ((1,5,4,2,3), (1,3)(2,4), (3,4,5)), ((1,2,5,4,3), (1,2,3), (3,4,5)), ((2,5)(3,4), (2,3,5), (3,4,5)), ((1,2,5), (1,2,3,4,5), (3,4,5)), ((1,5)(2,4), (1,3,4,2,5), (3,4,5)), ((2,4,5), (2,5)(3,4), (3,4,5)), ((1,4)(2,3), (1,5,3,2,4), (3,4,5)), ((1,5)(2,3), (1,3,2,4,5), (3,4,5)), ((1,3,5,2,4), (1,4)(2,5), (3,4,5)), ((1,4,5), (1,5)(3,4), (3,4,5)), ((1,5)(3,4), (1,3,5), (3,4,5))]}
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py", line 8902:
    sage: P = G.coloring(); P
Expected:
    [[1, 2, 3], [0, 5, 6], [4]]
Got:
    [This is the Trac macro *0, 1, 4, 2, 5, 6, 3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#0, 1, 4, 2, 5, 6, 3-macro)
**********************************************************************
File "/Users/ncalexan/sage-4.0.1.alpha0/devel/sage-nca/sage/graphs/graph.py", line 8907:
    sage: for c in sorted(H.keys()):
       print c, H[c]
Expected:
    #0000ff [4]
    #00ff00 [1, 2, 3]
    #ff0000 [0, 5, 6]
Got:
    #ff0000 [0, 1, 4, 2, 5, 6, 3]
**********************************************************************
2 items had failures:
   1 of   5 in __main__.example_132
   2 of   8 in __main__.example_163
***Test Failed*** 3 failures.
For whitespace errors, see the file /Users/ncalexan/sage-4.0.1.alpha0/tmp/.doctest_graph.py
         [287.4 s]
 
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/sage/graphs/graph_coloring.py # 3 doctests failed
        sage -t -long devel/sage/sage/graphs/graph.py # 3 doctests failed
----------------------------------------------------------------------
Total time for all tests: 287.5 seconds
Tests failed!
```



---

Comment by kcrisman created at 2009-06-16 02:39:48

I should have caught this - I only tested files in plot/, forgot about the graphs/ changes...

At first I thought that somehow rainbow() was giving only one color to all these graphs (which have n=3) but as far as I can tell rainbow works fine.  And (for example) doing

```
sage: from sage.graphs.graph_coloring import *
sage: G = Graph({0:[1,2,3],1:[2]})
sage: list(all_graph_colorings(G,3))
```

gives the correct answer.  For some reason something in the generator (as opposed to list) definition of all_graph_colorings() is causing a problem, but why this wouldn't have cropped up before is puzzling.  I will try to look at it soon.


---

Comment by kcrisman created at 2009-06-16 14:19:02

Changing assignee from was to kcrisman.


---

Comment by kcrisman created at 2009-06-16 14:19:02

I finally figured out what is going on.  

```
sage: rainbow(3)
['#ff0000', '#00ff00', '#0000ff']
sage: rainbow(int(3))
['#ff0000', '#ff0000', '#ff0000']
```

This is because 

```
sage: int(1)/3
1/3
sage: int(1)/int(3)
0
```

and in all the above cases I believe the rainbow input is a Python int coming from a range() or len().  Very annoying.

The patch trac_6269.patch should now pass graph and plot doctests, at least it does for me.


---

Comment by kcrisman created at 2009-06-16 14:19:02

Changing status from new to assigned.


---

Attachment


---

Comment by ncalexan created at 2009-06-16 17:49:59

Looks good to me.


---

Comment by mvngu created at 2009-06-24 22:22:42

Some hunk failures when applied against Sage 4.1.alpha0:

```
sage: hg_sage.apply("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6269/trac_6269.patch")
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/6269/trac_6269.patch
Loading: [......]
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg status
cd "/scratch/mvngu/sage-4.1.alpha0-sage.math-only-x86_64-Linux/devel/sage" && hg import   "/home/mvngu/.sage/temp/sage.math.washington.edu/11758/tmp_1.patch"
applying /home/mvngu/.sage/temp/sage.math.washington.edu/11758/tmp_1.patch
patching file sage/plot/complex_plot.pyx
Hunk #2 FAILED at 43
Hunk #6 FAILED at 195
2 out of 6 hunks FAILED -- saving rejects to file sage/plot/complex_plot.pyx.rej
abort: patch failed to apply
```



---

Comment by mvngu created at 2009-06-24 23:12:02

After testing the library of Sage 4.1.alpha0, I received the following test failures, as reported at this by [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c15b5f57e380cc19) thread by Robert Miller. 

```
The following tests failed:

	sage -t -long devel/sage-main/sage/databases/database.py # 20 doctests failed
	sage -t -long devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
	sage -t -long devel/sage-main/sage/graphs/graph.py # 25 doctests failed
```

So when rebasing the patch `trac_6269.patch`, I think the part that touches `sage/graphs/graph.py` should be left out. As Robert Miller is currently working on a Cython implementation of a graph theory backend, called c_graph (see #6085), perhaps the graph theory modules should not be touched by the rebase so as to prevent any further complication with getting c_graph in.


---

Comment by mvngu created at 2009-06-25 00:11:51

The patch `trac_6269-rebased.patch` is rebased against Sage 4.1.alpha0. Unlike the patch `trac_6269.patch`, the `trac_6269-rebased.patch` doesn't touch anything to do with the graph theory modules.


---

Comment by mvngu created at 2009-06-25 00:19:43

Reinstating ncalexan's positive review.


---

Comment by kcrisman created at 2009-06-25 13:42:04

Replying to [comment:13 mvngu]:
> After testing the library of Sage 4.1.alpha0, I received the following test failures, as reported at this by [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/c15b5f57e380cc19) thread by Robert Miller. 
> {{{
> The following tests failed:
> 
> 	sage -t -long devel/sage-main/sage/databases/database.py # 20 doctests failed
> 	sage -t -long devel/sage-main/sage/geometry/polyhedra.py # 1 doctests failed
> 	sage -t -long devel/sage-main/sage/graphs/graph.py # 25 doctests failed
> }}}
> So when rebasing the patch `trac_6269.patch`, I think the part that touches `sage/graphs/graph.py` should be left out. As Robert Miller is currently working on a Cython implementation of a graph theory backend, called c_graph (see #6085), perhaps the graph theory modules should not be touched by the rebase so as to prevent any further complication with getting c_graph in.

But rlm says in the same thread,  "These are all due to the removal of graph_isom.pyx, and I will be...".  So that should not be the problem.  In fact, I am not sure how one can NOT include graph stuff, because the graph theory modules need some of the coloring stuff, e.g. in graph_colorings.py and several other such files there is the line 


```
from sage.plot.plot import rainbow
```


and that is no longer where rainbow lives.  Now, it is true that rainbow lives in the global namespace, so maybe those lines are all redundant, but as it stands they might cause failure at startup because sage.plot.plot doesn't have rainbow anymore.  

Since sage.plot.plot does import rainbow, maybe that's enough for rainbow to be re-imported into those files from there for now.  I don't feel I have enough of an understanding of Python imports to judge all that.  But at the very least the import statements should be correct or deleted; it makes no sense to leave in imports of a non-existent function which cause no problems (now that I fixed the Integer thing noted above).


---

Comment by mvngu created at 2009-06-25 21:15:17

rebased against Sage 4.1.alpha1


---

Attachment

The patch `trac_6269-rebased.patch` is rebased against Sage 4.1.alpha1. It also touches those graph theory modules that `trac_6269.patch` touches. For all files that `trac_6269-rebased.patch` touches, testing passed with options `-t -long`. I'm re-instating Nick Alexander's positive review, unless there's a reason not to.


---

Comment by boothby created at 2009-06-26 17:44:02

Resolution: fixed
