# Issue 9625: solve hangs on a small algebraic system with 4 equations in 4 unknowns

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-07-28 14:33:24

Assignee: burcin

CC:  jason kcrisman malb was

The following command hangs with Sage 4.4.4:

```
var = [s,t,w,z]
sys = [-83065036657810695629*s^2 + 83065036657810695629*t*w - 68998003149632685\
30106646060491053792528*s - 395748941050538664245556665401237631434*w + 6899800\
710712292645598903080085537498136631434, 124597554986716043444*s^2 - 1245975549\
86716043444*t*w + 10349700472444902795201501609065485036608*s - 268851627794621\
336185309600880111037777*w - 10349700203593399598010554584812612113052962223, -\
282961047374832134660970*s^2 - 8410334961603332923585*s*z + 8410334961603332923\
585*t^2 + 282961047374832134660970*t*w - 23504169772922374247873205131210852239\
883040*s - 30616067929472784598571512251700309424241225*t - 7028115267891297114\
2272480500812537457*w - 349302390945015468969034253953644989640360*z - 94573827\
6702217921211141587964108207667243789392, -5322973679105824997312280*s^2 + 9157\
920291523629102472*s*z - 9157920291523629102472*t^2 + 5322973679105824997312280\
*t*w - 442153003783476173947515315017330812575960960*s + 3127353268883216472554\
94866020283168151616125*t - 167582752514587776396443776337970730676*w + 3803514\
92362350173958234007398030593401152*z - 176904945185291980573382635775655917064\
32113716525]
solve(sys,var)
```

In comparison, Maple 13 answers in 38 milliseconds...


---

Comment by mpatel created at 2010-07-28 21:52:43

I see this problem on both bsd and sage.math.  Pressing Control-C yields

```
sage: solve(sys, [s, t, w, z])
Control-C pressed.  Interrupting Maxima. Please wait a few seconds...
Maxima crashed -- automatically restarting.
[]
sage: 
```

Possibly naive question: Is this a problem in the Maxima wrapper or in Maxima itself?

On sage.math, Maple 12 responds to `solve({...}, [s, t, w, z]);` almost immediately with

```
[[s = 1/15 RootOf(145777 _Z  - 2724518665994742900057173191849397

                                                         57108616849397
     + 181634577732980673347190960 _Z, label = _L6), t = --------------, w = 1,
                                                            32799825

          137699550319729285466821911369819307114778019367342119879667352
    z = - --------------------------------------------------------------- -
              618583496779496012457663125225479925612236417948265175

          9946390625479936819718245891740613642685141                        2
    -------------------------------------------------------- RootOf(145777 _Z
    27836257355077320560594840635146596652550638807671932875

     - 2724518665994742900057173191849397 + 181634577732980673347190960 _Z,

    label = _L6)]]
```


But I think it's too late in the 4.5.2 release cycle to fix this problem, so I've changed the milestone to 4.5.3.

Out of curiosity: Does this system have a special provenance?


---

Comment by mpatel created at 2010-07-28 21:55:28

Replying to [comment:1 mpatel]:
> But I think it's too late in the 4.5.2 release cycle to fix this problem, so I've changed the milestone to 4.5.3.

Or is there a simple fix someone can post very soon?


---

Comment by zimmerma created at 2010-07-29 08:01:19

Replying to [comment:1 mpatel]:
> Possibly naive question: Is this a problem in the Maxima wrapper or in Maxima itself?

it seems to be a problem in the main Maxima `to_poly_solve` function. With the option
`use_grobner=true` it returns (but never gets a chance to get there in the try ... except).

> Out of curiosity: Does this system have a special provenance?

yes, it comes from Coppersmith's algorithm to find small roots of a polynomial system, which was itself used by a master student (Thomas Prest) in the context of polynomial selection for the
Number Field Sieve with two non-linear polynomials.

Paul


---

Comment by mpatel created at 2010-08-12 23:01:31

Is this purely an upstream problem?


---

Comment by mpatel created at 2010-08-15 07:07:06

The 4.5.3 series will soon be in "feature freeze."


---

Comment by zimmerma created at 2010-09-01 20:19:51

Replying to [comment:4 mpatel]:
> Is this purely an upstream problem?

I have no idea. The maxima SPKG.txt contains no maintainer name, thus I don't know who to put in cc to report this problem upstream (if needed). Can anybody help?

Paul


---

Comment by kcrisman created at 2010-09-01 20:25:35

Eventually someone will look into it - it can just take a while to have the time.  I'll try to look at this soon.


---

Comment by mpatel created at 2010-09-19 06:50:17

Changing priority from blocker to major.


---

Comment by boothby created at 2010-11-08 06:45:30

I'm not sure if this is related or not:


```
z = var('z')
f =  1 - z - z^2 - z^3 - z^4 - z^5
solve(f == 0,z)
```


this takes about 2 minutes before 


```
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored
Exception GeneratorExit in <generator object <genexpr> at 0x6af3a00> ignored
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "_sage_input_100.py", line 10, in <module>
    exec compile(u'open("___code___.py","w").write("# -*- coding: utf-8 -*-\\n" + _support_.preparse_worksheet_cell(base64.b64decode("c29sdmUoZiA9PSAwLHop"),globals())+"\\n"); execfile(os.path.abspath("___code___.py"))' + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "/tmp/tmpTusLV8/___code___.py", line 3, in <module>
    exec compile(u'solve(f == _sage_const_0 ,z)' + '\n', '', 'single')
  File "", line 1, in <module>
    
  File "/tmp/tmpfp2kNu/___code___.py", line 7, in solve
    z = solve(z,n-_sage_const_1 )
... 2000 or so lines ...
  File "/tmp/tmpfp2kNu/___code___.py", line 7, in solve
    z = solve(z,n-_sage_const_1 )
  File "/tmp/tmpfp2kNu/___code___.py", line 4, in solve
    if n <= _sage_const_0 :
  File "expression.pyx", line 1647, in sage.symbolic.expression.Expression.__nonzero__ (sage/symbolic/expression.cpp:8049)
  File "/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/relation.py", line 381, in test_relation_maxima
    m = relation._maxima_()
  File "expression.pyx", line 433, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3382)
  File "sage_object.pyx", line 379, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3374)
  File "sage_object.pyx", line 468, in sage.structure.sage_object.SageObject._maxima_init_ (sage/structure/sage_object.c:5083)
  File "expression.pyx", line 458, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3510)
  File "/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 216, in __call__
    return self.relation(ex, operator)
  File "/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 459, in relation
    return "%s %s %s"%(self(ex.lhs()), self.relation_symbols[operator],
  File "/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 214, in __call__
    return self.arithmetic(ex, operator)
  File "/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 505, in arithmetic
    args = ["(%s)"%self(op) for op in ex.operands()]
  File "/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 201, in __call__
    return self.pyobject(ex, obj)
  File "/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py", line 443, in pyobject
    return getattr(obj, self.name_init)()
  File "sage_object.pyx", line 468, in sage.structure.sage_object.SageObject._maxima_init_ (sage/structure/sage_object.c:5083)
  File "integer.pyx", line 4329, in sage.rings.integer.Integer._interface_init_ (sage/rings/integer.c:24709)
  File "integer.pyx", line 815, in sage.rings.integer.Integer.__repr__ (sage/rings/integer.c:7526)
RuntimeError: maximum recursion depth exceeded while calling a Python object
```



---

Comment by boothby created at 2010-11-08 06:47:02

Dang, can't undo comments.  This is entirely user error, and has nothing to do with this ticket.
