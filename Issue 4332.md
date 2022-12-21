# Issue 4332: notebook() docstring needs improvement

Issue created by migration from Trac.

Original creator: ddrake

Original creation time: 2008-10-21 00:28:35

Assignee: ddrake

CC:  jason

The docstring for notebook() could use a bit of improvement. In particular, the `directory` option should be clearer. I also think we should *not* say "do a web search for more details"; if the information is too much for the docstring, we should make a page on the wiki and point users to that.

Also, given the recent forkbomb on sage.math, the `-u` flag for ulimit should be documented.

I plan to work on this during this week's Bug Day.


---

Attachment

Patch attached. A lot of it is reformatting and typos, but I also added a reference to a new page on the wiki: http://wiki.sagemath.org/StartingTheNotebook. The installation guide only has a page on running a publically-accessible notebook server (http://sagemath.org/doc/inst/node10.html) and nothing on other single-user cases.

Also, that page on the installation guide is outdated; someone should go through and fix it up, and perhaps add something on using virtual machines, which these days seems to be the way to go; I have a start at that at http://wiki.sagemath.org/DanDrake/JustEnoughSageServer.


---

Comment by mhansen created at 2008-10-24 02:55:32

Nice work.


---

Comment by mabshoff created at 2008-10-26 03:25:14

Resolution: fixed


---

Comment by mabshoff created at 2008-10-26 03:25:14

Merged in Sage 3.2.alpha1.

Dan: Please post patches and not diffs in the future.

Cheers,

Michael


---

Comment by ddrake created at 2008-10-26 23:52:03

Replying to [comment:4 mabshoff]:
> Dan: Please post patches and not diffs in the future.

Oops. Sorry. I keep doing `qdiff` when I mean `export qtip`.
