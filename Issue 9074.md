# Issue 9074: Expand latex support for combinatorial graphs via tkz-graph

Issue created by migration from https://trac.sagemath.org/ticket/9074

Original creator: rbeezer

Original creation time: 2010-05-28 05:33:11

Assignee: jason, ncohen, rlm

CC:  nthiery jhpalmieri jason

Examples of recent progress at:

http://wiki.sagemath.org/daysff/tkz-graphs


---

Attachment

Working version, but needs doctest, some error trapping


---

Comment by rbeezer created at 2010-05-30 06:27:18

Functional, just needs doctests of final format


---

Attachment

Example graphic of a Cayley graph


---

Comment by rbeezer created at 2010-05-30 06:31:49

I've attached an image produced with this patch.  With the necessary files in place and added to the latex preamble, this labeled Cayley graph comes from the following code:


```
G=CyclicPermutationGroup(7)
C=G.cayley_graph(generators=[G((1,2,3,4,5,6,7)), G((1,4,7,3,6,2,5))])
C.set_pos(C.layout_circular())
C.set_latex_options(graphic_size=(12,12),vertex_shape="rectangle", edge_labels=True)
view(C)
```



---

Attachment

Image file needed for documentation


---

Attachment


---

Comment by rbeezer created at 2010-05-31 21:07:47

Alright, version 3 patch is ready for review.  You'll need all the bits of tex to test this out properly, see the documentation at the top of graph_latex.py for hints.  Notes:

(a) This depends on the (trivial) #9091, otherwise a doctest or two will fail.

(b) The attached file  heawood-graph-latex.png needs to be placed into `doc/en/reference/static` for the documentation to build properly. (Is this the right place?)

(c) There is more to do, but this is a big improvement, and ready to go out into the wild and be useful.  Another push could address the suggestions listed in the source.



---

Comment by rbeezer created at 2010-05-31 21:07:47

Changing status from new to needs_review.


---

Comment by rbeezer created at 2010-06-13 18:54:38

To test this patch properly may require several additional latex packages, which may need to be installed properly by hand.

At

http://altermundus.com/pages/download.html

find

tkz-graph.sty

tkz-arith.sty

tkz-berge.sty


and put these where tex can find them.  These depend on the tikz and pgf packages which you should be able to install more easily if you don't already have them.

(It is possible that one or both of the latter two are not required.)


---

Comment by jhpalmieri created at 2010-06-13 20:47:59

Hi Rob,

> The attached file heawood-graph-latex.png needs to be placed into doc/en/reference/static for the documentation to build properly. (Is this the right place?)

It should go in doc/en/reference/media.  You should also add it to the mercurial repository: it should just be part of the patch file.  (So do "hg add ..." (or `hg_sage.add(...)`) to add it, and then when you export the patch, use "hg export -g ..." (or `hg_sage.export(..., options='-g')`) so that the patch file deals with the binary file correctly.)


---

Comment by rbeezer created at 2010-06-13 21:18:18

Replying to [comment:4 jhpalmieri]:
> It should go in doc/en/reference/media.  You should also add it to the mercurial repository: it should just be part of the patch file.  (So do "hg add ..." (or `hg_sage.add(...)`) to add it, and then when you export the patch, use "hg export -g ..." (or `hg_sage.export(..., options='-g')`) so that the patch file deals with the binary file correctly.)

Thanks, John.  I'll get a revised patch up tonight (or sooner).


---

Comment by rbeezer created at 2010-06-14 05:04:51

Sel-contained, including Heawood graph as binary file


---

Attachment

New version 4 patch is almost identical to v3.

Heawood graph image file is now in the patch as a binary file, and will land in the media subdirectory, as suggested above.  The only other change is to have the link in the documentation point to the new home of the graphic file, and this has been tested through rebuilding the affected HTML documentation.

Thanks again for the help, John.

Rob


---

Comment by jhpalmieri created at 2010-06-22 22:22:13

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2010-06-22 22:22:13

I'm getting a doctest failure:

```
File "/Applications/sage/devel/sage/sage/graphs/graph_latex.py", line 271:
    sage: print latex(G)
Expected:
    \begin{tikzpicture}
    %
    \useasboundingbox (0,0) rectangle (4.0in,4.0in);
    %
    \definecolor{cv0}{rgb}{0.8,0.8,0.8}
    \definecolor{cfv0}{rgb}{0.0,0.0,1.0}
    \definecolor{clv0}{rgb}{0.0,0.5,0.0}
    \definecolor{cv1}{rgb}{0.8,0.8,0.8}
    \definecolor{cfv1}{rgb}{0.0,0.0,1.0}

[snip]

Got:
    \begin{tikzpicture}
    %
    \useasboundingbox (0,0) rectangle (4.0in,4.0in);
    %
    \definecolor{cv0}{rgb}{0.8,0.8,0.8}
    \definecolor{cfv0}{rgb}{0.0,0.0,1.0}
    \definecolor{clv0}{rgb}{0.0,0.5,0.0}
    \definecolor{cv1}{rgb}{0.0,0.0,1.0}
    \definecolor{cfv1}{rgb}{1.0,0.0,1.0}
```

cv1 and cfv1 are not correct.  I wonder if this is because the examples are not being run in order, and so some later example is changing some settings before this one gets run.

Also, as I noted on another ticket, jsMath doesn't know about the `\LaTeX` command, so the simplest solution is just to replace it with plain-text `LaTeX` everywhere.  Try typesetting the reference manual with "sage -docbuild reference html -j" to see the jsMath version.

In line 51 of graph_latex.py, the phrase `though at the command line the call to jsmath_avoid_list() is only needed in the notebook`: delete "at the command line".

Line 605-606:


```
- ``format`` -- default: 'tkz_graph' -- either 'dot2tex' 
   or 'tkz_graph'. 
```

The "or" on the second line doesn't line up with the ```` on the first line, so it doesn't get typeset right.

While you're fixing these issues, you might want to modify this code:

```
@cached_function
def setup_latex_preamble():
  ...
```

For reasons I don't understand, decorating a function with ``@`cached_function` prevents it from appearing in the reference manual, so instead you can change it to the following (note the trailing underscores, just used to create a new name similar to the original one):

```
def setup_latex_preamble_():
  ...

setup_latex_preamble = cached_function(setup_latex_preamble_)
```



---

Comment by rbeezer created at 2010-07-24 06:54:39

Apply on top of v4 patch


---

Attachment

Hi John,

Nice catch with the random order doctesting - see below.

(1) \LaTeX -> LaTeX and the two suggested edits have been made.

(2) Big doctest failed with a random order because I was
not using a sorted version of the vertex list, so a change has
been made to the code to always use a single sorted list.

Only the list really isn't sorted since graphs allow
nearly arbitrary objects to be vertices.  So I removed
the relabeling of vertex 1 as a symbolic expression.  I'll
pursue this on sage-devel.  Doctest should now work
consistently, even under random ordering.

(3)  Discovered a typo in the error checking for
"edge_label_placements" since a doctest was raising
an error (when it shouldn't have). That code has been fixed.

(4)  I made the suggested change with the cached function.
Then other doctests began to fail.  And that function
itself began to fail doctests with a random order, and
still does despite restoring the original state.  So
I'm afraid I don't get it on this one, and I'm not
the original author.  Can we move the two problems:
(a) not in the docs, and (b) failing random tests;
to another ticket (I'll do it)?

I've run tests in the graph directory, built html
and jsmath documentation.  I've attached a "v4-plus"
patch so you can see the changes, it needs to go on
top of the v4 patch.

Thanks for all your careful work on this!

Rob


---

Comment by rbeezer created at 2010-07-24 06:57:34

Changing status from needs_work to needs_review.


---

Comment by rbeezer created at 2010-07-26 18:30:53

I've put the preamble setup situation on a new ticket, #9605.


---

Comment by rbeezer created at 2010-07-27 18:30:16

Two doctest failures on a system without the necessary tkz-graph files installed.  Need to add some "random" comments, and some "check_tkz_graph" calls.  Likely worse for random-order testing.  Soon.


---

Comment by rbeezer created at 2010-07-27 18:30:16

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by rbeezer created at 2010-07-27 19:08:22

v4_missing  patch should solve failures with randomized order on systems missing tkz-graph style files - its been tested where one of the tkz-graph files has been renamed so as to go "missing."  About 15 runs in random order raise no errors (with #9607 applied first).

Basically, there needs to be a  check_tkz_graph()  call prior to every  latex(G)  to "clear out" the one-time warnings, since we can't predict the order of the tests.

You may see a very rare failure at line 435 (true/false) with random order testing - this is being addressed at #9605.

Apply v4, v4-plus, v4-missing.  I'll roll up a mega patch once this is done.


---

Comment by rbeezer created at 2010-07-27 19:08:22

Changing status from needs_work to needs_review.


---

Comment by jason created at 2010-10-12 02:31:45

jhpalmieri, are you interested in giving this a final review?


---

Comment by jhpalmieri created at 2010-10-12 20:09:23

I'm not an expert in the tkz stuff, but the code looks okay to me, it passes doctests, and the documentation looks very good: very good descriptions of how to do things.

A few small issues in the file graph-latex.py:

 - line 28: `the pre-builts styles`
 - line 584: `controlling the rendering a graph` -- missing "of"
 - line 609: `delegated to `dot2tex`` -- you should have double backquotes around "dot2tex"
 - line 716: ```vertex_label_color`` -- default: `black``  -- "black" should be in ordinary quotes, not backquotes
 - line 727: ```vertex_label_placement`` -- default: `center`` -- "center" should be in ordinary quotes, not backquotes
 - line 1179: `positive number between and a copmpass point` -- missing words after "between", and "compass" is misspelled

This passes all tests on a machine with the tkz files, on a machine with latex but without those files, and on a machine without latex.  I tried "sage -i graphviz", but the installation failed on my mac, so I couldn't test the dot2tex parts.

For some of the argument error-checking, it might be nice in the future to have some sort of conversion, so I could enter "E" or "e" instead of "EA" for a direction, for instance.  But that can go on another ticket.

Fix the typos, and it can have a positive review.


---

Comment by rbeezer created at 2010-10-14 05:53:22

Changing status from needs_review to needs_work.


---

Comment by rbeezer created at 2010-10-14 05:53:22

Hi John,

Thanks very much for giving this another look.  (And thanks, Jason, for your interest.)  I'm into an intense few weeks of *teaching* Sage, but will try and wrap this up ASAP.

Rob


---

Comment by rbeezer created at 2010-10-18 18:54:54

Standalone patch


---

Comment by rbeezer created at 2010-10-18 18:56:05

Changing status from needs_work to needs_review.


---

Attachment

OK, should be ready to go, all wrapped up in the v5 patch.  Figured the changes are so small that I would just consolidate the 3 patches into one, hope that's not a problem.  The mis-spelled `copmpass` was part of a doctest, and so I had to change the source as well.  Also found another default argument of `black` without quotes.  Otherwise all the changes are exactly as suggested.  Passes all tests in `sage/graphs`.

Thanks for the very careful review.

Rob


---

Comment by jhpalmieri created at 2010-11-02 19:18:02

Oops, the png file is missing from the v5 patch.  Otherwise, I think it's ready to go.


---

Comment by jhpalmieri created at 2010-12-04 19:21:25

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-12-04 19:21:25

I've added the png file to the new patch. 

Apply: trac_9074-tkz-graph-latex-v6.patch


---

Attachment

Standalone patch, apply only this one


---

Comment by rbeezer created at 2010-12-04 20:46:30

Hi John,

Thanks for doing this.  I was traveling a lot when this first came across (safari in Africa with family) and have been on a big push with some linear algebra stuff since I got home.

I hadn't forgotten, but obviously hadn't been very responsive.  THANKS for all your work keeping up with this one and my minor goof-ups along the way.  I'll see you at Bug Days I'm sure, if not sooner.

Rob


---

Comment by jdemeyer created at 2011-01-12 06:32:24

Resolution: fixed
