# Issue 5082: remove power_mod method

archive/issues_005082.json:
```json
{
    "body": "Assignee: somebody\n\nThe `power_mod` function is redundant, since python already supports this.\n \n {{{\n sage: pow?\n Type:           builtin_function_or_method\n Base Class:     <type 'builtin_function_or_method'>\n String Form:    <built-in function pow>\n Namespace:      Python builtin\n Docstring:\n     pow(x, y[, z]) -> number\n     \n     With two arguments, equivalent to x**y.  With three arguments,\n     equivalent to (x**y) % z, but may be more efficient (e.g. for longs).\n Class Docstring:\n     <attribute '__doc__' of 'builtin_function_or_method' objects>\n }}}\n \n This would call the `__pow__` method of the function in question with the right arguments, so we can handle the modulo powering operation in the right place. Recall that the signature of the `__pow__` method is actually:\n \n {{{\n __pow__(self, other[, modulus]).\n }}}\n \n \n So the objective of this ticket should be changed to:\n* let `sage.structure.element.generic_power_c` handle modulus arguments\n* change the `__pow__` methods in sage.structure.element to accept and pass on the third argument\n* deprecate `sage.rings.arith.power_mod`\n* deprecate `Integer.powermod`\n\nIssue created by migration from https://trac.sagemath.org/ticket/5082\n\n",
    "created_at": "2009-01-24T01:48:01Z",
    "labels": [
        "component: basic arithmetic",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "remove power_mod method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5082",
    "user": "https://github.com/burcin"
}
```
Assignee: somebody

The `power_mod` function is redundant, since python already supports this.
 
 {{{
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
 }}}
 
 This would call the `__pow__` method of the function in question with the right arguments, so we can handle the modulo powering operation in the right place. Recall that the signature of the `__pow__` method is actually:
 
 {{{
 __pow__(self, other[, modulus]).
 }}}
 
 
 So the objective of this ticket should be changed to:
* let `sage.structure.element.generic_power_c` handle modulus arguments
* change the `__pow__` methods in sage.structure.element to accept and pass on the third argument
* deprecate `sage.rings.arith.power_mod`
* deprecate `Integer.powermod`

Issue created by migration from https://trac.sagemath.org/ticket/5082


