# Issue 9652: Unnecesary and buggy code in arith.py

archive/issues_009652.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @mstreng @lftabera\n\nThis code was added in #1148. I really think that the lines removed in my patch should be gone. The current (4.4.4) code is:\n\n```\ndef valuation(m, p):\n    if hasattr(m, 'valuation'):\n        return m.valuation(p)\n    if is_FractionFieldElement(m):  \n        return valuation(m.numerator()) - valuation(m.denominator())\n    if m == 0:\n        import sage.rings.all\n        return sage.rings.all.infinity\n    r = 0\n    power = p\n    while not (m % power): # m % power == 0\n        r += 1\n        power *= p\n    return r\n```\n\nPutting implementation specific to Fraction fields in a global function is bad practice. And since fraction fields have an implementation of valuation part of the above code will not be execucted. If it magicaly get's excecuted it will return bad results since it doesn't take into account the input variable \"p\" as it should.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9652\n\n",
    "created_at": "2010-07-31T20:35:45Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "Unnecesary and buggy code in arith.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9652",
    "user": "https://github.com/koffie"
}
```
Assignee: @aghitza

CC:  @mstreng @lftabera

This code was added in #1148. I really think that the lines removed in my patch should be gone. The current (4.4.4) code is:

```
def valuation(m, p):
    if hasattr(m, 'valuation'):
        return m.valuation(p)
    if is_FractionFieldElement(m):  
        return valuation(m.numerator()) - valuation(m.denominator())
    if m == 0:
        import sage.rings.all
        return sage.rings.all.infinity
    r = 0
    power = p
    while not (m % power): # m % power == 0
        r += 1
        power *= p
    return r
```

Putting implementation specific to Fraction fields in a global function is bad practice. And since fraction fields have an implementation of valuation part of the above code will not be execucted. If it magicaly get's excecuted it will return bad results since it doesn't take into account the input variable "p" as it should.

Issue created by migration from https://trac.sagemath.org/ticket/9652





---

archive/issue_comments_093480.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-31T20:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93480",
    "user": "https://github.com/koffie"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093481.json:
```json
{
    "body": "Two questions:\n\n* Is there any case in which any code after `return infinity` is executed and succesful?\n* Is there any case in which any code after `return m.valuation(...)` is executed and useful?\n\nCan't you remove a lot more while you are at it? The code seems to be there to catch off weird unexpected cases that don't have a valuation attribute, but\n\n1. if the case is weird enough, then nothing guarantees that this function terminates\n2. if the case happens to have a negative valuation, then the function returns 0 instead of a negative number\n\nWhile you are at it, I found that the function doesn't handle the valuation attribute of power series well (because it doesn't allow you to specify the (unique) prime p).\n\n```\nx = QQ[['x']].gen()\nvaluation(x^2, x)\nTypeError: valuation() takes no arguments (1 given)\nvaluation(x^2)\nTypeError: valuation() takes exactly 2 arguments (1 given)\n```\nThe first error is because `PowerSeries.valuation()` takes no arguments; the second is because the global function takes exactly 2 arguments.\n\nHow about defining the global function simply as follows?\n\n```\ndef valuation(m, *args1, **args2):\n    return m.valuation(*args1, **args2)\n```\nor\n\n```\ndef valuation(m, *args1, **args2):\n    if m == 0:\n        return sage.rings.all.infinity\n    return m.valuation(*args1, **args2)\n```\nI haven't tried and/or ran any doctests with this, but anything that is broken by this isn't good coding practice, as you said :) Plus this fixes my example with `valuation(x^2)`.",
    "created_at": "2010-08-02T14:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93481",
    "user": "https://github.com/mstreng"
}
```

Two questions:

* Is there any case in which any code after `return infinity` is executed and succesful?
* Is there any case in which any code after `return m.valuation(...)` is executed and useful?

Can't you remove a lot more while you are at it? The code seems to be there to catch off weird unexpected cases that don't have a valuation attribute, but

1. if the case is weird enough, then nothing guarantees that this function terminates
2. if the case happens to have a negative valuation, then the function returns 0 instead of a negative number

While you are at it, I found that the function doesn't handle the valuation attribute of power series well (because it doesn't allow you to specify the (unique) prime p).

```
x = QQ[['x']].gen()
valuation(x^2, x)
TypeError: valuation() takes no arguments (1 given)
valuation(x^2)
TypeError: valuation() takes exactly 2 arguments (1 given)
```
The first error is because `PowerSeries.valuation()` takes no arguments; the second is because the global function takes exactly 2 arguments.

How about defining the global function simply as follows?

```
def valuation(m, *args1, **args2):
    return m.valuation(*args1, **args2)
```
or

```
def valuation(m, *args1, **args2):
    if m == 0:
        return sage.rings.all.infinity
    return m.valuation(*args1, **args2)
```
I haven't tried and/or ran any doctests with this, but anything that is broken by this isn't good coding practice, as you said :) Plus this fixes my example with `valuation(x^2)`.



---

archive/issue_comments_093482.json:
```json
{
    "body": "I guess the code underneath there is for python integers, but I'm not sure. I will look into your questions when I have the time.\n\nps. similar practices seem to be going on a lot in arith.py I created a discussion on sage-devel. This discussion is not so much to discuss this specific example in detail, but to find a nice general solution for dealing with the problems involved when both using global functions an class methods to do the same thing.\n\nI guess your remark about just passing all the aruments to the class method instead of having a static signature should be of value in that discussion also.",
    "created_at": "2010-08-02T15:06:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93482",
    "user": "https://github.com/koffie"
}
```

I guess the code underneath there is for python integers, but I'm not sure. I will look into your questions when I have the time.

ps. similar practices seem to be going on a lot in arith.py I created a discussion on sage-devel. This discussion is not so much to discuss this specific example in detail, but to find a nice general solution for dealing with the problems involved when both using global functions an class methods to do the same thing.

I guess your remark about just passing all the aruments to the class method instead of having a static signature should be of value in that discussion also.



---

archive/issue_comments_093483.json:
```json
{
    "body": "The code is indeed for python integers, and produces the right output in that case as the following shows.\n\n```\nsage: a=344r\nsage: type(a)\n<type 'int'>\nsage: hasattr(a,\"valuation\")\nFalse\nsage: valuation(a,2)\n3\n```\n\nI agree with you that that code should not be excecuted on general ring elements.\n\nIt crashes on local elements of the symbolic ring for example.\n\n```\nsage: var(\"z\")\nz\nsage: valuation(z^2,z)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Applications/sage/devel/sage-mderickx/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/rings/arith.pyc in valuation(m, p)\n    604     r = 0\n    605     power = p\n--> 606     while not (m % power): # m % power == 0\n    607         r += 1\n    608         power *= p\n\nTypeError: unsupported operand type(s) for %: 'sage.symbolic.expression.Expression' and 'sage.symbolic.expression.Expression'\n```\n.\n\nIn your remark 2. The code could also crash, for example try (1/2) % 2.\nI tried to find some real examples in sage, but I can't seem to find how to localize rings in sage. Maybe it's not implemented yet. The only thing I could find is: http://www.sagemath.org/doc/reference/coercion.html#example.\n\nMy failing quest to find other examples than python integers lead me to believe that this code should indeed only be excecuted on python integers.",
    "created_at": "2010-08-02T16:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93483",
    "user": "https://github.com/koffie"
}
```

The code is indeed for python integers, and produces the right output in that case as the following shows.

```
sage: a=344r
sage: type(a)
<type 'int'>
sage: hasattr(a,"valuation")
False
sage: valuation(a,2)
3
```

I agree with you that that code should not be excecuted on general ring elements.

It crashes on local elements of the symbolic ring for example.

```
sage: var("z")
z
sage: valuation(z^2,z)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Applications/sage/devel/sage-mderickx/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/arith.pyc in valuation(m, p)
    604     r = 0
    605     power = p
--> 606     while not (m % power): # m % power == 0
    607         r += 1
    608         power *= p

TypeError: unsupported operand type(s) for %: 'sage.symbolic.expression.Expression' and 'sage.symbolic.expression.Expression'
```
.

In your remark 2. The code could also crash, for example try (1/2) % 2.
I tried to find some real examples in sage, but I can't seem to find how to localize rings in sage. Maybe it's not implemented yet. The only thing I could find is: http://www.sagemath.org/doc/reference/coercion.html#example.

My failing quest to find other examples than python integers lead me to believe that this code should indeed only be excecuted on python integers.



---

archive/issue_comments_093484.json:
```json
{
    "body": "Ah yes, python integers. Then perhaps first test if m is a python integer and call `Integer(m).valuation(*args1, **args2)` if it is and `m.valuation(*args1, **args2)` otherwise. I think you should leave out the `m == 0` check because nobody wants `valuation(0, 0)` or `valuation(0, 'whatever')` to give any output.",
    "created_at": "2010-08-02T17:18:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93484",
    "user": "https://github.com/mstreng"
}
```

Ah yes, python integers. Then perhaps first test if m is a python integer and call `Integer(m).valuation(*args1, **args2)` if it is and `m.valuation(*args1, **args2)` otherwise. I think you should leave out the `m == 0` check because nobody wants `valuation(0, 0)` or `valuation(0, 'whatever')` to give any output.



---

archive/issue_comments_093485.json:
```json
{
    "body": "`valuation(int(1), int(1))` goes into an infinite loop",
    "created_at": "2010-08-02T18:06:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93485",
    "user": "https://github.com/mstreng"
}
```

`valuation(int(1), int(1))` goes into an infinite loop



---

archive/issue_comments_093486.json:
```json
{
    "body": "Ok so the code behaves buggy for valuation(1r,1r).  I really think we should just let sage integers handle it. I really don't like having unneccery double code. Especially if one of the two is buggy.\n\nBy the way, the problem with valuation(0r,0r) is not just a problem of this code, it also happes with valuation on sage ints. Should we report that as a bug?\n\n```\nsage: 0.valuation(0)\n+Infinity\nsage: 8.valuation(0)\nValueError                                Traceback (most recent call last)\n...\nValueError: You can only compute the valuation with respect to a integer larger than 1.\n```\nps. if you want a number to not be converted to a sage integer by the preparser you should just put an r behind the number. Or else the preparser will generate the following silly code:\n\n```\nsage: preparse(\"valuation(int(1),int(1)\")\n'valuation(int(Integer(1)),int(Integer(1))'\n```\nWhat you want is this:\n\n```\nsage: preparse(\"valuation(1r,1r)\")\n'valuation(1,1)'\n```",
    "created_at": "2010-08-02T18:38:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93486",
    "user": "https://github.com/koffie"
}
```

Ok so the code behaves buggy for valuation(1r,1r).  I really think we should just let sage integers handle it. I really don't like having unneccery double code. Especially if one of the two is buggy.

By the way, the problem with valuation(0r,0r) is not just a problem of this code, it also happes with valuation on sage ints. Should we report that as a bug?

```
sage: 0.valuation(0)
+Infinity
sage: 8.valuation(0)
ValueError                                Traceback (most recent call last)
...
ValueError: You can only compute the valuation with respect to a integer larger than 1.
```
ps. if you want a number to not be converted to a sage integer by the preparser you should just put an r behind the number. Or else the preparser will generate the following silly code:

```
sage: preparse("valuation(int(1),int(1)")
'valuation(int(Integer(1)),int(Integer(1))'
```
What you want is this:

```
sage: preparse("valuation(1r,1r)")
'valuation(1,1)'
```



---

archive/issue_comments_093487.json:
```json
{
    "body": "Attachment [smallfix1-arith_valuation.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation.patch) by @koffie created at 2010-08-02 18:57:05",
    "created_at": "2010-08-02T18:57:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93487",
    "user": "https://github.com/koffie"
}
```

Attachment [smallfix1-arith_valuation.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation.patch) by @koffie created at 2010-08-02 18:57:05



---

archive/issue_comments_093488.json:
```json
{
    "body": "You have added the extra arguments but have not documented them, or given any examples where they might be used.  That's not good!\n\nFor the main code, why not do\n\n```\ntry:\n  return m.valuation(p)\nexcept AttributeError:\n   pass\ntry:\n   return Integer(m).valuation(Integer(p))\nexcept (something):\n   raise an error\n```",
    "created_at": "2010-08-22T13:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93488",
    "user": "https://github.com/JohnCremona"
}
```

You have added the extra arguments but have not documented them, or given any examples where they might be used.  That's not good!

For the main code, why not do

```
try:
  return m.valuation(p)
except AttributeError:
   pass
try:
   return Integer(m).valuation(Integer(p))
except (something):
   raise an error
```



---

archive/issue_comments_093489.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-22T13:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93489",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093490.json:
```json
{
    "body": "Wasn't the whole point of the extra arguments *args1, **args2 to make the global function `valuation` also work for power series? It doesn't in the current Sage, and it wouldn't with John's suggestion, but actually, it also doesn't with Maarten's patch.\n\nTo make it work, remove p. That is, replace \"`p,*args1, **args2`\" by \"`*args1, **args2`\" or simply \"`*args1`\" both times it occurs in your patch.\n\nIn the EXAMPLES block, you could add\n\n```\nsage: y = QQ['y'].gen()\nsage: valuation(y^3, y)\n3\nsage: x = QQ[['x']].gen()\nsage: valuation(x^2)\n2\n```\n\nThis doesn't really belong to the topic of this patch, but as you are rewriting the function anyway...",
    "created_at": "2010-08-22T19:55:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93490",
    "user": "https://github.com/mstreng"
}
```

Wasn't the whole point of the extra arguments *args1, **args2 to make the global function `valuation` also work for power series? It doesn't in the current Sage, and it wouldn't with John's suggestion, but actually, it also doesn't with Maarten's patch.

To make it work, remove p. That is, replace "`p,*args1, **args2`" by "`*args1, **args2`" or simply "`*args1`" both times it occurs in your patch.

In the EXAMPLES block, you could add

```
sage: y = QQ['y'].gen()
sage: valuation(y^3, y)
3
sage: x = QQ[['x']].gen()
sage: valuation(x^2)
2
```

This doesn't really belong to the topic of this patch, but as you are rewriting the function anyway...



---

archive/issue_comments_093491.json:
```json
{
    "body": "That looks better!",
    "created_at": "2010-08-22T20:57:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93491",
    "user": "https://github.com/JohnCremona"
}
```

That looks better!



---

archive/issue_comments_093492.json:
```json
{
    "body": "I added a second patch which takes most of the comments into account. (please only apply the second patch, it got added as a second patch since I forgot to check the \"replace existing file\" box).\n\nI didn't do anything with the \"For the main code, why not !do:\" suggestion since to me it seemed to do the same thing but then with a different coding style. (My version is the \"look before you leap version\", and yours the \"Easier to ask for forgiveness than permission.\"). If there are reasons to chose one above the other I would certainly do that. I know that my code will raise an attribute error sometimes, an error that you would rewrite in your case. But I guess that error should be not confusing at all to the enduser.\n\n```\n\nsage: valuation(graphs.!PetersenGraph())\n\n---------------------------------------------------------------------------\n\n!AttributeError \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0 \u00a0Traceback (most recent call last)\n\n/Users/maarten/<ipython console> in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/rings/arith.pyc in valuation(m, *args1, **args2)\n\n\u00a0\u00a0 \u00a0600 \u00a0 \u00a0 if isinstance(m,(int,long)):\n\n\u00a0\u00a0 \u00a0601 \u00a0 \u00a0 \u00a0 \u00a0 m=Integer(m)\n\n--> 602 \u00a0 \u00a0 return m.valuation(*args1, **args2)\n\n\u00a0\u00a0 \u00a0603\u00a0\n\n\u00a0\u00a0 \u00a0604 def prime_powers(start, stop=None):\n\n!AttributeError: 'Graph' object has no attribute 'valuation'\n\nsage:\u00a0\n\n```",
    "created_at": "2010-09-06T17:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93492",
    "user": "https://github.com/koffie"
}
```

I added a second patch which takes most of the comments into account. (please only apply the second patch, it got added as a second patch since I forgot to check the "replace existing file" box).

I didn't do anything with the "For the main code, why not !do:" suggestion since to me it seemed to do the same thing but then with a different coding style. (My version is the "look before you leap version", and yours the "Easier to ask for forgiveness than permission."). If there are reasons to chose one above the other I would certainly do that. I know that my code will raise an attribute error sometimes, an error that you would rewrite in your case. But I guess that error should be not confusing at all to the enduser.

```

sage: valuation(graphs.!PetersenGraph())

---------------------------------------------------------------------------

!AttributeError                            Traceback (most recent call last)

/Users/maarten/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/arith.pyc in valuation(m, *args1, **args2)

    600     if isinstance(m,(int,long)):

    601         m=Integer(m)

--> 602     return m.valuation(*args1, **args2)

    603 

    604 def prime_powers(start, stop=None):

!AttributeError: 'Graph' object has no attribute 'valuation'

sage: 

```



---

archive/issue_comments_093493.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-06T17:21:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93493",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093494.json:
```json
{
    "body": "You have to import \"Integer\" somewhere in the code:\n\n```\nsage: a=int(3)\nsage: valuation(a,2)\n...\n--> 695         m=Integer(m)\n...\nNameError: global name 'Integer' is not defined\n```\n\nAdd a doctest that uses an 'int' as argument to check that the previous code will work.\n\nIn the documentation, it says that valuation os zero is +Infinity but valuation with respect to zero is an error. However:\n\n```\nsage: valuation(0,0)\n+Infinity\nsage: K=QQ['x']\nsage: x=K.gen()\nsage: valuation(x,K(0))\n...\nPariError\nsage: valuation(K(0),K(0))\n+Infinity\n```",
    "created_at": "2010-09-08T13:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93494",
    "user": "https://github.com/lftabera"
}
```

You have to import "Integer" somewhere in the code:

```
sage: a=int(3)
sage: valuation(a,2)
...
--> 695         m=Integer(m)
...
NameError: global name 'Integer' is not defined
```

Add a doctest that uses an 'int' as argument to check that the previous code will work.

In the documentation, it says that valuation os zero is +Infinity but valuation with respect to zero is an error. However:

```
sage: valuation(0,0)
+Infinity
sage: K=QQ['x']
sage: x=K.gen()
sage: valuation(x,K(0))
...
PariError
sage: valuation(K(0),K(0))
+Infinity
```



---

archive/issue_comments_093495.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-08T13:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93495",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093496.json:
```json
{
    "body": "Why do you let the code work for float, but not for RealNumber? (I wouldn't let it work for float at all.)",
    "created_at": "2010-09-08T14:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93496",
    "user": "https://github.com/mstreng"
}
```

Why do you let the code work for float, but not for RealNumber? (I wouldn't let it work for float at all.)



---

archive/issue_comments_093497.json:
```json
{
    "body": "Replying to [comment:14 mstreng]:\n> Why do you let the code work for float, but not for RealNumber? (I wouldn't let it work for float at all.)\n\n\nCould you elaborate that? For me, the code fails for floats with an AttributeError exception (as well as RealNumber).",
    "created_at": "2010-09-08T15:48:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93497",
    "user": "https://github.com/lftabera"
}
```

Replying to [comment:14 mstreng]:
> Why do you let the code work for float, but not for RealNumber? (I wouldn't let it work for float at all.)


Could you elaborate that? For me, the code fails for floats with an AttributeError exception (as well as RealNumber).



---

archive/issue_comments_093498.json:
```json
{
    "body": "I talked with Marco (mstreng) in real live. And his comment should be ignored as it was based on something he misread.",
    "created_at": "2010-09-08T18:27:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93498",
    "user": "https://github.com/koffie"
}
```

I talked with Marco (mstreng) in real live. And his comment should be ignored as it was based on something he misread.



---

archive/issue_comments_093499.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-08T21:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93499",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093500.json:
```json
{
    "body": "I added the import and doctest as lftabera suggested. \n\nI didn't do anything with the comment about QQ['x'] since I already changed the documentation of the global function to say that you really should look at the documentation of the attribute functions. And the behaviour you show is consistent with the documentation of the attribute function.",
    "created_at": "2010-09-08T21:36:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93500",
    "user": "https://github.com/koffie"
}
```

I added the import and doctest as lftabera suggested. 

I didn't do anything with the comment about QQ['x'] since I already changed the documentation of the global function to say that you really should look at the documentation of the attribute functions. And the behaviour you show is consistent with the documentation of the attribute function.



---

archive/issue_comments_093501.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-10T07:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93501",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093502.json:
```json
{
    "body": "I found the following doctest failures (4.5.2):\n\nsage -t -long \"devel/sage-devel/sage/quadratic_forms/count_local_2.pyx\"\n\nsage -t -long \"devel/sage-devel/sage/quadratic_forms/quadratic_form__count_local_2.py\"\n\nsage -t -long \"devel/sage-devel/sage/quadratic_forms/quadratic_form__local_density_congruence.py\"\n\nsage -t -long \"devel/sage-devel/sage/quadratic_forms/quadratic_form__local_representation_conditions.py\"\n\n\nall related with\n\nAttributeError: 'sage.rings.finite_rings.integer_mod.IntegerMod_int' object has no attribute 'valuation'\n\n\n\nAlso, in the code, you import Integers in the case of 'int' or 'float'. However, the local namespace of arith contains ZZ. I have checked and it is fastr to use ZZ(m) instead of importing Integer and using Integer(m). This is a corner case though.",
    "created_at": "2010-09-10T07:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93502",
    "user": "https://github.com/lftabera"
}
```

I found the following doctest failures (4.5.2):

sage -t -long "devel/sage-devel/sage/quadratic_forms/count_local_2.pyx"

sage -t -long "devel/sage-devel/sage/quadratic_forms/quadratic_form__count_local_2.py"

sage -t -long "devel/sage-devel/sage/quadratic_forms/quadratic_form__local_density_congruence.py"

sage -t -long "devel/sage-devel/sage/quadratic_forms/quadratic_form__local_representation_conditions.py"


all related with

AttributeError: 'sage.rings.finite_rings.integer_mod.IntegerMod_int' object has no attribute 'valuation'



Also, in the code, you import Integers in the case of 'int' or 'float'. However, the local namespace of arith contains ZZ. I have checked and it is fastr to use ZZ(m) instead of importing Integer and using Integer(m). This is a corner case though.



---

archive/issue_comments_093503.json:
```json
{
    "body": "Is there somewhere in the math literature a definition of what a valuation should be for \"Ring of integers modulo n\", cause the way it behaves right now in sage doesn't agree with my definition of what conditions a valuation should satisfy. If v is a valuation then in particular I would like to have v(a*b)=v(a)+v(b). But in sage right now you get the following:\n\n sage: for i in R: \n....:     for j in R: \n....:         if not valuation(i,Integer(3))+valuation(j,Integer(3))==valuation(i*j,Integer(3)):\n....:             print i,j\n....:             \n3 3\n3 6\n6 3\n6 6",
    "created_at": "2010-09-10T12:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93503",
    "user": "https://github.com/koffie"
}
```

Is there somewhere in the math literature a definition of what a valuation should be for "Ring of integers modulo n", cause the way it behaves right now in sage doesn't agree with my definition of what conditions a valuation should satisfy. If v is a valuation then in particular I would like to have v(a*b)=v(a)+v(b). But in sage right now you get the following:

 sage: for i in R: 
....:     for j in R: 
....:         if not valuation(i,Integer(3))+valuation(j,Integer(3))==valuation(i*j,Integer(3)):
....:             print i,j
....:             
3 3
3 6
6 3
6 6



---

archive/issue_comments_093504.json:
```json
{
    "body": "oops, now with the right formatting:\n\n```\n\n sage: for i in R: \n....:     for j in R: \n....:         if not valuation(i,Integer(3))+valuation(j,Integer(3))==valuation(i*j,Integer(3)):\n....:             print i,j\n....:             \n3 3\n3 6\n6 3\n6 6\n```",
    "created_at": "2010-09-10T12:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93504",
    "user": "https://github.com/koffie"
}
```

oops, now with the right formatting:

```

 sage: for i in R: 
....:     for j in R: 
....:         if not valuation(i,Integer(3))+valuation(j,Integer(3))==valuation(i*j,Integer(3)):
....:             print i,j
....:             
3 3
3 6
6 3
6 6
```



---

archive/issue_comments_093505.json:
```json
{
    "body": "By the way: R=ZZ.quo(9)",
    "created_at": "2010-09-10T12:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93505",
    "user": "https://github.com/koffie"
}
```

By the way: R=ZZ.quo(9)



---

archive/issue_comments_093506.json:
```json
{
    "body": "I am afraid that there are quite a bit of algorithms in SAGE that deal with IntegerModInt as plain Integer. The algorithms work, but you may fail to give a standar mathematical sense to them. This would be an example.",
    "created_at": "2010-09-10T13:12:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93506",
    "user": "https://github.com/lftabera"
}
```

I am afraid that there are quite a bit of algorithms in SAGE that deal with IntegerModInt as plain Integer. The algorithms work, but you may fail to give a standar mathematical sense to them. This would be an example.



---

archive/issue_comments_093507.json:
```json
{
    "body": "Ok, then i'll just move the relevant parts of the old code so it becomes an attribute function of\u00a0IntegerModInt\u00a0together with a note section that sais that it's not a valuation in the mathematical sense.",
    "created_at": "2010-09-10T13:39:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93507",
    "user": "https://github.com/koffie"
}
```

Ok, then i'll just move the relevant parts of the old code so it becomes an attribute function of IntegerModInt together with a note section that sais that it's not a valuation in the mathematical sense.



---

archive/issue_comments_093508.json:
```json
{
    "body": "Changing assignee from @aghitza to @koffie.",
    "created_at": "2010-09-11T08:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93508",
    "user": "https://github.com/koffie"
}
```

Changing assignee from @aghitza to @koffie.



---

archive/issue_comments_093509.json:
```json
{
    "body": "Use this one, the other is an old version",
    "created_at": "2010-09-11T08:54:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93509",
    "user": "https://github.com/koffie"
}
```

Use this one, the other is an old version



---

archive/issue_comments_093510.json:
```json
{
    "body": "Attachment [smallfix1-arith_valuation.2.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation.2.patch) by @koffie created at 2010-09-11 08:56:48\n\nOk, I moved the code, and the integer mod classes now also have a valuation attribute. All doctest should pass now when patching against 4.4.4 (sorry haven't updated in a while).",
    "created_at": "2010-09-11T08:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93510",
    "user": "https://github.com/koffie"
}
```

Attachment [smallfix1-arith_valuation.2.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation.2.patch) by @koffie created at 2010-09-11 08:56:48

Ok, I moved the code, and the integer mod classes now also have a valuation attribute. All doctest should pass now when patching against 4.4.4 (sorry haven't updated in a while).



---

archive/issue_comments_093511.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-11T08:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93511",
    "user": "https://github.com/koffie"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093512.json:
```json
{
    "body": "Attachment [smallfix1-arith_valuation.2.2.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation.2.2.patch) by @koffie created at 2010-09-12 10:52:26\n\nUse this one, the other is an old version",
    "created_at": "2010-09-12T10:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93512",
    "user": "https://github.com/koffie"
}
```

Attachment [smallfix1-arith_valuation.2.2.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation.2.2.patch) by @koffie created at 2010-09-12 10:52:26

Use this one, the other is an old version



---

archive/issue_comments_093513.json:
```json
{
    "body": "previous patch with clenaer comment in the header",
    "created_at": "2010-09-14T11:26:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93513",
    "user": "https://github.com/lftabera"
}
```

previous patch with clenaer comment in the header



---

archive/issue_comments_093514.json:
```json
{
    "body": "Attachment [smallfix1-arith_valuation-doctest.2.3.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation-doctest.2.3.patch) by @lftabera created at 2010-09-14 11:27:08\n\nadditional doctest",
    "created_at": "2010-09-14T11:27:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93514",
    "user": "https://github.com/lftabera"
}
```

Attachment [smallfix1-arith_valuation-doctest.2.3.patch](tarball://root/attachments/some-uuid/ticket9652/smallfix1-arith_valuation-doctest.2.3.patch) by @lftabera created at 2010-09-14 11:27:08

additional doctest



---

archive/issue_comments_093515.json:
```json
{
    "body": "Everything looks fine. Applies and passes doctest in 4.5.3\n\nI have modified the header of the patch in smallfix1-arith_valuation.2.3.patch and I have added another patch with a new doctest regarding a previous issue that arrived before valuation(1r,1r) not terminating.\n\nSince I have not touched the code, I fell I can give possitive review, but before doing so, mderickx, give me the OK for the change in the header of your patch.",
    "created_at": "2010-09-14T11:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93515",
    "user": "https://github.com/lftabera"
}
```

Everything looks fine. Applies and passes doctest in 4.5.3

I have modified the header of the patch in smallfix1-arith_valuation.2.3.patch and I have added another patch with a new doctest regarding a previous issue that arrived before valuation(1r,1r) not terminating.

Since I have not touched the code, I fell I can give possitive review, but before doing so, mderickx, give me the OK for the change in the header of your patch.



---

archive/issue_comments_093516.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-14T11:30:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93516",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_093517.json:
```json
{
    "body": "I'm ok with the changes. Hooray, my first patch got through :).",
    "created_at": "2010-09-14T11:59:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93517",
    "user": "https://github.com/koffie"
}
```

I'm ok with the changes. Hooray, my first patch got through :).



---

archive/issue_comments_093518.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-14T12:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93518",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_093519.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-14T12:32:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93519",
    "user": "https://github.com/lftabera"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093520.json:
```json
{
    "body": "Please remember to update the \"Author(s)\" and \"Reviewer(s)\" fields.",
    "created_at": "2010-09-15T11:06:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93520",
    "user": "https://github.com/qed777"
}
```

Please remember to update the "Author(s)" and "Reviewer(s)" fields.



---

archive/issue_events_024062.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T11:06:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9652#event-24062"
}
```



---

archive/issue_events_024063.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-09-15T11:14:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9652#event-24063"
}
```



---

archive/issue_comments_093521.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-15T11:14:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9652",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9652#issuecomment-93521",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
