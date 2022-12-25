# Issue 5323: "./sage -t" gives misleading error message when doctesting non-existing file with absolute patch

archive/issues_005323.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @orlitzky\n\nThe `./` should not be here:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.3.rc3$ ./sage -t /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py \nERROR: File .//scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py is missing\n```\n\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5323\n\n",
    "created_at": "2009-02-20T15:49:37Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "\"./sage -t\" gives misleading error message when doctesting non-existing file with absolute patch",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5323",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

CC:  @orlitzky

The `./` should not be here:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc3$ ./sage -t /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py 
ERROR: File .//scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py is missing
```


Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5323





---

archive/issue_comments_040900.json:
```json
{
    "body": "Fixed in 4.8.alpha6:\n\n\n```\n$ ./sage -t /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py \nERROR: File /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py is missing\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\t/scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py # File not found\nTotal time for all tests: 0.0 seconds\n```\n",
    "created_at": "2012-01-05T00:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5323#issuecomment-40900",
    "user": "https://github.com/orlitzky"
}
```

Fixed in 4.8.alpha6:


```
$ ./sage -t /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py 
ERROR: File /scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py is missing
 
----------------------------------------------------------------------
The following tests failed:


	/scratch/mabshoff/sage-3.3.rc3/devel/sage/sage/plot/plotg.py # File not found
Total time for all tests: 0.0 seconds
```




---

archive/issue_comments_040901.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-05T00:31:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5323#issuecomment-40901",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_040902.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-01-05T00:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5323#issuecomment-40902",
    "user": "https://github.com/orlitzky"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_040903.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2012-01-05T13:37:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5323",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5323#issuecomment-40903",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme
