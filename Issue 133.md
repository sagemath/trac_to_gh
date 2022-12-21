# Issue 133: Galois action

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2006-10-15 16:47:17

Assignee: was

Keywords: Galois group, algebric number theory

It would be great if something like the following worked:


```
sage: F = CyclotomicField(7)

sage: z = F.gen()

sage: G = F.galois_group()

sage: phi = G.random()

sage: z.galois_action(phi)
```


Also needed, I think, are embedding into CC.
AFAIK, neither of these has been entered onto the SAGE
"wish list".


---

Comment by was created at 2006-10-15 17:42:17

Complex embeddings were written long ago.  In your example above, try:

```
    F.complex_embeddings()
```



---

Comment by cremona created at 2008-09-04 16:13:05

This is quite usable:

```
sage: F = CyclotomicField(7)
sage: z = F.gen()           
sage: G = F.embeddings(F)   
sage: G                     

[
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^2,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^3,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^4,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^5,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> -zeta7^5 - zeta7^4 - zeta7^3 - zeta7^2 - zeta7 - 1
]
sage: [g(z) for g in G]     

[zeta7,
 zeta7^2,
 zeta7^3,
 zeta7^4,
 zeta7^5,
 -zeta7^5 - zeta7^4 - zeta7^3 - zeta7^2 - zeta7 - 1]
```


One could easily implement F.autumorphisms() to return F.embeddings(F), but in fact there is already End(F) -- whose existence I discovered by doing F.galois_group?

So what should be done is to change the structure returned by F.galois_group() which is <class 'sage.rings.number_field.galois_group.GaloisGroup'> to be derived from that of End(F) which is <class 'sage.rings.number_field.morphism.NumberFieldHomset'>,  which does not look very difficult to me...


---

Comment by davidloeffler created at 2009-05-25 13:39:54

This one was almost fixed by #5159; but unfortunately the above snippet didn't quite work, because my new GaloisGroup class derived from PermutationGroup_generic, and the random_element method of that class always returned a PermutationGroupElement (rather than a GaloisGroupElement, which has more functionality).

The above patch makes the necessary tiny changes to the permutation groups code so this now works, although the interface is slightly different from the above:

```
sage: F.<z> = CyclotomicField(7)
sage: G = F.galois_group()
sage: phi = G.random_element()
sage: phi(z)
z^4
```



---

Comment by davidloeffler created at 2009-05-25 13:39:54

Changing status from new to assigned.


---

Comment by davidloeffler created at 2009-05-25 13:39:54

Changing assignee from was to davidloeffler.


---

Comment by davidloeffler created at 2009-05-28 15:42:18

patch against 4.0.rc1


---

Attachment

The previous patch broke a doctest due to silly sorting issues; here's a better patch.


---

Comment by AlexGhitza created at 2009-05-30 09:07:16

Changing keywords from "Galois group, algebric number theory" to "Galois group, algebraic number theory".


---

Comment by AlexGhitza created at 2009-05-30 09:15:01

Very good!


---

Comment by mhansen created at 2009-06-01 04:43:38

Merged in 4.0.1.alpha0.


---

Comment by mhansen created at 2009-06-01 04:43:38

Resolution: fixed


---

Comment by was created at 2009-06-01 04:53:45

Lowest ticket award!
