# Issue 9556: Dynamic attributes for symbolic expressions

archive/issues_009556.json:
```json
{
    "body": "Assignee: segfaulting doctests\n\nCC:  burcin kcrisman vbraun eviatarbach\n\nKeywords: symbolic expression dynamic attribute\n\nLet `e` be a symbolic expression. It may happen that `e.operator()` has a certain callable attribute, say, `foo`, that is not a method of `Function`. In this situation, one would like to use `e.foo()`, which is supposed to return `e.operator().foo(*e.operands())` - apparently this is useful for working with hypergeometric functions.\n\n**__Example__**\n\n\n```\nsage: from sage.symbolic.function import BuiltinFunction\nsage: class ExampleBuiltin(BuiltinFunction):\n...     def __init__(self):\n...         BuiltinFunction.__init__(self, 'ex_func', nargs=0) #arbitrary no of args\n...     def some_function_name(self, *args):\n...         return len(args)\n...\nsage: ex_func = ExampleBuiltin()\nsage: ex_func\nex_func\n```\n\n\nWe obtain a symbolic expression by calling `ex_func`:\n\n```\nsage: e = ex_func(x,x+1, x+2)\nsage: type(e)\n<type 'sage.symbolic.expression.Expression'>\n```\n\n\nWe add a callable and a non-callable attribute to `ex_func`:\n\n```\nsage: def some_function(slf, *L): print slf,'called with',L\n...\nsage: ex_func.foo_bar = some_function\nsage: ex_func.bar_foo = 4\n```\n\n\nNow, both the new method and the callable attribute `foo_bar` of\n`ex_func` are available from `e`, but not the non-callable:\n\n\n```\nsage: e.some_function_name()\n3\nsage: e.foo_bar()\nex_func called with (x, x + 1, x + 2)\nsage: e.bar_foo\nTraceback (most recent call last):\n...\nAttributeError: <type 'sage.symbolic.expression.Expression'> has no attribute 'bar_foo'\n```\n\n\nTab completion  and introspection work:\n\n\n```\nsage: 'foo_bar' in dir(e)     # indirect doctest\nTrue\nsage: 'some_function_name' in dir(e)\nTrue\nsage: 'bar_foo' in dir(e)\nFalse\nsage: import sagenb.misc.support as s\nsage: s.completions('e.some', globals(), system='python')\n['e.some_function_name']\n```\n\n\n**__Problems__**\n\nWhen I ran `sage -testall`, several doctests segfaulted:\n\n```\n        sage -t  -verbose \"devel/sage/sage/functions/hyperbolic.py\"\n        sage -t  -verbose \"devel/sage/sage/games/hexad.py\"\n        sage -t  -verbose \"devel/sage/sage/matrix/tests.py\"\n        sage -t  -verbose \"devel/sage/sage/misc/sage_eval.py\"\n        sage -t  -verbose \"devel/sage/sage/plot/animate.py\"\n        sage -t  -verbose \"devel/sage/sage/quadratic_forms/quadratic_form__mass__Conway_Sloane_masses.py\"\n        sage -t  -verbose \"devel/sage/sage/rings/polynomial/polynomial_element.pyx\"\n```\n\n\nI tried (using `sage -t -verbose`) to find out what exactly fails. When I ran some of these failing examples in an interactive session, no segfault occured. So, is there a nasty side effect?\n\nIssue created by migration from https://trac.sagemath.org/ticket/9556\n\n",
    "created_at": "2010-07-20T12:21:13Z",
    "labels": [
        "symbolics",
        "major",
        "enhancement"
    ],
    "title": "Dynamic attributes for symbolic expressions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9556",
    "user": "SimonKing"
}
```
Assignee: segfaulting doctests

CC:  burcin kcrisman vbraun eviatarbach

Keywords: symbolic expression dynamic attribute

Let `e` be a symbolic expression. It may happen that `e.operator()` has a certain callable attribute, say, `foo`, that is not a method of `Function`. In this situation, one would like to use `e.foo()`, which is supposed to return `e.operator().foo(*e.operands())` - apparently this is useful for working with hypergeometric functions.

**__Example__**


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


**__Problems__**

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

Issue created by migration from https://trac.sagemath.org/ticket/9556





---

archive/issue_comments_092111.json:
```json
{
    "body": "The patch implements dynamic attributes, but some doctests segfault",
    "created_at": "2010-07-20T12:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92111",
    "user": "SimonKing"
}
```

The patch implements dynamic attributes, but some doctests segfault



---

archive/issue_comments_092112.json:
```json
{
    "body": "Attachment [trac-9556_dynamic_attributes_symbolics.patch](tarball://root/attachments/some-uuid/ticket9556/trac-9556_dynamic_attributes_symbolics.patch) by SimonKing created at 2010-07-20 12:26:59",
    "created_at": "2010-07-20T12:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92112",
    "user": "SimonKing"
}
```

Attachment [trac-9556_dynamic_attributes_symbolics.patch](tarball://root/attachments/some-uuid/ticket9556/trac-9556_dynamic_attributes_symbolics.patch) by SimonKing created at 2010-07-20 12:26:59



---

archive/issue_comments_092113.json:
```json
{
    "body": "Remove assignee segfaulting doctests.",
    "created_at": "2010-07-20T12:26:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92113",
    "user": "SimonKing"
}
```

Remove assignee segfaulting doctests.



---

archive/issue_comments_092114.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-07-20T12:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92114",
    "user": "SimonKing"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_092115.json:
```json
{
    "body": "Sorry, accidentally I inserted the work issue \"segfaulting doctests\" into the owner field.\n\nIt would be nice to have a segfaulting example that works interactively.",
    "created_at": "2010-07-20T12:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92115",
    "user": "SimonKing"
}
```

Sorry, accidentally I inserted the work issue "segfaulting doctests" into the owner field.

It would be nice to have a segfaulting example that works interactively.



---

archive/issue_comments_092116.json:
```json
{
    "body": "What is the typical use case for this?  Are you just looking for a place to put the functions for evaluated function?  Or do you really want the function to appear on both the function and its evaluations?  It seems like the first case is what you really want.\n\nWe currently have all of the machinery to do this and it's used for the category code.  Using this, you would have something like the following:\n\n\n```\nclass ExampleBuiltin(BuiltinFunction):\n    def __init__(self):\n        BuiltinFunction.__init__(self, 'ex_func', nargs=0) #arbitrary no of args\n \n    class EvaluationMethods:\n        def some_function_name(self):\n            return len(self.operands())\n```\n",
    "created_at": "2010-07-20T13:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92116",
    "user": "mhansen"
}
```

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

archive/issue_comments_092117.json:
```json
{
    "body": "I did a little mockup using this idea.\n\n\n```\n\nsage: from sage.symbolic.function import BuiltinFunction\nsage: class ExampleBuiltin(BuiltinFunction):\n....:         def __init__(self):\n....:             BuiltinFunction.__init__(self, 'ex_func', nargs=0) #arbitrary no of args\n....:     class EvaluationMethods:\n....:             def some_function_name(self):\n....:                 return len(self.operands())\n....: \nsage: ex_func = ExampleBuiltin()\nsage: f = ex_func(x, x+1, x+2)\nsage: f.some_function_name()\n3\nsage: abs(f)\nabs(ex_func(x, x + 1, x + 2))\n```\n",
    "created_at": "2010-07-20T13:45:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92117",
    "user": "mhansen"
}
```

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

archive/issue_comments_092118.json:
```json
{
    "body": "Attachment [trac_9556-dynamic_class.patch](tarball://root/attachments/some-uuid/ticket9556/trac_9556-dynamic_class.patch) by mhansen created at 2010-07-20 14:22:01",
    "created_at": "2010-07-20T14:22:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92118",
    "user": "mhansen"
}
```

Attachment [trac_9556-dynamic_class.patch](tarball://root/attachments/some-uuid/ticket9556/trac_9556-dynamic_class.patch) by mhansen created at 2010-07-20 14:22:01



---

archive/issue_comments_092119.json:
```json
{
    "body": "Note that pickling also works:\n\n\n```\nsage: loads(dumps(ceil(x))).foo_bar()\n4\n```\n\n\nOne issue is that in order to get the dynamic features, you have to go through the __call__ method of the function.  Thus, you'd have to change Expression.__abs__\n\n\n```\n        return new_Expression_from_GEx(self._parent, g_abs(self._gobj))\n```\n\n\nto return the dynamic class version.  Similarly, unpickling old objects will just return an Expression object.",
    "created_at": "2010-07-20T14:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92119",
    "user": "mhansen"
}
```

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

archive/issue_comments_092120.json:
```json
{
    "body": "Also, all tests pass with this.",
    "created_at": "2010-07-20T14:27:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92120",
    "user": "mhansen"
}
```

Also, all tests pass with this.



---

archive/issue_comments_092121.json:
```json
{
    "body": "Replying to [comment:3 mhansen]:\n> What is the typical use case for this?  Are you just looking for a place to put the functions for evaluated function?  Or do you really want the function to appear on both the function and its evaluations? \n\nSorry that I was absent for some hours. \n\nUnfortunately I don't know what the real use case is. It was a suggestion of Burcin, and I merely tried to implement what he suggested. \n\nBurcin, could you comment on what is really expected?",
    "created_at": "2010-07-20T19:32:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92121",
    "user": "SimonKing"
}
```

Replying to [comment:3 mhansen]:
> What is the typical use case for this?  Are you just looking for a place to put the functions for evaluated function?  Or do you really want the function to appear on both the function and its evaluations? 

Sorry that I was absent for some hours. 

Unfortunately I don't know what the real use case is. It was a suggestion of Burcin, and I merely tried to implement what he suggested. 

Burcin, could you comment on what is really expected?



---

archive/issue_comments_092122.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> I did a little mockup using this idea.\n> \n> sage: f = ex_func(x, x+1, x+2)\n> sage: f.some_function_name()\n> 3\n> sage: abs(f)\n> abs(ex_func(x, x + 1, x + 2))\n\n... which seems like the correct answer to me. So, the fact that `ex_func` has an `_abs_` method helps to get the right answer for `f`.",
    "created_at": "2010-07-20T19:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92122",
    "user": "SimonKing"
}
```

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

archive/issue_comments_092123.json:
```json
{
    "body": "I uploaded a new patch that uses Mike's dynamic class idea, but applies to all code paths that might generate symbolic expressions with minimal speed penalty. Please review.\n\nPatchbot, apply only [This is the Trac macro *attachment:trac_9556-dynamic_class_everywhere.patch* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#attachment:trac_9556-dynamic_class_everywhere.patch-macro).",
    "created_at": "2013-06-19T18:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92123",
    "user": "burcin"
}
```

I uploaded a new patch that uses Mike's dynamic class idea, but applies to all code paths that might generate symbolic expressions with minimal speed penalty. Please review.

Patchbot, apply only [This is the Trac macro *attachment:trac_9556-dynamic_class_everywhere.patch* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#attachment:trac_9556-dynamic_class_everywhere.patch-macro).



---

archive/issue_comments_092124.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2013-06-19T18:05:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92124",
    "user": "burcin"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_092125.json:
```json
{
    "body": "Changing keywords from \"symbolic expression dynamic attribute\" to \"symbolic expression dynamic attribute sd48\".",
    "created_at": "2013-06-19T21:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92125",
    "user": "eviatarbach"
}
```

Changing keywords from "symbolic expression dynamic attribute" to "symbolic expression dynamic attribute sd48".



---

archive/issue_comments_092126.json:
```json
{
    "body": "patchbot apply trac_9556-dynamic_class_everywhere.patch",
    "created_at": "2013-06-19T21:48:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92126",
    "user": "burcin"
}
```

patchbot apply trac_9556-dynamic_class_everywhere.patch



---

archive/issue_comments_092127.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-06-19T22:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92127",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_092128.json:
```json
{
    "body": "Looks good to me",
    "created_at": "2013-06-19T22:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92128",
    "user": "vbraun"
}
```

Looks good to me



---

archive/issue_comments_092129.json:
```json
{
    "body": "Attachment [trac_9556-dynamic_class_everywhere.patch](tarball://root/attachments/some-uuid/ticket9556/trac_9556-dynamic_class_everywhere.patch) by burcin created at 2013-06-19 22:58:24",
    "created_at": "2013-06-19T22:58:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92129",
    "user": "burcin"
}
```

Attachment [trac_9556-dynamic_class_everywhere.patch](tarball://root/attachments/some-uuid/ticket9556/trac_9556-dynamic_class_everywhere.patch) by burcin created at 2013-06-19 22:58:24



---

archive/issue_comments_092130.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-06-20T21:33:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92130",
    "user": "jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_092131.json:
```json
{
    "body": "Attachment [trac_9556-dynamic_class_everywhere.part2.patch](tarball://root/attachments/some-uuid/ticket9556/trac_9556-dynamic_class_everywhere.part2.patch) by burcin created at 2013-06-20 23:29:49",
    "created_at": "2013-06-20T23:29:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92131",
    "user": "burcin"
}
```

Attachment [trac_9556-dynamic_class_everywhere.part2.patch](tarball://root/attachments/some-uuid/ticket9556/trac_9556-dynamic_class_everywhere.part2.patch) by burcin created at 2013-06-20 23:29:49



---

archive/issue_comments_092132.json:
```json
{
    "body": "As discussed with Burcin, patch needs to move to a different ticket.\n\nAlso, unpacking goes too far and doesn't let me preserve SR objects. This leads to funny behavior for constant functions etc::\n\n```\nsage: o = (SR(1), x)\nsage: map(type, o)\n[sage.symbolic.expression.Expression, sage.symbolic.expression.Expression]\nsage: o = SR._force_pyobject(o)._unpack_operands()\nsage: map(type, o)\n[sage.rings.integer.Integer, sage.symbolic.expression.Expression]\n```\n",
    "created_at": "2013-06-21T19:46:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92132",
    "user": "vbraun"
}
```

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

archive/issue_comments_092133.json:
```json
{
    "body": "For future historians: The part2 was moved to #14802",
    "created_at": "2013-06-23T15:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92133",
    "user": "vbraun"
}
```

For future historians: The part2 was moved to #14802



---

archive/issue_comments_092134.json:
```json
{
    "body": "These `EvaluationMethods` should be a new-style class: #20825.",
    "created_at": "2016-06-14T14:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9556",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9556#issuecomment-92134",
    "user": "jdemeyer"
}
```

These `EvaluationMethods` should be a new-style class: #20825.
