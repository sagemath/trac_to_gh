# Issue 266: sloane functions -- get rid of any pre-initialization

archive/issues_000266.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  sage-combinat\n\nDo some standard python trickier so that the sloane sequence objects are not created until they are used.   According to this, just importing sloane_sequences.py is now a nontrivial part of the SAGE startup time, which is ridiculous:\n\n\n```\n   Ordered by: internal time\n\n   ncalls  tottime  percall  cumtime  percall filename:lineno(function)\n        1    0.070    0.070    0.093    0.093 functional.py:9(<module>)\n       30    0.049    0.002    1.224    0.041 all.py:1(<module>)\n 1575/274    0.046    0.000    0.087    0.000 ro.py:58(_flatten)\n     5284    0.039    0.000    0.039    0.000 :0(append)\n        1    0.038    0.038    0.038    0.038 matrix_space.py:15(<module>)\n        8    0.036    0.005    0.495    0.062 all.py:3(<module>)\n        2    0.036    0.018    1.284    0.642 all.py:4(<module>)\n        1    0.027    0.027    0.049    0.049 sloane_functions.py:42(<module>)\n```\n\n\nOf course, the sloane_functions.py module needs to be broken up a lot. \n\nIssue created by migration from https://trac.sagemath.org/ticket/266\n\n",
    "created_at": "2007-02-16T07:21:21Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "sloane functions -- get rid of any pre-initialization",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/266",
    "user": "@williamstein"
}
```
Assignee: @williamstein

CC:  sage-combinat

Do some standard python trickier so that the sloane sequence objects are not created until they are used.   According to this, just importing sloane_sequences.py is now a nontrivial part of the SAGE startup time, which is ridiculous:


```
   Ordered by: internal time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.070    0.070    0.093    0.093 functional.py:9(<module>)
       30    0.049    0.002    1.224    0.041 all.py:1(<module>)
 1575/274    0.046    0.000    0.087    0.000 ro.py:58(_flatten)
     5284    0.039    0.000    0.039    0.000 :0(append)
        1    0.038    0.038    0.038    0.038 matrix_space.py:15(<module>)
        8    0.036    0.005    0.495    0.062 all.py:3(<module>)
        2    0.036    0.018    1.284    0.642 all.py:4(<module>)
        1    0.027    0.027    0.049    0.049 sloane_functions.py:42(<module>)
```


Of course, the sloane_functions.py module needs to be broken up a lot. 

Issue created by migration from https://trac.sagemath.org/ticket/266





---

archive/issue_comments_001253.json:
```json
{
    "body": "Changing assignee from @williamstein to @ncalexan.",
    "created_at": "2007-02-18T21:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/266#issuecomment-1253",
    "user": "@ncalexan"
}
```

Changing assignee from @williamstein to @ncalexan.



---

archive/issue_comments_001254.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-02-18T21:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/266#issuecomment-1254",
    "user": "@ncalexan"
}
```

Resolution: fixed



---

archive/issue_comments_001255.json:
```json
{
    "body": "Fixed for 2.1.5.  Sloane now computes and caches trait_names() and __getattribute__ to pull SloaneSequence objects starting with 'A' from sage.combinat.sloane_functions.",
    "created_at": "2007-02-18T21:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/266",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/266#issuecomment-1255",
    "user": "@ncalexan"
}
```

Fixed for 2.1.5.  Sloane now computes and caches trait_names() and __getattribute__ to pull SloaneSequence objects starting with 'A' from sage.combinat.sloane_functions.
