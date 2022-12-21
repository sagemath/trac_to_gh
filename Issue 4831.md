# Issue 4831: More number field ideal utilities

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-12-19 12:31:40

Assignee: was

CC:  davidloeffler m.t.aranes@warwick.ac.uk

Keywords: number fields, orders, ideals

This follows on from #4536:

    1. New invertible_residues() iterator for iterating though only the invertible residues modulo an integral ideal.
    2. New function like pari's add_to_1 so that A.add_to_1(B) return a in A such that 1-a is in B.  (The name of this might change before we upload a patch).

Patch to follows later today.

John Cremona and Maite Aranes


---

Attachment


---

Comment by cremona created at 2008-12-19 16:41:48

The attached file (based on 3.2.2) adds three functions, the ones mentioned in the description (with the second one called `element_1_mod()` as we could not think of a better name) and a 3rd one which is a version for integral ideas of the `prime_to_m_part()` function for integers.  the second and third of these were written by Maite Aranes.


---

Comment by mabshoff created at 2008-12-20 14:07:31

John,

we will probably not merge an aweful lot of patches into 3.3 before all the ReST patches go in.

Cheers,

Michael


---

Comment by cremona created at 2008-12-20 16:02:00

Replying to [comment:2 mabshoff]:
> John,
> 
> we will probably not merge an aweful lot of patches into 3.3 before all the ReST patches go in.
> 

That's fine, I knew that and meant to put 3.4 on it.

> Cheers,
> 
> Michael


---

Comment by davidloeffler created at 2009-01-15 12:17:58

Patch applies fine under 3.2.3; all tests in sage/rings/number_field pass; code looks fine and is very clearly laid out; and some experimentation with various random absolute number fields works fine. (I tried to test it for relative number fields, but they are currently so broken that I didn't succeed in even creating the objects to test it on.)

I like the element_1_mod function, but there is a natural generalisation: given ideals I, J which are not assumed coprime, one might want a function that expresses a given element of I + J as a sum of elements of I and J. But if anyone really wants this we can have a separate ticket for it.

My one reservation is that the docstrings will need tweaking for compatibility with the new ReST system. Other than that I think this is fine to go in.

David


---

Comment by cremona created at 2009-01-15 12:42:44

I agree that the more general function David suggests is useful, and it is also very easy to write:  set D=I+J, write 1=x+y with x in I/D, y in J/D using the function here, then for any d in D we have d=(dx)+(dy) with the factors in I,J.

On the other hand implementing this directly using the method we already use would perhaps be more efficient.  So let's not hold this up for that.

On the docstring comment -- yes, and the same is true for very many patches in there now!


---

Comment by mabshoff created at 2009-01-15 12:51:06

Replying to [comment:5 cremona]:

> On the docstring comment -- yes, and the same is true for very many patches in there now!

The patches for the ReST transition will be rebased post Sage 3.3.x, so no need to worry about that now. One of the goals of SD 12 is to get every patch that is ready into 3.3.x (where x probably is equal to 1).

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-19 01:34:44

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 01:34:44

Merged in Sage 3.3.alpha0
