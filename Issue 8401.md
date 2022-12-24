# Issue 8401: doctest devel/sage/sage/graphs/graph_database.py fails on Solaris 10 (SPARC)

archive/issues_008401.json:
```json
{
    "body": "Assignee: tbd\n\n## Details of the computer\n* Sun Blade 1000\n* 2 x 900 MHz UltraSPARC III+ CPUs\n* 2 GB RAM\n* Solaris 10 03/2005 (first release of Solaris 10)\n* gcc 4.4.3\n\n == Sage version 4.3.3 (with several patches) ==\nI'm using a patched version of Sage sage-4.3.3, build as a 32-bit binary. The patches include:\n\n* #7867 Python patch, to allow Sage library to build. \n* #8191 Addition of iconv, which is needed for R\n* #8285 Update R's spkg-install to work on Solaris\n* #8363 Remove a useless check for mpir in cddlib \n* #8375 Numerical noise in devel/sage/sage/symbolic/pynac.pyx\n* #8374 Numerical noise in devel/sage/sage/symbolic/constants_c.pyx\n* #8371 Patch to allow pyprocessing to build - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely). \n\n == The problem ==\nThere are 8 test failures on this rather old SPARC. Increasing SAGE_TIMEOUT allowed 3 to pass. The longest is \"devel/sage/sage/rings/polynomial/symmetric_ideal.py\" which takes 459.4 s. \n\nHowever, 5 failures remain outstanding. \n\n\n```\n    sage -t  \"devel/sage/sage/graphs/graph_list.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/generic_graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph.py\" # Segfault\n    sage -t  \"devel/sage/sage/graphs/graph_database.py\" # Segfault\n    sage -t  \"devel/sage/sage/databases/database.py\" # Segfault\n```\n\n\n## Specific failure of this ticket\n\nThis ticket is documenting graph_database.py, or to be more precise\n\n\n```\n\"devel/sage/sage/graphs/graph_database.py\"\n```\n\n\n\n## Related tickets\nThe other failures observed on this build of Solaris 10 are #8397, #8398, #8399 and #8400\n\nIssue created by migration from https://trac.sagemath.org/ticket/8401\n\n",
    "created_at": "2010-02-28T16:41:18Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "doctest devel/sage/sage/graphs/graph_database.py fails on Solaris 10 (SPARC)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8401",
    "user": "drkirkby"
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
I'm using a patched version of Sage sage-4.3.3, build as a 32-bit binary. The patches include:

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

This ticket is documenting graph_database.py, or to be more precise


```
"devel/sage/sage/graphs/graph_database.py"
```



## Related tickets
The other failures observed on this build of Solaris 10 are #8397, #8398, #8399 and #8400

Issue created by migration from https://trac.sagemath.org/ticket/8401





---

archive/issue_comments_075246.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-06T23:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8401#issuecomment-75246",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_075247.json:
```json
{
    "body": "Fixed by #8408",
    "created_at": "2010-03-06T23:11:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8401",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8401#issuecomment-75247",
    "user": "mhansen"
}
```

Fixed by #8408
