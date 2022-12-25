# Issue 1464: [with patch] binary code canonical labels & automorphism group generators

archive/issues_001464.json:
```json
{
    "body": "Assignee: @rlmill\n\nThe following bundle is based on 2.9 alpha5, so should merge easily\n\nhttp://sage.math.washington.edu/home/rlmill/sage-2.9.alpha5/binary_codes.hg\n\nNote that the coverage in the new file, binary_codes.pyx, is 100%.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1464\n\n",
    "created_at": "2007-12-11T23:25:32Z",
    "labels": [
        "component: coding theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.9",
    "title": "[with patch] binary code canonical labels & automorphism group generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1464",
    "user": "https://github.com/rlmill"
}
```
Assignee: @rlmill

The following bundle is based on 2.9 alpha5, so should merge easily

http://sage.math.washington.edu/home/rlmill/sage-2.9.alpha5/binary_codes.hg

Note that the coverage in the new file, binary_codes.pyx, is 100%.

Issue created by migration from https://trac.sagemath.org/ticket/1464





---

archive/issue_comments_009397.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-12-11T23:26:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1464#issuecomment-9397",
    "user": "https://github.com/rlmill"
}
```

Changing status from new to assigned.



---

archive/issue_comments_009398.json:
```json
{
    "body": "The bundle worked for me on Fedora 7.\n\n\n```\nsage -t  devel/sage-main/sage/coding/binary_code.pyx        \n         [2.8 s]\n \n----------------------------------------------------------------------\nAll tests passed!\n\n```\n\n\n\n\n```\n[jaap@paix sage-2.9.alpha5]$ ./sage -t devel/sage/sage/graphs*\nsage -t  devel/sage-main/sage/graphs/print_graphs.py        \n         [1.5 s]\nsage -t  devel/sage-main/sage/graphs/graph_database.py      \n         [12.9 s]\nsage -t  devel/sage-main/sage/graphs/graph_fast.pyx         \n         [1.8 s]\nsage -t  devel/sage-main/sage/graphs/graph_list.py          \n         [8.9 s]\nsage -t  devel/sage-main/sage/graphs/graph_genus1.py        \n         [12.8 s]\nsage -t  devel/sage-main/sage/graphs/graph.py               \n         [36.8 s]\nsage -t  devel/sage-main/sage/graphs/linearextensions.py    \n         [1.5 s]\nsage -t  devel/sage-main/sage/graphs/graph_isom.pyx         \n         [28.6 s]\nsage -t  devel/sage-main/sage/graphs/all.py                 \n         [1.5 s]\nsage -t  devel/sage-main/sage/graphs/graph_generators.py    \n         [61.9 s]\nsage -t  devel/sage-main/sage/graphs/bruhat_sn.pyx          \n         [1.6 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 169.8 seconds\n\n```\n",
    "created_at": "2007-12-12T00:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1464#issuecomment-9398",
    "user": "https://github.com/jaapspies"
}
```

The bundle worked for me on Fedora 7.


```
sage -t  devel/sage-main/sage/coding/binary_code.pyx        
         [2.8 s]
 
----------------------------------------------------------------------
All tests passed!

```




```
[jaap@paix sage-2.9.alpha5]$ ./sage -t devel/sage/sage/graphs*
sage -t  devel/sage-main/sage/graphs/print_graphs.py        
         [1.5 s]
sage -t  devel/sage-main/sage/graphs/graph_database.py      
         [12.9 s]
sage -t  devel/sage-main/sage/graphs/graph_fast.pyx         
         [1.8 s]
sage -t  devel/sage-main/sage/graphs/graph_list.py          
         [8.9 s]
sage -t  devel/sage-main/sage/graphs/graph_genus1.py        
         [12.8 s]
sage -t  devel/sage-main/sage/graphs/graph.py               
         [36.8 s]
sage -t  devel/sage-main/sage/graphs/linearextensions.py    
         [1.5 s]
sage -t  devel/sage-main/sage/graphs/graph_isom.pyx         
         [28.6 s]
sage -t  devel/sage-main/sage/graphs/all.py                 
         [1.5 s]
sage -t  devel/sage-main/sage/graphs/graph_generators.py    
         [61.9 s]
sage -t  devel/sage-main/sage/graphs/bruhat_sn.pyx          
         [1.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 169.8 seconds

```




---

archive/issue_events_003728.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-14T18:02:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1464#event-3728"
}
```



---

archive/issue_comments_009399.json:
```json
{
    "body": "There are still some bugs...",
    "created_at": "2007-12-14T18:02:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1464#issuecomment-9399",
    "user": "https://github.com/rlmill"
}
```

There are still some bugs...



---

archive/issue_comments_009400.json:
```json
{
    "body": "Use the bundle at\n\nhttp://sage.math.washington.edu/home/rlmill/bcodes_2.9.alpha7.hg\n\ninstead.",
    "created_at": "2007-12-15T22:24:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1464#issuecomment-9400",
    "user": "https://github.com/rlmill"
}
```

Use the bundle at

http://sage.math.washington.edu/home/rlmill/bcodes_2.9.alpha7.hg

instead.



---

archive/issue_events_003729.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-15T22:24:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "milestone": "sage-2.9.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1464#event-3729"
}
```



---

archive/issue_events_003730.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2007-12-15T22:24:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "milestone": "sage-2.9",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1464#event-3730"
}
```



---

archive/issue_comments_009401.json:
```json
{
    "body": "Do this after applying the bundle:\n\n```\nwas@sage:~/build/sage-2.9.rc0/devel/sage/sage/coding$ hg rm binary_code_backup.pyx \nwas@sage:~/build/sage-2.9.rc0/devel/sage/sage/coding$ hg ci\n```\n",
    "created_at": "2007-12-15T23:37:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1464#issuecomment-9401",
    "user": "https://github.com/williamstein"
}
```

Do this after applying the bundle:

```
was@sage:~/build/sage-2.9.rc0/devel/sage/sage/coding$ hg rm binary_code_backup.pyx 
was@sage:~/build/sage-2.9.rc0/devel/sage/sage/coding$ hg ci
```




---

archive/issue_comments_009402.json:
```json
{
    "body": "Merged in 2.9.rc2.",
    "created_at": "2007-12-16T00:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1464#issuecomment-9402",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in 2.9.rc2.



---

archive/issue_comments_009403.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-16T00:46:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1464#issuecomment-9403",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_003731.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2007-12-16T00:46:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1464",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1464#event-3731"
}
```
