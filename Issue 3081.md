# Issue 3081: [with patch; needs review] Added support for Kloosterman sums

Issue created by migration from Trac.

Original creator: kkilger

Original creation time: 2008-05-02 15:05:31

Assignee: mabshoff

CC:  ncalexan

This (nearly trivial patch) adds support for exact and numerical evaluation of "twisted" Kloosterman sums. This generalizes Gauss sums, Salie sums and normal Kloosterman sums. 



---

Comment by mabshoff created at 2008-05-02 15:10:39

Changing assignee from mabshoff to was.


---

Comment by mabshoff created at 2008-05-02 15:10:39

Hi Kilian,

Aside from the fact that this is a number theory ticket everything looks good. Hopefully somebody will review this patch shortly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-05-02 15:10:39

Changing component from Cygwin to number theory.


---

Attachment


---

Comment by wdj created at 2008-05-02 15:23:06

This sounds extremely cool!
What is based on? I can't get it to apply on either 3.0 or 3.0.1.alpha1.


---

Comment by was created at 2008-05-02 15:27:40

QUESTION:

You've rewritten some of the functions to be more general, e.g., this

```
707	 	            z *= zeta 
708	 	            g += phi(c)*z 
```

becomes this:

```
763	                z = zeta ** (a*e + b*(e**(-1))) 
764	                g += phi(self.__call__(c))*z        
```


What impact does this have on performance in the original case of computing Gauss
sums?  Is it slower or faster or the same?

Also, why use 

```
self.__call__(c)
```

instead of 

```
self(c)
```

?


---

Comment by kkilger created at 2008-05-02 15:50:08

It computes the modular inverse every time. So it should be somewhat slower as before. I read that there is an ongoing discussion between code duplication and speed ...  

I wanted to use this to introduce Poincare series in SAGE (and compute their Fourier coefficients) but this is far to slow. I am planning to reimplement the numerical stuff in C/Cython next week (or this weekend). 

Question: Why are Dirichlet characters in modular/dirichlet.py? Is it for historical reasons?

Regards,
Kilian.


---

Comment by kkilger created at 2008-05-02 15:54:37

P.S.: ... oh. I will change self.__call__(c) to self(c). I have to get used to python ;-).


---

Comment by kkilger created at 2008-05-02 15:59:29

P.P.S: It should be based on 3.0 ...


---

Comment by was created at 2008-05-02 16:08:11

> Question: Why are Dirichlet characters in modular/dirichlet.py? Is it for historical reasons?

Yep, Historical reasons.  Where would you want to put it.

> It computes the modular inverse every time. So it should be somewhat 
> slower as before. I read that there is an ongoing discussion between 
> code duplication and speed ...

Worrisome, but like you say below it is too slow in the first place. 

> I wanted to use this to introduce Poincare series in SAGE (and compute their 
> Fourier coefficients) but this is far to slow. I am planning to reimplement 
> the numerical stuff in C/Cython next week (or this weekend). 

Excellent!

 -- William


---

Comment by kkilger created at 2008-05-02 17:25:15

> Yep, Historical reasons. Where would you want to put it.

Are there some other character groups implemented? Perhaps it should go to the dual groups?

Another question:

If I compute for example the Kloosterman sum K(2,4,13) in Magma it returns:
2*zeta_13^10 + 2*zeta_13^9 + 2*zeta_13^7 + 2*zeta_13^6 + 2*zeta_13^4 + 2*zeta_13^3

If I compute it with SAGE it returns:
2*zeta156^40 - 2*zeta156^34 + 2*zeta156^28 - 2*zeta156^24 + 2*zeta156^18 - 2*zeta156^14 - 2*zeta156^12 + 2*zeta156^8 - 2*zeta156^2 - 2

This is the same number but it is much more reduced in MAGMA. The corresponding MAGMA code is:

> Kloosterman := func< u, v, n |
>     &+[z^(IntegerRing() ! (u*x+v*x^-1)) : x in F | IsUnit(x) ]
>         where z is RootOfUnity(n, CyclotomicField(n))
>         where F is ResidueClassRing(n) >;

Kilian.


---

Comment by kkilger created at 2008-05-02 17:28:19

Again ... I forgot the code block

Magma-Number:


```
2*zeta_13^10 + 2*zeta_13^9 + 2*zeta_13^7 + 2*zeta_13^6 + 2*zeta_13^4 + 2*zeta_13^3
```


SAGE-Number:

```
2*zeta156^40 - 2*zeta156^34 + 2*zeta156^28 - 2*zeta156^24 + 2*zeta156^18 - 2*zeta156^14 - 2*zeta156^12 + 2*zeta156^8 - 2*zeta156^2 - 2
```


Magma-Code:

```
>  Kloosterman := func< u, v, n |
>      &+[z^(IntegerRing() ! (u*x+v*x^-1)) : x in F | IsUnit(x) ]
>          where z is RootOfUnity(n, CyclotomicField(n))
>          where F is ResidueClassRing(n) >;
```



---

Comment by craigcitro created at 2008-06-15 21:40:36

Changing keywords from "" to "editor_craigcitro".


---

Comment by mabshoff created at 2008-09-25 00:18:39

Nick,

anything going on here?

Cheers,

Michael


---

Comment by was created at 2008-10-30 18:07:15

From Nick:

```
I seem to remember thinking this code was mildly flawed (easily fixed) and not fast.  But please pass it on to someone more tuned in.
```



---

Comment by was created at 2008-11-28 04:39:42

REFEREE REPORT:

This patch needs work.  Just totally delete the first part of the patch that
replaces lines 636-652 by nothing and calls kloosterman_sum, since kloosterman_sum is much slower.  Just leave the code like it used to be.

Otherwise, i think the code is good to have included in sage.    In particular, the issue the author raises about the representation of a certain output and a root of unity is interesting, but not something to stop this patch from going in.

So I think with some very obvious simple work, this can easily be included.  Just delete the part that will slow down the gauss_sum.


---

Attachment

Repaired patch


---

Comment by kkilger created at 2009-04-11 14:25:01

Sorry ... a bit late but what comes late is better than everything what comes never :-)


---

Comment by craigcitro created at 2009-04-11 15:55:56

Just changing the title so this gets noticed.


---

Comment by mabshoff created at 2009-04-12 20:53:10

Resolution: fixed


---

Comment by mabshoff created at 2009-04-12 20:53:10

Merged kloosterman.patch in Sage 3.4.1.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-18 08:20:15

I just notices that this patch uses tabs instead of spaces. In Sage we do not use tabs but spaces, so please adjust your editor.

Cheers,

Michael
