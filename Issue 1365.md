# Issue 1365: golden_ratio._algebraic_() should synthesize the value

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2007-12-02 05:28:02

Assignee: was

CC:  donmorrison robertwb

Robert Bradshaw points out that golden_ratio._algebraic_ might as well synthesize the value, instead of using a special-purpose function in qqbar.py (and there's a patch to do this as part of Robert's patch at #1275).  But I want to make qqbar.py a bit more efficient for that case, before making the change.


---

Comment by cwitty created at 2007-12-02 18:24:31

Changing status from new to assigned.


---

Comment by cwitty created at 2007-12-02 18:24:31

Changing assignee from was to cwitty.


---

Comment by kcrisman created at 2009-09-28 20:08:26

Has this been resolved by #1275?  This ticket has had no change for nearly two years.


---

Comment by donmorrison created at 2010-11-07 19:34:56

The docstring examples look like they return RLF(1/2*sqrt(5) + 1/2).  Since phi is known to be algebraic, would it be ok to just return that?


---

Comment by donmorrison created at 2010-11-07 19:34:56

Changing status from new to needs_info.


---

Comment by donmorrison created at 2010-11-09 00:47:16

I tried RLF, and it's not the correct datatype for the current doctests and/or framework.  Certainly someone familiar with the internals must know the correct datatype...the ticket is only 3 years old.  If it's straightforward, I have a spare machine...


---

Comment by donmorrison created at 2010-11-09 03:50:15

"return (field(5).sqrt() + 1) / 2"

Works except for one test:

File "/home/donmorrison/sage46fromsrc/sage/devel/sage/sage/rings/qqbar.py",
line 135:
   sage: AA(golden_ratio)^2 - AA(golden_ratio)
Expected:
   1
Got:
   1.000000000000000?

The doctest could be changed to 
sage: bool(1 == AA(golden_ratio)^2 - AA(golden_ratio))
True

but Robert says that's not good.  What's the next step?


---

Comment by donmorrison created at 2010-11-09 03:54:01

Sorry, I didn't notice there was special trac markup obscuring my last update.

The former and proposed doctests should read:

File "/home/donmorrison/sage46fromsrc/sage/devel/sage/sage/rings/qqbar.py",
line 135:
   sage: AA(golden_ratio)!^2 - AA(golden_ratio)
Expected:
   1
Got:
   1.000000000000000?

vs.

sage: bool(1 == AA(golden_ratio)!^2 - AA(golden_ratio))

True


---

Comment by robertwb created at 2010-11-09 07:29:48

Changing component from algebraic geometry to basic arithmetic.


---

Comment by robertwb created at 2010-11-09 07:29:48

I'm thinking this ticket could just be closed--the current way of doing things works fine (lots has changed since this ticket was opened, in particular the entire Sage symbolics system was moved to PyNaC, so this isn't very relevant anymore. In particular, I don't see any benefit to the `AA(golden_ratio)^2 - AA(golden_ratio)` regression.


---

Comment by mhansen created at 2011-12-17 20:07:04

I agree with Robert's analysis.


---

Comment by mhansen created at 2011-12-17 20:07:04

Resolution: invalid
