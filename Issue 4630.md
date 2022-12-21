# Issue 4630: bug in functions real() and imag().

Issue created by migration from Trac.

Original creator: ggrafendorfer

Original creation time: 2008-11-26 23:39:46

Assignee: somebody

Using sage-3.2 (compiled with make), but the same behaviour also happens on sage-3.1.4,
OS:Debian on a 32-bit Core-Duo machine,

the examples where I use 'a' as variable work well,
the examples where I use 'b' as variable ('I' is substituted by 'CDF(I)') are buggy:


```
georg`@`HILBERT:~/Daten/Sync/Phd/Code/sde$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 3.2, Release Date: 2008-11-20                         |
| Type notebook() for the GUI, and license() for information.        |
sage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()
e^(0.200000000000000*I*pi)
<class 'sage.calculus.calculus.SymbolicComposition'>
cos(0.200000000000000*pi)
0.809016994374947
sage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()
e^(0.200000000000000*pi*I)
<class 'sage.calculus.calculus.SymbolicComposition'>
e^(0.200000000000000*pi*I)
0.809016994374947 + 0.587785252292473*I
sage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()
e^(0.200000000000000*I*pi)
<class 'sage.calculus.calculus.SymbolicComposition'>
sin(0.200000000000000*pi)
0.587785252292473
sage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()
e^(0.200000000000000*pi*I)
<class 'sage.calculus.calculus.SymbolicComposition'>
0
0.000000000000000
sage: n(exp(CDF(I)*0.2*pi))
0.809016994374947 + 0.587785252292473*I
```


Georg


---

Comment by AlexGhitza created at 2009-06-03 07:43:38

This appears to be fixed in sage-4.0.1.alpha0:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.200000000000000*pi)
0.809016994374947
sage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.2*pi)
0.809016994375
sage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.200000000000000*pi)
0.587785252292473
sage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.2*pi)
0.587785252292
sage: n(exp(CDF(I)*0.2*pi))
0.809016994375 + 0.587785252292*I
```



---

Comment by mvngu created at 2009-07-26 03:33:48

Resolution: fixed


---

Comment by mvngu created at 2009-07-26 03:33:48

It looks like this is fixed in Sage 4.1:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: a = exp(I*0.2*pi); a; type(a); real(a); real(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.200000000000000*pi)
0.809016994374947
sage: b = exp(CDF(I)*0.2*pi); b; type(b); real(b); real(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
cos(0.2*pi)
0.809016994375
sage: a = exp(I*0.2*pi); a; type(a); imag(a); imag(a).n()
e^(0.200000000000000*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.200000000000000*pi)
0.587785252292473
sage: b = exp(CDF(I)*0.2*pi); b; type(b); imag(b); imag(b).n()
e^(0.2*I*pi)
<type 'sage.symbolic.expression.Expression'>
sin(0.2*pi)
0.587785252292
sage: n(exp(CDF(I)*0.2*pi))
0.809016994375 + 0.587785252292*I
```

I'm closing this ticket as fixed.
