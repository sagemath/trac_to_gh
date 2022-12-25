# Issue 8397: doctest devel/sage/sage/graphs/graph_list.py fails on Solaris 10 (SPARC)

archive/issues_008397.json:
```json
{
    "body": "Assignee: tbd\n\n == Details of the computer == \n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3 (uses Sun linker and assembler)\n\n == Sage version 4.3.3 (with several patches) ==\nI'm using a patched version of Sage 4.3.3, built as a 32-bit binary. The patches include:\n\n* #7867 Python patch, to allow Sage library to build. \n* #8191 Addition of iconv, which is needed for R\n* #8285 Update R's spkg-install to work on Solaris\n* #8363 Remove a useless check for mpir in cddlib \n* #8375 Numerical noise in devel/sage/sage/symbolic/pynac.pyx\n* #8374 Numerical noise in devel/sage/sage/symbolic/constants_c.pyx\n* #8371 Patch to allow pyprocessing to build - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely). \n\n == The problem ==\nThere are 8 test failures on this rather old SPARC. Increasing SAGE_TIMEOUT allowed 3 to pass. The longest is \"devel/sage/sage/rings/polynomial/symmetric_ideal.py\" which takes 459.4 s. \n\nHowever, 5 failures remain outstanding. \n\n```\n    sage -t  \"devel/sage/sage/graphs/graph_list.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/generic_graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph_database.py\" # Segfault\n    sage -t  \"devel/sage/sage/databases/database.py\" # Segfault\n```\n## Specific failure of this ticket\n\nThis ticket is documenting  graph_list.py, or to be more precise\n\n```\n\"devel/sage/sage/graphs/graph_list.py\"\n```\n\n## Related tickets\nThe other failures observed on this build of Solaris 10 are #8398, #8399, #8400 and #8401\n\n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8397\n\n",
    "closed_at": "2010-03-06T23:10:41Z",
    "created_at": "2010-02-28T16:19:48Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "doctest devel/sage/sage/graphs/graph_list.py fails on Solaris 10 (SPARC)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8397",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

 == Details of the computer == 
* Sun Blade 1000
* 2 x 900 MHz UltraSPARC III+ CPUs
* 2 GB RAM
* Solaris 10 03/2005 (first release of Solaris 10)
* gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version 4.3.3 (with several patches) ==
I'm using a patched version of Sage 4.3.3, built as a 32-bit binary. The patches include:

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
## Specific failure of this ticket

This ticket is documenting  graph_list.py, or to be more precise

```
"devel/sage/sage/graphs/graph_list.py"
```

## Related tickets
The other failures observed on this build of Solaris 10 are #8398, #8399, #8400 and #8401






Issue created by migration from https://trac.sagemath.org/ticket/8397





---

archive/issue_events_020135.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-03-06T23:10:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8397",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8397#event-20135"
}
```



---

archive/issue_comments_075111.json:
```json
{
    "body": "Fixed by #8408",
    "created_at": "2010-03-06T23:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8397",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8397#issuecomment-75111",
    "user": "https://github.com/mwhansen"
}
```

Fixed by #8408



---

archive/issue_comments_075112.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T23:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8397",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8397#issuecomment-75112",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
