# Issue 5154: bug in modular composition over GF(2)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-02-01 23:18:34

Assignee: malb

CC:  zimmerma


```
sage: P.<x> = PolynomialRing(GF(2))
sage: f = x^97 + x^95 + x^94 + x^93 + x^92 + x^91 + x^88 + x^86 + x^84 + x^79 + x^78 + x^77 + x^75 + x^72 + x^71 + x^70 + x^69 + x^66 + x^65 + x^63 + x^58 + x^55 + x^54 + x^52 + x^50 + x^46 + x^42 + x^39 + x^35 + x^33 + x^29 + x^28 + x^26 + x^24 + x^18 + x^16 + x^14 + x^13 + x^8 + x^6 + x^3
sage: g = x^100 + x^99 + x^98 + x^97 + x^96 + x^95 + x^94 + x^93 + x^92 + x^91 + x^90 + x^88 + x^87 + x^86 + x^85 + x^81 + x^80 + x^79 + x^78 + x^75 + x^73 + x^68 + x^66 + x^65 + x^64 + x^60 + x^59 + x^58 + x^57 + x^56 + x^54 + x^53 + x^52 + x^51 + x^49 + x^48 + x^42 + x^41 + x^40 + x^35 + x^32 + x^31 + x^30 + x^28 + x^26 + x^23 + x^21 + x^17 + x^16 + x^15 + x^14 + x^13 + x^11 + x^3 + x + 1
sage: h = x^99 + x^98 + x^95 + x^94 + x^93 + x^92 + x^89 + x^85 + x^84 + x^83 + x^81 + x^80 + x^79 + x^77 + x^76 + x^75 + x^72 + x^70 + x^65 + x^64 + x^63 + x^61 + x^60 + x^57 + x^53 + x^52 + x^50 + x^48 + x^47 + x^45 + x^44 + x^40 + x^39 + x^37 + x^36 + x^32 + x^31 + x^30 + x^29 + x^28 + x^26 + x^25 + x^24 + x^20 + x^17 + x^16 + x^14 + x^13 + x^12 + x^7 + x^6 + x^5 + x^4 + x^2 + 1
sage: f(g) % h == f.modular_composition(g,h)
False
```


I assume this is due to

```
sage: g % h == g
False
```

which should probably be checked first.


---

Attachment


---

Attachment

shows that the bug is indeed fixed


---

Comment by malb created at 2009-02-02 14:26:44

Paul's patch gets a positive review, someone needs to look over my doctest patch.


---

Comment by mabshoff created at 2009-02-02 14:30:51

Positive review for malb's doctest patch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 18:05:06

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 18:05:06

Merged in Sage 3.3.alpha4.

Cheers,

Michael
