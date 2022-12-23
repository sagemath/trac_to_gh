# Issue 8954: Implementation of the affine nilTemperley Lieb algebra of type A

Issue created by migration from https://trac.sagemath.org/ticket/8954

Original creator: aschilling

Original creation time: 2010-05-12 06:52:47

Assignee: AlexGhitza

CC:  sage-combinat




---

Comment by aschilling created at 2010-05-13 00:32:26

Changing status from new to needs_review.


---

Comment by jbandlow created at 2010-05-13 19:53:12

Changing status from needs_review to needs_work.


---

Comment by jbandlow created at 2010-05-13 19:53:12

Hi Anne, here are some comments.  I think all of these should be easy to implement, and I'm happy to do them myself, if you like.  But I'd like to know what you think first.

  1. It looks like your implementation assumes ZZ as a base ring.  Any reason not to allow any ring?
  2. I would prefer the elements print as `a[0] a[1]` instead of `a0 a1` so that copy-paste can work.  Do you have a preference one way or the other?
  3. In the documentation for the class, you should mention that the relations should be understood mod n.
  4. In the _element_constructor, I would expect the presence of a braid relation trigger to return 0.  Is there a reason that you raise an error instead?

This will be useful to have in sage... thanks!


---

Comment by aschilling created at 2010-05-14 17:50:29

Hi Jason,

Thank you for your comments! I have uploaded a revised patch addressing the issues you raised:

>   1. It looks like your implementation assumes ZZ as a base ring.  Any reason not to allow any ring?

Done.

>   2. I would prefer the elements print as `a[0] a[1]` instead of `a0 a1` so that copy-paste can work.  Do you have a preference one way or the other?

There is now an option in 

    def _repr_term(self, t, display = "short"):

which allows to display the output in the long or short notation.

>   3. In the documentation for the class, you should mention that the relations should be understood mod n.

Done.

>   4. In the _element_constructor, I would expect the presence of a braid relation trigger to return 0.  Is there a reason that you raise an error instead?

Done now. As we discussed by e-mail in private, it might make more sense to eventually construct this algebra as a quotient algebra. This would depend on the 'functorial constructions' patch of Nicolas and Florent. I left a note about this in the code.

One slight warning: I now inserted a line

        assert(self(w) != self.zero())

in product_on_basis, which might slow down calculations, but is safer.

Cheers,

Anne


---

Comment by aschilling created at 2010-05-14 17:50:29

Changing status from needs_work to needs_review.


---

Comment by jbandlow created at 2010-05-21 14:06:40

Changing status from needs_review to positive_review.


---

Attachment

Anne,

Thanks for making the changes I suggested.  I'm happy with the code now, and I've run the tests on sage-4.4.2 and they all pass. Positive review!


---

Comment by mhansen created at 2010-06-06 01:13:11

Resolution: fixed
