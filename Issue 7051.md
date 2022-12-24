# Issue 7051: latex issues

archive/issues_007051.json:
```json
{
    "body": "Assignee: jhpalmieri\n\nHere are several LaTeX issues:\n\n- because of how Python works (I think), if you set `T = type(identity_matrix(3))`, then T has all of the methods of an identity matrix.  In particular, if you run `latex(T)`, the code calls `hasattr(T, '_latex_')`, and this returns True because `hasattr(identity_matrix(3), '_latex_')` is True.  But then `T._latex_()` produces a `TypeError`.  This is the cause of the error reported [here](http://groups.google.com/group/sage-support/browse_frm/thread/498eb1dae179fc3f).\n\nSolution: catch `TypeError`s when calling `T._latex_()` in this sort of situation.\n\n- In the notebook, try \n\n``` \n%latex \n$\\sage{type(35)}$ \n```\n \nIn this case, Sage typesets the string `<type 'sage.rings.integer.Integer'>`, but the < and > signs get converted into an upside-down exclamation point and question mark. \n\nSolution: typeset strings differently, using `\\textttt` instead of `\\text`.\n\n- Click the \"Typeset\" button and try \n\n``` \ntype(35) \n```\n \nIn this case, jsMath kicks in and tries to typeset `\\text{<type 'sage.rings.integer.Integer'>`}, but the symbols < and > confuse jsMath -- it thinks they're part of an html command.  As a result, there is *no* output at all. \n\nSolution: for typesetting strings in jsMath, replace `\\texttt` with `\\hbox`.\n\n- This comes from a Sage doctest: \n\n``` \nsage: R.<x,y>=QQbar[] \nsage: latex(-x^2-y+1) \n-x^{2} - y + \\text{1} \n```\n \nThe `\\text{1`} should not be there.\n\nSolution: The `\\text{1`}  appears because the element 1 in R has no `_latex_` method, so it gets converted to a string, when then gets typeset by enclosing it in `\\text`.  So test strings: if they consist only of digits, just return the string.  If it contains anything else, enclose in `\\textttt`, as mentioned above.\n\nA patch will follow soon.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7051\n\n",
    "created_at": "2009-09-28T15:27:39Z",
    "labels": [
        "misc",
        "minor",
        "bug"
    ],
    "title": "latex issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7051",
    "user": "jhpalmieri"
}
```
Assignee: jhpalmieri

Here are several LaTeX issues:

- because of how Python works (I think), if you set `T = type(identity_matrix(3))`, then T has all of the methods of an identity matrix.  In particular, if you run `latex(T)`, the code calls `hasattr(T, '_latex_')`, and this returns True because `hasattr(identity_matrix(3), '_latex_')` is True.  But then `T._latex_()` produces a `TypeError`.  This is the cause of the error reported [here](http://groups.google.com/group/sage-support/browse_frm/thread/498eb1dae179fc3f).

Solution: catch `TypeError`s when calling `T._latex_()` in this sort of situation.

- In the notebook, try 

``` 
%latex 
$\sage{type(35)}$ 
```
 
In this case, Sage typesets the string `<type 'sage.rings.integer.Integer'>`, but the < and > signs get converted into an upside-down exclamation point and question mark. 

Solution: typeset strings differently, using `\textttt` instead of `\text`.

- Click the "Typeset" button and try 

``` 
type(35) 
```
 
In this case, jsMath kicks in and tries to typeset `\text{<type 'sage.rings.integer.Integer'>`}, but the symbols < and > confuse jsMath -- it thinks they're part of an html command.  As a result, there is *no* output at all. 

Solution: for typesetting strings in jsMath, replace `\texttt` with `\hbox`.

- This comes from a Sage doctest: 

``` 
sage: R.<x,y>=QQbar[] 
sage: latex(-x^2-y+1) 
-x^{2} - y + \text{1} 
```
 
The `\text{1`} should not be there.

Solution: The `\text{1`}  appears because the element 1 in R has no `_latex_` method, so it gets converted to a string, when then gets typeset by enclosing it in `\text`.  So test strings: if they consist only of digits, just return the string.  If it contains anything else, enclose in `\textttt`, as mentioned above.

A patch will follow soon.

Issue created by migration from https://trac.sagemath.org/ticket/7051





---

archive/issue_comments_058360.json:
```json
{
    "body": "I'm attaching a patch which implements all of the solutions discussed above.  When applied to version 4.1.2.alpha4, this passes all doctests on sage.math.\n\nIf you have questions about the design decision, say the appearance of strings typeset in `\\texttt` vs. `\\text`, well, for what it's worth, I tried to discuss some of these issues on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ae85918789e25f3b/71d71887154151cb?tvc=2#71d71887154151cb) a few months ago, but there was essentially no response.  With this version, typesetting Python strings via LaTeX will produce different looking output, but (a) I like the new look, and (b) this seemed like the best way to deal with symbols like <, >, and _.\n\nIf necessary, we can split this into several tickets, because the first issue (`_latex_` method for types) is separate from the others.",
    "created_at": "2009-09-28T20:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58360",
    "user": "jhpalmieri"
}
```

I'm attaching a patch which implements all of the solutions discussed above.  When applied to version 4.1.2.alpha4, this passes all doctests on sage.math.

If you have questions about the design decision, say the appearance of strings typeset in `\texttt` vs. `\text`, well, for what it's worth, I tried to discuss some of these issues on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/ae85918789e25f3b/71d71887154151cb?tvc=2#71d71887154151cb) a few months ago, but there was essentially no response.  With this version, typesetting Python strings via LaTeX will produce different looking output, but (a) I like the new look, and (b) this seemed like the best way to deal with symbols like <, >, and _.

If necessary, we can split this into several tickets, because the first issue (`_latex_` method for types) is separate from the others.



---

archive/issue_comments_058361.json:
```json
{
    "body": "Attachment [trac_7051-latex.patch](tarball://root/attachments/some-uuid/ticket7051/trac_7051-latex.patch) by timdumol created at 2009-10-01 13:36:12\n\nApplies well. Things look good here. Positive review.",
    "created_at": "2009-10-01T13:36:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58361",
    "user": "timdumol"
}
```

Attachment [trac_7051-latex.patch](tarball://root/attachments/some-uuid/ticket7051/trac_7051-latex.patch) by timdumol created at 2009-10-01 13:36:12

Applies well. Things look good here. Positive review.



---

archive/issue_comments_058362.json:
```json
{
    "body": "Attachment [trac_7051-latex.2.patch](tarball://root/attachments/some-uuid/ticket7051/trac_7051-latex.2.patch) by mhansen created at 2009-10-15 09:30:25",
    "created_at": "2009-10-15T09:30:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58362",
    "user": "mhansen"
}
```

Attachment [trac_7051-latex.2.patch](tarball://root/attachments/some-uuid/ticket7051/trac_7051-latex.2.patch) by mhansen created at 2009-10-15 09:30:25



---

archive/issue_comments_058363.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58363",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_058364.json:
```json
{
    "body": "I had to rebase the patch to get it to apply to my current tree.",
    "created_at": "2009-10-15T09:30:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58364",
    "user": "mhansen"
}
```

I had to rebase the patch to get it to apply to my current tree.



---

archive/issue_comments_058365.json:
```json
{
    "body": "If I evaluate\n\n```python\nhtml('$\\CDF$')\n```\n\nin the notebook, jsMath complains\n\n```\nUnknown control sequence '\\texttt'\n```\n\nIs this because `sage.misc.latex_macros.sage_jsmath_macros` contains\n\n```js\njsMath.Macro('CDF','\\\\\\\\texttt{Complex Double Field}');\n```\n\n?",
    "created_at": "2009-10-21T15:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58365",
    "user": "mpatel"
}
```

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

archive/issue_comments_058366.json:
```json
{
    "body": "In Sage 4.2.alpha0, if I evaluate\n\n```\nhtml('$\\CDF$')\n```\n\nin the notebook, I get the message \n\n```\nunknown control sequence '\\CDF'\n```\n\nI can't reproduce the error message about \\texttt, though.",
    "created_at": "2009-10-21T19:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58366",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_058367.json:
```json
{
    "body": "The sagenb spkg in 4.2.alpha0 and all more recent versions (to date) do not load the jsMath macros.  I'm working to fix this.  To see the `\\texttt` message, I did\n\n```python\nsage: from sage.misc.latex_macros import sage_jsmath_macros\nsage: for m in sage_jsmath_macros: print m\n```\n\nand inserted the definitions\n\n```js\njsMath.Macro('ZZ','\\\\Bold{Z}')\njsMath.Macro('RR','\\\\Bold{R}')\njsMath.Macro('CC','\\\\Bold{C}')\njsMath.Macro('QQ','\\\\Bold{Q}')\njsMath.Macro('QQbar','\\\\overline{\\\\QQ}')\njsMath.Macro('GF','\\\\Bold{F}_{#1}',1)\njsMath.Macro('Zp','\\\\ZZ_{#1}',1)\njsMath.Macro('Qp','\\\\QQ_{#1}',1)\njsMath.Macro('Zmod','\\\\ZZ/#1\\\\ZZ',1)\njsMath.Macro('CDF','\\\\texttt{Complex Double Field}')\njsMath.Macro('CIF','\\\\Bold{C}')\njsMath.Macro('CLF','\\\\Bold{C}')\njsMath.Macro('RDF','\\\\Bold{R}')\njsMath.Macro('RIF','\\\\Bold{I} \\\\Bold{R}')\njsMath.Macro('RLF','\\\\Bold{R}')\njsMath.Macro('CFF','\\\\Bold{CFF}')\njsMath.Macro('Bold','\\\\mathbf{#1}',1)\n```\n\ninto\n\n```\nSAGE_ROOT/local/lib/python/site-packages/sagenb/data/templates/notebook/head.tmpl\n```\n\nby hand.",
    "created_at": "2009-10-21T19:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58367",
    "user": "mpatel"
}
```

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

archive/issue_comments_058368.json:
```json
{
    "body": "You know, the right choice might be to remove 'CDF' from the list of macros.  After all, the whole point of the list is to be able to use `\\RR` in a docstring and have it look nice.  Using `\\CDF` in a docstring won't look very good with '\\\\texttt{Complex Double Field}' or any variant on it.  The only place I see '\\CDF' in the Sage library is in sage.misc.latex, where it comes from sage_jsmath_macros.  (I did `search_src('\\\\\\\\CDF')`.)  So I think we should delete it: it was a mistake of mine to include it in the first place.",
    "created_at": "2009-10-21T20:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58368",
    "user": "jhpalmieri"
}
```

You know, the right choice might be to remove 'CDF' from the list of macros.  After all, the whole point of the list is to be able to use `\RR` in a docstring and have it look nice.  Using `\CDF` in a docstring won't look very good with '\\texttt{Complex Double Field}' or any variant on it.  The only place I see '\CDF' in the Sage library is in sage.misc.latex, where it comes from sage_jsmath_macros.  (I did `search_src('\\\\CDF')`.)  So I think we should delete it: it was a mistake of mine to include it in the first place.



---

archive/issue_comments_058369.json:
```json
{
    "body": "Removal sounds good, but in case people use it outside the Sage library, should we ask on sage-*?",
    "created_at": "2009-10-21T20:21:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58369",
    "user": "mpatel"
}
```

Removal sounds good, but in case people use it outside the Sage library, should we ask on sage-*?



---

archive/issue_comments_058370.json:
```json
{
    "body": "unique name please",
    "created_at": "2017-07-19T08:52:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7051",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7051#issuecomment-58370",
    "user": "chapoton"
}
```

unique name please
