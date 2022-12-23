# Issue 9934: Make a symbolic mod function

Issue created by migration from https://trac.sagemath.org/ticket/9935

Original creator: jason

Original creation time: 2010-09-17 20:17:56

Assignee: burcin

CC:  burcin jdemeyer rws

A participant in the PREP program noticed that mod is not a symbolic function:


```
sage: mod(x,4)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (4562, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (4530, 0))

ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (842, 0))

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/grout/sage-4.5.2/devel/sage-main/sage/functions/<ipython console> in <module>()

/home/grout/sage/local/lib/python2.6/site-packages/sage/rings/finite_rings/integer_mod.so in sage.rings.finite_rings.integer_mod.Mod (sage/rings/finite_rings/integer_mod.c:2633)()

/home/grout/sage/local/lib/python2.6/site-packages/sage/rings/finite_rings/integer_mod.so in sage.rings.finite_rings.integer_mod.IntegerMod (sage/rings/finite_rings/integer_mod.c:2952)()

/home/grout/sage/local/lib/python2.6/site-packages/sage/rings/finite_rings/integer_mod.so in sage.rings.finite_rings.integer_mod.IntegerMod_int.__init__ (sage/rings/finite_rings/integer_mod.c:14249)()

/home/grout/sage/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:6407)()

/home/grout/sage/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4053)()

/home/grout/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._integer_ (sage/symbolic/expression.cpp:4026)()

TypeError: unable to convert x (=x) to an integer
```


Hopefully it should be easy to wrap mod in a symbolic function, something like:


```
sage: def eval_mod(self, x):
....:     if isinstance(x, (int, Integer)):
....:         return mod(x,5)
....:     return None
....:
sage: f=function('f', eval_func=eval_mod)
sage: f(x)
f(x)
sage: f(13)
3
sage: f(x^2+x+1)
f(x^2 + x + 1)
sage: f(x^2+x+1).subs(x=2)
2
sage: f(x^2+x+1).subs(x=3)
3
sage: f(x^2+x^3).subs(x=1)
2
sage: f(x^2+x^3).subs(x=2)
2
sage: f(x^2+x^3).subs(x=3)
1 
```



---

Comment by jason created at 2010-09-17 20:18:53

Burcin, is there a nice example somewhere that we can just copy and modify to make a symbolic function?  This sounds like it would be easy for a beginner to do if there was a good example almost like it somewhere.


---

Comment by burcin created at 2010-09-18 22:05:52

There are plenty of examples in the directory `sage/functions/`, just look for classes deriving from `BuiltinFunction`. You'll probably want to deprecate the `parent` keyword argument to `mod()`, so `sage.functions.transcendental.Function_exp_integral` might provide a good template.


---

Comment by mkoeppe created at 2016-08-10 20:50:02

We still don't have a good "mod".
I would suspect that this has been discussed at length in the past years.

I'm bringing this up because I'm in need of periodic piecewise functions (#21215). Using a suitable symbolic mod would be one way. 
On Mathematica, using their 3-argument Mod function seems to be the standard way for defining periodic piecewise functions - see for example here: http://community.wolfram.com/groups/-/m/t/156025
We could to the same (one possible route).


---

Comment by rws created at 2016-08-11 07:50:22

Replying to [comment:9 mkoeppe]:
> I'm bringing this up because I'm in need of periodic piecewise functions (#21215). Using a suitable symbolic mod would be one way. 

It is the more complicated way. You are asking for a feature of `piecewise` which can be had just by the addition of a `period` keyword. A symbolic `mod` is not necessary for it, and I'm arguing it's not necessary at all because there are no use cases that are handled better in the symbolic ring than in a dedicated finite ring, even if Sage does not have it at the moment. As the user of the ask.sagemath question above finally realized as well.


---

Comment by mkoeppe created at 2016-08-12 00:16:31

Replying to [comment:12 rws]:
> Replying to [comment:9 mkoeppe]:
> > I'm bringing this up because I'm in need of periodic piecewise functions (#21215). Using a suitable symbolic mod would be one way. 
> 
> It is the more complicated way. You are asking for a feature of `piecewise` which can be had just by the addition of a `period` keyword. A symbolic `mod` is not necessary for it, and I'm arguing it's not necessary at all because there are no use cases that are handled better in the symbolic ring than in a dedicated finite ring, even if Sage does not have it at the moment. As the user of the ask.sagemath question above finally realized as well.

Thanks!
