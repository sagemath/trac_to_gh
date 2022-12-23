# Issue 4940: dokchitser L-series at least for number fields claims a pole at zero, though the zeta function has a zero there

Issue created by migration from https://trac.sagemath.org/ticket/4940

Original creator: was

Original creation time: 2009-01-05 08:01:29

Assignee: was


```
sage: K.<a> = NumberField(x^2-2)
sage: z = K.zeta_function()
sage: z(0)
Traceback (most recent call last):
...
ArithmeticError:   ###   user error: L*(s) has a pole at s=0
sage: z(0.0000001)
-4.40686861437826e-8
```


Notice that there is in fact a zero at s=0, not a pole as the ArithmeticError claims.

In fact, it's a theorem that there is a zero at s=0 of order the unit rank of the number field.


---

Comment by robertwb created at 2009-01-23 04:44:34

The function ` L*(s) = sqrt(8)<sup>s/pi</sup>s * gamma(s/2)^2 ` does have a pole at s=0, even though L(s) doesn't. That being said, it shouldn't raise this error. 

I have made some progress on the re-implementation of dokchitser the last couple of days.


---

Comment by chapoton created at 2013-09-21 11:33:36

Changing keywords from "" to "dokchitser".
