# Issue 4937: bug in _p_primary_torsion_basis() for elliptic curves

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2009-01-04 19:21:48

Assignee: was

Keywords: elliptic curve torsion

Testing for #4901 has revealed a bug (an embarrassing one in code of mine) in _p_primary_torsion_basis() as exemplified here:

```
 sage: p=10^60+3201
sage: K=GF(p)
sage: a=804515977734860566494239770982282063895480484302363715494873
sage: b=584772221603632866665682322899297141793188252000674256662071
sage: E=EllipticCurve(K,[0,a,0,b,0])
sage: E.cardinality().factor()
2^17 * 13115567671 * 581705246972988608203110387504181554514650287
sage: E._p_primary_torsion_basis(2)

[[(656068448840236768725810484116830935925716002501543862440466 : 324360550482744921974063628110267202720852104214117741680354 : 1),
  2],
 [(21059802536298599082171845328893691100757301985761775129713 : 0 : 1), 1]]
```

Here the 2-sylow subgroup has structure `2^16 * 2` but E._p_primary_torsion_basis(2) only gives `2<sup>2*2</sup>1`.  I know what the problem is and am working out how to fix it.

NB This function is called in ell_torsion.py in computing torsion groups over number fields, which is rather likely to give wrong answers (though not over Q where pari is used ;)) until this is fixed.  Hence I made this a separate ticket marked "major defect"!

Michael: I set the milestone for this as 3.3 since it's a potentially serious bug in this corner of Sage, but feel free to bump it up.  I hope I might be able to fix it tonight but if not then it will take a few days as teaching starts again tomorrow...



---

Comment by mabshoff created at 2009-01-04 19:25:29

John,

this is fine as long as it applies after the ReST conversion. There are already a bunch of tickets lined up, so 3.3 will contain a bunch of fixes besides the ReST conversion.

Cheers,

Michael


---

Comment by cremona created at 2009-01-06 21:49:59

The patch which fixes this bug is actually at #4900 (sorry), based on 3.2.3 + #4926 (sphinxification).  So this one should not be applied until after those two.  All this one does is to add a doctest which shows that the bug reported here separately has been fixed.


---

Comment by roed created at 2009-01-24 14:34:35

Works for me.


---

Comment by mabshoff created at 2009-01-24 15:51:32

There are other doctests that have been added in that docstring in 3.3.alphaX, so I will rebase this once 3.3.alpha2 is out.

Cheers,

Michael


---

Attachment

This patch is the rebased version of John's patch.


---

Comment by mabshoff created at 2009-01-28 17:42:01

Resolution: fixed


---

Comment by mabshoff created at 2009-01-28 17:42:01

Merged the rebased trac_4937.patch in Sage 3.3.alpha3.

Cheers,

Michael
