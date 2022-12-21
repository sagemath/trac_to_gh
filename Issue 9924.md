# Issue 9924: Doctest error in sage/graphs/graph.py

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-16 23:56:40

Assignee: mvngu

CC:  dimpase edward.scheinerman jason kcrisman mvngu ncohen

I get this doctest error with a trial 4.6.alpha1 on sage.math and many other Sage cluster and Skynet machines:

```python
sage -t -long  devel/sage/sage/graphs/graph.py
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/graph.py", line 1347:
    sage: cycle.order() % 2 == 0
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[9]>", line 1, in <module>
        cycle.order() % Integer(2) == Integer(0)###line 1347:
    sage: cycle.order() % 2 == 0
    AttributeError: 'bool' object has no attribute 'order'
**********************************************************************
File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/devel/sage-main/sage/graphs/graph.py", line 1349:
    sage: cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/mpatel/tmp/sage-4.6.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[10]>", line 1, in <module>
        cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))###line 1349:
    sage: cycle.is_isomorphic(graphs.CycleGraph(cycle.order()))
    AttributeError: 'bool' object has no attribute 'is_isomorphic'
**********************************************************************
```



---

Comment by mpatel created at 2010-09-16 23:58:08

If it's feasible to create a patch now, I can merge it into 4.6.alpha1, while I wait for a response to a build error at #4000. 

Edward, could you add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?


---

Comment by jhpalmieri created at 2010-09-17 00:12:37

Is this repeatable?  I think I've seen this before, but it's always passed on the second try.


---

Comment by mpatel created at 2010-09-17 00:36:41

Oops.  You're right.  I confused this with a different error.  I got error above only on sage.math and cicero.skynet (x86-Linux-pentium4-fc) and it's not reproducible.

I apologize for the noise.  Does anyone know why this test might be "flaky"?


---

Comment by mpatel created at 2010-09-17 00:37:03

Resolution: worksforme


---

Comment by ncohen created at 2010-09-17 05:58:42

Hmmm..... If ``cycle`` is a boolean, it means it is equal to True (the method called returns "True", or a certificate that it is not true otherwise -- a graph object). I have already seen this method to return wrong answers (and this is fixed in #9420), but the code *IS* deterministic and in this case I do not understand why you would not get an error at the previous docstring :


```
            sage: g.is_even_hole_free()      
            True
```


which uses the same graph. Of course, this doctest is another one of the kind I'm trying to get rid off these days : it theoretically fails with a probability of 1/9999999999999999.... which means that it "can happen"... But once again, this would mean an error at the previous docstring too `O_o`

if you are finding yourself on one of the machines on which you have seen it failing, could you give this a try ?


```
    sage: all( isinstance(graphs.RandomBipartite(10, 10, .5).is_even_hole_free(certificate = True), "Graph") for i in range(10000) )
```


Nathann


---

Comment by ncohen created at 2010-09-17 06:12:29

Hmmm.... It looks like it's not --so-- rare O_o


```
sage: sum( not isinstance(graphs.RandomBipartite(10, 10, .5).is_even_hole_free(certificate = True), Graph) for i in range(10000) )
96
```


something like 1%...`:-/`

And with this :


```
sage: t = lambda x: Graph(x).is_forest() or isinstance(x.is_even_hole_free(certificate = True), Graph)
sage: sum( not t(graphs.RandomBipartite(10, 10, .5)) for i in range(10000) )
111
```


Which means it comes from .... the bug in the method subgraph_search, and not from the theoretical probability `:-/`

With the patch applied :


```
sage: sage: t = lambda x: Graph(x).is_forest() or isinstance(x.is_even_hole_free(certificate = True), Graph)
sage: sage: sum( not t(graphs.RandomBipartite(10, 10, .5)) for i in range(10000) )
0
```


Which **relieved** me. I should post a patch to add this is_forest condition anyway. Can I put it on this ticket ?

Nathann


---

Comment by dimpase created at 2010-09-17 06:19:28

Changing status from closed to needs_work.


---

Comment by dimpase created at 2010-09-17 06:19:28

go ahead, Nathann, add the patch...


---

Comment by dimpase created at 2010-09-17 06:21:03

Nathann, could you also add a doctest that does *boom* to the unpatched code?


---

Comment by ncohen created at 2010-09-17 07:48:57

I can do that, but this patch will require #9925 to be applied first... Here is the explanation : for the moment, the docstring works by generating a random bipartite graph, and looking for a cycle inside it. With a (very small) probability, this graph can be a forest, which means there is no cycle --> the doctest fails. This is not checked right now, and means that even though veeeery unlikely, it may fail because the generated graph is a forest. I can write a patch for this, and it will be available here in a second. The problem now, is that even if the graph is not a forest, a bug in subgraph_search may appear during the doctests (and does, with a probability of 1%). Even when the patch checking whether the graph is a forest will be applied, these errors will *STILL* appear until #9420 is applied.

I will then add a patch right now to test for forests, just in case, and another patch based upon #9420, to check this never appears again :-)

Nathann


---

Attachment

There is now one ticket to be reviewed here, and the patch Dima requested is also waiting for review at #9930 (though it depends on #9420 too)..

Sorry for all that !!! `^^;`

Nathann


---

Comment by ncohen created at 2010-09-17 08:17:38

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-09-19 06:48:41

Changing priority from blocker to major.


---

Comment by dimpase created at 2010-09-19 08:03:42

I don't get how these lines in the doctest test anything.

```
... 
 	1354	            sage: print "Everything is Fine !" 
 	1355	            Everything is Fine ! 
```

Unless I am mistaken, they only indicate that the coder was in a jolly good mood while writing them :-)


---

Comment by dimpase created at 2010-09-19 08:03:42

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-09-19 08:34:33

First, you are right, then it was also to avoid having a docstring returning nothing on success, and returning "Error" on failure... It is just meant to say "this section has been run", and check that it was not bypassed for some reason.. Do you prefer it without this part ?

If so, tell me and I update it.

But I consider it a very pertinent information that Sage developpers have fun writing docstring, and the user may like to know it `:-D`

Nathann


---

Comment by dimpase created at 2010-09-19 08:59:55

Nathan, you do not *return* error, you just *print* "Error"!
All that print stuff gets lost when running "sage -t", imho...


---

Comment by ncohen created at 2010-09-19 09:03:05

> Nathan, you do not *return* error, you just *print* "Error"!
> All that print stuff gets lost when running "sage -t", imho...

Yes, but if the message "Error" is printed and the docstring doesn't expect it, an error will reported, won't it ? `O_o`

In case of failure, this piece of code will print :

Error !
Everything is fine !

While the code only expects to find "Everything is fine !".

Nathann


---

Comment by dimpase created at 2010-09-19 09:04:26

OK, my bad...


---

Comment by dimpase created at 2010-09-19 09:04:26

Changing status from needs_work to positive_review.


---

Comment by davidloeffler created at 2010-09-27 09:44:47

Typo, my apologies.


---

Comment by mpatel created at 2010-09-29 08:39:23

Resolution changed from worksforme to fixed


---

Comment by mpatel created at 2010-10-04 21:40:56

Karl-Dieter Crisman reported this error on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/6bb037c1f4a1ace9/baa93cd5c1dc489f#baa93cd5c1dc489f):

```python
On OS X 10.4 PPC, I get a variant on #10042 (I put this on the ticket)
and the toric divisor one, and a known Maxima timeout due to tab-
completion.  I also got the following non-repeating failure:

File "/Users/student/Desktop/sage-4.6.alpha2/devel/sage/sage/graphs/graph.py", line 1346:
    sage: if not g.is_forest():
         cycle = g.is_even_hole_free(certificate = True)
         if cycle.order() % Integer(2) == Integer(1):
             print "Error !"
         if not cycle.is_isomorphic(
                graphs.CycleGraph(cycle.order())):
             print "Error !"
Exception raised:
    Traceback (most recent call last):
      File "/Users/student/Desktop/sage-4.6.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[8]>", line 1, in <module>
        if not g.is_forest():###line 1346:
    sage: if not g.is_forest():
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 1823, in is_forest
        for g in self.connected_components_subgraphs():
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 3136, in connected_components_subgraphs
        list.append(self.subgraph(c, inplace=False))
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 8170, in subgraph
        edge_property=edge_property)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 8279, in _subgraph_by_adding
        G.add_vertices(vertices)
      File "/Users/student/Desktop/sage-4.6.alpha2/local/lib/python/site-packages/sage/graphs/bipartite_graph.py", line 534, in add_vertices
        raise RuntimeError("Partition must be specified (e.g. left=True).")
    RuntimeError: Partition must be specified (e.g. left=True).
```

Dima and Nathann, could you look into this?  If it's a new problem, please open a new 4.6 blocker with this in the description.


---

Comment by ncohen created at 2010-10-04 21:46:58

It's another of this SERGHLIGHLWIEUGH BipartiteGraph-related errors --> they overload methods like add-edge to stay compatible. Usually wrapping the graph inside Graph(g) to cast it toward a regular graph is enough, but I'll give it a look only tomorrow. I have far too much of this wonderful red wine in the brain at the moment. You'll have a patch tomorrow -- sorry for that !

Nathann


---

Comment by mpatel created at 2010-10-05 03:43:13

Replying to [comment:20 mpatel]:
> Karl-Dieter Crisman reported this error on [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/6bb037c1f4a1ace9/baa93cd5c1dc489f#baa93cd5c1dc489f):

I saw the same non-repeating error on Skynet's fulvia (x86_64-SunOS-core2).  The full log is [here](http://build.sagemath.org/sage/builders/fulvia%20full/builds/1/steps/shell_5/logs/stdio).


---

Comment by ncohen created at 2010-10-05 08:15:56

This is fixed by both #10067 and #9422


---

Comment by mpatel created at 2010-10-05 08:55:38

Replying to [comment:23 ncohen]:
> This is fixed by both #10067 and #9422

Could you give before-after example(s) here analogous to those in [comment:6 comment 6], that show statistically, at least, that the new patches fix the problem?  Is it practical to use one of these examples as a long doctest?


---

Comment by ncohen created at 2010-10-05 09:20:27

To be honest I have no idea at all of the probability in this case. I just followed the path of the code, and saw where it can only have happened. With patch #9422, the method is_forest does not call connected_components_subgraphs anymore, which clearly avoids the bug (caused by the subgraph method. adding edges in a BipartiteGraph can lead to such exceptions). With #10067, the BipartiteGraph class is not used anymore, which means that these checks when adding edges (creating the failure) are not done anymore.

My previous checks were all about being sure there was no mistake in subgraph_search, which is some not-so-trivial Cython code. In this case, the cause of the error is crystal clear `:-)`

Nathann


---

Comment by mpatel created at 2010-10-05 21:49:28

I don't have time to apply the patches, but without them, the code:

```python
def example(verbose=False):
    try:
        g = graphs.RandomBipartite(10, 10, .5)
        g.is_even_hole_free() and not g.is_forest()
        if not g.is_forest():
            cycle = g.is_even_hole_free(certificate = True)
            if cycle.order() % 2 == 1:
                print "Error !"
            if not cycle.is_isomorphic(graphs.CycleGraph(cycle.order())):
                print "Error !"
        error = False
    except RuntimeError as exc:
        error = True
        if verbose:
            print exc
    return error

def runner(n=1000):
    fail = 0
    for i in xrange(n):
        fail += example()
    return fail

runner()
```

gives 20 or so failures.  Could you check your patches against this or a similar statistical diagnostic?


---

Comment by mpatel created at 2010-10-05 22:08:06

You could also try, e.g.,


```sh
env SAGE_TEST_ITER=100 ./sage -tp -long devel/sage/sage/graphs/graph.py 
```

on various files.  I believe this will "break" on the first failure in a file.  There's also `SAGE_TEST_GLOBAL_ITER`.  For this, I recommend capturing the output in a file and checking later for failures.  Note: `sage -tp` uses these variables, but `sage -t` does not.


---

Comment by mpatel created at 2010-10-06 04:28:59

I've opened #10081 as a 4.6 blocker for the problem in [comment:20 comment 20].


---

Comment by ncohen created at 2010-10-06 12:25:52

Well, as you had taken the time to write this testing function, I tested it against the patches (with n = 10 000, as I was working on a sheet of paper at the same time and did not mind forgetting it for several minutes `:-D`) :

With #9422 applied :

```python
sage: runner(10000)
0
```


With no patch applied, but with 

```python
g = graphs.RandomBipartite(10, 10, .5)
```

replaced by 

```python
g = Graph(graphs.RandomBipartite(10, 10, .5))
```


in your code (which is exactly what the docstring in #10067 does) :


```python
sage: runner(10000)
0
```


Be sure that this is not just a statistical proof : #9422 "disconnects" the call to the ``is_subgraph`` command, so there is really no path left leading to this exception from BipartiteGraph !

Nathann

P.S. : Thank you for this ``#!python`` trick ! Very nice `;-)`
