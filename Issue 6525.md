# Issue 6525: Enabling some GraphLatex options that were hard coded.

archive/issues_006525.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  @rbeezer\n\nKeywords: latex, graph, graphlatex\n\nNow that `latex(G)` has been enabled for combinatorial graphs,\nsome of the options in the graph latex class are still hard coded. Some of these options are now being enabled to have more control over the graph latex options.\n\nPreviously\n\n```\nsage: G.latex_options()\nLaTeX options for Graph on 7 vertices: {'tkz_style': 'Normal'}\n```\n\nWith the attached patch\n\n```\nsage: G.latex_options()\nLaTeX options for Graph on 7 vertices: {'tkz_style': 'Normal', 'units': 'cm', 'labels': True, \n'layout': '', 'vertex_math': True}\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/6525\n\n",
    "created_at": "2009-07-13T18:04:53Z",
    "labels": [
        "component: graph theory",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-feature",
    "title": "Enabling some GraphLatex options that were hard coded.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6525",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```
Assignee: @rlmill

CC:  @rbeezer

Keywords: latex, graph, graphlatex

Now that `latex(G)` has been enabled for combinatorial graphs,
some of the options in the graph latex class are still hard coded. Some of these options are now being enabled to have more control over the graph latex options.

Previously

```
sage: G.latex_options()
LaTeX options for Graph on 7 vertices: {'tkz_style': 'Normal'}
```

With the attached patch

```
sage: G.latex_options()
LaTeX options for Graph on 7 vertices: {'tkz_style': 'Normal', 'units': 'cm', 'labels': True, 
'layout': '', 'vertex_math': True}
```

Issue created by migration from https://trac.sagemath.org/ticket/6525





---

archive/issue_comments_053113.json:
```json
{
    "body": "Hard coded latex options for combinatorial graphs enabled.",
    "created_at": "2009-07-13T18:06:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6525#issuecomment-53113",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Hard coded latex options for combinatorial graphs enabled.



---

archive/issue_comments_053114.json:
```json
{
    "body": "Attachment [graph_latex_options.patch](tarball://root/attachments/some-uuid/ticket6525/graph_latex_options.patch) by mvngu created at 2009-07-13 22:21:53",
    "created_at": "2009-07-13T22:21:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6525#issuecomment-53114",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [graph_latex_options.patch](tarball://root/attachments/some-uuid/ticket6525/graph_latex_options.patch) by mvngu created at 2009-07-13 22:21:53



---

archive/issue_comments_053115.json:
```json
{
    "body": "1.  Spelling:  \"whether\" (not \"wether\") in a couple places.\n\n2.  In the docstrings, you don't need blank lines to separate list items.  Too many blank lines and the text versions from tab completion get spread-out.  But a few (like at the end of long sub-lists) I think are helpful.\n\n3.  Should probably raise a `ValueError` when input is bad, such as \n\n```\nif not units in ['in','mm','cm','pt', 'em', 'ex']:\n    print 'Unknown units: %s.  Must be one of: in, mm, cm, pt, em, ex'% units\n    return\n```\n\nbecomes (note lower case, no periods)\n\n```\nif not units in ['in','mm','cm','pt', 'em', 'ex']:\n    raise ValueError('unknown units: %s, must be one of: in, mm, cm, pt, em, ex'% units)\n```\n\nMight want to test some of these error messages with doctests.\n\n4.  Would it make sense to trap errors like the one above when it is set (ie in `GraphLatex.set_option()`?  It is possible some errors won't be apparent until it is time to plot, but the one above could be caught when the option is set.  But maybe it is best to put all the error-checking in the routine building the latex code?  Probably so, especially if there is ever support for some other latex graph drawing package.\n\n5.  About 11 doctests fail for me - they all look trivial - just update the options produced since there are now default values for several new options.  All the latex code seems alright, as you would expect/hope.\n\n6.  Once there are a few more options available, I'll expand the documentation at the top of the module to advertise the possibilities.",
    "created_at": "2009-07-14T05:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6525#issuecomment-53115",
    "user": "https://github.com/rbeezer"
}
```

1.  Spelling:  "whether" (not "wether") in a couple places.

2.  In the docstrings, you don't need blank lines to separate list items.  Too many blank lines and the text versions from tab completion get spread-out.  But a few (like at the end of long sub-lists) I think are helpful.

3.  Should probably raise a `ValueError` when input is bad, such as 

```
if not units in ['in','mm','cm','pt', 'em', 'ex']:
    print 'Unknown units: %s.  Must be one of: in, mm, cm, pt, em, ex'% units
    return
```

becomes (note lower case, no periods)

```
if not units in ['in','mm','cm','pt', 'em', 'ex']:
    raise ValueError('unknown units: %s, must be one of: in, mm, cm, pt, em, ex'% units)
```

Might want to test some of these error messages with doctests.

4.  Would it make sense to trap errors like the one above when it is set (ie in `GraphLatex.set_option()`?  It is possible some errors won't be apparent until it is time to plot, but the one above could be caught when the option is set.  But maybe it is best to put all the error-checking in the routine building the latex code?  Probably so, especially if there is ever support for some other latex graph drawing package.

5.  About 11 doctests fail for me - they all look trivial - just update the options produced since there are now default values for several new options.  All the latex code seems alright, as you would expect/hope.

6.  Once there are a few more options available, I'll expand the documentation at the top of the module to advertise the possibilities.



---

archive/issue_comments_053116.json:
```json
{
    "body": "Some hard coded LaTeX options enabled. Please apply on top of graph_latex_options.patch",
    "created_at": "2009-07-21T12:40:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6525#issuecomment-53116",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Some hard coded LaTeX options enabled. Please apply on top of graph_latex_options.patch



---

archive/issue_comments_053117.json:
```json
{
    "body": "Attachment [graph_latex_options-2.patch](tarball://root/attachments/some-uuid/ticket6525/graph_latex_options-2.patch) by fidelbarrera created at 2009-07-21 12:51:43\n\nAttached patch file (`graph_latex_options-2.patch`) features\n\n1. Spelling of \"whether\" fixed.\n\n2. Removed some blank lines in docstrings.\n\n3. `ValueError` exception is raised instead of printing error message.\n\n4. Errors for unknown values for options are now trapped when the option is set, this is in `GraphLatex.set_option()`.\n\n4.1 In `GraphLatex.set_option()`, if `option_name` is `None`, the value of `option_name` is set to its default value, instead of deleting the option.\n\n5. Docstrings were updated.",
    "created_at": "2009-07-21T12:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6525#issuecomment-53117",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Attachment [graph_latex_options-2.patch](tarball://root/attachments/some-uuid/ticket6525/graph_latex_options-2.patch) by fidelbarrera created at 2009-07-21 12:51:43

Attached patch file (`graph_latex_options-2.patch`) features

1. Spelling of "whether" fixed.

2. Removed some blank lines in docstrings.

3. `ValueError` exception is raised instead of printing error message.

4. Errors for unknown values for options are now trapped when the option is set, this is in `GraphLatex.set_option()`.

4.1 In `GraphLatex.set_option()`, if `option_name` is `None`, the value of `option_name` is set to its default value, instead of deleting the option.

5. Docstrings were updated.



---

archive/issue_comments_053118.json:
```json
{
    "body": "Hi Fidel,\n\nThis looks good and passes all tests.  I like setting an option back to its default when None is passed in on the `set_option()` and putting the input checks there look good.\n\nOne concern, which I should have thought of earlier.\n\n```\nsage: G=graph.PetersenGraph()\nsage: opts = G.latex_options()\nsage: opts\n```\n\nprints a dictionary, whose order is not guaranteed, so doctests that use this construction could fail just for being in the \"wrong\" order.  Even though the new tests all passed for me.  When there was only one option, it wasn't a problem.\n\nTwo options would be:\n\n1.  Use `G.get_option('foo')` to just test specific option(s) that are affected in a test.\n\n2.  Do something like \n\n```\nsage: G=graph.PetersenGraph()\nsage: opts = G.latex_options()\nsage: sorted(list(opts._options.items()))\n```\n\nwhich will provide unique output.  I don't like this as much since it uses the \"hidden\" atrribute `_options` which is best not exposed in the reference manual.  Maybe you could add a `get_options()` method that simply returned `_options` which could be mashed into the sorted list in a doctest which needs to see the whole range of options (like testing all the defaults at once).\n\nAgain, I should have thought of this sooner, but I think it needs to be changed before this gets merged.  I'll try to look at it right away once you make the changes.",
    "created_at": "2009-07-23T05:02:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6525",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6525#issuecomment-53118",
    "user": "https://github.com/rbeezer"
}
```

Hi Fidel,

This looks good and passes all tests.  I like setting an option back to its default when None is passed in on the `set_option()` and putting the input checks there look good.

One concern, which I should have thought of earlier.

```
sage: G=graph.PetersenGraph()
sage: opts = G.latex_options()
sage: opts
```

prints a dictionary, whose order is not guaranteed, so doctests that use this construction could fail just for being in the "wrong" order.  Even though the new tests all passed for me.  When there was only one option, it wasn't a problem.

Two options would be:

1.  Use `G.get_option('foo')` to just test specific option(s) that are affected in a test.

2.  Do something like 

```
sage: G=graph.PetersenGraph()
sage: opts = G.latex_options()
sage: sorted(list(opts._options.items()))
```

which will provide unique output.  I don't like this as much since it uses the "hidden" atrribute `_options` which is best not exposed in the reference manual.  Maybe you could add a `get_options()` method that simply returned `_options` which could be mashed into the sorted list in a doctest which needs to see the whole range of options (like testing all the defaults at once).

Again, I should have thought of this sooner, but I think it needs to be changed before this gets merged.  I'll try to look at it right away once you make the changes.
