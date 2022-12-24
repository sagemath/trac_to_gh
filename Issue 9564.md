# Issue 9564: libsingular exponentiation can not be interrupted

archive/issues_009564.json:
```json
{
    "body": "Assignee: malb\n\nKeywords: KeyboardInterrupt libsingular exponentiation\n\nWhen trying to get some timings for #7795, I did\n\n```\nsage: R.<x,y,z> = QQ[]\nsage: p = R.random_element()\nsage: p\n-x^2 + 1/3*x*y + 7/2*y + 2*z\nsage: timeit('q=p^(2^10)')\n```\n\nwhich might be stupid. \n\nAnyway, it was impossible to interrupt the computation with ctrl-C, which I think is a bug.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9564\n\n",
    "created_at": "2010-07-21T13:50:23Z",
    "labels": [
        "commutative algebra",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "libsingular exponentiation can not be interrupted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9564",
    "user": "SimonKing"
}
```
Assignee: malb

Keywords: KeyboardInterrupt libsingular exponentiation

When trying to get some timings for #7795, I did

```
sage: R.<x,y,z> = QQ[]
sage: p = R.random_element()
sage: p
-x^2 + 1/3*x*y + 7/2*y + 2*z
sage: timeit('q=p^(2^10)')
```

which might be stupid. 

Anyway, it was impossible to interrupt the computation with ctrl-C, which I think is a bug.

Issue created by migration from https://trac.sagemath.org/ticket/9564





---

archive/issue_comments_092328.json:
```json
{
    "body": "After applying #10018, the interrupt gives a segmentation fault instead of not doing anything at all.",
    "created_at": "2010-09-27T11:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92328",
    "user": "jdemeyer"
}
```

After applying #10018, the interrupt gives a segmentation fault instead of not doing anything at all.



---

archive/issue_comments_092329.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-09-27T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92329",
    "user": "jdemeyer"
}
```

Changing priority from major to critical.



---

archive/issue_comments_092330.json:
```json
{
    "body": "Changing assignee from malb to tba.",
    "created_at": "2010-09-27T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92330",
    "user": "jdemeyer"
}
```

Changing assignee from malb to tba.



---

archive/issue_comments_092331.json:
```json
{
    "body": "Changing component from commutative algebra to c_lib.",
    "created_at": "2010-09-27T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92331",
    "user": "jdemeyer"
}
```

Changing component from commutative algebra to c_lib.



---

archive/issue_comments_092332.json:
```json
{
    "body": "The problem is the following:\n\nWhen an interrupt is caught, the program acts as if `_sig_on` returns the value 0.  So, when using `_sig_on`, functions should be declared `except 0` and not `except -1`, which is what the Singular functions do.\n\nThe attached patch is purely proof-of-concept showing some improvement (but it doesn't fully fix the problem).",
    "created_at": "2010-09-27T13:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92332",
    "user": "jdemeyer"
}
```

The problem is the following:

When an interrupt is caught, the program acts as if `_sig_on` returns the value 0.  So, when using `_sig_on`, functions should be declared `except 0` and not `except -1`, which is what the Singular functions do.

The attached patch is purely proof-of-concept showing some improvement (but it doesn't fully fix the problem).



---

archive/issue_comments_092333.json:
```json
{
    "body": "Changing keywords from \"KeyboardInterrupt libsingular exponentiation\" to \"KeyboardInterrupt interrupt singular exception cython\".",
    "created_at": "2010-09-27T13:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92333",
    "user": "jdemeyer"
}
```

Changing keywords from "KeyboardInterrupt libsingular exponentiation" to "KeyboardInterrupt interrupt singular exception cython".



---

archive/issue_comments_092334.json:
```json
{
    "body": "Note also that what I just said is completely undocumented :-)",
    "created_at": "2010-09-27T13:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92334",
    "user": "jdemeyer"
}
```

Note also that what I just said is completely undocumented :-)



---

archive/issue_comments_092335.json:
```json
{
    "body": "Fixed by #9678.",
    "created_at": "2011-01-14T17:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92335",
    "user": "jdemeyer"
}
```

Fixed by #9678.



---

archive/issue_comments_092336.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-14T17:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92336",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_092337.json:
```json
{
    "body": "Isn't \"closed\" more fitting that \"need_review\" in that case ? `:-)`\n\nNathann",
    "created_at": "2011-05-04T14:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92337",
    "user": "ncohen"
}
```

Isn't "closed" more fitting that "need_review" in that case ? `:-)`

Nathann



---

archive/issue_comments_092338.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-04T15:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92338",
    "user": "jdemeyer"
}
```

Resolution: duplicate
