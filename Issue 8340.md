# Issue 8340: add a lift method to elements of the residue class field

archive/issues_008340.json:
```json
{
    "body": "Assignee: robertwb\n\nCC:  roed\n\nMake this work:\n\n```\nsage: var('x')\nsage: K.<a> = NumberField(x^3 + x + 1)\nsage: P = K.factor(11)[0][0]; P\nFractional ideal (a^2 + 2*a + 5)\nsage: k = P.residue_field(); k\nResidue field in abar of Fractional ideal (a^2 + 2*a + 5)\nsage: k.degree()\n2\nsage: alpha = k.random_element(); alpha\n3*abar + 6\nsage: k.lift(alpha)\n3*a + 6\nsage: K(alpha)\nTraceback (most recent call last):\n...\nTypeError: <type 'sage.rings.finite_field_givaro.FiniteField_givaroElement'>\nsage: alpha.lift()\nTraceback (most recent call last):\n...\nAttributeError: 'sage.rings.finite_field_givaro.FiniteField_givaroElement' object has no attribute 'lift'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8340\n\n",
    "created_at": "2010-02-23T22:46:40Z",
    "labels": [
        "number fields",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "add a lift method to elements of the residue class field",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8340",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/8340





---

archive/issue_comments_074455.json:
```json
{
    "body": "Currently, elements of residue fields are the same class as elements of any other finite field (IntegerMod_gmp, FiniteFieldElement_givaro, etc).  Only the parent records the fact that they're actually in a residue field.  We can change the lift method on all such elements to call the parent's lift method, but that's going to impose a performance penalty on every IntegerMod's lift.\n\nI think the right solution is as follows.  I want to make a common base class FiniteRingElement that all of the finite field elements and integermods will inherit from (currently their common superclass is CommutativeRingElement).  This class can then have a Cache object that will serve the purpose of NativeIntStruct, Cache_givaro and Cache_ntl_gf2e (once FiniteField_ntl_gf2e is converted to Python).  Each subclass will have a corresponding subclass of Cache defined.\n\nOn the common Cache we can hang things like _is_field and _use_parent_lift.  Then elements can have C access to these attributes.\n\nI tried changing the superclasses of IntegerMod and FiniteFieldElement_givaro to a common one, but got some strange error about Givaro not being able to find the sub method.  If someone else wants to do it I'd be happy.  :-)",
    "created_at": "2010-02-23T23:08:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8340#issuecomment-74455",
    "user": "roed"
}
```

Currently, elements of residue fields are the same class as elements of any other finite field (IntegerMod_gmp, FiniteFieldElement_givaro, etc).  Only the parent records the fact that they're actually in a residue field.  We can change the lift method on all such elements to call the parent's lift method, but that's going to impose a performance penalty on every IntegerMod's lift.

I think the right solution is as follows.  I want to make a common base class FiniteRingElement that all of the finite field elements and integermods will inherit from (currently their common superclass is CommutativeRingElement).  This class can then have a Cache object that will serve the purpose of NativeIntStruct, Cache_givaro and Cache_ntl_gf2e (once FiniteField_ntl_gf2e is converted to Python).  Each subclass will have a corresponding subclass of Cache defined.

On the common Cache we can hang things like _is_field and _use_parent_lift.  Then elements can have C access to these attributes.

I tried changing the superclasses of IntegerMod and FiniteFieldElement_givaro to a common one, but got some strange error about Givaro not being able to find the sub method.  If someone else wants to do it I'd be happy.  :-)
