# Issue 7492: Decomposition of a doubly stochastic matrix as a convex sum of permutations

Issue created by migration from https://trac.sagemath.org/ticket/7492

Original creator: ncohen

Original creation time: 2009-11-19 09:50:11

Assignee: mhansen

As the title says, there is a theorem saying that any doubly stochastic matrix ( http://en.wikipedia.org/wiki/Doubly_stochastic_matrix ) can be written as a convex sum of permutations.

A proof and an algorithm can be found in this book : http://www.thi.informatik.uni-frankfurt.de/~jukna/EC_Book/

Nathann


---

Comment by ncohen created at 2009-11-20 09:27:28

Changing status from new to needs_review.


---

Comment by mhansen created at 2009-12-27 18:42:22

Changing status from needs_review to needs_work.


---

Comment by mhansen created at 2009-12-27 18:42:22

This patch needs to be updated as there is no max_matching method for graphs.


---

Comment by ncohen created at 2009-12-27 19:28:08

Changing status from needs_work to needs_review.


---

Comment by davidloeffler created at 2010-05-17 10:45:13

Changing status from needs_review to needs_work.


---

Comment by davidloeffler created at 2010-05-17 10:45:13

Needs work, I'm afraid.

- Firstly, there are no checks on the input type. It will happily accept non-doubly-stochastic matrices, and return garbage; and it seems to silently replace real numbers with rational approximations to them, which is frankly rather weird. The docstring should state clearly what base rings are allowed (integers? rationals? reals?) and there should be a check to make sure that the input matrix really is a doubly stochastic matrix over one of these base rings.

- The doctests won't work without an optional spkg, so they should be flagged as such.

- Non-ASCII character in the docstring (it reads as "Birkhoff[a-with-circumflex][empty-square-box][empty-square-box]von Neumann" on my system)

- There's not a lot of point in adding functions when there's no obvious way of calling them from the command line. Either this should be imported in an all.py somewhere, or (much preferably) there should be a method of one of the matrix classes that calls it.


---

Comment by davidloeffler created at 2010-05-17 11:02:40

Replying to [comment:7 davidloeffler]:
> and it seems to silently replace real numbers with rational approximations to them, which is frankly rather weird. 

Sorry, that was a mistake in my test script, not in your code. But I still think that the code should do some sanity checks on its input.


---

Comment by ncohen created at 2010-05-17 17:27:40

Hello !!

This patch needed to be updated anyway, as it was veeeeery old and many things changed since. I will gladly add a chechking that the matrix is indeed bistochastic if you think it necessary (though I like to think of functions doing just what they are meant to, and not spend too much time checking the user is not doing anything wrong). It is not very long anyway :-)

   * Considering how the algorithm works, it does not really care about the base ring. Anyone will work (well, as long as it is completely ordered !), so Reals, Integers, Rationals are all ok. How would you like this to be mentionned ? I never use these types, and I do not know at all how it is usually done.

   * The doctests *needed* an optional package. With #8166, they don't anymore, and I will update the patch in consequence :-)

   * Sorry about the non-ASCII character !!

   * Another place where I wouldn't know how to do otherwise. There are some graph functions which are not method of the Graph object, just because they are too specific to be, and the users can find out about them by reading the reference manual, or the correct module. If it is not the custom in this part of Sage, where would you like to see it ? I have to admit I have no clue... :-)

Thank you for your help !!

Nathann


---

Comment by ncohen created at 2010-05-17 17:27:40

Changing status from needs_work to needs_info.


---

Comment by davidloeffler created at 2010-05-17 18:34:34

I think the standard practice is to have an optional argument "check", which defaults to True but can be set to False if you know your input is valid and you don't want to waste time checking.

Rather than having an explicit list of allowable base rings, I suggest checking that the base ring has a canonical coercion map to RR.

Maybe you could put in a method under (perhaps) sage.matrix.matrix2 that calls this, and cross-reference between the two docstrings.

David


---

Comment by ncohen created at 2010-05-17 20:15:01

Well, it took me some time but.... Would this patch suit your taste ? :-)

Nathann


---

Comment by ncohen created at 2010-05-17 20:15:01

Changing status from needs_info to needs_review.


---

Attachment


---

Attachment

apply over previous patch


---

Comment by davidloeffler created at 2010-05-18 13:55:27

Excellent! I only have one minor suggestion: I think it's also worth checking that the matrix has nonnegative entries. I've added a reviewer patch that makes this change, and also adds a couple more doctests. I'm happy with the code now, modulo these changes; so if you (or anyone else who happens to be reading this) could double-check my second patch, then we can call this a positive review.


---

Comment by ncohen created at 2010-05-18 21:35:03

Thank you for your corrections ! It introduces no docstring error, is nicely applied, etc... Positive review to your changes, and hence to this whole ticket. It still depends on two other tickets waiting for review, though  (#8364 and #8166) :-)

Nathann


---

Comment by ncohen created at 2010-05-18 21:35:03

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-05-18 21:53:23

(if you have a few seconds for them, by the way ^^; ... they are very simple and require absolutely no knowledge of graph theory -- #8364 just adds arguments to graph functions that are immediately forwarded to a sub-function, and #8166 merges two functions which were doing the same thing in different ways ) :-)

Nathann


---

Comment by mhansen created at 2010-06-05 22:41:10

Resolution: fixed


---

Comment by mhansen created at 2010-06-05 22:41:10

Some of doctests had to be marked as optional as they required a linear programming solver.


---

Comment by mhansen created at 2010-06-06 00:42:41

I somehow missed the dependence on #8166.  I've removed the optional markings from the doctests in this patch.
