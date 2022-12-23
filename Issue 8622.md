# Issue 8622: Atkin-Lehner operators don't work for odd weight modular forms

Issue created by migration from https://trac.sagemath.org/ticket/8622

Original creator: davidloeffler

Original creation time: 2010-03-29 10:27:02

Assignee: craigcitro

Keywords: atkin-lehner

In ticket #5262 I implemented a method to find the Atkin-Lehner eigenvalue of a modular form. Sadly this does not work if the form has odd weight:


```
sage: f = Newforms(Gamma1(13),3,names='a')[0]
sage: f
q + a0*q^2 + (1/7*a0^3 + 2/7*a0^2 - 3/7*a0 - 27/7)*q^3 + (-8/21*a0^3 - 23/21*a0^2 - 88/21*a0 + 16/7)*q^4 + (2/7*a0^3 + 11/7*a0^2 + 29/7*a0 + 9/7)*q^5 + O(q^6)
sage: f.atkin_lehner_eigenvalue()
---------------------------------------------------------------------------
ArithmeticError                           Traceback (most recent call last)
...
ArithmeticError: subspace is not invariant under matrix
```


This comes up because for modular symbols of any odd weight, the Atkin-Lehner involution doesn't commute with the star involution and hence doesn't restrict to an operator on the plus submodule of the modular forms (hence "subspace not invariant under matrix"). In fact they _anti-commute_:

```
sage: N = f.modular_symbols(sign=0)
sage: a = N.atkin_lehner_operator(13).matrix()
sage: b = N.star_involution().matrix()
sage: a * b * ~a * ~b
[-1  0  0  0  0  0  0  0]
[ 0 -1  0  0  0  0  0  0]
[ 0  0 -1  0  0  0  0  0]
[ 0  0  0 -1  0  0  0  0]
[ 0  0  0  0 -1  0  0  0]
[ 0  0  0  0  0 -1  0  0]
[ 0  0  0  0  0  0 -1  0]
[ 0  0  0  0  0  0  0 -1]
```



---

Comment by robharron created at 2012-05-17 05:15:56

What's worse is the following:

```
sage: f = Newforms(Gamma1(7),3,names='a')[0]
sage: f
q - 3*q^2 + 5*q^4 + O(q^6)
sage: f.atkin_lehner_eigenvalue()
3
```

Here, f is a CM form with CM by its own Nebentype and hence has totally real coefficients. It is therefore an eigenvector of Atkin–Lehner. But the eigenvalue is certainly not 3, since it must be i or -i. This function should at least raise an NotImplementedError for odd weights. Note that the documentation for this function says that it always returns 1 or -1 (which would be wrong even if it was properly implemented).

Would it be silly to simply compute a ratio of L-values? I.e. if you have an odd weight newform with totally real Hecke eigenvalue field (i.e. with CM by its own Nebentypus), you could use Dokchitser's code to determine the sign of the functional equation and hence the Atkin–Lehner eigenvalue. You don't know the sign, so you could just try 1 and -1 and use checkfeq(). Then, for the above modular form, you can compute 2*pi*i*L(1,f) / (sqrt(8)*L(2,f) and get i, which is therefore the Atkin–Lehner eigvenvalue. In general, in the odd weight case (with totally real coefficients), a ratio of near-central L-values should tell you the Atkin–Lehner eigenvalue.


---

Comment by davidloeffler created at 2012-05-17 07:20:19

I have some old code lying around which prevents obviously bogus values being returned; I'll see if I can dig it up as a stopgap.

The trouble with the trick you mention is that (unless I've misunderstood) you would only get a numerical approximation to the eigenvalue, and you'd have to choose an embedding of the coefficient field into CC; and it is difficult to recognise a number field element from a numerical approximation to it, as always. 

One of the PhD students here at Warwick, Barinder Banwait, has been working on calculating Atkin-Lehner eigenvalues and he may have some code ready soon.


---

Comment by robharron created at 2012-05-17 18:04:05

Well, you do only get a numerical approximation to the eigenvalue, but in the odd weight case, you know the eigenvalue is i or -i, since the square of Atkin–Lehner acts by (-1)<sup>k</sup> (where k is the weight).

As for embeddings, I think I'd have to consider it more carefully to be sure, but my feeling is that this shouldn't matter. The functional equation relates the L-function of f at s to the L-function of W(f) at k-s and W(f) = w*f', where f' is the newform whose coefficients are the complex conjugates of those of f. The newforms we are discussing have totally real coefficients, so f'=f and L(s,f) is related to L(k-s,f) by a functional equation, and w, the Atkin–Lehner eigenvalue, appears in that functional equation (and w<sup>2</sup> = -1). Now, L(s,f) really depends on a complex embedding of the Hecke eigenvalue field of f into C, but such a dependancy shouldn't change the sign of the functional equation (right?). Now, I found a newform with CM by its own Nebentypus and Hecke eigenvalue field a totally real cubic extension and tried this out and the answer I got was independent of the complex embedding:


```
sage: def lseries(selfe, prec = 100, max_imaginary_part=0, max_asymp_coeffs=40, threshold = 1e-10):
    K = selfe.hecke_eigenvalue_field()
    iotas = K.complex_embeddings()
    Ls = []
    i = 0
    for iota in iotas:
        Ls.append(Dokchitser(conductor = selfe.level(), gammaV = [0, 1], weight = selfe.weight(), eps = 1, prec = prec))
        coeffs = 'coeff = %s;'%[iota(a_n) for a_n in selfe.q_expansion(prec).list()]
        #print coeffs
        Ls[-1].init_coeffs('coeff[k+1]', pari_precode = coeffs, max_imaginary_part = max_imaginary_part, max_asymp_coeffs = max_asymp_coeffs)
        if Ls[-1].check_functional_equation().abs() > threshold:
            Ls[-1] = Dokchitser(conductor = selfe.level(), gammaV = [0, 1], weight = selfe.weight(), eps = -1, prec = prec)
            Ls[-1].init_coeffs('coeff[k+1]', pari_precode = coeffs, max_imaginary_part = max_imaginary_part, max_asymp_coeffs = max_asymp_coeffs)
            if Ls[-1].check_functional_equation().abs() > threshold:
                print "Sign not found!"
    return Ls
....: 
sage: f = Newforms(Gamma1(23),3,names='a')[0]sage: f.hecke_eigenvalue_field()
Number Field in a0 with defining polynomial x^3 - 12*x + 7
sage: f.q_expansion(10)
q + a0*q^2 + (-1/3*a0^2 - 5/3*a0 + 8/3)*q^3 + (a0^2 - 4)*q^4 + (-5/3*a0^2 - 4/3*a0 + 7/3)*q^6 + (4*a0 - 7)*q^8 + (7/3*a0^2 + 11/3*a0 - 29/3)*q^9 + O(q^10)
sage: Ls = lseries(f)
sage: for L in Ls:
    print L(1) * 2 * pi.N() * I/(sqrt(f.level()).N() * L(2))
....: 
1.00000000000000*I
1.00000000000000*I
1.00000000000000*I
```


Obviously, it would be nice to be able to deal with the pseudo-eigenvalues in the general case, but in the meantime, if this makes sense, it would be nice. Also, note that I had to write my own function for getting the L-function of f since the current implementation only deals with Γ<sub>0</sub>. (Is there a reason the latter hasn't been implemented?)


---

Comment by davidloeffler created at 2012-05-18 07:37:44

> Well, you do only get a numerical approximation to the eigenvalue, but in the odd weight case, you know the eigenvalue is i or -i, since the square of Atkin–Lehner acts by (-1)k (where k is the weight). 

Just to be clear: are you referring here to your very specific case of odd weight CM forms with CM by their own nebentypus? Otherwise this statement is false: you know the product of the pseudo-eigenvalues of f and f*, but there is no reason why these two numbers should be equal.


---

Comment by robharron created at 2012-05-18 13:23:06

Replying to [comment:6 davidloeffler]:
> 
> Just to be clear: are you referring here to your very specific case of odd weight CM forms with CM by their own nebentypus? Otherwise this statement is false: you know the product of the pseudo-eigenvalues of f and f*, but there is no reason why these two numbers should be equal.

Right. I'm only referring to that specific case. And while it does seem like an extremely specific case, it is also true that the only newforms on Γ<sub>1</sub> that are actual eigenvectors of Atkin–Lehner are those of trivial character and those with CM by their own Nebentypus. Since the function in question is atkin_lehner_eigenvalue, and it seems like we can deal with all cases in which it makes sense to call this function, I think it makes sense it implement it. For the pseudoeigenvalues, it might be better to make a new function atkin_lehner_pseudoeigenvalue which can return the eigenvalue in the above cases. Of course, if you think this student working on pseudoeigenvalues will be done soon, then maybe it's not worth the trouble.


---

Comment by pbruin created at 2015-08-20 08:18:34

This will hopefully be solved by #18061 (I didn't know about this ticket when I opened that one), although currently it isn't.  With #18061 applied I now get (choosing the base ring such that `gauss_sum()` has a chance of working)

```
sage: f = Newforms(Gamma1(13), 3, CyclotomicField(40), names='a')[0]
sage: f.atkin_lehner_eigenvalue()
Traceback (most recent call last):
...
TypeError: Cannot coerce zeta52 into Cyclotomic Field of order 40 and degree 16
```

This seems to be caused by `gauss_sum()` working in the wrong cyclotomic field; doing `f.character().gauss_sum()` leads to the same error.  Applying #19056 does not solve this (yet).


---

Comment by pbruin created at 2015-08-20 11:46:47

The bug in the above comment is now #19060.


---

Comment by pbruin created at 2016-07-11 10:14:13

In SageMath 7.3.beta7 with #18061 merged, one gets yet another error:

```
sage: f = Newforms(Gamma1(13), 3, CyclotomicField(40), names='a')[0]
sage: f.atkin_lehner_eigenvalue()
Traceback (most recent call last):
...
TypeError: unsupported operand parents for '/': 'Cyclotomic Field of order 52 and degree 24' and 'Cyclotomic Field of order 40 and degree 16'
```



---

Comment by davidloeffler created at 2017-12-01 17:29:01

I've uploaded some fixes to the Atkin-Lehner action code at #24086 which fix this issue; with that patch merged we get

```
sage: f = Newforms(Gamma1(13),3,names='a')[0]
sage: f.atkin_lehner_eigenvalue()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
[...]
ValueError: q + a0*q^2 + (1/7*a0^3 + 2/7*a0^2 - 3/7*a0 - 27/7)*q^3 + (-8/21*a0^3 - 23/21*a0^2 - 88/21*a0 + 16/7)*q^4 + (2/7*a0^3 + 11/7*a0^2 + 29/7*a0 + 9/7)*q^5 + O(q^6) is not an eigenform for W_13
```

which is the **right answer** -- the form is not an eigenform for W_13 and hence the error message is mathematically correct. I propose that this ticket be closed when #24086 is merged.


---

Comment by davidloeffler created at 2017-12-01 17:29:12

Changing status from new to needs_review.


---

Comment by chapoton created at 2018-05-21 08:18:16

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2018-05-21 08:18:16

ok


---

Comment by embray created at 2019-02-26 13:58:00

Resolution: invalid


---

Comment by embray created at 2019-02-26 13:58:00

Presuming these are all correctly reviewed as either duplicate, invalid, or wontfix.
