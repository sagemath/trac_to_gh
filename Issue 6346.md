# Issue 6346: sage-4.0.2.rc2 build test problem on ppc os x 10.5

Issue created by migration from https://trac.sagemath.org/ticket/6346

Original creator: was

Original creation time: 2009-06-17 08:40:58

Assignee: tbd

this is the only problem:

```
sage -t -long "devel/sage/sage/rings/number_field/number_field_rel.py"
**********************************************************************
File "/Users/wstein/build/sage-4.0.2.rc2/devel/sage/sage/rings/number_field/number_field_rel.py", line 1767:
    sage: L.places()
Expected:
    [Relative number field morphism:
    From: Number Field in b with defining polynomial x^2 - 5 over its base field
    To:   Real Field with 106 bits of precision
    Defn: b |--> -2.236067977499789696409173668937
    c |--> -1.213411662762229634132131377426,
    Relative number field morphism:
    From: Number Field in b with defining polynomial x^2 - 5 over its base field
    To:   Real Field with 106 bits of precision
    Defn: b |--> 2.236067977499789696411548005367
    c |--> -1.213411662762229634130492421800,
    Relative number field morphism:
    From: Number Field in b with defining polynomial x^2 - 5 over its base field
    To:   Complex Field with 53 bits of precision
    Defn: b |--> -2.23606797749979 - 2.22044604925031e-16*I
    c |--> 0.606705831381115 - 1.45061224918844*I,
    Relative number field morphism:
    From: Number Field in b with defining polynomial x^2 - 5 over its base field
    To:   Complex Field with 53 bits of precision 
    Defn: b |--> 2.23606797749979 - 4.44089209850063e-16*I
    c |--> 0.606705831381115 - 1.45061224918844*I]
Got:
    [Relative number field morphism:
      From: Number Field in b with defining polynomial x^2 - 5 over its base field
      To:   Real Field with 106 bits of precision 
      Defn: b |--> -2.236067977499789696409173668937
            c |--> -1.213411662762229634132131377426, Relative number field morphism:
      From: Number Field in b with defining polynomial x^2 - 5 over its base field
      To:   Real Field with 106 bits of precision 
      Defn: b |--> 2.236067977499789696411548005367
            c |--> -1.213411662762229634130492421800, Relative number field morphism:
      From: Number Field in b with defining polynomial x^2 - 5 over its base field
      To:   Complex Field with 53 bits of precision
      Defn: b |--> -2.23606797749979 - 1.11022302462516e-15*I
            c |--> 0.606705831381116 - 1.45061224918844*I, Relative number field morphism:
      From: Number Field in b with defining polynomial x^2 - 5 over its base field
      To:   Complex Field with 53 bits of precision
      Defn: b |--> 2.23606797749979 - 4.44089209850063e-16*I
            c |--> 0.606705831381115 - 1.45061224918844*I]
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_54
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/wstein/build/sage-4.0.2.rc2/tmp/.doctest_number_field_rel.py
         [46.5 s]
```


It's just numerical noise I think.  Replace some e- term by ... to fix.


---

Attachment


---

Comment by craigcitro created at 2009-06-17 09:10:58

Looks good, and it fixes the issue.


---

Comment by craigcitro created at 2009-06-17 23:58:11

Resolution: fixed
