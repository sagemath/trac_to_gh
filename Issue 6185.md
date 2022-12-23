# Issue 6185: [with patch, needs review] Add SBox -> CNF Conversion

Issue created by migration from https://trac.sagemath.org/ticket/6185

Original creator: malb

Original creation time: 2009-06-02 13:56:38

Assignee: malb

CC:  mvngu rpw burcin

Keywords: crypto, cnf

While not really complicated it is nice to have a direct conversion from S-Boxes to CNF since SAT-solves enjoy some attention right now in crypto.


---

Comment by malb created at 2009-06-02 13:57:34

Minh, can I ask you to review this ticket?


---

Comment by mvngu created at 2009-06-03 19:13:19

Replying to [comment:1 malb]:
> Minh, can I ask you to review this ticket?
Hi Martin. Sorry for my simple question: Is there a reference or paper that describes the algorithm you use for converting an S-box to CNF? I only know about the application of SAT to cryptanalysis by reading this ticket. I usually find it much easier to understand code if I can access a reference somewhere that describes the algorithm.


---

Comment by malb created at 2009-06-03 22:17:22

Hi Minh,

the standard reference for SAT-solvers in block cipher cryptanalysis is:

   http://eprint.iacr.org/2007/024

I've implemented a converter along those lines at

   http://bitbucket.org/malb/algebraic_attacks/src/tip/anf2cnf.py

which isn't ready for inclusion yet. This ticket follows a different approach and converts the S-Box directly. The algorithm used is the standard algorithm for computing CNF from a truth table, 

   cf. `sage.sage.logic.boolformula`


---

Comment by malb created at 2009-06-08 10:53:32

Hi Burcin, Ralf,

can I ask for this (hopefully) easy review?


---

Comment by ylchapuy created at 2009-06-11 07:42:19

My 2 cents:

* the complexity is 'n * 2**m' (instead of 'm * 2**n'):

```
  for x in X:                        <-- 2^m
      for output_bit in output_bits: <-- n
```

* typos:
   * line 866: evaluate instead of evaulate
   * line 840: endianness instead of endianess

* maybe add an exception if xi or yi has wrong size

* maybe (but as you like) construct x's on the fly:

```
  for e in xrange(2**m):
      x = self.to_bits(e)
```

otherwise seems good to me.


---

Attachment

The attached updated patch addresses the reviewer's comments. Is that a positive review then?


---

Comment by ylchapuy created at 2009-06-11 13:43:17

Yes it is. Positive review.


---

Comment by ncalexan created at 2009-06-13 20:43:33

Resolution: fixed
