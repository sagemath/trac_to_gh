# Issue 7311: Change min/max arguments

archive/issues_007311.json:
```json
{
    "body": "Assignee: jkantor\n\nCC:  abmasse\n\nInstead of None when a variable or a constraint of a MixedIntegerLinearProgram is not bounded, it may be more correct to set it to infinity.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7311\n\n",
    "created_at": "2009-10-26T13:33:33Z",
    "labels": [
        "numerical",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4",
    "title": "Change min/max arguments",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7311",
    "user": "ncohen"
}
```
Assignee: jkantor

CC:  abmasse

Instead of None when a variable or a constraint of a MixedIntegerLinearProgram is not bounded, it may be more correct to set it to infinity.

Issue created by migration from https://trac.sagemath.org/ticket/7311





---

archive/issue_comments_061071.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-15T15:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61071",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061072.json:
```json
{
    "body": "Jeffrey Kantor smartly noticed it may not be a good idea to have > be an alias for >= when dealing with integer programs... Fixed :-)\n\nNathann",
    "created_at": "2010-01-27T08:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61072",
    "user": "ncohen"
}
```

Jeffrey Kantor smartly noticed it may not be a good idea to have > be an alias for >= when dealing with integer programs... Fixed :-)

Nathann



---

archive/issue_comments_061073.json:
```json
{
    "body": "Changing priority from minor to critical.",
    "created_at": "2010-01-30T20:01:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61073",
    "user": "ncohen"
}
```

Changing priority from minor to critical.



---

archive/issue_comments_061074.json:
```json
{
    "body": "I started looking at your patch. I think it shouldn't be too hard to review. All tests pass !\n\nHowever, I have one question: is there a reason why you implement all operators <, >, >=, etc. ? You could only implement `__richcmp__` and would do the same job with only one function.\n\nAnother strange thing is that the tests pass only when I install GLPK. With CBC, nothing works. Is that normal ?",
    "created_at": "2010-02-28T10:53:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61074",
    "user": "abmasse"
}
```

I started looking at your patch. I think it shouldn't be too hard to review. All tests pass !

However, I have one question: is there a reason why you implement all operators <, >, >=, etc. ? You could only implement `__richcmp__` and would do the same job with only one function.

Another strange thing is that the tests pass only when I install GLPK. With CBC, nothing works. Is that normal ?



---

archive/issue_comments_061075.json:
```json
{
    "body": "Hello !!!!\n\nI remember having tried the two This patch has had many different versions At some point some of these classes were \"cdef class\", then got back to usual python... I remember having noticed at some point that if I were to define < > == ... using richcmp instead of the usual python operators, other low-level comparators would be used by default instead of mine. Well, I had many troubles with this class, so perhaps I should give it a try again now that it works again :-)\n\nIt is not normal at all that nothing works with CBC :-/\nCould you tell me which kind of errors you get ? \n\nThank youuuuuuuuu !!\n\nNathann",
    "created_at": "2010-02-28T11:08:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61075",
    "user": "ncohen"
}
```

Hello !!!!

I remember having tried the two This patch has had many different versions At some point some of these classes were "cdef class", then got back to usual python... I remember having noticed at some point that if I were to define < > == ... using richcmp instead of the usual python operators, other low-level comparators would be used by default instead of mine. Well, I had many troubles with this class, so perhaps I should give it a try again now that it works again :-)

It is not normal at all that nothing works with CBC :-/
Could you tell me which kind of errors you get ? 

Thank youuuuuuuuu !!

Nathann



---

archive/issue_comments_061076.json:
```json
{
    "body": "Here is what I did:\n\n1. I tested all sage with `sage -testall` and all tests passed.\n\n2. I tried `sage -t -optional` on the folder sage/numerical. Of course, some tests didn't pass.\n\n3. I installed CBC. All tests passed with `sage -t *` in the sage/numerical folder, but when I type `sage -t -optional *`, I get the following:\n\n\n```\n[~/Applications/sage/devel/sage-linear/sage/numerical]$ sage -t -optional *\nsage -t -optional \"devel/sage-linear/sage/numerical/__init__.py\"\n\t [0.2 s]\nsage -t -optional \"devel/sage-linear/sage/numerical/all.py\" \n\t [0.1 s]\nsage -t -optional \"devel/sage-linear/sage/numerical/knapsack.py\"\n\t [13.8 s]\nsage -t -optional \"devel/sage-linear/sage/numerical/mip.pyx\"\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx\", line 444:\n    sage: p.write_mps(SAGE_TMP+\"/lp_problem.mps\") # optional - requires GLPK\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_12[6]>\", line 1, in <module>\n        p.write_mps(SAGE_TMP+\"/lp_problem.mps\") # optional - requires GLPK###line 444:\n    sage: p.write_mps(SAGE_TMP+\"/lp_problem.mps\") # optional - requires GLPK\n      File \"mip.pyx\", line 453, in sage.numerical.mip.MixedIntegerLinearProgram.write_mps (sage/numerical/mip.c:4108)\n        raise NotImplementedError(\"You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\")\n    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx\", line 476:\n    sage: p.write_lp(SAGE_TMP+\"/lp_problem.lp\") # optional - requires GLPK\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[6]>\", line 1, in <module>\n        p.write_lp(SAGE_TMP+\"/lp_problem.lp\") # optional - requires GLPK###line 476:\n    sage: p.write_lp(SAGE_TMP+\"/lp_problem.lp\") # optional - requires GLPK\n      File \"mip.pyx\", line 484, in sage.numerical.mip.MixedIntegerLinearProgram.write_lp (sage/numerical/mip.c:4329)\n        raise NotImplementedError(\"You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\")\n    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx\", line 978:\n    sage: p.solve(solver='GLPK', objective_only=True) # optional - requires GLPK\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError\nGot:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_23[21]>\", line 1, in <module>\n        p.solve(solver='GLPK', objective_only=True) # optional - requires GLPK###line 978:\n    sage: p.solve(solver='GLPK', objective_only=True) # optional - requires GLPK\n      File \"mip.pyx\", line 1004, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7627)\n        raise NotImplementedError(\"GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')\")\n    NotImplementedError: GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx\", line 1175:\n    sage: p.solve(solver=\"GLPK\") # optional - requires GLPK\nExpected:\n    Traceback (most recent call last):\n    ...\n    MIPSolverException: 'GLPK : Solution is undefined'\nGot:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_30[9]>\", line 1, in <module>\n        p.solve(solver=\"GLPK\") # optional - requires GLPK###line 1175:\n    sage: p.solve(solver=\"GLPK\") # optional - requires GLPK\n      File \"mip.pyx\", line 1004, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7627)\n        raise NotImplementedError(\"GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')\")\n    NotImplementedError: GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip.pyx\", line 1191:\n    sage: p.solve(solver=\"GLPK\") # optional - requires GLPK\nExpected:\n    Traceback (most recent call last):\n    ...\n    MIPSolverException: 'GLPK : Solution is undefined'\nGot:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_30[16]>\", line 1, in <module>\n        p.solve(solver=\"GLPK\") # optional - requires GLPK###line 1191:\n    sage: p.solve(solver=\"GLPK\") # optional - requires GLPK\n      File \"mip.pyx\", line 1004, in sage.numerical.mip.MixedIntegerLinearProgram.solve (sage/numerical/mip.c:7627)\n        raise NotImplementedError(\"GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')\")\n    NotImplementedError: GLPK is not installed and cannot be used to solve this MixedIntegerLinearProgram. To install it, you can type in Sage: install_package('glpk')\n**********************************************************************\n4 items had failures:\n   1 of   7 in __main__.example_12\n   1 of   7 in __main__.example_13\n   1 of  22 in __main__.example_23\n   2 of  17 in __main__.example_30\n***Test Failed*** 5 failures.\nFor whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_mip.py\n\t [3.1 s]\nsage -t -optional \"devel/sage-linear/sage/numerical/mip_coin.pyx\"\n\t [2.6 s]\nsage -t -optional \"devel/sage-linear/sage/numerical/mip_glpk.pyx\"\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx\", line 41:\n    sage: from sage.numerical.mip_glpk import solve_glpk    # optional - requires Glpk\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[2]>\", line 1, in <module>\n        from sage.numerical.mip_glpk import solve_glpk    # optional - requires Glpk###line 41:\n    sage: from sage.numerical.mip_glpk import solve_glpk    # optional - requires Glpk\n    ImportError: No module named mip_glpk\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx\", line 49:\n    sage: solve_glpk(p, objective_only=True)     # optional - requires Glpk\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[9]>\", line 1, in <module>\n        solve_glpk(p, objective_only=True)     # optional - requires Glpk###line 49:\n    sage: solve_glpk(p, objective_only=True)     # optional - requires Glpk\n    NameError: name 'solve_glpk' is not defined\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx\", line 123:\n    sage: p.write_mps(SAGE_TMP+\"/lp_problem.mps\") # optional - requires GLPK\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[6]>\", line 1, in <module>\n        p.write_mps(SAGE_TMP+\"/lp_problem.mps\") # optional - requires GLPK###line 123:\n    sage: p.write_mps(SAGE_TMP+\"/lp_problem.mps\") # optional - requires GLPK\n      File \"mip.pyx\", line 453, in sage.numerical.mip.MixedIntegerLinearProgram.write_mps (sage/numerical/mip.c:4108)\n        raise NotImplementedError(\"You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\")\n    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\n**********************************************************************\nFile \"/Users/alexandre/Applications/sage/devel/sage-linear/sage/numerical/mip_glpk.pyx\", line 164:\n    sage: p.write_lp(SAGE_TMP+\"/lp_problem.lp\") # optional - requires GLPK\nException raised:\n    Traceback (most recent call last):\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/Users/alexandre/Applications/sage/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[6]>\", line 1, in <module>\n        p.write_lp(SAGE_TMP+\"/lp_problem.lp\") # optional - requires GLPK###line 164:\n    sage: p.write_lp(SAGE_TMP+\"/lp_problem.lp\") # optional - requires GLPK\n      File \"mip.pyx\", line 484, in sage.numerical.mip.MixedIntegerLinearProgram.write_lp (sage/numerical/mip.c:4329)\n        raise NotImplementedError(\"You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\")\n    NotImplementedError: You need GLPK installed to use this function. To install it, you can type in Sage: install_package('glpk')\n**********************************************************************\n3 items had failures:\n   2 of  10 in __main__.example_1\n   1 of   7 in __main__.example_2\n   1 of   7 in __main__.example_3\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /Users/alexandre/.sage//tmp/.doctest_mip_glpk.py\n\t [2.6 s]\nsage -t -optional \"devel/sage-linear/sage/numerical/optimize.py\"\n\t [5.7 s]\nsage -t -optional \"devel/sage-linear/sage/numerical/test.py\"\n\t [5.7 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -optional \"devel/sage-linear/sage/numerical/mip.pyx\"\n\tsage -t -optional \"devel/sage-linear/sage/numerical/mip_glpk.pyx\"\nTotal time for all tests: 33.9 seconds\n```\n\n\n4. I then installed GLPK, and then all tests passed, with the command `sage -t *` as well as the command `sage -t -optional *`.\n\nIf I'm not mistaken and if my installation is not broken, it means that the examples you included in the docstring are based on GLPK and not CBC.",
    "created_at": "2010-02-28T11:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61076",
    "user": "abmasse"
}
```

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

archive/issue_comments_061077.json:
```json
{
    "body": "Then it is not a problem at all :-)\n\nThe errors you see are in no way related to the present patch. You can see in all of your error messages that the line at fault if followed by : optional - requires GLPK. Note that there is no mention of CBC in those.\n\nThese lines are GLPK-specific as they are those who define the functions exporting a LP to a .mps or a .lp file, which make use of the GLPK library.\n\nYou had me worried for a while ! :-)\n\nNathann",
    "created_at": "2010-02-28T12:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61077",
    "user": "ncohen"
}
```

Then it is not a problem at all :-)

The errors you see are in no way related to the present patch. You can see in all of your error messages that the line at fault if followed by : optional - requires GLPK. Note that there is no mention of CBC in those.

These lines are GLPK-specific as they are those who define the functions exporting a LP to a .mps or a .lp file, which make use of the GLPK library.

You had me worried for a while ! :-)

Nathann



---

archive/issue_comments_061078.json:
```json
{
    "body": "Great ! Sorry for my comments, I'm not familiar enough with these two optional packages. I'll resume reviewing the patch later today.",
    "created_at": "2010-02-28T12:15:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61078",
    "user": "abmasse"
}
```

Great ! Sorry for my comments, I'm not familiar enough with these two optional packages. I'll resume reviewing the patch later today.



---

archive/issue_comments_061079.json:
```json
{
    "body": "I looked once again at your patch. It seems correct, but I have a few comments:\n\n1. Around line 711, you write\n\n\n```\nf = linear_function.f\n```\n\n\nWoudn't be better to access this value by a function that LinearFunction provides ? More precisely, LinearFunction objects should have a method `f()` or `function()` and a private attribute `_f`. This is not a big problem, but seems cleaner. Same remark with `linear_function.constraints` of line 733 and `linear_function.equality` of line 735.\n\n2. This is more a style remark. You tend to put a lot of space in your code, but I feel there is too much, which causes the body of the functions to span more lines than terminals can display.\n\nShort of that, the code seems ok, and all tests even optional pass. There are some typos in the doc, but I can fix it while reviewing. As soon as you answer/correct item 1, I should be able to finish reviewing it.",
    "created_at": "2010-03-01T21:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61079",
    "user": "abmasse"
}
```

I looked once again at your patch. It seems correct, but I have a few comments:

1. Around line 711, you write


```
f = linear_function.f
```


Woudn't be better to access this value by a function that LinearFunction provides ? More precisely, LinearFunction objects should have a method `f()` or `function()` and a private attribute `_f`. This is not a big problem, but seems cleaner. Same remark with `linear_function.constraints` of line 733 and `linear_function.equality` of line 735.

2. This is more a style remark. You tend to put a lot of space in your code, but I feel there is too much, which causes the body of the functions to span more lines than terminals can display.

Short of that, the code seems ok, and all tests even optional pass. There are some typos in the doc, but I can fix it while reviewing. As soon as you answer/correct item 1, I should be able to finish reviewing it.



---

archive/issue_comments_061080.json:
```json
{
    "body": "Here it is ! A new .dict() method for LinearFunction :-)\n\nI looked for long lines in the code, but I did not know how to fold them without making it much harder to understand... :-/\n\nIf you find one you think can be safely cut, do not hesitate though :-)\n\nThank you again for your help !\n\nNathann",
    "created_at": "2010-03-02T09:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61080",
    "user": "ncohen"
}
```

Here it is ! A new .dict() method for LinearFunction :-)

I looked for long lines in the code, but I did not know how to fold them without making it much harder to understand... :-/

If you find one you think can be safely cut, do not hesitate though :-)

Thank you again for your help !

Nathann



---

archive/issue_comments_061081.json:
```json
{
    "body": "Hello again Nathann !\n\nI looked once again at your patch. You'll see that I added one on top of yours: it only modifies the formatting in the code and in the documentation, nothing major. In particular, I removed empty lines where they didn't seem necessary to me. I should give a positive review to your ticket very soon, but before that, there are some questions I would like you to answer.\n\n1. There is a parameter `name` to the `add_constraint` function of `MixedIntegerLinearProgram`. Why do you need such a parameter ? I'm sure there is a good reason, but it would be nice to illustrate by an example why this is helpful.\n\n2. Around line 715, you have `constant_coefficient = f.pop(-1,0)`. Isn't it dangerous ? If I'm not mistaken, this modifies the parameter `linear_function` and could have unsuspected side effects ?\n\n3. Since functions such as `__init__`, `__eq__`, etc. do not appear in the documentation, it would be better to have more detailed documentation just under the declaration of the class. Instead of `A class to represent Linear Constraints`, you could describe in detail what it is used for and give some examples.\n\nSorry again for bothering you ! Don't forget to apply my patch if you want to add some modifications to yours. Next time should be a positive review !",
    "created_at": "2010-03-02T22:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61081",
    "user": "abmasse"
}
```

Hello again Nathann !

I looked once again at your patch. You'll see that I added one on top of yours: it only modifies the formatting in the code and in the documentation, nothing major. In particular, I removed empty lines where they didn't seem necessary to me. I should give a positive review to your ticket very soon, but before that, there are some questions I would like you to answer.

1. There is a parameter `name` to the `add_constraint` function of `MixedIntegerLinearProgram`. Why do you need such a parameter ? I'm sure there is a good reason, but it would be nice to illustrate by an example why this is helpful.

2. Around line 715, you have `constant_coefficient = f.pop(-1,0)`. Isn't it dangerous ? If I'm not mistaken, this modifies the parameter `linear_function` and could have unsuspected side effects ?

3. Since functions such as `__init__`, `__eq__`, etc. do not appear in the documentation, it would be better to have more detailed documentation just under the declaration of the class. Instead of `A class to represent Linear Constraints`, you could describe in detail what it is used for and give some examples.

Sorry again for bothering you ! Don't forget to apply my patch if you want to add some modifications to yours. Next time should be a positive review !



---

archive/issue_comments_061082.json:
```json
{
    "body": "4. There are still lines of code of the form\n\n```\nfunctions = linear_function.constraints \nif linear_function.equality: \n```\n\nIt's true that you do not modify the `linear_function` object (you seem only to access the `constraints` and `equality` objects, but this would be cleaner to have methods that give you access to these.",
    "created_at": "2010-03-03T07:53:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61082",
    "user": "abmasse"
}
```

4. There are still lines of code of the form

```
functions = linear_function.constraints 
if linear_function.equality: 
```

It's true that you do not modify the `linear_function` object (you seem only to access the `constraints` and `equality` objects, but this would be cleaner to have methods that give you access to these.



---

archive/issue_comments_061083.json:
```json
{
    "body": "Hello !! I will be answering your questions today :-)\n\nMeanhile, I understand that I access many fields without calling methods, but in the end as this class is very short (and as I don't directly access fields without calling methods when outside of the definition of this class), I feel like adding many other methods would just create more calls to function, thus slowing it a bit, without really improving the readability.\n\nWell, I don't mind changing it anyway, but ... What do you think ?\n\nNathann",
    "created_at": "2010-03-03T09:49:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61083",
    "user": "ncohen"
}
```

Hello !! I will be answering your questions today :-)

Meanhile, I understand that I access many fields without calling methods, but in the end as this class is very short (and as I don't directly access fields without calling methods when outside of the definition of this class), I feel like adding many other methods would just create more calls to function, thus slowing it a bit, without really improving the readability.

Well, I don't mind changing it anyway, but ... What do you think ?

Nathann



---

archive/issue_comments_061084.json:
```json
{
    "body": "I agree with you, since speed is very important in MILPs, it is reasonable... Forget about what I said. However, I still think there is a reasonable way to extract the constant coefficient without having to modify the object returned by the `dict()` function. As for item 4, maybe this could be addressed in another ticket.",
    "created_at": "2010-03-03T09:56:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61084",
    "user": "abmasse"
}
```

I agree with you, since speed is very important in MILPs, it is reasonable... Forget about what I said. However, I still think there is a reasonable way to extract the constant coefficient without having to modify the object returned by the `dict()` function. As for item 4, maybe this could be addressed in another ticket.



---

archive/issue_comments_061085.json:
```json
{
    "body": "Hello !!!!\n\nFirst, this new patch contains first my file trac_7311.patch, along with your corrections from trac_7311_review-abm.patch (and my thanks for your time!).\n\n # (we talked about this together, but for the completeness of this ticket...). The names for Variables and Constraints are totally \"useless\" at the moment. Well, they can be useful only when one is trying to export a MixedIntegerLinearProgram object to a .mps or a .lp file using the methods write_mps and write_lp. This way, anyone can export the program and try to solve it using a different solver, as these files are standard types to encode a LP, and clearly having names in such a file instead of having variables like x1 x2 x3, .... and constraints like c1 c2 c3, ... can help at some point :-)\n\n   Besides, I have not lost hope of touching the .show() method so that it would use the names of these variables/constraints when the user wants to see his LP.\n\n # It is dangerous. And it is a mistake :-)\n\n # I thought the documentation from __init__ appeared when typing MixedIntegerLinearProgram? .... A bit silly not to have noticed it until now.... You're perfectly right ! I copied the documentation from __init__ several lines above and added a few lines to explain what the class does. It is likely no one but developpers will ever get interested in this class, as it does not appear when using LP.\n\nAnd here is the new version of the patch :-)\n\nNathann",
    "created_at": "2010-03-03T13:16:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61085",
    "user": "ncohen"
}
```

Hello !!!!

First, this new patch contains first my file trac_7311.patch, along with your corrections from trac_7311_review-abm.patch (and my thanks for your time!).

 # (we talked about this together, but for the completeness of this ticket...). The names for Variables and Constraints are totally "useless" at the moment. Well, they can be useful only when one is trying to export a MixedIntegerLinearProgram object to a .mps or a .lp file using the methods write_mps and write_lp. This way, anyone can export the program and try to solve it using a different solver, as these files are standard types to encode a LP, and clearly having names in such a file instead of having variables like x1 x2 x3, .... and constraints like c1 c2 c3, ... can help at some point :-)

   Besides, I have not lost hope of touching the .show() method so that it would use the names of these variables/constraints when the user wants to see his LP.

 # It is dangerous. And it is a mistake :-)

 # I thought the documentation from __init__ appeared when typing MixedIntegerLinearProgram? .... A bit silly not to have noticed it until now.... You're perfectly right ! I copied the documentation from __init__ several lines above and added a few lines to explain what the class does. It is likely no one but developpers will ever get interested in this class, as it does not appear when using LP.

And here is the new version of the patch :-)

Nathann



---

archive/issue_comments_061086.json:
```json
{
    "body": "Attachment [trac_7311.patch](tarball://root/attachments/some-uuid/ticket7311/trac_7311.patch) by abmasse created at 2010-03-04 13:43:28\n\nMinor doc and code formatting fixes -- apply on top of Nathann's patch",
    "created_at": "2010-03-04T13:43:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61086",
    "user": "abmasse"
}
```

Attachment [trac_7311.patch](tarball://root/attachments/some-uuid/ticket7311/trac_7311.patch) by abmasse created at 2010-03-04 13:43:28

Minor doc and code formatting fixes -- apply on top of Nathann's patch



---

archive/issue_comments_061087.json:
```json
{
    "body": "Attachment [trac_7311_review-abm.patch](tarball://root/attachments/some-uuid/ticket7311/trac_7311_review-abm.patch) by abmasse created at 2010-03-04 13:51:35\n\nI tested Nathann's patch on sage-4.3.3. All tests passed and the documentation builds fine, except for the signature of many functions since the main involved file is a Cython file (this issue seems to have been solved in #8244).\n\nNote that all non optional tests passed with neither GLPK nor CBC installed, and all tests including optional ones pass when I installed both GLPK and CBC.\n\nI made some minor changes on code formatting and documentation. If Nathann agrees with my changes, I allow him to set this ticket to a positive review.",
    "created_at": "2010-03-04T13:51:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61087",
    "user": "abmasse"
}
```

Attachment [trac_7311_review-abm.patch](tarball://root/attachments/some-uuid/ticket7311/trac_7311_review-abm.patch) by abmasse created at 2010-03-04 13:51:35

I tested Nathann's patch on sage-4.3.3. All tests passed and the documentation builds fine, except for the signature of many functions since the main involved file is a Cython file (this issue seems to have been solved in #8244).

Note that all non optional tests passed with neither GLPK nor CBC installed, and all tests including optional ones pass when I installed both GLPK and CBC.

I made some minor changes on code formatting and documentation. If Nathann agrees with my changes, I allow him to set this ticket to a positive review.



---

archive/issue_comments_061088.json:
```json
{
    "body": "Thank you very much !! But what do you mean about problems with the signatures of functions ? O_o\n\nNathann",
    "created_at": "2010-03-04T14:34:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61088",
    "user": "ncohen"
}
```

Thank you very much !! But what do you mean about problems with the signatures of functions ? O_o

Nathann



---

archive/issue_comments_061089.json:
```json
{
    "body": "When you run ``sage -docbuild reference html``, you get the following warnings:\n\n\n```\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.LinearFunction.dict: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.depth: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.items: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.keys: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MIPVariable.values: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.add_constraint: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.constraints: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_max: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_min: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.get_values: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_binary: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_integer: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.is_real: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.new_variable: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_binary: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_integer: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_max: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_min: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_objective_name: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_problem_name: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.set_real: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.show: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.solve: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_lp: arg is not a Python function\n/Users/alexandre/Applications/sage/devel/sage/doc/en/reference/sage/numerical/mip.rst:6: (WARNING/2) error while formatting signature for sage.numerical.mip.MixedIntegerLinearProgram.write_mps: arg is not a Python function\n```\n\n\nSphinx has some problem to deal with Cython files when generating the documentation and this issue was discussed in #8244.",
    "created_at": "2010-03-04T14:43:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61089",
    "user": "abmasse"
}
```

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

archive/issue_comments_061090.json:
```json
{
    "body": "OOps, ok, I see.... Then I accept your positive review and your fixes :-)\n\nThank you very much !!!!\n\nNathann",
    "created_at": "2010-03-04T16:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61090",
    "user": "ncohen"
}
```

OOps, ok, I see.... Then I accept your positive review and your fixes :-)

Thank you very much !!!!

Nathann



---

archive/issue_comments_061091.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T16:20:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61091",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061092.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-03-10T21:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61092",
    "user": "abmasse"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_061093.json:
```json
{
    "body": "While retesting the patch, I noticed that some tests didn't pass when one doesn't have CBC or GLPK installed.\n\nThis means that some doctest wasn't tagged \"optional\" properly. Sorry about that, Nathann, but there is still some work to do. I'll try to identify the bugs tonight.",
    "created_at": "2010-03-10T21:33:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61093",
    "user": "abmasse"
}
```

While retesting the patch, I noticed that some tests didn't pass when one doesn't have CBC or GLPK installed.

This means that some doctest wasn't tagged "optional" properly. Sorry about that, Nathann, but there is still some work to do. I'll try to identify the bugs tonight.



---

archive/issue_comments_061094.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-10T21:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61094",
    "user": "abmasse"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_061095.json:
```json
{
    "body": "Sorry about my last comment, everything seems fine. This is very complicated to test optional packages properly... I have too many copies of sage on my computer. Positive review.",
    "created_at": "2010-03-10T21:40:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61095",
    "user": "abmasse"
}
```

Sorry about my last comment, everything seems fine. This is very complicated to test optional packages properly... I have too many copies of sage on my computer. Positive review.



---

archive/issue_comments_061096.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-10T21:40:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61096",
    "user": "abmasse"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061097.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-04-15T23:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61097",
    "user": "jhpalmieri"
}
```

Resolution: fixed



---

archive/issue_comments_061098.json:
```json
{
    "body": "Merged into 4.4.alpha0:\n- trac_7311.patch\n- trac_7311_review-abm.patch",
    "created_at": "2010-04-15T23:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7311",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7311#issuecomment-61098",
    "user": "jhpalmieri"
}
```

Merged into 4.4.alpha0:
- trac_7311.patch
- trac_7311_review-abm.patch
