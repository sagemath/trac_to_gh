# Issue 6525: Enabling some GraphLatex options that were hard coded.

Issue created by migration from Trac.

Original creator: fidelbarrera

Original creation time: 2009-07-13 18:04:53

Assignee: rlm

CC:  rbeezer

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



---

Comment by fidelbarrera created at 2009-07-13 18:06:32

Hard coded latex options for combinatorial graphs enabled.


---

Attachment


---

Comment by rbeezer created at 2009-07-14 05:59:12

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

Comment by fidelbarrera created at 2009-07-21 12:40:07

Some hard coded LaTeX options enabled. Please apply on top of graph_latex_options.patch


---

Attachment

Attached patch file (`graph_latex_options-2.patch`) features

1. Spelling of "whether" fixed.

2. Removed some blank lines in docstrings.

3. `ValueError` exception is raised instead of printing error message.

4. Errors for unknown values for options are now trapped when the option is set, this is in `GraphLatex.set_option()`.

4.1 In `GraphLatex.set_option()`, if `option_name` is `None`, the value of `option_name` is set to its default value, instead of deleting the option.

5. Docstrings were updated.


---

Comment by rbeezer created at 2009-07-23 05:02:21

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
