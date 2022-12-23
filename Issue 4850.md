# Issue 4850: bug in power_mod

archive/issues_004850.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.1.4, Release Date: 2008-10-16                       |\n| Type notebook() for the GUI, and license() for information.        |\nsage: power_mod(11,1,7)\n11\nsage: mod(11^1,7)\n4\nsage: # Hmmm...???\nsage:\n\n...al\n```\n\n\nNote above that power_mod(11,1,7) should return 4.  The fix is to look at the *pure python* code that defines power_mod in rings/arith.py and:\n\n1. change it to use some much more intelligent compiled code, i.e., either the powermod or powermod_ui methods when the first input coerces to ZZ, and\n\n2. when a doesn't coerce to ZZ, just revert to the existing Python code, but make sure to throw in an `%m` somewhere before returning the answer. \n\n3. Add a doctest like this that illustrates non-integer input for the first argument to power_mod:\n\n```\nsage: power_mod(3*x, 10, 7)\n4*x^10\n```\n\n\n4. There is an inconsistency in that the Integer method for power_mod is called \"powermod\" instead of \"power_mod\".  I think the Integer method should be changed, for consistency with the naming conventions used throughout sage (namely, be generous with underscores). \n\nIssue created by migration from https://trac.sagemath.org/ticket/4850\n\n",
    "created_at": "2008-12-22T04:21:59Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in power_mod",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4850",
    "user": "was"
}
```
Assignee: somebody


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.1.4, Release Date: 2008-10-16                       |
| Type notebook() for the GUI, and license() for information.        |
sage: power_mod(11,1,7)
11
sage: mod(11^1,7)
4
sage: # Hmmm...???
sage:

...al
```


Note above that power_mod(11,1,7) should return 4.  The fix is to look at the *pure python* code that defines power_mod in rings/arith.py and:

1. change it to use some much more intelligent compiled code, i.e., either the powermod or powermod_ui methods when the first input coerces to ZZ, and

2. when a doesn't coerce to ZZ, just revert to the existing Python code, but make sure to throw in an `%m` somewhere before returning the answer. 

3. Add a doctest like this that illustrates non-integer input for the first argument to power_mod:

```
sage: power_mod(3*x, 10, 7)
4*x^10
```


4. There is an inconsistency in that the Integer method for power_mod is called "powermod" instead of "power_mod".  I think the Integer method should be changed, for consistency with the naming conventions used throughout sage (namely, be generous with underscores). 

Issue created by migration from https://trac.sagemath.org/ticket/4850





---

archive/issue_comments_036774.json:
```json
{
    "body": "I suggest we remove the `power_mod` function completely, since python already supports this.\n\n\n```\nsage: pow?\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in function pow>\nNamespace:      Python builtin\nDocstring:\n    pow(x, y[, z]) -> number\n    \n    With two arguments, equivalent to x**y.  With three arguments,\n    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).\nClass Docstring:\n    <attribute '__doc__' of 'builtin_function_or_method' objects>\n```\n\n\nThis would call the `__pow__` method of the function in question with the right arguments, so we can handle the modulo powering operation in the right place. Recall that the signature of the `__pow__` method is actually:\n\n\n```\n__pow__(self, other[, modulus]).\n```\n\n\n\nSo the objective of this ticket should be changed to:\n* let `sage.structure.element.generic_power_c` handle modulus arguments\n* change the `__pow__` methods in sage.structure.element to accept and pass on the third argument\n* deprecate `sage.rings.arith.power_mod`\n* deprecate `Integer.powermod`\n\nThoughts?",
    "created_at": "2008-12-23T12:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4850#issuecomment-36774",
    "user": "burcin"
}
```

I suggest we remove the `power_mod` function completely, since python already supports this.


```
sage: pow?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function pow>
Namespace:      Python builtin
Docstring:
    pow(x, y[, z]) -> number
    
    With two arguments, equivalent to x**y.  With three arguments,
    equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
Class Docstring:
    <attribute '__doc__' of 'builtin_function_or_method' objects>
```


This would call the `__pow__` method of the function in question with the right arguments, so we can handle the modulo powering operation in the right place. Recall that the signature of the `__pow__` method is actually:


```
__pow__(self, other[, modulus]).
```



So the objective of this ticket should be changed to:
* let `sage.structure.element.generic_power_c` handle modulus arguments
* change the `__pow__` methods in sage.structure.element to accept and pass on the third argument
* deprecate `sage.rings.arith.power_mod`
* deprecate `Integer.powermod`

Thoughts?



---

archive/issue_comments_036775.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-24T01:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4850#issuecomment-36775",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_036776.json:
```json
{
    "body": "This is a humble patch that solves the problem of the ticket. I'm not addressing burcin's far more difficult enhancement of introducing a whole arithmetic architecture.  I'm also not addressing the powermod versus power_mod, since I don't want to break existing code by third party people.",
    "created_at": "2009-01-24T01:14:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4850#issuecomment-36776",
    "user": "was"
}
```

This is a humble patch that solves the problem of the ticket. I'm not addressing burcin's far more difficult enhancement of introducing a whole arithmetic architecture.  I'm also not addressing the powermod versus power_mod, since I don't want to break existing code by third party people.



---

archive/issue_comments_036777.json:
```json
{
    "body": "Given patch fixes the reported problem, and it's really simple.\n\nI will open a sage-wishlist issue for removing power_mod.",
    "created_at": "2009-01-24T01:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4850#issuecomment-36777",
    "user": "burcin"
}
```

Given patch fixes the reported problem, and it's really simple.

I will open a sage-wishlist issue for removing power_mod.



---

archive/issue_comments_036778.json:
```json
{
    "body": "Merged in Sage 3.3.alpha2",
    "created_at": "2009-01-24T14:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4850#issuecomment-36778",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha2



---

archive/issue_comments_036779.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-24T14:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4850",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4850#issuecomment-36779",
    "user": "mabshoff"
}
```

Resolution: fixed
