# Issue 2928: another p-adic extension segfault

archive/issues_002928.json:
```json
{
    "body": "Assignee: @roed314\n\n\n```\nK.<b> = Qp(13).extension(x^2+x-1)\nfatal error:\n   internal error: can't grow this _ntl_gbigint\nexit...\n/Users/robert/sage/current/local/bin/sage-sage: line 357: 18024 Abort\ntrap              python \"$@\"\n```\n\n\nApplying the patches from #2843 didn't fix this. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2928\n\n",
    "created_at": "2008-04-15T05:49:17Z",
    "labels": [
        "component: number theory",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "another p-adic extension segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2928",
    "user": "https://github.com/robertwb"
}
```
Assignee: @roed314


```
K.<b> = Qp(13).extension(x^2+x-1)
fatal error:
   internal error: can't grow this _ntl_gbigint
exit...
/Users/robert/sage/current/local/bin/sage-sage: line 357: 18024 Abort
trap              python "$@"
```


Applying the patches from #2843 didn't fix this. 

Issue created by migration from https://trac.sagemath.org/ticket/2928





---

archive/issue_comments_020113.json:
```json
{
    "body": "Hi Robert, \n\nmy alpha5 merge tree doesn't experience the problem:\n\n```\nmabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha5$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 3.0.alpha4, Release Date: 2008-04-12                  |\n| Type notebook() for the GUI, and license() for information.        |\nsage: K.<b> = Qp(13).extension(x^2+x-1)\nsage:\n```\n\nI would suggest you wait for alpha5 [out once I merge #2927, #2929 and the LinBox.spkg update not yet in trac] and then verify that it works for you, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T05:56:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20113",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Robert, 

my alpha5 merge tree doesn't experience the problem:

```
mabshoff@sage:/scratch/mabshoff/release-cycle/sage-3.0.alpha5$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 3.0.alpha4, Release Date: 2008-04-12                  |
| Type notebook() for the GUI, and license() for information.        |
sage: K.<b> = Qp(13).extension(x^2+x-1)
sage:
```

I would suggest you wait for alpha5 [out once I merge #2927, #2929 and the LinBox.spkg update not yet in trac] and then verify that it works for you, too.

Cheers,

Michael



---

archive/issue_events_003128.json:
```json
{
    "actor": "https://github.com/kedlaya",
    "created_at": "2008-04-15T11:14:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2928#event-3128"
}
```



---

archive/issue_comments_020114.json:
```json
{
    "body": "This is fixed in my alpha4 tree (which also has #2903 and #2928 applied):\n\n```\nsage: K.<b> = Qp(13).extension(x^2+x-1)\nsage: print K\nUnramified Extension of 13-adic Field with capped relative precision 20 in b defined by (1 + O(13^20))*x^2 + (1 + O(13^20))*x + (12 + 12*13 + 12*13^2 + 12*13^3 + 12*13^4 + 12*13^5 + 12*13^6 + 12*13^7 + 12*13^8 + 12*13^9 + 12*13^10 + 12*13^11 + 12*13^12 + 12*13^13 + 12*13^14 + 12*13^15 + 12*13^16 + 12*13^17 + 12*13^18 + 12*13^19 + O(13^20))\n```\n\nso this ticket is being closed.",
    "created_at": "2008-04-15T11:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20114",
    "user": "https://github.com/kedlaya"
}
```

This is fixed in my alpha4 tree (which also has #2903 and #2928 applied):

```
sage: K.<b> = Qp(13).extension(x^2+x-1)
sage: print K
Unramified Extension of 13-adic Field with capped relative precision 20 in b defined by (1 + O(13^20))*x^2 + (1 + O(13^20))*x + (12 + 12*13 + 12*13^2 + 12*13^3 + 12*13^4 + 12*13^5 + 12*13^6 + 12*13^7 + 12*13^8 + 12*13^9 + 12*13^10 + 12*13^11 + 12*13^12 + 12*13^13 + 12*13^14 + 12*13^15 + 12*13^16 + 12*13^17 + 12*13^18 + 12*13^19 + O(13^20))
```

so this ticket is being closed.



---

archive/issue_comments_020115.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-15T11:14:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20115",
    "user": "https://github.com/kedlaya"
}
```

Resolution: fixed



---

archive/issue_comments_020116.json:
```json
{
    "body": "This is apparently not fixed for robertwb, and it's not fixed for me either on 32-bit Ubuntu, so this ticket is being reopened. (In my previous comment, #2928 should of course have been #2843.)",
    "created_at": "2008-04-16T11:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20116",
    "user": "https://github.com/kedlaya"
}
```

This is apparently not fixed for robertwb, and it's not fixed for me either on 32-bit Ubuntu, so this ticket is being reopened. (In my previous comment, #2928 should of course have been #2843.)



---

archive/issue_comments_020117.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-16T11:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20117",
    "user": "https://github.com/kedlaya"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_020118.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-16T11:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20118",
    "user": "https://github.com/kedlaya"
}
```

Changing status from closed to reopened.



---

archive/issue_events_003129.json:
```json
{
    "actor": "https://github.com/kedlaya",
    "created_at": "2008-04-16T11:27:27Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2928#event-3129"
}
```



---

archive/issue_comments_020119.json:
```json
{
    "body": "`PowComputer_ZZ_pX_small.__new__` has a `ZZ_pX_c tmp` that gets used a number of times. It seems that the `ZZ_p`'s that are allocated for the coefficients of `tmp` the first time it is used have non-resizable storage. On a 32-bit machine this fixed size turns out to be too small for one of the later uses of `tmp`, causing the reported error message.\n\nIt's too late at night for me to write a patch for this now, but I'll probably take a shot at it tomorrow unless somebody else wants to.",
    "created_at": "2008-04-20T00:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20119",
    "user": "https://github.com/wjp"
}
```

`PowComputer_ZZ_pX_small.__new__` has a `ZZ_pX_c tmp` that gets used a number of times. It seems that the `ZZ_p`'s that are allocated for the coefficients of `tmp` the first time it is used have non-resizable storage. On a 32-bit machine this fixed size turns out to be too small for one of the later uses of `tmp`, causing the reported error message.

It's too late at night for me to write a patch for this now, but I'll probably take a shot at it tomorrow unless somebody else wants to.



---

archive/issue_comments_020120.json:
```json
{
    "body": "To expand on this a little bit, I think that the right way to fix it is making `ZZ_pX_conv_modulus` re-allocate its `fout` argument if necessary.",
    "created_at": "2008-04-20T01:06:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20120",
    "user": "https://github.com/wjp"
}
```

To expand on this a little bit, I think that the right way to fix it is making `ZZ_pX_conv_modulus` re-allocate its `fout` argument if necessary.



---

archive/issue_comments_020121.json:
```json
{
    "body": "Attachment [padics_tmp_coeff_size.patch](tarball://root/attachments/some-uuid/ticket2928/padics_tmp_coeff_size.patch) by @wjp created at 2008-04-20 13:19:25",
    "created_at": "2008-04-20T13:19:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20121",
    "user": "https://github.com/wjp"
}
```

Attachment [padics_tmp_coeff_size.patch](tarball://root/attachments/some-uuid/ticket2928/padics_tmp_coeff_size.patch) by @wjp created at 2008-04-20 13:19:25



---

archive/issue_comments_020122.json:
```json
{
    "body": "Attachment [padics_tmp_coeff_size.2.patch](tarball://root/attachments/some-uuid/ticket2928/padics_tmp_coeff_size.2.patch) by @wjp created at 2008-04-20 13:39:07",
    "created_at": "2008-04-20T13:39:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20122",
    "user": "https://github.com/wjp"
}
```

Attachment [padics_tmp_coeff_size.2.patch](tarball://root/attachments/some-uuid/ticket2928/padics_tmp_coeff_size.2.patch) by @wjp created at 2008-04-20 13:39:07



---

archive/issue_comments_020123.json:
```json
{
    "body": "Following the suggestion from Roed on IRC, the attached patch allocates `ZZ_pX tmp` with large enough coefficient size to handle all moduli.\n\nDone for both `PowComputer_ZZ_pX_small` and `PowComputer_ZZ_pX_big`.\n\n(Please ignore the first patch (it broke `_big`), and only apply/review the second.)",
    "created_at": "2008-04-20T13:42:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20123",
    "user": "https://github.com/wjp"
}
```

Following the suggestion from Roed on IRC, the attached patch allocates `ZZ_pX tmp` with large enough coefficient size to handle all moduli.

Done for both `PowComputer_ZZ_pX_small` and `PowComputer_ZZ_pX_big`.

(Please ignore the first patch (it broke `_big`), and only apply/review the second.)



---

archive/issue_comments_020124.json:
```json
{
    "body": "Applied against 3.0.rc0, this fixes the problem on my 32-bit machine (where I was able to replicate the problem before). It seems like a pretty clean way to do it without imposing a serious performance hit. Positive review.",
    "created_at": "2008-04-20T22:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20124",
    "user": "https://github.com/kedlaya"
}
```

Applied against 3.0.rc0, this fixes the problem on my 32-bit machine (where I was able to replicate the problem before). It seems like a pretty clean way to do it without imposing a serious performance hit. Positive review.



---

archive/issue_events_003130.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-21T00:37:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2928#event-3130"
}
```



---

archive/issue_comments_020125.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T00:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20125",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020126.json:
```json
{
    "body": "Merged padics_tmp_coeff_size.2.patch in Sage 3.0.rc1",
    "created_at": "2008-04-21T00:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2928#issuecomment-20126",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged padics_tmp_coeff_size.2.patch in Sage 3.0.rc1
