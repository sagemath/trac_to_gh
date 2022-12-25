# Issue 4064: [with new patch, positive review] pari precision issues

archive/issues_004064.json:
```json
{
    "body": "Assignee: @williamstein\n\nJohn Cremona found this:\n\n```\nsage: E = EllipticCurve('37a')                     \nsage: E.period_lattice().basis(prec=30)[0].parent()\nReal Field with 896 bits of precision\nsage: E.period_lattice().basis(prec=100)[0].parent()\nReal Field with 3136 bits of precision\n```\n\nSo we ask for 30 decimal digits of precision (which should be about 100 bits), and pari (apparently) gives us 896 bits.  Or we ask for 100 decimal digits (about 333 bits), and we get 3136 bits.  This probably has nothing to do with elliptic curves, but rather with the pari interface.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4064\n\n",
    "closed_at": "2008-09-08T19:42:18Z",
    "created_at": "2008-09-04T23:34:40Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "[with new patch, positive review] pari precision issues",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4064",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

John Cremona found this:

```
sage: E = EllipticCurve('37a')                     
sage: E.period_lattice().basis(prec=30)[0].parent()
Real Field with 896 bits of precision
sage: E.period_lattice().basis(prec=100)[0].parent()
Real Field with 3136 bits of precision
```

So we ask for 30 decimal digits of precision (which should be about 100 bits), and pari (apparently) gives us 896 bits.  Or we ask for 100 decimal digits (about 333 bits), and we get 3136 bits.  This probably has nothing to do with elliptic curves, but rather with the pari interface.

Issue created by migration from https://trac.sagemath.org/ticket/4064





---

archive/issue_comments_029254.json:
```json
{
    "body": "Replying to [ticket:4064 AlexGhitza]:\n> John Cremona found this:\n> \n> \n> ```\n> sage: E = EllipticCurve('37a')                     \n> sage: E.period_lattice().basis(prec=30)[0].parent()\n> Real Field with 896 bits of precision\n> sage: E.period_lattice().basis(prec=100)[0].parent()\n> Real Field with 3136 bits of precision\n> ```\n> \n> So we ask for 30 decimal digits of precision (which should be about 100 bits), and pari (apparently) gives us 896 bits.  Or we ask for 100 decimal digits (about 333 bits), and we get 3136 bits.  This probably has nothing to do with elliptic curves, but rather with the pari interface.\n\n\nIn fact when I rewrote the precision-handling in period lattice functions, I intended the prec parameter to be Sage-precision (in bits) and not pari-precision (in digits).  I suggested on sage-devel that if parameters represent decimal precision their name should reflect that and be called (for example) prec10.\n\nThis does not alter the substance of this ticket, and I hope to look into it today.",
    "created_at": "2008-09-05T08:14:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29254",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [ticket:4064 AlexGhitza]:
> John Cremona found this:
> 
> 
> ```
> sage: E = EllipticCurve('37a')                     
> sage: E.period_lattice().basis(prec=30)[0].parent()
> Real Field with 896 bits of precision
> sage: E.period_lattice().basis(prec=100)[0].parent()
> Real Field with 3136 bits of precision
> ```
> 
> So we ask for 30 decimal digits of precision (which should be about 100 bits), and pari (apparently) gives us 896 bits.  Or we ask for 100 decimal digits (about 333 bits), and we get 3136 bits.  This probably has nothing to do with elliptic curves, but rather with the pari interface.


In fact when I rewrote the precision-handling in period lattice functions, I intended the prec parameter to be Sage-precision (in bits) and not pari-precision (in digits).  I suggested on sage-devel that if parameters represent decimal precision their name should reflect that and be called (for example) prec10.

This does not alter the substance of this ticket, and I hope to look into it today.



---

archive/issue_comments_029255.json:
```json
{
    "body": "I actually figured out what's wrong and fixed it today, but I haven't had time to write doctests.  I will try to get to it soon and post a patch.",
    "created_at": "2008-09-05T11:36:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29255",
    "user": "https://github.com/aghitza"
}
```

I actually figured out what's wrong and fixed it today, but I haven't had time to write doctests.  I will try to get to it soon and post a patch.



---

archive/issue_comments_029256.json:
```json
{
    "body": "Replying to [comment:2 AlexGhitza]:\n> I actually figured out what's wrong and fixed it today, but I haven't had time to write doctests.  I will try to get to it soon and post a patch.\n\n\nAlex, please tell me what you have done a.s.a.p. since I have looking into this in some detail too...\n\nThe main point is that converting from pari to Sage using .python() has a precision parameter which is *not* the desired Sage precision, and in fact is a useless parameter since it changes the precision of the pari object, which is rather a stupid thing to do after the object has been created.  Add to that the fact that there are at least *three* different precision scales in ues (bits, digits, and words) and we can see how it is easy for the precision to suddenly go up by a factor of 32 or 64!",
    "created_at": "2008-09-05T13:04:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29256",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:2 AlexGhitza]:
> I actually figured out what's wrong and fixed it today, but I haven't had time to write doctests.  I will try to get to it soon and post a patch.


Alex, please tell me what you have done a.s.a.p. since I have looking into this in some detail too...

The main point is that converting from pari to Sage using .python() has a precision parameter which is *not* the desired Sage precision, and in fact is a useless parameter since it changes the precision of the pari object, which is rather a stupid thing to do after the object has been created.  Add to that the fact that there are at least *three* different precision scales in ues (bits, digits, and words) and we can see how it is easy for the precision to suddenly go up by a factor of 32 or 64!



---

archive/issue_comments_029257.json:
```json
{
    "body": "Attachment [4064-ell_pari_precision.patch](tarball://root/attachments/some-uuid/ticket4064/4064-ell_pari_precision.patch) by @aghitza created at 2008-09-06 11:14:19",
    "created_at": "2008-09-06T11:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29257",
    "user": "https://github.com/aghitza"
}
```

Attachment [4064-ell_pari_precision.patch](tarball://root/attachments/some-uuid/ticket4064/4064-ell_pari_precision.patch) by @aghitza created at 2008-09-06 11:14:19



---

archive/issue_comments_029258.json:
```json
{
    "body": "Phew!\n\nThe patch fixes the issues reported here and some of those brought up by John Cremona at http://groups.google.com/group/sage-devel/browse_thread/thread/128a780383c44ce0\n\nThere has been a lot of movement in this area of the code between alpha4 and rc0.  The patch is currently based on alpha4 + patches from #3377, #1115, #3954, and #4023.  (I realize that this makes it more trouble to review, but it will make it easier to apply to rc0 once that's out).\n\nThere is one doctest failure that I am aware of, in ell_number_field.py (I'll try to sort it out tomorrow if nobody beats me to it).",
    "created_at": "2008-09-06T11:14:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29258",
    "user": "https://github.com/aghitza"
}
```

Phew!

The patch fixes the issues reported here and some of those brought up by John Cremona at http://groups.google.com/group/sage-devel/browse_thread/thread/128a780383c44ce0

There has been a lot of movement in this area of the code between alpha4 and rc0.  The patch is currently based on alpha4 + patches from #3377, #1115, #3954, and #4023.  (I realize that this makes it more trouble to review, but it will make it easier to apply to rc0 once that's out).

There is one doctest failure that I am aware of, in ell_number_field.py (I'll try to sort it out tomorrow if nobody beats me to it).



---

archive/issue_comments_029259.json:
```json
{
    "body": "Great work, Alex!  I will get to work reviewing what you have done.\n\nQuick idea:  instead of having all these doctests requiring different expected answers for 32 vs.64 bit, why don't we automatically initialise pari on *both* 32- and 64-bit machines to the same precision, say 38 decimals?  (Or 19, which makes sense for both, if we want to be faster).\n\nI can never work out what time of day it is for you, but I hope to work on this on Saturday afternoon.",
    "created_at": "2008-09-06T11:43:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29259",
    "user": "https://github.com/JohnCremona"
}
```

Great work, Alex!  I will get to work reviewing what you have done.

Quick idea:  instead of having all these doctests requiring different expected answers for 32 vs.64 bit, why don't we automatically initialise pari on *both* 32- and 64-bit machines to the same precision, say 38 decimals?  (Or 19, which makes sense for both, if we want to be faster).

I can never work out what time of day it is for you, but I hope to work on this on Saturday afternoon.



---

archive/issue_comments_029260.json:
```json
{
    "body": "I successfully applied the whole sequence of patches ending with 4064-ell_pari_precision.patch to fresh 3.1.2.alpha4 builds on two machines, a 32-bit and a 64-bit.  \n\nTesting all of sage.schemes.elliptic_curves, the only failure on 32-bit was (as Alex reported) in ell_number_field.py:\n\n```\nFile \"/home/jec/sage-current/tmp/ell_number_field.py\", line 1133:\n    sage: L.basis(prec=10)\nExpected:\n    (4.1310718527050167743096955262475367...,\n    -2.0655359263525083871548477631237683... + 0.98863042446910777236901069433960633...*I)\nGot:\n    (4.13107185270501677, -2.06553592635250838 + 0.988630424469107772*I)\n```\n\nOn the 64-bit I also had stuff in period_lattice.py and in ell_rational_field.py this:\n\n```\nFile \"/home/jec/sage-current/tmp/ell_rational_field.py\", line 448:\n    sage: [a.precision() for a in E]\nExpected:\n    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4]\nGot:\n    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3]\n```\n\nThis is just on account of differing behaviour on 64-bit machines which Alex had not tested, so I'll edit the doctests accorsingly and come back with an additional patch.",
    "created_at": "2008-09-06T16:18:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29260",
    "user": "https://github.com/JohnCremona"
}
```

I successfully applied the whole sequence of patches ending with 4064-ell_pari_precision.patch to fresh 3.1.2.alpha4 builds on two machines, a 32-bit and a 64-bit.  

Testing all of sage.schemes.elliptic_curves, the only failure on 32-bit was (as Alex reported) in ell_number_field.py:

```
File "/home/jec/sage-current/tmp/ell_number_field.py", line 1133:
    sage: L.basis(prec=10)
Expected:
    (4.1310718527050167743096955262475367...,
    -2.0655359263525083871548477631237683... + 0.98863042446910777236901069433960633...*I)
Got:
    (4.13107185270501677, -2.06553592635250838 + 0.988630424469107772*I)
```

On the 64-bit I also had stuff in period_lattice.py and in ell_rational_field.py this:

```
File "/home/jec/sage-current/tmp/ell_rational_field.py", line 448:
    sage: [a.precision() for a in E]
Expected:
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4]
Got:
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3]
```

This is just on account of differing behaviour on 64-bit machines which Alex had not tested, so I'll edit the doctests accorsingly and come back with an additional patch.



---

archive/issue_comments_029261.json:
```json
{
    "body": "Attachment [4064-ell_pari_precision-1a.patch](tarball://root/attachments/some-uuid/ticket4064/4064-ell_pari_precision-1a.patch) by @JohnCremona created at 2008-09-06 19:31:02",
    "created_at": "2008-09-06T19:31:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29261",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [4064-ell_pari_precision-1a.patch](tarball://root/attachments/some-uuid/ticket4064/4064-ell_pari_precision-1a.patch) by @JohnCremona created at 2008-09-06 19:31:02



---

archive/issue_comments_029262.json:
```json
{
    "body": "The patch 4064-ell_pari_precision-1a.patch (to be applied after 4064-ell_pari_precision.patch) does the following:\n1. Fixes the problem in ell_number_field reported by Alex;\n2. Fixes doctests to work in both 32-and 64-bit (though in fact thanks to Alex's work most functions, apart from a few low-level tests, work identically on both);\n3. Add some fairly minor features in period_lattice.py (e.g. the real_period() function William wanted)\n4. Complete doctests for period_lattice.py\n\nI guess that now we need a review who is neither Alex nor me.  (Note that the dependencies for these two patches have been merged in 3.1.2.rc0 so testing this will be easier after that is released, but it is quite possible to test on 3.1.2.alpha4 if you have the patience to apply 6 previous patches as listed by Alex.)",
    "created_at": "2008-09-06T19:38:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29262",
    "user": "https://github.com/JohnCremona"
}
```

The patch 4064-ell_pari_precision-1a.patch (to be applied after 4064-ell_pari_precision.patch) does the following:
1. Fixes the problem in ell_number_field reported by Alex;
2. Fixes doctests to work in both 32-and 64-bit (though in fact thanks to Alex's work most functions, apart from a few low-level tests, work identically on both);
3. Add some fairly minor features in period_lattice.py (e.g. the real_period() function William wanted)
4. Complete doctests for period_lattice.py

I guess that now we need a review who is neither Alex nor me.  (Note that the dependencies for these two patches have been merged in 3.1.2.rc0 so testing this will be easier after that is released, but it is quite possible to test on 3.1.2.alpha4 if you have the patience to apply 6 previous patches as listed by Alex.)



---

archive/issue_comments_029263.json:
```json
{
    "body": "ok, there's some numeric fuzz in one doctest on 32-bit:\n\n```\nFile \"/home/john/sage-3.1.2.alpha4/tmp/period_lattice.py\", line 281:\n    sage: EllipticCurve('389a1').period_lattice().sigma(CC(2,1))\nExpected:\n    2.609121635701083769 - 0.20086508082458695134*I\nGot:\n    2.609121635701083769 - 0.20086508082458695200*I\n```\nbut I'll leave it for now since there may be more of the same.  That's what comes of adding doctests to functions which have never had them (this files now has 100% coverage!)",
    "created_at": "2008-09-06T19:53:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29263",
    "user": "https://github.com/JohnCremona"
}
```

ok, there's some numeric fuzz in one doctest on 32-bit:

```
File "/home/john/sage-3.1.2.alpha4/tmp/period_lattice.py", line 281:
    sage: EllipticCurve('389a1').period_lattice().sigma(CC(2,1))
Expected:
    2.609121635701083769 - 0.20086508082458695134*I
Got:
    2.609121635701083769 - 0.20086508082458695200*I
```
but I'll leave it for now since there may be more of the same.  That's what comes of adding doctests to functions which have never had them (this files now has 100% coverage!)



---

archive/issue_comments_029264.json:
```json
{
    "body": "apply before the above two patches, on top of pristine 3.1.2.alpha4 (ignore if using rc0)",
    "created_at": "2008-09-06T22:09:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29264",
    "user": "https://github.com/aghitza"
}
```

apply before the above two patches, on top of pristine 3.1.2.alpha4 (ignore if using rc0)



---

archive/issue_comments_029265.json:
```json
{
    "body": "Attachment [4064-prerequisites.patch](tarball://root/attachments/some-uuid/ticket4064/4064-prerequisites.patch) by @aghitza created at 2008-09-06 22:14:53\n\nFor the record, John's patch looks good to me.\n\nIn order to ease the work of whoever might want to look at this before rc0 comes out, I have attached a patch with all the prerequisites listed in the above comments.  So if you're on a 3.1.2.alpha4 and want to check this out, first apply 4064-prerequisites.patch, then the two others from this ticket.  You of course don't have to review any of the changes in 4064-prerequisites.patch, since these have all already been reviewed and merged.\n\nIf you're on rc0 just apply the two first patches.",
    "created_at": "2008-09-06T22:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29265",
    "user": "https://github.com/aghitza"
}
```

Attachment [4064-prerequisites.patch](tarball://root/attachments/some-uuid/ticket4064/4064-prerequisites.patch) by @aghitza created at 2008-09-06 22:14:53

For the record, John's patch looks good to me.

In order to ease the work of whoever might want to look at this before rc0 comes out, I have attached a patch with all the prerequisites listed in the above comments.  So if you're on a 3.1.2.alpha4 and want to check this out, first apply 4064-prerequisites.patch, then the two others from this ticket.  You of course don't have to review any of the changes in 4064-prerequisites.patch, since these have all already been reviewed and merged.

If you're on rc0 just apply the two first patches.



---

archive/issue_comments_029266.json:
```json
{
    "body": "I am also preparing a further patch which is not specifically relevant to elliptic curves, since the pari interface still does some other wrong (and also misleading) things owing to an earlier misunderstanding of the pari precision parameter.  That would have to go after all these, but is separate.  Your 6 functions for converting petween the three precision measures will play an important role!",
    "created_at": "2008-09-06T22:19:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29266",
    "user": "https://github.com/JohnCremona"
}
```

I am also preparing a further patch which is not specifically relevant to elliptic curves, since the pari interface still does some other wrong (and also misleading) things owing to an earlier misunderstanding of the pari precision parameter.  That would have to go after all these, but is separate.  Your 6 functions for converting petween the three precision measures will play an important role!



---

archive/issue_comments_029267.json:
```json
{
    "body": "FYI: doctests pass with the two patches applied on top of rc0 on a 64 bit box. If you two can review each other's patches they will make it into rc1.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-07T02:07:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29267",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

FYI: doctests pass with the two patches applied on top of rc0 on a 64 bit box. If you two can review each other's patches they will make it into rc1.

Cheers,

Michael



---

archive/issue_comments_029268.json:
```json
{
    "body": "I'm happy with John's patch.",
    "created_at": "2008-09-07T02:41:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29268",
    "user": "https://github.com/aghitza"
}
```

I'm happy with John's patch.



---

archive/issue_comments_029269.json:
```json
{
    "body": "Replying to [comment:12 AlexGhitza]:\n> I'm happy with John's patch.\n\n\n.. and I am more than happy with Alex's.  It has been a very good collaborative effort, and knowing that two of us have got to grips with the issue is very good to know.\n\nI'll put the next patch concerning pari precision issues onto a new ticket;  it will certainly depend on all these,",
    "created_at": "2008-09-07T10:26:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29269",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:12 AlexGhitza]:
> I'm happy with John's patch.


.. and I am more than happy with Alex's.  It has been a very good collaborative effort, and knowing that two of us have got to grips with the issue is very good to know.

I'll put the next patch concerning pari precision issues onto a new ticket;  it will certainly depend on all these,



---

archive/issue_comments_029270.json:
```json
{
    "body": "Merged 4064-ell_pari_precision.patch and 4064-ell_pari_precision-1a.patch in Sage 3.1.2.rc1. I had to merge the hunk from lisp.py manually.\n\nCheers,\n\nMichael",
    "created_at": "2008-09-08T19:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29270",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4064-ell_pari_precision.patch and 4064-ell_pari_precision-1a.patch in Sage 3.1.2.rc1. I had to merge the hunk from lisp.py manually.

Cheers,

Michael



---

archive/issue_comments_029271.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-09-08T19:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4064#issuecomment-29271",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_009276.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-09-08T19:42:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4064",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4064#event-9276"
}
```
