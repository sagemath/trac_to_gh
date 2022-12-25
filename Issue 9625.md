# Issue 9625: solve hangs on a small algebraic system with 4 equations in 4 unknowns

archive/issues_009625.json:
```json
{
    "body": "Assignee: @burcin\n\nCC:  @jasongrout @kcrisman @malb @williamstein\n\nThe following command hangs with Sage 4.4.4:\n\n```\nvar = [s,t,w,z]\nsys = [-83065036657810695629*s^2 + 83065036657810695629*t*w - 68998003149632685\\\n30106646060491053792528*s - 395748941050538664245556665401237631434*w + 6899800\\\n710712292645598903080085537498136631434, 124597554986716043444*s^2 - 1245975549\\\n86716043444*t*w + 10349700472444902795201501609065485036608*s - 268851627794621\\\n336185309600880111037777*w - 10349700203593399598010554584812612113052962223, -\\\n282961047374832134660970*s^2 - 8410334961603332923585*s*z + 8410334961603332923\\\n585*t^2 + 282961047374832134660970*t*w - 23504169772922374247873205131210852239\\\n883040*s - 30616067929472784598571512251700309424241225*t - 7028115267891297114\\\n2272480500812537457*w - 349302390945015468969034253953644989640360*z - 94573827\\\n6702217921211141587964108207667243789392, -5322973679105824997312280*s^2 + 9157\\\n920291523629102472*s*z - 9157920291523629102472*t^2 + 5322973679105824997312280\\\n*t*w - 442153003783476173947515315017330812575960960*s + 3127353268883216472554\\\n94866020283168151616125*t - 167582752514587776396443776337970730676*w + 3803514\\\n92362350173958234007398030593401152*z - 176904945185291980573382635775655917064\\\n32113716525]\nsolve(sys,var)\n```\n\nIn comparison, Maple 13 answers in 38 milliseconds...\n\nIssue created by migration from https://trac.sagemath.org/ticket/9625\n\n",
    "created_at": "2010-07-28T14:33:24Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "solve hangs on a small algebraic system with 4 equations in 4 unknowns",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9625",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @burcin

CC:  @jasongrout @kcrisman @malb @williamstein

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

Issue created by migration from https://trac.sagemath.org/ticket/9625





---

archive/issue_comments_093127.json:
```json
{
    "body": "I see this problem on both bsd and sage.math.  Pressing Control-C yields\n\n```\nsage: solve(sys, [s, t, w, z])\nControl-C pressed.  Interrupting Maxima. Please wait a few seconds...\nMaxima crashed -- automatically restarting.\n[]\nsage: \n```\n\nPossibly naive question: Is this a problem in the Maxima wrapper or in Maxima itself?\n\nOn sage.math, Maple 12 responds to `solve({...}, [s, t, w, z]);` almost immediately with\n\n```\n[[s = 1/15 RootOf(145777 _Z  - 2724518665994742900057173191849397\n\n                                                         57108616849397\n     + 181634577732980673347190960 _Z, label = _L6), t = --------------, w = 1,\n                                                            32799825\n\n          137699550319729285466821911369819307114778019367342119879667352\n    z = - --------------------------------------------------------------- -\n              618583496779496012457663125225479925612236417948265175\n\n          9946390625479936819718245891740613642685141                        2\n    -------------------------------------------------------- RootOf(145777 _Z\n    27836257355077320560594840635146596652550638807671932875\n\n     - 2724518665994742900057173191849397 + 181634577732980673347190960 _Z,\n\n    label = _L6)]]\n```\n\n\nBut I think it's too late in the 4.5.2 release cycle to fix this problem, so I've changed the milestone to 4.5.3.\n\nOut of curiosity: Does this system have a special provenance?",
    "created_at": "2010-07-28T21:52:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93127",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_093128.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> But I think it's too late in the 4.5.2 release cycle to fix this problem, so I've changed the milestone to 4.5.3.\n\nOr is there a simple fix someone can post very soon?",
    "created_at": "2010-07-28T21:55:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93128",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:1 mpatel]:
> But I think it's too late in the 4.5.2 release cycle to fix this problem, so I've changed the milestone to 4.5.3.

Or is there a simple fix someone can post very soon?



---

archive/issue_comments_093129.json:
```json
{
    "body": "Replying to [comment:1 mpatel]:\n> Possibly naive question: Is this a problem in the Maxima wrapper or in Maxima itself?\n\nit seems to be a problem in the main Maxima `to_poly_solve` function. With the option\n`use_grobner=true` it returns (but never gets a chance to get there in the try ... except).\n\n> Out of curiosity: Does this system have a special provenance?\n\nyes, it comes from Coppersmith's algorithm to find small roots of a polynomial system, which was itself used by a master student (Thomas Prest) in the context of polynomial selection for the\nNumber Field Sieve with two non-linear polynomials.\n\nPaul",
    "created_at": "2010-07-29T08:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93129",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:1 mpatel]:
> Possibly naive question: Is this a problem in the Maxima wrapper or in Maxima itself?

it seems to be a problem in the main Maxima `to_poly_solve` function. With the option
`use_grobner=true` it returns (but never gets a chance to get there in the try ... except).

> Out of curiosity: Does this system have a special provenance?

yes, it comes from Coppersmith's algorithm to find small roots of a polynomial system, which was itself used by a master student (Thomas Prest) in the context of polynomial selection for the
Number Field Sieve with two non-linear polynomials.

Paul



---

archive/issue_comments_093130.json:
```json
{
    "body": "Is this purely an upstream problem?",
    "created_at": "2010-08-12T23:01:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93130",
    "user": "https://github.com/qed777"
}
```

Is this purely an upstream problem?



---

archive/issue_comments_093131.json:
```json
{
    "body": "The 4.5.3 series will soon be in \"feature freeze.\"",
    "created_at": "2010-08-15T07:07:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93131",
    "user": "https://github.com/qed777"
}
```

The 4.5.3 series will soon be in "feature freeze."



---

archive/issue_events_023989.json:
```json
{
    "actor": "https://github.com/qed777",
    "created_at": "2010-08-15T07:07:06Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23989"
}
```



---

archive/issue_comments_093132.json:
```json
{
    "body": "Replying to [comment:4 mpatel]:\n> Is this purely an upstream problem?\n\nI have no idea. The maxima SPKG.txt contains no maintainer name, thus I don't know who to put in cc to report this problem upstream (if needed). Can anybody help?\n\nPaul",
    "created_at": "2010-09-01T20:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93132",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:4 mpatel]:
> Is this purely an upstream problem?

I have no idea. The maxima SPKG.txt contains no maintainer name, thus I don't know who to put in cc to report this problem upstream (if needed). Can anybody help?

Paul



---

archive/issue_comments_093133.json:
```json
{
    "body": "Eventually someone will look into it - it can just take a while to have the time.  I'll try to look at this soon.",
    "created_at": "2010-09-01T20:25:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93133",
    "user": "https://github.com/kcrisman"
}
```

Eventually someone will look into it - it can just take a while to have the time.  I'll try to look at this soon.



---

archive/issue_comments_093134.json:
```json
{
    "body": "I'm not sure if this is related or not:\n\n\n```\nz = var('z')\nf =  1 - z - z^2 - z^3 - z^4 - z^5\nsolve(f == 0,z)\n```\n\n\nthis takes about 2 minutes before \n\n\n```\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.TypeError'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored\nException RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.GeneratorExit'> ignored\nException GeneratorExit in <generator object <genexpr> at 0x6af3a00> ignored\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"_sage_input_100.py\", line 10, in <module>\n    exec compile(u'open(\"___code___.py\",\"w\").write(\"# -*- coding: utf-8 -*-\\\\n\" + _support_.preparse_worksheet_cell(base64.b64decode(\"c29sdmUoZiA9PSAwLHop\"),globals())+\"\\\\n\"); execfile(os.path.abspath(\"___code___.py\"))' + '\\n', '', 'single')\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpTusLV8/___code___.py\", line 3, in <module>\n    exec compile(u'solve(f == _sage_const_0 ,z)' + '\\n', '', 'single')\n  File \"\", line 1, in <module>\n    \n  File \"/tmp/tmpfp2kNu/___code___.py\", line 7, in solve\n    z = solve(z,n-_sage_const_1 )\n... 2000 or so lines ...\n  File \"/tmp/tmpfp2kNu/___code___.py\", line 7, in solve\n    z = solve(z,n-_sage_const_1 )\n  File \"/tmp/tmpfp2kNu/___code___.py\", line 4, in solve\n    if n <= _sage_const_0 :\n  File \"expression.pyx\", line 1647, in sage.symbolic.expression.Expression.__nonzero__ (sage/symbolic/expression.cpp:8049)\n  File \"/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/relation.py\", line 381, in test_relation_maxima\n    m = relation._maxima_()\n  File \"expression.pyx\", line 433, in sage.symbolic.expression.Expression._maxima_ (sage/symbolic/expression.cpp:3382)\n  File \"sage_object.pyx\", line 379, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3374)\n  File \"sage_object.pyx\", line 468, in sage.structure.sage_object.SageObject._maxima_init_ (sage/structure/sage_object.c:5083)\n  File \"expression.pyx\", line 458, in sage.symbolic.expression.Expression._interface_init_ (sage/symbolic/expression.cpp:3510)\n  File \"/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py\", line 216, in __call__\n    return self.relation(ex, operator)\n  File \"/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py\", line 459, in relation\n    return \"%s %s %s\"%(self(ex.lhs()), self.relation_symbols[operator],\n  File \"/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py\", line 214, in __call__\n    return self.arithmetic(ex, operator)\n  File \"/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py\", line 505, in arithmetic\n    args = [\"(%s)\"%self(op) for op in ex.operands()]\n  File \"/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py\", line 201, in __call__\n    return self.pyobject(ex, obj)\n  File \"/home/boothby/sage-4.4.4/local/lib/python2.6/site-packages/sage/symbolic/expression_conversions.py\", line 443, in pyobject\n    return getattr(obj, self.name_init)()\n  File \"sage_object.pyx\", line 468, in sage.structure.sage_object.SageObject._maxima_init_ (sage/structure/sage_object.c:5083)\n  File \"integer.pyx\", line 4329, in sage.rings.integer.Integer._interface_init_ (sage/rings/integer.c:24709)\n  File \"integer.pyx\", line 815, in sage.rings.integer.Integer.__repr__ (sage/rings/integer.c:7526)\nRuntimeError: maximum recursion depth exceeded while calling a Python object\n```\n",
    "created_at": "2010-11-08T06:45:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93134",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

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

archive/issue_comments_093135.json:
```json
{
    "body": "Dang, can't undo comments.  This is entirely user error, and has nothing to do with this ticket.",
    "created_at": "2010-11-08T06:47:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9625#issuecomment-93135",
    "user": "https://trac.sagemath.org/admin/accounts/users/boothby"
}
```

Dang, can't undo comments.  This is entirely user error, and has nothing to do with this ticket.



---

archive/issue_events_023990.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-4.6",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23990"
}
```



---

archive/issue_events_023991.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23991"
}
```



---

archive/issue_events_023992.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23992"
}
```



---

archive/issue_events_023993.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23993"
}
```



---

archive/issue_events_023994.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23994"
}
```



---

archive/issue_events_023995.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23995"
}
```



---

archive/issue_events_023996.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23996"
}
```



---

archive/issue_events_023997.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9625",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9625#event-23997"
}
```
