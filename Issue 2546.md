# Issue 2546: vectors over SR should be callable? over function rings?

Issue created by migration from Trac.

Original creator: edrex

Original creation time: 2008-03-16 16:42:12

Assignee: was

Keywords: function rings vectors

Elements of SR are "callable", perhaps vectors over SR should be too, which wouldallows symbolic vectors to act as vector-valued mappings from R<sup>m</sup> -> R<sup>n</sup>.

Now that I think about it, I don't know if it really makes sense for SR elts to be callable, since how does one define order of arguments (or arguments period for that matter)? The problem gets worse if you are talking about a vector with SR coefficients.

I actually like the symbolic function ring syntax/construction much better since it makes the mapping explicit (if a mapping is what you want to represent), but these seem to be less well-supported (for example, ` _f(x,y)=x<sup>2+y</sup>2; g(x,y)=1;vector((f,g)) ` yields a NotImplementedError ) and are definitely less common in doctest examples. I think a vector over a particular symbolic function ring  (say the one from (x,y,z)) would be a particularly useful mathematical object. vector((x1, x2, ..., xn)) could give an error (NotImplemented or just NotAGoodIdea). Then the resulting vector would be a clear mapping from R<sup>m</sup> to R<sup>n</sup>, with a well-defined argument order. 


---

Comment by gfurnish created at 2008-03-16 20:09:08

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-03-16 20:09:08

Changing assignee from was to gfurnish.


---

Comment by was created at 2008-03-16 20:48:42

Invalid.  This is the sort of thing that needs to be discussed on sage-support or sage-devel.  If a VERY CLEAR task emerges, then that goes into trac.


---

Comment by was created at 2008-03-16 20:48:42

Resolution: invalid


---

Comment by jason created at 2009-02-13 17:44:22

See also #2549 for a related ticket.
