# Issue 383: quo_rem in the polynomial rings does not use canonical coercion

archive/issues_000383.json:
```json
{
    "body": "Assignee: somebody\n\nI'm looking at the polynomial function quo_rem and I see that it does it's own\ncoercion manually.  This feels a little wrong to me.  I think it should go\nthrough the standard coercion routines.  Here's a \"bug\" that results:\n\n\n```\nsage: x=ZZ['x'].0\nsage: y=QQ['x'].0\nsage: (y+1).quo_rem(1/2*x)\n(2, 1)\nsage: (x+1).quo_rem(1/2*y)\n...\n<type 'exceptions.TypeError'>: no coercion of this rational to integer\n```\n\n\nThe bug is that I don't see why these two things are treated substantially\ndifferently.  The reason I found this is because the simple \"TypeError\"\nexception did not provide the usual message about parents being\nmis-matched -- I think this is a bug in itself\n\nThe fix for all that is to make the quo_rem stuff use canonical coercion model.\n\nAll of the quo_rem instances in sage/rings/polynomial/polynomial_element_generic.py suffer from some sort of coercion impropriety.\n\nIssue created by migration from https://trac.sagemath.org/ticket/383\n\n",
    "created_at": "2007-06-01T15:24:59Z",
    "labels": [
        "basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "quo_rem in the polynomial rings does not use canonical coercion",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/383",
    "user": "jbmohler"
}
```
Assignee: somebody

I'm looking at the polynomial function quo_rem and I see that it does it's own
coercion manually.  This feels a little wrong to me.  I think it should go
through the standard coercion routines.  Here's a "bug" that results:


```
sage: x=ZZ['x'].0
sage: y=QQ['x'].0
sage: (y+1).quo_rem(1/2*x)
(2, 1)
sage: (x+1).quo_rem(1/2*y)
...
<type 'exceptions.TypeError'>: no coercion of this rational to integer
```


The bug is that I don't see why these two things are treated substantially
differently.  The reason I found this is because the simple "TypeError"
exception did not provide the usual message about parents being
mis-matched -- I think this is a bug in itself

The fix for all that is to make the quo_rem stuff use canonical coercion model.

All of the quo_rem instances in sage/rings/polynomial/polynomial_element_generic.py suffer from some sort of coercion impropriety.

Issue created by migration from https://trac.sagemath.org/ticket/383





---

archive/issue_comments_001863.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-17T08:34:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1863",
    "user": "robertwb"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_001864.json:
```json
{
    "body": "Typo:  arithmatic  --> arithmetic",
    "created_at": "2010-01-17T10:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1864",
    "user": "was"
}
```

Typo:  arithmatic  --> arithmetic



---

archive/issue_comments_001865.json:
```json
{
    "body": "Attachment [383-binop-decorator.patch](tarball://root/attachments/some-uuid/ticket383/383-binop-decorator.patch) by robertwb created at 2010-01-17 10:24:52\n\nOops. Thanks, fixed.",
    "created_at": "2010-01-17T10:24:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1865",
    "user": "robertwb"
}
```

Attachment [383-binop-decorator.patch](tarball://root/attachments/some-uuid/ticket383/383-binop-decorator.patch) by robertwb created at 2010-01-17 10:24:52

Oops. Thanks, fixed.



---

archive/issue_comments_001866.json:
```json
{
    "body": "I read the code.  Looks AWESOME!\n\nIt appears to expose numerous issues:\n\n\n```\n\nsage -t devel/sage/sage/rings\n...\n\nThe following tests failed:\n\n        sage -t  devel/sage/sage/rings/finite_field_element.py # 3 doctests failed\n        sage -t  devel/sage/sage/rings/tests.py # 1 doctests failed\n        sage -t  devel/sage/sage/rings/finite_field_ext_pari.py # 1 doctests failed\n        sage -t  devel/sage/sage/rings/fraction_field_element.pyx # 1 doctests failed\n        sage -t  devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx # 1 doctests failed\n        sage -t  devel/sage/sage/rings/residue_field.pyx # 3 doctests failed\n        sage -t  devel/sage/sage/rings/polynomial/polynomial_zmod_flint.pyx # 5 doctests failed\n        sage -t  devel/sage/sage/rings/number_field/number_field_ideal.py # 2 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 192.3 seconds\n\n[1]+  Done                    ./sage -tp 10 devel/sage/sage/rings > 383.out\nwstein@boxen:~/build/sage-4.3.1.rc0$ pwd\n/home/wstein/build/sage-4.3.1.rc0\nwstein@boxen:~/build/sage-4.3.1.rc0$ ls\n383.out   6207.out~    data   dist      install.log  local     README.txt  sage-python          spkg      tmp\n6207.out  COPYING.txt  devel  examples  ipython      makefile  sage        sage-README-osx.txt  test.log\nwstein@boxen:~/build/sage-4.3.1.rc0$ pwd\n/home/wstein/build/sage-4.3.1.rc0\nwstein@boxen:~/build/sage-4.3.1.rc0$\n```\n",
    "created_at": "2010-01-17T10:49:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1866",
    "user": "was"
}
```

I read the code.  Looks AWESOME!

It appears to expose numerous issues:


```

sage -t devel/sage/sage/rings
...

The following tests failed:

        sage -t  devel/sage/sage/rings/finite_field_element.py # 3 doctests failed
        sage -t  devel/sage/sage/rings/tests.py # 1 doctests failed
        sage -t  devel/sage/sage/rings/finite_field_ext_pari.py # 1 doctests failed
        sage -t  devel/sage/sage/rings/fraction_field_element.pyx # 1 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_integer_dense_flint.pyx # 1 doctests failed
        sage -t  devel/sage/sage/rings/residue_field.pyx # 3 doctests failed
        sage -t  devel/sage/sage/rings/polynomial/polynomial_zmod_flint.pyx # 5 doctests failed
        sage -t  devel/sage/sage/rings/number_field/number_field_ideal.py # 2 doctests failed
----------------------------------------------------------------------
Total time for all tests: 192.3 seconds

[1]+  Done                    ./sage -tp 10 devel/sage/sage/rings > 383.out
wstein@boxen:~/build/sage-4.3.1.rc0$ pwd
/home/wstein/build/sage-4.3.1.rc0
wstein@boxen:~/build/sage-4.3.1.rc0$ ls
383.out   6207.out~    data   dist      install.log  local     README.txt  sage-python          spkg      tmp
6207.out  COPYING.txt  devel  examples  ipython      makefile  sage        sage-README-osx.txt  test.log
wstein@boxen:~/build/sage-4.3.1.rc0$ pwd
/home/wstein/build/sage-4.3.1.rc0
wstein@boxen:~/build/sage-4.3.1.rc0$
```




---

archive/issue_comments_001867.json:
```json
{
    "body": "Attachment [383-fixes.patch](tarball://root/attachments/some-uuid/ticket383/383-fixes.patch) by robertwb created at 2010-01-17 11:40:45",
    "created_at": "2010-01-17T11:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1867",
    "user": "robertwb"
}
```

Attachment [383-fixes.patch](tarball://root/attachments/some-uuid/ticket383/383-fixes.patch) by robertwb created at 2010-01-17 11:40:45



---

archive/issue_comments_001868.json:
```json
{
    "body": "OK, I've fixed all the above doctests issues.",
    "created_at": "2010-01-17T11:41:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1868",
    "user": "robertwb"
}
```

OK, I've fixed all the above doctests issues.



---

archive/issue_comments_001869.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-01-19T06:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1869",
    "user": "was"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_001870.json:
```json
{
    "body": "Ut oh:\n\n```\n----------------------------------------------------------------------\n\nThe following tests failed:\n\n        sage -t  devel/sage/sage/crypto/classical.py # 14 doctests failed\n        sage -t  devel/sage/sage/modular/etaproducts.py # 24 doctests failed\n        sage -t  devel/sage/sage/structure/element.pyx # 1 doctests failed\n        sage -t  devel/sage/sage/libs/pari/gen.pyx # Segfault\n        sage -t  devel/sage/sage/modular/arithgroup/arithgroup_generic.py # 4 doctests failed\n        sage -t  devel/sage/sage/modular/arithgroup/congroup_gamma0.py # 2 doctests failed\n        sage -t  devel/sage/sage/quadratic_forms/quadratic_form__split_local_covering.py # 2 doctests failed\n        sage -t  devel/sage/sage/modular/cusps.py # 1 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 478.6 seconds\nwstein@boxen:~/build/sage-4.3.1.rc0-boxen-x86_64-Linux$\n```\n",
    "created_at": "2010-01-19T06:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1870",
    "user": "was"
}
```

Ut oh:

```
----------------------------------------------------------------------

The following tests failed:

        sage -t  devel/sage/sage/crypto/classical.py # 14 doctests failed
        sage -t  devel/sage/sage/modular/etaproducts.py # 24 doctests failed
        sage -t  devel/sage/sage/structure/element.pyx # 1 doctests failed
        sage -t  devel/sage/sage/libs/pari/gen.pyx # Segfault
        sage -t  devel/sage/sage/modular/arithgroup/arithgroup_generic.py # 4 doctests failed
        sage -t  devel/sage/sage/modular/arithgroup/congroup_gamma0.py # 2 doctests failed
        sage -t  devel/sage/sage/quadratic_forms/quadratic_form__split_local_covering.py # 2 doctests failed
        sage -t  devel/sage/sage/modular/cusps.py # 1 doctests failed
----------------------------------------------------------------------
Total time for all tests: 478.6 seconds
wstein@boxen:~/build/sage-4.3.1.rc0-boxen-x86_64-Linux$
```




---

archive/issue_comments_001871.json:
```json
{
    "body": "Attachment [383-more-fixes.patch](tarball://root/attachments/some-uuid/ticket383/383-more-fixes.patch) by robertwb created at 2010-01-19 12:16:57\n\nOK, I've doctested the entire sage library this time.",
    "created_at": "2010-01-19T12:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1871",
    "user": "robertwb"
}
```

Attachment [383-more-fixes.patch](tarball://root/attachments/some-uuid/ticket383/383-more-fixes.patch) by robertwb created at 2010-01-19 12:16:57

OK, I've doctested the entire sage library this time.



---

archive/issue_comments_001872.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-19T12:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1872",
    "user": "robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_001873.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-19T12:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1873",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_001874.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T20:26:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/383",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/383#issuecomment-1874",
    "user": "rlm"
}
```

Resolution: fixed
