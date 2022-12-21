# Issue 536: off by one in NZL::vec_ZZ::SetLength(long) (from modular/dirichlet.py)

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-08-30 18:54:24

Assignee: mabshoff

From Sage 2.8.3rc3:

```
==25034==  Address 0x24DB2020 is 8 bytes before a block of size 64 alloc'd
==25034==    by 0x97D3C09: NTL::vec_ZZ::SetLength(long) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/libntl.so)
==25034==    by 0x972D78F: NTL::PlainPseudoDivRem(NTL::ZZX&, NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sag
e-2.8.3.rc3/local/lib/libntl.so)
==25034==    by 0x972D9E6: NTL::PlainPseudoRem(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8.3.rc3/lo
cal/lib/libntl.so)
==25034==    by 0x9732BA2: NTL::rem(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8.3.rc3/local/lib/lib
ntl.so)
==25034==    by 0x9732E1C: NTL::MulMod(NTL::ZZX&, NTL::ZZX const&, NTL::ZZX const&, NTL::ZZX const&) (in /tmp/Work2/sage-2.8
.3.rc3/local/lib/libntl.so)
==25034==    by 0x1B790919: __pyx_f_20number_field_element_18NumberFieldElement__mul_c_impl(__pyx_obj_20number_field_element
_NumberFieldElement*, __pyx_obj_4sage_9structure_7element_RingElement*) (number_field_element.cpp:4198)
==25034==    by 0xE3C999D: __pyx_f_7element_11RingElement__mul_c (element.c:8340)
==25034==    by 0xE3BD3E4: __pyx_f_7element_11RingElement___mul__ (element.c:7922)
==25034==    by 0x41596C: binary_op1 (abstract.c:398)
==25034==    by 0x418EC3: PyNumber_InPlaceMultiply (abstract.c:744)
==25034==    by 0x481053: PyEval_EvalFrameEx (ceval.c:1274)
```

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-30 18:54:33

Changing status from new to assigned.


---

Comment by craigcitro created at 2010-01-17 22:48:30

I'm closing this as wontfix -- we don't know which doctest caused this, and it's old enough that the guilty code could well be gone anyway (for instance, all the arithmetic code was reworked with the coercion switch). Plus, this might actually be an issue in NTL. I'd be happy to look at this again if we had a way to reproduce it, but as it stands, it's not worth trying to hunt this down. (I guess I could rebuild 2.8.3, but that seems excessive ...)


---

Comment by craigcitro created at 2010-01-17 22:48:30

Resolution: wontfix
