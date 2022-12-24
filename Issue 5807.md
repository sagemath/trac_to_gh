# Issue 5807: dsage with @parallel doesn't work at all

archive/issues_005807.json:
```json
{
    "body": "Assignee: yi\n\nI tried to use dsage with the `@`parallel directory and sage-3.4, and it's 100% broken.  The log just spews forever:\n\n```\n\n2009-04-16 18:25:05-0700 [-] [Worker: 0] Restarting...\n2009-04-16 18:25:05-0700 [-] [Worker 0] Started...\n2009-04-16 18:25:05-0700 [-] [Worker 1] Job vISI9r9Dzs failed!\n2009-04-16 18:25:05-0700 [-] Traceback: \n         execfile('/scratch/wstein/sage/dsage/tmp_worker_files/vISI9r9Dzs/f.py')\n        re\n        Traceback (most recent call last):\n          File \"<stdin>\", line 1, in <module>\n          File \"/scratch/wstein/sage/dsage/tmp_worker_files/vISI9r9Dzs/f.py\", line 8, in <module>\n            f = unpickle_function(p_f)\n        NameError: name 'p_f' is not defined\n\n2009-04-16 18:25:05-0700 [-] [Worker: 1] Restarting...\n2009-04-16 18:25:05-0700 [-] [Worker 1] Started...\n2009-04-16 18:25:05-0700 [Broker,client] [Worker 0] Starting job 5pzNNCImcd \n2009-04-16 18:25:05-0700 [Broker,client] [Worker 1] Starting job vISI9r9Dzs \n```\n\n\nUsing `@`parallel and multiprocessing for what I want to do (just some simple no-pexpect C library stuff involving modular symbols) doesn't work either, since I get weird pari_trap error exceptions.\n\nIt is so sad, that after all these years and all this work to write code to run things in parallel, that even the most trivial basic thing that I would like to do in parallel, which is evaluate a function on a bunch of integer inputs, still doesn't work robustly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5807\n\n",
    "created_at": "2009-04-17T01:27:50Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "dsage with @parallel doesn't work at all",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5807",
    "user": "was"
}
```
Assignee: yi

I tried to use dsage with the `@`parallel directory and sage-3.4, and it's 100% broken.  The log just spews forever:

```

2009-04-16 18:25:05-0700 [-] [Worker: 0] Restarting...
2009-04-16 18:25:05-0700 [-] [Worker 0] Started...
2009-04-16 18:25:05-0700 [-] [Worker 1] Job vISI9r9Dzs failed!
2009-04-16 18:25:05-0700 [-] Traceback: 
         execfile('/scratch/wstein/sage/dsage/tmp_worker_files/vISI9r9Dzs/f.py')
        re
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "/scratch/wstein/sage/dsage/tmp_worker_files/vISI9r9Dzs/f.py", line 8, in <module>
            f = unpickle_function(p_f)
        NameError: name 'p_f' is not defined

2009-04-16 18:25:05-0700 [-] [Worker: 1] Restarting...
2009-04-16 18:25:05-0700 [-] [Worker 1] Started...
2009-04-16 18:25:05-0700 [Broker,client] [Worker 0] Starting job 5pzNNCImcd 
2009-04-16 18:25:05-0700 [Broker,client] [Worker 1] Starting job vISI9r9Dzs 
```


Using `@`parallel and multiprocessing for what I want to do (just some simple no-pexpect C library stuff involving modular symbols) doesn't work either, since I get weird pari_trap error exceptions.

It is so sad, that after all these years and all this work to write code to run things in parallel, that even the most trivial basic thing that I would like to do in parallel, which is evaluate a function on a bunch of integer inputs, still doesn't work robustly.

Issue created by migration from https://trac.sagemath.org/ticket/5807





---

archive/issue_comments_045608.json:
```json
{
    "body": "Note that dsage is so broken that it isn't even possible to test this out.  See #7975.",
    "created_at": "2010-01-18T12:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5807#issuecomment-45608",
    "user": "was"
}
```

Note that dsage is so broken that it isn't even possible to test this out.  See #7975.



---

archive/issue_comments_045609.json:
```json
{
    "body": "Dsage is now deprecated.",
    "created_at": "2010-01-19T07:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5807#issuecomment-45609",
    "user": "was"
}
```

Dsage is now deprecated.



---

archive/issue_comments_045610.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-01-19T07:41:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5807",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5807#issuecomment-45610",
    "user": "was"
}
```

Resolution: wontfix
