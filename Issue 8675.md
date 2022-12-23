# Issue 8675: Remove AmbientSpace._constructor and fix consequences

Issue created by migration from https://trac.sagemath.org/ticket/8675

Original creator: novoselt

Original creation time: 2010-04-11 23:31:02

Assignee: AlexGhitza

Currently in schemes/generic/ambient_space we see


```
...
# Derived classes must overload all of the following functions
...
def _constructor(self):
    """
    TEST::

        sage: from sage.schemes.generic.ambient_space import AmbientSpace
        sage: A = AmbientSpace(5, ZZ)
        sage: A._constructor()
        Traceback (most recent call last):
        ...
        NotImplementedError
    """
    raise NotImplementedError
...
# End overloads
...
def base_extend(self, S, check=True):
    """
	...
    """
    if is_CommutativeRing(S):
        R = self.base_ring()
        if S == R:
            return self
        if check:
            if not S.has_coerce_map_from(R):
                raise ValueError, "No natural map from the base ring (=%s) to S (=%s)"%(R, S)
        return self._constructor(self.__n, S, self.variable_names())
    else:
        raise NotImplementedError
...
```


I have the following problems with it:
 * _constructor function has no documentation and a very strange name (because !__init!__ IS a constructor, why do we need another one?)
 * Its usage in the same class calls it with arguments different from specified.
 * With these arguments _constructor still would not quite make sense for toric varieties, where dimension and base ring are not sufficient for creation (and if we do take extra information from self, why do we need to pass dimension explicitly?)
 * Digging further, I have found the following as a consequence of using _constructor:


```
sage: A = AffineSpace(2)
sage: (A^2).variable_names()
('x0', 'x1', 'x0', 'x1')
```


I propose the following solution, making AmbientSpace behave closer to FreeModule's like ZZ^n:
 * Remove _constructor
 * Make base_extend check if extension is possible and call change_ring
 * Make change_ring mandatory for overriding - it should create "exactly the same" ambient space but with a new ring, even if it is not a base extension.
 * Powers of affine ambient spaces use default indexed variables rather than trying to cook up something from variables of the base:


```
sage: A = AffineSpace(2)
sage: (A^2).variable_names()
('x0', 'x1', 'x2', 'x3')
```



---

Comment by novoselt created at 2010-04-11 23:36:55

Changing status from new to needs_review.


---

Attachment


---

Comment by AlexGhitza created at 2010-05-18 12:06:47

Changing status from needs_review to positive_review.


---

Comment by AlexGhitza created at 2010-05-18 12:06:47

Looks good, passes tests, and fixes a number of inconsistencies.


---

Comment by mhansen created at 2010-06-06 07:48:13

Resolution: fixed
