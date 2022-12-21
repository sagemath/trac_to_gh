# Issue 3828: Upgrade to linbox-1.1.6rc1

Issue created by migration from Trac.

Original creator: cpernet

Original creation time: 2008-08-12 23:54:36

Assignee: cpernet

Keywords: charpoly

The main improvement in 1.1.6rc1 is the fix to the charpoly bug (see #3671), plus some memory management improvement and memleak fixes.

Therefore the workaround with 1.1.6rc0, bypassing this implementation is now removed.



---

Comment by cpernet created at 2008-08-12 23:56:40

The proposed spkg is here:
[http://sage.math.washington.edu/home/pernet/linbox-1.1.6rc1.spkg](http://sage.math.washington.edu/home/pernet/linbox-1.1.6rc1.spkg)


---

Comment by mabshoff created at 2008-08-13 07:04:43

Works for me. Positive review. Clement also ran ssmod.py 300 times and it no longer failed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-13 07:05:01

Merged in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-13 07:05:01

Resolution: fixed
