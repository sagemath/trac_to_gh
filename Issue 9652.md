# Issue 9652: Unnecesary and buggy code in arith.py

Issue created by migration from Trac.

Original creator: mderickx

Original creation time: 2010-07-31 20:35:45

Assignee: AlexGhitza

CC:  mstreng lftabera

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


---

Comment by mderickx created at 2010-07-31 20:39:32

Changing status from new to needs_review.


---

Comment by mstreng created at 2010-08-02 14:39:57

Two questions:

 * Is there any case in which any code after `return infinity` is executed and succesful?
 * Is there any case in which any code after `return m.valuation(...)` is executed and useful?

Can't you remove a lot more while you are at it? The code seems to be there to catch off weird unexpected cases that don't have a valuation attribute, but

 1. if the case is weird enough, then nothing guarantees that this function terminates
 2. if the case happens to have a negative valuation, then the function returns 0 instead of a negative number

While you are at it, I found that the function doesn't handle the valuation attribute of power series well (because it doesn't allow you to specify the (unique) prime p).


```
x = QQ[This is the Trac macro *'x'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'x'-macro).gen()
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

Comment by mderickx created at 2010-08-02 15:06:53

I guess the code underneath there is for python integers, but I'm not sure. I will look into your questions when I have the time.

ps. similar practices seem to be going on a lot in arith.py I created a discussion on sage-devel. This discussion is not so much to discuss this specific example in detail, but to find a nice general solution for dealing with the problems involved when both using global functions an class methods to do the same thing.

I guess your remark about just passing all the aruments to the class method instead of having a static signature should be of value in that discussion also.


---

Comment by mderickx created at 2010-08-02 16:57:26

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

Comment by mstreng created at 2010-08-02 17:18:04

Ah yes, python integers. Then perhaps first test if m is a python integer and call `Integer(m).valuation(*args1, **args2)` if it is and `m.valuation(*args1, **args2)` otherwise. I think you should leave out the `m == 0` check because nobody wants `valuation(0, 0)` or `valuation(0, 'whatever')` to give any output.


---

Comment by mstreng created at 2010-08-02 18:06:21

`valuation(int(1), int(1))` goes into an infinite loop


---

Comment by mderickx created at 2010-08-02 18:38:02

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

Attachment


---

Comment by cremona created at 2010-08-22 13:16:42

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

Comment by cremona created at 2010-08-22 13:16:42

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-08-22 19:55:10

Wasn't the whole point of the extra arguments *args1, **args2 to make the global function `valuation` also work for power series? It doesn't in the current Sage, and it wouldn't with John's suggestion, but actually, it also doesn't with Maarten's patch.

To make it work, remove p. That is, replace "`p,*args1, **args2`" by "`*args1, **args2`" or simply "`*args1`" both times it occurs in your patch.

In the EXAMPLES block, you could add

```
sage: y = QQ['y'].gen()
sage: valuation(y^3, y)
3
sage: x = QQ[This is the Trac macro *'x'* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#'x'-macro).gen()
sage: valuation(x^2)
2
```


This doesn't really belong to the topic of this patch, but as you are rewriting the function anyway...


---

Comment by cremona created at 2010-08-22 20:57:58

That looks better!


---

Comment by mderickx created at 2010-09-06 17:21:54

I added a second patch which takes most of the comments into account. (please only apply the second patch, it got added as a second patch since I forgot to check the "replace existing file" box).

I didn't do anything with the "For the main code, why not !do:" suggestion since to me it seemed to do the same thing but then with a different coding style. (My version is the "look before you leap version", and yours the "Easier to ask for forgiveness than permission."). If there are reasons to chose one above the other I would certainly do that. I know that my code will raise an attribute error sometimes, an error that you would rewrite in your case. But I guess that error should be not confusing at all to the enduser.


```

sage: valuation(graphs.PetersenGraph())

---------------------------------------------------------------------------

AttributeError                            Traceback (most recent call last)

/Users/maarten/<ipython console> in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/rings/arith.pyc in valuation(m, *args1, **args2)

    600     if isinstance(m,(int,long)):

    601         m=Integer(m)

--> 602     return m.valuation(*args1, **args2)

    603 

    604 def prime_powers(start, stop=None):

AttributeError: 'Graph' object has no attribute 'valuation'

sage: 

```



---

Comment by mderickx created at 2010-09-06 17:21:54

Changing status from needs_work to needs_review.


---

Comment by lftabera created at 2010-09-08 13:35:21

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

Comment by lftabera created at 2010-09-08 13:35:21

Changing status from needs_review to needs_work.


---

Comment by mstreng created at 2010-09-08 14:17:14

Why do you let the code work for float, but not for RealNumber? (I wouldn't let it work for float at all.)


---

Comment by lftabera created at 2010-09-08 15:48:07

Replying to [comment:14 mstreng]:
> Why do you let the code work for float, but not for RealNumber? (I wouldn't let it work for float at all.)

Could you elaborate that? For me, the code fails for floats with an AttributeError exception (as well as RealNumber).


---

Comment by mderickx created at 2010-09-08 18:27:57

I talked with Marco (mstreng) in real live. And his comment should be ignored as it was based on something he misread.


---

Comment by mderickx created at 2010-09-08 21:36:19

Changing status from needs_work to needs_review.


---

Comment by mderickx created at 2010-09-08 21:36:19

I added the import and doctest as lftabera suggested. 

I didn't do anything with the comment about QQ['x'] since I already changed the documentation of the global function to say that you really should look at the documentation of the attribute functions. And the behaviour you show is consistent with the documentation of the attribute function.


---

Comment by lftabera created at 2010-09-10 07:45:39

Changing status from needs_review to needs_work.


---

Comment by lftabera created at 2010-09-10 07:45:39

I found the following doctest failures (4.5.2):

sage -t -long "devel/sage-devel/sage/quadratic_forms/count_local_2.pyx"

sage -t -long "devel/sage-devel/sage/quadratic_forms/quadratic_form__count_local_2.py"

sage -t -long "devel/sage-devel/sage/quadratic_forms/quadratic_form__local_density_congruence.py"

sage -t -long "devel/sage-devel/sage/quadratic_forms/quadratic_form__local_representation_conditions.py"


all related with

AttributeError: 'sage.rings.finite_rings.integer_mod.IntegerMod_int' object has no attribute 'valuation'



Also, in the code, you import Integers in the case of 'int' or 'float'. However, the local namespace of arith contains ZZ. I have checked and it is fastr to use ZZ(m) instead of importing Integer and using Integer(m). This is a corner case though.


---

Comment by mderickx created at 2010-09-10 12:18:22

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

Comment by mderickx created at 2010-09-10 12:19:03

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

Comment by mderickx created at 2010-09-10 12:19:59

By the way: R=ZZ.quo(9)


---

Comment by lftabera created at 2010-09-10 13:12:58

I am afraid that there are quite a bit of algorithms in SAGE that deal with IntegerModInt as plain Integer. The algorithms work, but you may fail to give a standar mathematical sense to them. This would be an example.


---

Comment by mderickx created at 2010-09-10 13:39:33

Ok, then i'll just move the relevant parts of the old code so it becomes an attribute function of IntegerModInt together with a note section that sais that it's not a valuation in the mathematical sense.


---

Comment by mderickx created at 2010-09-11 08:53:24

Changing assignee from AlexGhitza to mderickx.


---

Comment by mderickx created at 2010-09-11 08:54:12

Use this one, the other is an old version


---

Attachment

Ok, I moved the code, and the integer mod classes now also have a valuation attribute. All doctest should pass now when patching against 4.4.4 (sorry haven't updated in a while).


---

Comment by mderickx created at 2010-09-11 08:56:48

Changing status from needs_work to needs_review.


---

Attachment

Use this one, the other is an old version


---

Comment by lftabera created at 2010-09-14 11:26:54

previous patch with clenaer comment in the header


---

Attachment

additional doctest


---

Comment by lftabera created at 2010-09-14 11:30:37

Everything looks fine. Applies and passes doctest in 4.5.3

I have modified the header of the patch in smallfix1-arith_valuation.2.3.patch and I have added another patch with a new doctest regarding a previous issue that arrived before valuation(1r,1r) not terminating.

Since I have not touched the code, I fell I can give possitive review, but before doing so, mderickx, give me the OK for the change in the header of your patch.


---

Comment by lftabera created at 2010-09-14 11:30:37

Changing status from needs_review to needs_info.


---

Comment by mderickx created at 2010-09-14 11:59:29

I'm ok with the changes. Hooray, my first patch got through :).


---

Comment by lftabera created at 2010-09-14 12:32:29

Changing status from needs_info to needs_review.


---

Comment by lftabera created at 2010-09-14 12:32:39

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:06:49

Please remember to update the "Author(s)" and "Reviewer(s)" fields.


---

Comment by mpatel created at 2010-09-15 11:14:02

Resolution: fixed
