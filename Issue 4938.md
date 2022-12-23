# Issue 4938: Words.count() returns a Python int instead of a Sage Integer

Issue created by migration from https://trac.sagemath.org/ticket/4938

Original creator: saliola

Original creation time: 2009-01-04 19:55:25

Assignee: saliola

CC:  sage-combinat

Keywords: sage-words


```
Hi guys,

I sat around and was looking at the new ReST Words documentation and
noticed the following:

[5:40pm] mabs: WTF:
[5:40pm] mabs: sage: Words(7,13).count()
[5:40pm] mabs: 96889010407L              # 32-bit
[5:40pm] mabs: 96889010407                # 64-bit
[5:40pm] mabs: So Words().count() returns a Python int?
[5:40pm] wstein: ick
[5:40pm] wstein: That stupid L at theend was suck an annoying decision by Guido.

I would expect that count() returns a Sage Integer since that seems to
be the expected result in general. If you agree please open a ticket,
but this is not a high priority issue for me.

Cheers,

Michael
```



---

Comment by hivert created at 2009-04-02 09:14:36

The problem should be fixed with #5308. So you can close it as a duplicate.

Cheers,

Florent


---

Comment by mabshoff created at 2009-04-05 00:07:16

This ticket can be closed once #5308 is merged.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-05 23:54:40

Resolution: fixed


---

Comment by mabshoff created at 2009-04-05 23:54:40

Fixed in Sage 3.4.1.rc1 via #5308.

Cheers,

Michael
