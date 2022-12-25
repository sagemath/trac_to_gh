# Issue 4097: [with patch, needs review] matrix automorphism groups

archive/issues_004097.json:
```json
{
    "body": "Assignee: @rlmill\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4097\n\n",
    "created_at": "2008-09-10T09:29:49Z",
    "labels": [
        "component: coding theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with patch, needs review] matrix automorphism groups",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4097",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill



Issue created by migration from https://trac.sagemath.org/ticket/4097





---

archive/issue_comments_029502.json:
```json
{
    "body": "Attachment [trac_4097-mat-aut.patch](tarball://root/attachments/some-uuid/ticket4097/trac_4097-mat-aut.patch) by @wdjoyner created at 2008-09-10 10:55:32\n\nThis is a very important patch - thanks Robert! \n\nI've started testing it and will report back.",
    "created_at": "2008-09-10T10:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29502",
    "user": "https://github.com/wdjoyner"
}
```

Attachment [trac_4097-mat-aut.patch](tarball://root/attachments/some-uuid/ticket4097/trac_4097-mat-aut.patch) by @wdjoyner created at 2008-09-10 10:55:32

This is a very important patch - thanks Robert! 

I've started testing it and will report back.



---

archive/issue_comments_029503.json:
```json
{
    "body": "This failure is on an amd64 gutsy gibbon box (and uses the patch emailed to me by\nRobert, which I guess is the same as the one attached to this ticket):\n\n\n```\nwdj@tinah:~/sagefiles/sage-3.1.2.rc1$ ./sage -t  devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\nsage -t  devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 5:\n    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[2]>\", line 1, in <module>\n        import sage.groups.perm_gps.partn_ref.refinement_matrices###line 5:\n    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices\n    ImportError: No module named refinement_matrices\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 111:\n    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[2]>\", line 1, in <module>\n        from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct###line 111:\n    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct\n    ImportError: No module named refinement_matrices\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 113:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[3]>\", line 1, in <module>\n        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)]]))###line 113:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))\n    NameError: name 'MatrixStruct' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 114:\n    sage: M.run()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[4]>\", line 1, in <module>\n        M.run()###line 114:\n    sage: M.run()\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 115:\n    sage: M.automorphism_group()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[5]>\", line 1, in <module>\n        M.automorphism_group()###line 115:\n    sage: M.automorphism_group()\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 117:\n    sage: M.canonical_relabeling()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[6]>\", line 1, in <module>\n        M.canonical_relabeling()###line 117:\n    sage: M.canonical_relabeling()\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 120:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[7]>\", line 1, in <module>\n        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)],[Integer(1),Integer(0),Integer(2)],[Integer(1),Integer(2),Integer(0)],[Integer(2),Integer(0),Integer(1)],[Integer(2),Integer(1),Integer(0)]]))###line 120:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]))\n    NameError: name 'MatrixStruct' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 121:\n    sage: M.automorphism_group()[1] == 6\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[8]>\", line 1, in <module>\n        M.automorphism_group()[Integer(1)] == Integer(6)###line 121:\n    sage: M.automorphism_group()[1] == 6\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 124:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[9]>\", line 1, in <module>\n        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(1),Integer(2)]]))###line 124:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]]))\n    NameError: name 'MatrixStruct' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 125:\n    sage: M.automorphism_group()[1] == factorial(14)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[10]>\", line 1, in <module>\n        M.automorphism_group()[Integer(1)] == factorial(Integer(14))###line 125:\n    sage: M.automorphism_group()[1] == factorial(14)\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 161:\n    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct###line 161:\n    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct\n    ImportError: No module named refinement_matrices\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 163:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>\n        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)]]))###line 163:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))\n    NameError: name 'MatrixStruct' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 164:\n    sage: M.automorphism_group()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[4]>\", line 1, in <module>\n        M.automorphism_group()###line 164:\n    sage: M.automorphism_group()\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 186:\n    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[2]>\", line 1, in <module>\n        from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct###line 186:\n    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct\n    ImportError: No module named refinement_matrices\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 188:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[3]>\", line 1, in <module>\n        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)]]))###line 188:\n    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))\n    NameError: name 'MatrixStruct' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 189:\n    sage: M.canonical_relabeling()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[4]>\", line 1, in <module>\n        M.canonical_relabeling()###line 189:\n    sage: M.canonical_relabeling()\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 253:\n    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[2]>\", line 1, in <module>\n        import sage.groups.perm_gps.partn_ref.refinement_matrices###line 253:\n    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices\n    ImportError: No module named refinement_matrices\n**********************************************************************\nFile \"/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py\", line 254:\n    sage: sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_4[3]>\", line 1, in <module>\n        sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests()###line 254:\n    sage: sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests()\n    AttributeError: 'module' object has no attribute 'refinement_matrices'\n**********************************************************************\n5 items had failures:\n   1 of   3 in __main__.example_0\n   9 of  11 in __main__.example_1\n   3 of   5 in __main__.example_2\n   3 of   5 in __main__.example_3\n   2 of   4 in __main__.example_4\n***Test Failed*** 18 failures.\nFor whitespace errors, see the file /home/wdj/sagefiles/sage-3.1.2.rc1/tmp/.doctest_refinement_matrices.py\n         [1.4 s]\nexit code: 1024\n\n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t  devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\nTotal time for all tests: 1.4 seconds\n```\n",
    "created_at": "2008-09-10T12:00:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29503",
    "user": "https://github.com/wdjoyner"
}
```

This failure is on an amd64 gutsy gibbon box (and uses the patch emailed to me by
Robert, which I guess is the same as the one attached to this ticket):


```
wdj@tinah:~/sagefiles/sage-3.1.2.rc1$ ./sage -t  devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
sage -t  devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 5:
    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        import sage.groups.perm_gps.partn_ref.refinement_matrices###line 5:
    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices
    ImportError: No module named refinement_matrices
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 111:
    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct###line 111:
    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
    ImportError: No module named refinement_matrices
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 113:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[3]>", line 1, in <module>
        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)]]))###line 113:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
    NameError: name 'MatrixStruct' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 114:
    sage: M.run()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[4]>", line 1, in <module>
        M.run()###line 114:
    sage: M.run()
    NameError: name 'M' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 115:
    sage: M.automorphism_group()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        M.automorphism_group()###line 115:
    sage: M.automorphism_group()
    NameError: name 'M' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 117:
    sage: M.canonical_relabeling()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        M.canonical_relabeling()###line 117:
    sage: M.canonical_relabeling()
    NameError: name 'M' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 120:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]))
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[7]>", line 1, in <module>
        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)],[Integer(1),Integer(0),Integer(2)],[Integer(1),Integer(2),Integer(0)],[Integer(2),Integer(0),Integer(1)],[Integer(2),Integer(1),Integer(0)]]))###line 120:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1],[1,0,2],[1,2,0],[2,0,1],[2,1,0]]))
    NameError: name 'MatrixStruct' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 121:
    sage: M.automorphism_group()[1] == 6
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[8]>", line 1, in <module>
        M.automorphism_group()[Integer(1)] == Integer(6)###line 121:
    sage: M.automorphism_group()[1] == 6
    NameError: name 'M' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 124:
    sage: M = MatrixStruct(matrix(GF(3),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]]))
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[9]>", line 1, in <module>
        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(0),Integer(1),Integer(2)]]))###line 124:
    sage: M = MatrixStruct(matrix(GF(3),[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2]]))
    NameError: name 'MatrixStruct' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 125:
    sage: M.automorphism_group()[1] == factorial(14)
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[10]>", line 1, in <module>
        M.automorphism_group()[Integer(1)] == factorial(Integer(14))###line 125:
    sage: M.automorphism_group()[1] == factorial(14)
    NameError: name 'M' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 161:
    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct###line 161:
    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
    ImportError: No module named refinement_matrices
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 163:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)]]))###line 163:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
    NameError: name 'MatrixStruct' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 164:
    sage: M.automorphism_group()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[4]>", line 1, in <module>
        M.automorphism_group()###line 164:
    sage: M.automorphism_group()
    NameError: name 'M' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 186:
    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[2]>", line 1, in <module>
        from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct###line 186:
    sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
    ImportError: No module named refinement_matrices
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 188:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[3]>", line 1, in <module>
        M = MatrixStruct(matrix(GF(Integer(3)),[[Integer(0),Integer(1),Integer(2)],[Integer(0),Integer(2),Integer(1)]]))###line 188:
    sage: M = MatrixStruct(matrix(GF(3),[[0,1,2],[0,2,1]]))
    NameError: name 'MatrixStruct' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 189:
    sage: M.canonical_relabeling()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[4]>", line 1, in <module>
        M.canonical_relabeling()###line 189:
    sage: M.canonical_relabeling()
    NameError: name 'M' is not defined
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 253:
    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[2]>", line 1, in <module>
        import sage.groups.perm_gps.partn_ref.refinement_matrices###line 253:
    sage: import sage.groups.perm_gps.partn_ref.refinement_matrices
    ImportError: No module named refinement_matrices
**********************************************************************
File "/home/wdj/sagefiles/sage-3.1.2.rc1/tmp/refinement_matrices.py", line 254:
    sage: sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests()
Exception raised:
    Traceback (most recent call last):
      File "/home/wdj/sagefiles/sage-3.1.2.rc1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_4[3]>", line 1, in <module>
        sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests()###line 254:
    sage: sage.groups.perm_gps.partn_ref.refinement_matrices.random_tests()
    AttributeError: 'module' object has no attribute 'refinement_matrices'
**********************************************************************
5 items had failures:
   1 of   3 in __main__.example_0
   9 of  11 in __main__.example_1
   3 of   5 in __main__.example_2
   3 of   5 in __main__.example_3
   2 of   4 in __main__.example_4
***Test Failed*** 18 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-3.1.2.rc1/tmp/.doctest_refinement_matrices.py
         [1.4 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
Total time for all tests: 1.4 seconds
```




---

archive/issue_comments_029504.json:
```json
{
    "body": "Based on:\n\n> {{{\n>     sage: import sage.groups.perm_gps.partn_ref.refinement_matrices\n>     ImportError: No module named refinement_matrices\n> }}}\n\nIt looks like you might not have built before running tests... If that's not it, definitely try the patch attached to this ticket, and let me know if you still get these errors.",
    "created_at": "2008-09-10T12:03:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29504",
    "user": "https://github.com/rlmill"
}
```

Based on:

> {{{
>     sage: import sage.groups.perm_gps.partn_ref.refinement_matrices
>     ImportError: No module named refinement_matrices
> }}}

It looks like you might not have built before running tests... If that's not it, definitely try the patch attached to this ticket, and let me know if you still get these errors.



---

archive/issue_comments_029505.json:
```json
{
    "body": "You are right. Ignore my last post. After the build, all tests pass. I'll try your code out on examples now....",
    "created_at": "2008-09-10T12:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29505",
    "user": "https://github.com/wdjoyner"
}
```

You are right. Ignore my last post. After the build, all tests pass. I'll try your code out on examples now....



---

archive/issue_comments_029506.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2008-09-12T16:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29506",
    "user": "https://github.com/rlmill"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_029507.json:
```json
{
    "body": "Is this supposed to happen?\n\nUsing the patch at #3943: pydesign patch, we get\n\n\n```\nsage: BD = WittDesign(9)\nsage: BD.automorphism_group()\nPermutation Group with generators [(1,2,3)(4,5,6)(8,9,11)(14,15,20)(16,18,17), (2,3)(4,8)(5,11)(6,9)(13,19)(15,20)(16,18), (1,2)(4,6)(7,10)(9,11)(14,16)(15,17)(18,20), (1,21)(5,8)(6,7)(9,10)(13,14)(15,16)(17,19), (1,4)(2,6)(3,5)(9,11)(12,13)(15,20)(17,18)]\nsage: BD.automorphism_group().order()\n432\nsage: M\n\n[1 1 1 0 0 0 0]\n[1 0 0 1 1 0 0]\n[1 0 0 0 0 1 1]\n[0 1 0 1 0 1 0]\n[0 1 0 0 1 0 1]\n[0 0 1 1 0 0 1]\n[0 0 1 0 1 1 0]\nsage: M.save(\"BD_mat\")\n```\n\nand using the patch at #4097, we get\n\n```\nsage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct\nsage: load(\"/home/wdj/sagefiles/sage-3.1.rc0/BD_mat\")\n\n[1 1 1 0 0 0 0]\n[1 0 0 1 1 0 0]\n[1 0 0 0 0 1 1]\n[0 1 0 1 0 1 0]\n[0 1 0 0 1 0 1]\n[0 0 1 1 0 0 1]\n[0 0 1 0 1 1 0]\nsage: M = load(\"/home/wdj/sagefiles/sage-3.1.rc0/BD_mat\")\nsage: B = NonlinearBinaryCodeStruct(M)\nsage: B.run()\nsage: B.automorphism_group()\n\n([[0, 1, 2, 4, 3, 6, 5],\n  [0, 1, 2, 5, 6, 3, 4],\n  [0, 2, 1, 5, 6, 4, 3],\n  [0, 3, 4, 1, 2, 5, 6],\n  [1, 0, 2, 3, 5, 4, 6]],\n 168,\n [0, 1, 3])\n```\n\nNote 168 does not divide 432 so maybe I am misinterpreting this function or maybe there is a bug somewhere?",
    "created_at": "2008-09-13T21:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29507",
    "user": "https://github.com/wdjoyner"
}
```

Is this supposed to happen?

Using the patch at #3943: pydesign patch, we get


```
sage: BD = WittDesign(9)
sage: BD.automorphism_group()
Permutation Group with generators [(1,2,3)(4,5,6)(8,9,11)(14,15,20)(16,18,17), (2,3)(4,8)(5,11)(6,9)(13,19)(15,20)(16,18), (1,2)(4,6)(7,10)(9,11)(14,16)(15,17)(18,20), (1,21)(5,8)(6,7)(9,10)(13,14)(15,16)(17,19), (1,4)(2,6)(3,5)(9,11)(12,13)(15,20)(17,18)]
sage: BD.automorphism_group().order()
432
sage: M

[1 1 1 0 0 0 0]
[1 0 0 1 1 0 0]
[1 0 0 0 0 1 1]
[0 1 0 1 0 1 0]
[0 1 0 0 1 0 1]
[0 0 1 1 0 0 1]
[0 0 1 0 1 1 0]
sage: M.save("BD_mat")
```

and using the patch at #4097, we get

```
sage: from sage.groups.perm_gps.partn_ref.refinement_binary import NonlinearBinaryCodeStruct
sage: load("/home/wdj/sagefiles/sage-3.1.rc0/BD_mat")

[1 1 1 0 0 0 0]
[1 0 0 1 1 0 0]
[1 0 0 0 0 1 1]
[0 1 0 1 0 1 0]
[0 1 0 0 1 0 1]
[0 0 1 1 0 0 1]
[0 0 1 0 1 1 0]
sage: M = load("/home/wdj/sagefiles/sage-3.1.rc0/BD_mat")
sage: B = NonlinearBinaryCodeStruct(M)
sage: B.run()
sage: B.automorphism_group()

([[0, 1, 2, 4, 3, 6, 5],
  [0, 1, 2, 5, 6, 3, 4],
  [0, 2, 1, 5, 6, 4, 3],
  [0, 3, 4, 1, 2, 5, 6],
  [1, 0, 2, 3, 5, 4, 6]],
 168,
 [0, 1, 3])
```

Note 168 does not divide 432 so maybe I am misinterpreting this function or maybe there is a bug somewhere?



---

archive/issue_comments_029508.json:
```json
{
    "body": "I also get this:\n\n\n```\nsage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct\nsage: M2 = MatrixStruct(M)\nsage: M2.run()\nsage: M2.automorphism_group()\n\n([[0, 1, 2, 4, 3, 6, 5],\n  [0, 1, 2, 5, 6, 3, 4],\n  [0, 2, 1, 5, 6, 4, 3],\n  [0, 3, 4, 1, 2, 5, 6],\n  [1, 0, 2, 3, 5, 4, 6]],\n 168,\n [0, 1, 3])\n```\n\nMaybe this is predictable based on the last comment but thought I'd mention it anyway. Anyway, then I tried comparing it with GAP's matrix automorphism function:\n\n\n```\nsage: GM = M._gap_init_()\nsage: GM\n'[[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[1,0,0,0,0,1,1],[0,1,0,1,0,1,0],[0,1,0,0,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,1,1,0]]*One($sage1)'\nsage: gap.eval(\"MatrixAutomorphisms(%s)\"%GM)\n'Group( [ (4,5)(6,7), (4,6)(5,7), (2,3)(6,7), (2,4)(3,5), (1,2)(5,6) ] )'\nsage: gap.eval(\"Size(MatrixAutomorphisms(%s))\"%GM)\n'168'\n```\n\nThis proves I think you are write and that the bug must lie in the pydesign code.\n\nSorry for the wasted bandwidth on this! I'll keep testing.",
    "created_at": "2008-09-14T01:15:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29508",
    "user": "https://github.com/wdjoyner"
}
```

I also get this:


```
sage: from sage.groups.perm_gps.partn_ref.refinement_matrices import MatrixStruct
sage: M2 = MatrixStruct(M)
sage: M2.run()
sage: M2.automorphism_group()

([[0, 1, 2, 4, 3, 6, 5],
  [0, 1, 2, 5, 6, 3, 4],
  [0, 2, 1, 5, 6, 4, 3],
  [0, 3, 4, 1, 2, 5, 6],
  [1, 0, 2, 3, 5, 4, 6]],
 168,
 [0, 1, 3])
```

Maybe this is predictable based on the last comment but thought I'd mention it anyway. Anyway, then I tried comparing it with GAP's matrix automorphism function:


```
sage: GM = M._gap_init_()
sage: GM
'[[1,1,1,0,0,0,0],[1,0,0,1,1,0,0],[1,0,0,0,0,1,1],[0,1,0,1,0,1,0],[0,1,0,0,1,0,1],[0,0,1,1,0,0,1],[0,0,1,0,1,1,0]]*One($sage1)'
sage: gap.eval("MatrixAutomorphisms(%s)"%GM)
'Group( [ (4,5)(6,7), (4,6)(5,7), (2,3)(6,7), (2,4)(3,5), (1,2)(5,6) ] )'
sage: gap.eval("Size(MatrixAutomorphisms(%s))"%GM)
'168'
```

This proves I think you are write and that the bug must lie in the pydesign code.

Sorry for the wasted bandwidth on this! I'll keep testing.



---

archive/issue_comments_029509.json:
```json
{
    "body": "It turns out there is no bug at all anywhere, I made a typing mistake.\n\nOkay. Here is a really cool example which will make up for the whole thing:-) The Witt block design of index 12 has the Mathieu group M_12 as the automorphism group:\n\n\n```\nsage: BD = WittDesign(12)\nsage: BD.automorphism_group().order()\n95040\nsage: M = BD.incidence_matrix()\nsage: M\n12 x 132 dense matrix over Integer Ring\nsage: M.save(\"BD_mat\")\nsage: MathieuGroup(12).order()\n95040\nsage: G = BD.automorphism_group()\nsage: G.is_isomorphic(MathieuGroup(12))\nTrue\n```\n\nNow move over to the patch at #4097:\n\n\n```\nsage: M = load(\"/home/wdj/sagefiles/sage-3.1.rc0/BD_mat\")\nsage: M2 = MatrixStruct(M)\nsage: M2.run()\nsage: print M2.automorphism_group()\n([[0, 1, 3, 2, 7, 10, 9, 4, 8, 6, 5, 11, 33, 36, 35, 30, 34, 31, 32, 37, 38, 43, 41, 40, 46, 39, 45, 44, 42, 47, 15, 17, 18, 12, 16, 14, 13, 19, 20, 25, 23, 22, 28, 21, 27, 26, 24, 29, 48, 53, 51, 50, 56, 49, 54, 55, 52, 57, 58, 63, 64, 61, 65, 59, 60, 62, 69, 71, 72, 66, 70, 67, 68, 73, 74, 79, 76, 77, 82, 75, 81, 80, 78, 83, 102, 107, 105, 104, 110, 103, 109, 108, 106, 111, 112, 118, 117, 115, 119, 113, 114, 116, 84, 89, 87, 86, 92, 85, 91, 90, 88, 93, 94, 99, 100, 97, 101, 96, 95, 98, 120, 126, 125, 123, 127, 122, 121, 124, 129, 128, 130, 131], [0, 5, 6, 4, 9, 10, 7, 2, 8, 3, 1, 11, 20, 23, 22, 13, 24, 12, 14, 21, 17, 28, 18, 15, 25, 16, 29, 26, 19, 27, 40, 38, 41, 31, 39, 32, 30, 42, 33, 46, 36, 35, 43, 37, 47, 44, 34, 45, 50, 61, 51, 48, 58, 49, 59, 62, 52, 60, 56, 63, 64, 53, 65, 54, 57, 55, 76, 74, 77, 66, 78, 67, 68, 75, 71, 79, 69, 72, 82, 73, 83, 80, 70, 81, 86, 97, 87, 84, 94, 88, 96, 95, 85, 98, 89, 101, 99, 92, 100, 90, 93, 91, 104, 112, 105, 102, 115, 106, 116, 113, 103, 114, 110, 117, 119, 107, 118, 109, 108, 111, 120, 130, 128, 123, 129, 124, 121, 122, 127, 125, 126, 131], [0, 2, 1, 3, 9, 7, 10, 5, 8, 4, 6, 11, 17, 15, 18, 13, 16, 12, 14, 19, 20, 28, 22, 23, 25, 24, 26, 29, 21, 27, 71, 69, 72, 66, 73, 68, 67, 70, 76, 79, 74, 77, 82, 78, 80, 83, 75, 81, 86, 89, 84, 87, 92, 88, 90, 93, 85, 91, 97, 99, 101, 94, 100, 96, 95, 98, 33, 36, 35, 31, 37, 30, 32, 34, 40, 46, 38, 41, 43, 39, 44, 47, 42, 45, 50, 56, 48, 51, 53, 49, 54, 57, 52, 55, 61, 64, 63, 58, 65, 59, 62, 60, 104, 110, 102, 105, 107, 106, 108, 109, 103, 111, 112, 117, 119, 115, 118, 113, 116, 114, 120, 125, 127, 123, 126, 121, 124, 122, 128, 130, 129, 131], [0, 1, 2, 3, 9, 10, 7, 6, 11, 4, 5, 8, 18, 15, 17, 13, 19, 14, 12, 16, 22, 25, 20, 23, 28, 21, 26, 29, 24, 27, 36, 35, 33, 32, 37, 31, 30, 34, 41, 43, 40, 38, 46, 39, 47, 45, 42, 44, 48, 56, 51, 50, 53, 52, 55, 54, 49, 57, 61, 65, 64, 58, 63, 62, 60, 59, 72, 71, 69, 68, 73, 67, 66, 70, 74, 82, 77, 76, 79, 78, 81, 80, 75, 83, 87, 89, 86, 84, 92, 85, 93, 91, 88, 90, 97, 101, 100, 94, 99, 98, 96, 95, 104, 107, 102, 105, 110, 103, 108, 111, 106, 109, 115, 119, 117, 112, 118, 114, 116, 113, 123, 126, 127, 120, 125, 124, 121, 122, 128, 129, 130, 131], [0, 2, 1, 3, 13, 12, 14, 17, 16, 15, 18, 19, 5, 4, 6, 9, 8, 7, 10, 11, 20, 24, 22, 23, 21, 28, 26, 29, 25, 27, 31, 30, 32, 33, 37, 36, 35, 34, 50, 49, 48, 51, 52, 56, 54, 57, 53, 55, 40, 39, 38, 41, 42, 46, 44, 47, 43, 45, 61, 59, 62, 58, 60, 64, 63, 65, 66, 68, 67, 71, 73, 69, 72, 70, 86, 88, 84, 87, 85, 89, 90, 93, 92, 91, 76, 78, 74, 77, 75, 79, 80, 83, 82, 81, 97, 96, 95, 94, 98, 99, 101, 100, 104, 106, 102, 105, 103, 110, 108, 109, 107, 111, 120, 121, 124, 123, 122, 125, 127, 126, 112, 113, 116, 115, 114, 117, 119, 118, 128, 130, 129, 131], [1, 0, 3, 2, 6, 11, 9, 4, 5, 7, 8, 10, 13, 18, 19, 12, 14, 16, 15, 17, 21, 22, 25, 26, 29, 20, 23, 24, 27, 28, 32, 37, 36, 30, 31, 34, 33, 35, 39, 41, 45, 43, 47, 38, 42, 40, 44, 46, 48, 52, 55, 54, 56, 49, 50, 51, 53, 57, 60, 62, 61, 64, 65, 59, 58, 63, 68, 73, 72, 66, 67, 70, 69, 71, 74, 78, 80, 81, 82, 75, 77, 76, 79, 83, 85, 87, 91, 89, 93, 84, 88, 86, 90, 92, 96, 98, 97, 100, 101, 95, 94, 99, 103, 104, 107, 108, 111, 102, 105, 106, 109, 110, 114, 116, 115, 117, 119, 112, 113, 118, 121, 123, 124, 126, 127, 122, 120, 125, 129, 128, 131, 130]], 95040, [0, 8, 55, 98])\n```\n\nHopefully trac will print the order 95040 at the end.\n\nI think this code works:-)\n\nAs far as I am concerned, this passes but I don't know enough Cython to read over the code to check for memory problems for example.\n\nGreat job Robert and Thanks!",
    "created_at": "2008-09-14T01:26:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29509",
    "user": "https://github.com/wdjoyner"
}
```

It turns out there is no bug at all anywhere, I made a typing mistake.

Okay. Here is a really cool example which will make up for the whole thing:-) The Witt block design of index 12 has the Mathieu group M_12 as the automorphism group:


```
sage: BD = WittDesign(12)
sage: BD.automorphism_group().order()
95040
sage: M = BD.incidence_matrix()
sage: M
12 x 132 dense matrix over Integer Ring
sage: M.save("BD_mat")
sage: MathieuGroup(12).order()
95040
sage: G = BD.automorphism_group()
sage: G.is_isomorphic(MathieuGroup(12))
True
```

Now move over to the patch at #4097:


```
sage: M = load("/home/wdj/sagefiles/sage-3.1.rc0/BD_mat")
sage: M2 = MatrixStruct(M)
sage: M2.run()
sage: print M2.automorphism_group()
([[0, 1, 3, 2, 7, 10, 9, 4, 8, 6, 5, 11, 33, 36, 35, 30, 34, 31, 32, 37, 38, 43, 41, 40, 46, 39, 45, 44, 42, 47, 15, 17, 18, 12, 16, 14, 13, 19, 20, 25, 23, 22, 28, 21, 27, 26, 24, 29, 48, 53, 51, 50, 56, 49, 54, 55, 52, 57, 58, 63, 64, 61, 65, 59, 60, 62, 69, 71, 72, 66, 70, 67, 68, 73, 74, 79, 76, 77, 82, 75, 81, 80, 78, 83, 102, 107, 105, 104, 110, 103, 109, 108, 106, 111, 112, 118, 117, 115, 119, 113, 114, 116, 84, 89, 87, 86, 92, 85, 91, 90, 88, 93, 94, 99, 100, 97, 101, 96, 95, 98, 120, 126, 125, 123, 127, 122, 121, 124, 129, 128, 130, 131], [0, 5, 6, 4, 9, 10, 7, 2, 8, 3, 1, 11, 20, 23, 22, 13, 24, 12, 14, 21, 17, 28, 18, 15, 25, 16, 29, 26, 19, 27, 40, 38, 41, 31, 39, 32, 30, 42, 33, 46, 36, 35, 43, 37, 47, 44, 34, 45, 50, 61, 51, 48, 58, 49, 59, 62, 52, 60, 56, 63, 64, 53, 65, 54, 57, 55, 76, 74, 77, 66, 78, 67, 68, 75, 71, 79, 69, 72, 82, 73, 83, 80, 70, 81, 86, 97, 87, 84, 94, 88, 96, 95, 85, 98, 89, 101, 99, 92, 100, 90, 93, 91, 104, 112, 105, 102, 115, 106, 116, 113, 103, 114, 110, 117, 119, 107, 118, 109, 108, 111, 120, 130, 128, 123, 129, 124, 121, 122, 127, 125, 126, 131], [0, 2, 1, 3, 9, 7, 10, 5, 8, 4, 6, 11, 17, 15, 18, 13, 16, 12, 14, 19, 20, 28, 22, 23, 25, 24, 26, 29, 21, 27, 71, 69, 72, 66, 73, 68, 67, 70, 76, 79, 74, 77, 82, 78, 80, 83, 75, 81, 86, 89, 84, 87, 92, 88, 90, 93, 85, 91, 97, 99, 101, 94, 100, 96, 95, 98, 33, 36, 35, 31, 37, 30, 32, 34, 40, 46, 38, 41, 43, 39, 44, 47, 42, 45, 50, 56, 48, 51, 53, 49, 54, 57, 52, 55, 61, 64, 63, 58, 65, 59, 62, 60, 104, 110, 102, 105, 107, 106, 108, 109, 103, 111, 112, 117, 119, 115, 118, 113, 116, 114, 120, 125, 127, 123, 126, 121, 124, 122, 128, 130, 129, 131], [0, 1, 2, 3, 9, 10, 7, 6, 11, 4, 5, 8, 18, 15, 17, 13, 19, 14, 12, 16, 22, 25, 20, 23, 28, 21, 26, 29, 24, 27, 36, 35, 33, 32, 37, 31, 30, 34, 41, 43, 40, 38, 46, 39, 47, 45, 42, 44, 48, 56, 51, 50, 53, 52, 55, 54, 49, 57, 61, 65, 64, 58, 63, 62, 60, 59, 72, 71, 69, 68, 73, 67, 66, 70, 74, 82, 77, 76, 79, 78, 81, 80, 75, 83, 87, 89, 86, 84, 92, 85, 93, 91, 88, 90, 97, 101, 100, 94, 99, 98, 96, 95, 104, 107, 102, 105, 110, 103, 108, 111, 106, 109, 115, 119, 117, 112, 118, 114, 116, 113, 123, 126, 127, 120, 125, 124, 121, 122, 128, 129, 130, 131], [0, 2, 1, 3, 13, 12, 14, 17, 16, 15, 18, 19, 5, 4, 6, 9, 8, 7, 10, 11, 20, 24, 22, 23, 21, 28, 26, 29, 25, 27, 31, 30, 32, 33, 37, 36, 35, 34, 50, 49, 48, 51, 52, 56, 54, 57, 53, 55, 40, 39, 38, 41, 42, 46, 44, 47, 43, 45, 61, 59, 62, 58, 60, 64, 63, 65, 66, 68, 67, 71, 73, 69, 72, 70, 86, 88, 84, 87, 85, 89, 90, 93, 92, 91, 76, 78, 74, 77, 75, 79, 80, 83, 82, 81, 97, 96, 95, 94, 98, 99, 101, 100, 104, 106, 102, 105, 103, 110, 108, 109, 107, 111, 120, 121, 124, 123, 122, 125, 127, 126, 112, 113, 116, 115, 114, 117, 119, 118, 128, 130, 129, 131], [1, 0, 3, 2, 6, 11, 9, 4, 5, 7, 8, 10, 13, 18, 19, 12, 14, 16, 15, 17, 21, 22, 25, 26, 29, 20, 23, 24, 27, 28, 32, 37, 36, 30, 31, 34, 33, 35, 39, 41, 45, 43, 47, 38, 42, 40, 44, 46, 48, 52, 55, 54, 56, 49, 50, 51, 53, 57, 60, 62, 61, 64, 65, 59, 58, 63, 68, 73, 72, 66, 67, 70, 69, 71, 74, 78, 80, 81, 82, 75, 77, 76, 79, 83, 85, 87, 91, 89, 93, 84, 88, 86, 90, 92, 96, 98, 97, 100, 101, 95, 94, 99, 103, 104, 107, 108, 111, 102, 105, 106, 109, 110, 114, 116, 115, 117, 119, 112, 113, 118, 121, 123, 124, 126, 127, 122, 120, 125, 129, 128, 131, 130]], 95040, [0, 8, 55, 98])
```

Hopefully trac will print the order 95040 at the end.

I think this code works:-)

As far as I am concerned, this passes but I don't know enough Cython to read over the code to check for memory problems for example.

Great job Robert and Thanks!



---

archive/issue_comments_029510.json:
```json
{
    "body": "David,\n\nif you consider this code working (as indicated by the last ticket) please give this a positive review. I will check for memory leaks (Robert did tell me that he did valgrind the doctest in question and did not find any leaks), so that way the patch can be merged soon.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-14T02:06:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29510",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

David,

if you consider this code working (as indicated by the last ticket) please give this a positive review. I will check for memory leaks (Robert did tell me that he did valgrind the doctest in question and did not find any leaks), so that way the patch can be merged soon.

Cheers,

Michael



---

archive/issue_comments_029511.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-15T01:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29511",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_029512.json:
```json
{
    "body": "Merged in Sage 3.1.2.rc4",
    "created_at": "2008-09-15T01:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4097",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4097#issuecomment-29512",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.1.2.rc4
