# Issue 4250: In QQ[t], 2**t should raise an error, but it crashes

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-10-07 17:34:12

Assignee: malb

CC:  malb

Keywords: crash, polynomial ring, rationals

Of course, doing

```
sage: R.<t>=QQ[]
sage: 2**t
```

should result in a traceback. In fact it does so for `R.<t>=ZZ[]`. But over `QQ`, it crashes with a segmentation fault.

Running `sage -gdb` yields a very long output, too long to reproduce it here, and sorry that I don't know how to save the output of `bt`.

I use Sage version 3.1.2, and it occurs on two different Linux machines.


---

Comment by mabshoff created at 2008-10-26 15:47:45

Any progress here? Is anybody working on this?

Cheers,

Michael


---

Comment by burcin created at 2008-10-31 10:42:21

Changing status from new to assigned.


---

Comment by burcin created at 2008-10-31 10:42:21

The segfault is caused by an infinite loop, where 2 is cast to a polynomial and its `__pow__` method is called, and the polynomial ring calls the `__pow__` method of the base ring on constant polynomials.

attachment:trac_4250_QQx_pow_segfault.3.patch (thanks trac for screwing up the name again) fixes the issue.


---

Comment by burcin created at 2008-10-31 10:42:21

Changing assignee from malb to burcin.


---

Attachment


---

Comment by mabshoff created at 2008-10-31 14:20:32

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-31 14:20:50

Merged in Sage 3.2.alpha2


---

Comment by mabshoff created at 2008-10-31 14:20:50

Resolution: fixed
