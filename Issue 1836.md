# Issue 1836: [with patch] return reduced Groebner bases by default

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-01-18 19:28:42

Assignee: malb

... to avoid ambiguousness


---

Attachment


---

Comment by ncalexan created at 2008-01-20 03:48:16

There are an awful lot of places that Groebner bases are computed.  (complete_prime_decomposition, etc).  I'd really like to guarantee that *all* such bases are reduced.  Is that unreasonable?


---

Comment by malb created at 2008-01-20 22:27:23

updated patch which uses Python techniques to implement reduction of Groebner bases, and forces all GB calculations to be reduced


---

Attachment

Replying to [comment:1 ncalexan]:
> There are an awful lot of places that Groebner bases are computed.  (complete_prime_decomposition, etc).  I'd really like to guarantee that *all* such bases are reduced.  Is that unreasonable?

The updated patch is supposed to implement that.


---

Comment by mabshoff created at 2008-01-22 00:11:33

Patch looks good to me. I think that all of Nick's concerns have been addressed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-22 00:11:59

Resolution: fixed


---

Comment by mabshoff created at 2008-01-22 00:11:59

Merged in Sage 2.10.1.alpha1
