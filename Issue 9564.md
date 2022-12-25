# Issue 9564: libsingular exponentiation can not be interrupted

archive/issues_009564.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: KeyboardInterrupt libsingular exponentiation\n\nWhen trying to get some timings for #7795, I did\n\n```\nsage: R.<x,y,z> = QQ[]\nsage: p = R.random_element()\nsage: p\n-x^2 + 1/3*x*y + 7/2*y + 2*z\nsage: timeit('q=p^(2^10)')\n```\n\nwhich might be stupid. \n\nAnyway, it was impossible to interrupt the computation with ctrl-C, which I think is a bug.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9564\n\n",
    "created_at": "2010-07-21T13:50:23Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "libsingular exponentiation can not be interrupted",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9564",
    "user": "https://github.com/simon-king-jena"
}
```
Assignee: @malb

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

archive/issue_comments_092174.json:
```json
{
    "body": "After applying #10018, the interrupt gives a segmentation fault instead of not doing anything at all.",
    "created_at": "2010-09-27T11:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92174",
    "user": "https://github.com/jdemeyer"
}
```

After applying #10018, the interrupt gives a segmentation fault instead of not doing anything at all.



---

archive/issue_comments_092175.json:
```json
{
    "body": "Changing priority from major to critical.",
    "created_at": "2010-09-27T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92175",
    "user": "https://github.com/jdemeyer"
}
```

Changing priority from major to critical.



---

archive/issue_comments_092176.json:
```json
{
    "body": "Changing assignee from @malb to tba.",
    "created_at": "2010-09-27T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92176",
    "user": "https://github.com/jdemeyer"
}
```

Changing assignee from @malb to tba.



---

archive/issue_comments_092177.json:
```json
{
    "body": "Changing component from commutative algebra to c_lib.",
    "created_at": "2010-09-27T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92177",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from commutative algebra to c_lib.



---

archive/issue_comments_092178.json:
```json
{
    "body": "The problem is the following:\n\nWhen an interrupt is caught, the program acts as if `_sig_on` returns the value 0.  So, when using `_sig_on`, functions should be declared `except 0` and not `except -1`, which is what the Singular functions do.\n\nThe attached patch is purely proof-of-concept showing some improvement (but it doesn't fully fix the problem).",
    "created_at": "2010-09-27T13:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92178",
    "user": "https://github.com/jdemeyer"
}
```

The problem is the following:

When an interrupt is caught, the program acts as if `_sig_on` returns the value 0.  So, when using `_sig_on`, functions should be declared `except 0` and not `except -1`, which is what the Singular functions do.

The attached patch is purely proof-of-concept showing some improvement (but it doesn't fully fix the problem).



---

archive/issue_comments_092179.json:
```json
{
    "body": "Changing keywords from \"KeyboardInterrupt libsingular exponentiation\" to \"KeyboardInterrupt interrupt singular exception cython\".",
    "created_at": "2010-09-27T13:38:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92179",
    "user": "https://github.com/jdemeyer"
}
```

Changing keywords from "KeyboardInterrupt libsingular exponentiation" to "KeyboardInterrupt interrupt singular exception cython".



---

archive/issue_comments_092180.json:
```json
{
    "body": "Note also that what I just said is completely undocumented :-)",
    "created_at": "2010-09-27T13:39:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92180",
    "user": "https://github.com/jdemeyer"
}
```

Note also that what I just said is completely undocumented :-)



---

archive/issue_comments_092181.json:
```json
{
    "body": "Fixed by #9678.",
    "created_at": "2011-01-14T17:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92181",
    "user": "https://github.com/jdemeyer"
}
```

Fixed by #9678.



---

archive/issue_comments_092182.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-01-14T17:39:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92182",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_events_023816.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-14T17:39:16Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9564#event-23816"
}
```



---

archive/issue_comments_092183.json:
```json
{
    "body": "Isn't \"closed\" more fitting that \"need_review\" in that case ? `:-)`\n\nNathann",
    "created_at": "2011-05-04T14:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92183",
    "user": "https://github.com/nathanncohen"
}
```

Isn't "closed" more fitting that "need_review" in that case ? `:-)`

Nathann



---

archive/issue_comments_092184.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-05-04T15:06:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9564#issuecomment-92184",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_023817.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-04T15:06:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9564",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9564#event-23817"
}
```
