# Issue 1500: solve_mod -- implement solving modulo n in sage

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-14 00:25:25

Assignee: was

I've already had two requests just today to solve simple equations modulo n.

Here is code to be pasted into the notebook that can do it:


```
def solve_mod(eqns, modulus):
    """
    Return all solutions to an equation or lists of equations modulo 
    the given integer modulus.  Each equation must involve only 
    polynomials in 1 or many variables. 

    The solutions are returned as n-tuples, where n is the 
    number of variables appearing anywhere in the given equations.  
    The variables are in alphabetical order. 


    INPUT:
        eqns -- equation or list of equations
        modulus -- an integer 

    EXAMPLES:
        sage: var('x,y')
        (x, y)
        sage: solve_mod([x^2 + 2 == x, x^2 + y == y^2], 14)
        [(2, 4), (6, 4), (9, 4), (13, 4)]

    Fermat's equation modulo 3 with exponent 5:
        sage: var('x,y,z')
        (x, y, z)
        sage: time solve_mod([x^5 + y^5 == z^5], 3)
        [(0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 1), (1, 1, 2), (1, 2, 0), (2, 0, 2), (2, 1, 0), (2, 2, 1)]
        
    WARNING:
        Currently this naively enumerates all possible solutions.
        The interface is good, but the algorithm is horrible if the
        modulus is at all large!   Sage *does* have the ability to do
        something much faster in certain cases at least by using
        the Chinese Remainder Theorem, Groebner basis, linear algebra
        techniques, etc.  But for a lot of toy problems this function
        as is might be useful.  At least it establishes an interface.
    """
    if not isinstance(eqns, (list, tuple)):
        eqns = [eqns]
    vars = list(set(sum([list(e.variables()) for e in eqns], [])))
    vars.sort()
    n = len(vars)
    R = Integers(modulus)
    S = PolynomialRing(R, vars)
    eqns_mod = [S(eq) if is_SymbolicExpression(eq) else \
                  S(eq.lhs() - eq.rhs()) for eq in eqns]
    ans = []
    for t in cartesian_product_iterator([R]*len(vars)):
        is_soln = True
        for e in eqns_mod:
            if e(t) != 0:
                is_soln = False
                break
        if is_soln:
            ans.append(t)

    return ans
```


I'll incorporate this into sage as a patch in a moment.


---

Attachment


---

Comment by TimothyClemans created at 2007-12-14 01:06:42

This seems to be a good implementation for the toy cryptanalysis i want to play around with.


```
a,b = var('a,b')
solve_mod([4*a + b == 17,19*a + b == 3],26)
///
[(6, 19)]
```


I like the interface a little better than "Solve[{x^2  == 1, 4*x  == 2, Modulus==10}, x, Mode->Modular]."


---

Comment by mabshoff created at 2007-12-14 04:21:07

Looks good to me, is doctested, doesn't touch any existing code, so merge it.

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-14 05:09:28

Merged in 2.9.alpha7.


---

Comment by mabshoff created at 2007-12-14 05:09:28

Resolution: fixed
