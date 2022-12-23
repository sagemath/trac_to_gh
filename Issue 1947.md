# Issue 1947: Implement homomorphisms between vector spaces

Issue created by migration from https://trac.sagemath.org/ticket/1947

Original creator: craigcitro

Original creation time: 2008-01-27 10:46:59

Assignee: craigcitro

CC:  mmezzarobba slelievre jipilab

It's surprising that this isn't already done -- it should be easy, since the morphisms don't have to do too much, and one already has the more complicated ring homomorphism code to use as a guide. I'll do this at SD7, if no one beats me to it.


---

Comment by was created at 2008-01-27 13:11:37

Craig, since homomorphisms between vector spaces *are* implemented (as I explained to you in irc last week), could you change the title of this trac ticket and explain what you are actually proposing be implemented?  Thanks.

```
sage: V = QQ^3; W = QQ^2
sage: H = V.Hom(W)
sage: H([1..6])

Free module morphism defined by the matrix
[1 2]
[3 4]
[5 6]
Domain: Vector space of dimension 3 over Rational Field
Codomain: Vector space of dimension 2 over Rational Field
```



---

Comment by craigcitro created at 2008-01-27 17:59:22

Note that my first title for this ticket was ridiculous -- Sage has homomorphisms between vector spaces. The issue is to have homomorphisms over vector spaces V --> W when V and W are over different fields, but one has a map from the base field of V to the base field of W.


---

Comment by AlexGhitza created at 2009-01-23 02:44:41

Changing type from defect to enhancement.


---

Comment by was created at 2012-02-26 18:53:08

Changing priority from major to minor.


---

Comment by mmezzarobba created at 2015-04-13 14:47:01

Works now, but may be worth a few tests:

```
sage: Hom(QQ^3, RR^2)([[1,2],[3,4],[5,6]])
Vector space morphism represented by the matrix:
[1 2]
[3 4]
[5 6]
Domain: Vector space of dimension 3 over Rational Field
Codomain: Vector space of dimension 2 over Real Field with 53 bits of precision
```



---

Comment by slelievre created at 2018-05-11 20:47:19

Where should such documentation and tests go?


---

Comment by git created at 2019-05-11 16:51:36

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by @black-stones created at 2019-05-11 16:56:56

Changing status from new to needs_review.


---

Comment by @black-stones created at 2019-05-11 16:56:56

Replying to [comment:9 mmezzarobba]:
> Works now, but may be worth a few tests:
> {{{
> sage: Hom(QQ^3, RR^2)([[1,2],[3,4],[5,6]])
> Vector space morphism represented by the matrix:
> [1 2]
> [3 4]
> [5 6]
> Domain: Vector space of dimension 3 over Rational Field
> Codomain: Vector space of dimension 2 over Real Field with 53 bits of precision
> }}}

I took this example and turned it into two doctests. Nothing new was added, just wanted to close this decade-old ticket.


---

Comment by @mwageringel created at 2019-05-17 15:50:23

It seems odd that the following also works. Is there a reason that this is not prevented?


```
sage: f = Hom(RR^2, QQ^2)([[1,2],[3,4]]); f
Vector space morphism represented by the matrix:
[1 2]
[3 4]
Domain: Vector space of dimension 2 over Real Field with 53 bits of precision
Codomain: Vector space of dimension 2 over Rational Field
sage: f(vector(RR, [1,2]))
(7, 10)
```



---

Comment by embray created at 2019-07-03 11:37:56

Moving tickets from the Sage 8.8 milestone that have been actively worked on in the last six months to the next release milestone (optimistically).


---

Comment by embray created at 2019-12-30 14:48:17

Ticket retargeted after milestone closed


---

Comment by vdelecroix created at 2020-02-15 15:26:38

Please:
- update the ticket description to something meaningful.
- break the lines in the documentation so that there are at most 72 characters wide.


---

Comment by vdelecroix created at 2020-02-15 15:26:38

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2020-04-14 19:41:51

Batch modifying tickets that will likely not be ready for 9.1, based on a review of the ticket title, branch/review status, and last modification date.


---

Comment by mkoeppe created at 2021-02-13 20:51:01

Setting new milestone based on a cursory review of ticket status, priority, and last modification date.


---

Comment by mkoeppe created at 2021-07-19 00:44:56

Setting a new milestone for this ticket based on a cursory review.
