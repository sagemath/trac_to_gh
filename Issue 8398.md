# Issue 8398: doctest devel/sage/sage/graphs/generic_graph.py fails on Solaris 10 (SPARC)

archive/issues_008398.json:
```json
{
    "body": "Assignee: tbd\n\n## Details of the computer\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3\n\n == Sage version 4.3.3 (with several patches) ==\nI'm using a patched version of Sage sage-4.3.3. The patches include:\n\n* #7867 Python patch, to allow Sage library to build. \n* #8191 Addition of iconv, which is needed for R\n* #8285 Update R's spkg-install to work on Solaris\n* #8363 Remove a useless check for mpir in cddlib \n* #8375 Numerical noise in devel/sage/sage/symbolic/pynac.pyx\n* #8374 Numerical noise in devel/sage/sage/symbolic/constants_c.pyx\n* #8371 Patch to allow pyprocessing to build - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely). \n\n == The problem ==\nThere are 8 test failures on this rather old SPARC. Increasing SAGE_TIMEOUT allowed 3 to pass. The longest is \"devel/sage/sage/rings/polynomial/symmetric_ideal.py\" which takes 459.4 s. \n\nHowever, 5 failures remain outstanding. \n\n\n```\n    sage -t  \"devel/sage/sage/graphs/graph_list.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/generic_graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph_database.py\" # Segfault\n    sage -t  \"devel/sage/sage/databases/database.py\" # Segfault\n```\n\n\nThis ticket is documenting generic_graph.py, or to be more precise\n\n\"devel/sage/sage/graphs/generic_graph.py\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/8398\n\n",
    "created_at": "2010-02-28T16:22:49Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "doctest devel/sage/sage/graphs/generic_graph.py fails on Solaris 10 (SPARC)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8398",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

## Details of the computer
* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3

 == Sage version 4.3.3 (with several patches) ==
I'm using a patched version of Sage sage-4.3.3. The patches include:

* #7867 Python patch, to allow Sage library to build. 
* #8191 Addition of iconv, which is needed for R
* #8285 Update R's spkg-install to work on Solaris
* #8363 Remove a useless check for mpir in cddlib 
* #8375 Numerical noise in devel/sage/sage/symbolic/pynac.pyx
* #8374 Numerical noise in devel/sage/sage/symbolic/constants_c.pyx
* #8371 Patch to allow pyprocessing to build - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely). 

 == The problem ==
There are 8 test failures on this rather old SPARC. Increasing SAGE_TIMEOUT allowed 3 to pass. The longest is "devel/sage/sage/rings/polynomial/symmetric_ideal.py" which takes 459.4 s. 

However, 5 failures remain outstanding. 


```
    sage -t  "devel/sage/sage/graphs/graph_list.py" # Segfault
    sage -t  "devel/sage/sage/graphs/generic_graph.py" # Segfault
    sage -t  "devel/sage/sage/graphs/graph.py" # Segfault
    sage -t  "devel/sage/sage/graphs/graph_database.py" # Segfault
    sage -t  "devel/sage/sage/databases/database.py" # Segfault
```


This ticket is documenting generic_graph.py, or to be more precise

"devel/sage/sage/graphs/generic_graph.py"

Issue created by migration from https://trac.sagemath.org/ticket/8398





---

archive/issue_events_008583.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-03-06T23:10:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8398",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8398#event-8583"
}
```



---

archive/issue_comments_075113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T23:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8398#issuecomment-75113",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_075114.json:
```json
{
    "body": "Fixed by #8408.",
    "created_at": "2010-03-06T23:10:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8398#issuecomment-75114",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #8408.
