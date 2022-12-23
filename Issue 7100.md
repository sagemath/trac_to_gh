# Issue 7100: rounding error in QuadraticForm.vectors_by_length()

archive/issues_007100.json:
```json
{
    "body": "Assignee: justin\n\nCC:  tornaria\n\nA rounding error causes an issue in `vectors_by_length()`. The square root of a very tiny negative number (which should be rounded to zero) is computed, creating a symbolic imaginary expression which floor can't round to a nearest integer (e.g. `floor(2.0 + 1.49011611938e-08*I)` below).\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: Q = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1])\nsage: Q.vectors_by_length(2)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (1093, 0))\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n---------------------------------------------------------------------------\nTypeError                                 Traceback (most recent call last)\n\n/home/tornaria/.sage/temp/sage.math.washington.edu/20501/_home_tornaria__sage_init_sage_0.py in <module>()\n\n/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/quadratic_forms/quadratic_form__split_local_covering.py in vectors_by_length(self, bound)\n    207             ## 2. Compute bounds\n    208             Z = sqrt(T[i] / Q[i][i])\n--> 209             L[i] = ZZ(floor(Z - U[i]))  \n    210             x[i] = ZZ(ceil(-Z - U[i]) - 0)  \n    211 \n\n/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)()\n\n/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)()\n\n/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._integer_ (sage/symbolic/expression.cpp:4136)()\n\nTypeError: unable to convert x (=floor(2.0 + 1.49011611938e-08*I)) to an integer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7100\n\n",
    "created_at": "2009-10-03T13:35:57Z",
    "labels": [
        "quadratic forms",
        "major",
        "bug"
    ],
    "title": "rounding error in QuadraticForm.vectors_by_length()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7100",
    "user": "tornaria"
}
```
Assignee: justin

CC:  tornaria

A rounding error causes an issue in `vectors_by_length()`. The square root of a very tiny negative number (which should be rounded to zero) is computed, creating a symbolic imaginary expression which floor can't round to a nearest integer (e.g. `floor(2.0 + 1.49011611938e-08*I)` below).

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Q = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1])
sage: Q.vectors_by_length(2)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (1093, 0))
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)

/home/tornaria/.sage/temp/sage.math.washington.edu/20501/_home_tornaria__sage_init_sage_0.py in <module>()

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/quadratic_forms/quadratic_form__split_local_covering.py in vectors_by_length(self, bound)
    207             ## 2. Compute bounds
    208             Z = sqrt(T[i] / Q[i][i])
--> 209             L[i] = ZZ(floor(Z - U[i]))  
    210             x[i] = ZZ(ceil(-Z - U[i]) - 0)  
    211 

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/structure/parent.so in sage.structure.parent.Parent.__call__ (sage/structure/parent.c:4171)()

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/structure/coerce_maps.so in sage.structure.coerce_maps.NamedConvertMap._call_ (sage/structure/coerce_maps.c:4064)()

/home/tornaria/sage-4.1.1-sage.math.washington.edu-x86_64-Linux/local/lib/python2.6/site-packages/sage/symbolic/expression.so in sage.symbolic.expression.Expression._integer_ (sage/symbolic/expression.cpp:4136)()

TypeError: unable to convert x (=floor(2.0 + 1.49011611938e-08*I)) to an integer
```


Issue created by migration from https://trac.sagemath.org/ticket/7100





---

archive/issue_comments_058767.json:
```json
{
    "body": "I changed it to take the abs of Z, but I don't know if this goes the right way for the bounds.  Someone familiar with the algorithm should check this.  All tests do pass.",
    "created_at": "2009-10-04T03:07:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58767",
    "user": "mhansen"
}
```

I changed it to take the abs of Z, but I don't know if this goes the right way for the bounds.  Someone familiar with the algorithm should check this.  All tests do pass.



---

archive/issue_comments_058768.json:
```json
{
    "body": "Replying to [comment:1 mhansen]:\n> I changed it to take the abs of Z, but I don't know if this goes the right way for the bounds.  Someone familiar with the algorithm should check this.  All tests do pass.\n\nActually, this is wrong:\n\n```\nQ = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1]) \nsage: map(len, Q.vectors_by_length(2)) \n[1, 12, 11]\n```\n\nBecause it's missing one of the vectors of norm 2 (namely `[0, -1, 0, -1]`) due to roundoff errors.\n\nThe way to fix this is to use a bound for searching which is an epsilon larger than an integer --- enough to cover the roundoff errors. Pari uses `1e-6` for this epsilon.\n\nI'll post a patch in a moment.",
    "created_at": "2010-01-14T15:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58768",
    "user": "tornaria"
}
```

Replying to [comment:1 mhansen]:
> I changed it to take the abs of Z, but I don't know if this goes the right way for the bounds.  Someone familiar with the algorithm should check this.  All tests do pass.

Actually, this is wrong:

```
Q = QuadraticForm(ZZ, 4, [1,1,1,1, 1,0,0, 1,0, 1]) 
sage: map(len, Q.vectors_by_length(2)) 
[1, 12, 11]
```

Because it's missing one of the vectors of norm 2 (namely `[0, -1, 0, -1]`) due to roundoff errors.

The way to fix this is to use a bound for searching which is an epsilon larger than an integer --- enough to cover the roundoff errors. Pari uses `1e-6` for this epsilon.

I'll post a patch in a moment.



---

archive/issue_comments_058769.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-14T15:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58769",
    "user": "tornaria"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_058770.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-14T15:41:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58770",
    "user": "tornaria"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_058771.json:
```json
{
    "body": "Use this patch instead of the other one (updated)",
    "created_at": "2010-01-14T16:55:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58771",
    "user": "tornaria"
}
```

Use this patch instead of the other one (updated)



---

archive/issue_comments_058772.json:
```json
{
    "body": "Attachment\n\nAll tests pass with my patch on top of a clean sage-4.3.",
    "created_at": "2010-01-14T16:57:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58772",
    "user": "tornaria"
}
```

Attachment

All tests pass with my patch on top of a clean sage-4.3.



---

archive/issue_comments_058773.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-14T17:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58773",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058774.json:
```json
{
    "body": "Looks good.  Thanks for looking over this!",
    "created_at": "2010-01-14T17:20:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58774",
    "user": "mhansen"
}
```

Looks good.  Thanks for looking over this!



---

archive/issue_comments_058775.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-16T02:48:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7100",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7100#issuecomment-58775",
    "user": "rlm"
}
```

Resolution: fixed
