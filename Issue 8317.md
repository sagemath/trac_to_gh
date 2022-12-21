# Issue 8317: Protecting special names against assignation

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-02-21 00:19:55

Assignee: olazo

Keywords: assignation,names

I'd like to propose that certain special names should be protected so that they could not become variable names (for example pi, e, and i)

if by accident you assign them like:

e=factorial(10)

and then you need to need to use e with it's standard meaning, like

e^100

you will have a very hard to spot error ( (factorial(10)^100).


---

Comment by olazo created at 2010-02-21 00:26:34

Changing component from misc to symbolics.


---

Comment by was created at 2010-02-21 01:21:58

his is something that can (and will) be made an optional mode.  We'll have several -- implicit multiplication, automatic variable name creation, and protected names. Having them all on could be useful for people teaching, e.g., calculus labs.   This protected mode, by the way, will in the long run use the same technique as automatic variable name creation: replacing the globals() dictionary by a customized wrapper.  This has a slight performance penalty, so definitely can't be the default.  But it is a fine idea for an optional mode.


---

Comment by burcin created at 2010-04-05 12:38:38

I see that this would be a desirable feature for users of symbolics. I don't think the implementation is related to the symbolics subsystem however. I'm assigning this back to the misc component.


---

Comment by burcin created at 2010-04-05 12:38:38

Changing component from symbolics to misc.


---

Comment by burcin created at 2010-04-05 12:38:38

Changing type from defect to enhancement.


---

Comment by olazo created at 2010-08-21 21:41:06

Changing priority from minor to major.
