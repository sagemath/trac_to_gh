# Issue 5743: Solaris 10/Sparc: Fix numerical noise issues in doctests

archive/issues_005743.json:
```json
{
    "body": "Assignee: mabshoff\n\nThere are a couple doctests on Solaris 10/Sparc that fail due to numerical noise. Fix it. \n\nA patch is coming up.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5743\n\n",
    "created_at": "2009-04-11T01:25:26Z",
    "labels": [
        "component: doctest coverage",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Solaris 10/Sparc: Fix numerical noise issues in doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5743",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

There are a couple doctests on Solaris 10/Sparc that fail due to numerical noise. Fix it. 

A patch is coming up.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5743





---

archive/issue_comments_044817.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-04-11T01:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5743#issuecomment-44817",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_044818.json:
```json
{
    "body": "Attachment [trac_5743.patch](tarball://root/attachments/some-uuid/ticket5743/trac_5743.patch) by mabshoff created at 2009-04-16 10:05:39",
    "created_at": "2009-04-16T10:05:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5743#issuecomment-44818",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_5743.patch](tarball://root/attachments/some-uuid/ticket5743/trac_5743.patch) by mabshoff created at 2009-04-16 10:05:39



---

archive/issue_comments_044819.json:
```json
{
    "body": "This patch fixes the following two doctest failures on Solaris 10/Sparc:\n\n```\nsage -t  \"devel/sage/sage/modules/free_module_element.pyx\"  \n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/modules/free_module_element.pyx\", line 505:\n    sage: vector(RDF, {1:pi, 1000:e})._sage_input_(SageInputBuilder(), False)\nExpected:\n    {call: {atomic:vector}({atomic:RDF}, {dict: {{atomic:1}:{atomic:3.1415926535897931}, {atomic:1000}:{atomic:2.7182818284590451}}})}\nGot:\n    {call: {atomic:vector}({atomic:RDF}, {dict: {{atomic:1}:{atomic:3.1415926535897931}, {atomic:1000}:{atomic:2.7182818284590455}}})}\n**********************************************************************\n1 items had failures:\n   1 of  10 in __main__.example_8\n```\n\nand\n\n```\nsage -t  \"devel/sage/sage/rings/real_double.pyx\"            \n**********************************************************************\nFile \"/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/rings/real_double.pyx\", line 727:\n    sage: sage_input(RDF(-e), verify=True, preparse=False)\nExpected:\n    # Verified\n    -RDF(2.7182818284590451)\nGot:\n    # Verified\n    -RDF(2.7182818284590455)\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T10:06:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5743#issuecomment-44819",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This patch fixes the following two doctest failures on Solaris 10/Sparc:

```
sage -t  "devel/sage/sage/modules/free_module_element.pyx"  
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/modules/free_module_element.pyx", line 505:
    sage: vector(RDF, {1:pi, 1000:e})._sage_input_(SageInputBuilder(), False)
Expected:
    {call: {atomic:vector}({atomic:RDF}, {dict: {{atomic:1}:{atomic:3.1415926535897931}, {atomic:1000}:{atomic:2.7182818284590451}}})}
Got:
    {call: {atomic:vector}({atomic:RDF}, {dict: {{atomic:1}:{atomic:3.1415926535897931}, {atomic:1000}:{atomic:2.7182818284590455}}})}
**********************************************************************
1 items had failures:
   1 of  10 in __main__.example_8
```

and

```
sage -t  "devel/sage/sage/rings/real_double.pyx"            
**********************************************************************
File "/home/mabshoff/build-3.4.1.rc1/sage-3.4.1.rc1-mark-gcc-4.3.3/devel/sage/sage/rings/real_double.pyx", line 727:
    sage: sage_input(RDF(-e), verify=True, preparse=False)
Expected:
    # Verified
    -RDF(2.7182818284590451)
Got:
    # Verified
    -RDF(2.7182818284590455)
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_044820.json:
```json
{
    "body": "Yep, that's some numerical noise.",
    "created_at": "2009-04-16T10:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5743#issuecomment-44820",
    "user": "https://github.com/craigcitro"
}
```

Yep, that's some numerical noise.



---

archive/issue_comments_044821.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-16T10:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5743#issuecomment-44821",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc3.

Cheers,

Michael



---

archive/issue_events_013472.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-16T10:21:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5743",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5743#event-13472"
}
```



---

archive/issue_comments_044822.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-16T10:21:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5743",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5743#issuecomment-44822",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
