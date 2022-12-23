# Issue 5610: [with patch, not ready for review?] LaTeX customization

Issue created by migration from https://trac.sagemath.org/ticket/5610

Original creator: jhpalmieri

Original creation time: 2009-03-25 17:56:57

Assignee: jhpalmieri

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


---

Comment by robertwb created at 2009-03-25 18:59:12

I think it looks good, but why "latex_customize" rather than just attaching methods to "latex"?


---

Comment by jhpalmieri created at 2009-03-25 19:14:05

Replying to [comment:1 robertwb]:
> I think it looks good, but why "latex_customize" rather than just attaching methods to "latex"? 

Well, when I tried to attach some methods to Latex, I got all sorts of weird doctesting errors for latex.py (all of the output for latex_variable_name acted as if EMBEDDED_MODE were True, for example).  I have no idea why, but I fixed it by setting it up like this.


---

Comment by robertwb created at 2009-03-25 19:41:25

Strange.


---

Comment by jhpalmieri created at 2009-03-25 21:58:46

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

Comment by jhpalmieri created at 2009-03-31 22:16:34

[Here's a picture.](http://sage.math.washington.edu/home/palmieri/misc/bbold.png)  The last part -- the docstring -- relies on #5653.


---

Comment by jhpalmieri created at 2009-04-12 22:54:18

Replying to [comment:2 jhpalmieri]:
> Replying to [comment:1 robertwb]:
> > I think it looks good, but why "latex_customize" rather than just attaching methods to "latex"? 
> 
> Well, when I tried to attach some methods to Latex, I got all sorts of weird doctesting errors for latex.py (all of the output for latex_variable_name acted as if EMBEDDED_MODE were True, for example).  I have no idea why, but I fixed it by setting it up like this.

Just to follow up, I think this is the same issue as discussed [in this thread on sage-devel](http://groups.google.com/group/sage-devel/browse_frm/thread/320845a4c9b9c75f).  I would be happy to attach  methods to `latex` if we can get this straightened out.


---

Comment by jhpalmieri created at 2009-04-14 18:49:38

Here are new versions of the patches.  There are two changes: they are rebased against 3.4.1.rc2, and I managed to fix the weird problem with doctests in latex.  Therefore we now have commands like `latex.set_matrix_delimiters` instead of `latex_customize.set_matrix_delimiters`.


---

Comment by jhpalmieri created at 2009-04-14 20:17:25

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

Comment by robertwb created at 2009-04-15 23:14:18

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

Comment by jhpalmieri created at 2009-04-16 01:48:19

Replying to [comment:9 robertwb]:
> This is really cool. I might recommend making the names a bit shorter, e.g. 

That's a good idea.  Here's a new version of the patch doing that.


---

Comment by rbeezer created at 2009-04-20 03:37:04

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

Comment by rbeezer created at 2009-04-20 03:45:10

Screenshot of garbled list_function() documentation (yellow highlight on "indirect" is from my search function)


---

Attachment

Replying to [comment:11 rbeezer]:
>The new methods for setting matrix and vector delimiters are a very welcome addition, and the options for "bolding" rings provide a good example for future options like this. One should note that work still needs to be done to make this work for all rings, this patch appears to only demonstrate use for ZZ and GF (though I could have missed some). 

The second patch also changes QQ, RR, and CC.  It leaves `\mathbb{P`} and `\mathbb{A`} unchanged.  (The first patch includes only the core of the customization code, and the relevant files happened not to use QQ, RR, or CC.)

> The use of an instance of the Latex class, named "latex" had me confused for a while, since now `latex.__call__` replaces the functionality of the old `latex()`.  Some commentary highlighting the `latex` instance in the source (at some point - either now, or later) might save others the same confusion.

Does this affect end-users, or just developers?  I mean, does `latex(blah)` behave the same as it used to?  I hope so -- that was my intention.  You're right, though, that the syntax from the development end is different, but that seemed like the nicest way to do the customization: as methods (which could be tab-completed) attached to latex.  Do you have suggestions about what sorts of comments to add?

> `sage -docbuild pdf reference` seemed to choke on the doctest for the `list_function` method in `misc/latex.py`.  

I think this is easy to fix: put an "r" in front of the triple quotes at the beginning of the docstring.  It was there originally, and then I deleted it (I don't know why) in the new version.

I'll produce a new patch soon with the "r", and with part 2 rebased against 3.4.1.rc4.


---

Comment by rbeezer created at 2009-04-21 04:13:22

Replying to [comment:12 jhpalmieri]:
> The second patch also changes QQ, RR, and CC.  It leaves `\mathbb{P`} and `\mathbb{A`} unchanged.  (The first patch includes only the core of the customization code, and the relevant files happened not to use QQ, RR, or CC.)

OK, that explains the split.  ;-) 

> Does this affect end-users, or just developers?  I mean, does `latex(blah)` behave the same as it used to?  I hope so -- that was my intention.  

I didn't notice any change from a user's perspective.  And maybe it was just the change that threw me.  I saw `def latex()` going away and it took me a while to figure out how the functionality came back.  I just thought for others reading the code it might help to make the definition of the `latex` instance more prominient with some source code comments.  Right now, it just seems to be slipped in there, when it is fairly important since users will be accessing/changing its contents.  I did like the way you made the change while preserving `latex()`.


> I'll produce a new patch soon with the "r", and with part 2 rebased against 3.4.1.rc4.

I'll keep an eye out for it so you don't have to rebase yet again.


---

Comment by jhpalmieri created at 2009-04-21 05:41:39

Here's are two new patches, same subdivision as before, rebased against 3.4.1.rc4.  I also added a comment about `latex()`, as rbeezer suggested: this is in the first patch, right before the line 

```
latex = Latex()
```

in latex.py.


---

Attachment

apply this one first


---

Attachment

apply this one second (this is the same as latex-customization-part2.2.patch)


---

Comment by rbeezer created at 2009-04-22 05:50:44

Latest patches work well:  apply cleanly, builds and tests fine, including documentation.  Looks ready to go.  Great addition to the LaTeX-Sage interaction.


---

Comment by mabshoff created at 2009-04-24 08:53:59

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

Comment by mabshoff created at 2009-04-24 09:16:57

Ok, I took out the failing hunk and merged it manually. Since this patch will potentially cause merge issues elsewhere I will push out 3.4.2.alpha0 in the morning after merging some spkg fixes.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 09:17:18

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 09:17:18

Resolution: fixed
