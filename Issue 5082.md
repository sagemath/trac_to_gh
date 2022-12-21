# Issue 5082: remove power_mod method

Issue created by migration from Trac.

Original creator: burcin

Original creation time: 2009-01-24 01:48:01

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
