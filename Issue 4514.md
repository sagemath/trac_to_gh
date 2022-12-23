# Issue 4514: Equality test fails for element coerced back into GL(2,7)

Issue created by migration from https://trac.sagemath.org/ticket/4514

Original creator: saliola

Original creation time: 2008-11-13 17:20:00

Assignee: tbd

The element below is constructed as an element of GL(2,7), but when converted into an element in GL(2,7) it is not equal to itself.

```
sage: G = GL(2,7)
sage: z = G.center().an_element()
sage: z
[3 0]
[0 3]
sage: z in G
True
sage: G(z)
[3 0]
[0 3]
sage: G(z) == z
False
sage: G(G(z)) == G(z)
True
```



---

Comment by saliola created at 2008-11-13 17:31:51

Hmm. Maybe this isn't a bug afterall: the element z isn't really from G, but from G.center().


---

Comment by mabshoff created at 2008-11-14 05:06:55

So: let's close this as invalid?

Cheers,

Michael


---

Comment by saliola created at 2008-11-14 17:49:08

Resolution: invalid


---

Comment by saliola created at 2008-11-14 17:49:08

That's fine with me. I left it as is in case someone else might have something to say, but I think it has been long enough.
