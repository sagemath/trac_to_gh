# Issue 6089: [with patch, needs review] view command: don't always use jsMath

archive/issues_006089.json:
```json
{
    "body": "Assignee: @jhpalmieri\n\nCC:  @rbeezer fidelbarrera\n\nThe attached patch provides a way to not always use jsMath when rendering LaTeX for the 'view' command in the notebook.  It works by looking for certain strings in the latex code for the object, and if it finds them, it creates and displays a png file, bypassing jsMath altogether.  The \"certain strings\" are stored in a list which is initially empty, but can be populated by using\n\n```\nlatex.jsmath_avoid_list(...)\n```\n\nor\n\n```\nlatex.add_to_jsmath_avoid_list(...)\n```\n\nTo test it out, for example: in a notebook cell, try\n\n```\nclass bozo(SageObject):\n    def __init__(self):\n        pass\n    def _latex_(self):\n        return r\"\"\"\\begin{pspicture}(0,-4)(14,0)\n  \\psline{-}(0,0)(0,-4)\n  \\psline[linewidth=2pt]{-}(0,0)(1,-3)\n  \\qdisk(1,-3){3pt}\n  \\psarc{-}(0,0){0.6}{270}{292}\n  \\psline{->}(1,-3.3)(1,-4)\n  \\psline{->}(1.1,-2.7)(0.85,-1.95)\n  \\psline{-}(5,0)(5,-4)\n  \\psline[linewidth=2pt]{-}(5,0)(6,-3)\n  \\qdisk(6,-3){3pt}\n  \\psarc{-}(5,0){0.6}{270}{292}\n  \\psarc{-}(5,0){3.2}{270}{290}\n\\end{pspicture}\"\"\"\n```\n \nThen the latex string for instances of this class contains commands that jsMath can't handle, and indeed, `view(bozo())` ought to produce a typical jsMath error: a little box saying `Unknown environment \"pspicture\"`.  Then do\n\n```\nlatex.add_to_jsmath_avoid_list(\"pspicture\")\n```\n\nand try viewing again; it ought to pop up a pstricks picture.  It's a little slow, but I think we may have to live with that.\n\nTo the graph theorists: You ought to be able to do the same thing with graphs, as long as `'\\\\usepackage{tkz-graph}'` has been added to the latex preamble.  If you're doing that automatically, then you could also add an entry to `jsmath_avoid_list`...\n\nIssue created by migration from https://trac.sagemath.org/ticket/6089\n\n",
    "created_at": "2009-05-20T03:40:23Z",
    "labels": [
        "misc",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.2",
    "title": "[with patch, needs review] view command: don't always use jsMath",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6089",
    "user": "@jhpalmieri"
}
```
Assignee: @jhpalmieri

CC:  @rbeezer fidelbarrera

The attached patch provides a way to not always use jsMath when rendering LaTeX for the 'view' command in the notebook.  It works by looking for certain strings in the latex code for the object, and if it finds them, it creates and displays a png file, bypassing jsMath altogether.  The "certain strings" are stored in a list which is initially empty, but can be populated by using

```
latex.jsmath_avoid_list(...)
```

or

```
latex.add_to_jsmath_avoid_list(...)
```

To test it out, for example: in a notebook cell, try

```
class bozo(SageObject):
    def __init__(self):
        pass
    def _latex_(self):
        return r"""\begin{pspicture}(0,-4)(14,0)
  \psline{-}(0,0)(0,-4)
  \psline[linewidth=2pt]{-}(0,0)(1,-3)
  \qdisk(1,-3){3pt}
  \psarc{-}(0,0){0.6}{270}{292}
  \psline{->}(1,-3.3)(1,-4)
  \psline{->}(1.1,-2.7)(0.85,-1.95)
  \psline{-}(5,0)(5,-4)
  \psline[linewidth=2pt]{-}(5,0)(6,-3)
  \qdisk(6,-3){3pt}
  \psarc{-}(5,0){0.6}{270}{292}
  \psarc{-}(5,0){3.2}{270}{290}
\end{pspicture}"""
```
 
Then the latex string for instances of this class contains commands that jsMath can't handle, and indeed, `view(bozo())` ought to produce a typical jsMath error: a little box saying `Unknown environment "pspicture"`.  Then do

```
latex.add_to_jsmath_avoid_list("pspicture")
```

and try viewing again; it ought to pop up a pstricks picture.  It's a little slow, but I think we may have to live with that.

To the graph theorists: You ought to be able to do the same thing with graphs, as long as `'\\usepackage{tkz-graph}'` has been added to the latex preamble.  If you're doing that automatically, then you could also add an entry to `jsmath_avoid_list`...

Issue created by migration from https://trac.sagemath.org/ticket/6089





---

archive/issue_comments_048506.json:
```json
{
    "body": "I've just posted a new version of the patch.  The only difference (aside from fixing a few typos) is the addition of a 'latex_examples' class at the bottom of the file.  This provides people (like me) with a handful of  ready-made examples of objects with interesting `_latex_` methods, for testing with 'view', the typeset button, etc.  This class is not imported into the global name space, so you need to access it with\n\n```\nsage: from sage.misc.latex import latex_examples\nsage: G = latex_examples.graph()\nsage: view(G)\n```\n\netc.\n\nOf course, the typeset button won't handle any of these yet, but I have hope that there may be a solution some day...",
    "created_at": "2009-05-21T05:20:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48506",
    "user": "@jhpalmieri"
}
```

I've just posted a new version of the patch.  The only difference (aside from fixing a few typos) is the addition of a 'latex_examples' class at the bottom of the file.  This provides people (like me) with a handful of  ready-made examples of objects with interesting `_latex_` methods, for testing with 'view', the typeset button, etc.  This class is not imported into the global name space, so you need to access it with

```
sage: from sage.misc.latex import latex_examples
sage: G = latex_examples.graph()
sage: view(G)
```

etc.

Of course, the typeset button won't handle any of these yet, but I have hope that there may be a solution some day...



---

archive/issue_comments_048507.json:
```json
{
    "body": "Attachment [avoid-jsmath.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath.patch) by @jhpalmieri created at 2009-05-21 05:31:26",
    "created_at": "2009-05-21T05:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48507",
    "user": "@jhpalmieri"
}
```

Attachment [avoid-jsmath.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath.patch) by @jhpalmieri created at 2009-05-21 05:31:26



---

archive/issue_comments_048508.json:
```json
{
    "body": "Works very well, and the examples class will be very useful.\n\nPasses   sage -t devel/sage-avoid-jsmath/sage/misc/latex.py and additions have doctests.\n\nComments:\n\n1.  For `g = latex_examples.graph()` at the sage command-line `view(g)` creates a DVI file which doesn't render properly in xdvi or evince.  However, `view(g pdflatex=True)` produces a PDF that is fine.  DVI behavior was variable depending on the two viewers, so maybe it was my setup.  If some DVI's really are problematic, could `dvipng --picky` be used to test for complicated DVI's, and then pdflatex/convert could be called as a fallback?\n\n2.  Passing a list of objects to `view()` at the command line creates a list of the objects properly rendered, line-by-line, in a DVI.  The same command from the notebook, goes into jsmath-avoidance mode if just one object is problematic, and makes one giant image of everything in the list, including the [].  Is it possible to examine each object in the list for jsmath-avoidance, handle those individually and return as PNG's wrapped in html <img> tags?  This way, a user in the notebook could right-click on pieces of the list to get individual images of individual objects.  \n\n3.  The `add_to_jsmath_avoid_list()` adds strings without checking to see if they are present already.  I could see a user repeatedly adding a string inside of a loop, without perhaps realizing it got repeated over and over.  Seems it would be easy enough to test for presence before adding.  `add_to_preamble()` behaves similarly.\n\nI think (3) is easy and should probably be adjusted, (1) feels a bit like an error if we want every combination to \"just work\" while (2) is more wishlist/suggestion.  This will be another good piece of the puzzle, and it will be very good to have the canonical examples always available for testing and demos.",
    "created_at": "2009-05-22T04:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48508",
    "user": "@rbeezer"
}
```

Works very well, and the examples class will be very useful.

Passes   sage -t devel/sage-avoid-jsmath/sage/misc/latex.py and additions have doctests.

Comments:

1.  For `g = latex_examples.graph()` at the sage command-line `view(g)` creates a DVI file which doesn't render properly in xdvi or evince.  However, `view(g pdflatex=True)` produces a PDF that is fine.  DVI behavior was variable depending on the two viewers, so maybe it was my setup.  If some DVI's really are problematic, could `dvipng --picky` be used to test for complicated DVI's, and then pdflatex/convert could be called as a fallback?

2.  Passing a list of objects to `view()` at the command line creates a list of the objects properly rendered, line-by-line, in a DVI.  The same command from the notebook, goes into jsmath-avoidance mode if just one object is problematic, and makes one giant image of everything in the list, including the [].  Is it possible to examine each object in the list for jsmath-avoidance, handle those individually and return as PNG's wrapped in html <img> tags?  This way, a user in the notebook could right-click on pieces of the list to get individual images of individual objects.  

3.  The `add_to_jsmath_avoid_list()` adds strings without checking to see if they are present already.  I could see a user repeatedly adding a string inside of a loop, without perhaps realizing it got repeated over and over.  Seems it would be easy enough to test for presence before adding.  `add_to_preamble()` behaves similarly.

I think (3) is easy and should probably be adjusted, (1) feels a bit like an error if we want every combination to "just work" while (2) is more wishlist/suggestion.  This will be another good piece of the puzzle, and it will be very good to have the canonical examples always available for testing and demos.



---

archive/issue_comments_048509.json:
```json
{
    "body": "I'm not sure I agree with point 1, because I think it's asking Sage to be smarter than LaTeX about processing LaTeX.  If you can't use xdvi or evince to view a file outside of Sage, why should you expect Sage to do a better job?  We can certainly rewrite the descriptions of the latex_examples saying that there might be rendering problems depending on how the system is set up, and perhaps setting pdflatex=True would do a better job.  Would that be good enough?\n\nFor point 2, I'm not sure what do to.  First, it seems that in the notebook, view is rather broken: running\n\n```\nview([ZZ[x], RR, CC])\n```\n\nproduces\n\n```\n[Univariate Polynomial Ring in x over Integer Ring, Real Field with 53 bits of precision, Complex Field with 53 bits of precision]\n```\n\ntypeset by jsMath as if in math mode, so there are no spaces between words.  It's terrible.  Since view works fine on single objects, I can put in a small change which fixes this and would change the output to \n\n```\nZ[x]\nR\nC\n```\n\n(with the appropriate letters in bold face).  Notice: no brackets any more, and this is consistent with how it works in the command line. This will also work, sort of, with jsmath-avoidance: each object in a list will be typeset separately, so you only get pictures when you need them.  However, the pictures always appear at the end, and this might just be how the notebook displays things: text first followed by pictures.  Therefore\n\n```\nview([ZZ[x], latex_examples.knot(), RR, CC])\n```\n\nwill produce\n\n```\nZ[x]\nR\nC\n```\n\nand then a picture of the knot.  Is this good enough?  Maybe we can add a place-holder \"picture below\", or something like that.  I'll keep investigating, but we may not have a good solution here.\n\nI completely agree about point 3.  This is actually innocuous with jsmath_avoid (except for speed issues, I guess), but could lead to errors with the preamble or macros: if you repeat the same newcommand, it produces a latex error, which would probably make the typesetting fail.",
    "created_at": "2009-05-22T19:08:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48509",
    "user": "@jhpalmieri"
}
```

I'm not sure I agree with point 1, because I think it's asking Sage to be smarter than LaTeX about processing LaTeX.  If you can't use xdvi or evince to view a file outside of Sage, why should you expect Sage to do a better job?  We can certainly rewrite the descriptions of the latex_examples saying that there might be rendering problems depending on how the system is set up, and perhaps setting pdflatex=True would do a better job.  Would that be good enough?

For point 2, I'm not sure what do to.  First, it seems that in the notebook, view is rather broken: running

```
view([ZZ[x], RR, CC])
```

produces

```
[Univariate Polynomial Ring in x over Integer Ring, Real Field with 53 bits of precision, Complex Field with 53 bits of precision]
```

typeset by jsMath as if in math mode, so there are no spaces between words.  It's terrible.  Since view works fine on single objects, I can put in a small change which fixes this and would change the output to 

```
Z[x]
R
C
```

(with the appropriate letters in bold face).  Notice: no brackets any more, and this is consistent with how it works in the command line. This will also work, sort of, with jsmath-avoidance: each object in a list will be typeset separately, so you only get pictures when you need them.  However, the pictures always appear at the end, and this might just be how the notebook displays things: text first followed by pictures.  Therefore

```
view([ZZ[x], latex_examples.knot(), RR, CC])
```

will produce

```
Z[x]
R
C
```

and then a picture of the knot.  Is this good enough?  Maybe we can add a place-holder "picture below", or something like that.  I'll keep investigating, but we may not have a good solution here.

I completely agree about point 3.  This is actually innocuous with jsmath_avoid (except for speed issues, I guess), but could lead to errors with the preamble or macros: if you repeat the same newcommand, it produces a latex error, which would probably make the typesetting fail.



---

archive/issue_comments_048510.json:
```json
{
    "body": "Hi John,\n\n(3) Hadn't thought about repeated `\\newcommand`'s.  That would indeed cause problems.\n\n(2) It's odd the items come out in a different order.  But maybe this would shakeout in the notebook overhaul that is coming up?  I think even with the pictures at the end, the suggested changes would be an improvement.\n\n(1) So it seems that some of these latex packages inject `\\special`'s into DVI's and in the past you would have to run dvips to get out something usable.  Anymore, my habit is to avoid DVI altogether and strictly run pdflatex with PDF's as output.  So my suggestion was to look at DVI's by running `dvipng --picky` to see how \"complicated\" a DVI might be.  If `dvipng --picky` failed, then take another approach: run pdflatex and then use convert to make a PNG for the notebook.  So the \"smarts\" would be in `--picky`, as I think was done elsewhere.\n\nCan you make a DVI of the graph example in latex_examples and render it properly in a DVI viewer?  Is it just me?\n\nMore generally, I've been thinking that the latex->DVI->PNG conversion process could perhaps just be replaced by pdflatex->PDF->PNG.  Mostly because it seems to me like the capabilities added into TeX for graphics (like we've been adding) have outgrown the DVI format.\n\nThe cons would be that a PDF viewer would have to be installed on a system, as opposed to xdvi (or similar), and the imagemagick suite (for convert) rather than dvipng.\n\nThe pros would be that view() could just call the PDF viewer every time from both the command line and the notebook, without using the `pdflatex=True` option, and without a second conversion step.  And %latex and %pdflatex could be consolidated into just the latter command.  Thoughts?\n\nRob",
    "created_at": "2009-05-22T21:26:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48510",
    "user": "@rbeezer"
}
```

Hi John,

(3) Hadn't thought about repeated `\newcommand`'s.  That would indeed cause problems.

(2) It's odd the items come out in a different order.  But maybe this would shakeout in the notebook overhaul that is coming up?  I think even with the pictures at the end, the suggested changes would be an improvement.

(1) So it seems that some of these latex packages inject `\special`'s into DVI's and in the past you would have to run dvips to get out something usable.  Anymore, my habit is to avoid DVI altogether and strictly run pdflatex with PDF's as output.  So my suggestion was to look at DVI's by running `dvipng --picky` to see how "complicated" a DVI might be.  If `dvipng --picky` failed, then take another approach: run pdflatex and then use convert to make a PNG for the notebook.  So the "smarts" would be in `--picky`, as I think was done elsewhere.

Can you make a DVI of the graph example in latex_examples and render it properly in a DVI viewer?  Is it just me?

More generally, I've been thinking that the latex->DVI->PNG conversion process could perhaps just be replaced by pdflatex->PDF->PNG.  Mostly because it seems to me like the capabilities added into TeX for graphics (like we've been adding) have outgrown the DVI format.

The cons would be that a PDF viewer would have to be installed on a system, as opposed to xdvi (or similar), and the imagemagick suite (for convert) rather than dvipng.

The pros would be that view() could just call the PDF viewer every time from both the command line and the notebook, without using the `pdflatex=True` option, and without a second conversion step.  And %latex and %pdflatex could be consolidated into just the latter command.  Thoughts?

Rob



---

archive/issue_comments_048511.json:
```json
{
    "body": "Try the \"version 2\" patch.  This one:\n\n1. removes the 'typeset' command (as discussed on sage-devel recently)\n2. adds a new command `_run_latex_on_file` -- instead of having several different calls to latex, each slightly different, scattered throughout the file, this provides a single consistent way to do it, and it runs dvipng with the picky option, so catches problematic latex.\n3. tidies up some docstrings\n4. fixes item (3) about repeated entries in latex.extra_preamble(), etc.\n5. adds jsmath_avoid_list, etc.\n6. deals with item (2) above, and things seem to appear in order, at least on my Mac.\n7. adds the latex examples class\n\nBy the way, re running pdflatex instead of latex: note that some packages like pstricks don't actually work with pdflatex.  Running latex, then dvips, then converting to png, might be the most robust method.",
    "created_at": "2009-05-23T15:01:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48511",
    "user": "@jhpalmieri"
}
```

Try the "version 2" patch.  This one:

1. removes the 'typeset' command (as discussed on sage-devel recently)
2. adds a new command `_run_latex_on_file` -- instead of having several different calls to latex, each slightly different, scattered throughout the file, this provides a single consistent way to do it, and it runs dvipng with the picky option, so catches problematic latex.
3. tidies up some docstrings
4. fixes item (3) about repeated entries in latex.extra_preamble(), etc.
5. adds jsmath_avoid_list, etc.
6. deals with item (2) above, and things seem to appear in order, at least on my Mac.
7. adds the latex examples class

By the way, re running pdflatex instead of latex: note that some packages like pstricks don't actually work with pdflatex.  Running latex, then dvips, then converting to png, might be the most robust method.



---

archive/issue_comments_048512.json:
```json
{
    "body": "This should also work with the \"Typeset\" box checked: if you do \n\n```\nG = latex_examples.graph()\n```\n\nand add the appropriate strings to the preamble and the jsmath_avoid_list, then clicking the Typeset box and evaluating G should produce a pretty picture.",
    "created_at": "2009-05-23T20:18:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48512",
    "user": "@jhpalmieri"
}
```

This should also work with the "Typeset" box checked: if you do 

```
G = latex_examples.graph()
```

and add the appropriate strings to the preamble and the jsmath_avoid_list, then clicking the Typeset box and evaluating G should produce a pretty picture.



---

archive/issue_comments_048513.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-05-23T20:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48513",
    "user": "@jhpalmieri"
}
```

apply only this patch



---

archive/issue_comments_048514.json:
```json
{
    "body": "Attachment [avoid-jsmath-version2.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath-version2.patch) by @rbeezer created at 2009-05-24 00:21:57\n\nHi John,\n\nI've been putting this all through the paces, though I'm not sure I've covered every possible scenario.  ;-) Just one hitch that I have found.\n\n(a) Open a new worksheet, tick the typeset button, type `x<sup>2+y</sup>2` in a cell, and output is the appropriate jsMath rendering.\n\n(b) Mess around with some of the `latex_examples` - add preamble information, and add a string to the jsmath-avoid-list, and `view()` or evaluate with typeset ticked.\n\n(c) Now repeat part (a).  I get a graphic out (not jsMath) and the x is missing (but the exponent of 2 on x is there and in the right place).\n\nIts like the `jsMathOkay` boolean is still set to `False`, but I couldn't track down where in the code there might be a problem.  Certainly it shouldn't be a graphic, but I'm also getting the missing character problem when I try to view lists of objects.  For example, suppose `var('x y z')` and `k` and `g` are variables and the knot and graph examples and all the preamble/avoid setup is in place, then in the notebook\n\n`view([k, z<sup>2+x</sup>2+y^2, gr])`\n\nis a nice run of three graphics, but the x is missing from the expression, so this is after Sage has reordered the terms of the expression.\n\nA couple minor comments.\n\n1.  In latex _examples, the docstring might benefit from including \"\\\\usepackage{tkz-berge}\" in the preamble addition suggestion.  This package is not needed for the example, but will be needed for the more general latex code for graphs being built.  If somebody goes to get the one package, they might as well get the other one while they are at it.  Can you tell I made two trips to get the packages a while ago after being very confused for the need for the second one?  ;-)\n\n2.  I ran `_run_latex_on_file()` on a six-page test file I've been using for debugging lots of this.  It creates several PNG's (numbered) if you run it this way.  Maybe that can go in the doc_string.  Each page of my test file has one image that gets created by the PGF/tikz/tkz-graph stuff, and the pages seem to get clipped on the left/right sides appropriately, but are all 1293 pixels tall.  Not a big deal, but maybe a switch would control this better?  My test file is at http://sage.pastebin.com/m540bee4f\n\nGreat stuff - I'll keep looking at this and we can get it reviewed soon.\n\nRob",
    "created_at": "2009-05-24T00:21:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48514",
    "user": "@rbeezer"
}
```

Attachment [avoid-jsmath-version2.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath-version2.patch) by @rbeezer created at 2009-05-24 00:21:57

Hi John,

I've been putting this all through the paces, though I'm not sure I've covered every possible scenario.  ;-) Just one hitch that I have found.

(a) Open a new worksheet, tick the typeset button, type `x<sup>2+y</sup>2` in a cell, and output is the appropriate jsMath rendering.

(b) Mess around with some of the `latex_examples` - add preamble information, and add a string to the jsmath-avoid-list, and `view()` or evaluate with typeset ticked.

(c) Now repeat part (a).  I get a graphic out (not jsMath) and the x is missing (but the exponent of 2 on x is there and in the right place).

Its like the `jsMathOkay` boolean is still set to `False`, but I couldn't track down where in the code there might be a problem.  Certainly it shouldn't be a graphic, but I'm also getting the missing character problem when I try to view lists of objects.  For example, suppose `var('x y z')` and `k` and `g` are variables and the knot and graph examples and all the preamble/avoid setup is in place, then in the notebook

`view([k, z<sup>2+x</sup>2+y^2, gr])`

is a nice run of three graphics, but the x is missing from the expression, so this is after Sage has reordered the terms of the expression.

A couple minor comments.

1.  In latex _examples, the docstring might benefit from including "\\usepackage{tkz-berge}" in the preamble addition suggestion.  This package is not needed for the example, but will be needed for the more general latex code for graphs being built.  If somebody goes to get the one package, they might as well get the other one while they are at it.  Can you tell I made two trips to get the packages a while ago after being very confused for the need for the second one?  ;-)

2.  I ran `_run_latex_on_file()` on a six-page test file I've been using for debugging lots of this.  It creates several PNG's (numbered) if you run it this way.  Maybe that can go in the doc_string.  Each page of my test file has one image that gets created by the PGF/tikz/tkz-graph stuff, and the pages seem to get clipped on the left/right sides appropriately, but are all 1293 pixels tall.  Not a big deal, but maybe a switch would control this better?  My test file is at http://sage.pastebin.com/m540bee4f

Great stuff - I'll keep looking at this and we can get it reviewed soon.

Rob



---

archive/issue_comments_048515.json:
```json
{
    "body": "I've tried, and I can't repeat the `x<sup>2+y</sup>2` problem, either on a Mac (Safari, Firefox) or linux (Firefox).\n\nI'll look at the dvipng switches (or maybe they're \"convert\" switches in this case) for your second comment.",
    "created_at": "2009-05-24T01:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48515",
    "user": "@jhpalmieri"
}
```

I've tried, and I can't repeat the `x<sup>2+y</sup>2` problem, either on a Mac (Safari, Firefox) or linux (Firefox).

I'll look at the dvipng switches (or maybe they're "convert" switches in this case) for your second comment.



---

archive/issue_comments_048516.json:
```json
{
    "body": "Never mind about switches: the images are big because they include the page numbers.  Use \\pagestyle{empty} at the beginning of the document.",
    "created_at": "2009-05-24T01:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48516",
    "user": "@jhpalmieri"
}
```

Never mind about switches: the images are big because they include the page numbers.  Use \pagestyle{empty} at the beginning of the document.



---

archive/issue_comments_048517.json:
```json
{
    "body": "Replying to [comment:9 jhpalmieri]:\n> Never mind about switches: the images are big because they include the page numbers.  Use \\pagestyle{empty} at the beginning of the document.\n\nOK, that makes sense.  Sorry about that one.\n\nI'll experiment some more with the `x^2` problem and see if I can isolate it better (or make it go away).",
    "created_at": "2009-05-24T03:01:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48517",
    "user": "@rbeezer"
}
```

Replying to [comment:9 jhpalmieri]:
> Never mind about switches: the images are big because they include the page numbers.  Use \pagestyle{empty} at the beginning of the document.

OK, that makes sense.  Sorry about that one.

I'll experiment some more with the `x^2` problem and see if I can isolate it better (or make it go away).



---

archive/issue_comments_048518.json:
```json
{
    "body": "OK, now I can't reproduce the missing x either, so who knows what that is about.  I'm afraid I've cried \"wolf\" too many times now.\n\nPasses: sage -t devel/sage/sage/graphs/\n\nAnother big step forward - positive review.",
    "created_at": "2009-05-24T05:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48518",
    "user": "@rbeezer"
}
```

OK, now I can't reproduce the missing x either, so who knows what that is about.  I'm afraid I've cried "wolf" too many times now.

Passes: sage -t devel/sage/sage/graphs/

Another big step forward - positive review.



---

archive/issue_comments_048519.json:
```json
{
    "body": "Does this work for you from the command line with the graph example?  I think it still needs some tinkering there.  For one thing, the 'view' command should not bomb if the user doesn't have dvipng or convert -- it should try to work just with latex or pdflatex.  I'll post a new patch soon.",
    "created_at": "2009-05-24T16:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48519",
    "user": "@jhpalmieri"
}
```

Does this work for you from the command line with the graph example?  I think it still needs some tinkering there.  For one thing, the 'view' command should not bomb if the user doesn't have dvipng or convert -- it should try to work just with latex or pdflatex.  I'll post a new patch soon.



---

archive/issue_comments_048520.json:
```json
{
    "body": "Replying to [comment:12 jhpalmieri]:\n> Does this work for you from the command line with the graph example?  I think it still needs some tinkering there.  For one thing, the 'view' command should not bomb if the user doesn't have dvipng or convert -- it should try to work just with latex or pdflatex.  I'll post a new patch soon.\n\nAt the command line, where `g` is the graph example, `view(g)` produces a DVI, which xdvi can only partially display - the curved edges are missing for starters.  `view(g, pdflatex=True)` builds a PDF which is fine.\n\nI have not experimented with the scenarios where some of the tools (like convert) are missing, but can try those cases against the next patch.",
    "created_at": "2009-05-24T17:21:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48520",
    "user": "@rbeezer"
}
```

Replying to [comment:12 jhpalmieri]:
> Does this work for you from the command line with the graph example?  I think it still needs some tinkering there.  For one thing, the 'view' command should not bomb if the user doesn't have dvipng or convert -- it should try to work just with latex or pdflatex.  I'll post a new patch soon.

At the command line, where `g` is the graph example, `view(g)` produces a DVI, which xdvi can only partially display - the curved edges are missing for starters.  `view(g, pdflatex=True)` builds a PDF which is fine.

I have not experimented with the scenarios where some of the tools (like convert) are missing, but can try those cases against the next patch.



---

archive/issue_comments_048521.json:
```json
{
    "body": "Attachment [avoid-jsmath-version3.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath-version3.patch) by @jhpalmieri created at 2009-05-30 15:35:46\n\napply only this patch",
    "created_at": "2009-05-30T15:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48521",
    "user": "@jhpalmieri"
}
```

Attachment [avoid-jsmath-version3.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath-version3.patch) by @jhpalmieri created at 2009-05-30 15:35:46

apply only this patch



---

archive/issue_comments_048522.json:
```json
{
    "body": "Here's a new patch.  In addition to the changes listed earlier, this:\n\n1. rewrites `list_function` etc.  These were a little broken before (e.g., putting `\\sage{range(10)`} in a %latex cell should have produced a list with each number on a different line, but it didn't; putting `\\sage{range(100)`} did put each number on a different line, which looks horrible).  Now lists and tuples are typeset with all of their entries on a single line.  This is I think what you would expect: if you ask to typeset `[2,3,5,7]`, then you expect the list to be typeset in the obvious way.   (This is only in the notebook; the command-line behavior is unchanged.)\n\n2. it slightly changes `bool_function` -- changes `\\rm blah` to `\\mathrm{blah`}\n\n3. the command `_run_latex_on_file` now takes arguments \"png\" (whether to produce a png file) and \"do_in_background\".  It tries to check whether a dvi file was created correctly by processing it with dvipng (if dvipng is present).  If something goes wrong, it calls dvips and ps2pdf.  (It doesn't just call pdflatex, because some packages, like pstricks, don't work with pdflatex.)\n\n4. Unfortunately, lists are now typeset all-in-one: if any part of the list contains jsmath avoidance text, then the whole thing turns into a png file.  This is partly because I couldn't write the code cleanly to deal with all of the cases (lists, tuples, nesting, etc.), and partly for speed issues: if A and B each require jsmath avoidance, for example, then `view([A, ZZ, B])` would run two separate latex processes, and this seemed slow on the machines I was using.",
    "created_at": "2009-05-30T16:10:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48522",
    "user": "@jhpalmieri"
}
```

Here's a new patch.  In addition to the changes listed earlier, this:

1. rewrites `list_function` etc.  These were a little broken before (e.g., putting `\sage{range(10)`} in a %latex cell should have produced a list with each number on a different line, but it didn't; putting `\sage{range(100)`} did put each number on a different line, which looks horrible).  Now lists and tuples are typeset with all of their entries on a single line.  This is I think what you would expect: if you ask to typeset `[2,3,5,7]`, then you expect the list to be typeset in the obvious way.   (This is only in the notebook; the command-line behavior is unchanged.)

2. it slightly changes `bool_function` -- changes `\rm blah` to `\mathrm{blah`}

3. the command `_run_latex_on_file` now takes arguments "png" (whether to produce a png file) and "do_in_background".  It tries to check whether a dvi file was created correctly by processing it with dvipng (if dvipng is present).  If something goes wrong, it calls dvips and ps2pdf.  (It doesn't just call pdflatex, because some packages, like pstricks, don't work with pdflatex.)

4. Unfortunately, lists are now typeset all-in-one: if any part of the list contains jsmath avoidance text, then the whole thing turns into a png file.  This is partly because I couldn't write the code cleanly to deal with all of the cases (lists, tuples, nesting, etc.), and partly for speed issues: if A and B each require jsmath avoidance, for example, then `view([A, ZZ, B])` would run two separate latex processes, and this seemed slow on the machines I was using.



---

archive/issue_comments_048523.json:
```json
{
    "body": "I installed the latest patch on top of my own work on #5975, just to have a few more examples to practice with.\n\nWith all the right programs installed (dvipng, convert, dvips, etc.) this seems to work as advertised both at the command line and in the notebook.  The only oddity I noticed is the following:  Let  g  and  k  be the graph and knot examples, respectively, from the `latex_examples` class.  Then in the notebook execute `view([k,g])`.  The graphic for the knot is centered vertically relative to the comma, but the graphic for the graph has its bottom edge aligned with the commas.  More experimentation with other objects, including other graphs, would indicate that it is the graphs that are behaving differently, but perhaps it is just the graphics format used, or converter applied?  Since the graph example is big, the left/right brackets are much longer than needed below the midline.\n\nWhen moving dvipng and convert out of the way, I ran into more serious problems.\n\nRemove just dvipng, then in notebook run `view(k)`  (with correct preamble, jsmath-avoid, etc).\n\nI get a \"local unbound variable\"  e  in line 401  of `_run_latex_on_file`.\n\nChasing through the code by hand it seems that  e  never gets set when `pdflatex` is not True and dvipng is missing.\n\nThis seems to happen on any of the examples.\n\nRemove just convert, then run  `view(g)`   (with correct preamble, jsmath-avoid, etc).\n\nI get \"An error occured\", a latex log file, and \"Latex error\"\n\nTo my eye the latex log doesn't seem to present any errors.\n\nI'm less certain just what is happening here.\n\nI found `_run_latex_on_file()` and `png()` a bit hard to follow.  I know you've done a lot of rearrangement to accomodate all the cases and scenarios, but maybe there is more that can be done?  Maybe more along the lines of the return \"code\" from `_run_latex_on_file()`, but related to inputs, targets, processing of tex, etc.  I'm still a bit uncomfortable with all the possibilities, so I don't really have any well-formed ideas at the moment.",
    "created_at": "2009-06-04T04:07:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48523",
    "user": "@rbeezer"
}
```

I installed the latest patch on top of my own work on #5975, just to have a few more examples to practice with.

With all the right programs installed (dvipng, convert, dvips, etc.) this seems to work as advertised both at the command line and in the notebook.  The only oddity I noticed is the following:  Let  g  and  k  be the graph and knot examples, respectively, from the `latex_examples` class.  Then in the notebook execute `view([k,g])`.  The graphic for the knot is centered vertically relative to the comma, but the graphic for the graph has its bottom edge aligned with the commas.  More experimentation with other objects, including other graphs, would indicate that it is the graphs that are behaving differently, but perhaps it is just the graphics format used, or converter applied?  Since the graph example is big, the left/right brackets are much longer than needed below the midline.

When moving dvipng and convert out of the way, I ran into more serious problems.

Remove just dvipng, then in notebook run `view(k)`  (with correct preamble, jsmath-avoid, etc).

I get a "local unbound variable"  e  in line 401  of `_run_latex_on_file`.

Chasing through the code by hand it seems that  e  never gets set when `pdflatex` is not True and dvipng is missing.

This seems to happen on any of the examples.

Remove just convert, then run  `view(g)`   (with correct preamble, jsmath-avoid, etc).

I get "An error occured", a latex log file, and "Latex error"

To my eye the latex log doesn't seem to present any errors.

I'm less certain just what is happening here.

I found `_run_latex_on_file()` and `png()` a bit hard to follow.  I know you've done a lot of rearrangement to accomodate all the cases and scenarios, but maybe there is more that can be done?  Maybe more along the lines of the return "code" from `_run_latex_on_file()`, but related to inputs, targets, processing of tex, etc.  I'm still a bit uncomfortable with all the possibilities, so I don't really have any well-formed ideas at the moment.



---

archive/issue_comments_048524.json:
```json
{
    "body": "Here's a new patch: avoid-jsmath-version4.patch.  I've also attached avoid-delta34.patch, which is the difference between version3 and version4, in case that makes refereeing any easier.  \n\nA summary of the changes: \n\n- I've added doctests to many of the functions in latex.py, so we're over 90% coverage now.  (For some reason, `sage -coverage` wasn't seeing the doctest for `pretty_print`, which is why I added \"# indirect doctest\" there.)\n\n- I made some of the reST cleaner and fancier (with cross-references, as described in #6226).\n\n- I reworked `_run_latex_` (which used to be called `_run_latex_on_file_`, which I decided was sort of redundant).  For me at least, this seems to behave right with the various combinations of the presence/absence of dvipng and convert.  I also added some comments so that the structure would be clearer. (I'm not sure what else you mean about it being hard to follow.) I think that running in the background might be problematic, but this is off by default anyway.\n\nAs far as the `view([k,g])` issue, that's purely a LaTeX thing: the code\n\n```\n\\[  <code for k>, <code for g> \\]\n```\n\ngets passed directly to LaTeX, and that's why the vertical spacing and the size of the brackets is the way it is.  Maybe we could modify the LaTeX code for either k or g to fix this, but since these are toy examples anyway, I don't think it's worth fixing.  My suggestion would instead be to either not view graphs or knots as members of lists, or write the `_latex_` methods for the real Sage objects so that they work well in this context.",
    "created_at": "2009-06-08T04:00:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48524",
    "user": "@jhpalmieri"
}
```

Here's a new patch: avoid-jsmath-version4.patch.  I've also attached avoid-delta34.patch, which is the difference between version3 and version4, in case that makes refereeing any easier.  

A summary of the changes: 

- I've added doctests to many of the functions in latex.py, so we're over 90% coverage now.  (For some reason, `sage -coverage` wasn't seeing the doctest for `pretty_print`, which is why I added "# indirect doctest" there.)

- I made some of the reST cleaner and fancier (with cross-references, as described in #6226).

- I reworked `_run_latex_` (which used to be called `_run_latex_on_file_`, which I decided was sort of redundant).  For me at least, this seems to behave right with the various combinations of the presence/absence of dvipng and convert.  I also added some comments so that the structure would be clearer. (I'm not sure what else you mean about it being hard to follow.) I think that running in the background might be problematic, but this is off by default anyway.

As far as the `view([k,g])` issue, that's purely a LaTeX thing: the code

```
\[  <code for k>, <code for g> \]
```

gets passed directly to LaTeX, and that's why the vertical spacing and the size of the brackets is the way it is.  Maybe we could modify the LaTeX code for either k or g to fix this, but since these are toy examples anyway, I don't think it's worth fixing.  My suggestion would instead be to either not view graphs or knots as members of lists, or write the `_latex_` methods for the real Sage objects so that they work well in this context.



---

archive/issue_comments_048525.json:
```json
{
    "body": "apply only this patch",
    "created_at": "2009-06-08T05:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48525",
    "user": "@jhpalmieri"
}
```

apply only this patch



---

archive/issue_comments_048526.json:
```json
{
    "body": "Attachment [avoid-jsmath-version4.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath-version4.patch) by @jhpalmieri created at 2009-06-08 05:36:40\n\ndo not apply: for reference only",
    "created_at": "2009-06-08T05:36:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48526",
    "user": "@jhpalmieri"
}
```

Attachment [avoid-jsmath-version4.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-jsmath-version4.patch) by @jhpalmieri created at 2009-06-08 05:36:40

do not apply: for reference only



---

archive/issue_comments_048527.json:
```json
{
    "body": "Attachment [avoid-delta34.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-delta34.patch) by @rbeezer created at 2009-06-08 06:56:58\n\nPasses all tests (sage -testall) and documentation builds cleanly.\n\nWorks well as designed, and I'm getting much more sensible behavior (fallbacks and error messages) when I simulate dvipng or convert missing.  The extra comments and rearrangements in the code make it easier to understand what's happening.\n\nI meant to say a while back that it makes sense to not work too hard on the lists of objects - if you want a nice graphic of just a single object, you can just view it all by itself.  And then simple lists should/can behave rationally.\n\nDocumentation looks real good, plus its great to see doctests getting very close to 100%.\n\nI applied #5975 on top of this, and then it works well for displaying any graph.\n\nNice work!",
    "created_at": "2009-06-08T06:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48527",
    "user": "@rbeezer"
}
```

Attachment [avoid-delta34.patch](tarball://root/attachments/some-uuid/ticket6089/avoid-delta34.patch) by @rbeezer created at 2009-06-08 06:56:58

Passes all tests (sage -testall) and documentation builds cleanly.

Works well as designed, and I'm getting much more sensible behavior (fallbacks and error messages) when I simulate dvipng or convert missing.  The extra comments and rearrangements in the code make it easier to understand what's happening.

I meant to say a while back that it makes sense to not work too hard on the lists of objects - if you want a nice graphic of just a single object, you can just view it all by itself.  And then simple lists should/can behave rationally.

Documentation looks real good, plus its great to see doctests getting very close to 100%.

I applied #5975 on top of this, and then it works well for displaying any graph.

Nice work!



---

archive/issue_comments_048528.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-13T21:09:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6089",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6089#issuecomment-48528",
    "user": "@ncalexan"
}
```

Resolution: fixed
