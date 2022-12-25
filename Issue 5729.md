# Issue 5729: [with patch, positive review] Cleanup of crystal code: cartan_type now a method rather than attribute

archive/issues_005729.json:
```json
{
    "body": "Assignee: aschillin\n\nCC:  sage-combinat\n\nCrystals: cartan_type is a method\n- Changed the API to have cartan type as a method rather than attribute\n- Systematically use .parent() instead of ._parent\n- Minor doc improvements\n\nIssue created by migration from https://trac.sagemath.org/ticket/5729\n\n",
    "closed_at": "2009-04-11T00:43:56Z",
    "created_at": "2009-04-09T20:07:32Z",
    "labels": [
        "component: combinatorics"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] Cleanup of crystal code: cartan_type now a method rather than attribute",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5729",
    "user": "https://github.com/anneschilling"
}
```
Assignee: aschillin

CC:  sage-combinat

Crystals: cartan_type is a method
- Changed the API to have cartan type as a method rather than attribute
- Systematically use .parent() instead of ._parent
- Minor doc improvements

Issue created by migration from https://trac.sagemath.org/ticket/5729





---

archive/issue_comments_044676.json:
```json
{
    "body": "Attachment [crystal-cleanup-track.patch](tarball://root/attachments/some-uuid/ticket5729/crystal-cleanup-track.patch) by @anneschilling created at 2009-04-10 01:19:31\n\nchanged according to Nicolas' suggestions",
    "created_at": "2009-04-10T01:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44676",
    "user": "https://github.com/anneschilling"
}
```

Attachment [crystal-cleanup-track.patch](tarball://root/attachments/some-uuid/ticket5729/crystal-cleanup-track.patch) by @anneschilling created at 2009-04-10 01:19:31

changed according to Nicolas' suggestions



---

archive/issue_comments_044677.json:
```json
{
    "body": "Attachment [crystal-5729-track.patch](tarball://root/attachments/some-uuid/ticket5729/crystal-5729-track.patch) by @anneschilling created at 2009-04-10 02:09:14",
    "created_at": "2009-04-10T02:09:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44677",
    "user": "https://github.com/anneschilling"
}
```

Attachment [crystal-5729-track.patch](tarball://root/attachments/some-uuid/ticket5729/crystal-5729-track.patch) by @anneschilling created at 2009-04-10 02:09:14



---

archive/issue_comments_044678.json:
```json
{
    "body": "Attachment [crystal-5729-track.2.patch](tarball://root/attachments/some-uuid/ticket5729/crystal-5729-track.2.patch) by @nthiery created at 2009-04-10 05:49:20\n\nFinal version of the patch uploaded:\n- fixes 2/3 remaining calls to parent() \n- Micro doc improvements",
    "created_at": "2009-04-10T05:49:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44678",
    "user": "https://github.com/nthiery"
}
```

Attachment [crystal-5729-track.2.patch](tarball://root/attachments/some-uuid/ticket5729/crystal-5729-track.2.patch) by @nthiery created at 2009-04-10 05:49:20

Final version of the patch uploaded:
- fixes 2/3 remaining calls to parent() 
- Micro doc improvements



---

archive/issue_events_013448.json:
```json
{
    "actor": "https://github.com/anneschilling",
    "created_at": "2009-04-10T23:52:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5729#event-13448"
}
```



---

archive/issue_comments_044679.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-10T23:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44679",
    "user": "https://github.com/anneschilling"
}
```

Resolution: fixed



---

archive/issue_comments_044680.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-04-10T23:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44680",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_044681.json:
```json
{
    "body": "Huh? This ticket has not been merged.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-10T23:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44681",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Huh? This ticket has not been merged.

Cheers,

Michael



---

archive/issue_comments_044682.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-04-10T23:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44682",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_events_013449.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-10T23:58:52Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5729#event-13449"
}
```



---

archive/issue_events_013450.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-11T00:43:56Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5729#event-13450"
}
```



---

archive/issue_comments_044683.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-11T00:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44683",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_044684.json:
```json
{
    "body": "Merged crystal-5729-track.2.patch in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-11T00:43:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5729",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5729#issuecomment-44684",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged crystal-5729-track.2.patch in Sage 3.4.1.rc2.

Cheers,

Michael
