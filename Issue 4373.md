# Issue 4373: doctest failure in sage/algebras/group_algebra.py on 32 bit platforms

archive/issues_004373.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  mhansen\n\n\n```\nsage -t  devel/sage/sage/algebras/group_algebra.py          \n********************************************************************** \nFile \"/home/jaap/downloads/sage-3.2.alpha0/tmp/group_algebra.py\", line 230: \n     sage: OG(FormalSum([ (1, G(2)), (2, RR(0.77)) ]), check=False) \nExpected: \n     [2 0] \n     [0 2] + 2*0.770000000000000 \nGot: \n     2*0.770000000000000 + [2 0] \n     [0 2] \n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4373\n\n",
    "created_at": "2008-10-27T05:35:02Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "doctest failure in sage/algebras/group_algebra.py on 32 bit platforms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4373",
    "user": "mabshoff"
}
```
Assignee: mabshoff

CC:  mhansen


```
sage -t  devel/sage/sage/algebras/group_algebra.py          
********************************************************************** 
File "/home/jaap/downloads/sage-3.2.alpha0/tmp/group_algebra.py", line 230: 
     sage: OG(FormalSum([ (1, G(2)), (2, RR(0.77)) ]), check=False) 
Expected: 
     [2 0] 
     [0 2] + 2*0.770000000000000 
Got: 
     2*0.770000000000000 + [2 0] 
     [0 2] 
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4373





---

archive/issue_comments_032153.json:
```json
{
    "body": "David,\n\nsince this is your patch any clue what is going on here?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T12:54:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32153",
    "user": "mabshoff"
}
```

David,

since this is your patch any clue what is going on here?

Cheers,

Michael



---

archive/issue_comments_032154.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-10-28T12:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32154",
    "user": "mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_032155.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-28T13:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32155",
    "user": "davidloeffler"
}
```

Attachment



---

archive/issue_comments_032156.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-28T13:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32156",
    "user": "davidloeffler"
}
```

Changing status from new to assigned.



---

archive/issue_comments_032157.json:
```json
{
    "body": "The failed doctest was just verifying that the \"check\" flag could be disabled, by using this to create a bogus group algebra element that is a formal sum of things that aren't in the right group. The string representation of such an element depends on the sort order of the elements, which is completely arbitrary and subject to changing between platforms, hence the failure here.\n\nAll that's really needed is to check that the method runs; it's inconceivable that it could run but not give the expected answer. So I've uploaded a 1-line patch that marks the doctest with \"# random\".\n\n(I didn't use the \"#64-bit\" and \"#32-bit\" flags as then it would just break again next time someone changed the sort order of real numbers versus integer matrices, which is bound to happen before long.)",
    "created_at": "2008-10-28T13:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32157",
    "user": "davidloeffler"
}
```

The failed doctest was just verifying that the "check" flag could be disabled, by using this to create a bogus group algebra element that is a formal sum of things that aren't in the right group. The string representation of such an element depends on the sort order of the elements, which is completely arbitrary and subject to changing between platforms, hence the failure here.

All that's really needed is to check that the method runs; it's inconceivable that it could run but not give the expected answer. So I've uploaded a 1-line patch that marks the doctest with "# random".

(I didn't use the "#64-bit" and "#32-bit" flags as then it would just break again next time someone changed the sort order of real numbers versus integer matrices, which is bound to happen before long.)



---

archive/issue_comments_032158.json:
```json
{
    "body": "Changing assignee from mabshoff to davidloeffler.",
    "created_at": "2008-10-28T13:31:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32158",
    "user": "davidloeffler"
}
```

Changing assignee from mabshoff to davidloeffler.



---

archive/issue_comments_032159.json:
```json
{
    "body": "Ok, I think in that situation then #random is warranted. But could you please replace the patch by a version that adds the explanation you just gave on the ticket why this fails so that in the future people looking at that doctest understand why. It would also be nice to mention this ticket number in the string, i.e. \"the issue was also discussed at #4373\".\n\nMike: FYI since you also had some comments about this code.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T13:41:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32159",
    "user": "mabshoff"
}
```

Ok, I think in that situation then #random is warranted. But could you please replace the patch by a version that adds the explanation you just gave on the ticket why this fails so that in the future people looking at that doctest understand why. It would also be nice to mention this ticket number in the string, i.e. "the issue was also discussed at #4373".

Mike: FYI since you also had some comments about this code.

Cheers,

Michael



---

archive/issue_comments_032160.json:
```json
{
    "body": "Attachment\n\nok, here it is again, with a more informative comment on the doctest.",
    "created_at": "2008-10-28T14:21:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32160",
    "user": "davidloeffler"
}
```

Attachment

ok, here it is again, with a more informative comment on the doctest.



---

archive/issue_comments_032161.json:
```json
{
    "body": "Two small issues: The explanation should be before the doctest and indented and the '#' in the docstring needs to be escaped. I will take care of both small issues. \n\nCheers,\n\nMichael",
    "created_at": "2008-10-28T15:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32161",
    "user": "mabshoff"
}
```

Two small issues: The explanation should be before the doctest and indented and the '#' in the docstring needs to be escaped. I will take care of both small issues. 

Cheers,

Michael



---

archive/issue_comments_032162.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-28T16:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32162",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032163.json:
```json
{
    "body": "Merged in Sage 3.2.alpha2",
    "created_at": "2008-10-28T16:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4373",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4373#issuecomment-32163",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha2
