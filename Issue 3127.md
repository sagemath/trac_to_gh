# Issue 3127: abelian groups (are lame?) -- bug in comparison of subgroups with group

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-07 22:22:43

Assignee: joyner

WARNINGS: 
  1. David Roe is recently rumored to be rewriting abelian groups.  
  2. I recently rewrote abelian groups but my patch rotted: #1849
  3. There are other known problems with subgroups of abelian groups: #2272


OK, now the bug report.  This is inconsistent and lame:


```
sage: A = AbelianGroup(1,[6])
sage: A.subgroup(list(A.gens())) == A
False
sage: A = AbelianGroup(2,[2,3])
sage: A.subgroup(list(A.gens())) == A
True
```


This is the original email reporting the bug:

```
Hi there,

When I define an abelian group
A = AbelianGroup(1,[6])
and then generate a subgroup that actually is the whole group itself,
and then compare it to the original group:
A.subgroup(list(A.gens())) == A
the result may be either True or False. In this example it is False.
When defining A as
A = AbelianGroup(2,[3,2])
it is False as well, but when I define it as
A = AbelianGroup(2,[2,3])
it is True.
My guess is that this is because comparison of finite Abelian groups
is implemented using their invariant factors, but when you create the
group using factors that are not in canonical form or not in
increasing order, these are used instead of the ordered list of
invariant factors anyway.

Greetings,

Utpal Sarkar
```



---

Comment by roed created at 2008-05-07 22:30:39

I am working on rewriting, but won't be able to work on it for the next week (I'm at a conference then need to finish a final).  If someone else wants to do something in this direction, let me (or sage-devel) know.


---

Comment by cremona created at 2008-05-08 08:17:53

Is this actually a bug?  It would certainly wrong if the test being
performed was isomorphism rather than equality, but I think it is
actually reasonable for two finite abelian groups to only be reported
as "equal" when they are presented the same way.

Having said that I agree that is does not look right for a group to have a _subgroup_ which is isomorphic to but not equal to itself.


---

Comment by wdj created at 2008-05-08 11:33:14

Will all due respect to myself, I think it is better if someone like David Roe works on this package than the original author, who seems to have created a mess of things:-). Can someone (Michael?) please change the owner from "joyner" to "David Roe" or whatever abbreviation he likes to use?


---

Comment by mabshoff created at 2008-05-08 11:35:06

Changing assignee from joyner to roed.


---

Comment by fwclarke created at 2008-05-09 08:38:46

See also #1284.


---

Comment by rlm created at 2008-05-10 23:36:56

Patch at #1284 fixes this.


---

Comment by mabshoff created at 2008-05-26 16:43:50

Fixed by merging #1284 in Sage 3.0.3.alpha0.


---

Comment by mabshoff created at 2008-05-26 16:43:50

Resolution: fixed
