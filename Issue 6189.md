# Issue 6189: 'integrate' produces incorrect answer

Issue created by migration from Trac.

Original creator: emchristiansen

Original creation time: 2009-06-02 19:29:04

Assignee: burcin

Keywords: integrate, integral, incorrect

Affects: 
x64 Ubuntu 9.04 (Jaunty)
Sage 4.0, compiled from source, and updated (sage -upgrade) as of this posting

By simply casting a number using 'n()', I can cause integrate to return a vastly different result. See below:

```
var = sage.calculus.calculus.var

def NormalPDF(x,mu,sigma):
    return 1/sqrt(2*pi*sigma^2)*exp(-1/(2*sigma**2)*(x-mu)^2)

x = var('x')
mu = var('m')
sigma = var('s')
assume(sigma>0)
child1 = NormalPDF(x,0,1)
child2 = NormalPDF(x,n(0),n(1))
parent = NormalPDF(x,mu,sigma)

# this expansion helps Sage to do the integral
integrand1 = ((parent-child1)^2).expand()
integrand2 = ((parent-child2)^2).expand()

int1 = integrate(integrand1,x,-infinity,infinity)
int2 = integrate(integrand2,x,-infinity,infinity)

print "THIS EXPRESSION:"
print int1
print "\nSHOULD BE VERY SIMILIAR TO THIS EXPRESSION:"
print int2

print "\nMAKING THIS NUMBER:"
print int1.subs({mu:0,sigma:1}).n()
print "\nVERY SIMILAR TO THIS NUMBER:"
print int2.subs({mu:0,sigma:1}).n()
```


The above produces the output:

```
THIS EXPRESSION:
1/2*((s + 1)*sqrt(s^2 + 1)*e^(1/2*m^2/(s^2 + 1)) - 2*sqrt(2)*s)*e^(-1/2*m^2/(s^2 + 1))/(sqrt(s^2 + 1)*sqrt(pi)*s)

SHOULD BE VERY SIMILIAR TO THIS EXPRESSION:
1/2*(sqrt(0.5*s^2 + 0.5)*e^(1/2*m^2/(s^2 + 1)) - sqrt(2)*s)*e^(-1/2*m^2/(s^2 + 1))/(sqrt(0.5*s^2 + 0.5)*sqrt(pi)*s)

MAKING THIS NUMBER:
0.000000000000000

VERY SIMILAR TO THIS NUMBER:
-0.116847488627555
```


Mathematica claims the correct integral is:

```
\frac{1+\sigma }{2 \sqrt{\pi } \sigma }-\frac{\sqrt{2} e^{-\frac{\mu ^2}{2+2 \sigma ^2}}}{\sqrt{\pi +\pi  \sigma ^2}}
```



---

Comment by kcrisman created at 2009-09-29 14:45:13

This is now fixed, presumably in the Maxima upgrade.  Note that the integral in fact computes _without_ expand(), and in that case there is no 'experimental error'!  Attached patch verifies this.


---

Attachment

Based on 4.1.2.alpha2


---

Comment by kcrisman created at 2009-09-29 14:46:14

Despite what it says, actually based on 4.1.2.alpha4.


---

Comment by mhansen created at 2009-10-16 08:14:19

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-10-16 08:14:19

Looks good to me.


---

Comment by mhansen created at 2009-10-16 08:15:46

Resolution: fixed
