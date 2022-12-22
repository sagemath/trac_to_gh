# Issue 7051: latex issues

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-09-28 15:27:39

Assignee: jhpalmieri

Here are several LaTeX issues:

 - because of how Python works (I think), if you set `T = type(identity_matrix(3))`, then T has all of the methods of an identity matrix.  In particular, if you run `latex(T)`, the code calls `hasattr(T, '_latex_')`, and this returns True because `hasattr(identity_matrix(3), '_latex_')` is True.  But then `T._latex_()` produces a `TypeError`.  This is the cause of the error reported [here](http://groups.google.com/group/sage-support/browse_frm/thread/498eb1dae179fc3f).

Solution: catch `TypeError`s when calling `T._latex_()` in this sort of situation.

 - In the notebook, try 

``` 
%latex 
$\sage{type(35)}$ 
}}} 
In this case, Sage typesets the string `<type 'sage.rings.integer.Integer'>`, but the < and > signs get converted into an upside-down exclamation point and question mark. 

Solution: typeset strings differently, using `\textttt` instead of `\text`.

 - Click the "Typeset" button and try 
{{{ 
type(35) 
}}} 
In this case, jsMath kicks in and tries to typeset `\text{<type 'sage.rings.integer.Integer'>`}, but the symbols < and > confuse jsMath -- it thinks they're part of an html command.  As a result, there is *no* output at all. 

Solution: for typesetting strings in jsMath, replace `\texttt` with `\hbox`.

 - This comes from a Sage doctest: 
{{{ 
sage: R.<x,y>=QQbar[] 
sage: latex(-x^2-y+1) 
-x^{2} - y + \text{1} 
}}} 
The `\text{1`} should not be there.

Solution: The `\text{1`}  appears because the element 1 in R has no `_latex_` method, so it gets converted to a string, when then gets typeset by enclosing it in `\text`.  So test strings: if they consist only of digits, just return the string.  If it contains anything else, enclose in `\textttt`, as mentioned above.

A patch will follow soon.


---

Comment by jhpalmieri created at 2009-09-28 20:13:01

I'm attaching a patch which implements all of the solutions discussed above.  When applied to version 4.1.2.alpha4, this passes all doctests on sage.math.

If you have questions about the design decision, say the appearance of strings typeset in `\texttt` vs. `\text`, well, for what it's worth, I tried to discuss some of these issues on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ae85918789e25f3b/71d71887154151cb?tvc=2#71d71887154151cb) a few months ago, but there was essentially no response.  With this version, typesetting Python strings via LaTeX will produce different looking output, but (a) I like the new look, and (b) this seemed like the best way to deal with symbols like <, >, and _.

If necessary, we can split this into several tickets, because the first issue (`_latex_` method for types) is separate from the others.


---

Attachment

Applies well. Things look good here. Positive review.


---

Attachment


---

Comment by mhansen created at 2009-10-15 09:30:51

Resolution: fixed


---

Comment by mhansen created at 2009-10-15 09:30:51

I had to rebase the patch to get it to apply to my current tree.


---

Comment by mpatel created at 2009-10-21 15:25:42

If I evaluate

```python
html('$\CDF$')
```

in the notebook, jsMath complains

```
Unknown control sequence '\texttt'
```

Is this because `sage.misc.latex_macros.sage_jsmath_macros` contains

```js
jsMath.Macro('CDF','\\\\texttt{Complex Double Field}');
```

?


---

Comment by jhpalmieri created at 2009-10-21 19:09:07

In Sage 4.2.alpha0, if I evaluate

```
html('$\CDF$')
```

in the notebook, I get the message 

```
unknown control sequence '\CDF'
```

I can't reproduce the error message about \texttt, though.


---

Comment by mpatel created at 2009-10-21 19:53:31

The sagenb spkg in 4.2.alpha0 and all more recent versions (to date) do not load the jsMath macros.  I'm working to fix this.  To see the `\texttt` message, I did

```python
sage: from sage.misc.latex_macros import sage_jsmath_macros
sage: for m in sage_jsmath_macros: print m
```

and inserted the definitions

```js
jsMath.Macro('ZZ','\\Bold{Z}')
jsMath.Macro('RR','\\Bold{R}')
jsMath.Macro('CC','\\Bold{C}')
jsMath.Macro('QQ','\\Bold{Q}')
jsMath.Macro('QQbar','\\overline{\\QQ}')
jsMath.Macro('GF','\\Bold{F}_{#1}',1)
jsMath.Macro('Zp','\\ZZ_{#1}',1)
jsMath.Macro('Qp','\\QQ_{#1}',1)
jsMath.Macro('Zmod','\\ZZ/#1\\ZZ',1)
jsMath.Macro('CDF','\\texttt{Complex Double Field}')
jsMath.Macro('CIF','\\Bold{C}')
jsMath.Macro('CLF','\\Bold{C}')
jsMath.Macro('RDF','\\Bold{R}')
jsMath.Macro('RIF','\\Bold{I} \\Bold{R}')
jsMath.Macro('RLF','\\Bold{R}')
jsMath.Macro('CFF','\\Bold{CFF}')
jsMath.Macro('Bold','\\mathbf{#1}',1)
```

into

```
SAGE_ROOT/local/lib/python/site-packages/sagenb/data/templates/notebook/head.tmpl
```

by hand.


---

Comment by jhpalmieri created at 2009-10-21 20:14:40

You know, the right choice might be to remove 'CDF' from the list of macros.  After all, the whole point of the list is to be able to use `\RR` in a docstring and have it look nice.  Using `\CDF` in a docstring won't look very good with '\\texttt{Complex Double Field}' or any variant on it.  The only place I see '\CDF' in the Sage library is in sage.misc.latex, where it comes from sage_jsmath_macros.  (I did `search_src('\\\\CDF')`.)  So I think we should delete it: it was a mistake of mine to include it in the first place.


---

Comment by mpatel created at 2009-10-21 20:21:41

Removal sounds good, but in case people use it outside the Sage library, should we ask on sage-*?


---

Comment by chapoton created at 2017-07-19 08:52:55

unique name please
