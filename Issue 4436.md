# Issue 4436: Sage 3.2.a2: numerical noise in sage/calculus/calculus.py

archive/issues_004436.json:
```json
{
    "body": "Assignee: mabshoff\n\nOn an Itanium:\n\n```\nsage -t  devel/sage/sage/calculus/calculus.py              \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-iras/tmp/calculus.py\", line 7533:\n    sage: float(sinh(pi))\nExpected:\n    11.548739357257748\nGot:\n    11.548739357257746\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-iras/tmp/calculus.py\", line 7642:\n    sage: float(csch(pi))\nExpected:\n    0.086589537530046945\nGot:\n    0.086589537530046959\n**********************************************************************\n```\n\nOn an x86:\n\n```\nsage -t  devel/sage/sage/calculus/calculus.py               \n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py\", line 120:\n    sage: float(f(pi))\nExpected:\n    6.1232339957367663e-16\nGot:\n    6.1230317691118863e-16\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py\", line 7533:\n    sage: float(sinh(pi))\nExpected:\n    11.548739357257748\nGot:\n    11.548739357257746\n**********************************************************************\nFile \"/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py\", line 7642:\n    sage: float(csch(pi))\nExpected:\n    0.086589537530046945\nGot:\n    0.086589537530046959\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4436\n\n",
    "created_at": "2008-11-04T13:52:39Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.a2: numerical noise in sage/calculus/calculus.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4436",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

On an Itanium:

```
sage -t  devel/sage/sage/calculus/calculus.py              
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-iras/tmp/calculus.py", line 7533:
    sage: float(sinh(pi))
Expected:
    11.548739357257748
Got:
    11.548739357257746
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-iras/tmp/calculus.py", line 7642:
    sage: float(csch(pi))
Expected:
    0.086589537530046945
Got:
    0.086589537530046959
**********************************************************************
```

On an x86:

```
sage -t  devel/sage/sage/calculus/calculus.py               
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py", line 120:
    sage: float(f(pi))
Expected:
    6.1232339957367663e-16
Got:
    6.1230317691118863e-16
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py", line 7533:
    sage: float(sinh(pi))
Expected:
    11.548739357257748
Got:
    11.548739357257746
**********************************************************************
File "/home/mabshoff/build-3.2.a2/sage-3.2.alpha2-cicero/tmp/calculus.py", line 7642:
    sage: float(csch(pi))
Expected:
    0.086589537530046945
Got:
    0.086589537530046959
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4436





---

archive/issue_comments_032553.json:
```json
{
    "body": "The is also an issue in a G4:\n\n```\n    sage -t  devel/sage/sage/calculus/calculus.py \n         this has been reported, but I just noticed that there is   \n\"significant bit noise\", not insignificant bit noise: \n            Expected: \n                6.1232339957367663e-16 \n            Got: \n                6.1230317691118863e-16 \n```\n",
    "created_at": "2008-11-04T13:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4436#issuecomment-32553",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The is also an issue in a G4:

```
    sage -t  devel/sage/sage/calculus/calculus.py 
         this has been reported, but I just noticed that there is   
"significant bit noise", not insignificant bit noise: 
            Expected: 
                6.1232339957367663e-16 
            Got: 
                6.1230317691118863e-16 
```




---

archive/issue_comments_032554.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-04T13:53:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4436#issuecomment-32554",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032555.json:
```json
{
    "body": "Attachment [trac_4436.patch](tarball://root/attachments/some-uuid/ticket4436/trac_4436.patch) by mabshoff created at 2008-11-05 21:44:03",
    "created_at": "2008-11-05T21:44:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4436#issuecomment-32555",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [trac_4436.patch](tarball://root/attachments/some-uuid/ticket4436/trac_4436.patch) by mabshoff created at 2008-11-05 21:44:03



---

archive/issue_comments_032556.json:
```json
{
    "body": "Looks fine.",
    "created_at": "2008-11-05T22:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4436#issuecomment-32556",
    "user": "https://github.com/mwhansen"
}
```

Looks fine.



---

archive/issue_comments_032557.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-05T23:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4436#issuecomment-32557",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032558.json:
```json
{
    "body": "Merged in Sage 3.2.alpha3",
    "created_at": "2008-11-05T23:12:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4436",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4436#issuecomment-32558",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.alpha3



---

archive/issue_events_004680.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-05T23:12:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4436",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4436#event-4680"
}
```
