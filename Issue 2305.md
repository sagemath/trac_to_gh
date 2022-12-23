# Issue 2305: Docstrings and doctests for rings/ideal.py

Issue created by migration from https://trac.sagemath.org/ticket/2305

Original creator: cswiercz

Original creation time: 2008-02-25 21:48:54

Assignee: cswiercz

Keywords: docstring, doctest

Provide missing docstrings and doctests for all non-"_" functions in rings/ideal.py. These include:

id_Ideal(x)
base_ring(self)
is_maximal(self)
is_prime(self)
is_principal(self)
is_principal(self)
gen(self)
gcd(self, other)


---

Attachment

Remaining docstrings and doctetst for rings/ideal.py


---

Comment by cswiercz created at 2008-02-27 23:40:14

Changing status from new to assigned.


---

Comment by ncalexan created at 2008-02-28 20:18:28

The patch is mostly fine, but there are some formatting issues.

This looks wrong:

```
 	155	        sage: R = ZZ
 	156	        sage: R; is_Ideal(R) 
 	157	        Integer Ring 
 	158	        False 
```


Please typeset sage's output all on one line.  So rather than


```
 	168	        sage: I = R.ideal(x^2 + 1); I 
 	169	        Principal ideal (x^2 + 1) of Univariate Polynomial Ring in x over 
 	170	        Rational Field 
```


give me


```
 	168	        sage: I = R.ideal(x^2 + 1); I 
 	169	        Principal ideal (x^2 + 1) of Univariate Polynomial Ring in x over Rational Field 
```


Also, there are *tons* of typos.  'th' instead of 'the', incorrectly spelled words, etc.  I will work on some emacs code that will spell-check only sage comments, and ignore examples as appropriate, but until then you'll have to do it by hand :)


---

Attachment

Corrected docstring and doctest patch for rings/ideal.py


---

Comment by cswiercz created at 2008-02-28 23:20:45

Accidentally renamed the patch. Be sure to review rings.ideal.patch and ignore ring.ideal.patch. Thanks!


---

Comment by dfdeshom created at 2008-03-06 04:01:02

Doctest-formatting looks good and typos are out. So I say apply!


---

Comment by mabshoff created at 2008-03-07 20:09:40

Merged rings.ideal.patch in 2.10.3.rc3. The patch does add a single docstring in numerical/optimize.py, so I am not quite sure if that was intended for this patch.


---

Comment by mabshoff created at 2008-03-07 20:09:40

Resolution: fixed


---

Comment by malb created at 2008-03-07 20:25:04

Sorry for being late to the party, but please open another ticket to address the following minor issues:
 * `def ring` the docstring uses backslashes but is not treated raw: `r"""` missing
 * "Note that \code{self.ring()} is different from \code{self.ring()}" seems like a typo
