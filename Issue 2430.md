# Issue 2430: is_EuclideanDomain() gives wrong answers

Issue created by migration from Trac.

Original creator: cremona

Original creation time: 2008-03-08 20:35:42

Assignee: mabshoff

In 2.10.2 and 2.10.3.rc2:

```
sage: is_EuclideanDomain(ZZ)
False
```


I looked to whether any of Sage's rings would ever return True for this function, and came up with pAdicRingGeneric and no others:

```
sage: is_EuclideanDomain(pAdicRing(7))
True
```


So this idea (to have EuclideanDomains as a class) just has not been properly implemented.
As a start we could make rings which are certainly Euclidean (e,g, ZZ and univariate polynomials over a field) be derived from EuclideanDomain instead of PrincipalIdealDomain as they are now.

That would not be a complete solution, since (for example) some rings of integers of number fields are Euclidean, though it is not easy to say which;  and there is no functionality to answer the question "is R Euclidean" except to see if R's class is (derived from) EuclideanDomain, which for rings of integers it never will be!

One other puzzling -- and inconsistent -- thing is that EuclideanDomainElement has a broader scope than EuclideanDomain:

```
sage: is_EuclideanDomain(ZZ)
False
sage: is_EuclideanDomainElement(ZZ(1))
True

sage: is_EuclideanDomain(R)
False
sage: is_EuclideanDomainElement(x)
True
```





---

Comment by mabshoff created at 2008-03-09 00:09:22

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2008-03-09 00:09:22

Changing component from Cygwin to linear algebra.


---

Comment by AlexGhitza created at 2008-03-16 02:29:07

Changing assignee from was to malb.


---

Comment by AlexGhitza created at 2008-03-16 02:29:07

Changing component from linear algebra to commutative algebra.


---

Comment by malb created at 2008-06-03 14:20:55

Remove assignee malb.


---

Comment by jhpalmieri created at 2008-09-26 18:19:10

I think that the current behavior is in line with the issues dealt with by #4192, and so this ticket should be closed.


---

Comment by mabshoff created at 2008-09-26 18:48:24

Resolution: wontfix


---

Comment by mabshoff created at 2008-09-26 18:48:24

I agreee. Closed as wontix. 

John: If you disagree please open another ticket that takes into consideration #4192, i.e. implements the proper methods exposed on the top level.

Cheers,

Michael
