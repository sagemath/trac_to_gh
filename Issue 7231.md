# Issue 7231: cryptanalysis of the Vigenere cipher

Issue created by migration from https://trac.sagemath.org/ticket/7231

Original creator: mvngu

Original creation time: 2009-10-16 00:52:35

Assignee: somebody

CC:  rbeezer rws

Keywords: Vigenere cipher, cryptanalysis

As the subject says. This depends on #7124.


---

Comment by @DaveWitteMorris created at 2022-04-03 20:47:56

A method could be added to the `VigenereCryptosystem` class in `src/sage/crypto/classical.py`. I would suggest calling the method something like `cryptanalyze`. If more than one method of cryptanalysis is implemented, then I would suggest providing an `algorithm` keyword argument, so the user can choose between them.

Follow-up ticket: The `AffineCryptosystem` and `ShiftCryptosystem` classes have methods `rank_by_chi_square`, `rank_by_squared_differences`, and `brute_force`. I would suggest making them all available from a single `cryptanalyze` method (with `algorithm` keyword argument) so they are easier to find.
