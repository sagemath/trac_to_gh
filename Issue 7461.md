# Issue 7461: partition_refinement.pyx

archive/issues_007461.json:
```json
{
    "body": "Assignee: mhansen\n\nI have witnessed this on many 32-bit linux machines:\n\n```\n[wstein@flavius sage-4.2.1.rc0]$ ./sage -t --long \"devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\"\nsage -t --long \"devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\"\n\n[[times out after 1800 seconds]]\n\n^CKeyboardInterrupt -- interrupted after 1386.7687881 seconds!\n         [1387.2 s]\n \n```\n\n\nDoing the same with --verbose dosn't necessarily time out. \n\nIssue created by migration from https://trac.sagemath.org/ticket/7461\n\n",
    "created_at": "2009-11-14T18:38:48Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "partition_refinement.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7461",
    "user": "was"
}
```
Assignee: mhansen

I have witnessed this on many 32-bit linux machines:

```
[wstein@flavius sage-4.2.1.rc0]$ ./sage -t --long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
sage -t --long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"

[[times out after 1800 seconds]]

^CKeyboardInterrupt -- interrupted after 1386.7687881 seconds!
         [1387.2 s]
 
```


Doing the same with --verbose dosn't necessarily time out. 

Issue created by migration from https://trac.sagemath.org/ticket/7461





---

archive/issue_comments_062841.json:
```json
{
    "body": "Changing assignee from mhansen to rlm.",
    "created_at": "2009-11-14T18:39:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62841",
    "user": "was"
}
```

Changing assignee from mhansen to rlm.



---

archive/issue_comments_062842.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2009-11-14T19:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62842",
    "user": "rlm"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_062843.json:
```json
{
    "body": "Is this consistently reproducible, or something you hit randomly?",
    "created_at": "2009-11-14T19:20:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62843",
    "user": "rlm"
}
```

Is this consistently reproducible, or something you hit randomly?



---

archive/issue_comments_062844.json:
```json
{
    "body": "> Is this consistently reproducible, or something you hit randomly? \n\nIt *always* happens on I think every single 32-bit Linux platform with non-verbose doctests.",
    "created_at": "2009-11-17T06:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62844",
    "user": "was"
}
```

> Is this consistently reproducible, or something you hit randomly? 

It *always* happens on I think every single 32-bit Linux platform with non-verbose doctests.



---

archive/issue_comments_062845.json:
```json
{
    "body": "On my virtual machine, 32-bit Ubuntu with non-verbose doctests:\n\n```\nrlmill@rlm32ubu:~/sage-4.2.1-linux-Ubuntu_9.10-i686-Linux$ ./sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\ninit.sage does not exist ... creating\nsage -t -long \"devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\"\n\t [228.4 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 228.4 seconds\n```\n\nThey passed three times in a row.\n\nAny ideas where to try next?",
    "created_at": "2009-11-18T18:45:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62845",
    "user": "rlm"
}
```

On my virtual machine, 32-bit Ubuntu with non-verbose doctests:

```
rlmill@rlm32ubu:~/sage-4.2.1-linux-Ubuntu_9.10-i686-Linux$ ./sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
init.sage does not exist ... creating
sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
	 [228.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 228.4 seconds
```

They passed three times in a row.

Any ideas where to try next?



---

archive/issue_comments_062846.json:
```json
{
    "body": "I think I am seeing this on centos32 on boxen. On this machine, the trouble is that the walltime is somehow severely messed up.\n\n\n```\nsage: walltime()\n1256774719.748621\n```\n\n\n*Exactly* ten seconds later:\n\n\n```\nsage: walltime()\n1256774720.2823999\n```\n\n\nThe difference is only 0.533. At that rate, what is supposed to be a 180 second doctest would take 3,374 seconds.\n\nI'm noticing other strange behavior here too. To debug, I had the code writing to a file. When I kill the doctest, I get my terminal back. But, in the other terminal which I am using to \"tail\" the file, I watch things continue to be written. Also, running the doctest for one minute, and sending a keyboard interrupt, gives the following:\n\n\n```\nwstein@centos53-32:/tmp/wstein/farm/sage-4.2.1$ ./sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\nsage -t -long \"devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\"\nKeyboardInterrupt -- interrupted after 3.99422097206 seconds!\n\t [4.5 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx\"\nTotal time for all tests: 4.5 seconds\n```\n\n\nHuh!?!",
    "created_at": "2009-11-19T09:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62846",
    "user": "rlm"
}
```

I think I am seeing this on centos32 on boxen. On this machine, the trouble is that the walltime is somehow severely messed up.


```
sage: walltime()
1256774719.748621
```


*Exactly* ten seconds later:


```
sage: walltime()
1256774720.2823999
```


The difference is only 0.533. At that rate, what is supposed to be a 180 second doctest would take 3,374 seconds.

I'm noticing other strange behavior here too. To debug, I had the code writing to a file. When I kill the doctest, I get my terminal back. But, in the other terminal which I am using to "tail" the file, I watch things continue to be written. Also, running the doctest for one minute, and sending a keyboard interrupt, gives the following:


```
wstein@centos53-32:/tmp/wstein/farm/sage-4.2.1$ ./sage -t -long devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx
sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
KeyboardInterrupt -- interrupted after 3.99422097206 seconds!
	 [4.5 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/sage/groups/perm_gps/partn_ref/refinement_matrices.pyx"
Total time for all tests: 4.5 seconds
```


Huh!?!



---

archive/issue_comments_062847.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2009-11-28T06:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62847",
    "user": "rlm"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_062848.json:
```json
{
    "body": "The agreed fix was to have the tests run for a certain number of cases, not for a certain time. This will also improve the valgrind testing when it is done, since it won't just time out after one test.\n\nHowever, these are new estimates for the number of tests that should be run (in particular, in the `-long` case). The release manager should give an opinion on whether the long doctests are too long for any of the systems we regularly test on.\n\nAlso, I have fixed the doctests to ensure that they are truly random, so that all this testing might actually find something.",
    "created_at": "2009-11-28T06:42:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62848",
    "user": "rlm"
}
```

The agreed fix was to have the tests run for a certain number of cases, not for a certain time. This will also improve the valgrind testing when it is done, since it won't just time out after one test.

However, these are new estimates for the number of tests that should be run (in particular, in the `-long` case). The release manager should give an opinion on whether the long doctests are too long for any of the systems we regularly test on.

Also, I have fixed the doctests to ensure that they are truly random, so that all this testing might actually find something.



---

archive/issue_comments_062849.json:
```json
{
    "body": "Attachment [trac_7461.patch](tarball://root/attachments/some-uuid/ticket7461/trac_7461.patch) by rlm created at 2009-11-28 06:42:42",
    "created_at": "2009-11-28T06:42:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62849",
    "user": "rlm"
}
```

Attachment [trac_7461.patch](tarball://root/attachments/some-uuid/ticket7461/trac_7461.patch) by rlm created at 2009-11-28 06:42:42



---

archive/issue_comments_062850.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-12-01T04:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62850",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_062851.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-01T04:51:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7461#issuecomment-62851",
    "user": "mhansen"
}
```

Resolution: fixed
