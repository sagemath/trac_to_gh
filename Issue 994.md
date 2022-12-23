# Issue 994: ntl_GF2X class has very strange __int__ method

archive/issues_000994.json:
```json
{
    "body": "Assignee: malb\n\nThe `__int__` method on the ntl_GF2X class is quite strange.   It takes the terms of the polynomial from x<sup>0</sup> to x<sup>31</sup> (or x<sup>63</sup>), and treats them as the bits of a machine long (in a non-portable way, depending on the endianness of the processor).\n\nPerhaps it should use all the terms, and return a Python long if necessary (in little-endian format, as documented for the conversion from Integer to GF2X)?  Or maybe the `__int__` method should not be implemented at all?\n\nIssue created by migration from https://trac.sagemath.org/ticket/994\n\n",
    "created_at": "2007-10-25T05:15:01Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "title": "ntl_GF2X class has very strange __int__ method",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/994",
    "user": "cwitty"
}
```
Assignee: malb

The `__int__` method on the ntl_GF2X class is quite strange.   It takes the terms of the polynomial from x<sup>0</sup> to x<sup>31</sup> (or x<sup>63</sup>), and treats them as the bits of a machine long (in a non-portable way, depending on the endianness of the processor).

Perhaps it should use all the terms, and return a Python long if necessary (in little-endian format, as documented for the conversion from Integer to GF2X)?  Or maybe the `__int__` method should not be implemented at all?

Issue created by migration from https://trac.sagemath.org/ticket/994





---

archive/issue_comments_006058.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-25T22:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/994#issuecomment-6058",
    "user": "malb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006059.json:
```json
{
    "body": "as I called it __int__ and not BytesFromGF2X I think the behaviour is \nwrong and thus I changed it locally to return the constant coefficient if the  polynomial is constant. The patch to this is stuck in the patch attached to #416. So if that is accepted this ticket should be closed.",
    "created_at": "2007-10-25T22:05:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/994#issuecomment-6059",
    "user": "malb"
}
```

as I called it __int__ and not BytesFromGF2X I think the behaviour is 
wrong and thus I changed it locally to return the constant coefficient if the  polynomial is constant. The patch to this is stuck in the patch attached to #416. So if that is accepted this ticket should be closed.



---

archive/issue_comments_006060.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-27T02:48:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/994",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/994#issuecomment-6060",
    "user": "cwitty"
}
```

Resolution: fixed
