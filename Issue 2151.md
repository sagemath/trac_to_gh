# Issue 2151: Error in quotient ring loaded from a file

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2008-02-13 20:54:50

Assignee: malb

Keywords: load quotient ring

Create a ring, an ideal and the quotient ring, and save ideal and quotient:

```
sage: Ring = PolynomialRing(QQ,'x,y,z')
sage: R = PolynomialRing(QQ,'x,y,z')
sage: Rel=R.ideal('x*y*z-1')
sage: QR=R.quotient_ring(Rel)
sage: QR('y')
ybar
sage: save(Rel,'Relation')
sage: save(QR,'Quotient')
sage: quit
```


After restart, try to reconstruct R,Rel and QR:

```
sage: Rel=load('Relation.sobj')
sage: Rel
Ideal (x*y*z - 1) of Multivariate Polynomial Ring in x, y, z over Rational Field
sage: R=Rel.ring()
sage: R('y')
y
sage: QR=R.quotient_ring(Rel)
sage: QR
Quotient of Multivariate Polynomial Ring in x, y, z over Rational Field by the ideal (x*y*z - 1)
sage: QR('y')
sage: QR.gens()
```


Both the last two commands result in a traceback, ending with

```
<type 'exceptions.TypeError'>: Singular error:
   ? `x` is not defined
   ? error occurred in STDIN line 21: `def sage10=[x*y*z - 1];`
```


Also the other saved data do not help:

```
sage: QR = load('Quotient')
sage: QR('y')
```

resulting in the same error.

William Stein suggested the following workaround, which may also help to track down the bug:

```
sage: R._singular_()

//   characteristic : 0
//   number of vars : 3
//        block   1 : ordering dp
//                  : names    x y z
//        block   2 : ordering C
sage: QR('y')
ybar
```




---

Comment by SimonKing created at 2008-02-13 21:26:52

Addendum: The workaround does not solve all problems.

First session:

```
sage: R=PolynomialRing(QQ,'x0,y0,z0')
sage: Rel=R.ideal('z0**2-1','x0*y0-1')
sage: QR=R.quotient_ring(Rel)
sage: QR('x0*y0')
1
sage: save(Rel,'Relation.sobj')
sage: quit 
```

Second session:

```
sage: Rel=load('Relation.sobj')
sage: R=Rel.ring()
sage: R._singular_()

//   characteristic : 0
//   number of vars : 3
//        block   1 : ordering dp
//                  : names    x0 y0 z0
//        block   2 : ordering C
sage: QR=R.quotient_ring(Rel)
sage: QR('x0*y0')
x0bar*y0bar
```


But the result should be 1, as in the first session!


---

Comment by SimonKing created at 2008-08-14 11:38:26

I don't know who did it, but it seems that the problem is solved! 

I tried the above failing examples with 3.1.alpha0, and it all worked fine.

Thank you very much!


---

Comment by SimonKing created at 2008-08-14 11:38:26

Resolution: fixed


---

Comment by mabshoff created at 2008-08-14 14:25:10

Simon,

we do not just close tickets. Please add a patch adding a doctest that verifies that this functionality is fixed.

Cheers,

Michael


---

Comment by mabshoff created at 2008-08-14 14:25:10

Changing status from closed to reopened.


---

Comment by mabshoff created at 2008-08-14 14:25:10

Resolution changed from fixed to 


---

Comment by malb created at 2008-08-18 12:14:24

I don't see how this can be doctested, since it requires two Sage sessions.


---

Comment by SimonKing created at 2008-08-18 13:12:23

Replying to [comment:4 malb]:
> I don't see how this can be doctested, since it requires two Sage sessions.

It is about pickling/unpickling, hence it should be testable with loads(dumps(...)). I'll see if I succeed in finding a test. 

And sorry for closing the ticket. A question: Is it possible to modify the trac system such that *only* administrators are able to close a ticket? This would have prevented me from a couple of errors.


---

Comment by malb created at 2008-08-18 13:36:59

Replying to [comment:5 SimonKing]:
> Replying to [comment:4 malb]:
> > I don't see how this can be doctested, since it requires two Sage sessions.
> 
> It is about pickling/unpickling, hence it should be testable with loads(dumps(...)). I'll see if I succeed in finding a test. 

I thought the issue was only present if the dump is unpickled from a different session, nevermind then & know yourself out writing doctests :-)

> And sorry for closing the ticket. A question: Is it possible to modify the trac system such that *only* administrators are able to close a ticket? This would have prevented me from a couple of errors.

AFAIK no, there is repeated talk about a new Trac version which matches our process better, but nothing solid has emerged.


---

Comment by SimonKing created at 2010-07-05 11:45:05

Resolution: fixed


---

Comment by SimonKing created at 2010-07-05 11:45:05

Replying to [comment:2 SimonKing]:
> I don't know who did it, but it seems that the problem is solved! 
> 
> I tried the above failing examples with 3.1.alpha0, and it all worked fine.

I tried again, with sage 4.4.3, and it still works. So, can please someone finally close this ticket? I hope I am at least entitled to resolve it as "fixed".
