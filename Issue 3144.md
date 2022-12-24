# Issue 3144: bug in calculus var command

archive/issues_003144.json:
```json
{
    "body": "Assignee: was\n\nNote that the output of var('x,y') below the second time is *totally broken* - it returns a string:\n\n\n```\nsage: x,y=var(\"x,y\")\nsage: f(x,y)=sin(x)+cos(y)\nsage: grads=[diff(f,var) for var in (x,y)]\nsage: var('x,y')\n'x,y'\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3144\n\n",
    "created_at": "2008-05-09T15:16:51Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in calculus var command",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3144",
    "user": "was"
}
```
Assignee: was

Note that the output of var('x,y') below the second time is *totally broken* - it returns a string:


```
sage: x,y=var("x,y")
sage: f(x,y)=sin(x)+cos(y)
sage: grads=[diff(f,var) for var in (x,y)]
sage: var('x,y')
'x,y'
```


Issue created by migration from https://trac.sagemath.org/ticket/3144





---

archive/issue_comments_021816.json:
```json
{
    "body": "\n```\n\n\nOn Fri, May 9, 2008 at 9:28 AM, Marshall Hampton <hamptonio@gmail.com> wrote:\n>\n> I'm not sure I agree that this is a bug.  After using the name \"var\"\n> in the loop, the value of var is y.  y is a symbolic variable, and\n> when evaluated at the string \"x,y\" it returns \"x,y\"; this seems like\n> desirable behavior (to have string-valued functions seems OK to me).\n>\n> Or another way to put it: if the above behavior is a bug, then I think\n> the following would be as well:\n> sage: x,y = var(\"x,y\")\n> sage: y(2)\n> 2\n>\n> Or perhaps I am missing something.\n> -M. Hampton\n\nThere is an issue with the design, though it is arguable what it is.\nNotice that var('x') acts as the identity function irregardless of the input,\nwhere as var('x')^2 coerces its input to the SymbolicRing. \n\nsage: x = var('x')\nsage: x('hello world')\n'hello world'\nsage: type(x('hello world'))\n<type 'str'>\nsage: (x^2)('hello world')\nhello^2*world^2\nsage: type((x^2)('hello world'))\n<class 'sage.calculus.calculus.SymbolicArithmetic'>\nsage: x,y=var(\"x,y\")\n\nI thus think the right fix would be for var('x') to also coerce its input\nto the symbolic ring.  So, in the original question var('x,y') would\ngive an error since:\n\n sage: SR('x,y')\nTraceback (most recent call last):\n...\nTypeError: Malformed expression: x, !!! y\n\nBy the way, what's up with the !!! in the error message?  That looks very weird. \n\nWhat do you think.\n\n -- william\n```\n",
    "created_at": "2008-05-09T16:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3144#issuecomment-21816",
    "user": "was"
}
```


```


On Fri, May 9, 2008 at 9:28 AM, Marshall Hampton <hamptonio@gmail.com> wrote:
>
> I'm not sure I agree that this is a bug.  After using the name "var"
> in the loop, the value of var is y.  y is a symbolic variable, and
> when evaluated at the string "x,y" it returns "x,y"; this seems like
> desirable behavior (to have string-valued functions seems OK to me).
>
> Or another way to put it: if the above behavior is a bug, then I think
> the following would be as well:
> sage: x,y = var("x,y")
> sage: y(2)
> 2
>
> Or perhaps I am missing something.
> -M. Hampton

There is an issue with the design, though it is arguable what it is.
Notice that var('x') acts as the identity function irregardless of the input,
where as var('x')^2 coerces its input to the SymbolicRing. 

sage: x = var('x')
sage: x('hello world')
'hello world'
sage: type(x('hello world'))
<type 'str'>
sage: (x^2)('hello world')
hello^2*world^2
sage: type((x^2)('hello world'))
<class 'sage.calculus.calculus.SymbolicArithmetic'>
sage: x,y=var("x,y")

I thus think the right fix would be for var('x') to also coerce its input
to the symbolic ring.  So, in the original question var('x,y') would
give an error since:

 sage: SR('x,y')
Traceback (most recent call last):
...
TypeError: Malformed expression: x, !!! y

By the way, what's up with the !!! in the error message?  That looks very weird. 

What do you think.

 -- william
```




---

archive/issue_comments_021817.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-01-22T02:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3144#issuecomment-21817",
    "user": "was"
}
```

Resolution: invalid



---

archive/issue_comments_021818.json:
```json
{
    "body": "stupid mistake by me, since var is defined in the list...",
    "created_at": "2009-01-22T02:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3144",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3144#issuecomment-21818",
    "user": "was"
}
```

stupid mistake by me, since var is defined in the list...
