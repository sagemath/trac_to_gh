# Issue 262: extend point counting on elliptic curves to non-prime finite fields

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-02-15 15:57:47

Assignee: was

As a first step, do the case when the coefficients of the curve are
in GF(p).

```
Hello,
 
Currently, asking SAGE for the cardinality of an elliptic curve over a non-prime finite field gives the following message
 
WARNING: Using very very stupid algorithm for counting
points over non-prime finite field. Please rewrite.
 
For elliptic curves with coefficients in the integers this is a fairly easy rewrite, which I've attached as the function smartercard; I describe the mathematical background here- http://maths.straylight.co.uk/archives/67 . However, I lack the programming skills to tie this into SAGE; since there are coding sprints in the near future, perhaps someone could take a look at incorporating this idea?
 
Cheers, Graeme
```



```
def smartercard(E):
        G=E.base_field();
        p=G.characteristic();
        q=G.cardinality();
        r=log(q,b=p);
        Ep=EllipticCurve(GF(p,'a'),E.a_invariants());
        t=Ep.trace_of_frobenius();
        alphap=t/2 + I*sqrt(p-t^2/4);
        Np=q + 1 - (alphap)^r - (alphap.conjugate())^r;
        return(int(Np))
```



---

Comment by was created at 2007-09-13 05:56:00

I have added the code by Alex Ghitza that implements the algorithm mentioned above into SAGE for 2.8.4.2.


---

Comment by was created at 2007-09-13 05:56:00

Resolution: fixed
