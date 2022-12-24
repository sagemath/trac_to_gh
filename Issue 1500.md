# Issue 1500: solve_mod -- implement solving modulo n in sage

archive/issues_001500.json:
```json
{
    "body": "Assignee: was\n\nI've already had two requests just today to solve simple equations modulo n.\n\nHere is code to be pasted into the notebook that can do it:\n\n\n```\ndef solve_mod(eqns, modulus):\n    \"\"\"\n    Return all solutions to an equation or lists of equations modulo \n    the given integer modulus.  Each equation must involve only \n    polynomials in 1 or many variables. \n\n    The solutions are returned as n-tuples, where n is the \n    number of variables appearing anywhere in the given equations.  \n    The variables are in alphabetical order. \n\n\n    INPUT:\n        eqns -- equation or list of equations\n        modulus -- an integer \n\n    EXAMPLES:\n        sage: var('x,y')\n        (x, y)\n        sage: solve_mod([x^2 + 2 == x, x^2 + y == y^2], 14)\n        [(2, 4), (6, 4), (9, 4), (13, 4)]\n\n    Fermat's equation modulo 3 with exponent 5:\n        sage: var('x,y,z')\n        (x, y, z)\n        sage: time solve_mod([x^5 + y^5 == z^5], 3)\n        [(0, 0, 0), (0, 1, 1), (0, 2, 2), (1, 0, 1), (1, 1, 2), (1, 2, 0), (2, 0, 2), (2, 1, 0), (2, 2, 1)]\n        \n    WARNING:\n        Currently this naively enumerates all possible solutions.\n        The interface is good, but the algorithm is horrible if the\n        modulus is at all large!   Sage *does* have the ability to do\n        something much faster in certain cases at least by using\n        the Chinese Remainder Theorem, Groebner basis, linear algebra\n        techniques, etc.  But for a lot of toy problems this function\n        as is might be useful.  At least it establishes an interface.\n    \"\"\"\n    if not isinstance(eqns, (list, tuple)):\n        eqns = [eqns]\n    vars = list(set(sum([list(e.variables()) for e in eqns], [])))\n    vars.sort()\n    n = len(vars)\n    R = Integers(modulus)\n    S = PolynomialRing(R, vars)\n    eqns_mod = [S(eq) if is_SymbolicExpression(eq) else \\\n                  S(eq.lhs() - eq.rhs()) for eq in eqns]\n    ans = []\n    for t in cartesian_product_iterator([R]*len(vars)):\n        is_soln = True\n        for e in eqns_mod:\n            if e(t) != 0:\n                is_soln = False\n                break\n        if is_soln:\n            ans.append(t)\n\n    return ans\n```\n\n\nI'll incorporate this into sage as a patch in a moment.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1500\n\n",
    "created_at": "2007-12-14T00:25:25Z",
    "labels": [
        "algebraic geometry",
        "major",
        "enhancement"
    ],
    "title": "solve_mod -- implement solving modulo n in sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1500",
    "user": "was"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/1500





---

archive/issue_comments_009620.json:
```json
{
    "body": "Attachment [trac-1500.patch](tarball://root/attachments/some-uuid/ticket1500/trac-1500.patch) by was created at 2007-12-14 00:38:24",
    "created_at": "2007-12-14T00:38:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1500#issuecomment-9620",
    "user": "was"
}
```

Attachment [trac-1500.patch](tarball://root/attachments/some-uuid/ticket1500/trac-1500.patch) by was created at 2007-12-14 00:38:24



---

archive/issue_comments_009621.json:
```json
{
    "body": "This seems to be a good implementation for the toy cryptanalysis i want to play around with.\n\n\n```\na,b = var('a,b')\nsolve_mod([4*a + b == 17,19*a + b == 3],26)\n///\n[(6, 19)]\n```\n\n\nI like the interface a little better than \"Solve[{x^2  == 1, 4*x  == 2, Modulus==10}, x, Mode->Modular].\"",
    "created_at": "2007-12-14T01:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1500#issuecomment-9621",
    "user": "TimothyClemans"
}
```

This seems to be a good implementation for the toy cryptanalysis i want to play around with.


```
a,b = var('a,b')
solve_mod([4*a + b == 17,19*a + b == 3],26)
///
[(6, 19)]
```


I like the interface a little better than "Solve[{x^2  == 1, 4*x  == 2, Modulus==10}, x, Mode->Modular]."



---

archive/issue_comments_009622.json:
```json
{
    "body": "Looks good to me, is doctested, doesn't touch any existing code, so merge it.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-14T04:21:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1500#issuecomment-9622",
    "user": "mabshoff"
}
```

Looks good to me, is doctested, doesn't touch any existing code, so merge it.

Cheers,

Michael



---

archive/issue_comments_009623.json:
```json
{
    "body": "Merged in 2.9.alpha7.",
    "created_at": "2007-12-14T05:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1500#issuecomment-9623",
    "user": "mabshoff"
}
```

Merged in 2.9.alpha7.



---

archive/issue_comments_009624.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-14T05:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1500",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1500#issuecomment-9624",
    "user": "mabshoff"
}
```

Resolution: fixed
