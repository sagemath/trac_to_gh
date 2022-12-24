# Issue 1191: wrap pari's matsolvemodn for A.solve_right over Z/nZ

archive/issues_001191.json:
```json
{
    "body": "Assignee: was\n\nThis\n\n\n```\nmatsolvemod(M,D,B,{flag=0}): one solution of system of congruences \nMX=B mod D (M matrix, B and D column vectors). If (optional) flag is\nnon-null return all solutions.\n```\n\n\nshould allow to implement A.solve_right for matrices over Z/nZ.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1191\n\n",
    "created_at": "2007-11-17T15:24:47Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.9",
    "title": "wrap pari's matsolvemodn for A.solve_right over Z/nZ",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1191",
    "user": "malb"
}
```
Assignee: was

This


```
matsolvemod(M,D,B,{flag=0}): one solution of system of congruences 
MX=B mod D (M matrix, B and D column vectors). If (optional) flag is
non-null return all solutions.
```


should allow to implement A.solve_right for matrices over Z/nZ.

Issue created by migration from https://trac.sagemath.org/ticket/1191





---

archive/issue_comments_007391.json:
```json
{
    "body": "It seems like one would first have to add matsolvemod as a method in the gen class. (Or use the interface...).",
    "created_at": "2013-03-30T18:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7391",
    "user": "robharron"
}
```

It seems like one would first have to add matsolvemod as a method in the gen class. (Or use the interface...).



---

archive/issue_comments_007392.json:
```json
{
    "body": "I've added http://trac.sagemath.org/sage_trac/ticket/14391 so that one can access matsolvemod through the C-library interface. However, I now remember William telling me you can solve equations in **Z**/n**Z** using the code he wrote for finitely generated modular over a PID. And you can. It would be nice to use that implementation for A.solve_right.\n\nReplying to [comment:1 robharron]:\n> It seems like one would first have to add matsolvemod as a method in the gen class. (Or use the interface...).",
    "created_at": "2013-03-31T01:35:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7392",
    "user": "robharron"
}
```

I've added http://trac.sagemath.org/sage_trac/ticket/14391 so that one can access matsolvemod through the C-library interface. However, I now remember William telling me you can solve equations in **Z**/n**Z** using the code he wrote for finitely generated modular over a PID. And you can. It would be nice to use that implementation for A.solve_right.

Replying to [comment:1 robharron]:
> It seems like one would first have to add matsolvemod as a method in the gen class. (Or use the interface...).



---

archive/issue_comments_007393.json:
```json
{
    "body": "Okay, I've written a patch for this! Using pari is significantly faster than using the f.g. modules over a PID code, so the patch depends on #14391. This patch applies onto sage 5.8 and all doctests passed (using --testall --long).",
    "created_at": "2013-04-02T04:05:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7393",
    "user": "robharron"
}
```

Okay, I've written a patch for this! Using pari is significantly faster than using the f.g. modules over a PID code, so the patch depends on #14391. This patch applies onto sage 5.8 and all doctests passed (using --testall --long).



---

archive/issue_comments_007394.json:
```json
{
    "body": "Attachment [trac_1191_solve_right_Z_mod_n.patch](tarball://root/attachments/some-uuid/ticket1191/trac_1191_solve_right_Z_mod_n.patch) by robharron created at 2013-04-02 04:27:17",
    "created_at": "2013-04-02T04:27:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7394",
    "user": "robharron"
}
```

Attachment [trac_1191_solve_right_Z_mod_n.patch](tarball://root/attachments/some-uuid/ticket1191/trac_1191_solve_right_Z_mod_n.patch) by robharron created at 2013-04-02 04:27:17



---

archive/issue_comments_007395.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-02T04:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7395",
    "user": "robharron"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_007396.json:
```json
{
    "body": "Changing keywords from \"\" to \"solve_right, matsolvemod, Zmod\".",
    "created_at": "2013-04-02T04:28:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7396",
    "user": "robharron"
}
```

Changing keywords from "" to "solve_right, matsolvemod, Zmod".



---

archive/issue_comments_007397.json:
```json
{
    "body": "Can you post some timings comparing the two approaches (I am curious about larger dimensions & bitsizes)? The patch itself looks fine to me.",
    "created_at": "2013-04-02T11:32:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7397",
    "user": "malb"
}
```

Can you post some timings comparing the two approaches (I am curious about larger dimensions & bitsizes)? The patch itself looks fine to me.



---

archive/issue_comments_007398.json:
```json
{
    "body": "Here are some times (I temporarily added a method .solve_left_slow that uses the f.g. over a pid code; the latter naturally does things on the left):\n\n\n\n```\nsage: N = 124; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)\nsage: timeit('A.solve_right(b)')\n125 loops, best of 3: 3.72 ms per loop\nsage: timeit('AT.solve_left_slow(b)')\n5 loops, best of 3: 707 ms per loop\n\nsage: N = 12; r = 50; c = 38; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)\nsage: timeit('A.solve_right(b)')\n5 loops, best of 3: 44.3 ms per loop\nsage: timeit('AT.solve_left_slow(b)')\n5 loops, best of 3: 6.41 s per loop\n\nsage: N = 4829; r = 9; c = 5; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)\nsage: timeit('A.solve_right(b)')\n625 loops, best of 3: 343 \u00b5s per loop\nsage: timeit('AT.solve_left_slow(b)')\n5 loops, best of 3: 133 ms per loop\n\nsage: N = 2634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)\nsage: timeit('A.solve_right(b)')25 loops, best of 3: 13 ms per loop\nsage: timeit('AT.solve_left_slow(b)')5 loops, best of 3: 799 ms per loop\n\nsage: sage: N = 23457602398746509872634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)\nsage: timeit('A.solve_right(b)')\n5 loops, best of 3: 66.5 ms per loop\nsage: timeit('AT.solve_left_slow(b)')\n5 loops, best of 3: 1.18 s per loop\n\nsage: N = 29834756092364523457602398746509872634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)\nsage: timeit('A.solve_right(b)')\n5 loops, best of 3: 231 ms per loop\nsage: timeit('AT.solve_left_slow(b)')\n5 loops, best of 3: 1.54 s per loop\n```\n\n\n\nI also attached a code snippet of .solve_left_slow to this ticket for transparency and posterity!\n\nReplying to [comment:5 malb]:\n> Can you post some timings comparing the two approaches (I am curious about larger dimensions & bitsizes)? The patch itself looks fine to me.",
    "created_at": "2013-04-02T18:20:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7398",
    "user": "robharron"
}
```

Here are some times (I temporarily added a method .solve_left_slow that uses the f.g. over a pid code; the latter naturally does things on the left):



```
sage: N = 124; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
125 loops, best of 3: 3.72 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 707 ms per loop

sage: N = 12; r = 50; c = 38; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
5 loops, best of 3: 44.3 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 6.41 s per loop

sage: N = 4829; r = 9; c = 5; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
625 loops, best of 3: 343 µs per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 133 ms per loop

sage: N = 2634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')25 loops, best of 3: 13 ms per loop
sage: timeit('AT.solve_left_slow(b)')5 loops, best of 3: 799 ms per loop

sage: sage: N = 23457602398746509872634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
5 loops, best of 3: 66.5 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 1.18 s per loop

sage: N = 29834756092364523457602398746509872634095876; r = 21; c = 17; M = MatrixSpace(Zmod(N), r, c); A = M.random_element(); AL = A.lift(); X = Zmod(N) ** c; x = X.random_element(); xL = x.lift(); bL = AL * xL; bL = bL % N; AT = A.transpose(); b = (Zmod(N) ** r)(bL)
sage: timeit('A.solve_right(b)')
5 loops, best of 3: 231 ms per loop
sage: timeit('AT.solve_left_slow(b)')
5 loops, best of 3: 1.54 s per loop
```



I also attached a code snippet of .solve_left_slow to this ticket for transparency and posterity!

Replying to [comment:5 malb]:
> Can you post some timings comparing the two approaches (I am curious about larger dimensions & bitsizes)? The patch itself looks fine to me.



---

archive/issue_comments_007399.json:
```json
{
    "body": "Snippet of the f.g. modules over a PID implementation. This is much slower and only included for you curious people out there.",
    "created_at": "2013-04-02T18:21:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7399",
    "user": "robharron"
}
```

Snippet of the f.g. modules over a PID implementation. This is much slower and only included for you curious people out there.



---

archive/issue_comments_007400.json:
```json
{
    "body": "Attachment [solve_left_slow_snippet.py](tarball://root/attachments/some-uuid/ticket1191/solve_left_slow_snippet.py) by malb created at 2013-04-02 18:33:50\n\nOkay, that convinces me.",
    "created_at": "2013-04-02T18:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7400",
    "user": "malb"
}
```

Attachment [solve_left_slow_snippet.py](tarball://root/attachments/some-uuid/ticket1191/solve_left_slow_snippet.py) by malb created at 2013-04-02 18:33:50

Okay, that convinces me.



---

archive/issue_comments_007401.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-02T18:33:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7401",
    "user": "malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_007402.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2013-04-04T17:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1191",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1191#issuecomment-7402",
    "user": "jdemeyer"
}
```

Resolution: fixed
