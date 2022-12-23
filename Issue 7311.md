# Issue 7311: Change min/max arguments

Issue created by migration from https://trac.sagemath.org/ticket/7311

Original creator: ncohen

Original creation time: 2009-10-26 13:33:33

Assignee: jkantor

CC:  abmasse

Instead of None when a variable or a constraint of a MixedIntegerLinearProgram is not bounded, it may be more correct to set it to infinity.


---

Comment by ncohen created at 2010-01-15 15:56:55

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-01-27 08:47:31

Jeffrey Kantor smartly noticed it may not be a good idea to have > be an alias for >= when dealing with integer programs... Fixed :-)

Nathann


---

Comment by ncohen created at 2010-01-30 20:01:18

Changing priority from minor to critical.


---

Comment by abmasse created at 2010-02-28 10:53:31

I started looking at your patch. I think it shouldn't be too hard to review. All tests pass !

However, I have one question: is there a reason why you implement all operators <, >, >=, etc. ? You could only implement `__richcmp__` and would do the same job with only one function.

Another strange thing is that the tests pass only when I install GLPK. With CBC, nothing works. Is that normal ?


---

Comment by ncohen created at 2010-02-28 11:08:06

Hello !!!!

I remember having tried the two This patch has had many different versions At some point some of these classes were "cdef class", then got back to usual python... I remember having noticed at some point that if I were to define < > == ... using richcmp instead of the usual python operators, other low-level comparators would be used by default instead of mine. Well, I had many troubles with this class, so perhaps I should give it a try again now that it works again :-)

It is not normal at all that nothing works with CBC :-/
Could you tell me which kind of errors you get ? 

Thank youuuuuuuuu !!

Nathann


---

Comment by abmasse created at 2010-02-28 11:58:04

Here is what I did:

1. I tested all sage with `sage -testall` and all tests passed.

2. I tried `sage -t -optional` on the folder sage/numerical. Of course, some tests didn't pass.

3. I installed CBC. All tests passed with `sage -t *` in the sage/numerical folder, but when I type `sage -t -optional *`, I get the following:


```
[~/Applications/sage/devel/sage-linear/sage/numerical]$ sage -t -optional *
sage -t -optional "devel/sage-linear/sage/numerical/__init__.py"
	 [0.2 s]
sage -t -optional "devel/sage-linear/sage/numerical/all.py" 
	 [0.1 s]
sage -t -optional "devel/sage-linear/sage/numerical/knapsack.py"
	 [13.8 s]
sage -t -optional "devel/sage-linear/sage/numerical/mip.pyx"
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx", line 444:
    sage: p.write_mps(SAGE_TMP+"/lp_problem.mps") # optional - requires GLPK
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_12[6]>", line 1, in <module>
        p.write_mps(SAGE_TMP+"/lp_problem.mps") # optional - requires GLPK###line 444:
    sage: p.write_mps(SAGE_TMP+"/lp_problem.mps") # optional - requires GLPK
      File "mip.pyx", line 453, in sage.numerical.mip.MixedIntegerLinearProgram.write_mps (sage/numerical/mip.c:4108)
        raise NotImplementedError("You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')")
    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx", line 476:
    sage: p.write_lp(SAGE_TMP+"/lp_problem.lp") # optional - requires GLPK
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[6]>", line 1, in <module>
        p.write_lp(SAGE_TMP+"/lp_problem.lp") # optional - requires GLPK###line 476:
    sage: p.write_lp(SAGE_TMP+"/lp_problem.lp") # optional - requires GLPK
      File "mip.pyx", line 484, in sage.numerical.mip.MixedIntegerLinearProgram.write_lp (sage/numerical/mip.c:4329)
        raise NotImplementedError("You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')")
    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx", line 978:
    sage: p.solve(solver='GLPK', objective_only=True) # optional - requires GLPK
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError
Got:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_23[21]>", line 1, in <module>
        p.solve(solver='GLPK', objective_only=True) # optional - requires GLPK###line 978:
    sage: p.solve(solver='GLPK', objective_only=True) # optional - requires GLPK
      File "mip.pyx", line 1004, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7627)
        raise NotImplementedError("GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')")
    NotImplementedError: GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx", line 1175:
    sage: p.solve(solver="GLPK") # optional - requires GLPK
Expected:
    Traceback (most recent call last):
    ...
    MIPSolverException: 'GLPK : Solution is undefined'
Got:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_30[9]>", line 1, in <module>
        p.solve(solver="GLPK") # optional - requires GLPK###line 1175:
    sage: p.solve(solver="GLPK") # optional - requires GLPK
      File "mip.pyx", line 1004, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7627)
        raise NotImplementedError("GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')")
    NotImplementedError: GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx", line 1191:
    sage: p.solve(solver="GLPK") # optional - requires GLPK
Expected:
    Traceback (most recent call last):
    ...
    MIPSolverException: 'GLPK : Solution is undefined'
Got:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_30[16]>", line 1, in <module>
        p.solve(solver="GLPK") # optional - requires GLPK###line 1191:
    sage: p.solve(solver="GLPK") # optional - requires GLPK
      File "mip.pyx", line 1004, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7627)
        raise NotImplementedError("GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')")
    NotImplementedError: GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')
**********************************************************************
4 items had failures:
   1 of   7 in __main__.example_12
   1 of   7 in __main__.example_13
   1 of  22 in __main__.example_23
   2 of  17 in __main__.example_30
***Test Failed*** 5 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_mip.py
	 [3.1 s]
sage -t -optional "devel/sage-linear/sage/numerical/mip_coin.pyx"
	 [2.6 s]
sage -t -optional "devel/sage-linear/sage/numerical/mip_glpk.pyx"
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx", line 41:
    sage: from sage.numerical.mip_glpk import solve_glpk    # optional - requires Glpk
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        from sage.numerical.mip_glpk import solve_glpk    # optional - requires Glpk###line 41:
    sage: from sage.numerical.mip_glpk import solve_glpk    # optional - requires Glpk
    ImportError: No module named mip_glpk
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx", line 49:
    sage: solve_glpk(p, objective_only=True)     # optional - requires Glpk
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[9]>", line 1, in <module>
        solve_glpk(p, objective_only=True)     # optional - requires Glpk###line 49:
    sage: solve_glpk(p, objective_only=True)     # optional - requires Glpk
    NameError: name 'solve_glpk' is not defined
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx", line 123:
    sage: p.write_mps(SAGE_TMP+"/lp_problem.mps") # optional - requires GLPK
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[6]>", line 1, in <module>
        p.write_mps(SAGE_TMP+"/lp_problem.mps") # optional - requires GLPK###line 123:
    sage: p.write_mps(SAGE_TMP+"/lp_problem.mps") # optional - requires GLPK
      File "mip.pyx", line 453, in sage.numerical.mip.MixedIntegerLinearProgram.write_mps (sage/numerical/mip.c:4108)
        raise NotImplementedError("You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')")
    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')
**********************************************************************
File "/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx", line 164:
    sage: p.write_lp(SAGE_TMP+"/lp_problem.lp") # optional - requires GLPK
Exception raised:
    Traceback (most recent call last):
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/alexandre/Applications/sage/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[6]>", line 1, in <module>
        p.write_lp(SAGE_TMP+"/lp_problem.lp") # optional - requires GLPK###line 164:
    sage: p.write_lp(SAGE_TMP+"/lp_problem.lp") # optional - requires GLPK
      File "mip.pyx", line 484, in sage.numerical.mip.MixedIntegerLinearProgram.write_lp (sage/numerical/mip.c:4329)
        raise NotImplementedError("You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')")
    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')
**********************************************************************
3 items had failures:
   2 of  10 in __main__.example_1
   1 of   7 in __main__.example_2
   1 of   7 in __main__.example_3
***Test Failed*** 4 failures.
For whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_mip_glpk.py
	 [2.6 s]
sage -t -optional "devel/sage-linear/sage/numerical/optimize.py"
	 [5.7 s]
sage -t -optional "devel/sage-linear/sage/numerical/test.py"
	 [5.7 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -optional "devel/sage-linear/sage/numerical/mip.pyx"
	sage -t -optional "devel/sage-linear/sage/numerical/mip_glpk.pyx"
Total time for all tests: 33.9 seconds
```


4. I then installed GLPK, and then all tests passed, with the command `sage -t *` as well as the command `sage -t -optional *`.

If I'm not mistaken and if my installation is not broken, it means that the examples you included in the docstring are based on GLPK and not CBC.


---

Comment by ncohen created at 2010-02-28 12:03:26

Then it is not a problem at all :-)

The errors you see are in no way related to the present patch. You can see in all of your error messages that the line at fault if followed by : optional - requires GLPK. Note that there is no mention of CBC in those.

These lines are GLPK-specific as they are those who define the functions exporting a LP to a .mps or a .lp file, which make use of the GLPK library.

You had me worried for a while ! :-)

Nathann


---

Comment by abmasse created at 2010-02-28 12:15:47

Great ! Sorry for my comments, I'm not familiar enough with these two optional packages. I'll resume reviewing the patch later today.


---

Comment by abmasse created at 2010-03-01 21:56:13

I looked once again at your patch. It seems correct, but I have a few comments:

1. Around line 711, you write


```
f = linear_function.f
```


Woudn't be better to access this value by a function that LinearFunction provides ? More precisely, LinearFunction objects should have a method `f()` or `function()` and a private attribute `_f`. This is not a big problem, but seems cleaner. Same remark with `linear_function.constraints` of line 733 and `linear_function.equality` of line 735.

2. This is more a style remark. You tend to put a lot of space in your code, but I feel there is too much, which causes the body of the functions to span more lines than terminals can display.

Short of that, the code seems ok, and all tests even optional pass. There are some typos in the doc, but I can fix it while reviewing. As soon as you answer/correct item 1, I should be able to finish reviewing it.


---

Comment by ncohen created at 2010-03-02 09:35:50

Here it is ! A new .dict() method for LinearFunction :-)

I looked for long lines in the code, but I did not know how to fold them without making it much harder to understand... :-/

If you find one you think can be safely cut, do not hesitate though :-)

Thank you again for your help !

Nathann


---

Comment by abmasse created at 2010-03-02 22:23:24

Hello again Nathann !

I looked once again at your patch. You'll see that I added one on top of yours: it only modifies the formatting in the code and in the documentation, nothing major. In particular, I removed empty lines where they didn't seem necessary to me. I should give a positive review to your ticket very soon, but before that, there are some questions I would like you to answer.

1. There is a parameter `name` to the `add_constraint` function of `MixedIntegerLinearProgram`. Why do you need such a parameter ? I'm sure there is a good reason, but it would be nice to illustrate by an example why this is helpful.

2. Around line 715, you have `constant_coefficient = f.pop(-1,0)`. Isn't it dangerous ? If I'm not mistaken, this modifies the parameter `linear_function` and could have unsuspected side effects ?

3. Since functions such as `__init__`, `__eq__`, etc. do not appear in the documentation, it would be better to have more detailed documentation just under the declaration of the class. Instead of `A class to represent Linear Constraints`, you could describe in detail what it is used for and give some examples.

Sorry again for bothering you ! Don't forget to apply my patch if you want to add some modifications to yours. Next time should be a positive review !


---

Comment by abmasse created at 2010-03-03 07:53:12

4. There are still lines of code of the form

```
functions = linear_function.constraints 
if linear_function.equality: 
```

It's true that you do not modify the `linear_function` object (you seem only to access the `constraints` and `equality` objects, but this would be cleaner to have methods that give you access to these.


---

Comment by ncohen created at 2010-03-03 09:49:14

Hello !! I will be answering your questions today :-)

Meanhile, I understand that I access many fields without calling methods, but in the end as this class is very short (and as I don't directly access fields without calling methods when outside of the definition of this class), I feel like adding many other methods would just create more calls to function, thus slowing it a bit, without really improving the readability.

Well, I don't mind changing it anyway, but ... What do you think ?

Nathann


---

Comment by abmasse created at 2010-03-03 09:56:34

I agree with you, since speed is very important in MILPs, it is reasonable... Forget about what I said. However, I still think there is a reasonable way to extract the constant coefficient without having to modify the object returned by the `dict()` function. As for item 4, maybe this could be addressed in another ticket.


---

Comment by ncohen created at 2010-03-03 13:16:20

Hello !!!!

First, this new patch contains first my file trac_7311.patch, along with your corrections from trac_7311_review-abm.patch (and my thanks for your time!).

 # (we talked about this together, but for the completeness of this ticket...). The names for Variables and Constraints are totally "useless" at the moment. Well, they can be useful only when one is trying to export a MixedIntegerLinearProgram object to a .mps or a .lp file using the methods write_mps and write_lp. This way, anyone can export the program and try to solve it using a different solver, as these files are standard types to encode a LP, and clearly having names in such a file instead of having variables like x1 x2 x3, .... and constraints like c1 c2 c3, ... can help at some point :-)

   Besides, I have not lost hope of touching the .show() method so that it would use the names of these variables/constraints when the user wants to see his LP.

 # It is dangerous. And it is a mistake :-)

 # I thought the documentation from __init__ appeared when typing MixedIntegerLinearProgram? .... A bit silly not to have noticed it until now.... You're perfectly right ! I copied the documentation from __init__ several lines above and added a few lines to explain what the class does. It is likely no one but developpers will ever get interested in this class, as it does not appear when using LP.

And here is the new version of the patch :-)

Nathann


---

Attachment

Minor doc and code formatting fixes -- apply on top of Nathann's patch


---

Attachment

I tested Nathann's patch on sage-4.3.3. All tests passed and the documentation builds fine, except for the signature of many functions since the main involved file is a Cython file (this issue seems to have been solved in #8244).

Note that all non optional tests passed with neither GLPK nor CBC installed, and all tests including optional ones pass when I installed both GLPK and CBC.

I made some minor changes on code formatting and documentation. If Nathann agrees with my changes, I allow him to set this ticket to a positive review.


---

Comment by ncohen created at 2010-03-04 14:34:04

Thank you very much !! But what do you mean about problems with the signatures of functions ? O_o

Nathann


---

Comment by abmasse created at 2010-03-04 14:43:25

When you run ``sage -docbuild reference html``, you get the following warnings:


```
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.LinearFunction.dict: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.depth: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.items: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.keys: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.values: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.add_constraint: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.constraints: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_max: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_min: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_values: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_binary: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_integer: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_real: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.new_variable: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_binary: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_integer: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_max: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_min: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective_name: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_problem_name: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_real: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.show: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.solve: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_lp: arg is not a Python function
/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_mps: arg is not a Python function
```


Sphinx has some problem to deal with Cython files when generating the documentation and this issue was discussed in #8244.


---

Comment by ncohen created at 2010-03-04 16:20:46

OOps, ok, I see.... Then I accept your positive review and your fixes :-)

Thank you very much !!!!

Nathann


---

Comment by ncohen created at 2010-03-04 16:20:46

Changing status from needs_review to positive_review.


---

Comment by abmasse created at 2010-03-10 21:33:33

Changing status from positive_review to needs_work.


---

Comment by abmasse created at 2010-03-10 21:33:33

While retesting the patch, I noticed that some tests didn't pass when one doesn't have CBC or GLPK installed.

This means that some doctest wasn't tagged "optional" properly. Sorry about that, Nathann, but there is still some work to do. I'll try to identify the bugs tonight.


---

Comment by abmasse created at 2010-03-10 21:40:10

Changing status from needs_work to needs_review.


---

Comment by abmasse created at 2010-03-10 21:40:10

Sorry about my last comment, everything seems fine. This is very complicated to test optional packages properly... I have too many copies of sage on my computer. Positive review.


---

Comment by abmasse created at 2010-03-10 21:40:29

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-15 23:41:28

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-15 23:41:28

Merged into 4.4.alpha0:
 - trac_7311.patch
 - trac_7311_review-abm.patch
