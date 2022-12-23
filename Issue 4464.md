# Issue 4464: devel/sage/sage/combinat/root_system/weyl_characters.py test (too) long

Issue created by migration from https://trac.sagemath.org/ticket/4464

Original creator: jsp

Original creation time: 2008-11-07 17:58:33

Assignee: mabshoff

Keywords: test, long

Jaap,

can you please open a ticket for that one. I suspect that we don't
have anything tested via long or that the tests aren't properly marked
"#long time". This one has popped up so often that we really ought to
fix it once and for all since you hit it every time.

[...]

Cheers,

Michael


---

Comment by bump created at 2008-11-08 12:02:54

I think the file weyl_characters.py should be converted to Cython. The single most computationally intensive thing is the Freudenthal multiplicity formula (which is invoked a lot).


---

Comment by mabshoff created at 2008-11-09 00:30:56

Replying to [comment:1 bump]:
> I think the file weyl_characters.py should be converted to Cython. The single most computationally intensive thing is the Freudenthal multiplicity formula (which is invoked a lot).

Hi Dan,

that sounds fine to me, but we should do that on another ticket post Sage 3.2.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 22:40:25

#5721 fixed this.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 22:40:25

Resolution: fixed
