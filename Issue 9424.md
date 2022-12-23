# Issue 9424: numerical evaluation of symbolic sums

archive/issues_009424.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  whuss kcrisman eviatarbach\n\nSymbolics sums returned from maxima cannot be numerically evaluated, since they don't define an `_evalf_()` method.\n\nThis was reported by dirkd on sage-support:\n\n\n```\nWhy is evaluating this expression problematical?\n\ny1(x)=x^2;y2(x)=5-x;\na0=1;an=3;Delta=(an-a0)/n;p(k)=a0+(k-1/2)*Delta;\nI(n)=sum(abs(y2(p(k))-y1(p(k)))*Delta,k,1,n);\nN(I(10))\n\nSAGE respons:\n<snipped traceback>\n  File \"expression.pyx\", line 3797, in\nsage.symbolic.expression.Expression.n (sage/symbolic/expression.cpp:\n17022)\nTypeError: cannot evaluate symbolic expression numerically\n```\n\n\nHere is the thread:\n\nhttp://groups.google.com/group/sage-support/t/615b15ca638c9652\n\nIssue created by migration from https://trac.sagemath.org/ticket/9424\n\n",
    "created_at": "2010-07-04T13:13:14Z",
    "labels": [
        "symbolics",
        "major",
        "bug"
    ],
    "title": "numerical evaluation of symbolic sums",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9424",
    "user": "burcin"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9424





---

archive/issue_comments_089882.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-07-26T09:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89882",
    "user": "rws"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089883.json:
```json
{
    "body": "Your problem is threefold: 1. you use `n` both as sum endpoint and variable, 2. Sage `sum` is only intended with symbolic endpoints, and 3. the need to use Python summation may require defining a Python function instead of a Sage symbolic function:\n\n```\nsage: sum?\n...\nWarning: This function only works with symbolic expressions. To sum any\n     other objects like list elements or function return values,\n     please use python summation...\n\nsage: I(n)=sum(abs(y2(p(k))-y1(p(k)))*Delta,k,1,n);\nsage: I\nn |--> 2*sum(abs(-4*k^2 - 3*(2*k - 1)*n + 3*n^2 + 4*k - 1), k, 1, n)/n^3\n\nsage: def I(n):\n....:     return (2*sum(abs(-4*k^2 - 3*(2*k - 1)*n + 3*n^2 + 4*k - 1) for k in range(1,n+1))/n^3)\n....: \nsage: I(10)\n1301/250\nsage: [I(i) for i in range(1,11)]\n[2, 5, 46/9, 5, 26/5, 277/54, 254/49, 665/128, 418/81, 1301/250]\n```\n",
    "created_at": "2014-07-26T09:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89883",
    "user": "rws"
}
```

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

archive/issue_comments_089884.json:
```json
{
    "body": "I don't think any of these invalidate the ticket; the point is to extend the behavior.  Why is 1. a problem?  This seems like it should be a nice function to me.  See Burcin's reply in the thread:\n\n```\n> If I leave out the N( )-operator on the last line the block evaluates\n> to\n> \n> \n> 1/500*sum(abs(-4*k^2 - 56*k + 329), k, 1, 10)\n> \n> which can be evaluated in a new inputbox. Why not in one step?\nThe result returned from maxima uses a symbolic function object created\non the fly. This is quite different from the sum() function\navailable on the command line, and unfortunately, it doesn't define a\nnumerical evaluation function, _evalf_().\n```\n\nBurcin knows this code very well, so I would be surprised if he misdiagnosed this.  But I figure maybe changing to enhancement will appease everyone :)",
    "created_at": "2014-08-01T14:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89884",
    "user": "kcrisman"
}
```

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

archive/issue_comments_089885.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2014-08-01T14:48:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89885",
    "user": "kcrisman"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_089886.json:
```json
{
    "body": "Burcin is spot-on:\n\n```\nsage: S=(I(10).operands()[0].operator()); S\nsum\nsage: type(S)\n<class 'sage.symbolic.function_factory.NewSymbolicFunction'>\n```\n\n(Note the \"New\", not \"BuiltIn\" or similar. It's a completely generic placeholder)\nwe just need a symbolic function hooked up that can do some mildly intelligent evaluation when asked for it.\n\nIncidentally, we can just map back to maxima and do the right thing there:\n\n```\nsage: maxima_calculus(I(10))\n('sum(abs(4*_SAGE_VAR_k^2+56*_SAGE_VAR_k-329),_SAGE_VAR_k,1,10))/500\nsage: SR(maxima_calculus(I(10)).simplify_sum())\n1301/250\n```\n\n(I haven't checked if it's correct). You can see why the \"simplify_sum\" is required: the newly created \"sum\" function in SR is linked to the inert \"'sum\".",
    "created_at": "2014-08-01T18:32:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89886",
    "user": "nbruin"
}
```

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

archive/issue_comments_089887.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-08-05T14:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89887",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089888.json:
```json
{
    "body": "[A relevant ask.sagemath question](http://ask.sagemath.org/question/9937/how-do-i-evaluate-sum-containing-factorial/).\n\n[Another one](http://ask.sagemath.org/question/24911/exponentiation-makes-a-formula-go-crazy/).\n\nMaybe it's time we fixed this.",
    "created_at": "2014-11-19T03:05:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89888",
    "user": "kcrisman"
}
```

[A relevant ask.sagemath question](http://ask.sagemath.org/question/9937/how-do-i-evaluate-sum-containing-factorial/).

[Another one](http://ask.sagemath.org/question/24911/exponentiation-makes-a-formula-go-crazy/).

Maybe it's time we fixed this.



---

archive/issue_comments_089889.json:
```json
{
    "body": "Replying to [comment:12 kcrisman]:\n> Maybe it's time we fixed this.\nIt is not clear if forcing people to use `N()` and getting a float, even if there is an integer simplification of the sum, is the right thing to do. Granted, the error thrown on `N(I(10))` is a bug, and this ticket is about it. Here is a minimal example:\n\n```\nsage: (k,n) = var('k,n')\nsage: f(n)=sum(abs(-k*k+n),k,1,n)\nsage: f(n=8)\nsum(abs(-k^2 + 8), k, 1, 8)\nsage: N(f(8))\n```\n\nHowever, I would expect `f(n=8).simplify()` or `.expand()` to give me the result `162`, and this is #17422",
    "created_at": "2014-12-01T10:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89889",
    "user": "rws"
}
```

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

archive/issue_comments_089890.json:
```json
{
    "body": "Changing type from enhancement to defect.",
    "created_at": "2014-12-04T07:05:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89890",
    "user": "rws"
}
```

Changing type from enhancement to defect.



---

archive/issue_comments_089891.json:
```json
{
    "body": "As #15346 would implement `simplify_sum`, what remains for this ticket to do?",
    "created_at": "2015-02-01T08:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89891",
    "user": "rws"
}
```

As #15346 would implement `simplify_sum`, what remains for this ticket to do?



---

archive/issue_comments_089892.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2015-02-01T08:20:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89892",
    "user": "rws"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_089893.json:
```json
{
    "body": "> As #15346 would implement simplify_sum, what remains for this ticket to do?\n\nI suppose there is the issue that one might not want to have to simplify in order to get a floating-point number.  Really, we shouldn't *require* that.  With #15346 one needs\n\n```\nsage: I(10).expand_sum().n()\n```\n\nbut really `I(10).n()` should suffice, and for that we need a symbolic sum function.  I'll clarify the title, though, as you are right that this is at least now much more possible.  I'll probably add the example as a reviewer patch on #15346, in fact.",
    "created_at": "2015-02-04T19:53:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89893",
    "user": "kcrisman"
}
```

> As #15346 would implement simplify_sum, what remains for this ticket to do?

I suppose there is the issue that one might not want to have to simplify in order to get a floating-point number.  Really, we shouldn't *require* that.  With #15346 one needs

```
sage: I(10).expand_sum().n()
```

but really `I(10).n()` should suffice, and for that we need a symbolic sum function.  I'll clarify the title, though, as you are right that this is at least now much more possible.  I'll probably add the example as a reviewer patch on #15346, in fact.



---

archive/issue_comments_089894.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-02-04T20:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89894",
    "user": "kcrisman"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_089895.json:
```json
{
    "body": "This is a proof of concept-patch that works, but only with bare sums. I guess the walk on the expression tree happens somewhere in Pynac.\n\n```\ndiff --git a/src/sage/symbolic/expression.pyx b/src/sage/symbolic/expression.pyx\n--- a/src/sage/symbolic/expression.pyx\n+++ b/src/sage/symbolic/expression.pyx\n@@ -4847,6 +4847,19 @@ cdef class Expression(CommutativeRingElement):\n             sage: all(len(str(e.n(digits=k)))-1 >= k for k in ks)\n             True\n \n+        We also allow evaluation of unexpanded symbolic sums\n+        with numeric limits (:trac:`9424`)::\n+\n+            sage: (k,n) = var('k,n')\n+            sage: f(n) = sum(abs(-k*k+n), k, 1, n)\n+            sage: f(n=8)\n+            sum(abs(-k^2 + 8), k, 1, 8)\n+            sage: f(n=8).n()\n+            162.0\n+            sage: f(n=x).n()\n+            Traceback (most recent call last):\n+            ...\n+            TypeError: cannot evaluate symbolic expression numerically\n         \"\"\"\n         if prec is None:\n             if digits is None:\n@@ -4865,11 +4878,16 @@ cdef class Expression(CommutativeRingElement):\n             x = self._convert(kwds)\n \n         # we have to consider constants as well, since infinity is a constant\n-        # in pynac\n+        # in pynac. Also, catch symbolic sums with numeric limits.\n         if is_a_numeric(x._gobj):\n             res = py_object_from_numeric(x._gobj)\n-        elif  is_a_constant(x._gobj):\n+        elif is_a_constant(x._gobj):\n             res = x.pyobject()\n+        elif x.operator().name() == 'sum' and (\n+                    is_a_numeric((<Expression>x.operands()[2])._gobj)\n+                and is_a_numeric((<Expression>x.operands()[3])._gobj)):\n+            from sage.calculus.calculus import symbolic_sum\n+            return symbolic_sum(*(x.operands()))\n         else:\n             raise TypeError(\"cannot evaluate symbolic expression numerically\")\n```\n\nbut\n\n```\nsage: (k,n) = var('k,n')\nsage: f(n) = sum(abs(-k*k+n),k,1,n)\nsage: 1+f(n=8)\nsum(abs(-k^2 + 8), k, 1, 8) + 1\nsage: _.n()\nBOOM\n```\n",
    "created_at": "2015-02-06T17:10:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89895",
    "user": "rws"
}
```

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

archive/issue_comments_089896.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-10T15:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89896",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089897.json:
```json
{
    "body": "I think I found a satisfying solution.\n----\nNew commits:",
    "created_at": "2015-02-10T15:01:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89897",
    "user": "rws"
}
```

I think I found a satisfying solution.
----
New commits:



---

archive/issue_comments_089898.json:
```json
{
    "body": "You'd think that given the massive amounts of snow here lately I'd have time to carefully look this over - but I don't :-(\n\n*However* I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?  (There might be more people interested in that, honestly.)  Unless someone complained with the name change - but it was never globally imported and frankly we do need a general expression tree walker more easily accessible, see #9329 for instance.  So connecting this (not here, maybe) to the `Converter` class it inherits from and explaining when one would use each one would be useful too.\n\nThe main concern I have in terms of the main purpose of the ticket is to adequately test and debug `DefiniteSumExpander`, especially since it is in the code in such a way that it isn't doctested (other than the case in question).",
    "created_at": "2015-02-10T16:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89898",
    "user": "kcrisman"
}
```

You'd think that given the massive amounts of snow here lately I'd have time to carefully look this over - but I don't :-(

*However* I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?  (There might be more people interested in that, honestly.)  Unless someone complained with the name change - but it was never globally imported and frankly we do need a general expression tree walker more easily accessible, see #9329 for instance.  So connecting this (not here, maybe) to the `Converter` class it inherits from and explaining when one would use each one would be useful too.

The main concern I have in terms of the main purpose of the ticket is to adequately test and debug `DefiniteSumExpander`, especially since it is in the code in such a way that it isn't doctested (other than the case in question).



---

archive/issue_comments_089899.json:
```json
{
    "body": "Replying to [comment:21 kcrisman]:\n> *However* I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?\nI don't understand. You did see the number #17759?\n> The main concern I have in terms of the main purpose of the ticket is to adequately test and debug `DefiniteSumExpander`, especially since it is in the code in such a way that it isn't doctested (other than the case in question).\nMost of it is doctested in #17759, i.e., its base class.",
    "created_at": "2015-02-10T16:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89899",
    "user": "rws"
}
```

Replying to [comment:21 kcrisman]:
> *However* I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?
I don't understand. You did see the number #17759?
> The main concern I have in terms of the main purpose of the ticket is to adequately test and debug `DefiniteSumExpander`, especially since it is in the code in such a way that it isn't doctested (other than the case in question).
Most of it is doctested in #17759, i.e., its base class.



---

archive/issue_comments_089900.json:
```json
{
    "body": "> Replying to [comment:21 kcrisman]:\n> > *However* I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?\n> I don't understand. You did see the number #17759?\nNope!  I really didn't have a lot of time - never even saw the dependency field.  Maybe I shouldn't look at tickets after shoveling ;)\n> Most of it is doctested in #17759, i.e., its base class.\nI did see that doctesting, I just would want to see what was different in the sum case.\n\nI'll keep these on the front burner.",
    "created_at": "2015-02-10T16:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89900",
    "user": "kcrisman"
}
```

> Replying to [comment:21 kcrisman]:
> > *However* I think this looks like a good start at a solution, and definitely the first commit is an improvement in any case - perhaps one that deserves its own ticket, for quicker review?
> I don't understand. You did see the number #17759?
Nope!  I really didn't have a lot of time - never even saw the dependency field.  Maybe I shouldn't look at tickets after shoveling ;)
> Most of it is doctested in #17759, i.e., its base class.
I did see that doctesting, I just would want to see what was different in the sum case.

I'll keep these on the front burner.



---

archive/issue_comments_089901.json:
```json
{
    "body": "Replying to [comment:23 kcrisman]:\n> I did see that doctesting, I just would want to see what was different in the sum case.\nThere the `composition` method is overwritten (and tested).",
    "created_at": "2015-02-10T16:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89901",
    "user": "rws"
}
```

Replying to [comment:23 kcrisman]:
> I did see that doctesting, I just would want to see what was different in the sum case.
There the `composition` method is overwritten (and tested).



---

archive/issue_comments_089902.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-02-24T10:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89902",
    "user": "rws"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089903.json:
```json
{
    "body": "\n```\nsage -t --long src/sage/functions/hypergeometric.py  # 11 doctests failed\nsage -t --long src/sage/functions/trig.py  # 1 doctest failed\n```\n",
    "created_at": "2015-02-24T10:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89903",
    "user": "rws"
}
```


```
sage -t --long src/sage/functions/hypergeometric.py  # 11 doctests failed
sage -t --long src/sage/functions/trig.py  # 1 doctest failed
```




---

archive/issue_comments_089904.json:
```json
{
    "body": "Fixing these doctests will need the solutions found for fixing #17849 (or vice versa).",
    "created_at": "2015-02-24T14:49:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89904",
    "user": "rws"
}
```

Fixing these doctests will need the solutions found for fixing #17849 (or vice versa).



---

archive/issue_comments_089905.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-28T17:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89905",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089906.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-28T17:34:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89906",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089907.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-05-25T06:56:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89907",
    "user": "rws"
}
```

New commits:



---

archive/issue_comments_089908.json:
```json
{
    "body": "`TestsFailed` (says the patchbot)",
    "created_at": "2015-05-25T10:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89908",
    "user": "mmezzarobba"
}
```

`TestsFailed` (says the patchbot)



---

archive/issue_comments_089909.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-05-25T10:10:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89909",
    "user": "mmezzarobba"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089910.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-11T06:59:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89910",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_089911.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-11T07:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89911",
    "user": "rws"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089912.json:
```json
{
    "body": "LGTM",
    "created_at": "2016-04-30T05:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89912",
    "user": "dkrenn"
}
```

LGTM



---

archive/issue_comments_089913.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-04-30T05:58:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89913",
    "user": "dkrenn"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089914.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-05-01T16:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9424",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9424#issuecomment-89914",
    "user": "vbraun"
}
```

Resolution: fixed
