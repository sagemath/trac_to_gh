# Issue 1206: doc testing support for numerical computations with randomish output is insufficient

Issue created by migration from https://trac.sagemath.org/ticket/1206

Original creator: jkantor

Original creation time: 2007-11-19 06:42:59

Assignee: failure

The current way in which doc tests of numerical computations that produce randomish output are performed is not sufficient to actually detect regressions. 

Currently if the word #random follows the test, it is run but the output is not compared, this only tests that there was no failure doing something but not that what was computed was in any way correct or what was expected.

For computations with randomish output, what should be checked is that the difference between all the floating values in what is computed and in the doc string are less than some bound 1e-8 or something, or maybe the bound should be specified, so that

#random 1e-8 would check that the the computation differs from the output in the doc string by 1e-8.

  


---

Comment by mabshoff created at 2007-11-19 08:41:13

We have the "12.123.." notation to indicate that the last n, in this case 2 decimals are affected by numerical precision issues. Shouldn't that work for you, too?

Cheers,

Michael


---

Comment by jkantor created at 2007-11-21 21:08:37

That should be sufficient, it doesn't seem to be documented in the programming guide, though I may have just missed it.


---

Comment by mabshoff created at 2007-11-28 22:44:51

Ok, since was doubted that the following case could happen:

```
Expected:
    1.0000000000000000
Got:
    0.9999999999999999
```

here a real world example from 2.8.14 on Solaris:

```
File "complex_double.pyx", line 1496:
    sage: z^2 - z + 1
Expected:
    2.22044604925e-16 + 1.11022302463e-16*I
Got:
    2.22044604925e-16 + 2.22044604925e-16*I
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-04 14:39:09

Actually, the case

```
Expected:
    1.0000000000000000
Got:
    0.9999999999999999
```

Did happen a couple times in the 2.8.15 release cycle. The usual approach was to change the doctest to avoid results where such small rounding issues would cause `"..."` the doctest to be useless.

Cheers,

Michael


---

Comment by mhansen created at 2007-12-06 04:49:54

I believe implementing this would require a major restructuring of how doctesting is carried out.


---

Comment by AlexGhitza created at 2009-01-22 18:24:22

Changing type from defect to enhancement.


---

Comment by mderickx created at 2011-08-24 01:44:32

Changing status from new to needs_review.


---

Comment by mderickx created at 2011-08-24 01:44:32

There is a patch up for the same problem at #10952


---

Comment by kini created at 2012-05-16 14:12:40

Changing status from needs_review to positive_review.


---

Comment by kini created at 2012-05-16 14:12:40

Setting this to positive_review so the release manager will see it.


---

Comment by jdemeyer created at 2012-05-21 08:03:41

Resolution: duplicate
