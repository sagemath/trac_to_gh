# Issue 1566: NumberField infinite recursion

archive/issues_001566.json:
```json
{
    "body": "Assignee: was\n\nI think the input is wrong, but it should not loop forever and throw an error.\n\n\n\n```\nK3.<a>=NumberField([x^2+1,sqrt(x^3)+1])\n```\n\n\n\ngives \n\n\n```\nException (click to the left for traceback):\n...\nRuntimeError: maximum recursion depth exceeded in cmp\n```\n\n\n\nhere the infinite traceback:\n\n```\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/server4/sage_notebook/worksheets/phatsphere/0/code/123.py\", line 4, in <module>\n    exec compile(ur'K3=NumberField([x**Integer(2)+Integer(1),sqrt(x**Integer(3))+Integer(1)],names=(\\u0027a\\u0027,)); (a,) = K3._first_ngens(Integer(1))' + '\\n', '', 'single')\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sympy/plotting/\", line 1, in <module>\n    \n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 245, in NumberField\n    return NumberFieldTower(polynomial, name)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 389, in NumberFieldTower\n    w = NumberFieldTower(v[1:], names=names[1:])\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 387, in NumberFieldTower\n    return NumberField(v[0], names=names)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 251, in NumberField\n    polynomial = polynomial.polynomial(QQ)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1344, in polynomial\n    dict([(var(V[i]),G[i]) for i in range(len(G))]), ring=R)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 2825, in substitute_over_ring\n    return X._recursive_sub_over_ring(kwds, ring)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 3763, in _recursive_sub_over_ring\n    new_ops = [op._recursive_sub_over_ring(kwds, ring=ring) for op in ops]\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 4842, in _recursive_sub_over_ring\n    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 218, in __call__\n    return x._polynomial_(self)        \n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1409, in _polynomial_\n    return self.substitute_over_ring(dict(sub), ring=R)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 2825, in substitute_over_ring\n    return X._recursive_sub_over_ring(kwds, ring)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 4842, in _recursive_sub_over_ring\n    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 218, in __call__\n    return x._polynomial_(self)        \n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1409, in _polynomial_\n    return self.substitute_over_ring(dict(sub), ring=R)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 2825, in substitute_over_ring\n    return X._recursive_sub_over_ring(kwds, ring)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 4842, in _recursive_sub_over_ring\n    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))\n.\n.\n.\n File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1409, in _polynomial_\n    return self.substitute_over_ring(dict(sub), ring=R)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 2825, in substitute_over_ring\n    return X._recursive_sub_over_ring(kwds, ring)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 4842, in _recursive_sub_over_ring\n    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 218, in __call__\n    return x._polynomial_(self)        \n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 1387, in _polynomial_\n    vars = self.variables()\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 3524, in variables\n    return self.simplify().variables(vars)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 2555, in simplify\n    S = evaled_symbolic_expression_from_maxima_string(self._maxima_init_())\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py\", line 6466, in evaled_symbolic_expression_from_maxima_string\n    return symbolic_expression_from_maxima_string(maxima.eval(x))\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/expect.py\", line 707, in eval\n    return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/maxima.py\", line 540, in _eval_line\n    self._synchronize()\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/maxima.py\", line 600, in _synchronize\n    self._expect_expr(timeout=0.5)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/maxima.py\", line 453, in _expect_expr\n    i = self._expect.expect(expr,timeout=timeout)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/pexpect.py\", line 911, in expect\n    compiled_pattern_list = self.compile_pattern_list(pattern)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/pexpect.py\", line 843, in compile_pattern_list\n    compiled_pattern_list.append(re.compile(p, re.DOTALL))\n  File \"/usr/local/sage-2.6/local/lib/python2.5/re.py\", line 180, in compile\n    return _compile(pattern, flags)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/re.py\", line 222, in _compile\n    p = _cache.get(cachekey)\nRuntimeError: maximum recursion depth exceeded in cmp\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1566\n\n",
    "created_at": "2007-12-19T12:38:23Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9.1",
    "title": "NumberField infinite recursion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1566",
    "user": "phatsphere"
}
```
Assignee: was

I think the input is wrong, but it should not loop forever and throw an error.



```
K3.<a>=NumberField([x^2+1,sqrt(x^3)+1])
```



gives 


```
Exception (click to the left for traceback):
...
RuntimeError: maximum recursion depth exceeded in cmp
```



here the infinite traceback:

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server4/sage_notebook/worksheets/phatsphere/0/code/123.py", line 4, in <module>
    exec compile(ur'K3=NumberField([x**Integer(2)+Integer(1),sqrt(x**Integer(3))+Integer(1)],names=(\u0027a\u0027,)); (a,) = K3._first_ngens(Integer(1))' + '\n', '', 'single')
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sympy/plotting/", line 1, in <module>
    
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 245, in NumberField
    return NumberFieldTower(polynomial, name)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 389, in NumberFieldTower
    w = NumberFieldTower(v[1:], names=names[1:])
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 387, in NumberFieldTower
    return NumberField(v[0], names=names)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 251, in NumberField
    polynomial = polynomial.polynomial(QQ)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1344, in polynomial
    dict([(var(V[i]),G[i]) for i in range(len(G))]), ring=R)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2825, in substitute_over_ring
    return X._recursive_sub_over_ring(kwds, ring)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 3763, in _recursive_sub_over_ring
    new_ops = [op._recursive_sub_over_ring(kwds, ring=ring) for op in ops]
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4842, in _recursive_sub_over_ring
    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 218, in __call__
    return x._polynomial_(self)        
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1409, in _polynomial_
    return self.substitute_over_ring(dict(sub), ring=R)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2825, in substitute_over_ring
    return X._recursive_sub_over_ring(kwds, ring)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4842, in _recursive_sub_over_ring
    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 218, in __call__
    return x._polynomial_(self)        
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1409, in _polynomial_
    return self.substitute_over_ring(dict(sub), ring=R)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2825, in substitute_over_ring
    return X._recursive_sub_over_ring(kwds, ring)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4842, in _recursive_sub_over_ring
    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))
.
.
.
 File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1409, in _polynomial_
    return self.substitute_over_ring(dict(sub), ring=R)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2825, in substitute_over_ring
    return X._recursive_sub_over_ring(kwds, ring)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 4842, in _recursive_sub_over_ring
    return ring(ops[0](ops[1]._recursive_sub_over_ring(kwds, ring=ring)))
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 218, in __call__
    return x._polynomial_(self)        
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 1387, in _polynomial_
    vars = self.variables()
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 3524, in variables
    return self.simplify().variables(vars)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 2555, in simplify
    S = evaled_symbolic_expression_from_maxima_string(self._maxima_init_())
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/calculus/calculus.py", line 6466, in evaled_symbolic_expression_from_maxima_string
    return symbolic_expression_from_maxima_string(maxima.eval(x))
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 707, in eval
    return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/maxima.py", line 540, in _eval_line
    self._synchronize()
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/maxima.py", line 600, in _synchronize
    self._expect_expr(timeout=0.5)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/interfaces/maxima.py", line 453, in _expect_expr
    i = self._expect.expect(expr,timeout=timeout)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/pexpect.py", line 911, in expect
    compiled_pattern_list = self.compile_pattern_list(pattern)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/pexpect.py", line 843, in compile_pattern_list
    compiled_pattern_list.append(re.compile(p, re.DOTALL))
  File "/usr/local/sage-2.6/local/lib/python2.5/re.py", line 180, in compile
    return _compile(pattern, flags)
  File "/usr/local/sage-2.6/local/lib/python2.5/re.py", line 222, in _compile
    p = _cache.get(cachekey)
RuntimeError: maximum recursion depth exceeded in cmp
```


Issue created by migration from https://trac.sagemath.org/ticket/1566





---

archive/issue_comments_009966.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2007-12-19T16:36:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9966",
    "user": "mabshoff"
}
```

Changing priority from major to critical.



---

archive/issue_comments_009967.json:
```json
{
    "body": "I'm taking a look a this....\n\nhere is a simpler example that causes the same problem:\n\n\n```\nsage: K3.<a> = NumberField(sqrt(x))\n```\n",
    "created_at": "2007-12-20T23:59:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9967",
    "user": "dmharvey"
}
```

I'm taking a look a this....

here is a simpler example that causes the same problem:


```
sage: K3.<a> = NumberField(sqrt(x))
```




---

archive/issue_comments_009968.json:
```json
{
    "body": "aha it has nothing to do with number fields:\n\n\n```\nsage: f = sqrt(x)\nsage: g = f.polynomial(QQ)\n[boom]\n```\n",
    "created_at": "2007-12-21T00:02:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9968",
    "user": "dmharvey"
}
```

aha it has nothing to do with number fields:


```
sage: f = sqrt(x)
sage: g = f.polynomial(QQ)
[boom]
```




---

archive/issue_comments_009969.json:
```json
{
    "body": "ok it's some nastiness to do with recursive substitution in symbolic expressions. The same thing happens with `cos(x).polynomial(QQ)` etc. I will leave this voodoo to someone else who understands the symbolic calculus package.",
    "created_at": "2007-12-21T00:10:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9969",
    "user": "dmharvey"
}
```

ok it's some nastiness to do with recursive substitution in symbolic expressions. The same thing happens with `cos(x).polynomial(QQ)` etc. I will leave this voodoo to someone else who understands the symbolic calculus package.



---

archive/issue_comments_009970.json:
```json
{
    "body": "Changing component from algebraic geometry to calculus.",
    "created_at": "2007-12-21T00:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9970",
    "user": "dmharvey"
}
```

Changing component from algebraic geometry to calculus.



---

archive/issue_comments_009971.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-22T11:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9971",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009972.json:
```json
{
    "body": "Changing assignee from was to mhansen.",
    "created_at": "2007-12-22T11:15:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9972",
    "user": "mhansen"
}
```

Changing assignee from was to mhansen.



---

archive/issue_comments_009973.json:
```json
{
    "body": "Attachment [1566.patch](tarball://root/attachments/some-uuid/ticket1566/1566.patch) by mhansen created at 2007-12-22 16:57:44",
    "created_at": "2007-12-22T16:57:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9973",
    "user": "mhansen"
}
```

Attachment [1566.patch](tarball://root/attachments/some-uuid/ticket1566/1566.patch) by mhansen created at 2007-12-22 16:57:44



---

archive/issue_comments_009974.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-22T17:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9974",
    "user": "rlm"
}
```

Resolution: fixed



---

archive/issue_comments_009975.json:
```json
{
    "body": "merged in 2.9.1 rc0",
    "created_at": "2007-12-22T17:47:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1566",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1566#issuecomment-9975",
    "user": "rlm"
}
```

merged in 2.9.1 rc0
