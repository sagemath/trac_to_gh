# Issue 4850: bug in power_mod

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-12-22 04:21:59

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


---

Comment by burcin created at 2008-12-23 12:07:42

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

Attachment


---

Comment by was created at 2009-01-24 01:14:03

This is a humble patch that solves the problem of the ticket. I'm not addressing burcin's far more difficult enhancement of introducing a whole arithmetic architecture.  I'm also not addressing the powermod versus power_mod, since I don't want to break existing code by third party people.


---

Comment by burcin created at 2009-01-24 01:43:28

Given patch fixes the reported problem, and it's really simple.

I will open a sage-wishlist issue for removing power_mod.


---

Comment by mabshoff created at 2009-01-24 14:48:13

Merged in Sage 3.3.alpha2


---

Comment by mabshoff created at 2009-01-24 14:48:13

Resolution: fixed
