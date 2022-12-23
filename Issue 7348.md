# Issue 7348: speed up computation of multiplicative orders of finite field elements

Issue created by migration from https://trac.sagemath.org/ticket/7348

Original creator: fwclarke

Original creation time: 2009-10-29 10:01:10

Assignee: tbd

CC:  slelievre

Keywords: Finite Field

The function `sage.rings.finite_field_element.multiplicative_order` should use
`sage.groups.generic.order_from_multiple` (see the example in #7324), and 
the factorization of the order of the multiplicative group of the field 
should be cached; see the documentation for `order_from_multiple`.


---

Comment by slelievre created at 2021-03-20 00:12:43

Changing keywords from "Finite Field" to "finite field".


---

Comment by slelievre created at 2021-03-20 00:12:43

Changing component from algebra to finite rings.
