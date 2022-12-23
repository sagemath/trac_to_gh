# Issue 3909: Updating jmol package to latest [Needs Review]

Issue created by migration from https://trac.sagemath.org/ticket/3909

Original creator: jkantor

Original creation time: 2008-08-20 06:16:59

Assignee: mabshoff

The jmol package hasn't been updated recently and i've experienced frequent crashes (on windows) so I have updated the package to latest. I have only currently tested it on OSX, so validation on other browsers would be good. 

http://sage.math.washington.edu/home/jkantor/spkgs/jmol-11.6.RC8.spkg


---

Comment by robertwb created at 2008-08-22 07:45:16

Works great for me too, though I'm also on OS X.


---

Comment by jason created at 2008-08-27 14:25:16

Works great for me for a variety of plots from the plot3d and parametric_plot3d docstrings.  This is on Ubuntu 8.04 32bit with Firefox 3.

Positive review pending some changes to the spkg:

1. The Changelog in SPKG.txt should be in reverse chronological format, but the latest update is at the bottom.

2. The title at the top of SPKG.txt should be changed to reflect this version.

3. The SPKG.txt~ emacs backup file should be deleted


---

Comment by jason created at 2008-08-27 14:26:17

Does this spkg seem to solve your crash problems on Windows? (Just curious)


---

Comment by mabshoff created at 2008-08-28 23:42:26

A cleaned up spkg which fixes all of Jason's issues is at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/alpha2/jmol-11.6.rc8.spkg

So I consider this a positive review now.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-28 23:57:49

Merged in Sage 3.1.2.alpha2


---

Comment by mabshoff created at 2008-08-28 23:57:49

Resolution: fixed
