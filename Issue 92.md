# Issue 92: Complex embeddings for non-cyclotomic number fields?

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-28 05:45:04

Assignee: somebody

I think this was in an older version of SAGE, but now it seems only to
work for cyclotomic fields... =(  Was there a reason for dropping it?
I was using it to build archimedian valuations for an arbitrary number
field, and am sad to see it go... =(  Thanks,

						-Jon
						 =)


---

Comment by was created at 2007-01-13 02:18:11

It works fine now:

```

sage: k = NumberField(x^3 + 2,'a')
sage: k.complex_embeddings()
[Ring morphism:
  From: Number Field in a with defining polynomial x^3 + 2
  To:   Complex Field with 53 bits of precision
  Defn: a |--> -1.25992104989487, Ring morphism:
  From: Number Field in a with defining polynomial x^3 + 2
  To:   Complex Field with 53 bits of precision
  Defn: a |--> 0.629960524947436 + 1.09112363597172*I, Ring morphism:
  From: Number Field in a with defining polynomial x^3 + 2
  To:   Complex Field with 53 bits of precision
  Defn: a |--> 0.629960524947436 - 1.09112363597172*I]
```



---

Comment by was created at 2007-01-13 02:18:11

Resolution: fixed
