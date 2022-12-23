# Issue 9424: numerical evaluation of symbolic sums

Issue created by migration from https://trac.sagemath.org/ticket/9424

Original creator: burcin

Original creation time: 2010-07-04 13:13:14

Assignee: burcin

CC:  whuss kcrisman eviatarbach

Symbolics sums returned from maxima cannot be numerically evaluated, since they don't define an `_evalf_()` method.

This was reported by dirkd on sage-support:


```
Why is evaluating this expression problematical?

y1(x)=x^2;y2(x)=5-x;
a0=1;an=3;Delta=(an-a0)/n;p(k)=a0+(k-1/2)*Delta;
I(n)=sum(abs(y2(p(k))-y1(p(k)))*Delta,k,1,n);
N(I(10))

SAGE respons:
<snipped traceback>
  File "expression.pyx", line 3797, in
sage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:
17022)
TypeError: cannot evaluate symbolic expression numerically
```


Here is the thread:

http://groups.google.com/group/sage-support/t/615b15ca638c9652


---

Comment by rws created at 2014-07-26 09:51:12

Changing status from new to needs_review.


---

Comment by rws created at 2014-07-26 09:51:12

Your problem is threefold: 1. you use `n` both as sum endpoint and variable, 2. Sage `sum` is only intended with symbolic endpoints, and 3. the need to use Python summation may require defining a Python function instead of a Sage symbolic function:

```
sage: sum?
...
Warning: This function only works with symbolic expressions. To sum any
     other objects like list elements or function return values,
     please use python summation...

sage: I(n)=sum(abs(y2(p(k))-y1(p(k)))*Delta,k,1,n);
sage: I
n |--> 2*sum(abs(-4*k^2 - 3*(2*k - 1)*n + 3*n^2 + 4*k - 1), k, 1, n)/n^3

sage: def I(n):
....:     return (2*sum(abs(-4*k^2 - 3*(2*k - 1)*n + 3*n^2 + 4*k - 1) for k in range(1,n+1))/n^3)
....: 
sage: I(10)
1301/250
sage: [I(i) for i in range(1,11)]
[2, 5, 46/9, 5, 26/5, 277/54, 254/49, 665/128, 418/81, 1301/250]
```



---

Comment by kcrisman created at 2014-08-01 14:48:58

I don't think any of these invalidate the ticket; the point is to extend the behavior.  Why is 1. a problem?  This seems like it should be a nice function to me.  See Burcin's reply in the thread:

```
> If I leave out the N( )-operator on the last line the block evaluates
> to
> 
> 
> 1/500*sum(abs(-4*k^2 - 56*k + 329), k, 1, 10)
> 
> which can be evaluated in a new inputbox. Why not in one step?
The result returned from maxima uses a symbolic function object created
on the fly. This is quite different from the sum() function
available on the command line, and unfortunately, it doesn't define a
numerical evaluation function, _evalf_().
```

Burcin knows this code very well, so I would be surprised if he misdiagnosed this.  But I figure maybe changing to enhancement will appease everyone :)


---

Comment by kcrisman created at 2014-08-01 14:48:58

Changing type from defect to enhancement.


---

Comment by nbruin created at 2014-08-01 18:32:53

Burcin is spot-on:

```
sage: S=(I(10).operands()[0].operator()); S
sum
sage: type(S)
<class 'sage.symbolic.function_factory.NewSymbolicFunction'>
```

(Note the "New", not "BuiltIn" or similar. It's a completely generic placeholder)
we just need a symbolic function hooked up that can do some mildly intelligent evaluation when asked for it.

Incidentally, we can just map back to maxima and do the right thing there:

```
sage: maxima_calculus(I(10))
('sum(abs(4*_SAGE_VAR_k^2+56*_SAGE_VAR_k-329),_SAGE_VAR_k,1,10))/500
sage: SR(maxima_calculus(I(10)).simplify_sum())
1301/250
```

(I haven't checked if it's correct). You can see why the "simplify_sum" is required: the newly created "sum" function in SR is linked to the inert "'sum".


---

Comment by rws created at 2014-08-05 14:05:45

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2014-11-19 03:05:35

[A relevant ask.sagemath question](http://ask.sagemath.org/question/9937/how-do-i-evaluate-sum-containing-factorial/).

[Another one](http://ask.sagemath.org/question/24911/exponentiation-makes-a-formula-go-crazy/).

Maybe it's time we fixed this.


---

Comment by rws created at 2014-12-01 10:21:25

Replying to [comment:12 kcrisman]:
> Maybe it's time we fixed this.
It is not clear if forcing people to use `N()` and getting a float, even if there is an integer simplification of the sum, is the right thing to do. Granted, the error thrown on `N(I(10))` is a bug, and this ticket is about it. Here is a minimal example:

```
sage: (k,n) = var('k,n')
sage: f(n)=sum(abs(-k*k+n),k,1,n)
sage: f(n=8)
sum(abs(-k^2 + 8), k, 1, 8)
sage: N(f(8))
```

However, I would expect `f(n=8).simplify()` or `.expand()` to give me the result `162`, and this is #17422


---

Comment by rws created at 2014-12-04 07:05:33

Changing type from enhancement to defect.


---

Comment by rws created at 2015-02-01 08:20:31

As #15346 would implement `simplify_sum`, what remains for this ticket to do?


---

Comment by rws created at 2015-02-01 08:20:31

Changing status from needs_work to needs_info.


---

Comment by kcrisman created at 2015-02-04 19:53:38

> As #15346 would implement simplify_sum, what remains for this ticket to do?

I suppose there is the issue that one might not want to have to simplify in order to get a floating-point number.  Really, we shouldn't _require_ that.  With #15346 one needs

```
sage: I(10).expand_sum().n()
```

but really `I(10).n()` should suffice, and for that we need a symbolic sum function.  I'll clarify the title, though, as you are right that this is at least now much more possible.  I'll probably add the example as a reviewer patch on #15346, in fact.


---

Comment by kcrisman created at 2015-02-04 20:06:22

Changing status from needs_info to needs_work.


---

Comment by rws created at 2015-02-06 17:10:21

This is a proof of concept-patch that works, but only with bare sums. I guess the walk on the expression tree happens somewhere in Pynac.

```
diff --git a/src/sage/symbolic/expression.pyx b/src/sage/symbolic/expression.pyx
--- a/src/sage/symbolic/expression.pyx
+++ b/src/sage/symbolic/expression.pyx
@@ -4847,6 +4847,19 @@ cdef class Expression(CommutativeRingElement):
             sage: all(len(str(e.n(digits=k)))-1 >= k for k in ks)
             True
 
+        We also allow evaluation of unexpanded symbolic sums
+        with numeric limits (:trac:`9424`)::
+
+            sage: (k,n) = var('k,n')
+            sage: f(n) = sum(abs(-k*k+n), k, 1, n)
+            sage: f(n=8)
+            sum(abs(-k^2 + 8), k, 1, 8)
+            sage: f(n=8).n()
+            162.0
+            sage: f(n=x).n()
+            Traceback (most recent call last):
+            ...
+            TypeError: cannot evaluate symbolic expression numerically
         """
         if prec is None:
             if digits is None:
@@ -4865,11 +4878,16 @@ cdef class Expression(CommutativeRingElement):
             x = self._convert(kwds)
 
         # we have to consider constants as well, since infinity is a constant
-        # in pynac
+        # in pynac. Also, catch symbolic sums with numeric limits.
         if is_a_numeric(x._gobj):
             res = py_object_from_numeric(x._gobj)
-        elif  is_a_constant(x._gobj):
+        elif is_a_constant(x._gobj):
             res = x.pyobject()
+        elif x.operator().name() == 'sum' and (
+                    is_a_numeric((<Expression>x.operands()[2])._gobj)
+                and is_a_numeric((<Expression>x.operands()[3])._gobj)):
+            from sage.calculus.calculus import symbolic_sum
+            return symbolic_sum(*(x.operands()))
         else:
             raise TypeError("cannot evaluate symbolic expression numerically")
```

but

```
sage: (k,n) = var('k,n')
sage: f(n) = sum(abs(-k*k+n),k,1,n)
sage: 1+f(n=8)
sum(abs(-k^2 + 8), k, 1, 8) + 1
sage: _.n()
BOOM
```



---

Comment by rws created at 2015-02-10 15:01:50

Changing status from needs_work to needs_review.


---

Comment by rws created at 2015-02-10 15:01:50

I think I found a satisfying solution.
----
New commits:


---

Comment by kcrisman created at 2015-02-10 16:06:06

You'd think that given the massive amounts of snow here lately I'd have time to carefully look this over - but I don't :-(

_However_ I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?  (There might be more people interested in that, honestly.)  Unless someone complained with the name change - but it was never globally imported and frankly we do need a general expression tree walker more easily accessible, see #9329 for instance.  So connecting this (not here, maybe) to the `Converter` class it inherits from and explaining when one would use each one would be useful too.

The main concern I have in terms of the main purpose of the ticket is to adequately test and debug `DefiniteSumExpander`, especially since it is in the code in such a way that it isn't doctested (other than the case in question).


---

Comment by rws created at 2015-02-10 16:13:28

Replying to [comment:21 kcrisman]:
> _However_ I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?
I don't understand. You did see the number #17759?
> The main concern I have in terms of the main purpose of the ticket is to adequately test and debug `DefiniteSumExpander`, especially since it is in the code in such a way that it isn't doctested (other than the case in question).
Most of it is doctested in #17759, i.e., its base class.


---

Comment by kcrisman created at 2015-02-10 16:18:21

> Replying to [comment:21 kcrisman]:
> > _However_ I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?
> I don't understand. You did see the number #17759?
Nope!  I really didn't have a lot of time - never even saw the dependency field.  Maybe I shouldn't look at tickets after shoveling ;)
> Most of it is doctested in #17759, i.e., its base class.
I did see that doctesting, I just would want to see what was different in the sum case.

I'll keep these on the front burner.


---

Comment by rws created at 2015-02-10 16:21:22

Replying to [comment:23 kcrisman]:
> I did see that doctesting, I just would want to see what was different in the sum case.
There the `composition` method is overwritten (and tested).


---

Comment by rws created at 2015-02-24 10:05:10

Changing status from needs_review to needs_work.


---

Comment by rws created at 2015-02-24 10:05:10


```
sage -t --long src/sage/functions/hypergeometric.py  # 11 doctests failed
sage -t --long src/sage/functions/trig.py  # 1 doctest failed
```



---

Comment by rws created at 2015-02-24 14:49:04

Fixing these doctests will need the solutions found for fixing #17849 (or vice versa).


---

Comment by git created at 2015-02-28 17:32:40

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2015-02-28 17:34:22

Changing status from needs_work to needs_review.


---

Comment by rws created at 2015-05-25 06:56:14

New commits:


---

Comment by mmezzarobba created at 2015-05-25 10:10:09

`TestsFailed` (says the patchbot)


---

Comment by mmezzarobba created at 2015-05-25 10:10:09

Changing status from needs_review to needs_work.


---

Comment by git created at 2015-06-11 06:59:43

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2015-06-11 07:00:19

Changing status from needs_work to needs_review.


---

Comment by dkrenn created at 2016-04-30 05:58:30

LGTM


---

Comment by dkrenn created at 2016-04-30 05:58:30

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2016-05-01 16:30:11

Resolution: fixed
