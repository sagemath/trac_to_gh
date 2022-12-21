# Issue 9556: Dynamic attributes for symbolic expressions

Issue created by migration from Trac.

Original creator: SimonKing

Original creation time: 2010-07-20 12:21:13

Assignee: segfaulting doctests

CC:  burcin kcrisman vbraun eviatarbach

Keywords: symbolic expression dynamic attribute

Let `e` be a symbolic expression. It may happen that `e.operator()` has a certain callable attribute, say, `foo`, that is not a method of `Function`. In this situation, one would like to use `e.foo()`, which is supposed to return `e.operator().foo(*e.operands())` - apparently this is useful for working with hypergeometric functions.

*__Example__*


```
sage: from sage.symbolic.function import BuiltinFunction
sage: class ExampleBuiltin(BuiltinFunction):
...     def __init__(self):
...         BuiltinFunction.__init__(self, 'ex_func', nargs=0) #arbitrary no of args
...     def some_function_name(self, *args):
...         return len(args)
...
sage: ex_func = ExampleBuiltin()
sage: ex_func
ex_func
```


We obtain a symbolic expression by calling `ex_func`:

```
sage: e = ex_func(x,x+1, x+2)
sage: type(e)
<type 'sage.symbolic.expression.Expression'>
```


We add a callable and a non-callable attribute to `ex_func`:

```
sage: def some_function(slf, *L): print slf,'called with',L
...
sage: ex_func.foo_bar = some_function
sage: ex_func.bar_foo = 4
```


Now, both the new method and the callable attribute `foo_bar` of
`ex_func` are available from `e`, but not the non-callable:


```
sage: e.some_function_name()
3
sage: e.foo_bar()
ex_func called with (x, x + 1, x + 2)
sage: e.bar_foo
Traceback (most recent call last):
...
AttributeError: <type 'sage.symbolic.expression.Expression'> has no attribute 'bar_foo'
```


Tab completion  and introspection work:


```
sage: 'foo_bar' in dir(e)     # indirect doctest
True
sage: 'some_function_name' in dir(e)
True
sage: 'bar_foo' in dir(e)
False
sage: import sagenb.misc.support as s
sage: s.completions('e.some', globals(), system='python')
['e.some_function_name']
```


*__Problems__*

When I ran `sage -testall`, several doctests segfaulted:

```
        sage -t  -verbose "devel/sage/sage/functions/hyperbolic.py"
        sage -t  -verbose "devel/sage/sage/games/hexad.py"
        sage -t  -verbose "devel/sage/sage/matrix/tests.py"
        sage -t  -verbose "devel/sage/sage/misc/sage_eval.py"
        sage -t  -verbose "devel/sage/sage/plot/animate.py"
        sage -t  -verbose "devel/sage/sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py"
        sage -t  -verbose "devel/sage/sage/rings/polynomial/polynomial_element.pyx"
```


I tried (using `sage -t -verbose`) to find out what exactly fails. When I ran some of these failing examples in an interactive session, no segfault occured. So, is there a nasty side effect?


---

Comment by SimonKing created at 2010-07-20 12:26:00

The patch implements dynamic attributes, but some doctests segfault


---

Attachment


---

Comment by SimonKing created at 2010-07-20 12:26:59

Remove assignee segfaulting doctests.


---

Comment by SimonKing created at 2010-07-20 12:30:02

Changing status from new to needs_work.


---

Comment by SimonKing created at 2010-07-20 12:30:02

Sorry, accidentally I inserted the work issue "segfaulting doctests" into the owner field.

It would be nice to have a segfaulting example that works interactively.


---

Comment by mhansen created at 2010-07-20 13:01:19

What is the typical use case for this?  Are you just looking for a place to put the functions for evaluated function?  Or do you really want the function to appear on both the function and its evaluations?  It seems like the first case is what you really want.

We currently have all of the machinery to do this and it's used for the category code.  Using this, you would have something like the following:


```
class ExampleBuiltin(BuiltinFunction):
    def __init__(self):
        BuiltinFunction.__init__(self, 'ex_func', nargs=0) #arbitrary no of args
 
    class EvaluationMethods:
        def some_function_name(self):
            return len(self.operands())
```



---

Comment by mhansen created at 2010-07-20 13:45:38

I did a little mockup using this idea.


```

sage: from sage.symbolic.function import BuiltinFunction
sage: class ExampleBuiltin(BuiltinFunction):
....:         def __init__(self):
....:             BuiltinFunction.__init__(self, 'ex_func', nargs=0) #arbitrary no of args
....:     class EvaluationMethods:
....:             def some_function_name(self):
....:                 return len(self.operands())
....: 
sage: ex_func = ExampleBuiltin()
sage: f = ex_func(x, x+1, x+2)
sage: f.some_function_name()
3
sage: abs(f)
abs(ex_func(x, x + 1, x + 2))
```



---

Attachment


---

Comment by mhansen created at 2010-07-20 14:27:24

Note that pickling also works:


```
sage: loads(dumps(ceil(x))).foo_bar()
4
```


One issue is that in order to get the dynamic features, you have to go through the __call__ method of the function.  Thus, you'd have to change Expression.__abs__


```
        return new_Expression_from_GEx(self._parent, g_abs(self._gobj))
```


to return the dynamic class version.  Similarly, unpickling old objects will just return an Expression object.


---

Comment by mhansen created at 2010-07-20 14:27:42

Also, all tests pass with this.


---

Comment by SimonKing created at 2010-07-20 19:32:51

Replying to [comment:3 mhansen]:
> What is the typical use case for this?  Are you just looking for a place to put the functions for evaluated function?  Or do you really want the function to appear on both the function and its evaluations? 

Sorry that I was absent for some hours. 

Unfortunately I don't know what the real use case is. It was a suggestion of Burcin, and I merely tried to implement what he suggested. 

Burcin, could you comment on what is really expected?


---

Comment by SimonKing created at 2010-07-20 19:35:01

Replying to [comment:4 mhansen]:
> I did a little mockup using this idea.
> 
> sage: f = ex_func(x, x+1, x+2)
> sage: f.some_function_name()
> 3
> sage: abs(f)
> abs(ex_func(x, x + 1, x + 2))

... which seems like the correct answer to me. So, the fact that `ex_func` has an `_abs_` method helps to get the right answer for `f`.


---

Comment by burcin created at 2013-06-19 18:05:52

I uploaded a new patch that uses Mike's dynamic class idea, but applies to all code paths that might generate symbolic expressions with minimal speed penalty. Please review.

Patchbot, apply only [This is the Trac macro *attachment:trac_9556-dynamic_class_everywhere.patch* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#attachment:trac_9556-dynamic_class_everywhere.patch-macro).


---

Comment by burcin created at 2013-06-19 18:05:52

Changing status from needs_work to needs_review.


---

Comment by eviatarbach created at 2013-06-19 21:36:52

Changing keywords from "symbolic expression dynamic attribute" to "symbolic expression dynamic attribute sd48".


---

Comment by burcin created at 2013-06-19 21:48:54

patchbot apply trac_9556-dynamic_class_everywhere.patch


---

Comment by vbraun created at 2013-06-19 22:56:22

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2013-06-19 22:56:22

Looks good to me


---

Attachment


---

Comment by jdemeyer created at 2013-06-20 21:33:53

Resolution: fixed


---

Attachment


---

Comment by vbraun created at 2013-06-21 19:46:29

As discussed with Burcin, patch needs to move to a different ticket.

Also, unpacking goes too far and doesn't let me preserve SR objects. This leads to funny behavior for constant functions etc::

```
sage: o = (SR(1), x)
sage: map(type, o)
[sage.symbolic.expression.Expression, sage.symbolic.expression.Expression]
sage: o = SR._force_pyobject(o)._unpack_operands()
sage: map(type, o)
[sage.rings.integer.Integer, sage.symbolic.expression.Expression]
```



---

Comment by vbraun created at 2013-06-23 15:51:58

For future historians: The part2 was moved to #14802


---

Comment by jdemeyer created at 2016-06-14 14:36:48

These `EvaluationMethods` should be a new-style class: #20825.
