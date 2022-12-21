# Issue 1911: [with patch; needs review] elliptic curves -- make heegner_index command return index instead of square of index; clarify why sometimes results is not an integer (it's not a bug, it's part of the algorithm)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-24 15:18:51

Assignee: was




---

Attachment

Looks good to me, except for a very minor point: you changed the description of the output from "an interval that contains the index" to "an Integer", but the function is indeed returning an interval, not an integer.


---

Comment by craigcitro created at 2008-01-26 09:48:27

Several comments, but positive review with the additional patch:

- I've gone ahead and corrected the typo Alex pointed out, and a few more to boot. 

- There was a small problem with the patch -- there were one or two places that IR(...) was used, but IR was only defined in one of the functions there. I went ahead and moved that definition to the top, so that it worked everywhere, and added doctests to catch that in the future. I also made sure that every function in ell_rational_field that had the word "heegner" in it had at least one doctest.

- I changed the satisfies_heegner_hypothesis method to use legendre symbols instead of factoring in a quadratic extension of QQ, since that was overkill. This gives something like a 10X speedup to that one little function, which is probably completely irrelevant compared to the runtime for the rest of the code that actually uses it. There's the argument that the other method works over any base -- first, since this is in ell_rational_field, that shouldn't matter, and second, since the QuadraticField(...) was hardcoded to be over QQ, this code would need revisited anyway.

- Also corrected a silly typo I found in integer.pyx, which I just happened to notice while looking at code for this patch. I didn't think "returs -> returns" merited its own ticket.

- There's one thing that leaves me feeling a little unsettled -- E.heegner_index_bound() defaults to verbose=True. Given that William and his coauthors are the only people actively using this code, it's fine to leave it that way if it's the behavior they're used to. However, it's pretty shocking when you're not prepared for it; for something with that much output, I'd argue that verbose=False should be the default.

-cc


---

Attachment

Merged in Sage 2.10.1.rc0


---

Comment by mabshoff created at 2008-01-26 11:21:14

Resolution: fixed
