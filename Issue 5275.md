# Issue 5275: One-by-one declaration of morphisms to the coercion mechanism

Issue created by migration from https://trac.sagemath.org/ticket/5275

Original creator: nthiery

Original creation time: 2009-02-14 18:16:50

Assignee: robertwb

Would it be possible to add the following functionality (with whatever
appropriate syntax):

	declare_conversion(source, target, morphism)

which would add the morphism from source to target to the conversion
list (and probably similarly for coercions). Having some restrictions
on it (like making sure it's called before any coercion/conversion is
attempted) is no problem.

This functionality will make it possible for each category to
automatically declare the relevant morphisms, independently of the other
categories (like if A is in Algebras(K), then this category will
declare the morphism from K to A).

Thanks in advance!
					Nicolas


---

Comment by nthiery created at 2009-02-14 18:17:28

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2009-02-14 20:19:55

Nicolas,

if you have a wish and you ask whether it is possible or not to do you should wait for the answer before opening a ticket. In that case you should also assign it to the wishlist milestone unless someone tells you that he is working on it.

Obviously is you are a nice guy and you meant "I would like the following to be implemented" then opening the ticket is ok :)

Cheers,

Michael


---

Comment by robertwb created at 2009-02-14 23:42:15

This is certainly possible (I bet I could do it rather quickly). 

Discussion at http://groups.google.com/group/sage-devel/browse_thread/thread/7136f15aab6f6644?hl=en
