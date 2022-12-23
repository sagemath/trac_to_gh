# Issue 6819: multinomial to accept lists as argument too

archive/issues_006819.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: arithmetic\n\nI have modified multinomial to accept lists as argument too. It makes programming with it much easier\n\nIssue created by migration from https://trac.sagemath.org/ticket/6819\n\n",
    "created_at": "2009-08-24T18:23:05Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "multinomial to accept lists as argument too",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6819",
    "user": "rishi"
}
```
Assignee: tbd

Keywords: arithmetic

I have modified multinomial to accept lists as argument too. It makes programming with it much easier

Issue created by migration from https://trac.sagemath.org/ticket/6819





---

archive/issue_comments_056226.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-08-24T18:32:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6819#issuecomment-56226",
    "user": "rishi"
}
```

Attachment



---

archive/issue_comments_056227.json:
```json
{
    "body": "Seems ok to me ! I Applied it, used it, and did not understand why it was not possible already !\n\nBy the way, I added some docstrings to the function, so if you think it is ok.. ;-)",
    "created_at": "2009-08-25T07:26:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6819#issuecomment-56227",
    "user": "ncohen"
}
```

Seems ok to me ! I Applied it, used it, and did not understand why it was not possible already !

By the way, I added some docstrings to the function, so if you think it is ok.. ;-)



---

archive/issue_comments_056228.json:
```json
{
    "body": "Attachment\n\npatch reviewed + some docstrings",
    "created_at": "2009-08-25T07:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6819#issuecomment-56228",
    "user": "ncohen"
}
```

Attachment

patch reviewed + some docstrings



---

archive/issue_comments_056229.json:
```json
{
    "body": "Replying to [comment:2 ncohen]:\n> Seems ok to me ! I Applied it, used it, and did not understand why it was not possible already !\n> \n> By the way, I added some docstrings to the function, so if you think it is ok.. ;-)\n\nThanks for the docstrings.",
    "created_at": "2009-08-25T13:59:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6819#issuecomment-56229",
    "user": "rishi"
}
```

Replying to [comment:2 ncohen]:
> Seems ok to me ! I Applied it, used it, and did not understand why it was not possible already !
> 
> By the way, I added some docstrings to the function, so if you think it is ok.. ;-)

Thanks for the docstrings.



---

archive/issue_comments_056230.json:
```json
{
    "body": "Attachment\n\nncohen's reviewer patch",
    "created_at": "2009-08-30T07:51:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6819#issuecomment-56230",
    "user": "mvngu"
}
```

Attachment

ncohen's reviewer patch



---

archive/issue_comments_056231.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-30T08:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6819#issuecomment-56231",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_056232.json:
```json
{
    "body": "The patch `multinomial_list.patch` contains some badly formatted docstrings. But those shouldn't prevent the patch from being merged. Better to fix those formatting issues in a separate ticket. See #6845 for a follow up to fix this docstring issue.\n\n\n\nncohen -- Your username should be in your patches; it makes it easier to credit you for your contributions. Please also remember to put in a sensible commit message for your patches.\n\n\n\nWhile merging and testing these patches:\n\n1. `12846.patch` -- rishi's contribution\n2. `trac_6819-reviewer.patch` -- ncohen's contribution\n \nI ran into a doctest failure:\n\n```\nsage -t -long devel/sage-main/sage/misc/getusage.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/misc/getusage.py\", line 69:\n    sage: get_memory_usage(t)          # amount of memory more than when we defined t.\nExpected:\n    0.0\nGot:\n    0.34375\n**********************************************************************\n1 items had failures:\n   1 of   4 in __main__.example_2\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_getusage.py\n\t [2.6 s]\n\n```\n\nThis has nothing to do with the above patches. Strangely, it crops up when I run the test on sage.math. But the test passes on mod.math and geom.math. Merged patches in this order:\n\n1. `12846.patch`\n2. `trac_6819-reviewer.patch`",
    "created_at": "2009-08-30T08:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6819",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6819#issuecomment-56232",
    "user": "mvngu"
}
```

The patch `multinomial_list.patch` contains some badly formatted docstrings. But those shouldn't prevent the patch from being merged. Better to fix those formatting issues in a separate ticket. See #6845 for a follow up to fix this docstring issue.



ncohen -- Your username should be in your patches; it makes it easier to credit you for your contributions. Please also remember to put in a sensible commit message for your patches.



While merging and testing these patches:

1. `12846.patch` -- rishi's contribution
2. `trac_6819-reviewer.patch` -- ncohen's contribution
 
I ran into a doctest failure:

```
sage -t -long devel/sage-main/sage/misc/getusage.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.1/devel/sage-main/sage/misc/getusage.py", line 69:
    sage: get_memory_usage(t)          # amount of memory more than when we defined t.
Expected:
    0.0
Got:
    0.34375
**********************************************************************
1 items had failures:
   1 of   4 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.1/tmp/.doctest_getusage.py
	 [2.6 s]

```

This has nothing to do with the above patches. Strangely, it crops up when I run the test on sage.math. But the test passes on mod.math and geom.math. Merged patches in this order:

1. `12846.patch`
2. `trac_6819-reviewer.patch`
