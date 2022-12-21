# Issue 3549: change pari (and sage) so that one can add to the list of precomputed primes that are used for trial division

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-04 04:22:14

Assignee: was

CC:  jdemeyer

This is a very very useful unique feature that magma has.  We need to change pari so it can do it to and add an interface so sage can use that function.


---

Comment by cwitty created at 2008-07-10 01:20:48

Pari can already do this; it's the "addprimes" function.


---

Comment by jdemeyer created at 2010-08-01 15:32:42

Changing component from number theory to interfaces.


---

Comment by kedlaya created at 2016-04-09 23:22:27

The `addprimes` function is currently available via automatic import:

```
sage: pari([3, 7]).addprimes()
[3 ,7]
```

If this is sufficient, then I would propose to close this ticket as invalid.

A more proactive alternative would be to add a wrapper function somewhere, maybe `sage.rings.fast_arith` where things like `prime_range` live.
