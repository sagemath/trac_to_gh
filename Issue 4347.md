# Issue 4347: generalized bernoulli numbers -- massively optimize

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-10-23 16:25:31

Assignee: was

There is a simple algorithm to massively optimize computation of generalized bernoulli numbers.  This needs to be in Sage and replace the current stupid algorithm.


```
Already in sage for any character chi you can do

        chi.bernoulli(k)

Amusingly since the B_k (no character) are so fast, and
there is a relation between them and the B_{k,chi}, there
is a 5-line algorithm (see below) for computing B_{k,chi}
that with the worst implementation is still way faster than
Sage's built-in chi.bernoulli(k).

From page 656 of Cohen:

def S(n,chi):
 return sum(chi(r)*r^n for r in [0..chi.modulus()-1])

def bern(k,chi):
 m = chi.modulus()
 return sum([binomial(k,j) * bernoulli(j)*m^(j-1)*S(k-j,chi) for j
in [0..k]])
```



---

Attachment


---

Comment by was created at 2008-10-24 01:45:46

The attached patch massively speeds things up. For example in this example the new code is over TWO HUNDRED times faster!


```
sage: eps = DirichletGroup(9).0
sage: time s = eps.bernoulli(197, cache=False)
CPU time: 0.04 s,  Wall time: 0.04 s
sage: time s = eps.bernoulli(197, cache=False, algorithm='definition')
CPU time: 8.27 s,  Wall time: 8.50 s
sage: 8.27/0.04
206.750000000000
```



---

Comment by AlexGhitza created at 2008-10-25 22:28:27

I'm seeing doctest failures in sage/modular/ in both 3.1.4 and 3.2.alpha0, namely:


```
The following tests failed:


	sage -t  3.1.4/devel/sage-main/sage/modular/modform/eisenstein_submodule.py
	sage -t  3.1.4/devel/sage-main/sage/modular/modform/space.py
	sage -t  3.1.4/devel/sage-main/sage/modular/modform/hecke_operator_on_qexp.py
	sage -t  3.1.4/devel/sage-main/sage/modular/modform/ambient.py
	sage -t  3.1.4/devel/sage-main/sage/modular/modform/element.py
Total time for all tests: 285.7 seconds
```


For example:


```
[ghitza`@`artin sage]$ sage -t modular/modform/eisenstein_submodule.py 
sage -t  3.1.4/devel/sage-main/sage/modular/modform/eisenstein_submodule.py
**********************************************************************
File "/opt/sage/tmp/eisenstein_submodule.py", line 263:
    sage: EisensteinForms(22,4)._compute_q_expansion_basis(6)
Expected:
    [1 + O(q^6),
    q + 28*q^3 - 8*q^4 + 126*q^5 + O(q^6),
    q^2 + 9*q^4 + O(q^6),
    O(q^6)]
Got:
    [O(q^6), O(q^6), O(q^6), O(q^6)]
**********************************************************************
File "/opt/sage/tmp/eisenstein_submodule.py", line 268:
    sage: EisensteinForms(22,4)._compute_q_expansion_basis(15)
Expected:
    [1 + O(q^15),
    q + 28*q^3 - 8*q^4 + 126*q^5 + 344*q^7 - 72*q^8 + 757*q^9 - 224*q^12 + 2198*q^13 + O(q^15),
    q^2 + 9*q^4 + 28*q^6 + 73*q^8 + 126*q^10 + 252*q^12 + 344*q^14 + O(q^15),
    q^11 + O(q^15)]
Got:
    [O(q^15), O(q^15), O(q^15), O(q^15)]
**********************************************************************
File "/opt/sage/tmp/eisenstein_submodule.py", line 310:
    sage: (11*E.0 + 3*E.1).q_expansion(20)
Expected:
    11 + 3*q + 27*q^2 + 84*q^3 + 219*q^4 + 378*q^5 + 756*q^6 + 1032*q^7 + 1755*q^8 + 2271*q^9 + 3402*q^10 + 3996*q^11 + 6132*q^12 + 6594*q^13 + 9288*q^14 + 10584*q^15 + 14043*q^16 + 17379*q^17 + 20439*q^18 + 20580*q^19 + O(q^20)
Got:
    O(q^20)
**********************************************************************
File "/opt/sage/tmp/eisenstein_submodule.py", line 312:
    sage: E._q_expansion([0,0,0,0,11,3],20)
Expected:
    11 + 3*q + 27*q^2 + 84*q^3 + 219*q^4 + 378*q^5 + 756*q^6 + 1032*q^7 + 1755*q^8 + 2271*q^9 + 3402*q^10 + 3996*q^11 + 6132*q^12 + 6594*q^13 + 9288*q^14 + 10584*q^15 + 14043*q^16 + 17379*q^17 + 20439*q^18 + 20580*q^19 + O(q^20)
Got:
    O(q^20)
**********************************************************************
File "/opt/sage/tmp/eisenstein_submodule.py", line 205:
    sage: EisensteinForms(1,4).eisenstein_series()
Expected:
    [
    1/240 + q + 9*q^2 + 28*q^3 + 73*q^4 + 126*q^5 + O(q^6)
    ]
Got:
    [
    O(q^6)
    ]
**********************************************************************
File "/opt/sage/tmp/eisenstein_submodule.py", line 209:
    sage: EisensteinForms(1,24).eisenstein_series()
Expected:
    [
    236364091/131040 + q + 8388609*q^2 + 94143178828*q^3 + 70368752566273*q^4 + 11920928955078126*q^5 + O(q^6)
    ]
Got:
    [
    O(q^6)
    ]
**********************************************************************
File "/opt/sage/tmp/eisenstein_submodule.py", line 213:
    sage: EisensteinForms(5,4).eisenstein_series()
Expected:
    [
    1/240 + q + 9*q^2 + 28*q^3 + 73*q^4 + 126*q^5 + O(q^6),
    1/240 + q^5 + O(q^6)
    ]
Got:
    [
    O(q^6),
    O(q^6)
    ]
**********************************************************************
3 items had failures:
   2 of   4 in __main__.example_10
   2 of   5 in __main__.example_11
   3 of  14 in __main__.example_9
***Test Failed*** 7 failures.
For whitespace errors, see the file /opt/sage/tmp/.doctest_eisenstein_submodule.py
	 [3.9 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  3.1.4/devel/sage-main/sage/modular/modform/eisenstein_submodule.py
Total time for all tests: 3.9 seconds
```



---

Comment by was created at 2008-10-26 23:16:36

There was a bug in the modulus 1 case, which those doctests fortunately caught.  The second patch attached to this ticket fixes that.  Now all the doctests pass.


---

Attachment


---

Comment by AlexGhitza created at 2008-10-27 00:57:43

Great stuff!


---

Comment by mabshoff created at 2008-10-27 01:41:01

Resolution: fixed


---

Comment by mabshoff created at 2008-10-27 01:41:01

Merged both patches in Sage 3.2.alpha1
