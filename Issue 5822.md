# Issue 5822: cusps -- implement action of the Galois group on cusps for congruence subgroups as on page 12 of Steven's "Arithmetic on Modular Curves"

Issue created by migration from https://trac.sagemath.org/ticket/5822

Original creator: was

Original creation time: 2009-04-19 03:54:35

Assignee: was

CC:  robertwb craigcitro

It would be very useful if for a congruence subgroup G and an integer d coprime to the level N of G, one could compute the action on cusps (modulo G) of `tau_d \in Gal(Q(zeta_N)/Q)`.   This action is described on page 12 of Steven's "Arithmetic on Modular Curves". 

Note that Sage does not have a data type for "equivalence classes of cusps" yet, and the action is only well defined on equivalence classes.  However, one easy thing to implement (hopefully) is a function so that if G is a congruence subgroup, then we have

```
sage: G.galois_action_on_cusps(d, alpha)
```

which returns a cusp beta that is in the class of tau_d([alpha]).

Later when there is a data structure for equivalence classes of cusps, and also one for these Galois groups (as abstract groups), then that will call the above function.


---

Attachment


---

Comment by was created at 2009-04-19 06:03:33

NOTE: What I ended up implementing doesn't have an API exactly the same as the description in the ticket.  Please read the patch to see how to use it.


---

Comment by cremona created at 2009-04-20 08:42:36

Just a quick comment: Maite Aranes and I have been implementing number field cusps, and we decided not to have a class for cusp equivalence classes modulo a congruence subgroup, the reason being that there was no such class over Q.  So if the consensus is that such a class should exist, we'll include it over number fields too.

Our NFcusps code has not yet been put out to review, but probably should be soon - -it has had a lot os spinoffs in number field utilities, which have all now been merged.


---

Comment by cremona created at 2009-04-20 10:41:51

Positive review:  applies ok to 3.4.1.rc3, does what it says and works.

Comment:  OK, so this is how Galois acts, but would it not be a good idea to also mention that this gives the action of the so-called diamond operators?   i.e. the standard operation of `(Z/NZ)^* = Gamma_0(N)/Gamma_1(N)` ?  I looked to see if they were already defined, e.g. on ManinSymbols, but the only reference to "diamond" which search_src() revealed was a reference to the book by D & Shurman!

I would know the answer to the above if I had got further through the modular/modsym directory on the last docday, but doing just two files took up all the time I had.  And now term has started.


---

Comment by was created at 2009-04-20 15:14:55

> Just a quick comment: Maite Aranes and I have been implementing number 
> field cusps, and we decided not to have a class for cusp equivalence 
> classes modulo a congruence subgroup, the reason being that there 
> was no such class over Q. So if the consensus is that such a class 
> should exist, we'll include it over number fields too. 

I think it would be very natural to have a class for the set of cusps modulo a congruence subgroup.   The only reason Sage doesn't have that now is that I didn't have time yet to implement it.


---

Comment by mabshoff created at 2009-04-23 07:19:10

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-23 07:19:10

Resolution: fixed
