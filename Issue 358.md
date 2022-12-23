# Issue 358: padic_height_pairing_matrix computes too many heights

Issue created by migration from https://trac.sagemath.org/ticket/358

Original creator: dmharvey

Original creation time: 2007-04-25 22:39:16

Assignee: was

The function `padic_height_pairing_matrix()` is a bit lazy. It should do less work along the diagonal. e.g. for rank 2, if the generators are P and Q, it computes h(P), h(Q), h(P+Q), h(P+P), h(Q+Q). Clearly the last two are silly.



---

Attachment

Done.  Patch based on 3.0.alpha1


---

Comment by dmharvey created at 2008-04-06 15:35:19

Actually, it looks like someone has already fixed this ticket a while ago. John, I don't think your patch actually does anything significantly different, it just looks like a code rearrangement? (Although I do prefer the way you have written it to what was there before.)


---

Comment by cremona created at 2008-04-06 16:32:41

Replying to [comment:4 dmharvey]:
> Actually, it looks like someone has already fixed this ticket a while ago. John, I don't think your patch actually does anything significantly different, it just looks like a code rearrangement? (Although I do prefer the way you have written it to what was there before.)

OK, you are right.  I thought it was pointless to store the heights in a separate array and then put them in the matrix diagonal later.  So you can decide whether or not this patch should get used, and either way the ticket can be closed!


---

Comment by dmharvey created at 2008-04-06 16:39:19

I agree. Passes tests for me, so let's merge it.


---

Comment by mabshoff created at 2008-04-06 17:06:15

Merged in Sage 3.0.alpha2


---

Comment by mabshoff created at 2008-04-06 17:06:15

Resolution: fixed
