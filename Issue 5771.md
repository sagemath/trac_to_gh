# Issue 5771: %latex should issue a warning if latex isn't installed on the system

Issue created by migration from https://trac.sagemath.org/ticket/5771

Original creator: mabshoff

Original creation time: 2009-04-13 03:21:10

Assignee: cwitty

CC:  rbeezer

Right now on sagenb latex is not installed. So when someone evaluates a %latex cell, i.e. someone == Bill Hart, it just hangs:

```
mabshoff@sagenb:~$ latex
The program 'latex' is currently not installed.  You can install it by typing:
sudo apt-get install texlive-latex-base
-bash: latex: command not found
mabshoff@sagenb:~$ echo $?
127
```


Cheers,

Michael


---

Comment by was created at 2009-04-13 14:19:51

just an fyi, i just issued the command on sagenb.org to install latex, so it will be there soon...


---

Comment by jhpalmieri created at 2009-06-11 01:38:36

Changing assignee from cwitty to jhpalmieri.


---

Comment by jhpalmieri created at 2009-06-11 01:38:36

Here's a patch.  This depends on #6089.


---

Comment by jhpalmieri created at 2009-06-11 01:38:36

Changing status from new to assigned.


---

Comment by rbeezer created at 2009-06-11 04:51:59

This all looks good, especially since #6089 makes it so easy to add in these checks.

I'm getting a doctest failure at line 119, the first "have_dvipng" test is failing.  I suspect some other test is setting the global variable so it is no longer "None" and due to the way tests get re-ordered and since there are now more tests, by the time this test is run, it will fail.  Indeed,

`sage -t --randorder sage/misc/latex.py`

can sometimes make all four of the "have_xxx" tests fail at the first check of each group, all in the same way.  So I think just the tests need adjustment where they don't assume they are the first ones run.

If I simulate having `latex` and `pdflatex` missing, then I get appropriate error messages.  But if I run the doctests with the two executables missing, then these error messages also bleed through in two doctests (at line 410 and line 1565).  Maybe the tests should each be converted into two variants and somehow logically combined with the values of `_have_latex` and `_have_pdflatex` and just return a logical value.  This doctest failure behavior is present with only #6089 applied (i.e. without the current patch) so we have a chance to fix it before #6089 gets merged (or we could hold it up).  I hadn't thought before to test with latex or pdflatex missing.  I'm presuming we don't want test failures just because a system does not include tex.

So I'm ready to give a positive review with adjusted doctests - everything else looks good.


---

Comment by jhpalmieri created at 2009-06-11 19:55:27

Here's a new patch.  This deletes the initial doctests for have_dvipng (etc.); I think the remaining doctests still adequately test whether the functions are working, and should work in any order of execution.  For the doctest failures when latex is missing, I just changed the doctests like this:

```
-        sage: _run_latex_(file)
+        sage: _run_latex_(file) # random - depends on whether latex is installed
}}} 
and similarly for the `png` doctest.  Do you think that's good enough?  It now passes all tests for me if latex and pdflatex are missing.


---

Attachment


---

Comment by rbeezer created at 2009-06-12 00:40:25

I was thinking today about the doctest failure with the global variable being set in the "wrong" order.  We've seen that movie before with this file, no?  :-;

Latex patch applies and builds against 4.0.1, now passes randomized testing on sage/misc/latex.py, documentation builds properly.

I think the current doctests are fine.  My thought for the two that failed with missing latex and missing pdflatex were along the lines of the following (but I haven't tested this at all).


```
sage: h, s = have_pdflatex(), png(ZZ[x], "zz.png", do_in_background=False)
sage: (h and s == None) or (not(h) and s.find('Error: PDFLatex') == 0)
True
```


That'd cover both possibilities, which was not really possible before the two new "have_xxx" checks.  So consider that simply a suggestion for the next time you are sprucing up the doctests in this file.

Positive review.

Release manager: Apply #6089 before the "trac_5771.patch" patch.


---

Comment by jhpalmieri created at 2009-06-12 01:36:29

Oh, I see, that's a nice idea.


---

Comment by rbeezer created at 2009-06-12 05:33:59

Replying to [comment:6 jhpalmieri]:
> Oh, I see, that's a nice idea.

I tried to do something similar on #5975 (which is coming along) and it didn't work so well.  The error messages come along via a "print", so are not part of a string that can be tested easily.

The minute you lose control over the user's environment it gets quite messy.  Oh well, ....


---

Comment by ncalexan created at 2009-06-13 21:44:11

Resolution: fixed
