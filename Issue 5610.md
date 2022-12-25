# Issue 5610: [with patch, not ready for review?] LaTeX customization

archive/issues_005610.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nThis patch attempts to implement LaTeX customizations for the following things:\n\n1. matrix and vector delimiters (see #5474 -- this patch moves that code around)\n\n2. the use of plain bold vs. blackboard bold for ZZ, RR, etc.\n\nIt almost succeeds, except that I don't know how to get jsMath to display blackboard bold fonts, so it doesn't work completely in the notebook.  (This is why the ticket is labeled as not being ready for review.)\n\nHere's what it does: from the command line,\n\n\n```\nsage: latex_customize.use_blackboard_bold(True)\nsage: view(ZZ)\n```\n\n\nwill pop up a PDF or DVI file with a blackboard bold ZZ.  Similarly, in the notebook,\n\n```\nlatex_customize.use_blackboard_bold(True)\n```\n\nfollowed by a cell containing\n\n```\n%latex\n$\\ZZ$\n```\n\nwill show a blackboard bold Z.\n\nFrom either the command line or the notebook,\n\n```\nlatex_customize.set_vector_delimiters(\"\\\\langle\", \"\\\\rangle\")\nlatex_customize.set_matrix_delimiters(\"\\\\{\", \"]\")\n```\n\nwill change the left and right vector and matrix delimiters as indicated.\n\nThere are also tons of changes in the second patch of the sort \"\\mathbf{Q}\" --> \"\\QQ\".  The idea here is, first, to make the docstrings more readable, and second, to make it easy to change between \\mathbf and \\mathbb.  Note that \"\\QQ\" is defined (via #5555) as the output of the `_latex_` method for QQ which this patch redefines to be \"\\Bold{QQ}\", and setting `use_blackboard_bold` controls the definition of the command \"\\Bold\". \n\nNow, if you want to typeset the reference manual, say, with blackboard bold instead of the default bold, the PDF version is relatively easy: just create the latex version (`sage -docbuild reference latex`) and edit the preamble: change the definition of \\Bold, and run latex.  For the html version, you probably have to edit the definition of \\Bold in sage/misc/latex_macros.py, or add \\renewcommand{\\Bold}... in the right place in sage/doc/conf.py; then run `sage -b`, then build the docs. As you can see, I don't have very good ideas about how to change the reference manuals -- should there be a command-line switch to `sage -docbuild`? -- so please chime in if you think of something.\n\nSee [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/68cdf05b40303286) on sage-devel for some more discussion, especially about mathbf vs. mathbb.\n\nThis ticket depends on #5359, #5433, and #5568 (all of which will be part of Sage 3.4.1.alpha0), and also on #5555.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5610\n\n",
    "created_at": "2009-03-25T17:56:57Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.2",
    "title": "[with patch, not ready for review?] LaTeX customization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5610",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: @jhpalmieri

This patch attempts to implement LaTeX customizations for the following things:

1. matrix and vector delimiters (see #5474 -- this patch moves that code around)

2. the use of plain bold vs. blackboard bold for ZZ, RR, etc.

It almost succeeds, except that I don't know how to get jsMath to display blackboard bold fonts, so it doesn't work completely in the notebook.  (This is why the ticket is labeled as not being ready for review.)

Here's what it does: from the command line,


```
sage: latex_customize.use_blackboard_bold(True)
sage: view(ZZ)
```


will pop up a PDF or DVI file with a blackboard bold ZZ.  Similarly, in the notebook,

```
latex_customize.use_blackboard_bold(True)
```

followed by a cell containing

```
%latex
$\ZZ$
```

will show a blackboard bold Z.

From either the command line or the notebook,

```
latex_customize.set_vector_delimiters("\\langle", "\\rangle")
latex_customize.set_matrix_delimiters("\\{", "]")
```

will change the left and right vector and matrix delimiters as indicated.

There are also tons of changes in the second patch of the sort "\mathbf{Q}" --> "\QQ".  The idea here is, first, to make the docstrings more readable, and second, to make it easy to change between \mathbf and \mathbb.  Note that "\QQ" is defined (via #5555) as the output of the `_latex_` method for QQ which this patch redefines to be "\Bold{QQ}", and setting `use_blackboard_bold` controls the definition of the command "\Bold". 

Now, if you want to typeset the reference manual, say, with blackboard bold instead of the default bold, the PDF version is relatively easy: just create the latex version (`sage -docbuild reference latex`) and edit the preamble: change the definition of \Bold, and run latex.  For the html version, you probably have to edit the definition of \Bold in sage/misc/latex_macros.py, or add \renewcommand{\Bold}... in the right place in sage/doc/conf.py; then run `sage -b`, then build the docs. As you can see, I don't have very good ideas about how to change the reference manuals -- should there be a command-line switch to `sage -docbuild`? -- so please chime in if you think of something.

See [this thread](http://groups.google.com/group/sage-devel/browse_frm/thread/68cdf05b40303286) on sage-devel for some more discussion, especially about mathbf vs. mathbb.

This ticket depends on #5359, #5433, and #5568 (all of which will be part of Sage 3.4.1.alpha0), and also on #5555.

Issue created by migration from https://trac.sagemath.org/ticket/5610





---

archive/issue_comments_043709.json:
```json
{
    "body": "I think it looks good, but why \"latex_customize\" rather than just attaching methods to \"latex\"?",
    "created_at": "2009-03-25T18:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43709",
    "user": "https://github.com/robertwb"
}
```

I think it looks good, but why "latex_customize" rather than just attaching methods to "latex"?



---

archive/issue_comments_043710.json:
```json
{
    "body": "Replying to [comment:1 robertwb]:\n> I think it looks good, but why \"latex_customize\" rather than just attaching methods to \"latex\"? \n\nWell, when I tried to attach some methods to Latex, I got all sorts of weird doctesting errors for latex.py (all of the output for latex_variable_name acted as if EMBEDDED_MODE were True, for example).  I have no idea why, but I fixed it by setting it up like this.",
    "created_at": "2009-03-25T19:14:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43710",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:1 robertwb]:
> I think it looks good, but why "latex_customize" rather than just attaching methods to "latex"? 

Well, when I tried to attach some methods to Latex, I got all sorts of weird doctesting errors for latex.py (all of the output for latex_variable_name acted as if EMBEDDED_MODE were True, for example).  I have no idea why, but I fixed it by setting it up like this.



---

archive/issue_comments_043711.json:
```json
{
    "body": "Strange.",
    "created_at": "2009-03-25T19:41:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43711",
    "user": "https://github.com/robertwb"
}
```

Strange.



---

archive/issue_comments_043712.json:
```json
{
    "body": "I think I have the jsMath thing figured out: we need to install the blackboard bold font in the jsMath directory, so install the spkg at #5611 first.  Then in the notebook try things like:\n\n```\nlatex_customize.use_blackboard_bold(False) # the default setting\nview(ZZ)\n```\n\nversus\n\n```\nlatex_customize.use_blackboard_bold(True)\nview(ZZ)\n```\n",
    "created_at": "2009-03-25T21:58:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43712",
    "user": "https://github.com/jhpalmieri"
}
```

I think I have the jsMath thing figured out: we need to install the blackboard bold font in the jsMath directory, so install the spkg at #5611 first.  Then in the notebook try things like:

```
latex_customize.use_blackboard_bold(False) # the default setting
view(ZZ)
```

versus

```
latex_customize.use_blackboard_bold(True)
view(ZZ)
```




---

archive/issue_comments_043713.json:
```json
{
    "body": "[Here's a picture.](http://sage.math.washington.edu/home/palmieri/misc/bbold.png)  The last part -- the docstring -- relies on #5653.",
    "created_at": "2009-03-31T22:16:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43713",
    "user": "https://github.com/jhpalmieri"
}
```

[Here's a picture.](http://sage.math.washington.edu/home/palmieri/misc/bbold.png)  The last part -- the docstring -- relies on #5653.



---

archive/issue_comments_043714.json:
```json
{
    "body": "Replying to [comment:2 jhpalmieri]:\n> Replying to [comment:1 robertwb]:\n> > I think it looks good, but why \"latex_customize\" rather than just attaching methods to \"latex\"? \n> \n> Well, when I tried to attach some methods to Latex, I got all sorts of weird doctesting errors for latex.py (all of the output for latex_variable_name acted as if EMBEDDED_MODE were True, for example).  I have no idea why, but I fixed it by setting it up like this.\n\nJust to follow up, I think this is the same issue as discussed [in this thread on sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/320845a4c9b9c75f).  I would be happy to attach  methods to `latex` if we can get this straightened out.",
    "created_at": "2009-04-12T22:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43714",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:2 jhpalmieri]:
> Replying to [comment:1 robertwb]:
> > I think it looks good, but why "latex_customize" rather than just attaching methods to "latex"? 
> 
> Well, when I tried to attach some methods to Latex, I got all sorts of weird doctesting errors for latex.py (all of the output for latex_variable_name acted as if EMBEDDED_MODE were True, for example).  I have no idea why, but I fixed it by setting it up like this.

Just to follow up, I think this is the same issue as discussed [in this thread on sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/320845a4c9b9c75f).  I would be happy to attach  methods to `latex` if we can get this straightened out.



---

archive/issue_comments_043715.json:
```json
{
    "body": "Here are new versions of the patches.  There are two changes: they are rebased against 3.4.1.rc2, and I managed to fix the weird problem with doctests in latex.  Therefore we now have commands like `latex.set_matrix_delimiters` instead of `latex_customize.set_matrix_delimiters`.",
    "created_at": "2009-04-14T18:49:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43715",
    "user": "https://github.com/jhpalmieri"
}
```

Here are new versions of the patches.  There are two changes: they are rebased against 3.4.1.rc2, and I managed to fix the weird problem with doctests in latex.  Therefore we now have commands like `latex.set_matrix_delimiters` instead of `latex_customize.set_matrix_delimiters`.



---

archive/issue_comments_043716.json:
```json
{
    "body": "By the way, in addition the changes noted above, when I was changing all of instances of `\\mathbb{Z`} to `\\ZZ`, etc., I discovered that the docstrings in the file `sage/rings/padics/tutorial.py` were garbled, or were using no-longer-defined macros: they had things like \n\n```\n\\mathbb{Z}p = \\lim_{\\leftarrow n} \\mathbb{Z}pn\n```\n\nin it.  I believe that this is supposed to be (in the new notation)\n\n```\n\\ZZ_p = \\lim_{\\leftarrow n} \\ZZ/p^{n} \\ZZ\n```\n\nand I fixed as many of these issues as I saw.",
    "created_at": "2009-04-14T20:17:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43716",
    "user": "https://github.com/jhpalmieri"
}
```

By the way, in addition the changes noted above, when I was changing all of instances of `\mathbb{Z`} to `\ZZ`, etc., I discovered that the docstrings in the file `sage/rings/padics/tutorial.py` were garbled, or were using no-longer-defined macros: they had things like 

```
\mathbb{Z}p = \lim_{\leftarrow n} \mathbb{Z}pn
```

in it.  I believe that this is supposed to be (in the new notation)

```
\ZZ_p = \lim_{\leftarrow n} \ZZ/p^{n} \ZZ
```

and I fixed as many of these issues as I saw.



---

archive/issue_comments_043717.json:
```json
{
    "body": "This is really cool. I might recommend making the names a bit shorter, e.g. \n\n\n```\nlatex.blackboard_bold(...)\n```\n\n\nThis is just to be more similar to the way proof works for setting global settings. Also, \n\n\n```\nlatex.matrix_delimiters(...)\n```\n\n\nwhich would return them if no arguments are given.",
    "created_at": "2009-04-15T23:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43717",
    "user": "https://github.com/robertwb"
}
```

This is really cool. I might recommend making the names a bit shorter, e.g. 


```
latex.blackboard_bold(...)
```


This is just to be more similar to the way proof works for setting global settings. Also, 


```
latex.matrix_delimiters(...)
```


which would return them if no arguments are given.



---

archive/issue_comments_043718.json:
```json
{
    "body": "Replying to [comment:9 robertwb]:\n> This is really cool. I might recommend making the names a bit shorter, e.g. \n\nThat's a good idea.  Here's a new version of the patch doing that.",
    "created_at": "2009-04-16T01:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43718",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:9 robertwb]:
> This is really cool. I might recommend making the names a bit shorter, e.g. 

That's a good idea.  Here's a new version of the patch doing that.



---

archive/issue_comments_043719.json:
```json
{
    "body": "Second patch (\"-part2\") is mostly minor changes in docstrings, but fails on four files.  I'd suspect this is due to some of the recent work on improving doctests.  So comments below pertain to just applying the first patch and testing from there.\n\nThe new methods for setting matrix and vector delimiters are a very welcome addition, and the options for \"bolding\" rings provide a good example for future options like this.  One should note that work still needs to be done to make this work for all rings, this patch appears to only demonstrate use for ZZ and GF (though I could have missed some).\n\nThe use of an instance of the Latex class, named \"latex\" had me confused for a while, since now `latex.__call__` replaces the functionality of the old `latex()`.  Some commentary highlighting the `latex` instance in the source (at some point - either now, or later) might save others the same confusion.\n\n`sage -docbuild pdf reference` seemed to choke on the doctest for the `list_function` method in `misc/latex.py`.  I'm going to attach the generated TeX below, we'll see how it fares.  I also have a screen shot of the output.  Its pretty jumbled up, and in particular the `\\begin{array`} has a \"b\" that is some non-ASCII character, so I wonder if there is a missing backslash and the  b  is being escaped?\n\nI'm ready to give this a positive review with a rebased part2 patch and if the latex problem on the reference manual goes away.  Maybe the best thing to do is just excise the problematic doctest for now and bring it back in another patch.\n\n\n```\nEXAMPLES:\n\n\\begin{Verbatim}[commandchars=@\\[\\]]\n@PYGaO[sage: ]@PYGbd[from] @PYGaV[sage.misc.latex] @PYGbd[import] list@_function\n@PYGaO[sage: ]list@_function(@lb[]@PYGaw[1],@PYGaw[2],@PYGaw[3]@rb[])\n@PYGaa['\\left@lb[]1, ]\n\\end{Verbatim}\n\\end{quote}\n\n2, \n3right{]}'\n\\begin{quote}\n\nsage: latex({[}1,2,3{]})  \\# indirect doctest\nleft{[}1,\n2,\n3\n\\end{quote}\n\\end{quote}\n\\begin{description}\n\\item[ight{]}]\nsage: latex({[}Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9)){]}) \\# indirect doctest\nleft{[}left(\ufffdegin\\{array\\}\\{rrr\\}\n0 \\& 1 \\& 2 3 \\& 4 \\& 5 6 \\& 7 \\& 8\nend\\{array\\}\n\n\\item[ight),]\n\\textbackslash{}left(\ufffdegin\\{array\\}\\{rrr\\}\n0 \\& 1 \\& 2 3 \\& 4 \\& 5 6 \\& 7 \\& 8\nend\\{array\\}\n\n\\end{description}\n\night)\night{]}\n\\end{funcdesc}\n```\n",
    "created_at": "2009-04-20T03:37:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43719",
    "user": "https://github.com/rbeezer"
}
```

Second patch ("-part2") is mostly minor changes in docstrings, but fails on four files.  I'd suspect this is due to some of the recent work on improving doctests.  So comments below pertain to just applying the first patch and testing from there.

The new methods for setting matrix and vector delimiters are a very welcome addition, and the options for "bolding" rings provide a good example for future options like this.  One should note that work still needs to be done to make this work for all rings, this patch appears to only demonstrate use for ZZ and GF (though I could have missed some).

The use of an instance of the Latex class, named "latex" had me confused for a while, since now `latex.__call__` replaces the functionality of the old `latex()`.  Some commentary highlighting the `latex` instance in the source (at some point - either now, or later) might save others the same confusion.

`sage -docbuild pdf reference` seemed to choke on the doctest for the `list_function` method in `misc/latex.py`.  I'm going to attach the generated TeX below, we'll see how it fares.  I also have a screen shot of the output.  Its pretty jumbled up, and in particular the `\begin{array`} has a "b" that is some non-ASCII character, so I wonder if there is a missing backslash and the  b  is being escaped?

I'm ready to give this a positive review with a rebased part2 patch and if the latex problem on the reference manual goes away.  Maybe the best thing to do is just excise the problematic doctest for now and bring it back in another patch.


```
EXAMPLES:

\begin{Verbatim}[commandchars=@\[\]]
@PYGaO[sage: ]@PYGbd[from] @PYGaV[sage.misc.latex] @PYGbd[import] list@_function
@PYGaO[sage: ]list@_function(@lb[]@PYGaw[1],@PYGaw[2],@PYGaw[3]@rb[])
@PYGaa['\left@lb[]1, ]
\end{Verbatim}
\end{quote}

2, 
3right{]}'
\begin{quote}

sage: latex({[}1,2,3{]})  \# indirect doctest
left{[}1,
2,
3
\end{quote}
\end{quote}
\begin{description}
\item[ight{]}]
sage: latex({[}Matrix(ZZ,3,range(9)), Matrix(ZZ,3,range(9)){]}) \# indirect doctest
left{[}left(�egin\{array\}\{rrr\}
0 \& 1 \& 2 3 \& 4 \& 5 6 \& 7 \& 8
end\{array\}

\item[ight),]
\textbackslash{}left(�egin\{array\}\{rrr\}
0 \& 1 \& 2 3 \& 4 \& 5 6 \& 7 \& 8
end\{array\}

\end{description}

ight)
ight{]}
\end{funcdesc}
```




---

archive/issue_comments_043720.json:
```json
{
    "body": "Screenshot of garbled list_function() documentation (yellow highlight on \"indirect\" is from my search function)",
    "created_at": "2009-04-20T03:45:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43720",
    "user": "https://github.com/rbeezer"
}
```

Screenshot of garbled list_function() documentation (yellow highlight on "indirect" is from my search function)



---

archive/issue_comments_043721.json:
```json
{
    "body": "Attachment [list-function-pdf.png](tarball://root/attachments/some-uuid/ticket5610/list-function-pdf.png) by @jhpalmieri created at 2009-04-20 21:18:30\n\nReplying to [comment:11 rbeezer]:\n>The new methods for setting matrix and vector delimiters are a very welcome addition, and the options for \"bolding\" rings provide a good example for future options like this. One should note that work still needs to be done to make this work for all rings, this patch appears to only demonstrate use for ZZ and GF (though I could have missed some). \n\nThe second patch also changes QQ, RR, and CC.  It leaves `\\mathbb{P`} and `\\mathbb{A`} unchanged.  (The first patch includes only the core of the customization code, and the relevant files happened not to use QQ, RR, or CC.)\n\n> The use of an instance of the Latex class, named \"latex\" had me confused for a while, since now `latex.__call__` replaces the functionality of the old `latex()`.  Some commentary highlighting the `latex` instance in the source (at some point - either now, or later) might save others the same confusion.\n\nDoes this affect end-users, or just developers?  I mean, does `latex(blah)` behave the same as it used to?  I hope so -- that was my intention.  You're right, though, that the syntax from the development end is different, but that seemed like the nicest way to do the customization: as methods (which could be tab-completed) attached to latex.  Do you have suggestions about what sorts of comments to add?\n\n> `sage -docbuild pdf reference` seemed to choke on the doctest for the `list_function` method in `misc/latex.py`.  \n\nI think this is easy to fix: put an \"r\" in front of the triple quotes at the beginning of the docstring.  It was there originally, and then I deleted it (I don't know why) in the new version.\n\nI'll produce a new patch soon with the \"r\", and with part 2 rebased against 3.4.1.rc4.",
    "created_at": "2009-04-20T21:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43721",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [list-function-pdf.png](tarball://root/attachments/some-uuid/ticket5610/list-function-pdf.png) by @jhpalmieri created at 2009-04-20 21:18:30

Replying to [comment:11 rbeezer]:
>The new methods for setting matrix and vector delimiters are a very welcome addition, and the options for "bolding" rings provide a good example for future options like this. One should note that work still needs to be done to make this work for all rings, this patch appears to only demonstrate use for ZZ and GF (though I could have missed some). 

The second patch also changes QQ, RR, and CC.  It leaves `\mathbb{P`} and `\mathbb{A`} unchanged.  (The first patch includes only the core of the customization code, and the relevant files happened not to use QQ, RR, or CC.)

> The use of an instance of the Latex class, named "latex" had me confused for a while, since now `latex.__call__` replaces the functionality of the old `latex()`.  Some commentary highlighting the `latex` instance in the source (at some point - either now, or later) might save others the same confusion.

Does this affect end-users, or just developers?  I mean, does `latex(blah)` behave the same as it used to?  I hope so -- that was my intention.  You're right, though, that the syntax from the development end is different, but that seemed like the nicest way to do the customization: as methods (which could be tab-completed) attached to latex.  Do you have suggestions about what sorts of comments to add?

> `sage -docbuild pdf reference` seemed to choke on the doctest for the `list_function` method in `misc/latex.py`.  

I think this is easy to fix: put an "r" in front of the triple quotes at the beginning of the docstring.  It was there originally, and then I deleted it (I don't know why) in the new version.

I'll produce a new patch soon with the "r", and with part 2 rebased against 3.4.1.rc4.



---

archive/issue_comments_043722.json:
```json
{
    "body": "Replying to [comment:12 jhpalmieri]:\n> The second patch also changes QQ, RR, and CC.  It leaves `\\mathbb{P`} and `\\mathbb{A`} unchanged.  (The first patch includes only the core of the customization code, and the relevant files happened not to use QQ, RR, or CC.)\n\nOK, that explains the split.  ;-) \n\n> Does this affect end-users, or just developers?  I mean, does `latex(blah)` behave the same as it used to?  I hope so -- that was my intention.  \n\nI didn't notice any change from a user's perspective.  And maybe it was just the change that threw me.  I saw `def latex()` going away and it took me a while to figure out how the functionality came back.  I just thought for others reading the code it might help to make the definition of the `latex` instance more prominient with some source code comments.  Right now, it just seems to be slipped in there, when it is fairly important since users will be accessing/changing its contents.  I did like the way you made the change while preserving `latex()`.\n\n\n> I'll produce a new patch soon with the \"r\", and with part 2 rebased against 3.4.1.rc4.\n\nI'll keep an eye out for it so you don't have to rebase yet again.",
    "created_at": "2009-04-21T04:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43722",
    "user": "https://github.com/rbeezer"
}
```

Replying to [comment:12 jhpalmieri]:
> The second patch also changes QQ, RR, and CC.  It leaves `\mathbb{P`} and `\mathbb{A`} unchanged.  (The first patch includes only the core of the customization code, and the relevant files happened not to use QQ, RR, or CC.)

OK, that explains the split.  ;-) 

> Does this affect end-users, or just developers?  I mean, does `latex(blah)` behave the same as it used to?  I hope so -- that was my intention.  

I didn't notice any change from a user's perspective.  And maybe it was just the change that threw me.  I saw `def latex()` going away and it took me a while to figure out how the functionality came back.  I just thought for others reading the code it might help to make the definition of the `latex` instance more prominient with some source code comments.  Right now, it just seems to be slipped in there, when it is fairly important since users will be accessing/changing its contents.  I did like the way you made the change while preserving `latex()`.


> I'll produce a new patch soon with the "r", and with part 2 rebased against 3.4.1.rc4.

I'll keep an eye out for it so you don't have to rebase yet again.



---

archive/issue_comments_043723.json:
```json
{
    "body": "Here's are two new patches, same subdivision as before, rebased against 3.4.1.rc4.  I also added a comment about `latex()`, as rbeezer suggested: this is in the first patch, right before the line \n\n```\nlatex = Latex()\n```\n\nin latex.py.",
    "created_at": "2009-04-21T05:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43723",
    "user": "https://github.com/jhpalmieri"
}
```

Here's are two new patches, same subdivision as before, rebased against 3.4.1.rc4.  I also added a comment about `latex()`, as rbeezer suggested: this is in the first patch, right before the line 

```
latex = Latex()
```

in latex.py.



---

archive/issue_comments_043724.json:
```json
{
    "body": "Attachment [latex-customization.patch](tarball://root/attachments/some-uuid/ticket5610/latex-customization.patch) by @jhpalmieri created at 2009-04-21 05:42:13\n\napply this one first",
    "created_at": "2009-04-21T05:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43724",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [latex-customization.patch](tarball://root/attachments/some-uuid/ticket5610/latex-customization.patch) by @jhpalmieri created at 2009-04-21 05:42:13

apply this one first



---

archive/issue_comments_043725.json:
```json
{
    "body": "Attachment [latex-customization-part2.patch](tarball://root/attachments/some-uuid/ticket5610/latex-customization-part2.patch) by @jhpalmieri created at 2009-04-21 05:43:06\n\napply this one second (this is the same as latex-customization-part2.2.patch)",
    "created_at": "2009-04-21T05:43:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43725",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [latex-customization-part2.patch](tarball://root/attachments/some-uuid/ticket5610/latex-customization-part2.patch) by @jhpalmieri created at 2009-04-21 05:43:06

apply this one second (this is the same as latex-customization-part2.2.patch)



---

archive/issue_comments_043726.json:
```json
{
    "body": "Latest patches work well:  apply cleanly, builds and tests fine, including documentation.  Looks ready to go.  Great addition to the LaTeX-Sage interaction.",
    "created_at": "2009-04-22T05:50:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43726",
    "user": "https://github.com/rbeezer"
}
```

Latest patches work well:  apply cleanly, builds and tests fine, including documentation.  Looks ready to go.  Great addition to the LaTeX-Sage interaction.



---

archive/issue_comments_043727.json:
```json
{
    "body": "Arrrg, the second patch has one reject in matrix1.pyx:\n\n```\npatching file sage/matrix/matrix1.pyx\nHunk #1 FAILED at 191.\n1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix1.pyx.rej\n```\n\nI will try to fix it. This patch will likely break some other patches, so I am considering applying the untabify patch, too (in case it applies).\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T08:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43727",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Arrrg, the second patch has one reject in matrix1.pyx:

```
patching file sage/matrix/matrix1.pyx
Hunk #1 FAILED at 191.
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix1.pyx.rej
```

I will try to fix it. This patch will likely break some other patches, so I am considering applying the untabify patch, too (in case it applies).

Cheers,

Michael



---

archive/issue_comments_043728.json:
```json
{
    "body": "Ok, I took out the failing hunk and merged it manually. Since this patch will potentially cause merge issues elsewhere I will push out 3.4.2.alpha0 in the morning after merging some spkg fixes.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T09:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43728",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Ok, I took out the failing hunk and merged it manually. Since this patch will potentially cause merge issues elsewhere I will push out 3.4.2.alpha0 in the morning after merging some spkg fixes.

Cheers,

Michael



---

archive/issue_comments_043729.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T09:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43729",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael



---

archive/issue_comments_043730.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T09:17:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5610#issuecomment-43730",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_005854.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2009-04-24T09:17:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5610",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5610#event-5854"
}
```
