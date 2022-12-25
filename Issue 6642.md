# Issue 6642: problem with solve (from the tutorial)

archive/issues_006642.json:
```json
{
    "body": "CC:  mvngu @jasongrout @burcin @robertwb\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/85929d86accdf94d):\n\n```\n     sage: theta = var('theta')\n     sage: solve(cos(theta)==sin(theta))\n```\n\nshould produce\n\n```\n     [sin(theta) == cos(theta)]\n```\n\nbut instead it produces\n\n```\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/palmieri/.sage/temp/Macintosh.local/69786/_Users_palmieri__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)\n    478     \"\"\"\n    479     try:\n--> 480         return f.solve(*args,**kwds)\n    481     except AttributeError:\n    482         from sage.symbolic.ring import is_SymbolicVariable\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:21764)()\n\nTypeError: solve() takes at least 1 positional argument (0 given)\n```\n\nProviding a second argument 'theta' gives another error:\n\n```\n    sage: solve(cos(theta)==sin(theta), theta)\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/Users/palmieri/.sage/temp/Macintosh.local/69786/_Users_palmieri__sage_init_sage_0.py in <module>()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)\n    478     \"\"\"\n    479     try:\n--> 480         return f.solve(*args,**kwds)\n    481     except AttributeError:\n    482         from sage.symbolic.ring import is_SymbolicVariable\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:22291)()\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, *args, **kwds)\n   1380 \n   1381     def __call__(self, *args, **kwds):\n-> 1382         return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)\n   1383 \n   1384     def help(self):\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in function_call(self, function, args, kwds)\n   1288                                        [s.name() for s in args],\n   1289                                        ['%s=%s'%(key,value.name()) for key, value in kwds.items()])\n-> 1290         return self.new(s)\n   1291 \n   1292     def _function_call_string(self, function, args, kwds):\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in new(self, code)\n   1084 \n   1085     def new(self, code):\n-> 1086         return self(code)\n   1087 \n   1088     ###################################################################\n\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)\n   1019 \n   1020         if isinstance(x, basestring):\n-> 1021             return cls(self, x, name=name)\n   1022         try:\n   1023             return self._coerce_from_special_method(x)\n\n/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)\n   1423             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:\n   1424                 self._session_number = -1\n-> 1425                 raise TypeError, x\n   1426         self._session_number = parent._session_number\n   1427 \n\nTypeError: Error executing code in Maxima\nCODE:\n\tsage4 : to_poly_solve(sage0,sage3)$\nMaxima ERROR:\n\t\nNonalgebraic argument given to 'topoly'\n#0: to_poly_solve(e=cos(theta) = sin(theta),vars=theta)(topoly_solver.mac line 10)\n```\n\nThe first version of this -- `solve(cos(theta)==sin(theta))` -- is in the tutorial, and so presumably used to work.  \n\nSee #6572 for a related ticket which, among other things, tells doctesting to skip this test in the tutorial.  If the underlying problem is solved, the test in the tutorial should be restored, and of course a test should be put into the main Sage code illustrating that it now works.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6642\n\n",
    "created_at": "2009-07-27T17:13:55Z",
    "labels": [
        "component: symbolics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "problem with solve (from the tutorial)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6642",
    "user": "https://github.com/jhpalmieri"
}
```
CC:  mvngu @jasongrout @burcin @robertwb

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/85929d86accdf94d):

```
     sage: theta = var('theta')
     sage: solve(cos(theta)==sin(theta))
```

should produce

```
     [sin(theta) == cos(theta)]
```

but instead it produces

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/palmieri/.sage/temp/Macintosh.local/69786/_Users_palmieri__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)
    478     """
    479     try:
--> 480         return f.solve(*args,**kwds)
    481     except AttributeError:
    482         from sage.symbolic.ring import is_SymbolicVariable

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:21764)()

TypeError: solve() takes at least 1 positional argument (0 given)
```

Providing a second argument 'theta' gives another error:

```
    sage: solve(cos(theta)==sin(theta), theta)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/Users/palmieri/.sage/temp/Macintosh.local/69786/_Users_palmieri__sage_init_sage_0.py in <module>()

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/relation.pyc in solve(f, *args, **kwds)
    478     """
    479     try:
--> 480         return f.solve(*args,**kwds)
    481     except AttributeError:
    482         from sage.symbolic.ring import is_SymbolicVariable

/Applications/sage/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression.solve (sage/symbolic/expression.cpp:22291)()

/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, *args, **kwds)
   1380 
   1381     def __call__(self, *args, **kwds):
-> 1382         return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
   1383 
   1384     def help(self):

/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in function_call(self, function, args, kwds)
   1288                                        [s.name() for s in args],
   1289                                        ['%s=%s'%(key,value.name()) for key, value in kwds.items()])
-> 1290         return self.new(s)
   1291 
   1292     def _function_call_string(self, function, args, kwds):

/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in new(self, code)
   1084 
   1085     def new(self, code):
-> 1086         return self(code)
   1087 
   1088     ###################################################################


/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1019 
   1020         if isinstance(x, basestring):
-> 1021             return cls(self, x, name=name)
   1022         try:
   1023             return self._coerce_from_special_method(x)

/Applications/sage/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1423             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1424                 self._session_number = -1
-> 1425                 raise TypeError, x
   1426         self._session_number = parent._session_number
   1427 

TypeError: Error executing code in Maxima
CODE:
	sage4 : to_poly_solve(sage0,sage3)$
Maxima ERROR:
	
Nonalgebraic argument given to 'topoly'
#0: to_poly_solve(e=cos(theta) = sin(theta),vars=theta)(topoly_solver.mac line 10)
```

The first version of this -- `solve(cos(theta)==sin(theta))` -- is in the tutorial, and so presumably used to work.  

See #6572 for a related ticket which, among other things, tells doctesting to skip this test in the tutorial.  If the underlying problem is solved, the test in the tutorial should be restored, and of course a test should be put into the main Sage code illustrating that it now works.

Issue created by migration from https://trac.sagemath.org/ticket/6642





---

archive/issue_comments_054358.json:
```json
{
    "body": "Attachment [trac_6642-solve-implicit-Maxima.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-solve-implicit-Maxima.patch) by @kcrisman created at 2009-08-26 21:19:24\n\nBased on 4.1.1",
    "created_at": "2009-08-26T21:19:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54358",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6642-solve-implicit-Maxima.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-solve-implicit-Maxima.patch) by @kcrisman created at 2009-08-26 21:19:24

Based on 4.1.1



---

archive/issue_comments_054359.json:
```json
{
    "body": "This should fix the problem.  The behavior of explicit_solutions has been clarified a bit, and should pass doctests in sage/calculus and sage/symbolic.  Please test thoroughly, though, as whenever one uses a black box (here, Maxima) there is potential for trouble!",
    "created_at": "2009-08-26T21:21:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54359",
    "user": "https://github.com/kcrisman"
}
```

This should fix the problem.  The behavior of explicit_solutions has been clarified a bit, and should pass doctests in sage/calculus and sage/symbolic.  Please test thoroughly, though, as whenever one uses a black box (here, Maxima) there is potential for trouble!



---

archive/issue_comments_054360.json:
```json
{
    "body": "In 4.1.2.alpha1, I'm getting something odd when I don't specify `explicit_solutions`:\n\n```\nsage: solve(sin(x) == cos(x), x, explicit_solutions=False)\n[sin(x) == cos(x)]\nsage: solve(sin(x) == cos(x), x, explicit_solutions=True)\n[]\nsage: solve(sin(x) == cos(x), x)\n[x == r2, x == r1]\n```\n\nI think at least two changes are in order, if I understand the code right: first, change the default value for explicit_solutions from \"None\" to \"False\".  As it stands, in the \"if\" block that starts with the line\n\n```\nif explicit_solutions is not False:\n```\n\nthe code is executed if explicit_solutions is None or True, but not if it's False.  I suppose this line could be changed to\n\n```\nif bool(explicit_solutions) is not False:\n```\n\nSecond, several comments (\"We only reach this if explicit_solutions is None\", \"This is fine because explicit_solutions is None\") may need to be changed to reflect this.\n\nOf course, I could be misunderstanding everything, and we want \"False\", \"True\", and \"None\" to each behave differently.  If so, this needs to be documented; for example, \"explicit_solutions\" is not a bool in this case.",
    "created_at": "2009-09-08T20:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54360",
    "user": "https://github.com/jhpalmieri"
}
```

In 4.1.2.alpha1, I'm getting something odd when I don't specify `explicit_solutions`:

```
sage: solve(sin(x) == cos(x), x, explicit_solutions=False)
[sin(x) == cos(x)]
sage: solve(sin(x) == cos(x), x, explicit_solutions=True)
[]
sage: solve(sin(x) == cos(x), x)
[x == r2, x == r1]
```

I think at least two changes are in order, if I understand the code right: first, change the default value for explicit_solutions from "None" to "False".  As it stands, in the "if" block that starts with the line

```
if explicit_solutions is not False:
```

the code is executed if explicit_solutions is None or True, but not if it's False.  I suppose this line could be changed to

```
if bool(explicit_solutions) is not False:
```

Second, several comments ("We only reach this if explicit_solutions is None", "This is fine because explicit_solutions is None") may need to be changed to reflect this.

Of course, I could be misunderstanding everything, and we want "False", "True", and "None" to each behave differently.  If so, this needs to be documented; for example, "explicit_solutions" is not a bool in this case.



---

archive/issue_comments_054361.json:
```json
{
    "body": "Hold up; this seems to be related to the new Maxima .spkg, actually - has nothing to do with the patch.  Perhaps they are interpreting something as a symbol which isn't?  Stay tuned.",
    "created_at": "2009-09-09T01:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54361",
    "user": "https://github.com/kcrisman"
}
```

Hold up; this seems to be related to the new Maxima .spkg, actually - has nothing to do with the patch.  Perhaps they are interpreting something as a symbol which isn't?  Stay tuned.



---

archive/issue_comments_054362.json:
```json
{
    "body": "Yeah, to_poly_solve has changed significantly - namely, it actually tries to solve these guys, so the TypeError is no longer raised.  But the way it tries to solve them seems to be a little unintelligible to Sage - even the Maxima documentation examples don't seem to come out the same way.  This will take some effort to figure out.  \n\nOne should check whether these errors show up without the patch.  Also, note that to_poly and to_poly_solve are experimental packages!  So whoever put it in was already playing with fire to some extent, though it is quite useful.",
    "created_at": "2009-09-09T02:08:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54362",
    "user": "https://github.com/kcrisman"
}
```

Yeah, to_poly_solve has changed significantly - namely, it actually tries to solve these guys, so the TypeError is no longer raised.  But the way it tries to solve them seems to be a little unintelligible to Sage - even the Maxima documentation examples don't seem to come out the same way.  This will take some effort to figure out.  

One should check whether these errors show up without the patch.  Also, note that to_poly and to_poly_solve are experimental packages!  So whoever put it in was already playing with fire to some extent, though it is quite useful.



---

archive/issue_comments_054363.json:
```json
{
    "body": "Okay, that's progress: at least we (meaning you) understand what the problem is.  However, if it's intentional that False and None should behave differently (as the code is currently written), then this should be documented and there should be doctests for it.",
    "created_at": "2009-09-09T05:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54363",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, that's progress: at least we (meaning you) understand what the problem is.  However, if it's intentional that False and None should behave differently (as the code is currently written), then this should be documented and there should be doctests for it.



---

archive/issue_comments_054364.json:
```json
{
    "body": "Attachment [trac_6642-to-poly-solve-take2.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-to-poly-solve-take2.patch) by @kcrisman created at 2009-09-20 02:03:55\n\nDepends on #4786",
    "created_at": "2009-09-20T02:03:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54364",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6642-to-poly-solve-take2.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-to-poly-solve-take2.patch) by @kcrisman created at 2009-09-20 02:03:55

Depends on #4786



---

archive/issue_comments_054365.json:
```json
{
    "body": "Okay, this is ready for review.  I expect that there will be some problems somewhere, but it has to get out there to be tested.  There is the possibility of it not applying properly if some of the other symbolic patches post-4.1.1.alpha1 have been merged, but I don't think they have been yet.  See also discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/e797a9904baaa4a6](http://groups.google.com/group/sage-devel/browse_thread/thread/e797a9904baaa4a6).  Note I have not done the solve_numerical=find_root, as that is probably for a different ticket.\n\nAlso, there is one doctest I am currently not testing.  It is fixed in the CVS version of Maxima, but I have absolutely no idea how to make a new .spkg, nor even really to build Maxima from scratch since I can't get cmucl to work on my computer (not to mention that the just-updated Maxima package is currently a little dicey because of Solaris and OSX build issues) so probably one would open a new ticket to fix that again with a new .spkg.",
    "created_at": "2009-09-20T02:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54365",
    "user": "https://github.com/kcrisman"
}
```

Okay, this is ready for review.  I expect that there will be some problems somewhere, but it has to get out there to be tested.  There is the possibility of it not applying properly if some of the other symbolic patches post-4.1.1.alpha1 have been merged, but I don't think they have been yet.  See also discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/e797a9904baaa4a6](http://groups.google.com/group/sage-devel/browse_thread/thread/e797a9904baaa4a6).  Note I have not done the solve_numerical=find_root, as that is probably for a different ticket.

Also, there is one doctest I am currently not testing.  It is fixed in the CVS version of Maxima, but I have absolutely no idea how to make a new .spkg, nor even really to build Maxima from scratch since I can't get cmucl to work on my computer (not to mention that the just-updated Maxima package is currently a little dicey because of Solaris and OSX build issues) so probably one would open a new ticket to fix that again with a new .spkg.



---

archive/issue_comments_054366.json:
```json
{
    "body": "This seems to fix the issue with the tutorial.  On the other hand, on sage.math, I'm getting a doctest failure:\n\n```\nsage -t -long \"devel/sage/sage/rings/number_field/number_field_element.pyx\"\n**********************************************************************\nFile \"/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/rings/number_field/number_field_element.pyx\", line 1421:\n    sage: SR(a)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_40[20]>\", line 1, in <module>\n        SR(a)###line 1421:\n    sage: SR(a)\n      File \"parent.pyx\", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4174)\n      File \"coerce_maps.pyx\", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4067)\n      File \"number_field_element.pyx\", line 1468, in sage.rings.number_field.number_field_element.NumberFieldElement._symbolic_ (sage/rings/number_field/number_field_element.cpp:11860)\n    TypeError: Unable to solve by radicals.\n```\n",
    "created_at": "2009-10-05T20:18:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54366",
    "user": "https://github.com/jhpalmieri"
}
```

This seems to fix the issue with the tutorial.  On the other hand, on sage.math, I'm getting a doctest failure:

```
sage -t -long "devel/sage/sage/rings/number_field/number_field_element.pyx"
**********************************************************************
File "/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/devel/sage/sage/rings/number_field/number_field_element.pyx", line 1421:
    sage: SR(a)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/palmieri/sage-4.1.2.rc0-sage.math.washington.edu-x86_64-Linux/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_40[20]>", line 1, in <module>
        SR(a)###line 1421:
    sage: SR(a)
      File "parent.pyx", line 323, in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4174)
      File "coerce_maps.pyx", line 156, in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4067)
      File "number_field_element.pyx", line 1468, in sage.rings.number_field.number_field_element.NumberFieldElement._symbolic_ (sage/rings/number_field/number_field_element.cpp:11860)
    TypeError: Unable to solve by radicals.
```




---

archive/issue_comments_054367.json:
```json
{
    "body": "Well, here I need to know from someone what the intended behavior of _symbolic_ is for algebraic number field elements.  Do they want an approximation or not?  Because right now it's not clear that the TypeError of unable to solve by radicals is ever going to show up, yet that would seem to be the appropriate response to this.  \n\nIf an approximation is still desired, it's easy to pass to_poly_solve=True in at line 1464 of number_field_element.pyx, but if not, then the doctest can just be changed, so either way the solution is easy.  I don't feel authorized to make changes like that in code I don't use on a daily basis, though; perhaps the numerical approximation is actually quite useful, though I have to say to me it sort of undermines the spirit of the rest of the method, where CC is used to get numerical approximations of radical solutions. \n\n(This is a place where Jason's idea of \"needs info\" would be really helpful.)",
    "created_at": "2009-10-05T20:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54367",
    "user": "https://github.com/kcrisman"
}
```

Well, here I need to know from someone what the intended behavior of _symbolic_ is for algebraic number field elements.  Do they want an approximation or not?  Because right now it's not clear that the TypeError of unable to solve by radicals is ever going to show up, yet that would seem to be the appropriate response to this.  

If an approximation is still desired, it's easy to pass to_poly_solve=True in at line 1464 of number_field_element.pyx, but if not, then the doctest can just be changed, so either way the solution is easy.  I don't feel authorized to make changes like that in code I don't use on a daily basis, though; perhaps the numerical approximation is actually quite useful, though I have to say to me it sort of undermines the spirit of the rest of the method, where CC is used to get numerical approximations of radical solutions. 

(This is a place where Jason's idea of "needs info" would be really helpful.)



---

archive/issue_comments_054368.json:
```json
{
    "body": "Well, it does say right before the doctest (lines 1416-1418 of number_field_element.pyx)\n\n```\n        For degree greater than 5, sometimes Galois theory prevents a\n        closed-form solution.  In this case, a numerical approximation\n        is used::\n```\n\nGiven this and the output of the doctest (-1.1673040153), I think numerical approximation is the way to go.  Do you want to make a new patch with this change (and also fixing the \"approximtae\" typo that you pointed out)?  I think that it can be given a positive review if it passes all doctests.",
    "created_at": "2009-10-08T02:21:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54368",
    "user": "https://github.com/jhpalmieri"
}
```

Well, it does say right before the doctest (lines 1416-1418 of number_field_element.pyx)

```
        For degree greater than 5, sometimes Galois theory prevents a
        closed-form solution.  In this case, a numerical approximation
        is used::
```

Given this and the output of the doctest (-1.1673040153), I think numerical approximation is the way to go.  Do you want to make a new patch with this change (and also fixing the "approximtae" typo that you pointed out)?  I think that it can be given a positive review if it passes all doctests.



---

archive/issue_comments_054369.json:
```json
{
    "body": "> Do you want to make a new patch \n\nSorry, this is silly.  I'll make a referee's patch since you already said exactly what to do.  I'm running doctests now, and if all goes well, I'll post the referee's patch and a positive review.",
    "created_at": "2009-10-08T03:25:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54369",
    "user": "https://github.com/jhpalmieri"
}
```

> Do you want to make a new patch 

Sorry, this is silly.  I'll make a referee's patch since you already said exactly what to do.  I'm running doctests now, and if all goes well, I'll post the referee's patch and a positive review.



---

archive/issue_comments_054370.json:
```json
{
    "body": "Attachment [trac_6642-to-poly-solve-take3.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-to-poly-solve-take3.patch) by @kcrisman created at 2009-10-08 03:54:15\n\nBased on 4.1.2.rc1.alpha3",
    "created_at": "2009-10-08T03:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54370",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6642-to-poly-solve-take3.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-to-poly-solve-take3.patch) by @kcrisman created at 2009-10-08 03:54:15

Based on 4.1.2.rc1.alpha3



---

archive/issue_comments_054371.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-10-08T03:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54371",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054372.json:
```json
{
    "body": "Sorry, I was away from the computer when you posted that last comment, and made a new patch already.  I assume that this patch will do the same thing you were about to do. However, it does fix a doctest issue in calculus/calculus.py (a numerical integral), so perhaps it will save you a little trouble if I post this.  The issue may also be platform-dependent, so maybe it helped discover something good - you can use ... to comment the last digit out if that's what it turns out to be.\n\nIncidentally, my initial thought was that the 1416ff. lines were an overzealous doctester earlier, after to_poly_solve was first incorporated.  But someone else can change that if that's not the desired behavior.",
    "created_at": "2009-10-08T03:57:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54372",
    "user": "https://github.com/kcrisman"
}
```

Sorry, I was away from the computer when you posted that last comment, and made a new patch already.  I assume that this patch will do the same thing you were about to do. However, it does fix a doctest issue in calculus/calculus.py (a numerical integral), so perhaps it will save you a little trouble if I post this.  The issue may also be platform-dependent, so maybe it helped discover something good - you can use ... to comment the last digit out if that's what it turns out to be.

Incidentally, my initial thought was that the 1416ff. lines were an overzealous doctester earlier, after to_poly_solve was first incorporated.  But someone else can change that if that's not the desired behavior.



---

archive/issue_comments_054373.json:
```json
{
    "body": "Okay, I checked on a Intel and it IS plaform-dependent.  So here's the real patch.  Sorry for the confusion, jhpalmieri - you've been very helpful.",
    "created_at": "2009-10-08T13:46:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54373",
    "user": "https://github.com/kcrisman"
}
```

Okay, I checked on a Intel and it IS plaform-dependent.  So here's the real patch.  Sorry for the confusion, jhpalmieri - you've been very helpful.



---

archive/issue_comments_054374.json:
```json
{
    "body": "Sorry, use last patch, I keep on forgetting to click \"replace\".",
    "created_at": "2009-10-08T13:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54374",
    "user": "https://github.com/kcrisman"
}
```

Sorry, use last patch, I keep on forgetting to click "replace".



---

archive/issue_comments_054375.json:
```json
{
    "body": "I came to the same conclusion.  Now all tests pass.",
    "created_at": "2009-10-08T14:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54375",
    "user": "https://github.com/jhpalmieri"
}
```

I came to the same conclusion.  Now all tests pass.



---

archive/issue_comments_054376.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-08T14:55:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54376",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054377.json:
```json
{
    "body": "Just FYI, this will probably not get in before 4.1.2, and at #7112 William has already fixed the numerical noise issue.  So we'll probably have to remove it.  Sigh.",
    "created_at": "2009-10-08T16:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54377",
    "user": "https://github.com/kcrisman"
}
```

Just FYI, this will probably not get in before 4.1.2, and at #7112 William has already fixed the numerical noise issue.  So we'll probably have to remove it.  Sigh.



---

archive/issue_comments_054378.json:
```json
{
    "body": "Attachment [trac_6642-to-poly-solve-take3.2.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-to-poly-solve-take3.2.patch) by @kcrisman created at 2009-10-14 20:07:22\n\nBased on 4.1.2.rc1.alpha3",
    "created_at": "2009-10-14T20:07:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54378",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_6642-to-poly-solve-take3.2.patch](tarball://root/attachments/some-uuid/ticket6642/trac_6642-to-poly-solve-take3.2.patch) by @kcrisman created at 2009-10-14 20:07:22

Based on 4.1.2.rc1.alpha3



---

archive/issue_comments_054379.json:
```json
{
    "body": "This most recent one should hopefully apply well to 4.1.2 itself.  The only change was to remove a doctest fix that was already in #7112, so shouldn't disturb anything else.",
    "created_at": "2009-10-14T20:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54379",
    "user": "https://github.com/kcrisman"
}
```

This most recent one should hopefully apply well to 4.1.2 itself.  The only change was to remove a doctest fix that was already in #7112, so shouldn't disturb anything else.



---

archive/issue_comments_054380.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T09:05:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6642",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6642#issuecomment-54380",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
