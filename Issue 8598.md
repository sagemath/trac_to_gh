# Issue 8598: Add graphical output to operation tables

archive/issues_008598.json:
```json
{
    "body": "Assignee: was\n\nKeywords: plotting, cayley table\n\nOperation tables can be output as grids with color or grayscale squares representing the different elements of the algebraic structure.  Adding these into `sage.matrix.operation_table.OperationTable` would be a nice self-contained project for someone looking for a project involving plotting and graphics.  Despite the localized nature of the project, it would see wide applicability throughout Sage.  Look for stubs in the source code, \n\nI'm pretty sure Mathematica does this for groups (Cayley table), but I can't get Wolfram Alpha or MathWorld to cough it up again for me now that I want it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8598\n\n",
    "created_at": "2010-03-24T15:15:14Z",
    "labels": [
        "graphics",
        "minor",
        "enhancement"
    ],
    "title": "Add graphical output to operation tables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8598",
    "user": "rbeezer"
}
```
Assignee: was

Keywords: plotting, cayley table

Operation tables can be output as grids with color or grayscale squares representing the different elements of the algebraic structure.  Adding these into `sage.matrix.operation_table.OperationTable` would be a nice self-contained project for someone looking for a project involving plotting and graphics.  Despite the localized nature of the project, it would see wide applicability throughout Sage.  Look for stubs in the source code, 

I'm pretty sure Mathematica does this for groups (Cayley table), but I can't get Wolfram Alpha or MathWorld to cough it up again for me now that I want it.

Issue created by migration from https://trac.sagemath.org/ticket/8598





---

archive/issue_comments_077844.json:
```json
{
    "body": "Changing keywords from \"plotting, cayley table\" to \"plotting, cayley table, beginner\".",
    "created_at": "2020-05-26T21:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77844",
    "user": "@DaveWitteMorris"
}
```

Changing keywords from "plotting, cayley table" to "plotting, cayley table, beginner".



---

archive/issue_comments_077845.json:
```json
{
    "body": "The basic functionality can be obtained from matplotlib by using `matrix_plot`:\n\n```\nsage: def color_table(OT, cmap):\n....:     return matrix_plot(matrix(OT._table), cmap=cmap)\n\nsage: import matplotlib.cm\nsage: from sage.matrix.operation_table import OperationTable\nsage: OT = OperationTable(SymmetricGroup(3), operation=operator.mul)\nsage: color_table(OT, matplotlib.cm.gist_rainbow)\nLaunched png viewer for Graphics object consisting of 1 graphics primitive\n```\n\nHowever, this picture has an unwanted border with tick marks, and the names of group elements should (optionally) be put in the boxes. See the multiplication tables created by [Group Explorer](https://nathancarter.github.io/group-explorer/index.html) for what the output should look like.\n\nAs in Group Explorer, there should be an option to organize the elements of the group by the cosets of a subgroup H (and use the same color for all elements of each coset), but that could be moved to a separate ticket if it turns out to be difficult.\n\nThis project will require an understanding of matplotlib and basic abstract algebra (groups, subgroups, and cosets). It will only be useful for fairly small groups, so there should not be any need for clever optimizations. The source code for `OperationTable` has stubs for `color_table()` and `gray_table()`, but only the `color_table` method is needed, because gray-scale output can be obtained by choosing a grayscale colormap.",
    "created_at": "2020-05-26T21:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77845",
    "user": "@DaveWitteMorris"
}
```

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

archive/issue_comments_077846.json:
```json
{
    "body": "Setting new milestone based on a cursory review of ticket status, priority, and last modification date.",
    "created_at": "2021-02-13T20:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77846",
    "user": "mkoeppe"
}
```

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.



---

archive/issue_comments_077847.json:
```json
{
    "body": "I've just opened a PR here https://github.com/sagemath/sage/pull/109\n\nHaven't contributed to sage before so please let me know if I've done anything wrong / need to do anything else!",
    "created_at": "2022-10-24T15:35:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77847",
    "user": "@Bruno-TT"
}
```

I've just opened a PR here https://github.com/sagemath/sage/pull/109

Haven't contributed to sage before so please let me know if I've done anything wrong / need to do anything else!



---

archive/issue_comments_077848.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2022-10-24T15:35:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77848",
    "user": "@Bruno-TT"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_077849.json:
```json
{
    "body": "Replying to [comment:1 Dave Morris]:\n> The basic functionality can be obtained from matplotlib by using `matrix_plot`:\n> {{{\n> sage: def color_table(OT, cmap):\n> ....:     return matrix_plot(matrix(OT._table), cmap=cmap)\n> \n> sage: import matplotlib.cm\n> sage: from sage.matrix.operation_table import OperationTable\n> sage: OT = OperationTable(SymmetricGroup(3), operation=operator.mul)\n> sage: color_table(OT, matplotlib.cm.gist_rainbow)\n> Launched png viewer for Graphics object consisting of 1 graphics primitive\n> }}}\n> However, this picture has an unwanted border with tick marks, and the names of group elements should (optionally) be put in the boxes. See the multiplication tables created by [Group Explorer](https://nathancarter.github.io/group-explorer/index.html) for what the output should look like.\n> \n> As in Group Explorer, there should be an option to organize the elements of the group by the cosets of a subgroup H (and use the same color for all elements of each coset), but that could be moved to a separate ticket if it turns out to be difficult.\n> \n> This project will require an understanding of matplotlib and basic abstract algebra (groups, subgroups, and cosets). It will only be useful for fairly small groups, so there should not be any need for clever optimizations. The source code for `OperationTable` has stubs for `color_table()` and `gray_table()`, but only the `color_table` method is needed, because gray-scale output can be obtained by choosing a grayscale colormap.\n\n\nThere's no immediately obvious way to implement coset functionality here, since the OperationTable type supports all magmas rather than just groups - I think we should have a separate ticket for this.",
    "created_at": "2022-10-24T15:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77849",
    "user": "@Bruno-TT"
}
```

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

archive/issue_comments_077850.json:
```json
{
    "body": "Replying to [comment:9 gh-Bruno-TT]:\n> I've just opened a PR here https://github.com/sagemath/sage/pull/109\n> \n> Haven't contributed to sage before so please let me know if I've done anything wrong / need to do anything else!\n\nCould you please add a branch here? We don't take PRs on github yet.\n\nTo do so, upload a public ssh key from an ssh keypair to your github account, then\nyou can push your branch, whose name should have the correct prefix, `u/gh-Bruno-TT/...`\n\n\n```shell\n$ git remote add trac git@trac.sagemath.org:sage.git\n$ git checkout -b u/gh-Bruno-TT/ticket_8598 # or something like this\n$ git puch trac HEAD\n```\n\n\nand add the branch name, i.e. `u/gh-Bruno-TT/ticket_8598` into `Branch:` field.",
    "created_at": "2022-10-25T09:17:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77850",
    "user": "dimpase"
}
```

Replying to [comment:9 gh-Bruno-TT]:
> I've just opened a PR here https://github.com/sagemath/sage/pull/109
> 
> Haven't contributed to sage before so please let me know if I've done anything wrong / need to do anything else!

Could you please add a branch here? We don't take PRs on github yet.

To do so, upload a public ssh key from an ssh keypair to your github account, then
you can push your branch, whose name should have the correct prefix, `u/gh-Bruno-TT/...`


```shell
$ git remote add trac git@trac.sagemath.org:sage.git
$ git checkout -b u/gh-Bruno-TT/ticket_8598 # or something like this
$ git puch trac HEAD
```


and add the branch name, i.e. `u/gh-Bruno-TT/ticket_8598` into `Branch:` field.



---

archive/issue_comments_077851.json:
```json
{
    "body": "New commits:",
    "created_at": "2022-10-31T16:12:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77851",
    "user": "@Bruno-TT"
}
```

New commits:



---

archive/issue_comments_077852.json:
```json
{
    "body": "Thanks. \nCould you add `EXAMPLES:` section in the docstring to give a clue how to use it?",
    "created_at": "2022-10-31T18:36:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77852",
    "user": "dimpase"
}
```

Thanks. 
Could you add `EXAMPLES:` section in the docstring to give a clue how to use it?



---

archive/issue_comments_077853.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-11-01T17:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77853",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077854.json:
```json
{
    "body": "Replying to [comment:15 Dima Pasechnik]:\n> Thanks. \n> Could you add `EXAMPLES:` section in the docstring to give a clue how to use it?\nDone",
    "created_at": "2022-11-01T17:31:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77854",
    "user": "@Bruno-TT"
}
```

Replying to [comment:15 Dima Pasechnik]:
> Thanks. 
> Could you add `EXAMPLES:` section in the docstring to give a clue how to use it?
Done



---

archive/issue_comments_077855.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-11-02T12:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77855",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077856.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-11-08T16:13:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77856",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077857.json:
```json
{
    "body": "while for magmas with a left and right identity the 1st column and the 1st row can be\nserved as lists of elements to multiply, this no longer is the case for more general objects. An option to have an extra row (and/or column) listing the elements might be useful then (and useful regardless, in fact).",
    "created_at": "2022-11-16T12:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77857",
    "user": "dimpase"
}
```

while for magmas with a left and right identity the 1st column and the 1st row can be
served as lists of elements to multiply, this no longer is the case for more general objects. An option to have an extra row (and/or column) listing the elements might be useful then (and useful regardless, in fact).



---

archive/issue_comments_077858.json:
```json
{
    "body": "in the HTML docs, I see weird\n\n```\ncolor_table(element_names=True, cmap=<matplotlib.colors.LinearSegmentedColormap object at 0x7fc24f7e10a0>, **options)\n```\n\n(not sure if this is easy to fix, it's probably a bug in our docbuilder)\n\n\nAlso, you'd remove TODO in the file in question - as this is precisely done in this ticket.\n\nFinally, can you add a colour image (of a smallish, maybe 4x4 or so table) in the docs?\nHopefully it can be done using `PLOT` docstrings directive and `sphinx_plot()`, e.g. as in\n\n```python\n    EXAMPLES::\n\n        sage: var('x,y,z')\n        (x, y, z)\n\n    A simple sphere::\n\n        sage: implicit_plot3d(x^2+y^2+z^2==4, (x,-3,3), (y,-3,3), (z,-3,3))\n        Graphics3d Object\n\n    .. PLOT::\n\n        var('x,y,z')\n        F = x**2 + y**2 + z**2\n        P = implicit_plot3d(F==4, (x,-3,3), (y,-3,3), (z,-3,3))\n        sphinx_plot(P)\n```\n\n \nin `plot/plot3d/implicit_plot3d.py`",
    "created_at": "2022-11-16T13:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77858",
    "user": "dimpase"
}
```

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

archive/issue_comments_077859.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-12-17T18:19:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77859",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077860.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-12-17T18:24:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77860",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077861.json:
```json
{
    "body": "Replying to [comment:21 Dima Pasechnik]:\n> in the HTML docs, I see weird\n> {{{\n> color_table(element_names=True, cmap=<matplotlib.colors.LinearSegmentedColormap object at 0x7fc24f7e10a0>, **options)\n> }}}\n> (not sure if this is easy to fix, it's probably a bug in our docbuilder)\nI've pushed a little hack which copies the colormap object and overrides the `__repr__` method which fixes the docstring. That being said, it's quite ugly since it requires instantiating a new class (ReprOverrideLinearSegmentedColormap), and fiddling with the `__class__` attribute of the copied colormap object. Not sure if this is worth fixing a small glitch in the documentation, I'll let someone else be the judge of that.\n\n> Also, you'd remove TODO in the file in question - as this is precisely done in this ticket.\nDone\n\n> Finally, can you add a colour image (of a smallish, maybe 4x4 or so table) in the docs?\n> Hopefully it can be done using `PLOT` docstrings directive and `sphinx_plot()`, e.g. as in ...\n\nI've spent quite a while trying to get this to work now but I'm getting stranger and stranger errors.\nThe docstring plot directive likes dealing with matplotlib plots rather than sage plots, however sage plots do have a matplotlib object underneath.\nIn theory it should be possible to work with the figure object returned by `color_table().matplotlib()`, however when I try and do this as described here\nhttps://stackoverflow.com/questions/40965733/how-to-show-matplotlib-plot-from-a-figure-object\nI get the following error\n\n\n\n```\n[sagemath_doc_html-none] [matrices ] .. PLOT::\n[sagemath_doc_html-none] [matrices ]     import matplotlib.pyplot as plt\n[sagemath_doc_html-none] [matrices ]     from sage.matrix.operation_table import OperationTable\n[sagemath_doc_html-none] [matrices ]     from sage.all import SymmetricGroup, operator\n[sagemath_doc_html-none] [matrices ]     OT = OperationTable(SymmetricGroup(3), operation=operator.mul)\n[sagemath_doc_html-none] [matrices ]     fig = OT.color_table().matplotlib()\n[sagemath_doc_html-none] [matrices ]     managed_fig=plt.figure()\n[sagemath_doc_html-none] [matrices ]     canvas_manager = managed_fig.canvas.manager\n[sagemath_doc_html-none] [matrices ]     canvas_manager.canvas.figure=fig\n[sagemath_doc_html-none] [matrices ]     fig.set_canvas(canvas_manager.canvas)\n[sagemath_doc_html-none] [matrices ]     plt.show()\n[sagemath_doc_html-none] [matrices ] The inventory files are in ../../local/share/doc/sage/inventory/en/reference/matrices.\n[sagemath_doc_html-none] Error building the documentation.\n[sagemath_doc_html-none] Traceback (most recent call last):\n[sagemath_doc_html-none]   File \"/usr/lib/python3.8/runpy.py\", line 194, in _run_module_as_main\n[sagemath_doc_html-none]     return _run_code(code, main_globals, None,\n[sagemath_doc_html-none]   File \"/usr/lib/python3.8/runpy.py\", line 87, in _run_code\n[sagemath_doc_html-none]     exec(code, run_globals)\n[sagemath_doc_html-none]   File \"/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/__main__.py\", line 498, in <module>\n[sagemath_doc_html-none]     sys.exit(main())\n[sagemath_doc_html-none]   File \"/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/__main__.py\", line 495, in main\n[sagemath_doc_html-none]     builder()\n[sagemath_doc_html-none]   File \"/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/builders.py\", line 819, in _wrapper\n[sagemath_doc_html-none]     getattr(DocBuilder, build_type)(self, *args, **kwds)\n[sagemath_doc_html-none]   File \"/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/builders.py\", line 163, in f\n[sagemath_doc_html-none]     runsphinx()\n[sagemath_doc_html-none]   File \"/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/sphinxbuild.py\", line 327, in runsphinx\n[sagemath_doc_html-none]     sys.stderr.raise_errors()\n[sagemath_doc_html-none]   File \"/home/bruno/Documents/sage/pkgs/sage-docbuild/sage_docbuild/sphinxbuild.py\", line 263, in raise_errors\n[sagemath_doc_html-none]     raise OSError(self._error)\n[sagemath_doc_html-none] OSError: /home/bruno/Documents/sage/src/sage/matrix/operation_table.py:docstring of sage.matrix.operation_table.OperationTable.color_table:19: ERROR: Error in \"PLOT\" directive:\n[sagemath_doc_html-none] \n[sagemath_doc_html-none]     Note: incremental documentation builds sometimes cause spurious\n[sagemath_doc_html-none]     error messages. To be certain that these are real errors, run\n[sagemath_doc_html-none]     \"make doc-clean doc-uninstall\" first and try again.\n[sagemath_doc_html-none] make[6]: *** [Makefile:27: doc-inventory--reference-matrices] Error 1\n```\n\n\nIf anyone has any insight into how to do this please let me know, I'm out of my depth. \n\nTrying to invoke `.show()` on the figure object or the sage plot object both yield a similar error.",
    "created_at": "2022-12-17T18:38:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77861",
    "user": "@Bruno-TT"
}
```

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

archive/issue_comments_077862.json:
```json
{
    "body": "fix for plot is easy; all you need to call `sphinx_plot(foo)` is that `foo.plot()` can be called.\n(my branch is rebased over the latest beta (always good), and the last commit does this fix)\n\n\nThis as written in https://doc.sagemath.org/html/en/developer/coding_basics.html (look up PLOT plot there). Admittedly, it's not easy to find - I used `git grep PLOT` to find that entry, and just read `src/doc/en/developer/coding_basics.rst` - from which a part of the above doc is built.\nWe certainly need to fix the index there, it's very poor, sorry.\n\n \n----\nNew commits:",
    "created_at": "2022-12-17T23:05:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77862",
    "user": "dimpase"
}
```

fix for plot is easy; all you need to call `sphinx_plot(foo)` is that `foo.plot()` can be called.
(my branch is rebased over the latest beta (always good), and the last commit does this fix)


This as written in https://doc.sagemath.org/html/en/developer/coding_basics.html (look up PLOT plot there). Admittedly, it's not easy to find - I used `git grep PLOT` to find that entry, and just read `src/doc/en/developer/coding_basics.rst` - from which a part of the above doc is built.
We certainly need to fix the index there, it's very poor, sorry.

 
----
New commits:



---

archive/issue_comments_077863.json:
```json
{
    "body": "Sorry, I should have told you a quick way to rebuild only this part of docs:\n\n```\n./sage --docbuild --no-pdf-links reference/matrices html --no-prune-empty-dirs\n```\n\n(something one can figure out by reading the log of docbuild...)",
    "created_at": "2022-12-17T23:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77863",
    "user": "dimpase"
}
```

Sorry, I should have told you a quick way to rebuild only this part of docs:

```
./sage --docbuild --no-pdf-links reference/matrices html --no-prune-empty-dirs
```

(something one can figure out by reading the log of docbuild...)



---

archive/issue_comments_077864.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-12-18T14:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77864",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077865.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-12-19T10:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77865",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077866.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2022-12-19T10:46:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77866",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_077867.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-12-19T10:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77867",
    "user": "dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_077868.json:
```json
{
    "body": "OK, looks good enough now. I took out the documentation hack - now it looks not necessary, in fact (no idea why)",
    "created_at": "2022-12-19T10:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77868",
    "user": "dimpase"
}
```

OK, looks good enough now. I took out the documentation hack - now it looks not necessary, in fact (no idea why)



---

archive/issue_comments_077869.json:
```json
{
    "body": "New commits:",
    "created_at": "2022-12-19T16:15:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77869",
    "user": "@Bruno-TT"
}
```

New commits:



---

archive/issue_comments_077870.json:
```json
{
    "body": "OK, fine, thanks.",
    "created_at": "2022-12-19T17:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8598",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8598#issuecomment-77870",
    "user": "dimpase"
}
```

OK, fine, thanks.
