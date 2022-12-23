# Issue 6480: .subs_expr() method doesn't work for argument of D derivative operator

Issue created by migration from https://trac.sagemath.org/ticket/6480

Original creator: gmhossain

Original creation time: 2009-07-08 11:37:56

CC:  kcrisman mjo eviatarbach jakobkroeker

In computing functional derivative, one needs to vary
a functional. For example, in sage-3.4 one can do as follows

```
sage: f(x) = function('f',x)
sage: df(x) = function('df',x)
sage: g = f(x).diff(x)
sage: g
diff(f(x), x, 1)
sage: g.subs_expr(f(x)==f(x)+df(x))
diff(f(x) + df(x), x, 1)
```


In new symbolics, if I do the same I get


```
sage: g
D[0](f)(x)
sage: g.subs_expr(f(x)==f(x)+df(x))
D[0](f)(x)
```



---

Comment by mjo created at 2012-01-03 22:51:30

I duped this in #11842. We might be able to make use of the test cases there when this gets fixed.


---

Comment by eviatarbach created at 2013-05-14 19:08:26

`.substitute_function` seems to work: http://ask.sagemath.org/question/2380/how-to-substitute-a-function-within-derivatives


---

Comment by mjo created at 2013-05-15 17:39:45

One of the  cases in #11842 that used to crash now works, but a lot of them still don't. I updated the list.


---

Comment by kcrisman created at 2013-05-15 18:11:49

I feel like if that one is closed, we should have the list here, so I'm updating the description.


---

Comment by rws created at 2017-02-21 09:08:57

I think these are different issues because `substitute_function` handles a narrowly defined set of cases, and it expects two functions (`f, g, sin`) not expressions (`f(x), diff(f(x),x)`) as function arguments. Cases above that are in the former category:

```
sage: f = function('f')(x)
....: g = function('g')(x)
....: df = f(x).diff(x)
sage: f.substitute_function(f,g)
f(x)
sage: f(1).substitute_function(f,g)
f(1)
sage: df.substitute_function(f,g)
diff(f(x), x)
sage: df(1).substitute_function(f,g)
D[0](f)(1)
```

The problem is that `f` and `g` are not function objects like `sin`. Taking this into account:

```
sage: f.substitute_function(f.operator(), g.operator())
g(x)
sage: f(1).substitute_function(f.operator(), g.operator())
g(1)
sage: df.substitute_function(f.operator(), g.operator())
diff(g(x), x)
sage: df(1).substitute_function(f.operator(), g.operator())
D[0](g)(1)
```

I opened #22401 for this.


---

Comment by rws created at 2017-02-21 14:53:36

Also, even if `subs` is fixed there is no way atm to get and use `diff(f(x)+g(x),x)`:

```
sage: diff(f(x)+g(x),x)
diff(f(x), x) + diff(g(x), x)
sage: diff(f(x)+g(x),x,hold=True)
TypeError: derivative() got an unexpected keyword argument 'hold'
```

`diff` is not a function, although it could well be theoretically:

```
sage: diff(f(x),x)
diff(f(x), x)
sage: _._dbgprinttree()
fderivative f @0x34a8c00, hash=0x1023d75fb40091, flags=0xb, nops=1, params=0
    x (symbol) @0x2895f10, serial=7, hash=0xe3706ef, flags=0xf, domain=0, iflags=0000000000000000
    =====
sage: diff(f(x),x)
diff(f(x), x)
sage: _.operator()
D[0](f)
sage: type(_)
<class 'sage.symbolic.operators.FDerivativeOperator'>
```

I cannot see why `diff(f(x)+g(x),x,hold=True)` should be supported so I'm not opening a ticket. Just don't expect that as output from a fixed `subs`.


---

Comment by rws created at 2017-02-22 07:10:12

So, what should work is

```
            sage: f = function('f')
            sage: g = function('g')
            sage: f(x).subs(f(x) == g(x))
            g(x)
            sage: f(x).subs(f == g)
            g(x)
            sage: f(x).subs({f : g})
            g(x)
            sage: df = f(x).diff(x); df
            diff(f(x), x)
            sage: df.subs(f(x) == g(x))
            diff(g(x), x)
            sage: df.subs(f == g)
            diff(g(x), x)
            sage: df.subs(f(x) == f(x) + g(x))
            diff(f(x), x) + diff(g(x), x)
            sage: df.subs(f == f + g)
            diff(f(x), x) + diff(g(x), x)
```

but it mostly doesn't:

```
Failed example:
    f(x).subs(f == g)
Exception raised:
    Traceback (most recent call last):
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 498, in _run
        self.compile_and_execute(example, compiler, test.globs)
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 861, in compile_and_execute
        exec(compiled, globs)
      File "<doctest sage.symbolic.expression.Expression.substitute[67]>", line 1, in <module>
        f(x).subs(f == g)
      File "sage/symbolic/expression.pyx", line 4961, in sage.symbolic.expression.Expression.substitute (build/cythonized/sage/symbolic/expression.cpp:29715)
        g(x)
      File "sage/symbolic/expression.pyx", line 348, in sage.symbolic.expression._subs_make_dict (build/cythonized/sage/symbolic/expression.cpp:5364)
        raise TypeError(msg.format(s))
    TypeError: not able to determine a substitution from False
**********************************************************************
Failed example:
    f(x).subs({f : g})
Exception raised:
    Traceback (most recent call last):
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 498, in _run
        self.compile_and_execute(example, compiler, test.globs)
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 861, in compile_and_execute
        exec(compiled, globs)
      File "<doctest sage.symbolic.expression.Expression.substitute[68]>", line 1, in <module>
        f(x).subs({f : g})
      File "sage/symbolic/expression.pyx", line 4971, in sage.symbolic.expression.Expression.substitute (build/cythonized/sage/symbolic/expression.cpp:30001)
        diff(f(x), x) + diff(g(x), x)
      File "sage/symbolic/expression.pyx", line 2885, in sage.symbolic.expression.Expression.coerce_in (build/cythonized/sage/symbolic/expression.cpp:21682)
        return self._parent._coerce_(z)
      File "sage/structure/parent_old.pyx", line 241, in sage.structure.parent_old.Parent._coerce_ (build/cythonized/sage/structure/parent_old.c:4949)
        return self.coerce(x)
      File "sage/structure/parent.pyx", line 1195, in sage.structure.parent.Parent.coerce (build/cythonized/sage/structure/parent.c:11169)
        raise TypeError("no canonical coercion from %s to %s" % (parent(x), self))
    TypeError: no canonical coercion from <class 'sage.symbolic.function_factory.NewSymbolicFunction'> to Symbolic Ring
**********************************************************************
    df.subs(f(x) == g(x))
Expected:
    diff(g(x), x)
Got:
    diff(f(x), x)
**********************************************************************
    df.subs(f == g)
Exception raised:
    Traceback (most recent call last):
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 498, in _run
        self.compile_and_execute(example, compiler, test.globs)
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 861, in compile_and_execute
        exec(compiled, globs)
      File "<doctest sage.symbolic.expression.Expression.substitute[71]>", line 1, in <module>
        df.subs(f == g)
      File "sage/symbolic/expression.pyx", line 4961, in sage.symbolic.expression.Expression.substitute (build/cythonized/sage/symbolic/expression.cpp:29715)
        g(x)
      File "sage/symbolic/expression.pyx", line 348, in sage.symbolic.expression._subs_make_dict (build/cythonized/sage/symbolic/expression.cpp:5364)
        raise TypeError(msg.format(s))
    TypeError: not able to determine a substitution from False
**********************************************************************
    df.subs(f(x) == f(x) + g(x))
Expected:
    diff(f(x), x) + diff(g(x), x)
Got:
    diff(f(x), x)
**********************************************************************
    df.subs(f == f + g)
Exception raised:
    Traceback (most recent call last):
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 498, in _run
        self.compile_and_execute(example, compiler, test.globs)
      File "/home/ralf/sage/local/lib/python2.7/site-packages/sage/doctest/forker.py", line 861, in compile_and_execute
        exec(compiled, globs)
      File "<doctest sage.symbolic.expression.Expression.substitute[73]>", line 1, in <module>
        df.subs(f == f + g)
    TypeError: unsupported operand type(s) for +: 'NewSymbolicFunction' and 'NewSymbolicFunction'
```



---

Comment by rws created at 2017-02-22 07:26:56

The above consists of three problems. The central one is the failure to `f(x).subs(f(x) == g(x))`; the `diff` case is probably only a result; it looks like this is a Pynac bug, and when fixed there it should be doctested here.

The second is the failure of `f(x).subs({f : g})`. Maybe we can delegate to `substitute_function` if the dict key/val pair consists of function objects.

The third is that `f+g` already bails out. But `SR('f')+SR('g')` does not so this would be a workaround.


---

Comment by rws created at 2017-02-22 07:34:40

Nah, it was wrong, only `diff(f(x),x).subs(f(x) == g(x))` doesn't work.


---

Comment by rws created at 2017-02-23 06:55:06

Replying to [comment:11 rws]:
> The above consists of three problems. The central one is the failure to `f(x).subs(f(x) == g(x))`; the `diff` case is probably only a result; it looks like this is a Pynac bug, and when fixed there it should be doctested here.

The special status of `fderivative` in Pynac (not a function) may be the reason, see also https://groups.google.com/d/msg/sage-support/lZ4AjbmvvQE/-BJ_xvMlAQAJ


---

Comment by jdemeyer created at 2017-02-24 10:47:02

Milestone renamed
