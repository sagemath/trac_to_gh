# Issue 8: Integer and Rational classes need nth_root and exact_power functions

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2006-09-12 02:39:12

Assignee: somebody

It would be useful for Integer and Rational classes to have:

(1) nth_root: this would wrap GMP's mpz_root.
(2) exact_power: would accept a *rational* number as an index, and work out which root to take. For example

(-8/27).exact_power(2/3) == 4/9

I had to take an exact 6th root of a rational in some code the other day and it was **painful** going via real numbers, worrying about bits of precision and all that.



---

Comment by dmharvey created at 2006-09-16 05:05:03

Fixed.

Fri Sep 15 17:19:10 PDT 2006  dmharvey`@`math.harvard.edu
  * Rational.nth_root() -- adds Rational nth root method

Fri Sep 15 17:18:20 PDT 2006  dmharvey`@`math.harvard.edu
  * Integer.nth_root() -- adds nth root method to Integer (wraps GMP mpz_root)


---

Comment by dmharvey created at 2006-09-16 05:05:03

Resolution: fixed
