# Issue 8399: doctest devel/sage/sage/graphs/graph.py fails on Solaris 10 (SPARC)

archive/issues_008399.json:
```json
{
    "body": "Assignee: @aghitza\n\n## Details of the computer\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3\n\n == Sage version 4.3.3 (with several patches) ==\nI'm using a patched version of Sage sage-4.3.3. The patches include:\n\n* #7867 Python patch, to allow Sage library to build. \n* #8191 Addition of iconv, which is needed for R\n* #8285 Update R's spkg-install to work on Solaris\n* #8363 Remove a useless check for mpir in cddlib \n* #8375 Numerical noise in devel/sage/sage/symbolic/pynac.pyx\n* #8374 Numerical noise in devel/sage/sage/symbolic/constants_c.pyx\n* #8371 Patch to allow pyprocessing to build - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely). \n\n == The problem ==\nThere are 8 test failures on this rather old SPARC. Increasing SAGE_TIMEOUT allowed 3 to pass. The longest is \"devel/sage/sage/rings/polynomial/symmetric_ideal.py\" which takes 459.4 s. \n\nHowever, 5 failures remain outstanding. \n\n\n```\n    sage -t  \"devel/sage/sage/graphs/graph_list.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/generic_graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph_database.py\" # Segfault\n    sage -t  \"devel/sage/sage/databases/database.py\" # Segfault\n```\n\n\nThis ticket is documenting graph.py, or to be more precise\n\n\"devel/sage/sage/graphs/graph.py\"\n\nIssue created by migration from https://trac.sagemath.org/ticket/8399\n\n",
    "created_at": "2010-02-28T16:23:50Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "doctest devel/sage/sage/graphs/graph.py fails on Solaris 10 (SPARC)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8399",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: @aghitza

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


This ticket is documenting graph.py, or to be more precise

"devel/sage/sage/graphs/graph.py"

Issue created by migration from https://trac.sagemath.org/ticket/8399





---

archive/issue_comments_075115.json:
```json
{
    "body": "Changing assignee from @aghitza to tbd.",
    "created_at": "2010-02-28T16:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8399#issuecomment-75115",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from @aghitza to tbd.



---

archive/issue_comments_075116.json:
```json
{
    "body": "Changing component from algebra to doctest.",
    "created_at": "2010-02-28T16:52:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8399#issuecomment-75116",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to doctest.



---

archive/issue_comments_075117.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T23:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8399#issuecomment-75117",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_075118.json:
```json
{
    "body": "Fixed by #8408",
    "created_at": "2010-03-06T23:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8399",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8399#issuecomment-75118",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #8408



---

archive/issue_events_008584.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-06T23:11:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8399",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8399#event-8584"
}
```
