# Issue 4708: sage -tp doesn't test absolute file names nor does it ignore non-existent files

archive/issues_004708.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: ptest parallel test absolute filename\n\n\n```\n-*- mode: sage-test; default-directory: \"~/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/\" -*-\nsage-test started at Thu Dec  4 20:43:38\n\n/Users/ncalexan/bin/sage -b >/dev/null && /Users/ncalexan/bin/sage -tp 2 /Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py\n\nreal\t0m1.413s\nuser\t0m0.875s\nsys\t0m0.426s\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 0.0 seconds\n\nsage-test finished (all test passed) at Thu Dec  4 20:43:40\n```\n\n\nAlso:\n\n\n```\n-*- mode: sage-test; default-directory: \"~/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/\" -*-\nsage-test started at Thu Dec  4 20:44:39\n\n/Users/ncalexan/bin/sage -b >/dev/null && /Users/ncalexan/bin/sage -t /Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2\n\nreal\t0m1.311s\nuser\t0m0.872s\nsys\t0m0.416s\nERROR: File .//Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2 is missing\nexit code: 1\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\t.//Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2\nTotal time for all tests: 0.0 seconds\n\nsage-test finished (all test passed) at Thu Dec  4 20:44:40\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4708\n\n",
    "created_at": "2008-12-05T04:47:56Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "sage -tp doesn't test absolute file names nor does it ignore non-existent files",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4708",
    "user": "https://github.com/ncalexan"
}
```
Assignee: mabshoff

Keywords: ptest parallel test absolute filename


```
-*- mode: sage-test; default-directory: "~/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/" -*-
sage-test started at Thu Dec  4 20:43:38

/Users/ncalexan/bin/sage -b >/dev/null && /Users/ncalexan/bin/sage -tp 2 /Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py

real	0m1.413s
user	0m0.875s
sys	0m0.426s
Global iterations: 1
File iterations: 1
TeX files: 0
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 0.0 seconds

sage-test finished (all test passed) at Thu Dec  4 20:43:40
```


Also:


```
-*- mode: sage-test; default-directory: "~/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/" -*-
sage-test started at Thu Dec  4 20:44:39

/Users/ncalexan/bin/sage -b >/dev/null && /Users/ncalexan/bin/sage -t /Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2

real	0m1.311s
user	0m0.872s
sys	0m0.416s
ERROR: File .//Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2 is missing
exit code: 1
 
----------------------------------------------------------------------
The following tests failed:


	.//Users/ncalexan/sage-3.2.1.alpha1/devel/sage-nca/sage/modules/free_module.py2
Total time for all tests: 0.0 seconds

sage-test finished (all test passed) at Thu Dec  4 20:44:40
```


Issue created by migration from https://trac.sagemath.org/ticket/4708





---

archive/issue_comments_035435.json:
```json
{
    "body": "Attachment [trac_4708_bin.patch](tarball://root/attachments/some-uuid/ticket4708/trac_4708_bin.patch) by @garyfurnish created at 2008-12-05 04:55:48",
    "created_at": "2008-12-05T04:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4708#issuecomment-35435",
    "user": "https://github.com/garyfurnish"
}
```

Attachment [trac_4708_bin.patch](tarball://root/attachments/some-uuid/ticket4708/trac_4708_bin.patch) by @garyfurnish created at 2008-12-05 04:55:48



---

archive/issue_comments_035436.json:
```json
{
    "body": "Trivial fix attached.",
    "created_at": "2008-12-05T04:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4708#issuecomment-35436",
    "user": "https://github.com/garyfurnish"
}
```

Trivial fix attached.



---

archive/issue_comments_035437.json:
```json
{
    "body": "Changing assignee from mabshoff to @garyfurnish.",
    "created_at": "2008-12-05T04:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4708#issuecomment-35437",
    "user": "https://github.com/garyfurnish"
}
```

Changing assignee from mabshoff to @garyfurnish.



---

archive/issue_comments_035438.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-05T04:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4708#issuecomment-35438",
    "user": "https://github.com/garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_035439.json:
```json
{
    "body": "Attachment [4708_bin-2.patch](tarball://root/attachments/some-uuid/ticket4708/4708_bin-2.patch) by @ncalexan created at 2008-12-05 05:44:12\n\nApply only 4708_bin-2.patch, all credit to gfurnish.",
    "created_at": "2008-12-05T05:44:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4708#issuecomment-35439",
    "user": "https://github.com/ncalexan"
}
```

Attachment [4708_bin-2.patch](tarball://root/attachments/some-uuid/ticket4708/4708_bin-2.patch) by @ncalexan created at 2008-12-05 05:44:12

Apply only 4708_bin-2.patch, all credit to gfurnish.



---

archive/issue_comments_035440.json:
```json
{
    "body": "Merged 4708_bin-2.patch in Sage 3.2.2.alpha0",
    "created_at": "2008-12-05T06:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4708#issuecomment-35440",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4708_bin-2.patch in Sage 3.2.2.alpha0



---

archive/issue_events_004953.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-12-05T06:38:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4708#event-4953"
}
```



---

archive/issue_comments_035441.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-05T06:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4708",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4708#issuecomment-35441",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
