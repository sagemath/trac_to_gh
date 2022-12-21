# Issue 4730: magma/sage -- conversion of finite field elements back and forth

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-06 23:16:45

Assignee: was

Make this work:

```
sage: k.<a> = GF(2^16)
sage: magma(a).sage()
boom
```


Also, explain this fun behavior of magma where finite fields are represented differently depending on their size, as discussed in irc here:

```
15:03 < ncalexan> I get this:
15:03 < ncalexan> sage: magma(GF(5^2, 'a')['x'].random_element())
15:03 < ncalexan> a^22*x + a^9
15:04 < ncalexan> And a should have order at most 2.
15:04 < ncalexan> (exactly 2)
15:04 < wstein> why?
15:04 < wstein> Why do you think that about a?
15:04 < wstein> ehh?
15:04 < ncalexan> It's a generator of GF(5^2).
15:05 < wstein> seria-mau -- if you wat long enough I can do it.
15:05 < ncalexan> It satisfies a polynomial of degree 2.
15:05 < wstein> My virtual machine was off.
15:05 < wstein> The order of a is 24:
15:05 < wstein> sage: GF(5^2,'a').0.multiplicative_order()
15:05 < wstein> 24
15:06 -!- Irssi: Pasting 7 lines to #sage-devel. Press Ctrl-K if you wish to do this or Ctrl-C to cancel.
15:06 < wstein> sage: k.<a> = GF(25)
15:06 < wstein> sage: magma(a)
15:06 < wstein> a
15:06 < wstein> sage: a^22
15:06 < wstein> a + 1
15:06 < wstein> sage: magma(a+1)
15:06 < wstein> a^22
15:06 < wstein> Magma represents finite field elements differently in some cases.
15:06 < ncalexan> Ah, I see, magma represents them totally differently.
15:06 < ncalexan> I had no idea.
15:06 < wstein> It's the sort of inconsistency that wouldn't fly among sage devs.
15:06 < wstein> We would shoot that down in a second.
15:06 < ncalexan> What do they do for huge fields/
15:06 < wstein> I think it only use that representation for small fields...
15:06 < wstein> maybe I'm wrong.
15:06 < ncalexan> You can't take dlogs everywhere.
15:07 < wstein> for big fields they don't use that representation:
15:07 < ncalexan> Okay, could you fix and apply my doctests (I think they're useful) and maybe add a line explaining the surprising representation differences/
15:07 < wstein> sage: magma.eval('FiniteField(997^2).1^1000')
15:07 < wstein> '94*$.1 + 597'
15:07 < ncalexan> That's so arbitrary.
```


Basically the above should be explained by some doctests.


---

Comment by was created at 2008-12-06 23:17:23

Fixing this requires adding a Sage(...) for univariate polynomials to the basic.m file.  Nick Alexander has this...


---

Comment by was created at 2008-12-06 23:18:23

See also the "referee patch" from #4701, which could go somehow with this ticket.


---

Attachment


---

Comment by was created at 2008-12-11 04:33:34

This didn't work because in Magma 2.13 one must do Polynomial(Eltseq(a)) rather than just Polynomial(a).  I fixed this.  I also added some doctests.


---

Attachment

Patch looks good to me and doctests pass. trac_4730-doc.patch fixes a slight problem with a Magma doctest in the documentation, so I am CCing Mike Hansen.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-13 11:27:00

Merged all three patches in Sage 3.2.2.alpha2


---

Comment by mabshoff created at 2008-12-13 11:27:00

Resolution: fixed
