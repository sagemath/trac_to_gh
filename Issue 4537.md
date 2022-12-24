# Issue 4537: inverse_mod for number field ideals

archive/issues_004537.json:
```json
{
    "body": "Assignee: @loefflerd\n\nThe inverse_mod method currently isn't implemented for ideals in rings of integers of number fields. It should be, as it's not difficult.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4537\n\n",
    "created_at": "2008-11-17T07:51:11Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "inverse_mod for number field ideals",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4537",
    "user": "@loefflerd"
}
```
Assignee: @loefflerd

The inverse_mod method currently isn't implemented for ideals in rings of integers of number fields. It should be, as it's not difficult.

Issue created by migration from https://trac.sagemath.org/ticket/4537





---

archive/issue_comments_033819.json:
```json
{
    "body": "Attachment [4537-inversemod.patch](tarball://root/attachments/some-uuid/ticket4537/4537-inversemod.patch) by @loefflerd created at 2008-11-17 07:58:40\n\nI've uploaded a patch. Should work under 3.2.rc1 with the patch for #4536 installed (as it uses the coordinates() method of orders). \n\nI've implemented quadratic fields and general absolute fields; it would be trivial to implement for relative orders too, but there is so much general brokenness for relative orders that there doesn't seem much point (we don't even have is_integral() for relative orders yet).",
    "created_at": "2008-11-17T07:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4537#issuecomment-33819",
    "user": "@loefflerd"
}
```

Attachment [4537-inversemod.patch](tarball://root/attachments/some-uuid/ticket4537/4537-inversemod.patch) by @loefflerd created at 2008-11-17 07:58:40

I've uploaded a patch. Should work under 3.2.rc1 with the patch for #4536 installed (as it uses the coordinates() method of orders). 

I've implemented quadratic fields and general absolute fields; it would be trivial to implement for relative orders too, but there is so much general brokenness for relative orders that there doesn't seem much point (we don't even have is_integral() for relative orders yet).



---

archive/issue_comments_033820.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-11-17T07:58:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4537#issuecomment-33820",
    "user": "@loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_033821.json:
```json
{
    "body": "I would find something slightly more general useful, and you could implement your functions via this one too:\n\nIf A and B are coprime integral ideals, express 1=a+b with a in A, b in B.  (cf Prop 1.3.1 of Cohen's GTM 193 which I know you are using already).  The more general version of Thm 1.3.3 (op cit) would also be useful.",
    "created_at": "2008-11-17T09:51:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4537#issuecomment-33821",
    "user": "@JohnCremona"
}
```

I would find something slightly more general useful, and you could implement your functions via this one too:

If A and B are coprime integral ideals, express 1=a+b with a in A, b in B.  (cf Prop 1.3.1 of Cohen's GTM 193 which I know you are using already).  The more general version of Thm 1.3.3 (op cit) would also be useful.



---

archive/issue_comments_033822.json:
```json
{
    "body": "Replying to [comment:1 davidloeffler]:\n> I've uploaded a patch. Should work under 3.2.rc1 with the patch for #4536 installed (as it uses the coordinates() method of orders). \n> \n> I've implemented quadratic fields and general absolute fields; it would be trivial to implement for relative orders too, but there is so much general brokenness for relative orders that there doesn't seem much point (we don't even have is_integral() for relative orders yet). \n\nNote that #4536 now has a second bug-fixing patch attached, though the coordinates() funciton is not affected.  John",
    "created_at": "2008-11-18T17:29:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4537#issuecomment-33822",
    "user": "@JohnCremona"
}
```

Replying to [comment:1 davidloeffler]:
> I've uploaded a patch. Should work under 3.2.rc1 with the patch for #4536 installed (as it uses the coordinates() method of orders). 
> 
> I've implemented quadratic fields and general absolute fields; it would be trivial to implement for relative orders too, but there is so much general brokenness for relative orders that there doesn't seem much point (we don't even have is_integral() for relative orders yet). 

Note that #4536 now has a second bug-fixing patch attached, though the coordinates() funciton is not affected.  John



---

archive/issue_comments_033823.json:
```json
{
    "body": "REFEREE REPORT:\n\nPositive review, since this is a very nice patch.  I agree with John that it would be nice to have something more general, but that can be for another patch later. \n\nThis is very nice.  Good to go.",
    "created_at": "2008-11-28T06:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4537#issuecomment-33823",
    "user": "@williamstein"
}
```

REFEREE REPORT:

Positive review, since this is a very nice patch.  I agree with John that it would be nice to have something more general, but that can be for another patch later. 

This is very nice.  Good to go.



---

archive/issue_comments_033824.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T08:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4537#issuecomment-33824",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc0



---

archive/issue_comments_033825.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T08:36:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4537",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4537#issuecomment-33825",
    "user": "mabshoff"
}
```

Resolution: fixed
