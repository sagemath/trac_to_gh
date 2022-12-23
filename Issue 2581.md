# Issue 2581: extend solve_right to all cases; implement solve_left

Issue created by migration from https://trac.sagemath.org/ticket/2581

Original creator: was

Original creation time: 2008-03-18 02:30:42

Assignee: was

A.solve_right only worked for A nonsingular, and there was no solve_left.  Now A.solve_right should work for any A and there is a solve_left. 


---

Attachment


---

Comment by was created at 2008-03-18 02:38:42

WARNING:     def restrict_codomain(self, V) is not done yet (it's just a copy of restrict_domain).  I'll create a patch later tonight that correctly implements this.


---

Comment by was created at 2008-03-18 07:22:27

this provides the extra restrict_codomain functionality.


---

Attachment

Looks great. Merge this right away!


---

Comment by mabshoff created at 2008-03-18 10:23:47

Merged both patches in Sage 2.11.alpha0


---

Comment by mabshoff created at 2008-03-18 10:23:47

Resolution: fixed


---

Comment by ncalexan created at 2008-03-18 23:42:26

An unexpected problem: `solve_right` is defined in `matrix_integer_dense` and the versions don't provide the same functionality.  This could happen more places.

Is there any hope for a `solution_space_right` that handles under-determined systems?


---

Comment by was created at 2008-03-18 23:55:59

Changing status from closed to reopened.


---

Comment by was created at 2008-03-18 23:55:59

Resolution changed from fixed to 


---

Comment by was created at 2008-03-18 23:55:59

> An unexpected problem: solve_right is defined in 
> matrix_integer_dense and the versions don't provide 
> the same functionality. This could happen more places.

Good point -- I had meant to address that but fell asleep and forgot. 
A patch will be forthcoming. 

> Is there any hope for a solution_space_right that handles under-determined systems?

Not in this patch.  Make a trac ticket and somebody will get to it.


---

Comment by mabshoff created at 2008-03-19 00:22:55

For the record: This ticket was reopened after sage-2581.patch and sage-2581_part2-restrict_codomain.patch had been merged. So any additional patch should make clear how it should be applied.

Cheers,

Michael


---

Comment by was created at 2008-03-19 01:06:06

I'm attaching a patch that:

  1. addresses Nick's concern about derived classes overloading solve_right.

  2. I found that Clement recently introduced a solve right for sparse modn matrices for some reason, and that it had several bugs.  I've fixed those as well in this patch.


---

Attachment


---

Comment by ncalexan created at 2008-03-19 19:26:43

I think this looks good and should be applied.  I think that means part3 should be applied since the other two already have been.


---

Comment by mabshoff created at 2008-03-19 23:58:43

Merged sage-2581_part3.patch in Sage 2.11.alpha0.


---

Comment by mabshoff created at 2008-03-19 23:58:43

Resolution: fixed
