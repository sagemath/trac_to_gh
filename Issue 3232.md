# Issue 3232: wrap NTL's BKZ

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-05-16 23:18:54

Assignee: was

The BKZ algorithm is a lattice reduction algorithm AFAIK only implemented in NTL. 


```
  -- BKZ: Block Korkin-Zolotarev reduction.
     This is slower, but yields a higher-quality basis,
     i.e., one with shorter vectors.
     See the Schnorr-Euchner paper for a description of this.
     This basically generalizes the LLL reduction condition
     from blocks of size 2 to blocks of larger size.
```


It enjoys more widespread use in cryptography these days and possibly other areas. Since Sage has Damien Stehle's fast fpLLL library and NTL's BKZ this would make Sage a very nice tool for people who care about these algorithms.


---

Comment by malb created at 2008-05-25 20:22:19

The attached patch wraps the appropriate NTL functions. It has doctests for all new methods. However, someone more familiar with BKZ might want to add an example (possibly #long) which showcases the difference between LLL and BKZ.


---

Comment by craigcitro created at 2008-06-15 21:45:43

Changing keywords from "" to "editor_malb".


---

Comment by malb created at 2008-06-16 03:32:05

Ralf forwarded the review request to a colleague of his. I'll ping him again by the end of the week to see what happened.


---

Comment by malb created at 2008-06-22 17:59:56

Ralf, can you review the patch without the forwarding which now seems pointless?


---

Comment by malb created at 2008-06-25 11:17:09

*state of affairs for editorial meeting 26/06/08*

I didn't hear back from rpw yet. Maybe another referee could jump in.


---

Attachment

NTRU derived lattice, n=47


---

Comment by rpw created at 2008-07-07 23:13:12

Patch applied against SAGE 3.0.3. Works fine, doctests OK. Successfully tested on some cryptographically relevant toy sample lattices (NTRU derived, one is attached, provided by Markus Rückert).

Two typos found in documentation: 
 * permuation -> permutation
 * Gramm-Schmidt -> Gram-Schmidt


---

Comment by malb created at 2008-07-08 08:32:30

w00t, I'll fix the typos today-ish.


---

Comment by malb created at 2008-07-08 11:53:44

To highlight BKZ's features here is a Sage session for the NTRU example rpw provided:

```
sage: M = eval(open("ntru_2_47.sage").read()[4:])
sage: M
94 x 94 dense matrix over Integer Ring

sage: %time M_BKZ = M.BKZ()
CPU times: user 17.64 s, sys: 0.03 s, total: 17.67 s
Wall time: 17.98 s

sage: %time M_LLL = M.LLL()
CPU times: user 0.30 s, sys: 0.00 s, total: 0.30 s
Wall time: 0.30 s

sage: %time M_LLL_NTL = M.LLL(algorithm="NTL:LLL")
CPU times: user 0.11 s, sys: 0.01 s, total: 0.12 s
Wall time: 0.16 s

sage: sqrt(sum([ a^2 for a in M_BKZ[0] ])).n()
10.1488915650922

sage: sqrt(sum([ a^2 for a in M_LLL[0] ])).n()
23.0000000000000

sage: sqrt(sum([ a^2 for a in M_LLL_NTL[0] ])).n()
23.0000000000000

sage: sqrt(sum([ a^2 for a in M_BKZ[93] ])).n()
20.7364413533277

sage: sqrt(sum([ a^2 for a in M_LLL[93] ])).n()
43.0116263352131

sage: sqrt(sum([ a^2 for a in M_LLL_NTL[93] ])).n()
47.6340214552582
```



---

Comment by malb created at 2008-07-08 11:54:57

addresses rpw's review


---

Attachment

Typos fixed in updated patch, apply `bkz.patch` only.


---

Comment by mabshoff created at 2008-07-15 03:24:46

Merged bkz.patch in Sage 3.0.6.alpha0


---

Comment by mabshoff created at 2008-07-15 03:24:46

Resolution: fixed
