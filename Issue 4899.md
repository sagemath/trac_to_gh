# Issue 4899: bug in sqrt(1) over GF(2^e) for e>15

Issue created by migration from https://trac.sagemath.org/ticket/4899

Original creator: cremona

Original creation time: 2009-01-01 12:14:52

Assignee: tbd

Keywords: finite fields


```
sage: GF(2^15,'a')(1).sqrt()
1
sage: GF(2^16,'a')(1).sqrt()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/john/<ipython console> in <module>()

/home/john/sage-3.2.2.rc1/local/lib/python2.5/site-packages/sage/rings/finite_field_ntl_gf2e.so in sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2eElement.sqrt (sage/rings/finite_field_ntl_gf2e.cpp:7072)()

AttributeError: 'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_g' object has no attribute '_one_element'
```

The point is that `GF(2^16)` (and higher) are of type  'sage.rings.finite_field_ntl_gf2e.FiniteField_ntl_gf2e'
and the code (lines 826,827 in finite_field_ntl_gf2e.pyx)

```
        if self.is_one():
            return self._one_element
```

fails.  It should be self.parent()._one_element  (though I don't know why "return self" would not be ok too).

Patch up very soon.


---

Attachment


---

Attachment

apply this after trac_4899.patch


---

Comment by was created at 2009-01-03 05:01:43

REFEREE REPORT:

Nice find.   You remark "It should be self.parent()._one_element (though I don't know why "return self" would not be ok too).".  In fact, I think returning self would be ok.  I tried that and it is also over twice as fast.  So I've posted a followup patch that does that instead.


---

Comment by mabshoff created at 2009-01-03 05:55:30

Shouldn't we add a doctest here?

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-03 06:03:14

Merged both patches in Sage 3.2.3.final


---

Comment by mabshoff created at 2009-01-03 06:03:14

Resolution: fixed


---

Comment by mabshoff created at 2009-01-03 06:13:09

Never mind, John's patch contained a doctest as William just pointed out to me in IRC.

Cheers,

Michael
