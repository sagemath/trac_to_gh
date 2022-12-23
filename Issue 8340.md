# Issue 8340: add a lift method to elements of the residue class field

Issue created by migration from https://trac.sagemath.org/ticket/8340

Original creator: was

Original creation time: 2010-02-23 22:46:40

Assignee: robertwb

CC:  roed

Make this work:

```
sage: var('x')
sage: K.<a> = NumberField(x^3 + x + 1)
sage: P = K.factor(11)[0][0]; P
Fractional ideal (a^2 + 2*a + 5)
sage: k = P.residue_field(); k
Residue field in abar of Fractional ideal (a^2 + 2*a + 5)
sage: k.degree()
2
sage: alpha = k.random_element(); alpha
3*abar + 6
sage: k.lift(alpha)
3*a + 6
sage: K(alpha)
Traceback (most recent call last):
...
TypeError: <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'>
sage: alpha.lift()
Traceback (most recent call last):
...
AttributeError: 'sage.rings.finite_field_givaro.FiniteField_givaroElement' object has no attribute 'lift'
```



---

Comment by roed created at 2010-02-23 23:08:57

Currently, elements of residue fields are the same class as elements of any other finite field (IntegerMod_gmp, FiniteFieldElement_givaro, etc).  Only the parent records the fact that they're actually in a residue field.  We can change the lift method on all such elements to call the parent's lift method, but that's going to impose a performance penalty on every IntegerMod's lift.

I think the right solution is as follows.  I want to make a common base class FiniteRingElement that all of the finite field elements and integermods will inherit from (currently their common superclass is CommutativeRingElement).  This class can then have a Cache object that will serve the purpose of NativeIntStruct, Cache_givaro and Cache_ntl_gf2e (once FiniteField_ntl_gf2e is converted to Python).  Each subclass will have a corresponding subclass of Cache defined.

On the common Cache we can hang things like _is_field and _use_parent_lift.  Then elements can have C access to these attributes.

I tried changing the superclasses of IntegerMod and FiniteFieldElement_givaro to a common one, but got some strange error about Givaro not being able to find the sub method.  If someone else wants to do it I'd be happy.  :-)
