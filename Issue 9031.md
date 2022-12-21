# Issue 9031: algebraic_dependency with algorithm=fpLLL

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-05-24 07:53:30

Assignee: AlexGhitza

The algebraic_dependency function currently calls Pari/GP.
For big problems fpLLL should be faster, thus there should be
an option to call fpLLL instead.


---

Comment by was created at 2014-11-06 23:07:57

Sage's command does call fpLLL.  This ticket should be closed. 

Type 

```
sage: algdep??
```

to see...


---

Comment by zimmerma created at 2014-11-07 06:35:42

>  Sage's command does call fpLLL. This ticket should be closed. 

ok, but the documentation should be fixed:

```
   Note that "algebraic_dependency" is a synonym for "algdep".
sage: a=sqrt(2)+sqrt(3);algebraic_dependency(a,4)
---------------------------------------------------------------------------
NameError                                Traceback (most recent call last)
<ipython-input-10-0409cbaa7642> in <module>()
----> 1 a=sqrt(Integer(2))+sqrt(Integer(3));algebraic_dependency(a,Integer(4))

NameError: name 'algebraic_dependency' is not defined
```

and:

```
   You can specify the number of known bits or digits of z with
   "known_bits=k" or "known_digits=k". PARI is then told to compute
   the result using 0.8k of these bits/digits.
```

If fpLLL is used now, `PARI` should be removed or replaced here.

Paul


---

Comment by was created at 2014-11-07 06:40:54

Early today, I coincidentally opened a ticket about algebraic_dependency vanishing: http://trac.sagemath.org/ticket/17302


---

Comment by zimmerma created at 2014-11-07 07:47:51

ok, then I agree we should close this one. I will add the `known_bits` issue to the other ticket. What should one do to close?

Paul


---

Comment by vbraun created at 2014-11-07 14:56:25

Resolution: invalid


---

Comment by vbraun created at 2014-11-07 14:56:25

You are supposed to set milestone to duplicate/invalid/wontfix and then positive review...
