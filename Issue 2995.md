# Issue 2995: [with patch, needs review] some new functionality and doctests for congruence subgroups

Issue created by migration from Trac.

Original creator: AlexGhitza

Original creation time: 2008-04-22 03:34:36

Assignee: craigcitro

Keywords: congruence subgroup

The attached patch does the following:

1. allow coercing a 2x2 matrix (or a list of 4 elements) into a congruence subgroup: Gamma0(5)([1,5,1,6]) now works

2. modified G.generators() so that it actually returns a list of elements of the group G instead of just matrices

3. added gens()

4. added a bunch of doctests

Right now, all these changes are for Gamma0 and Gamma1 subgroups; I will do the same with GammaH subgroups as soon as I figure out how these work.



---

Attachment

I've replaced the previous patch with one that also has the changes listed above for the groups Gamma_H.


---

Comment by ncalexan created at 2008-04-25 23:16:50

Patch looks good, doctests are good too.

I hate the name `acton` -- it looks like a typoed `action`.  Could we change that to `act_on`?


---

Comment by mabshoff created at 2008-04-26 00:42:19

Merged in Sage 3.0.1.alpha0


---

Comment by mabshoff created at 2008-04-26 00:42:19

Resolution: fixed


---

Comment by AlexGhitza created at 2008-04-26 02:49:53

Nick: good point about acton().  I am planning to do some more work on congroup.py and friends, and I'll fix this then.
