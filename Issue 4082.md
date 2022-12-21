# Issue 4082: [with patch, needs review] Sage 3.1.2.rc0: numerical noise on OSX/Intel in schemes/elliptic_curves/ell_number_field.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-09-09 01:53:21

Assignee: mabshoff


```
sage -t  devel/sage/sage/schemes/elliptic_curves/ell_number_field.py
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py", line 1108:
    sage: E.period_lattice(embs[0])
Expected:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
    From: Number Field in a with defining polynomial x^2 - 2
    To:   Real Field with 53 bits of precision
    Defn: a |--> -1.41421356237310
Got:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
      From: Number Field in a with defining polynomial x^2 - 2
      To:   Real Field with 53 bits of precision
      Defn: a |--> -1.41421356237309
**********************************************************************
File "/Users/mabshoff/sage-3.1.2.rc0/tmp/ell_number_field.py", line 1113:
    sage: E.period_lattice(embs[1])
Expected:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
    From: Number Field in a with defining polynomial x^2 - 2
    To:   Real Field with 53 bits of precision
    Defn: a |--> 1.41421356237309
Got:
    Period lattice associated to Elliptic Curve defined by y^2  = x^3 + a*x + 2 over Number Field in a with defining polynomial x^2 - 2 with respect to the real embedding Ring morphism:
      From: Number Field in a with defining polynomial x^2 - 2
      To:   Real Field with 53 bits of precision
      Defn: a |--> 1.41421356237310
**********************************************************************
```



---

Attachment


---

Comment by mhansen created at 2008-09-09 01:55:14

Looks good to me.


---

Comment by mabshoff created at 2008-09-09 02:03:33

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-09 02:03:33

Resolution: fixed
