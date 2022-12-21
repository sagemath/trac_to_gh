# Issue 3389: CartesianProduct infinite sequences

Issue created by migration from Trac.

Original creator: PolyBoRi

Original creation time: 2008-06-10 10:15:49

Assignee: mhansen

CC:  sage-combinat

Hi!

The Cartesian Product iterator of infinite sequences doesn't enumerate the
every element in the product.

I tried:

for t in CartesianProduct(QQ,ZZ):

....:     print t

....:     

[0, 0]

[0, 1]

[0, -1]

[0, 2]


This is equivalent to nest for loops, which won't work.
You have to enumerate the set in a different way.

See 
http://en.wikipedia.org/wiki/Recursively_enumerable
http://en.wikipedia.org/wiki/Cantor_pairing_function

Best regards,
Michael


---

Comment by mhansen created at 2008-06-10 10:24:28

How often does one want to iterate through a CartesianProduct of infinite things?  Is the speed tradeoff for implementing the general solution worth it?


---

Comment by PolyBoRi created at 2008-06-10 10:32:49

I would try checking via
len
if the sequence might be finite (of course, there are finite sequence, where len doesn't work).
If you know, that the sequences are finite, you can return an naive iterator.


---

Comment by mhansen created at 2008-06-10 10:44:46

Sure, but I still feel a bit like I'd be writing a bunch of useless code in the end.  I'd be more apt to rename CartesianProduct to CartesianProductOfFiniteSets or something like that.


---

Comment by mhansen created at 2008-06-10 18:01:28

Changing status from new to assigned.


---

Comment by mhansen created at 2008-06-10 18:01:28

So... it looks like I already have some code that does something similar in http://trac.sagemath.org/sage_trac/attachment/ticket/1448/1448-2.patch .  The question then becomes whether to cache the elements as you iterate over them or reiterate to them each time you need them.  Also, there are many things finite things whose cartesian product I want to iterate over for which len() takes a nontrivial amount of time.


---

Comment by PolyBoRi created at 2008-06-12 09:08:11

I don't think, this could give acceptable performance without caching in a similar way as in the code for the matrix spaces.
