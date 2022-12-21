# Issue 5819: make sage -coverage require a loads/dumps test for each class defined in a file

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2009-04-19 02:51:45

Assignee: mabshoff

Keywords: coverage loads dumps

At the moment, `sage -coverage file.py` complains if `file.py` has no doctests of the form `s == loads(dumps(s))`.  However, it says nothing if there is only one such doctest in `file.py`, independent of how many different classes are defined in that file.

Ideally, we would have a doctest `s == loads(dumps(s))` for every single class.  Thus, we should change `sage -coverage` to detect if there are classes without such doctests and complain about it.

See also the thread at
http://groups.google.com/group/sage-devel/browse_thread/thread/bc99d36058aff638


---

Comment by nthiery created at 2009-10-19 20:42:10

This should now be a test of the form TestSuite(s).run() (see also #7209).
