# Issue 9617: Broken export of LP files....

archive/issues_009617.json:
```json
{
    "body": "Assignee: jason, jkantor\n\nCC:  @nexttime @jhpalmieri\n\nThis error has been noticed throuugh #9584\n\nAfter taking a look at the corresponding part of the code, *OF COURSE* something needed to be changedm but to be honest I have no inkling why Sage did not report this as an error : I was adding str(k) in a string while k.... was not defined ? O_o\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/9617\n\n",
    "created_at": "2010-07-28T03:08:01Z",
    "labels": [
        "numerical",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Broken export of LP files....",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9617",
    "user": "@nathanncohen"
}
```
Assignee: jason, jkantor

CC:  @nexttime @jhpalmieri

This error has been noticed throuugh #9584

After taking a look at the corresponding part of the code, *OF COURSE* something needed to be changedm but to be honest I have no inkling why Sage did not report this as an error : I was adding str(k) in a string while k.... was not defined ? O_o

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/9617





---

archive/issue_comments_093150.json:
```json
{
    "body": "Attachment [trac_9617.patch](tarball://root/attachments/some-uuid/ticket9617/trac_9617.patch) by @nathanncohen created at 2010-07-28 03:09:26",
    "created_at": "2010-07-28T03:09:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93150",
    "user": "@nathanncohen"
}
```

Attachment [trac_9617.patch](tarball://root/attachments/some-uuid/ticket9617/trac_9617.patch) by @nathanncohen created at 2010-07-28 03:09:26



---

archive/issue_comments_093151.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T03:09:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93151",
    "user": "@nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093152.json:
```json
{
    "body": "Changing keywords from \"\" to \"CPLEX, GLPK, glpsol, MPS, file\".",
    "created_at": "2010-07-28T03:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93152",
    "user": "@nexttime"
}
```

Changing keywords from "" to "CPLEX, GLPK, glpsol, MPS, file".



---

archive/issue_comments_093153.json:
```json
{
    "body": "Thanks for (hopefully) fixing this; I won't be able to test/review this until tomorrow though. (But then will try to track down the non-terminating doctest from #9584 further.)\n\n-Leif",
    "created_at": "2010-07-28T03:52:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93153",
    "user": "@nexttime"
}
```

Thanks for (hopefully) fixing this; I won't be able to test/review this until tomorrow though. (But then will try to track down the non-terminating doctest from #9584 further.)

-Leif



---

archive/issue_comments_093154.json:
```json
{
    "body": "The good news: Your patch here seems to work fine.\n\nThe bad news: I've again exported (now valid) MPS and LP files for the `edge_disjoint_spanning_trees()` example with 30 vertices and run `glpsol` on those files on both a 64-bit machine and on the 32-bit machine (P4 Prescott) where that example did not terminate. The logs are slightly different, but *both terminate*:\n\n```\nGLPSOL: GLPK LP/MIP Solver, v4.44\nParameter(s) specified in the command line:\n --freemps edst-30_vertices.mps\nReading problem data from `edst-30_vertices.mps'...\nedst-30_vertices.mps:8: warning: missing model name in field 3\nObjective: R0000000\n1720 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\n8412 records were read\nGLPK Integer Optimizer, v4.44\n1720 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\nPreprocessing...\n1670 rows, 3605 columns, 9790 non-zeros\n1325 integer variables, all of which are binary\nScaling...\n A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00\nProblem data seem to be well scaled\nConstructing initial basis...\nSize of triangular part = 1670\nSolving LP relaxation...\nGLPK Simplex Optimizer, v4.44\n1670 rows, 3605 columns, 9790 non-zeros\n      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)\n   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)\n*  1589: obj =   0.000000000e+00  infeas =  2.132e-14 (0)\nOPTIMAL SOLUTION FOUND\nInteger optimization begins...\n+  1589: mip =     not found yet >=              -inf        (1; 0)\n+  4531: mip =     not found yet >=   0.000000000e+00        (26; 0)\n+  8462: mip =     not found yet >=   0.000000000e+00        (62; 0)\n+ 14689: mip =     not found yet >=   0.000000000e+00        (106; 0)\n+ 28430: >>>>>   0.000000000e+00 >=   0.000000000e+00   0.0% (223; 3)\n+ 28430: mip =   0.000000000e+00 >=     tree is empty   0.0% (0; 451)\nINTEGER OPTIMAL SOLUTION FOUND\nTime used:   19.1 secs\nMemory used: 5.6 Mb (5848196 bytes)\n```\n\n(64-bit machine, time due to high sysload)\n\n\n```\nGLPSOL: GLPK LP/MIP Solver, v4.44\nParameter(s) specified in the command line:\n --freemps /home/leif/Sage/new-mps-lp/edst-30_vertices.mps\nReading problem data from `/home/leif/Sage/new-mps-lp/edst-30_vertices.mps'...\n/home/leif/Sage/new-mps-lp/edst-30_vertices.mps:8: warning: missing model name in field 3\nObjective: R0000000\n1720 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\n8412 records were read\nGLPK Integer Optimizer, v4.44\n1720 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\nPreprocessing...\n1670 rows, 3605 columns, 9790 non-zeros\n1325 integer variables, all of which are binary\nScaling...\n A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00\nProblem data seem to be well scaled\nConstructing initial basis...\nSize of triangular part = 1670\nSolving LP relaxation...\nGLPK Simplex Optimizer, v4.44\n1670 rows, 3605 columns, 9790 non-zeros\n      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)\n   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)\n*  1589: obj =   0.000000000e+00  infeas =  2.132e-14 (0)\nOPTIMAL SOLUTION FOUND\nInteger optimization begins...\n+  1589: mip =     not found yet >=              -inf        (1; 0)\n+  3426: mip =     not found yet >=   0.000000000e+00        (10; 0)\n+  4687: mip =     not found yet >=   0.000000000e+00        (21; 0)\n+  5604: mip =     not found yet >=   0.000000000e+00        (32; 0)\n+  6640: mip =     not found yet >=   0.000000000e+00        (44; 0)\n+  7802: mip =     not found yet >=   0.000000000e+00        (58; 0)\n+  9123: mip =     not found yet >=   0.000000000e+00        (72; 0)\n+ 11067: mip =     not found yet >=   0.000000000e+00        (86; 0)\n+ 13203: mip =     not found yet >=   0.000000000e+00        (101; 0)\n+ 15411: mip =     not found yet >=   0.000000000e+00        (117; 1)\n+ 18254: mip =     not found yet >=   0.000000000e+00        (135; 1)\n+ 21870: mip =     not found yet >=   0.000000000e+00        (156; 1)\nTime used: 60.1 secs.  Memory used: 3.8 Mb.\n+ 26285: mip =     not found yet >=   0.000000000e+00        (186; 4)\n+ 29923: >>>>>   0.000000000e+00 >=   0.000000000e+00   0.0% (253; 15)\n+ 29923: mip =   0.000000000e+00 >=     tree is empty   0.0% (0; 535)\nINTEGER OPTIMAL SOLUTION FOUND\nTime used:   67.4 secs\nMemory used: 4.9 Mb (5146500 bytes)\n```\n\n(32-bit machine/Pentium 4 Prescott)\n\nThat means the bug causing the non-termination sits somewhere in the Sage library interface to GLPK.\n\nAll files were generated on the 64-bit machine; I've not yet tried to generate them on the 32-bit machine (they might differ, so I'll check that later).\n\n(The LP/MPS files of that example are too big to upload them here, approx. 260KB.)",
    "created_at": "2010-07-30T00:38:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93154",
    "user": "@nexttime"
}
```

The good news: Your patch here seems to work fine.

The bad news: I've again exported (now valid) MPS and LP files for the `edge_disjoint_spanning_trees()` example with 30 vertices and run `glpsol` on those files on both a 64-bit machine and on the 32-bit machine (P4 Prescott) where that example did not terminate. The logs are slightly different, but *both terminate*:

```
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --freemps edst-30_vertices.mps
Reading problem data from `edst-30_vertices.mps'...
edst-30_vertices.mps:8: warning: missing model name in field 3
Objective: R0000000
1720 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
8412 records were read
GLPK Integer Optimizer, v4.44
1720 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
Preprocessing...
1670 rows, 3605 columns, 9790 non-zeros
1325 integer variables, all of which are binary
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 1670
Solving LP relaxation...
GLPK Simplex Optimizer, v4.44
1670 rows, 3605 columns, 9790 non-zeros
      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)
   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)
*  1589: obj =   0.000000000e+00  infeas =  2.132e-14 (0)
OPTIMAL SOLUTION FOUND
Integer optimization begins...
+  1589: mip =     not found yet >=              -inf        (1; 0)
+  4531: mip =     not found yet >=   0.000000000e+00        (26; 0)
+  8462: mip =     not found yet >=   0.000000000e+00        (62; 0)
+ 14689: mip =     not found yet >=   0.000000000e+00        (106; 0)
+ 28430: >>>>>   0.000000000e+00 >=   0.000000000e+00   0.0% (223; 3)
+ 28430: mip =   0.000000000e+00 >=     tree is empty   0.0% (0; 451)
INTEGER OPTIMAL SOLUTION FOUND
Time used:   19.1 secs
Memory used: 5.6 Mb (5848196 bytes)
```

(64-bit machine, time due to high sysload)


```
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --freemps /home/leif/Sage/new-mps-lp/edst-30_vertices.mps
Reading problem data from `/home/leif/Sage/new-mps-lp/edst-30_vertices.mps'...
/home/leif/Sage/new-mps-lp/edst-30_vertices.mps:8: warning: missing model name in field 3
Objective: R0000000
1720 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
8412 records were read
GLPK Integer Optimizer, v4.44
1720 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
Preprocessing...
1670 rows, 3605 columns, 9790 non-zeros
1325 integer variables, all of which are binary
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 1670
Solving LP relaxation...
GLPK Simplex Optimizer, v4.44
1670 rows, 3605 columns, 9790 non-zeros
      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)
   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)
*  1589: obj =   0.000000000e+00  infeas =  2.132e-14 (0)
OPTIMAL SOLUTION FOUND
Integer optimization begins...
+  1589: mip =     not found yet >=              -inf        (1; 0)
+  3426: mip =     not found yet >=   0.000000000e+00        (10; 0)
+  4687: mip =     not found yet >=   0.000000000e+00        (21; 0)
+  5604: mip =     not found yet >=   0.000000000e+00        (32; 0)
+  6640: mip =     not found yet >=   0.000000000e+00        (44; 0)
+  7802: mip =     not found yet >=   0.000000000e+00        (58; 0)
+  9123: mip =     not found yet >=   0.000000000e+00        (72; 0)
+ 11067: mip =     not found yet >=   0.000000000e+00        (86; 0)
+ 13203: mip =     not found yet >=   0.000000000e+00        (101; 0)
+ 15411: mip =     not found yet >=   0.000000000e+00        (117; 1)
+ 18254: mip =     not found yet >=   0.000000000e+00        (135; 1)
+ 21870: mip =     not found yet >=   0.000000000e+00        (156; 1)
Time used: 60.1 secs.  Memory used: 3.8 Mb.
+ 26285: mip =     not found yet >=   0.000000000e+00        (186; 4)
+ 29923: >>>>>   0.000000000e+00 >=   0.000000000e+00   0.0% (253; 15)
+ 29923: mip =   0.000000000e+00 >=     tree is empty   0.0% (0; 535)
INTEGER OPTIMAL SOLUTION FOUND
Time used:   67.4 secs
Memory used: 4.9 Mb (5146500 bytes)
```

(32-bit machine/Pentium 4 Prescott)

That means the bug causing the non-termination sits somewhere in the Sage library interface to GLPK.

All files were generated on the 64-bit machine; I've not yet tried to generate them on the 32-bit machine (they might differ, so I'll check that later).

(The LP/MPS files of that example are too big to upload them here, approx. 260KB.)



---

archive/issue_comments_093155.json:
```json
{
    "body": "Weird O_o\n\nShort of these names, there is really no difference between the code used to produce the file and the one building the data structure for GLPK. Did you use the very Random Graph which produced timeouts before, or generated a different one ?\n\nNathann",
    "created_at": "2010-07-30T01:57:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93155",
    "user": "@nathanncohen"
}
```

Weird O_o

Short of these names, there is really no difference between the code used to produce the file and the one building the data structure for GLPK. Did you use the very Random Graph which produced timeouts before, or generated a different one ?

Nathann



---

archive/issue_comments_093156.json:
```json
{
    "body": "By the way, why do you think the non-termination is a bug ?\n\nIt just takes ages to solve, that's all... Sometimes the solver use non-deterministic methods, or detect a good cut for some reason... It would be weird to find out that the same problem always takes ages to solve through Sage, and is quickly done with through files, but other than this a LP which takes ages to be solved happens quite often.\n\nFor example the pretty pictures displayed there :\n\nhttp://www-sop.inria.fr/members/Nathann.Cohen/acyclicedgecoloring/\n\nstop at step 10. The reason is that the LP I wrote for 12 was still running after 4 days.\n\nNathann",
    "created_at": "2010-07-30T02:02:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93156",
    "user": "@nathanncohen"
}
```

By the way, why do you think the non-termination is a bug ?

It just takes ages to solve, that's all... Sometimes the solver use non-deterministic methods, or detect a good cut for some reason... It would be weird to find out that the same problem always takes ages to solve through Sage, and is quickly done with through files, but other than this a LP which takes ages to be solved happens quite often.

For example the pretty pictures displayed there :

http://www-sop.inria.fr/members/Nathann.Cohen/acyclicedgecoloring/

stop at step 10. The reason is that the LP I wrote for 12 was still running after 4 days.

Nathann



---

archive/issue_comments_093157.json:
```json
{
    "body": "Replying to [comment:4 ncohen]:\n> Weird O_o\n> \n> Short of these names, there is really no difference between the code used to produce the file and the one building the data structure for GLPK.\n\nYes, except for the variable and constraint names, which is why I believe something goes wrong in constructing the problem on the 32-bit machine (and this should be observable through differences in the generated files).\n\n> Did you use the very Random Graph which produced timeouts before, or generated a different one ?\n\nI did generate files for all examples, the logs above are from exactly the 30-vertices random graph one. (I made sure they are the same on both machines by adding some more doctests).",
    "created_at": "2010-07-30T02:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93157",
    "user": "@nexttime"
}
```

Replying to [comment:4 ncohen]:
> Weird O_o
> 
> Short of these names, there is really no difference between the code used to produce the file and the one building the data structure for GLPK.

Yes, except for the variable and constraint names, which is why I believe something goes wrong in constructing the problem on the 32-bit machine (and this should be observable through differences in the generated files).

> Did you use the very Random Graph which produced timeouts before, or generated a different one ?

I did generate files for all examples, the logs above are from exactly the 30-vertices random graph one. (I made sure they are the same on both machines by adding some more doctests).



---

archive/issue_comments_093158.json:
```json
{
    "body": "Hello !!!\n\nBy carefully looking at the two logs, the one you just gave and the one given by John on #9584, I noticed a difference, even though all the number of entries, lines/etc were the same. Yours \n\n```\n+  1589: mip =     not found yet >=              -inf        (1; 0)\n```\n\nHis\n\n```\n+  1589: mip =     not found yet <=              +inf        (1; 0)\n```\n\n\nAnd all the following inequalities are reversed... Well, it sounds like you are working on a minimization problem, while John his working on a maximization problem. That's when I remembered a problem I had had with GLPK a long time ago when using it through the command-line (but perhaps it was CPLEX or CBC, I do not remember). At least one of them was completely ignoring the direction of the optimization given in the file, and only behaved nicely when given the good flag... Could you give it a try with one of those ?\n\n\n```\n       --min  minimization\n       --max  maximization\n```\n\n\nI am really sorry but I can not do it myself, I am travelling these days and unable to find any place where I could use my own computer ^^;\n\nNathann",
    "created_at": "2010-07-30T02:56:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93158",
    "user": "@nathanncohen"
}
```

Hello !!!

By carefully looking at the two logs, the one you just gave and the one given by John on #9584, I noticed a difference, even though all the number of entries, lines/etc were the same. Yours 

```
+  1589: mip =     not found yet >=              -inf        (1; 0)
```

His

```
+  1589: mip =     not found yet <=              +inf        (1; 0)
```


And all the following inequalities are reversed... Well, it sounds like you are working on a minimization problem, while John his working on a maximization problem. That's when I remembered a problem I had had with GLPK a long time ago when using it through the command-line (but perhaps it was CPLEX or CBC, I do not remember). At least one of them was completely ignoring the direction of the optimization given in the file, and only behaved nicely when given the good flag... Could you give it a try with one of those ?


```
       --min  minimization
       --max  maximization
```


I am really sorry but I can not do it myself, I am travelling these days and unable to find any place where I could use my own computer ^^;

Nathann



---

archive/issue_comments_093159.json:
```json
{
    "body": "This is really funny. I've now exported the MPS file on the 32-bit machine, too.\n\nWhile the doctest itself did not terminate (at least not within reasonable time, so I manually killed the orphan process after the time-out), running `glpsol` on the exported (in theory identical) problem succeeds rather quickly:\n\n```\nGLPSOL: GLPK LP/MIP Solver, v4.44\nParameter(s) specified in the command line:\n --freemps edst-30_vertices.x86.mps\nReading problem data from `edst-30_vertices.x86.mps'...\nedst-30_vertices.x86.mps:8: warning: missing model name in field 3\nObjective: R0000000\n1720 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\n8412 records were read\nGLPK Integer Optimizer, v4.44\n1720 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\nPreprocessing...\n1670 rows, 3605 columns, 9790 non-zeros\n1325 integer variables, all of which are binary\nScaling...\n A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00\nProblem data seem to be well scaled\nConstructing initial basis...\nSize of triangular part = 1670\nSolving LP relaxation...\nGLPK Simplex Optimizer, v4.44\n1670 rows, 3605 columns, 9790 non-zeros\n      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)\n   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)\n*  1589: obj =   0.000000000e+00  infeas =  2.132e-14 (0)\nOPTIMAL SOLUTION FOUND\nInteger optimization begins...\n+  1589: mip =     not found yet >=              -inf        (1; 0)\n+  3426: mip =     not found yet >=   0.000000000e+00        (10; 0)\n+  4687: mip =     not found yet >=   0.000000000e+00        (21; 0)\n+  5604: mip =     not found yet >=   0.000000000e+00        (32; 0)\n+  6640: mip =     not found yet >=   0.000000000e+00        (44; 0)\n+  7802: mip =     not found yet >=   0.000000000e+00        (58; 0)\n+  9123: mip =     not found yet >=   0.000000000e+00        (72; 0)\n+ 11067: mip =     not found yet >=   0.000000000e+00        (86; 0)\n+ 13203: mip =     not found yet >=   0.000000000e+00        (101; 0)\n+ 15411: mip =     not found yet >=   0.000000000e+00        (117; 1)\n+ 18105: mip =     not found yet >=   0.000000000e+00        (134; 1)\n+ 21758: mip =     not found yet >=   0.000000000e+00        (154; 1)\nTime used: 60.1 secs.  Memory used: 3.8 Mb.\n+ 26154: mip =     not found yet >=   0.000000000e+00        (183; 4)\n+ 29923: >>>>>   0.000000000e+00 >=   0.000000000e+00   0.0% (253; 15)\n+ 29923: mip =   0.000000000e+00 >=     tree is empty   0.0% (0; 535)\nINTEGER OPTIMAL SOLUTION FOUND\nTime used:   67.6 secs\nMemory used: 4.9 Mb (5146500 bytes)\n```\n\n(This is again \"inverted\".)",
    "created_at": "2010-07-30T04:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93159",
    "user": "@nexttime"
}
```

This is really funny. I've now exported the MPS file on the 32-bit machine, too.

While the doctest itself did not terminate (at least not within reasonable time, so I manually killed the orphan process after the time-out), running `glpsol` on the exported (in theory identical) problem succeeds rather quickly:

```
GLPSOL: GLPK LP/MIP Solver, v4.44
Parameter(s) specified in the command line:
 --freemps edst-30_vertices.x86.mps
Reading problem data from `edst-30_vertices.x86.mps'...
edst-30_vertices.x86.mps:8: warning: missing model name in field 3
Objective: R0000000
1720 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
8412 records were read
GLPK Integer Optimizer, v4.44
1720 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
Preprocessing...
1670 rows, 3605 columns, 9790 non-zeros
1325 integer variables, all of which are binary
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 1670
Solving LP relaxation...
GLPK Simplex Optimizer, v4.44
1670 rows, 3605 columns, 9790 non-zeros
      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)
   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)
*  1589: obj =   0.000000000e+00  infeas =  2.132e-14 (0)
OPTIMAL SOLUTION FOUND
Integer optimization begins...
+  1589: mip =     not found yet >=              -inf        (1; 0)
+  3426: mip =     not found yet >=   0.000000000e+00        (10; 0)
+  4687: mip =     not found yet >=   0.000000000e+00        (21; 0)
+  5604: mip =     not found yet >=   0.000000000e+00        (32; 0)
+  6640: mip =     not found yet >=   0.000000000e+00        (44; 0)
+  7802: mip =     not found yet >=   0.000000000e+00        (58; 0)
+  9123: mip =     not found yet >=   0.000000000e+00        (72; 0)
+ 11067: mip =     not found yet >=   0.000000000e+00        (86; 0)
+ 13203: mip =     not found yet >=   0.000000000e+00        (101; 0)
+ 15411: mip =     not found yet >=   0.000000000e+00        (117; 1)
+ 18105: mip =     not found yet >=   0.000000000e+00        (134; 1)
+ 21758: mip =     not found yet >=   0.000000000e+00        (154; 1)
Time used: 60.1 secs.  Memory used: 3.8 Mb.
+ 26154: mip =     not found yet >=   0.000000000e+00        (183; 4)
+ 29923: >>>>>   0.000000000e+00 >=   0.000000000e+00   0.0% (253; 15)
+ 29923: mip =   0.000000000e+00 >=     tree is empty   0.0% (0; 535)
INTEGER OPTIMAL SOLUTION FOUND
Time used:   67.6 secs
Memory used: 4.9 Mb (5146500 bytes)
```

(This is again "inverted".)



---

archive/issue_comments_093160.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> This is really funny. I've now exported the MPS file on the 32-bit machine, too.\n> \n> While the doctest itself did not terminate [...], running `glpsol` on the exported (in theory identical) problem succeeds rather quickly [...]\n\nHmmm, even more weird (i.e. unexpected, but correct), the exported MPS files on both machines are identical; running `glpsol` with `--min` or `--max` on this file (on the 32-bit machine) succeeds in almost the same time, though `p.solve()` in the doctest (which should do nearly the same, acting on the same problem) does *not* terminate (I've added some doctests to ensure e.g. that the random graph is the same as on the other machine):\n\n```\n...\nTrying:\n    g = digraphs.RandomDirectedGNP(Integer(30),RealNumber('.3'))###line 3427:_sage_    >>> g = digraphs.RandomDirectedGNP(30,.3)\nExpecting nothing\nok\nTrying:\n    g.num_edges()###line 3428:_sage_    >>> g.num_edges()\nExpecting:\n    274\nok\nTrying:\n    g.is_connected(), g.is_strongly_connected()###line 3430:_sage_    >>> g.is_connected(), g.is_strongly_connected()\nExpecting:\n    (True, True)\nok\nTrying:\n    g.dig6_string()###line 3432:_sage_    >>> g.dig6_string()\nExpecting:\n    ']SgO??BsCQ_a?_ZEbOOJW@_glO_CZ`WkGQCQxD_]bOaVa@AQtGQROOwwGkG?_SKECgKe?QH`cf@@B@IOSQEhAO?GQ@MbmvGAAOOeG_[E?F?LoOo?O@GomMoQoWEdICAS@G@W@j?oCY@U_HeWCPG@SZI'\nok\nTrying:\n    k = Integer(g.edge_connectivity()) ; k###line 3434:_sage_    >>> k = Integer(g.edge_connectivity()) ; k\nExpecting:\n    5\nok\nTrying:\n    arborescences = g.edge_disjoint_spanning_trees(k,save_to_mps=\"edst-30_vertices.x86.mps\")###line 3436:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k,save_to_mps=\"edst-30_vertices.x86.mps\")\nExpecting nothing\nWriting problem data to `edst-30_vertices.x86.mps'...\n8412 records were written\nRunning the solver...\nGLPK Integer Optimizer, v4.44\n1719 rows, 3650 columns, 10040 non-zeros\n1370 integer variables, all of which are binary\nPreprocessing...\n1670 rows, 3605 columns, 9790 non-zeros\n1325 integer variables, all of which are binary\nScaling...\n A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00\nProblem data seem to be well scaled\nConstructing initial basis...\nSize of triangular part = 1670\nSolving LP relaxation...\nGLPK Simplex Optimizer, v4.44\n1670 rows, 3605 columns, 9790 non-zeros\n      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)\n   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)\n   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)\n*  1589: obj =   0.000000000e+00  infeas =  0.000e+00 (0)\nOPTIMAL SOLUTION FOUND\nInteger optimization begins...\n+  1589: mip =     not found yet <=              +inf        (1; 0)\n+  3027: mip =     not found yet <=   0.000000000e+00        (10; 0)\n+  4012: mip =     not found yet <=   0.000000000e+00        (21; 0)\n+  4827: mip =     not found yet <=   0.000000000e+00        (33; 0)\n+  6016: mip =     not found yet <=   0.000000000e+00        (45; 0)\n+  7325: mip =     not found yet <=   0.000000000e+00        (57; 0)\n+  8418: mip =     not found yet <=   0.000000000e+00        (71; 0)\n+ 10058: mip =     not found yet <=   0.000000000e+00        (86; 0)\n+ 12057: mip =     not found yet <=   0.000000000e+00        (102; 0)\n+ 14306: mip =     not found yet <=   0.000000000e+00        (119; 0)\n+ 16920: mip =     not found yet <=   0.000000000e+00        (138; 1)\n+ 19724: mip =     not found yet <=   0.000000000e+00        (161; 4)\nTime used: 60.1 secs.  Memory used: 4.5 Mb.\n+ 25085: mip =     not found yet <=   0.000000000e+00        (160; 37)\n+ 30069: mip =     not found yet <=   0.000000000e+00        (169; 66)\n+ 35413: mip =     not found yet <=   0.000000000e+00        (164; 114)\n+ 40592: mip =     not found yet <=   0.000000000e+00        (162; 148)\n+ 46308: mip =     not found yet <=   0.000000000e+00        (156; 202)\n+ 50687: mip =     not found yet <=   0.000000000e+00        (162; 226)\n+ 53833: mip =     not found yet <=   0.000000000e+00        (185; 227)\n+ 58922: mip =     not found yet <=   0.000000000e+00        (197; 235)\n+ 63603: mip =     not found yet <=   0.000000000e+00        (220; 239)\n+ 68927: mip =     not found yet <=   0.000000000e+00        (234; 267)\n+ 74057: mip =     not found yet <=   0.000000000e+00        (235; 309)\n+ 79491: mip =     not found yet <=   0.000000000e+00        (243; 327)\nTime used: 120.1 secs.  Memory used: 5.2 Mb.\n+ 84964: mip =     not found yet <=   0.000000000e+00        (249; 370)\n+ 90218: mip =     not found yet <=   0.000000000e+00        (246; 424)\n+ 94528: mip =     not found yet <=   0.000000000e+00        (262; 448)\n+ 98002: mip =     not found yet <=   0.000000000e+00        (274; 495)\n+101638: mip =     not found yet <=   0.000000000e+00        (269; 598)\n+104424: mip =     not found yet <=   0.000000000e+00        (281; 683)\n+108994: mip =     not found yet <=   0.000000000e+00        (271; 780)\n+113239: mip =     not found yet <=   0.000000000e+00        (272; 853)\n+116931: mip =     not found yet <=   0.000000000e+00        (277; 924)\n+120486: mip =     not found yet <=   0.000000000e+00        (288; 955)\n+125828: mip =     not found yet <=   0.000000000e+00        (278; 1021)\n+131593: mip =     not found yet <=   0.000000000e+00        (283; 1070)\nTime used: 180.2 secs.  Memory used: 5.7 Mb.\n...\nTime used: 480.2 secs.  Memory used: 7.1 Mb.\n+409472: mip =     not found yet <=   0.000000000e+00        (389; 6372)\n+414372: mip =     not found yet <=   0.000000000e+00        (392; 6505)\n+418908: mip =     not found yet <=   0.000000000e+00        (391; 6604)\n+423799: mip =     not found yet <=   0.000000000e+00        (403; 6673)\n+429213: mip =     not found yet <=   0.000000000e+00        (398; 6769)\n+434852: mip =     not found yet <=   0.000000000e+00        (389; 6876)\n+439868: mip =     not found yet <=   0.000000000e+00        (394; 6948)\n+445276: mip =     not found yet <=   0.000000000e+00        (401; 7011)\n+449608: mip =     not found yet <=   0.000000000e+00        (400; 7105)\n+453674: mip =     not found yet <=   0.000000000e+00        (409; 7184)\n+458621: mip =     not found yet <=   0.000000000e+00        (412; 7281)\n+464380: mip =     not found yet <=   0.000000000e+00        (391; 7412)\nTime used: 540.3 secs.  Memory used: 7.1 Mb.\n+469098: mip =     not found yet <=   0.000000000e+00        (399; 7494)\n*** *** Error: TIMED OUT! PROCESS KILLED! *** ***\n\n\t [600.9 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -verbose \"devel/sage-main/sage/graphs/generic_graph.py\" # Time out\nTotal time for all tests: 600.9 seconds\n+473909: mip =     not found yet <=   0.000000000e+00        (391; 7592)\n+479067: mip =     not found yet <=   0.000000000e+00        (391; 7669)\n+484074: mip =     not found yet <=   0.000000000e+00        (402; 7739)\n+489588: mip =     not found yet <=   0.000000000e+00        (405; 7825)\n+493883: mip =     not found yet <=   0.000000000e+00        (401; 7943)\n+498222: mip =     not found yet <=   0.000000000e+00        (408; 8030)\n+503017: mip =     not found yet <=   0.000000000e+00        (402; 8153)\n+507610: mip =     not found yet <=   0.000000000e+00        (412; 8231)\n+512031: mip =     not found yet <=   0.000000000e+00        (413; 8334)\n+516681: mip =     not found yet <=   0.000000000e+00        (410; 8439)\n+520300: mip =     not found yet <=   0.000000000e+00        (415; 8560)\nTime used: 600.3 secs.  Memory used: 7.1 Mb.\n...\nTime used: 3001.1 secs.  Memory used: 9.6 Mb.\n+2797586: mip =     not found yet <=   0.000000000e+00        (474; 56897)\n+2802741: mip =     not found yet <=   0.000000000e+00        (460; 57042)\n+2807948: mip =     not found yet <=   0.000000000e+00        (453; 57174)\n+2811236: mip =     not found yet <=   0.000000000e+00        (449; 57252)\n+2814551: mip =     not found yet <=   0.000000000e+00        (446; 57289)\n```\n\n(At this point I killed the orphaned Python process, since I'm pretty sure it wouldn't terminate. A previous run hadn't stopped after more than 44,000 seconds; cf. #9584.)\n\nSorry for abusing this ticket, which originally only dealt with the invalid MPS/LP file export issue.",
    "created_at": "2010-07-30T07:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93160",
    "user": "@nexttime"
}
```

Replying to [comment:8 leif]:
> This is really funny. I've now exported the MPS file on the 32-bit machine, too.
> 
> While the doctest itself did not terminate [...], running `glpsol` on the exported (in theory identical) problem succeeds rather quickly [...]

Hmmm, even more weird (i.e. unexpected, but correct), the exported MPS files on both machines are identical; running `glpsol` with `--min` or `--max` on this file (on the 32-bit machine) succeeds in almost the same time, though `p.solve()` in the doctest (which should do nearly the same, acting on the same problem) does *not* terminate (I've added some doctests to ensure e.g. that the random graph is the same as on the other machine):

```
...
Trying:
    g = digraphs.RandomDirectedGNP(Integer(30),RealNumber('.3'))###line 3427:_sage_    >>> g = digraphs.RandomDirectedGNP(30,.3)
Expecting nothing
ok
Trying:
    g.num_edges()###line 3428:_sage_    >>> g.num_edges()
Expecting:
    274
ok
Trying:
    g.is_connected(), g.is_strongly_connected()###line 3430:_sage_    >>> g.is_connected(), g.is_strongly_connected()
Expecting:
    (True, True)
ok
Trying:
    g.dig6_string()###line 3432:_sage_    >>> g.dig6_string()
Expecting:
    ']SgO??BsCQ_a?_ZEbOOJW@_glO_CZ`WkGQCQxD_]bOaVa@AQtGQROOwwGkG?_SKECgKe?QH`cf@@B@IOSQEhAO?GQ@MbmvGAAOOeG_[E?F?LoOo?O@GomMoQoWEdICAS@G@W@j?oCY@U_HeWCPG@SZI'
ok
Trying:
    k = Integer(g.edge_connectivity()) ; k###line 3434:_sage_    >>> k = Integer(g.edge_connectivity()) ; k
Expecting:
    5
ok
Trying:
    arborescences = g.edge_disjoint_spanning_trees(k,save_to_mps="edst-30_vertices.x86.mps")###line 3436:_sage_    >>> arborescences = g.edge_disjoint_spanning_trees(k,save_to_mps="edst-30_vertices.x86.mps")
Expecting nothing
Writing problem data to `edst-30_vertices.x86.mps'...
8412 records were written
Running the solver...
GLPK Integer Optimizer, v4.44
1719 rows, 3650 columns, 10040 non-zeros
1370 integer variables, all of which are binary
Preprocessing...
1670 rows, 3605 columns, 9790 non-zeros
1325 integer variables, all of which are binary
Scaling...
 A: min|aij| =  1.000e+00  max|aij| =  1.000e+00  ratio =  1.000e+00
Problem data seem to be well scaled
Constructing initial basis...
Size of triangular part = 1670
Solving LP relaxation...
GLPK Simplex Optimizer, v4.44
1670 rows, 3605 columns, 9790 non-zeros
      0: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
    500: obj =   0.000000000e+00  infeas =  2.610e+02 (0)
   1000: obj =   0.000000000e+00  infeas =  2.330e+02 (0)
   1500: obj =   0.000000000e+00  infeas =  1.172e+00 (0)
*  1589: obj =   0.000000000e+00  infeas =  0.000e+00 (0)
OPTIMAL SOLUTION FOUND
Integer optimization begins...
+  1589: mip =     not found yet <=              +inf        (1; 0)
+  3027: mip =     not found yet <=   0.000000000e+00        (10; 0)
+  4012: mip =     not found yet <=   0.000000000e+00        (21; 0)
+  4827: mip =     not found yet <=   0.000000000e+00        (33; 0)
+  6016: mip =     not found yet <=   0.000000000e+00        (45; 0)
+  7325: mip =     not found yet <=   0.000000000e+00        (57; 0)
+  8418: mip =     not found yet <=   0.000000000e+00        (71; 0)
+ 10058: mip =     not found yet <=   0.000000000e+00        (86; 0)
+ 12057: mip =     not found yet <=   0.000000000e+00        (102; 0)
+ 14306: mip =     not found yet <=   0.000000000e+00        (119; 0)
+ 16920: mip =     not found yet <=   0.000000000e+00        (138; 1)
+ 19724: mip =     not found yet <=   0.000000000e+00        (161; 4)
Time used: 60.1 secs.  Memory used: 4.5 Mb.
+ 25085: mip =     not found yet <=   0.000000000e+00        (160; 37)
+ 30069: mip =     not found yet <=   0.000000000e+00        (169; 66)
+ 35413: mip =     not found yet <=   0.000000000e+00        (164; 114)
+ 40592: mip =     not found yet <=   0.000000000e+00        (162; 148)
+ 46308: mip =     not found yet <=   0.000000000e+00        (156; 202)
+ 50687: mip =     not found yet <=   0.000000000e+00        (162; 226)
+ 53833: mip =     not found yet <=   0.000000000e+00        (185; 227)
+ 58922: mip =     not found yet <=   0.000000000e+00        (197; 235)
+ 63603: mip =     not found yet <=   0.000000000e+00        (220; 239)
+ 68927: mip =     not found yet <=   0.000000000e+00        (234; 267)
+ 74057: mip =     not found yet <=   0.000000000e+00        (235; 309)
+ 79491: mip =     not found yet <=   0.000000000e+00        (243; 327)
Time used: 120.1 secs.  Memory used: 5.2 Mb.
+ 84964: mip =     not found yet <=   0.000000000e+00        (249; 370)
+ 90218: mip =     not found yet <=   0.000000000e+00        (246; 424)
+ 94528: mip =     not found yet <=   0.000000000e+00        (262; 448)
+ 98002: mip =     not found yet <=   0.000000000e+00        (274; 495)
+101638: mip =     not found yet <=   0.000000000e+00        (269; 598)
+104424: mip =     not found yet <=   0.000000000e+00        (281; 683)
+108994: mip =     not found yet <=   0.000000000e+00        (271; 780)
+113239: mip =     not found yet <=   0.000000000e+00        (272; 853)
+116931: mip =     not found yet <=   0.000000000e+00        (277; 924)
+120486: mip =     not found yet <=   0.000000000e+00        (288; 955)
+125828: mip =     not found yet <=   0.000000000e+00        (278; 1021)
+131593: mip =     not found yet <=   0.000000000e+00        (283; 1070)
Time used: 180.2 secs.  Memory used: 5.7 Mb.
...
Time used: 480.2 secs.  Memory used: 7.1 Mb.
+409472: mip =     not found yet <=   0.000000000e+00        (389; 6372)
+414372: mip =     not found yet <=   0.000000000e+00        (392; 6505)
+418908: mip =     not found yet <=   0.000000000e+00        (391; 6604)
+423799: mip =     not found yet <=   0.000000000e+00        (403; 6673)
+429213: mip =     not found yet <=   0.000000000e+00        (398; 6769)
+434852: mip =     not found yet <=   0.000000000e+00        (389; 6876)
+439868: mip =     not found yet <=   0.000000000e+00        (394; 6948)
+445276: mip =     not found yet <=   0.000000000e+00        (401; 7011)
+449608: mip =     not found yet <=   0.000000000e+00        (400; 7105)
+453674: mip =     not found yet <=   0.000000000e+00        (409; 7184)
+458621: mip =     not found yet <=   0.000000000e+00        (412; 7281)
+464380: mip =     not found yet <=   0.000000000e+00        (391; 7412)
Time used: 540.3 secs.  Memory used: 7.1 Mb.
+469098: mip =     not found yet <=   0.000000000e+00        (399; 7494)
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***

	 [600.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -verbose "devel/sage-main/sage/graphs/generic_graph.py" # Time out
Total time for all tests: 600.9 seconds
+473909: mip =     not found yet <=   0.000000000e+00        (391; 7592)
+479067: mip =     not found yet <=   0.000000000e+00        (391; 7669)
+484074: mip =     not found yet <=   0.000000000e+00        (402; 7739)
+489588: mip =     not found yet <=   0.000000000e+00        (405; 7825)
+493883: mip =     not found yet <=   0.000000000e+00        (401; 7943)
+498222: mip =     not found yet <=   0.000000000e+00        (408; 8030)
+503017: mip =     not found yet <=   0.000000000e+00        (402; 8153)
+507610: mip =     not found yet <=   0.000000000e+00        (412; 8231)
+512031: mip =     not found yet <=   0.000000000e+00        (413; 8334)
+516681: mip =     not found yet <=   0.000000000e+00        (410; 8439)
+520300: mip =     not found yet <=   0.000000000e+00        (415; 8560)
Time used: 600.3 secs.  Memory used: 7.1 Mb.
...
Time used: 3001.1 secs.  Memory used: 9.6 Mb.
+2797586: mip =     not found yet <=   0.000000000e+00        (474; 56897)
+2802741: mip =     not found yet <=   0.000000000e+00        (460; 57042)
+2807948: mip =     not found yet <=   0.000000000e+00        (453; 57174)
+2811236: mip =     not found yet <=   0.000000000e+00        (449; 57252)
+2814551: mip =     not found yet <=   0.000000000e+00        (446; 57289)
```

(At this point I killed the orphaned Python process, since I'm pretty sure it wouldn't terminate. A previous run hadn't stopped after more than 44,000 seconds; cf. #9584.)

Sorry for abusing this ticket, which originally only dealt with the invalid MPS/LP file export issue.



---

archive/issue_comments_093161.json:
```json
{
    "body": "Changing component from numerical to linear programming.",
    "created_at": "2010-09-06T11:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93161",
    "user": "@nathanncohen"
}
```

Changing component from numerical to linear programming.



---

archive/issue_comments_093162.json:
```json
{
    "body": "This ticket should be closed, as it is made invalid because of #10043\n\nNathann",
    "created_at": "2010-10-23T16:16:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93162",
    "user": "@nathanncohen"
}
```

This ticket should be closed, as it is made invalid because of #10043

Nathann



---

archive/issue_comments_093163.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-11-16T17:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9617",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9617#issuecomment-93163",
    "user": "@jdemeyer"
}
```

Resolution: invalid
