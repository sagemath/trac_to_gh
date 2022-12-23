# Issue 4786: fix some bugs / typos in the solve function

Issue created by migration from https://trac.sagemath.org/ticket/4786

Original creator: was

Original creation time: 2008-12-13 21:43:31

Assignee: burcin


```
Is this the right place for suggestions for the function "solve" ?

1) The docstring has a typo : "... solve an equation of system ..."
Should be an "or" here.

2) The section
" solution_dict = True -- return a list of dictionaries containing the
solutions. "
made me think that solution_dict defaults to True which is not the case.
Maybe this could be made more clear.

3) 'solution_dict = True' fails when only a single univariate equation
is given. The solution is then not a list of lists and the conversion to
dictionary fails:

sage: var('a')
a
sage: solve ([a^2-1],a,solution_dict=True)
-
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)

/home/tom/<ipython console> in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/calculus/equations.pyc
in solve(f, *args, **kwds)
  1436         sol_list = string_to_list_of_solutions(a)
  1437         if 'solution_dict' in kwds and kwds['solution_dict']==True:
- -> 1438             sol_dict=[dict([[eq.left(),eq.right()] for eq in
solution]) for solution in sol_list]
  1439             return sol_dict
  1440         else:

AttributeError: 'SymbolicVariable' object has no attribute 'left'


Thanks for your great work.
Thomas
```



---

Attachment


---

Comment by jason created at 2009-01-22 18:27:45

I believe this patch takes care of all the issues pointed out above.


---

Comment by mhansen created at 2009-01-24 15:01:34

I get the following failures:


```
**********************************************************************
File "/opt/sage/devel/sage-main/sage/calculus/equations.py", line 1392:
    sage: solve([3==3, 1.00000000000000*x^3 == 0], x)
Expected:
    [x == 0]
Got:
    [[x == 0]]
**********************************************************************
File "/opt/sage/devel/sage-main/sage/calculus/equations.py", line 1394:
    sage: solve([1.00000000000000*x^3 == 0], x)
Expected:
    [x == 0]
Got:
    [[x == 0]]
```



---

Attachment

Based on 4.1.1


---

Comment by kcrisman created at 2009-08-26 15:27:02

Apply only second patch.  This should fix the same things post-Pynac switch, and passes all tests in sage/calculus and sage/symbolic.


---

Comment by burcin created at 2009-09-10 12:38:50

new version of kcrisman's patch


---

Attachment

Hi Karl-Dieter,

I uploaded a new version of your patch at attachment:trac_4786-solution_dict.take2.patch. The changes are:
 * used `sorted( d.items() )` to print a dictionary in a doctest
 * changed the block:
 {{{
            try:
                sol_dict=[dict([[eq.left(),eq.right()] for eq in solution]) for solution in sol_list]
            except TypeError:
                if not isinstance(sol_list[0],list):
                    sol_list = [[i] for i in sol_list]
                    sol_dict=[dict([[eq.left(),eq.right()] for eq in solution]) for solution in sol_list]
 }}}
 to
 {{{
            if isinstance(sol_list[0], list):
                sol_dict=[dict([[eq.left(),eq.right()] for eq in solution])
                        for solution in sol_list]
            else:
                sol_dict=[{eq.left():eq.right()} for eq in sol_list]
 }}}

Please give this ticket a positive review if you're ok with my changes.

----

Minh, only apply: attachment:trac_4786-solution_dict.take2.patch


---

Comment by kcrisman created at 2009-09-10 14:13:42

That change sounds fine - I am used to catching Errors, but in this case isinstance makes much more sense.

Ironically, though:

```
**********************************************************************
File "/Users/.../sage-4.1.1/devel/sage-morepatchtests/sage/symbolic/relation.py", line 455:
    sage: map(lambda x: sorted(x.items()), res)
Expected:
    [[(y, 4), (x, 2)], [(y, 4), (x, -2)]]
Got:
    [[(x, 2), (y, 4)], [(x, -2), (y, 4)]]
**********************************************************************
```

So I fixed that in the latest version, and hopefully now you can give it positive review!


---

Attachment

Apply only take3.


---

Attachment


---

Comment by burcin created at 2009-09-12 13:15:45

Somehow, `y` is shown first on my laptop, better to just print the values for each variable as Mike has done just a few lines above. 

I attached a new patch only with this doctest changed. Hopefully this is the last one. :)


---

Comment by kcrisman created at 2009-09-13 00:22:15

Looks good!  I guess I don't feel comfortable putting positive review on a patch I largely wrote, but I'll add my name to the reviewer list and you can add your name to the author list if you feel that's appropriate.


---

Comment by burcin created at 2009-09-13 10:35:33

Positive review.


---

Comment by mvngu created at 2009-09-15 19:34:55

Resolution: fixed


---

Comment by mvngu created at 2009-09-15 19:34:55

Merged `trac_4786-solution_dict.take4.patch`.
