# Issue 341: multiplicative order inconsistency

Issue created by migration from https://trac.sagemath.org/ticket/341

Original creator: was

Original creation time: 2007-04-01 14:46:07

Assignee: somebody


```
On 3/31/07, Pablo De Napoli <> wrote:
> In the process of investigating how rings are defined in sage I've found
> some 
> inconsistencies: the function multiplicative_order is not consistently
> defined
> for all rings.
> 
> Applying this function to a rational 
> integer which is not a unit raises an exception:
> 
> sage: a=ZZ(3)
> sage: a.multiplicative_order()
> ---------------------------------------------------------------------------
> <type 'exceptions.ArithmeticError '>       Traceback (most recent call last)
> 
> /hdc1/pablo.hdc1/sage/sage/<ipython console> in <module>()
> 
> /hdc1/pablo.hdc1/sage/sage/integer.pyx in
> integer.Integer.multiplicative_order()
> 
>  <type 'exceptions.ArithmeticError'>: no power of 3 is a unit
> 
> (and so does for example the ring ComplexDouble)
> 
> However, for complex numbers, things are different: (gives +infinity)
> 
>  b= 2+3*I 
> sage: type(b)
> <type 'sage.rings.complex_number.ComplexNumber'>
> sage: b.multiplicative_order()
> +Infinity
> 
> Which should be the correct behaviour? (I like more the one that answers
> +infinity) 

The correct behavior is +infinity, which is more useful and than an error,
and is technically correct.  
```



---

Comment by mabshoff created at 2007-08-24 23:12:52

I would consider this "worksforme":

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2, Release Date: 2007-08-22                       |
| Type notebook() for the GUI, and license() for information.        |
sage: a=ZZ(3)
sage: a.multiplicative_order()
+Infinity
```



---

Comment by was created at 2007-08-30 00:12:17

Resolution: fixed
