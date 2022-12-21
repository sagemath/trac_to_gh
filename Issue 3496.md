# Issue 3496: charpoly for 0 dimensional matrices is broken/wrong most places

Issue created by migration from Trac.

Original creator: craigcitro

Original creation time: 2008-06-23 19:14:46

Assignee: craigcitro

CC:  alexghitza

This should be fixed over all kinds of rings -- it's supposed to be `0` everywhere. It's currently either broken (e.g. over `CyclotomicField`s) or wrong (e.g. it's `1` over `QQ`) in lots of places.

I'll do this soon if no one beats me to it.


---

Comment by dmharvey created at 2008-06-23 22:27:25

Sorry, why should the charpoly be zero? I would have thought it should be 1.


---

Comment by craigcitro created at 2008-06-23 22:40:17

Alright, I'm convinced. The best argument for me was that if $V = W \oplus W'$, and you have an operator on $V$, you want to be able to say things like "the charpoly on the sum is the product of the charpolys."

I still need to fix it for cyclotomic fields.


---

Comment by craigcitro created at 2008-10-23 18:56:21

Changing status from new to assigned.


---

Attachment

This patch fixes the charpoly for 0-dimensional matrices, along with a bunch of other little issues in the cyclotomic linear algebra code. This code was written during the L-functions and Modular Forms Workshop in Seattle, mostly while discussing the code with Clement Pernet.


---

Comment by mabshoff created at 2008-10-27 01:48:10

Alex,

since you are reviewing can you take a shot at this one, too?

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-10-27 05:40:36

I'm pretty happy with this, except that it would be nice to have an actual doctest showing that the original issue (charpolys for 0 dimensional matrices) now works (yes, I can see it fixed in the new code, but let's have an explicit doctest).  So positive review with this tiny proviso.

I'll add a minipatch for this the next time I get a chance (soon), unless Craig (or someone else) beats me to it.


---

Attachment


---

Comment by craigcitro created at 2008-10-27 05:52:42

Oh, good call, Alex. I've added that doctest in the second patch.


---

Comment by AlexGhitza created at 2008-10-27 06:17:00

I'm happy.


---

Comment by mabshoff created at 2008-10-28 12:18:43

Resolution: fixed


---

Comment by mabshoff created at 2008-10-28 12:18:43

Merged both patches in Sage 3.2.alpha2
