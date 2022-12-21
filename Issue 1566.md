# Issue 1566: NumberField infinite recursion

Issue created by migration from Trac.

Original creator: phatsphere

Original creation time: 2007-12-19 12:38:23

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



---

Comment by mabshoff created at 2007-12-19 16:36:43

Changing priority from major to critical.


---

Comment by dmharvey created at 2007-12-20 23:59:47

I'm taking a look a this....

here is a simpler example that causes the same problem:


```
sage: K3.<a> = NumberField(sqrt(x))
```



---

Comment by dmharvey created at 2007-12-21 00:02:52

aha it has nothing to do with number fields:


```
sage: f = sqrt(x)
sage: g = f.polynomial(QQ)
[boom]
```



---

Comment by dmharvey created at 2007-12-21 00:10:17

ok it's some nastiness to do with recursive substitution in symbolic expressions. The same thing happens with `cos(x).polynomial(QQ)` etc. I will leave this voodoo to someone else who understands the symbolic calculus package.


---

Comment by dmharvey created at 2007-12-21 00:11:04

Changing component from algebraic geometry to calculus.


---

Comment by mhansen created at 2007-12-22 11:15:54

Changing status from new to assigned.


---

Comment by mhansen created at 2007-12-22 11:15:54

Changing assignee from was to mhansen.


---

Attachment


---

Comment by rlm created at 2007-12-22 17:47:44

Resolution: fixed


---

Comment by rlm created at 2007-12-22 17:47:44

merged in 2.9.1 rc0
