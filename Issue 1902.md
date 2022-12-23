# Issue 1902: mistake in the documentation for gens for Finite field givaro

Issue created by migration from https://trac.sagemath.org/ticket/1902

Original creator: was

Original creation time: 2008-01-24 00:37:08

Assignee: somebody


```
> sage: sage.rings.finite_field_givaro.FiniteField_givaro.gen?
> [...]
> Docstring:
> 
>             Return a generator of self. All elements x of self are
>             expressed as log_{self.gen()}(p) internally. If self is
>             a prime field this method returns 1.
> 
> (The sentence "If self is a prime field..." is wrong, but the first
> sentence is correct.)
```



---

Attachment

Attached patch corrects the docstring and adds a new doctest which is relevant,


---

Comment by cremona created at 2008-03-01 16:31:24

Changing status from new to assigned.


---

Comment by cremona created at 2008-03-01 16:31:24

Changing assignee from somebody to cremona.


---

Attachment

I hand-edited John's original 8683.patch to create edited-8683.patch: I changed "primitve" -> "primitive".

With this revised patch: looks good, the doctest passes.


---

Comment by mabshoff created at 2008-03-02 17:12:17

Merged edited-8683.patch in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-02 17:12:17

Resolution: fixed
