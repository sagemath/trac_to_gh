# Issue 2312: add support for braclets, necklaces, and Lyndon words, of a fixed length

Issue created by migration from https://trac.sagemath.org/ticket/2312

Original creator: mhansen

Original creation time: 2008-02-26 05:02:36

Assignee: mhansen

CC:  sage-combinat




---

Comment by mabshoff created at 2008-08-13 08:05:54

Hi Mike,

this has also been open for a while. I assume that combinat/lyndon_word.py contains the Lyndon words for example.

Cheers,

Michael


---

Comment by sage-combinat created at 2009-08-01 14:00:19

This is just a test to see if the temporary sage-combinat-commits-bis receives the trac e-mails. Please ignore.


---

Comment by nthiery created at 2009-08-01 14:31:39

And a second one, not as sage-combinat user.


---

Comment by slelievre created at 2019-01-14 19:11:29

Could you indicate if anything is still needed in that respect?

SageMath documentation

- [Words](http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/enumerated_sets.html#words)
  - [necklace](http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/necklace.html)
  - [Lyndon word](http://doc.sagemath.org/html/en/reference/combinat/sage/combinat/lyndon_word.html)

SageMath sources

- [bracelets, necklaces](https://github.com/sagemath/sage/blob/master/src/sage/combinat/necklace.py)
- [Lyndon word](https://github.com/sagemath/sage/blob/master/src/sage/combinat/lyndon_word.py)

Related tickets

- #26111: Implement faster iterator for Lyndon words
- #11386: Add a bracelet combinatorial class
