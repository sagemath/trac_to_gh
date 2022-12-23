# Issue 6642: problem with solve (from the tutorial)

Issue created by migration from https://trac.sagemath.org/ticket/6642

Original creator: jhpalmieri

Original creation time: 2009-07-27 17:13:55

CC:  mvngu jason burcin robertwb

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


---

Attachment

Based on 4.1.1


---

Comment by kcrisman created at 2009-08-26 21:21:44

This should fix the problem.  The behavior of explicit_solutions has been clarified a bit, and should pass doctests in sage/calculus and sage/symbolic.  Please test thoroughly, though, as whenever one uses a black box (here, Maxima) there is potential for trouble!


---

Comment by jhpalmieri created at 2009-09-08 20:32:12

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

Comment by kcrisman created at 2009-09-09 01:11:04

Hold up; this seems to be related to the new Maxima .spkg, actually - has nothing to do with the patch.  Perhaps they are interpreting something as a symbol which isn't?  Stay tuned.


---

Comment by kcrisman created at 2009-09-09 02:08:04

Yeah, to_poly_solve has changed significantly - namely, it actually tries to solve these guys, so the TypeError is no longer raised.  But the way it tries to solve them seems to be a little unintelligible to Sage - even the Maxima documentation examples don't seem to come out the same way.  This will take some effort to figure out.  

One should check whether these errors show up without the patch.  Also, note that to_poly and to_poly_solve are experimental packages!  So whoever put it in was already playing with fire to some extent, though it is quite useful.


---

Comment by jhpalmieri created at 2009-09-09 05:15:47

Okay, that's progress: at least we (meaning you) understand what the problem is.  However, if it's intentional that False and None should behave differently (as the code is currently written), then this should be documented and there should be doctests for it.


---

Attachment

Depends on #4786


---

Comment by kcrisman created at 2009-09-20 02:11:00

Okay, this is ready for review.  I expect that there will be some problems somewhere, but it has to get out there to be tested.  There is the possibility of it not applying properly if some of the other symbolic patches post-4.1.1.alpha1 have been merged, but I don't think they have been yet.  See also discussion at [http://groups.google.com/group/sage-devel/browse_thread/thread/e797a9904baaa4a6](http://groups.google.com/group/sage-devel/browse_thread/thread/e797a9904baaa4a6).  Note I have not done the solve_numerical=find_root, as that is probably for a different ticket.

Also, there is one doctest I am currently not testing.  It is fixed in the CVS version of Maxima, but I have absolutely no idea how to make a new .spkg, nor even really to build Maxima from scratch since I can't get cmucl to work on my computer (not to mention that the just-updated Maxima package is currently a little dicey because of Solaris and OSX build issues) so probably one would open a new ticket to fix that again with a new .spkg.


---

Comment by jhpalmieri created at 2009-10-05 20:18:49

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

Comment by kcrisman created at 2009-10-05 20:39:35

Well, here I need to know from someone what the intended behavior of _symbolic_ is for algebraic number field elements.  Do they want an approximation or not?  Because right now it's not clear that the TypeError of unable to solve by radicals is ever going to show up, yet that would seem to be the appropriate response to this.  

If an approximation is still desired, it's easy to pass to_poly_solve=True in at line 1464 of number_field_element.pyx, but if not, then the doctest can just be changed, so either way the solution is easy.  I don't feel authorized to make changes like that in code I don't use on a daily basis, though; perhaps the numerical approximation is actually quite useful, though I have to say to me it sort of undermines the spirit of the rest of the method, where CC is used to get numerical approximations of radical solutions. 

(This is a place where Jason's idea of "needs info" would be really helpful.)


---

Comment by jhpalmieri created at 2009-10-08 02:21:13

Well, it does say right before the doctest (lines 1416-1418 of number_field_element.pyx)

```
        For degree greater than 5, sometimes Galois theory prevents a
        closed-form solution.  In this case, a numerical approximation
        is used::
```

Given this and the output of the doctest (-1.1673040153), I think numerical approximation is the way to go.  Do you want to make a new patch with this change (and also fixing the "approximtae" typo that you pointed out)?  I think that it can be given a positive review if it passes all doctests.


---

Comment by jhpalmieri created at 2009-10-08 03:25:02

> Do you want to make a new patch 

Sorry, this is silly.  I'll make a referee's patch since you already said exactly what to do.  I'm running doctests now, and if all goes well, I'll post the referee's patch and a positive review.


---

Attachment

Based on 4.1.2.rc1.alpha3


---

Comment by kcrisman created at 2009-10-08 03:57:32

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2009-10-08 03:57:32

Sorry, I was away from the computer when you posted that last comment, and made a new patch already.  I assume that this patch will do the same thing you were about to do. However, it does fix a doctest issue in calculus/calculus.py (a numerical integral), so perhaps it will save you a little trouble if I post this.  The issue may also be platform-dependent, so maybe it helped discover something good - you can use ... to comment the last digit out if that's what it turns out to be.

Incidentally, my initial thought was that the 1416ff. lines were an overzealous doctester earlier, after to_poly_solve was first incorporated.  But someone else can change that if that's not the desired behavior.


---

Comment by kcrisman created at 2009-10-08 13:46:06

Okay, I checked on a Intel and it IS plaform-dependent.  So here's the real patch.  Sorry for the confusion, jhpalmieri - you've been very helpful.


---

Comment by kcrisman created at 2009-10-08 13:47:24

Sorry, use last patch, I keep on forgetting to click "replace".


---

Comment by jhpalmieri created at 2009-10-08 14:55:15

I came to the same conclusion.  Now all tests pass.


---

Comment by jhpalmieri created at 2009-10-08 14:55:15

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2009-10-08 16:01:27

Just FYI, this will probably not get in before 4.1.2, and at #7112 William has already fixed the numerical noise issue.  So we'll probably have to remove it.  Sigh.


---

Attachment

Based on 4.1.2.rc1.alpha3


---

Comment by kcrisman created at 2009-10-14 20:08:42

This most recent one should hopefully apply well to 4.1.2 itself.  The only change was to remove a doctest fix that was already in #7112, so shouldn't disturb anything else.


---

Comment by mhansen created at 2009-10-15 09:05:10

Resolution: fixed
