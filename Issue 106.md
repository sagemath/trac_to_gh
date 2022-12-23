# Issue 106: maple (etc?) tab completion -- asking for a list of all completions gives a bad error message if maple isn't installed

archive/issues_000106.json:
```json
{
    "body": "Assignee: was\n\nThis is especially a problem in the SAGE notebook.   Probably the same problem happens for Mathematica.\n\nIssue created by migration from https://trac.sagemath.org/ticket/106\n\n",
    "created_at": "2006-10-03T03:50:03Z",
    "labels": [
        "user interface",
        "minor",
        "bug"
    ],
    "title": "maple (etc?) tab completion -- asking for a list of all completions gives a bad error message if maple isn't installed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/106",
    "user": "was"
}
```
Assignee: was

This is especially a problem in the SAGE notebook.   Probably the same problem happens for Mathematica.

Issue created by migration from https://trac.sagemath.org/ticket/106





---

archive/issue_comments_000503.json:
```json
{
    "body": "This is still an issue with Sage 2.8.2-rc3:\n\n```\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.2.rc3, Release Date: 2007-08-21                   |\n| Type notebook() for the GUI, and license() for information.        |\nsage: maple.\nBuilding Maple command completion list (this takes\na few seconds only the first time you do it).\nTo force rebuild later, delete /home/mabshoff/.sage//maple_commandlist_cache.sobj.\n\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     maple.\n           ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n\nsage: maple.\nBuilding Maple command completion list (this takes\na few seconds only the first time you do it).\nTo force rebuild later, delete /home/mabshoff/.sage//maple_commandlist_cache.sobj.\n\n------------------------------------------------------------\n   File \"<ipython console>\", line 1\n     maple.\n           ^\n<type 'exceptions.SyntaxError'>: invalid syntax\n\nsage:\n```\n\n\nAn exception is raised you try execute a maple command without maple being installed:\n\n```\nsage: maple(1+1)\n---------------------------------------------------------------------------\n<type 'exceptions.TypeError'>             Traceback (most recent call last)\n\n/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/data/extcode/maple/user/<ipython console> in <module>()\n\n/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)\n    556                 return cls(self, str(x))\n    557             except TypeError, msg2:\n--> 558                 raise TypeError, msg\n    559\n    560\n\n<type 'exceptions.TypeError'>: Unable to start maple because the command 'maple -t' failed.\n```\n\n\nCheers,\n\nMichael\n\nCheers,\n\nMichael",
    "created_at": "2007-08-23T12:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/106#issuecomment-503",
    "user": "mabshoff"
}
```

This is still an issue with Sage 2.8.2-rc3:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.2.rc3, Release Date: 2007-08-21                   |
| Type notebook() for the GUI, and license() for information.        |
sage: maple.
Building Maple command completion list (this takes
a few seconds only the first time you do it).
To force rebuild later, delete /home/mabshoff/.sage//maple_commandlist_cache.sobj.

------------------------------------------------------------
   File "<ipython console>", line 1
     maple.
           ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage: maple.
Building Maple command completion list (this takes
a few seconds only the first time you do it).
To force rebuild later, delete /home/mabshoff/.sage//maple_commandlist_cache.sobj.

------------------------------------------------------------
   File "<ipython console>", line 1
     maple.
           ^
<type 'exceptions.SyntaxError'>: invalid syntax

sage:
```


An exception is raised you try execute a maple command without maple being installed:

```
sage: maple(1+1)
---------------------------------------------------------------------------
<type 'exceptions.TypeError'>             Traceback (most recent call last)

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/data/extcode/maple/user/<ipython console> in <module>()

/tmp/Work2/sage-2.8.1/sage-2.8.2.rc3/local/lib/python2.5/site-packages/sage/interfaces/expect.py in __call__(self, x)
    556                 return cls(self, str(x))
    557             except TypeError, msg2:
--> 558                 raise TypeError, msg
    559
    560

<type 'exceptions.TypeError'>: Unable to start maple because the command 'maple -t' failed.
```


Cheers,

Michael

Cheers,

Michael



---

archive/issue_comments_000504.json:
```json
{
    "body": "Attachment\n\nfixes the problem",
    "created_at": "2007-09-06T18:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/106#issuecomment-504",
    "user": "was"
}
```

Attachment

fixes the problem



---

archive/issue_comments_000505.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T18:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/106#issuecomment-505",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_000506.json:
```json
{
    "body": "fixed for sage-2.8.4",
    "created_at": "2007-09-06T18:45:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/106#issuecomment-506",
    "user": "was"
}
```

fixed for sage-2.8.4
