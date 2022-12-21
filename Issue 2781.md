# Issue 2781: bool() for SymbolicEquation should raise an error when it doesn't know the answer

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-04-02 21:45:36

Assignee: was

Currently, it returns False, which makes a return value of False fairly worthless.


---

Attachment

The patch currently passes minimal doctests, but breaks lots of other doctests.  I've run out of time to work on it now, but will look at this later.


---

Comment by jason created at 2008-04-09 06:16:07

Resolution: invalid


---

Comment by jason created at 2008-04-09 06:16:07

After discussion on IRC, the consensus was that this is *not* pythonic (see, for example, the docs for __nonzero__ at http://www.python.org/doc/2.3.5/ref/customization.html )

This functionality should probably be a different function than the builtin bool function.  The current functionality should stand as it is.

Eventually, as we get quantifiers worked into the system, it would be nice to have a function that said if an equation was always true, always false, sometimes true, sometimes false, etc.  Something like Reduce in Mma would be nice.
