# Issue 4469: Sage 3.2.a3: output ordering randomness in sage/rings/number_field/number_field.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-11-08 20:18:58

Assignee: tbd

eno:

```
sage -t  devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/home/wstein/eno/sage-3.2.alpha3/tmp/number_field.py", line 1025:
    sage: [phi(k.0^2) for phi in v]
Expected:
    [2.97572074038...,
     -2.40889943716 + 1.90254105304*I,
     -2.40889943716 - 1.90254105304*I,
     0.921039066973 + 3.07553311885*I,
     0.921039066973 - 3.07553311885*I]
Got:
    [2.97572074038, 
     -2.40889943716 + 1.90254105304*I, 
     -2.40889943716 - 1.90254105304*I, 
     0.921039066973 - 3.07553311885*I, 
     0.921039066973 + 3.07553311885*I]
**********************************************************************
```

cicero:

```
sage -t  devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/home/wstein/cicero/build/sage-3.2.alpha3/tmp/number_field.py", line 1032:
    sage: K.complex_embeddings() 
Expected:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field 
      Defn: a |--> -1.25992104989...,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> 0.629960524947 - 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> 0.629960524947 + 1.09112363597*I
    ]
Got:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> -1.25992104989 + 2.77555756156e-16*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2      To:   Complex Double Field
      Defn: a |--> 0.629960524947 + 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> 0.629960524947 - 1.09112363597*I
    ]
**********************************************************************
```

menas:

```
sage -t  devel/sage/sage/rings/number_field/number_field.py 
**********************************************************************
File "/home/wstein/menas/build/sage-3.2.alpha3/tmp/number_field.py", line 1025:
    sage: [phi(k.0^2) for phi in v]
Expected:
    [2.97572074038...,
     -2.40889943716 + 1.90254105304*I,
     -2.40889943716 - 1.90254105304*I,
     0.921039066973 + 3.07553311885*I,
     0.921039066973 - 3.07553311885*I]
Got:
    [2.97572074038, 
     -2.40889943716 + 1.90254105304*I, 
     -2.40889943716 - 1.90254105304*I, 
     0.921039066973 - 3.07553311885*I, 
     0.921039066973 + 3.07553311885*I]
**********************************************************************
```



---

Comment by mabshoff created at 2008-11-16 08:58:27

Resolution: fixed


---

Comment by mabshoff created at 2008-11-16 08:58:27

This has gone away in 3.2.rc1. I am not sure which patch is responsible here.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-16 21:07:04

These problems pop up with gcc 4.3.2 and the system compiler on the given system does not show the problem. Reopened.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-16 21:07:04

Resolution changed from fixed to 


---

Comment by mabshoff created at 2008-11-16 21:07:04

Changing status from closed to reopened.


---

Attachment


---

Comment by craigcitro created at 2008-11-18 09:32:36

Patch simply adds `#random`. The real underlying bug is that we don't have a consistent ordering on elements in `CDF`: see #4544 for a discussion of this issue.


---

Comment by mabshoff created at 2008-11-18 09:35:07

Looks good.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-18 18:18:53

Merged in Sage 3.2.rc2


---

Comment by mabshoff created at 2008-11-18 18:18:53

Resolution: fixed
