# Issue 9451: [with patch, needs work] sieve of atkin

Issue created by migration from https://trac.sagemath.org/ticket/9451

Original creator: ohanar

Original creation time: 2010-07-08 01:31:21

Assignee: was

CC:  was kevin.stueve robertwb

Keywords: prime, sieve, range

The goal of this ticket is to efficiently implement the sieve of atkin. This first version is a step in that direction.

Paper on the sieve can be found at http://bit.ly/sieveatkin

Due to the length of the implementation, I moved `prime_range` from `fast_arith` into a new module.

The current implementation uses 64-bit ints and hits that barrier at input around `2**56`, so I've capped it at `2**52` (in the future I plan to remove this limitation).

I've changed the default algorithm to atkins, since it is nearly as fast as the pari table, but doesn't use as much storage so it is more viable for large input.

Docstrings are incomplete.


---

Attachment

based on 4.4.4


---

Comment by mhansen created at 2010-07-08 06:28:06

A couple quick things without really looking at the content of the patch:

1) You should probably import prime_range into fast_arith for backward compatibility.

2) You don't need backslashes to continue lines when they're in brackets.

3) You should make the default algorithm `None` and choose it inside of the function.  That way it can choose a different algorithm if the input is outside of the range of atkins.
