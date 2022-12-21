# Issue 7368: Further work on isogenies and endomorphisms of elliptic curves

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2009-11-01 14:26:11

Assignee: cremona

CC:  weigandt pbruin sbesnier lorenz

Keywords: elliptic curves, isogeny, isogenies, endomorphism ring

Working on ticket #7096, I realised that there are many functionalities concerning morphisms of elliptic curves that are not implemented or implemented badly.

See also #6887, and #7262.

Here is a wish-list

 * General isogenies, not only cyclic ones should be implemented.
   Possibly this could be done in a clever way, by having it 
   internally factored into cyclic isogenies.
 * Non seperable isogenies, i.e. Frobenii should be there too. See 
   also #6413.
 * One should be able to compose them
 * Is there a way of constructing a (not necessarily normalized)
   isogeny knowing the degree and the domain and codomain ?
 * There should be an addition for isogenies with the same domain 
   and codomain.
 * There should be an endomorphism_ring for ellliptic curves whose
   elements are isogenies.
 * Similar automorphisms should give a group of isogenies.


---

Comment by adhalanay created at 2015-10-20 18:28:39

added
