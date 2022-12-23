# Issue 8513: Including documentation in the reference manual for some files related to graph theory

Issue created by migration from https://trac.sagemath.org/ticket/8513

Original creator: abmasse

Original creation time: 2010-03-12 23:52:07

Assignee: rlm

CC:  ncohen rlm

Keywords: documentation, graph theory

I noticed a few weeks ago while reviewing a patch that important files in the graph theory folder were not appearing anywhere in the reference manual. For instance, functions such as `vertex_cut` or `edge_cut` do not appear, as well as all functions defined only for directed graphs.

At that time, I thought about adding the missing files with the patch, but since there were a lot of warnings displayed by Sphinx while generating the documentation, I changed my mind.

I think it would be a good idea to use this ticket to fix this, but since it touches many files of graph theory, it may be hard to do it in a clean way. Someone has an idea of what would be the best approach ?


---

Comment by mvngu created at 2010-03-13 00:33:09

Wait until Sage 4.3.4 is released. I expect that release to fix all the warnings relating to building the HTML and PDF versions of the Sage standard documentation. At least, I expect that release to fix such warnings for the reference manual.


---

Comment by abmasse created at 2010-03-22 17:00:52

Here are the warnings I get on my computer:


```
[~/Applications/sage/devel/sage-combinat/doc/en/reference]$ sage -docbuild reference html
sphinx-build -b html -d /Users/alexandre/Applications/sage/devel/sage/doc/output/doctrees/en/reference    /Users/alexandre/Applications/sage/devel/sage/doc/en/reference /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 612 source files that are out of date
updating environment: 2 added, 612 changed, 0 removed
reading sources... [100%] sage/symbolic/ring                   curve_morphismtorcfield
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph:3: (ERROR/3) Unexpected indentation.
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.minimum_outdegree_orientation:7: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.spanning_trees_count:18: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/Users/alexandre/Applications/sage/local/lib/python2.6/site-packages/sage/graphs/generic_graph.py:docstring of sage.graphs.generic_graph.GenericGraph.spanning_trees_count:27: (WARNING/2) Bullet list ends without a blank line; unexpected unindent.
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7926: (WARNING/2) Duplicate explicit target name: "krg96".
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7930: (WARNING/2) Duplicate explicit target name: "gyll93".
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7926: WARNING: duplicate citation KRG96, other instance in /Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst:7930: WARNING: duplicate citation GYLL93, other instance in /Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/graphs/generic_graph.rst
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] structure                             urve_morphismtorcfield
writing additional files... genindex modindex search
copying images... media/homology/rp2.png media/homology/simplices.png media/homology/torus.png media/homology/klein.png media/homology/torus_labelled.png
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 8 warnings.
Build finished.  The built documents can be found in /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference
```


I'll try to fix them and upload a patch soon.


---

Comment by abmasse created at 2010-03-22 17:00:52

Changing status from new to needs_work.


---

Attachment

Adds digraph.py and generic_graph.py in the doctree


---

Comment by abmasse created at 2010-03-22 19:51:35

Finally, since there weren't too many warnings, I think it's worth trying to fix all of them. This is done in the patch I just submitted.

To summarize, this patch adds the two files digraph.py and generic_graph.py to the reference manual and correct the less than 10 warnings that Sphinx was displaying.

Needs review!


---

Comment by abmasse created at 2010-03-22 19:51:35

Changing priority from major to minor.


---

Comment by abmasse created at 2010-03-22 19:51:35

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-03-23 10:54:58

Excellent ! Now we appear in the doc, and there are no warnings anymore.

Reviewing your patch, I met a few things that needed fixing in the docs, so if you agree with my modifications, you can set this to positive review.. Thank you !! :-)

Nathann


---

Comment by abmasse created at 2010-03-23 13:12:21

I agree with your changes ! I just hope it won't overlap with any other ticket.

By the way, did you test my patch ? When I created it, I used the sage-combinat queue and it worked fine, but here, when I tried to test your patch, I created a clone (with `hg -clone t8513`) to apply your patch on top of mine, but I got the following warning.


```
[~/Applications/sage/devel/sage-t8513]$ sage -docbuild reference html
sphinx-build -b html -d /Users/alexandre/Applications/sage/devel/sage/doc/output/doctrees/en/reference    /Users/alexandre/Applications/sage/devel/sage/doc/en/reference /Users/alexandre/Applications/sage/devel/sage/doc/output/html/en/reference
Running Sphinx v0.6.3
loading pickled environment... done
building [html]: targets for 2 source files that are out of date
updating environment: 0 added, 2 changed, 0 removed
reading sources... [100%] sage/graphs/graph                          
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/graphs.rst:4: (WARNING/2) toctree references unknown document u'sage/graphs/digraph'
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/graphs.rst:4: (WARNING/2) toctree references unknown document u'sage/graphs/generic_graph'
looking for now-outdated files... none found
pickling environment... done
checking consistency... done
preparing documents... done
writing output... [100%] sage/graphs/graph                           
writing additional files... genindex modindex search
copying static files... done
dumping search index... done
dumping object inventory... done
build succeeded, 2 warnings.
```


It's strange, it doesn't accept to add the two files to the doctree, as if the path was not correct when creating a clone, but was ok with sage-combinat. Does it work fine for you?


---

Comment by ncohen created at 2010-03-23 13:34:44

O_o

Odd.... I applied your patch as usual, and I mean by this not using sage-combinat. It applied fine, and passed all tests. After my modifications, same result O_o

Have you tried cloning the branch using sage -clone instead of doing it manually with hg ?

Nathann


---

Comment by abmasse created at 2010-03-23 14:08:03

No idea... Anyway, I'll try it with the sage-combinat queue to look at the documentation generated by your patch and it should be fine.


---

Attachment


---

Comment by mvngu created at 2010-04-12 20:01:58

I have replaced ncohen's patch with one that has the ticket number in its commit message.


---

Comment by jhpalmieri created at 2010-04-12 21:50:06

I don't know much about graph theory, but is there any sense to the current order in the reference manual?  Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the "Graph Theory" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)


---

Comment by abmasse created at 2010-04-12 22:02:23

Replying to [comment:9 jhpalmieri]:
> I don't know much about graph theory, but is there any sense to the current order in the reference manual?  Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the "Graph Theory" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)

I agree with you! There is some cleanup needed in the documentation. But maybe we should wait for it in another ticket. The goal of #8513 is to quickly make the graph documentation available so that one may check if Sphinx builds all right when reviewing related tickets. If it's ok for you, of course.

Sorry for being so late, by the way, Nathann, I'll try to finish this ticket today or at most, during the week.


---

Comment by mvngu created at 2010-04-12 22:18:55

Replying to [comment:9 jhpalmieri]:
> I don't know much about graph theory, but is there any sense to the current order in the reference manual?

No, I don't think so. The current organization is a mess.





> Wouldn't it make more sense for `graph` to come first, for example, rather than `cliquer`?  

Yes. The current organization of the graph theory modules, as they appear in the reference manual, is rather unusual. For example, the interface to cliquer appears as the very first link. One would expect something along the following line to be more natural:

 * undirected graph
 * digraph
 * generic graph
 * applications of graph theory
 * fast compiled graph
 * etc. 

I have uploaded a reviewer patch that does something about this. With my reviewer patch, the organization of the graph theory modules should be more systematic.





> I don't think alphabetical is the right approach: someone who wants to know about graphs in Sage may very well start at the first link in the "Graph Theory" chapter.  (It might be even better to have an introductory section in the file devel/sage/doc/en/reference/graphs.rst (like matrices.rst, for example).  That probably belongs on another ticket, though.)

Nod. This needs to wait for another ticket.




After applying [trac_8513_graph_theory_documentation-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-abm.patch) and [trac_8513_graph_theory_documentation-smallfixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-smallfixes.patch), I then rebuilt the whole Sage documentation. A long doctest of the whole Sage library resulted in the following failure:

```
sage -t -long devel/sage-main/sage/misc/sagedoc.py
**********************************************************************
File "/dev/shm/mvngu/sandbox/sage-4.3.5-8513-graph-doc/devel/sage-main/sage/misc/sagedoc.py", line 892:
    sage: len(search_doc('tree', whole_word=True, interact=False).splitlines()) < 100
Expected:
    True
Got:
    False
```

This is due to adding two new files to the reference manual that happen to be about graph theory, hence the above search returns more matches for the word "tree". My reviewer patch should fix this doctest failure. It needs reviewing by anyone but me. I'm happy with both abmasse and ncohen's patches. Apply patches in the following order:

 1. [trac_8513_graph_theory_documentation-abm.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-abm.patch)
 1. [trac_8513_graph_theory_documentation-smallfixes.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513_graph_theory_documentation-smallfixes.patch)
 1. [trac_8513-reviewer.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8513/trac_8513-reviewer.patch)


---

Comment by abmasse created at 2010-04-12 22:51:28

I'm running the longtest on all sage right now. Giving some feedback later tonight.


---

Comment by jhpalmieri created at 2010-04-12 23:25:17

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-12 23:25:17

> My reviewer patch should fix this doctest failure. It needs reviewing by anyone but me.

Your patch fixes the problem, but it doesn't really fit in sagedoc.py: the doctests there are supposed to contrast what happens if `whole_word=True` is not used (more than 2000 matches) vs. when it is (used to be fewer than 100 matches).  How about changing it to `len(...) < 150` or `len(...) < 200`?


---

Attachment

reviewer patch


---

Comment by mvngu created at 2010-04-12 23:35:31

Changing status from needs_work to needs_review.


---

Comment by mvngu created at 2010-04-12 23:35:31

Replying to [comment:13 jhpalmieri]:
> Your patch fixes the problem, but it doesn't really fit in sagedoc.py: the doctests there are supposed to contrast what happens if `whole_word=True` is not used (more than 2000 matches) vs. when it is (used to be fewer than 100 matches).  How about changing it to `len(...) < 150` or `len(...) < 200`?

I see what you mean. Performing a search with `whole_word=False` results in too many matches. When using `whole_word=True`, we want to provide an upper bound on the number of matches. I have modified the reviewer patch accordingly.


---

Comment by jhpalmieri created at 2010-04-13 02:56:36

I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?


---

Comment by abmasse created at 2010-04-13 13:55:07

Replying to [comment:15 jhpalmieri]:
> I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?

Sure, if you're ok with the result. It's even better if the final reviewer isn't Nathann nor me.


---

Comment by mvngu created at 2010-04-13 23:33:03

Replying to [comment:15 jhpalmieri]:
> I'm happy with the reviewer patch now.  After rebuilding the docs, all tests pass on sage.math.  Does that mean the whole ticket gets a positive review?

I think so. Cleaning up the modules added by this ticket to the reference manual can be split off to an enhancement ticket.


---

Comment by jhpalmieri created at 2010-04-14 05:24:03

See #8684 for a follow-up ticket, the purpose of which is to organize the graph theory stuff in the reference manual.  I'm not going to do this myself, since I don't know enough about graph theory in general, or the graph theory in Sage, to know how to organize it.


---

Comment by jhpalmieri created at 2010-04-14 05:24:03

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-16 18:46:01

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-16 18:46:01

Merged in 4.4.alpha0:
 - trac_8513_graph_theory_documentation-abm.patch
 - trac_8513_graph_theory_documentation-smallfixes.patch
 - trac_8513-reviewer.patch
