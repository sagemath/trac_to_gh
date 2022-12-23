# Issue 8486: Xelatex and Sage notebook

Issue created by migration from https://trac.sagemath.org/ticket/8486

Original creator: klee

Original creation time: 2010-03-10 07:38:38

Assignee: tbd

I think I want, e.g., the following works in Sage notebook.

%latex
실수 $x$에 대해서 다음이 성립한다.
\[
    \sqrt{x^2}=|x|
\] 

Dan writes:

I've recently learned about xelatex and think it's awesome -- I can
*finally* include Hangeul in my documents! We should definitely have a xelatex function, although it would usually be necessary to add stuff to the preamble to get the right fonts set up. But we already have
latex.add_to_preamble(), so it should be easy to get xelatex working.


---

Comment by klee created at 2010-03-10 07:45:47

Example Sage notebook


---

Attachment


---

Comment by klee created at 2010-03-10 07:46:41

Changing status from new to needs_review.


---

Comment by klee created at 2010-03-10 07:58:06

The example Sage notebook use the font AppleGothic which is perhaps only found in Mac OS.


---

Comment by ddrake created at 2010-03-12 07:36:45

This looks pretty good. I have some comments and it will need some minor changes, but already it seems to work!

For anyone else wanting to test this who's using Linux, you can replace the `latex.extra_preamble` with something like

```
latex.extra_preamble("\\"+r"usepackage{fontspec,xunicode,xltxtra}\setmainfont[Mapping=tex-text]{UnBatang}\setmonofont[Mapping=tex-text,Colour=0000AA]{UnDotum}")
```

In Linux, you should be able to do `fc-list :lang=ko` to get a list of fonts installed that support Korean; pick one and put that in and try this out. XeTeX is a standard part of TeXLive as of TL 2008, so it's not too hard to get.

I'll look over this patch and post my comments soon.


---

Comment by ddrake created at 2010-03-16 02:35:45

Hrm, this doesn't pass doctests. The first problem is that the "official" way to do deprecation is like this: for the `pdflatex` function (line 1188), you should do:

```
from sage.misc.misc import deprecation
deprecation('Use engine("pdflatex") instead.')
if t is None:
    return _Latex_prefs._option["engine"] == "pdflatex"
self.engine("pdflatex")
```

and then in the first doctest that uses the function:

```
sage: latex.pdflatex()
doctest:1: DeprecationWarning: Use engine("pdflatex") instead.
False
```

Also, I see that the `pdflatex` function never unsets the pdflatex engine -- I think we need

```
if t is None:
    return _Latex_prefs._option["engine"] == "pdflatex"
elif t:
    self.engine("pdflatex")
else:
    self.engine("latex")
```

so that `pdflatex(False)` does properly reset the engine.

Finally, in the `png` function (line 1749 or so), you need to change the pdflatex keyword to engine, and change the `_run_latex_` command on line 1795 or so.

Hmmm, it seems like the `view` command can call {{{png}} with the pdflatex keyword: see line 1721 or so (I've fiddled with latex.py, so my line numbers are a bit off):

```
png(objects, os.path.join(base_dir, png_file),
                debug=debug, do_in_background=False, pdflatex=pdflatex)
```

I think you'll need to move up the little snippet where you use the pdflatex keyword to decide what engine to use.

With these changes, doctests should pass.


---

Comment by ddrake created at 2010-03-16 02:35:45

Changing status from needs_review to needs_work.


---

Comment by klee created at 2010-03-16 03:58:31

Thank you, Dan. I will work on that.


---

Attachment

Updated the patch. Now all doctests pass.


---

Comment by klee created at 2010-03-16 13:17:40

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-03-17 08:25:38

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-03-17 08:25:38

Doctests pass, and the code looks good. Positive review.

I did write up a little bit of extra documentation; I'll post that patch in a moment. Could you look it over? It just adds a bit of explanation about adding to the preamble.


---

Comment by ddrake created at 2010-03-17 08:26:18

add a bit of new documentation.


---

Comment by jhpalmieri created at 2010-03-17 15:47:19

Changing status from positive_review to needs_work.


---

Attachment

Using `os.system('which xelatex >/dev/null')` won't work right on Solaris: on that OS, "which" has a return value of 0 even if the command is not found, so 

```
not bool(os.system('which xelatex >/dev/null'))
```

will always return True there.  Use the function `have_program` from #8474 instead.


---

Comment by jhpalmieri created at 2010-03-17 16:43:05

Expanding on this a bit: there has been a fair amount of work getting Sage to work on Solaris, and I think it does as of version 4.3.4.alpha1.  So I think that it is not a good time to put in a patch that doesn't work on Solaris; hence I've marked this as "needs work".  All you have to do to fix it is apply the patch at #8474 (now merged in 4.3.4.rc0) and then make the obvious change to this one line of the program...


---

Comment by ddrake created at 2010-03-17 23:10:16

Replying to [comment:12 jhpalmieri]:
> Expanding on this a bit: there has been a fair amount of work getting Sage to work on Solaris, and I think it does as of version 4.3.4.alpha1.  So I think that it is not a good time to put in a patch that doesn't work on Solaris; hence I've marked this as "needs work".  All you have to do to fix it is apply the patch at #8474 (now merged in 4.3.4.rc0) and then make the obvious change to this one line of the program...

That sounds good. I was aware of #8474 and decided to ignore that problem and open #8552, so that Kwankyu wouldn't have to rebase his patch -- but if it's a simple one-line change, then I suppose that's more reasonable.

If I rebase his patch, will you do a quick review?


---

Comment by jhpalmieri created at 2010-03-17 23:29:04

Replying to [comment:13 ddrake]:
> If I rebase his patch, will you do a quick review? 

Sure, and thanks for offering to rebase it.  (I understand your point, but I don't want to break Solaris support right away.  Let's wait a few weeks instead.  :)


---

Attachment

one-line change to use have_program


---

Comment by ddrake created at 2010-03-18 01:13:00

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-03-18 01:13:00

John, could you take a look at attachment:trac_8486_use_have_program.patch and attachment:trac_8486_extra_documentation.patch? The first fixes the problem you mentioned and preserves Solaris compatibility (I'm sure Dave Kirkby will appreciate that) and the second just adds a bit of extra documentation.


---

Comment by jhpalmieri created at 2010-03-18 01:53:16

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-03-18 01:53:16

Looks good to me.  One docstring is missing the "r" before the triple quotes, so I've added that.


---

Attachment

combines and replaces all previous patches


---

Attachment

I looked at Dan's extra documentation. It is nice. But I deleted the last comment in the doc of "engine" because r"\usepackage..." only fails in the notebook. See the discussion in 

!http://groups.google.com/group/sage-devel/browse_frm/thread/71cd8ec6313b7e16/da96b8c19ab45224#da96b8c19ab45224

See also the ticket 3154 at 

http://trac.sagemath.org/sage_trac/ticket/3154

So I think the problem of "\u" in the raw string in notebook is only temporary, assuming the ticket 3154 is reviewed sooner or later.


---

Comment by jhpalmieri created at 2010-03-18 02:06:32

Okay, the new "v2" patch doesn't require the "referee" patch.  Only apply the "v2" patch.


---

Comment by jhpalmieri created at 2010-04-15 23:55:03

Merged "trac_8486_v2.patch" into 4.4.alpha0.


---

Comment by jhpalmieri created at 2010-04-15 23:55:03

Resolution: fixed
