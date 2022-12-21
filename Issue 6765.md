# Issue 6765: [with patch, needs review] Linear Programming in Tutorial's Tour !

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-08-16 18:50:02

Assignee: tba

CC:  mvngu

Hello !!!

Following http://groups.google.com/group/sage-devel/browse_thread/thread/9d9b09274f1eab83/79938a2139ba25d9?lnk=gst&q=isr#79938a2139ba25d9 , here is the requested Tutorial page for Linear Programming.

.... Even if until now, the Linear Programming patch is still waiting to be merged, and GLPK is not even included in Sage ;-)

I hope you will like it !!! And thanks to Minh for helping me with Sphinx !


---

Comment by mvngu created at 2009-08-22 23:44:05

folded patch


---

Attachment

The patch `trac_6765-tutorial-lp-folded.patch` folds all three patches in `tutorial_lp.patch`. With the folded patch, changes are easier to review. Only `trac_6765-tutorial-lp-folded.patch` should be reviewed.


---

Comment by mvngu created at 2009-08-23 11:16:27

I get the following error even after installing both GLPK and CBC:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: linear_function = {"variable1" : 2, "variable2" : -1}
sage: linear_function = {1 : 2, 2 : -1}
sage: linear_function={(1,1) : 1, (1,2) : 2, (2,1) : 3, (2,2) : 4}
sage: p = MIP(sense=1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/.sage/temp/sage.math.washington.edu/28962/_home_mvngu__sage_init_sage_0.py in <module>()

NameError: name 'MIP' is not defined
```

Nathann, you need to give commands on how to use the MIP capabilities of CBC. Where is `MIP()` defined? How do I import and use it? Please include those information in your patch.


---

Comment by mvngu created at 2009-08-23 12:19:34

Here's a conversion in IRC with Nathann:

```
05:00 < ncohen> mvngu: I do not understand the problem you have with MIP. It seems you copied some part of the examples into Sage
05:00 < ncohen> mvngu: and Sage answered it did not know where to find the class MIP
05:01 < ncohen> mvngu: even though I have added in sage/numerical/all.py a line : from MIP import *
05:01 < mvngu> ncohen: David Joyner replied to me in an email that it depends on #6502.
05:01 < mvngu> So I'll mark #6765 as depending on #6502.
05:02 < ncohen> ooooops
05:02 < ncohen> sorry ^^;
05:02 < mvngu> This means that #6502 must be merged first.
05:02 < ncohen> I've been working on this for some timme so sometimes I forget about it... ^^;
05:02 < ncohen> indeed
05:02 < ncohen> the thing is that I already posted something like 5 or 6 patches based upon #6502
05:02 < ncohen> LP is so useful for graphs !
05:03 < mvngu> Since GLPK is an optional spkg at the moment, so the doctests that depends on GLPK should be flagged as optional.
05:03 < mvngu> Do so with the flag "# optional" in doctests.
05:04 < mvngu> That way, when the test suite is run, anything with the flag "# optional" would be skipped over.
05:04 < mvngu> Unless you have the required optional spkg installed.
05:05 < ncohen> I see... :-/
05:05 < mvngu> And any doctests that depend on CBC must also be flagged as "# optional".
```

Also, this ticket depends on #6502.


---

Comment by ncohen created at 2009-08-24 15:54:57

I just updated tutorial_lp.patch. Please do not use trac_6765-tutorial-lp-folded.patch which is now an outdated version !


---

Comment by ncohen created at 2009-08-31 15:55:43

As the functions dealing with LP have not been reviewed, I prefer to rewrite the MIP class for Sage to make it easier to use. I will post a new version of the MIP patch as soon as possible, along with all the patches for functions using it.

Sorry for the trouble, I'll try to make it quick !

Nathann


---

Comment by ncohen created at 2009-09-03 12:40:18

The new LP tutorial matching the Trac ticket #6869 is here, ready for review ;-)

Nathann


---

Attachment


---

Comment by ncohen created at 2009-09-29 12:53:31

New version coherent with the changes from #7012


---

Comment by jhpalmieri created at 2009-11-19 22:13:14

Changing status from needs_review to needs_work.


---

Comment by jhpalmieri created at 2009-11-19 22:13:14

Some comments: 

(1) When I run "sage -docbuild tutorial html", it complains

```
/Applications/sage/devel/sage/doc/en/tutorial/tour_LP.rst:64: (WARNING/2) Title underline too short.

Variables in ``MixedIntegerLinearProgram``
""""""""""""""""""""""""""
```

The string of double quotes should line up exactly with the previous line.  (Maybe it's good enough it is at least as long, but I think it should be the same length.)

(2) In a string like `minimized ( for example `2 x + y` )`, you shouldn't have a space after `(` or before `)`: it should say `minimized (for example `2 x + y`)`.  This happens throughout the document.  Along the same lines, there should be no space before "?" or before ":".  Before a block of examples (like lines 69-70), I think you want a visible colon, and you achieve that by having "::" with no preceding space.  (Using "::" with a preceding space signals a block of examples but doesn't print a colon at all.)

(3) On line 75, "remperature" should presumably be "temperature".  Try running a spell check.

(4) You don't have a period at the sentence ending the paragraph "What is a Mixed Integer Linear Program ?"  I haven't done any more careful proofreading, but you should check for other spelling, usage, and grammar errors.

(5) In multiline doctests, you need to change "....:" to "...".  As it stands, doctesting bombs on these lines.

(6) If I don't have GLPK or numerical.MIP installed, doctests have to pass anyway.  Also, if I don't have them, I absolutely don't want doctesting to try to install them, which the lines

```
     sage: # To install GLPK
     sage: install_package('glpk')
     sage: # To install Coin-OR Branch and Cut ( CBC )
     sage: install_package('cbc')
```

will do.  Maybe mark those lines as "# not tested"?


---

Comment by jhpalmieri created at 2009-11-20 01:34:43

One more thing: since the content depends on the optional packages, you should say that at the *beginning* of the section, not the end.  Otherwise, someone may start working through the examples, only to have nothing go as advertised, and they quit trying before they get to the disclaimer at the end.


---

Comment by was created at 2009-11-20 01:51:42

We (me, John P., and Minh) discussed this on irc and think that optional packages shouldn't be required to work through the main Sage tutorial.


---

Comment by was created at 2009-11-20 01:51:42

Resolution: wontfix


---

Comment by mvngu created at 2009-12-08 23:54:49

Feel free to open another ticket to put the linear programming tutorial in the [Constructions](http://www.sagemath.org/doc/constructions/) document.


---

Comment by ncohen created at 2009-12-10 14:31:44

Could I do the same with my former ( and refused ) Graph Tour ?


---

Comment by mvngu created at 2009-12-10 18:32:52

Replying to [comment:15 ncohen]:
> Could I do the same with my former ( and refused ) Graph Tour ?

Sure! Go for it.
