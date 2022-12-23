# Issue 8040: given that m,n are optional inputs to CRT(a,b,m,n), given a,b mod m,n should work

Issue created by migration from https://trac.sagemath.org/ticket/8040

Original creator: was

Original creation time: 2010-01-22 15:24:37

Assignee: AlexGhitza

I think this should work:

```
sage: CRT(Mod(3,19), Mod(5, 13))
...
ValueError: arguments a and b must be coprime
```


This fix is to check the gcd precondition more carefully. 


---

Comment by saiharsh created at 2018-03-16 16:55:17

I have tried 


```
sage: CRT(Mod(3,19), Mod(5, 13))
```


The error is because of the return type of Mod is sage.rings.finite_rings.integer_mod.IntegerMod_int, not integer which is desire. 

if you try this


```
sage: CRT(int(Mod(3,19)), int(Mod(5, 13)))
```

it's working, is my suggestion right? or am I missing something.

I used Sage version 8.1, which was released on 2017-12-07.

Thanks,\\
Harsh
