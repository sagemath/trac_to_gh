# Issue 9463: Integer factorization should handle perfect powers efficiently

Issue created by migration from https://trac.sagemath.org/ticket/9463

Original creator: fredrik.johansson

Original creation time: 2010-07-09 09:03:28

Assignee: AlexGhitza

CC:  jdemeyer

factor() is extremely slow at factoring large perfect powers (with a nontrivial base).

```
sage: %time factor(next_prime(10^20)^150)
CPU times: user 0.75 s, sys: 0.00 s, total: 0.75 s
Wall time: 0.75 s
100000000000000000039^150
sage: %time factor(next_prime(10^20)^250)
CPU times: user 2.68 s, sys: 0.00 s, total: 2.68 s
Wall time: 2.69 s
100000000000000000039^250
sage: %time factor(next_prime(10^20)^500)
CPU times: user 13.19 s, sys: 0.00 s, total: 13.19 s
Wall time: 13.20 s
100000000000000000039^500
```

For comparison, SymPy handles such numbers in an instant:

```
sage: from sympy import factorint
sage: %time factorint(next_prime(10^20)^150)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
{100000000000000000039L: 150}
sage: %time factorint(next_prime(10^20)^250)
CPU times: user 0.01 s, sys: 0.00 s, total: 0.01 s
Wall time: 0.01 s
{100000000000000000039L: 250}
sage: %time factorint(next_prime(10^20)^500)
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
{100000000000000000039L: 500}
```

Perfect power testing is very cheap, so it should be attempted early on for large numbers.


---

Comment by jdemeyer created at 2010-07-11 08:03:07

Changing assignee from AlexGhitza to tbd.


---

Comment by jdemeyer created at 2010-07-11 08:03:07

This is because of the way PARI factors number (first trial division, then perfect power checking).  See http://pari.math.u-bordeaux.fr/cgi-bin/bugreport.cgi?bug=1074


---

Comment by jdemeyer created at 2010-07-11 08:03:07

Changing component from basic arithmetic to factorization.


---

Comment by jmantysalo created at 2016-08-20 05:51:58

Examples take milliseconds now even on old computer, so I guess this has been fixed and can be closed.


---

Comment by jmantysalo created at 2016-08-20 05:51:58

Changing status from new to needs_review.


---

Comment by bruno created at 2016-08-21 14:57:52

I agree!


---

Comment by bruno created at 2016-08-21 14:57:52

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-08-30 13:32:25

Determined to be invalid/duplicate/wontfix (closing as "wontfix" as a catch-all resolution).


---

Comment by embray created at 2016-08-30 13:32:25

Resolution: wontfix
