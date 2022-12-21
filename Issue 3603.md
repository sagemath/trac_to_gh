# Issue 3603: memleak in GF(2^n)

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2008-07-08 11:06:59

Assignee: mabshoff

CC:  jpflori

Valgrind Memcheck:


```
48 bytes in 1 blocks are possibly lost in loss record 459 of 3,113
   at 0x4C1FFEB: malloc (vg_replace_malloc.c:207)
   by 0x9BA45D7: NTL::WordVector::DoSetLength(long) (WordVector.c:33)
   by 0x9BA48B9: NTL::WordVector::operator=(NTL::WordVector const& (WordVector.h:80)
   by 0x9B554D1: NTL::operator>>(std::istream&, NTL::GF2E&) (GF2E.h:363)
   by 0x21DE011F: void _from_str<NTL::GF2E>(NTL::GF2E*, char*) (ccobject.h:86)
   by 0x21DD2033: __pyx_pf_4sage_5rings_21finite_field_ntl_gf2e_20FiniteField_ntl_gf2e_gen(_object*, _object*, _object*) (finite_field_ntl_gf2e.cpp:4416)
   by 0x417D72: PyObject_Call (abstract.c:1861)
   by 0xF4342C1: __pyx_pf_4sage_9structure_11parent_gens_14ParentWithGens_gens (parent_gens.c:1926)
   by 0x417D72: PyObject_Call (abstract.c:1861)
   by 0xF43819F: __pyx_pf_4sage_9structure_11parent_gens_14ParentWithGens__first_ngens (parent_gens.c:1377)
   by 0x487F49: PyEval_EvalFrameEx (ceval.c:3561)
   by 0x489855: PyEval_EvalCodeEx (ceval.c:2836)
```


Code in question in `finite_field_ntl_gf2e.pyx`:

```
        if PY_TYPE_CHECK(e, gen):
            e = e.lift().lift()
            try:
                GF2E_conv_long(res.x, int(e[0]))
            except TypeError:
                GF2E_conv_long(res.x, int(e))

            g = self._new()
            GF2E_from_str(&g.x, "[0 1]") # not the fastest
            x = self._new()
            GF2E_conv_long(x.x,1)

            for i from 0 < i <= e.poldegree():
                GF2E_mul(x.x, x.x, g.x)
                if e[i]:
                    GF2E_add(res.x, res.x, x.x )
            return res
```


Doctest which reveals leak: `ell_finite_field.py`


---

Comment by malb created at 2009-01-25 19:02:16

Changing status from new to assigned.


---

Comment by malb created at 2009-01-25 19:02:16

Changing assignee from mabshoff to malb.
