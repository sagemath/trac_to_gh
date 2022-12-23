# Issue 5397: SmallGroups library can't be used in Sage-3.3

Issue created by migration from https://trac.sagemath.org/ticket/5397

Original creator: SimonKing

Original creation time: 2009-02-27 21:06:24

Assignee: mabshoff

Keywords: SmallGroups library gap package

As I reported at http://groups.google.com/group/sage-support/browse_thread/thread/b82584e0ee6ba733, it seems that the `SmallGroups` library can not be used in `sage 3.3`.

More precisely: I installed `database_gap-4.4.10`
and `gap_packages-4.4.10_6` -- apparently with success. But when I tried to use it, say, with `gap('NumberSmallGroups(128)')`, an error is raised, complaining about the `SmallGroups` library being missing.

This occurs in the following settings:
 - sage-3.3 built from source on x86_64 GNU/Linux, Dual Core AMD Opteron(tm) Processor 270, gcc (GCC) 4.1.2 20061115 (prerelease) (SUSE Linux)
 - sage-3.3 obtained by an upgrade of sage-3.1.2 (built from source) on the same machine
 - sage-3.3 obtained by an upgrade of sage-3.2.3 (built from source) on x86_64 GNU/Linux, AMD Athlon(tm) 64 Processor 3700+, gcc (GCC) 4.2.1 

It does not occur in a sage-3.3.rc0 install on `sage.math`. Perhaps this helps to locate the source of trouble.


---

Comment by wdj created at 2009-03-03 02:39:39

The tarball at http://sage.math.washington.edu/home/wdj/patches/gap_packages-4.4.12_1.spkg fixes this for sage-3.4.alpha0 running on an amd 64 ubuntu 8.10 system. It probably works for other recent versions of sage running on other linux os computers. It fails on an OS 10.4 macbook running sage-3.2.3 (which had gap-4.4.10).

Hope this helps some.


---

Comment by wdj created at 2009-03-03 12:56:00

I mislabled this as needs review. I don't know how to fix the patch for an os 10.4 macbook. I tried a few possibilities (uncommenting a line which installs patches) but nothing I tried worked and I'm not sure what the solution is.


---

Comment by wdj created at 2009-03-03 13:43:52

I have posted the patch for the databases as well: http://sage.math.washington.edu/home/wdj/patches/database_gap-4.4.12.spkg. 

This also fails for an intel macbook running OS 10.4 and sage-3.3.alpha2 (I mistakenly said sage-3.2.3 before). I have not a clue why these fail for a macbook and not linux, so I don't know how to proceed further with this.

Hope this helps a little anyway.


---

Comment by SimonKing created at 2010-07-05 11:49:12

Can this be closed? I did not have any trouble with database_gap recently...


---

Comment by SimonKing created at 2012-03-02 10:16:21

Changing status from needs_work to positive_review.


---

Comment by SimonKing created at 2012-03-02 10:16:21

I'm giving a positive review, in the sense that I don't see a problem with the small groups library since many months.

I suggest to resolve it as duplicate, even though I couldn't point my finger to a ticket in which the problem had been solved.


---

Comment by jdemeyer created at 2012-03-02 13:54:52

Resolution: worksforme
