# Issue 4728: .roots() is inconsistent between polynomials and symbolic polynomials

archive/issues_004728.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: roots symbolic polynomial\n\nThe lack of multiplicities= keyword and the failure to try to convert to a polynomial first irritates me.  Actually, the default symbolic 'x' irritates me most of all, but I don't intend to open a ticket for that.\n\n\n```\nsage: (var('x') - 1).roots()\n[(1, 1)]\nsage: (var('x') - 1).roots(QQbar)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2816, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2790, 0))\n\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in roots(self, x, explicit_solutions)\n   3077         if x is None:\n   3078             x = self.default_variable()\n-> 3079         S, mul = self.solve(x, multiplicities=True, explicit_solutions=explicit_solutions)\n   3080         if len(mul) == 0 and explicit_solutions:\n   3081             raise RuntimeError, \"no explicit roots found\"\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in solve(self, x, multiplicities, explicit_solutions)\n   3103         \"\"\"\n   3104         x = var(x)\n-> 3105         return (self == 0).solve(x, multiplicities=multiplicities, explicit_solutions=explicit_solutions)\n   3106 \n   3107     def find_root(self, a, b, var=None, xtol=10e-13, rtol=4.5e-16, maxiter=100, full_output=False):\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/equations.pyc in solve(self, x, multiplicities, solution_dict, explicit_solutions)\n   1021         from sage.calculus.calculus import SymbolicVariable, SymbolicFunction, SymbolicFunctionEvaluation\n   1022         if not isinstance(x,(SymbolicVariable,SymbolicFunction,SymbolicFunctionEvaluation)):\n-> 1023             raise TypeError, \"%s is not a valid variable.\"%x\n   1024 \n   1025         m = self._maxima_()\n\nTypeError: not all arguments converted during string formatting\nsage: (var('x')^2 - 1).roots(CC)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2816, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (2791, 0))\n\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (592, 0))\n\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in roots(self, x, explicit_solutions)\n   3077         if x is None:\n   3078             x = self.default_variable()\n-> 3079         S, mul = self.solve(x, multiplicities=True, explicit_solutions=explicit_solutions)\n   3080         if len(mul) == 0 and explicit_solutions:\n   3081             raise RuntimeError, \"no explicit roots found\"\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in solve(self, x, multiplicities, explicit_solutions)\n   3102             [z == e^(2*I*pi/5), z == e^(4*I*pi/5), z == e^(-(4*I*pi/5)), z == e^(-(2*I*pi/5)), z == 1]        \n   3103         \"\"\"\n-> 3104         x = var(x)\n   3105         return (self == 0).solve(x, multiplicities=multiplicities, explicit_solutions=explicit_solutions)\n   3106 \n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in var(s, create)\n   5467         return tuple([var(x.strip()) for x in s.split(',')])\n   5468     elif ' ' in s:\n-> 5469         return tuple([var(x.strip()) for x in s.split()])\n   5470     try:\n   5471         v = _vars[s]\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in var(s, create)\n   5476             raise ValueError, \"the variable '%s' has not been defined\"%var\n   5477         pass\n-> 5478     v = SymbolicVariable(s)\n   5479     _vars[s] = v\n   5480     _syms[s] = v\n\n/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __init__(self, name)\n   5301             raise ValueError, \"variable name must be nonempty\"\n   5302         elif not is_python_identifier.match(name):\n-> 5303             raise ValueError, \"variable name is not a valid Python identifier\"\n   5304 \n   5305     def __hash__(self):\n\nValueError: variable name is not a valid Python identifier\nsage: (var('x')^2 - 1).roots(CC, multiplicities=False)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()\n----> 1 \n      2 \n      3 \n      4 \n      5 \n\nTypeError: roots() got an unexpected keyword argument 'multiplicities'\nsage: (QQ['x'].0^2 - 1).roots(CC, multiplicities=False)\n[-1.00000000000000, 1.00000000000000]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4728\n\n",
    "created_at": "2008-12-06T19:55:25Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": ".roots() is inconsistent between polynomials and symbolic polynomials",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4728",
    "user": "https://github.com/ncalexan"
}
```
Assignee: @malb

Keywords: roots symbolic polynomial

The lack of multiplicities= keyword and the failure to try to convert to a polynomial first irritates me.  Actually, the default symbolic 'x' irritates me most of all, but I don't intend to open a ticket for that.


```
sage: (var('x') - 1).roots()
[(1, 1)]
sage: (var('x') - 1).roots(QQbar)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2816, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2790, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in roots(self, x, explicit_solutions)
   3077         if x is None:
   3078             x = self.default_variable()
-> 3079         S, mul = self.solve(x, multiplicities=True, explicit_solutions=explicit_solutions)
   3080         if len(mul) == 0 and explicit_solutions:
   3081             raise RuntimeError, "no explicit roots found"

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in solve(self, x, multiplicities, explicit_solutions)
   3103         """
   3104         x = var(x)
-> 3105         return (self == 0).solve(x, multiplicities=multiplicities, explicit_solutions=explicit_solutions)
   3106 
   3107     def find_root(self, a, b, var=None, xtol=10e-13, rtol=4.5e-16, maxiter=100, full_output=False):

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/equations.pyc in solve(self, x, multiplicities, solution_dict, explicit_solutions)
   1021         from sage.calculus.calculus import SymbolicVariable, SymbolicFunction, SymbolicFunctionEvaluation
   1022         if not isinstance(x,(SymbolicVariable,SymbolicFunction,SymbolicFunctionEvaluation)):
-> 1023             raise TypeError, "%s is not a valid variable."%x
   1024 
   1025         m = self._maxima_()

TypeError: not all arguments converted during string formatting
sage: (var('x')^2 - 1).roots(CC)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2816, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (2791, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (592, 0))

---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in roots(self, x, explicit_solutions)
   3077         if x is None:
   3078             x = self.default_variable()
-> 3079         S, mul = self.solve(x, multiplicities=True, explicit_solutions=explicit_solutions)
   3080         if len(mul) == 0 and explicit_solutions:
   3081             raise RuntimeError, "no explicit roots found"

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in solve(self, x, multiplicities, explicit_solutions)
   3102             [z == e^(2*I*pi/5), z == e^(4*I*pi/5), z == e^(-(4*I*pi/5)), z == e^(-(2*I*pi/5)), z == 1]        
   3103         """
-> 3104         x = var(x)
   3105         return (self == 0).solve(x, multiplicities=multiplicities, explicit_solutions=explicit_solutions)
   3106 

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in var(s, create)
   5467         return tuple([var(x.strip()) for x in s.split(',')])
   5468     elif ' ' in s:
-> 5469         return tuple([var(x.strip()) for x in s.split()])
   5470     try:
   5471         v = _vars[s]

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in var(s, create)
   5476             raise ValueError, "the variable '%s' has not been defined"%var
   5477         pass
-> 5478     v = SymbolicVariable(s)
   5479     _vars[s] = v
   5480     _syms[s] = v

/Users/ncalexan/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/calculus/calculus.pyc in __init__(self, name)
   5301             raise ValueError, "variable name must be nonempty"
   5302         elif not is_python_identifier.match(name):
-> 5303             raise ValueError, "variable name is not a valid Python identifier"
   5304 
   5305     def __hash__(self):

ValueError: variable name is not a valid Python identifier
sage: (var('x')^2 - 1).roots(CC, multiplicities=False)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/ncalexan/.sage/temp/pv139196.reshsg.uci.edu/96844/_Users_ncalexan__sage_init_sage_0.py in <module>()
----> 1 
      2 
      3 
      4 
      5 

TypeError: roots() got an unexpected keyword argument 'multiplicities'
sage: (QQ['x'].0^2 - 1).roots(CC, multiplicities=False)
[-1.00000000000000, 1.00000000000000]
```


Issue created by migration from https://trac.sagemath.org/ticket/4728





---

archive/issue_comments_035622.json:
```json
{
    "body": "It's not perfect, but it's more in line with the polynomial .roots() method.\n\nMy least favourite thing is that giving one keyword argument must remain the variable, to maintain backwards compatability.",
    "created_at": "2009-01-22T09:47:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4728#issuecomment-35622",
    "user": "https://github.com/ncalexan"
}
```

It's not perfect, but it's more in line with the polynomial .roots() method.

My least favourite thing is that giving one keyword argument must remain the variable, to maintain backwards compatability.



---

archive/issue_comments_035623.json:
```json
{
    "body": "Attachment [trac_4728-symbolic-roots.patch](tarball://root/attachments/some-uuid/ticket4728/trac_4728-symbolic-roots.patch) by @ncalexan created at 2009-01-22 09:55:33",
    "created_at": "2009-01-22T09:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4728#issuecomment-35623",
    "user": "https://github.com/ncalexan"
}
```

Attachment [trac_4728-symbolic-roots.patch](tarball://root/attachments/some-uuid/ticket4728/trac_4728-symbolic-roots.patch) by @ncalexan created at 2009-01-22 09:55:33



---

archive/issue_comments_035624.json:
```json
{
    "body": "The only issue I see is:\n\n\n```\nmultiplicities -- bool (default True); when True, return \nmultiplicities \n```\n\n\nshould be\n\n\n```\nmultiplicities -- bool (default True); when True, return \n                  multiplicities \n```\n",
    "created_at": "2009-01-22T19:44:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4728#issuecomment-35624",
    "user": "https://github.com/malb"
}
```

The only issue I see is:


```
multiplicities -- bool (default True); when True, return 
multiplicities 
```


should be


```
multiplicities -- bool (default True); when True, return 
                  multiplicities 
```




---

archive/issue_comments_035625.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-01-28T17:54:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4728#issuecomment-35625",
    "user": "https://github.com/jasongrout"
}
```

apply on top of previous patch



---

archive/issue_comments_035626.json:
```json
{
    "body": "Attachment [trac_4728-docs.patch](tarball://root/attachments/some-uuid/ticket4728/trac_4728-docs.patch) by @jasongrout created at 2009-01-28 17:56:47\n\npositive review.  I've posted a small patch for the docs to correct the problem malb pointed out.  All tests pass in calculus.py.",
    "created_at": "2009-01-28T17:56:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4728#issuecomment-35626",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_4728-docs.patch](tarball://root/attachments/some-uuid/ticket4728/trac_4728-docs.patch) by @jasongrout created at 2009-01-28 17:56:47

positive review.  I've posted a small patch for the docs to correct the problem malb pointed out.  All tests pass in calculus.py.



---

archive/issue_events_004972.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-01-29T00:26:55Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4728#event-4972"
}
```



---

archive/issue_comments_035627.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-29T00:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4728#issuecomment-35627",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_035628.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha3.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-29T00:26:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4728",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4728#issuecomment-35628",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha3.

Cheers,

Michael
