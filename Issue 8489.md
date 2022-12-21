# Issue 8489: New `sageexample` environment for sagetex

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2010-03-10 15:24:32

Assignee: mvngu

CC:  ddrake zimmerma

Keywords: sagetex, doctest

The attached patch for sagetex adds a new sageexample environment for sagetex:


```
\begin{sageexample}
  sage: 1+1
  2
  sage: x^3
  x^3
\end{sageexample}
```


The (ultimate) goal is to allow for straightforward copy paste of
pieces of sage doctests into one's latex document. See the attached
pdf (the sources of which are included in the patch) for details.




---

Attachment


---

Attachment


---

Comment by nthiery created at 2010-03-10 15:27:52

Changing status from new to needs_review.


---

Attachment

Clone of the current spkg, with patch applied, but version number not bumped up


---

Comment by ddrake created at 2010-03-11 07:56:19

Hrm, your spkg contains a core dump from pdflatex. Perhaps that's a bad sign? :)

I'll take a look at this, and probably include it. My long-term goal is that you shouldn't need to include the answer -- you should just put `((x+1)^3).expand()` and it would automatically insert the nicely typeset version of `x^3 + 3*x^2 + 3*x + 1`.


---

Comment by ddrake created at 2010-03-11 08:14:36

Also, I should add that a nice way to make improvements to SageTeX is to clone http://bitbucket.org/ddrake/sagetex/ and send me patches. :)  In the spkg, you added your changes into the root hg repo, which just tracks SPKG.txt, spkg-install, and so on.


---

Comment by ddrake created at 2010-03-15 01:45:14

There's a spkg at http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.2.4.spkg that includes these changes. It needs further documentation, but you should be able to take the example file included in attachment:trac_8489-sagetex_sageexample-nt.patch and typeset it with the new spkg. There's also some examples in the usual example.tex file.

I have had troubles getting doctesting to work -- every time I try `sage -t my_file.sage`, it fails with a "mysterious error". Same thing if I try with the .py file.


---

Comment by nthiery created at 2010-03-17 22:56:05

Replying to [comment:4 ddrake]:
> Also, I should add that a nice way to make improvements to SageTeX is to clone http://bitbucket.org/ddrake/sagetex/ and send me patches. :)  In the spkg, you added your changes into the root hg repo, which just tracks SPKG.txt, spkg-install, and so on.

Ah, great, thanks for the link! I googled for it, somehow missed it, and went for the quickest way to send you a patch.


---

Comment by nthiery created at 2010-03-17 22:58:18

Replying to [comment:3 ddrake]:
> Hrm, your spkg contains a core dump from pdflatex. Perhaps that's a bad sign? :)

Yeah, I am not patient, and did kill pdflatex the hard way a couple times while trying things around :-)


---

Comment by nthiery created at 2010-03-17 23:00:12

Replying to [comment:5 ddrake]:
> I have had troubles getting doctesting to work -- every time I try `sage -t my_file.sage`, it fails with a "mysterious error". Same thing if I try with the .py file. 

Yeah, just reusing my_file.sage looked cool, and worked on trivial examples, but that is not robust. I am about to upload a new patch which produces a separate file with just the doctests, and that seems to work fine (and is probably more readable by the user in case of trouble).


---

Attachment


---

Comment by nthiery created at 2010-03-17 23:34:17

Changing assignee from mvngu to nthiery.


---

Comment by ddrake created at 2010-03-25 03:48:37

I've merged your doctest-spacing patch into SageTeX, and made some improvements -- the doctest file is now called `\jobname_doctest.sage`, and is only created if the user actually has a `sageexample` environment. It also includes a bit of explanatory text.

I also changed your vertical space fix to use `\abovedisplayskip` and friends, which I just learned about from http://www.ctan.org/tex-archive/info/math/voss/mathmode/.

There's more fixups to the documentation that should be done, but it seems to be working properly. Please pull from the bitbucket repo and test. I think I'll make a spkg for this new version and see if we can get it into the next Sage release.


---

Comment by jason created at 2010-03-30 03:52:13

This should be closed when #8605 is merged (possibly just closed now, since the changes are for upstream, not for something that is Sage code).


---

Comment by mmeulien created at 2010-03-30 21:51:55

For reference: Copy-paste from a PDF document to a Sage session won't necessarily work. That is, if a sageexample environment contains strings defined using (simple) quotes, those quotes can be rendered in PDF by differents characters: backquotes and quotes. The encoding used in TeX sources files seems to have its role here.


```
\documentclass[12pt]{book}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{sagetex}
\usepackage[frenchb]{babel}
\begin{document}
\begin{sageexample}
    sage: x, y, a, b, c, d = var('x y a b c d')
\end{sageexample}
\end{document}
```

Replying to [ticket:8489 nthiery]:

> The (ultimate) goal is to allow for straightforward copy paste of pieces of sage doctests into one's latex document. See the attached pdf (the sources of which are included in the patch) for details.^^


---

Comment by mmeulien created at 2010-03-30 21:54:06

Example of quotes changed to backquotes in PDF


---

Attachment

ddrake: what do you say about the last comment about quotes being changed?


---

Comment by mmeulien created at 2010-04-19 22:08:50

The following has no effect on sageexample environments:

\setlength{\sagetexindent}{15ex}

Seems to be a bug, no?


---

Comment by ddrake created at 2010-04-20 06:49:40

Replying to [comment:13 jason]:
> ddrake: what do you say about the last comment about quotes being changed?

I'm not sure how to fix that. I don't think it's an issue about encoding in the document; a single straight quote (ASCII character 39) should be the same in any non-crazy encoding, since all reasonable encodings that I know of agree for characters 0 to 127.

The issue, I think, is the character that gets put into the final PDF. I'm not sure how to bypass the usual TeX behavior of turning single quotes into curly final quotes.

In any case, Nicolas' original goal is cut and paste from Sage into a LaTeX document, which works now.

If this is a highly desired feature, I could work on it, but since cut and paste of things with single quotes generally doesn't work from TeX-generated PDFs anyway, I'm not sure how important this should be.


---

Comment by ddrake created at 2010-04-20 07:10:42

Replying to [comment:14 mmeulien]:
> The following has no effect on sageexample environments:
> 
> \setlength{\sagetexindent}{15ex}
> 
> Seems to be a bug, no?

Hmmm. I tried to get the indent to work, but adding an hspace in the obvious places didn't work. I can investigate this more, but one problem is that the example environment works in a completely different way than the other verbatim-like environments. I'll look into this and see if I can figure it out. Changing the parindent might work.


---

Comment by jhpalmieri created at 2010-04-23 17:13:50

Since #8605 is closed, should this be closed also?  It looks like there is still discussion going on here...


---

Comment by jhpalmieri created at 2010-07-22 22:45:01

This ticket is marked as "needs review", but is there anything still to review here?  Have the relevant pieces been merged into the sagetex spkg by now?


---

Comment by ddrake created at 2010-07-28 03:23:41

I think this ticket should be closed, since the sageexample environment has been implemented, and we ship a version of SageTeX with it. If there are further problems with sageexample, someone should open a new ticket.


---

Comment by ddrake created at 2010-07-28 03:23:41

Resolution: fixed
