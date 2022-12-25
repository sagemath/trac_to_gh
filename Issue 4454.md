# Issue 4454: bug in preparser

archive/issues_004454.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  @robertwb boothby\n\nsage 3.1.4 on a 32-bit core duo\n\nconsider a file 'time.sage' with the following content:\n\ndef func(time = 5):\n    time = RDF(time)\n    return time\n\nloading this file then yields following error:\n\nsage: load time.sage\n------------------------------------------------------------\n   File \"/home/georg/.sage/temp/HILBERT/4119/_home_georg_Daten_Sync_Software_Sage_Experimente_time_time_sage_0.py\", line 7\n     __time__=misc.cputime(); __wall__=misc.walltime();  = RDF(time); print     \"Time: CPU %.2f s, Wall: %.2f s\"%(misc.cputime(__time__), misc.walltime(__wall__))\n                                                         ^\nSyntaxError: invalid syntax\n\nWARNING: Failure executing file: </home/georg/.sage/temp/HILBERT/4119/_home_georg_Daten_Sync_Software_Sage_Experimente_time_time_sage_0.py>\n\n\nIf one quits the space between 'time' and '=' in the second line of 'time.sage' it works as expected.\nDefining this function directly on the sage prompt also works as expected.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4454\n\n",
    "created_at": "2008-11-06T15:25:38Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "bug in preparser",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4454",
    "user": "https://trac.sagemath.org/admin/accounts/users/ggrafendorfer"
}
```
Assignee: cwitty

CC:  @robertwb boothby

sage 3.1.4 on a 32-bit core duo

consider a file 'time.sage' with the following content:

def func(time = 5):
    time = RDF(time)
    return time

loading this file then yields following error:

sage: load time.sage
------------------------------------------------------------
   File "/home/georg/.sage/temp/HILBERT/4119/_home_georg_Daten_Sync_Software_Sage_Experimente_time_time_sage_0.py", line 7
     __time__=misc.cputime(); __wall__=misc.walltime();  = RDF(time); print     "Time: CPU %.2f s, Wall: %.2f s"%(misc.cputime(__time__), misc.walltime(__wall__))
                                                         ^
SyntaxError: invalid syntax

WARNING: Failure executing file: </home/georg/.sage/temp/HILBERT/4119/_home_georg_Daten_Sync_Software_Sage_Experimente_time_time_sage_0.py>


If one quits the space between 'time' and '=' in the second line of 'time.sage' it works as expected.
Defining this function directly on the sage prompt also works as expected.

Issue created by migration from https://trac.sagemath.org/ticket/4454





---

archive/issue_comments_032798.json:
```json
{
    "body": "I don't know why in the final view it looks like this, of course the 'return time' part of the second line of the function definition should be a separate line.",
    "created_at": "2008-11-06T15:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4454#issuecomment-32798",
    "user": "https://trac.sagemath.org/admin/accounts/users/ggrafendorfer"
}
```

I don't know why in the final view it looks like this, of course the 'return time' part of the second line of the function definition should be a separate line.



---

archive/issue_comments_032799.json:
```json
{
    "body": "Hi,\n\nyou need to use \"`\" and \"`\" to get verbatim output - see also the main trac page. It would also be useful to have a more descriptive summary since as is \"bug in preparser\" is not very detailed :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-06T22:06:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4454#issuecomment-32799",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi,

you need to use "`" and "`" to get verbatim output - see also the main trac page. It would also be useful to have a more descriptive summary since as is "bug in preparser" is not very detailed :)

Cheers,

Michael



---

archive/issue_comments_032800.json:
```json
{
    "body": "This is still a problem despite numerous preparser bugs being fixed during SD 12:\n\n```\nsage: load time.sage\n------------------------------------------------------------\n   File \"/scratch/mabshoff/dot_sage/temp/sage.math.washington.edu/4348/_scratch_mabshoff_sage_3_3_rc0_time_sage_1.py\", line 8\n     __time__=misc.cputime(); __wall__=misc.walltime();  = RDF(time); print         \"Time: CPU %.2f s, Wall: %.2f s\"%(misc.cputime(__time__), misc.walltime(__wall__))\n                                                         ^\nSyntaxError: invalid syntax\n\nWARNING: Failure executing file: </scratch/mabshoff/dot_sage/temp/sage.math.washington.edu/4348/_scratch_mabshoff_sage_3_3_rc0_time_sage_1.py>\n```\n",
    "created_at": "2009-02-11T07:53:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4454#issuecomment-32800",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is still a problem despite numerous preparser bugs being fixed during SD 12:

```
sage: load time.sage
------------------------------------------------------------
   File "/scratch/mabshoff/dot_sage/temp/sage.math.washington.edu/4348/_scratch_mabshoff_sage_3_3_rc0_time_sage_1.py", line 8
     __time__=misc.cputime(); __wall__=misc.walltime();  = RDF(time); print         "Time: CPU %.2f s, Wall: %.2f s"%(misc.cputime(__time__), misc.walltime(__wall__))
                                                         ^
SyntaxError: invalid syntax

WARNING: Failure executing file: </scratch/mabshoff/dot_sage/temp/sage.math.washington.edu/4348/_scratch_mabshoff_sage_3_3_rc0_time_sage_1.py>
```




---

archive/issue_comments_032801.json:
```json
{
    "body": "Have you verified that this is not taken care of by #5106?",
    "created_at": "2009-02-11T07:57:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4454#issuecomment-32801",
    "user": "https://github.com/robertwb"
}
```

Have you verified that this is not taken care of by #5106?



---

archive/issue_comments_032802.json:
```json
{
    "body": "This has been fixed by #5106:\n\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: load time.sage\nsage: func()\n5.0\nsage: func(10)\n10.0\n```\n",
    "created_at": "2009-06-04T23:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4454#issuecomment-32802",
    "user": "https://github.com/mwhansen"
}
```

This has been fixed by #5106:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: load time.sage
sage: func()
5.0
sage: func(10)
10.0
```




---

archive/issue_comments_032803.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-06-04T23:35:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4454",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4454#issuecomment-32803",
    "user": "https://github.com/mwhansen"
}
```

Resolution: invalid
