# Issue 8598: Add graphical output to operation tables

Issue created by migration from Trac.

Original creator: rbeezer

Original creation time: 2010-03-24 15:15:14

Assignee: was

Keywords: plotting, cayley table

Operation tables can be output as grids with color or grayscale squares representing the different elements of the algebraic structure.  Adding these into `sage.matrix.operation_table.OperationTable` would be a nice self-contained project for someone looking for a project involving plotting and graphics.  Despite the localized nature of the project, it would see wide applicability throughout Sage.  Look for stubs in the source code, 

I'm pretty sure Mathematica does this for groups (Cayley table), but I can't get Wolfram Alpha or MathWorld to cough it up again for me now that I want it.


---

Comment by @DaveWitteMorris created at 2020-05-26 21:45:24

Changing keywords from "plotting, cayley table" to "plotting, cayley table, beginner".


---

Comment by @DaveWitteMorris created at 2020-05-26 21:45:24

The basic functionality can be obtained from matplotlib by using `matrix_plot`:

```
sage: def color_table(OT, cmap):
....:     return matrix_plot(matrix(OT._table), cmap=cmap)

sage: import matplotlib.cm
sage: from sage.matrix.operation_table import OperationTable
sage: OT = OperationTable(SymmetricGroup(3), operation=operator.mul)
sage: color_table(OT, matplotlib.cm.gist_rainbow)
Launched png viewer for Graphics object consisting of 1 graphics primitive
```

However, this picture has an unwanted border with tick marks, and the names of group elements should (optionally) be put in the boxes. See the multiplication tables created by [Group Explorer](https://nathancarter.github.io/group-explorer/index.html) for what the output should look like.

As in Group Explorer, there should be an option to organize the elements of the group by the cosets of a subgroup H (and use the same color for all elements of each coset), but that could be moved to a separate ticket if it turns out to be difficult.

This project will require an understanding of matplotlib and basic abstract algebra (groups, subgroups, and cosets). It will only be useful for fairly small groups, so there should not be any need for clever optimizations. The source code for `OperationTable` has stubs for `color_table()` and `gray_table()`, but only the `color_table` method is needed, because gray-scale output can be obtained by choosing a grayscale colormap.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by @Bruno-TT created at 2022-10-24 15:35:18

I've just opened a PR here https://github.com/sagemath/sage/pull/109

Haven't contributed to sage before so please let me know if I've done anything wrong / need to do anything else!


---

Comment by @Bruno-TT created at 2022-10-24 15:35:36

Changing status from new to needs_review.


---

Comment by @Bruno-TT created at 2022-10-24 15:37:09

Replying to [comment:1 Dave Morris]:
> The basic functionality can be obtained from matplotlib by using `matrix_plot`:
> {{{
> sage: def color_table(OT, cmap):
> ....:     return matrix_plot(matrix(OT._table), cmap=cmap)
> 
> sage: import matplotlib.cm
> sage: from sage.matrix.operation_table import OperationTable
> sage: OT = OperationTable(SymmetricGroup(3), operation=operator.mul)
> sage: color_table(OT, matplotlib.cm.gist_rainbow)
> Launched png viewer for Graphics object consisting of 1 graphics primitive
> }}}
> However, this picture has an unwanted border with tick marks, and the names of group elements should (optionally) be put in the boxes. See the multiplication tables created by [Group Explorer](https://nathancarter.github.io/group-explorer/index.html) for what the output should look like.
> 
> As in Group Explorer, there should be an option to organize the elements of the group by the cosets of a subgroup H (and use the same color for all elements of each coset), but that could be moved to a separate ticket if it turns out to be difficult.
> 
> This project will require an understanding of matplotlib and basic abstract algebra (groups, subgroups, and cosets). It will only be useful for fairly small groups, so there should not be any need for clever optimizations. The source code for `OperationTable` has stubs for `color_table()` and `gray_table()`, but only the `color_table` method is needed, because gray-scale output can be obtained by choosing a grayscale colormap.


There's no immediately obvious way to implement coset functionality here, since the OperationTable type supports all magmas rather than just groups - I think we should have a separate ticket for this.


---

Comment by dimpase created at 2022-10-25 09:17:16

Replying to [comment:9 gh-Bruno-TT]:
> I've just opened a PR here https://github.com/sagemath/sage/pull/109
> 
> Haven't contributed to sage before so please let me know if I've done anything wrong / need to do anything else!

Could you please add a branch here? We don't take PRs on github yet.

To do so, upload a public ssh key from an ssh keypair to your github account, then
you can push your branch, whose name should have the correct prefix, `u/gh-Bruno-TT/...`


```shell
$ git remote add trac git`@`trac.sagemath.org:sage.git
$ git checkout -b u/gh-Bruno-TT/ticket_8598 # or something like this
$ git puch trac HEAD
```


and add the branch name, i.e. `u/gh-Bruno-TT/ticket_8598` into `Branch:` field.


---

Comment by @Bruno-TT created at 2022-10-31 16:12:26

New commits:


---

Comment by dimpase created at 2022-10-31 18:36:28

Thanks. 
Could you add `EXAMPLES:` section in the docstring to give a clue how to use it?


---

Comment by git created at 2022-11-01 17:25:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @Bruno-TT created at 2022-11-01 17:31:49

Replying to [comment:15 Dima Pasechnik]:
> Thanks. 
> Could you add `EXAMPLES:` section in the docstring to give a clue how to use it?
Done


---

Comment by git created at 2022-11-02 12:46:35

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2022-11-08 16:13:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dimpase created at 2022-11-16 12:26:58

while for magmas with a left and right identity the 1st column and the 1st row can be
served as lists of elements to multiply, this no longer is the case for more general objects. An option to have an extra row (and/or column) listing the elements might be useful then (and useful regardless, in fact).


---

Comment by dimpase created at 2022-11-16 13:14:19

in the HTML docs, I see weird

```
color_table(element_names=True, cmap=<matplotlib.colors.LinearSegmentedColormap object at 0x7fc24f7e10a0>, **options)
```

(not sure if this is easy to fix, it's probably a bug in our docbuilder)


Also, you'd remove TODO in the file in question - as this is precisely done in this ticket.

Finally, can you add a colour image (of a smallish, maybe 4x4 or so table) in the docs?
Hopefully it can be done using `PLOT` docstrings directive and `sphinx_plot()`, e.g. as in

```python
    EXAMPLES::

        sage: var('x,y,z')
        (x, y, z)

    A simple sphere::

        sage: implicit_plot3d(x^2+y^2+z^2==4, (x,-3,3), (y,-3,3), (z,-3,3))
        Graphics3d Object

    .. PLOT::

        var('x,y,z')
        F = x**2 + y**2 + z**2
        P = implicit_plot3d(F==4, (x,-3,3), (y,-3,3), (z,-3,3))
        sphinx_plot(P)
```

 
in `plot/plot3d/implicit_plot3d.py`


---

Comment by git created at 2022-12-17 18:19:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2022-12-17 18:24:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @Bruno-TT created at 2022-12-17 18:38:45

Replying to [comment:21 Dima Pasechnik]:
> in the HTML docs, I see weird
> {{{
> color_table(element_names=True, cmap=<matplotlib.colors.LinearSegmentedColormap object at 0x7fc24f7e10a0>, **options)
> }}}
> (not sure if this is easy to fix, it's probably a bug in our docbuilder)
I've pushed a little hack which copies the colormap object and overrides the `__repr__` method which fixes the docstring. That being said, it's quite ugly since it requires instantiating a new class (ReprOverrideLinearSegmentedColormap), and fiddling with the `__class__` attribute of the copied colormap object. Not sure if this is worth fixing a small glitch in the documentation, I'll let someone else be the judge of that.

> Also, you'd remove TODO in the file in question - as this is precisely done in this ticket.
Done

> Finally, can you add a colour image (of a smallish, maybe 4x4 or so table) in the docs?
> Hopefully it can be done using `PLOT` docstrings directive and `sphinx_plot()`, e.g. as in ...

I've spent quite a while trying to get this to work now but I'm getting stranger and stranger errors.
The docstring plot directive likes dealing with matplotlib plots rather than sage plots, however sage plots do have a matplotlib object underneath.
In theory it should be possible to work with the figure object returned by `color_table().matplotlib()`, however when I try and do this as described here
https://stackoverflow.com/questions/40965733/how-to-show-matplotlib-plot-from-a-figure-object
I get the following error



```
[sagemath_doc_html-none] [matrices ] .. PLOT::
[sagemath_doc_html-none] [matrices ]     import matplotlib.pyplot as plt
[sagemath_doc_html-none] [matrices ]     from sage.matrix.operation_table import OperationTable
[sagemath_doc_html-none] [matrices ]     from sage.all import SymmetricGroup, operator
[sagemath_doc_html-none] [matrices ]     OT = OperationTable(SymmetricGroup(3), operation=operator.mul)
[sagemath_doc_html-none] [matrices ]     fig = OT.color_table().matplotlib()
[sagemath_doc_html-none] [matrices ]     managed_fig=plt.figure()
[sagemath_doc_html-none] [matrices ]     canvas_manager = managed_fig.canvas.manager
[sagemath_doc_html-none] [matrices ]     canvas_manager.canvas.figure=fig
[sagemath_doc_html-none] [matrices ]     fig.set_canvas(canvas_manager.canvas)
[sagemath_doc_html-none] [matrices ]     plt.show()
[sagemath_doc_html-none] [matrices ] The inventory files are in ../../local/share/doc/sage/inventory/en/reference/matrices.
[sagemath_doc_html-none] Error building the documentation.
[sagemath_doc_html-none] Traceback (most recent call last):
[sagemath_doc_html-none]   File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
[sagemath_doc_html-none]     return _run_code(code, main_globals, None,
[sagemath_doc_html-none]   File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
[sagemath_doc_html-none]     exec(code, run_globals)
[sagemath_doc_html-none]   File "/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/__main__.py", line 498, in <module>
[sagemath_doc_html-none]     sys.exit(main())
[sagemath_doc_html-none]   File "/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/__main__.py", line 495, in main
[sagemath_doc_html-none]     builder()
[sagemath_doc_html-none]   File "/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/builders.py", line 819, in _wrapper
[sagemath_doc_html-none]     getattr(DocBuilder, build_type)(self, *args, **kwds)
[sagemath_doc_html-none]   File "/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/builders.py", line 163, in f
[sagemath_doc_html-none]     runsphinx()
[sagemath_doc_html-none]   File "/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/sphinxbuild.py", line 327, in runsphinx
[sagemath_doc_html-none]     sys.stderr.raise_errors()
[sagemath_doc_html-none]   File "/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/sphinxbuild.py", line 263, in raise_errors
[sagemath_doc_html-none]     raise OSError(self._error)
[sagemath_doc_html-none] OSError: /home/bruno/Documents/sage/src/sage/matrix/operation_table.py:docstring of sage.matrix.operation_table.OperationTable.color_table:19: ERROR: Error in "PLOT" directive:
[sagemath_doc_html-none] 
[sagemath_doc_html-none]     Note: incremental documentation builds sometimes cause spurious
[sagemath_doc_html-none]     error messages. To be certain that these are real errors, run
[sagemath_doc_html-none]     "make doc-clean doc-uninstall" first and try again.
[sagemath_doc_html-none] make[6]: *** [Makefile:27: doc-inventory--reference-matrices] Error 1
```


If anyone has any insight into how to do this please let me know, I'm out of my depth. 

Trying to invoke `.show()` on the figure object or the sage plot object both yield a similar error.


---

Comment by dimpase created at 2022-12-17 23:05:42

fix for plot is easy; all you need to call `sphinx_plot(foo)` is that `foo.plot()` can be called.
(my branch is rebased over the latest beta (always good), and the last commit does this fix)


This as written in https://doc.sagemath.org/html/en/developer/coding_basics.html (look up PLOT plot there). Admittedly, it's not easy to find - I used `git grep PLOT` to find that entry, and just read `src/doc/en/developer/coding_basics.rst` - from which a part of the above doc is built.
We certainly need to fix the index there, it's very poor, sorry.

 
----
New commits:


---

Comment by dimpase created at 2022-12-17 23:08:26

Sorry, I should have told you a quick way to rebuild only this part of docs:

```
./sage --docbuild --no-pdf-links reference/matrices html --no-prune-empty-dirs
```

(something one can figure out by reading the log of docbuild...)


---

Comment by git created at 2022-12-18 14:28:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2022-12-19 10:34:04

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2022-12-19 10:46:35

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by dimpase created at 2022-12-19 10:48:12

Changing status from needs_review to positive_review.


---

Comment by dimpase created at 2022-12-19 10:48:12

OK, looks good enough now. I took out the documentation hack - now it looks not necessary, in fact (no idea why)


---

Comment by @Bruno-TT created at 2022-12-19 16:15:50

New commits:


---

Comment by dimpase created at 2022-12-19 17:05:01

OK, fine, thanks.
