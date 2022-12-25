# Issue 5491: sylow_subgroup gives syntax error

archive/issues_005491.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @orlitzky\n\nKeywords: sylow_subgroup PSL\n\nThis gives a syntax error:\n\nPSL(8,2).sylow_subgroup(7)\n\nI attach a file showing the details.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5491\n\n",
    "closed_at": "2012-03-04T21:19:59Z",
    "created_at": "2009-03-11T22:33:28Z",
    "labels": [
        "component: interfaces",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.0",
    "title": "sylow_subgroup gives syntax error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5491",
    "user": "https://github.com/DanGrayson"
}
```
Assignee: @aghitza

CC:  @orlitzky

Keywords: sylow_subgroup PSL

This gives a syntax error:

PSL(8,2).sylow_subgroup(7)

I attach a file showing the details.


Issue created by migration from https://trac.sagemath.org/ticket/5491





---

archive/issue_events_012845.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-11T23:21:22Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "milestone": "sage-3.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5491#event-12845"
}
```



---

archive/issue_comments_042562.json:
```json
{
    "body": "Attachment [c](tarball://root/attachments/some-uuid/ticket5491/c) by mabshoff created at 2009-03-11 23:21:22",
    "created_at": "2009-03-11T23:21:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42562",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [c](tarball://root/attachments/some-uuid/ticket5491/c) by mabshoff created at 2009-03-11 23:21:22



---

archive/issue_comments_042563.json:
```json
{
    "body": "Yep, this is bizrre:\n\n```\nsage: PSL(4,2).sylow_subgroup(7)\nPermutation Group with generators [(2,10,12,15,4,9,7)(3,11,13,14,5,8,6)]\nsage: PSL(5,2).sylow_subgroup(7)\nPermutation Group with generators [(4,30,10,13,16,25,23)(5,31,11,12,17,24,22)(6,28,8,15,18,27,21)(7,29,9,14,19,26,20)]\nsage: PSL(6,2).sylow_subgroup(7)\nPermutation Group with generators [(1,13,56,21,44,52,32)(3,15,58,23,46,54,34)(4,8,61,16,41,49,37)(6,10,63,18,43,51,39)(9,48,40,60,29,17,36)(11,50,42,62,31,19,38)(12,53,45,57,24,20,33)(14,55,47,59,26,22,35), (1,29,26,4,31,6,3)(2,28,7,30,27,25,5)(8,19,10,15,13,17,22)(9,14,16,11,18,23,21)(32,60,59,37,62,39,34)(35,61,38,63,58,56,36)(40,47,49,42,51,54,52)(41,50,43,46,44,48,55)]\nsage: PSL(7,2).sylow_subgroup(7)\nPermutation Group with generators [(2,5,53,110,50,94,105)(3,4,52,111,51,95,104)(6,49,90,93,109,54,106)(7,48,91,92,108,55,107)(8,63,84,83,99,56,100)(9,62,85,82,98,57,101)(10,58,97,61,81,102,13)(11,59,96,60,80,103,12)(16,23,39,124,32,76,123)(17,22,38,125,33,77,122)(20,35,72,79,127,36,120)(21,34,73,78,126,37,121)(24,40,115,47,67,116,31)(25,41,114,46,66,117,30)(26,45,70,65,113,42,118)(27,44,71,64,112,43,119), (2,9,114,65,34,61,38)(3,8,115,64,35,60,39)(4,63,47,112,72,80,124)(5,62,46,113,73,81,125)(6,54,93,49,106,109,90)(7,55,92,48,107,108,91)(10,122,50,98,30,26,37)(11,123,51,99,31,27,36)(12,76,111,83,116,119,127)(13,77,110,82,117,118,126)(14,69,29,18,86,74,89)(15,68,28,19,87,75,88)(16,95,56,24,44,120,59)(17,94,57,25,45,121,58)(20,96,23,104,100,40,71)(21,97,22,105,101,41,70)(32,52,84,67,43,79,103)(33,53,85,66,42,78,102)]\nsage: PSL(8,2).sylow_subgroup(7)\n------------------------------------------------------------\n   File \"<string>\", line 1\n     [(8,41,52,61,21,32,28,),(9,40,53,60,20,33,29,),(10,43,54,63,23,34,30,),(11,42,55,62,22,35,31,),(12,45,48,57,17,36,24,),(13,44,49,56,16,37,25,),(14,47,50,59,19,38,26,),(15,46,51,58,18,39,27,),(72,105,116,125,85,96,92,),(73,104,117,124,84,97,93,),(74,107,118,127,87,98,94,),(75,106,119,126,86,99,95,),(76,109,112,121,81,100,88,),(77,108,113,120,80,101,89,),(78,111,114,123,83,102,90,),(79,110,115,122,82,103,91,),(128,137,161,148,168,188,157,),(129,136,160,149,169,189,156,),(130,139,163,150,170,190,159,),(131,138,162,151,171,191,158,),(132,141,165,144,172,184,153,),(133,140,164,145,173,185,152,),(134,143,167,146,174,186,155,),(135,142,166,147,175,187,154,),(192,201,225,212,232,252,221,),(193,200,224,213,233,253,220,),(194,203,227,214,234,254,223,),(195,202,226,215,235,255,222,),(196,205,229,208,236,248,217,),([...],)]\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^\nSyntaxError: invalid syntax\n\nsage: \n```",
    "created_at": "2009-03-12T01:44:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42563",
    "user": "https://github.com/wdjoyner"
}
```

Yep, this is bizrre:

```
sage: PSL(4,2).sylow_subgroup(7)
Permutation Group with generators [(2,10,12,15,4,9,7)(3,11,13,14,5,8,6)]
sage: PSL(5,2).sylow_subgroup(7)
Permutation Group with generators [(4,30,10,13,16,25,23)(5,31,11,12,17,24,22)(6,28,8,15,18,27,21)(7,29,9,14,19,26,20)]
sage: PSL(6,2).sylow_subgroup(7)
Permutation Group with generators [(1,13,56,21,44,52,32)(3,15,58,23,46,54,34)(4,8,61,16,41,49,37)(6,10,63,18,43,51,39)(9,48,40,60,29,17,36)(11,50,42,62,31,19,38)(12,53,45,57,24,20,33)(14,55,47,59,26,22,35), (1,29,26,4,31,6,3)(2,28,7,30,27,25,5)(8,19,10,15,13,17,22)(9,14,16,11,18,23,21)(32,60,59,37,62,39,34)(35,61,38,63,58,56,36)(40,47,49,42,51,54,52)(41,50,43,46,44,48,55)]
sage: PSL(7,2).sylow_subgroup(7)
Permutation Group with generators [(2,5,53,110,50,94,105)(3,4,52,111,51,95,104)(6,49,90,93,109,54,106)(7,48,91,92,108,55,107)(8,63,84,83,99,56,100)(9,62,85,82,98,57,101)(10,58,97,61,81,102,13)(11,59,96,60,80,103,12)(16,23,39,124,32,76,123)(17,22,38,125,33,77,122)(20,35,72,79,127,36,120)(21,34,73,78,126,37,121)(24,40,115,47,67,116,31)(25,41,114,46,66,117,30)(26,45,70,65,113,42,118)(27,44,71,64,112,43,119), (2,9,114,65,34,61,38)(3,8,115,64,35,60,39)(4,63,47,112,72,80,124)(5,62,46,113,73,81,125)(6,54,93,49,106,109,90)(7,55,92,48,107,108,91)(10,122,50,98,30,26,37)(11,123,51,99,31,27,36)(12,76,111,83,116,119,127)(13,77,110,82,117,118,126)(14,69,29,18,86,74,89)(15,68,28,19,87,75,88)(16,95,56,24,44,120,59)(17,94,57,25,45,121,58)(20,96,23,104,100,40,71)(21,97,22,105,101,41,70)(32,52,84,67,43,79,103)(33,53,85,66,42,78,102)]
sage: PSL(8,2).sylow_subgroup(7)
------------------------------------------------------------
   File "<string>", line 1
     [(8,41,52,61,21,32,28,),(9,40,53,60,20,33,29,),(10,43,54,63,23,34,30,),(11,42,55,62,22,35,31,),(12,45,48,57,17,36,24,),(13,44,49,56,16,37,25,),(14,47,50,59,19,38,26,),(15,46,51,58,18,39,27,),(72,105,116,125,85,96,92,),(73,104,117,124,84,97,93,),(74,107,118,127,87,98,94,),(75,106,119,126,86,99,95,),(76,109,112,121,81,100,88,),(77,108,113,120,80,101,89,),(78,111,114,123,83,102,90,),(79,110,115,122,82,103,91,),(128,137,161,148,168,188,157,),(129,136,160,149,169,189,156,),(130,139,163,150,170,190,159,),(131,138,162,151,171,191,158,),(132,141,165,144,172,184,153,),(133,140,164,145,173,185,152,),(134,143,167,146,174,186,155,),(135,142,166,147,175,187,154,),(192,201,225,212,232,252,221,),(193,200,224,213,233,253,220,),(194,203,227,214,234,254,223,),(195,202,226,215,235,255,222,),(196,205,229,208,236,248,217,),([...],)]
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ^
SyntaxError: invalid syntax

sage: 
```



---

archive/issue_comments_042564.json:
```json
{
    "body": "Changing assignee from tbd to @aghitza.",
    "created_at": "2009-03-12T05:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42564",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from tbd to @aghitza.



---

archive/issue_comments_042565.json:
```json
{
    "body": "This is due to GAP's default behaviour, which is to truncate output that it deems too long to print.  In this particular case, the generators of the Sylow subgroup are *huge* permutations, so GAP gets bored and sticks in a [...] at some point.\n\nThis could potentially come up in other situations in dealing with the GAP interface.",
    "created_at": "2009-03-12T05:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42565",
    "user": "https://github.com/aghitza"
}
```

This is due to GAP's default behaviour, which is to truncate output that it deems too long to print.  In this particular case, the generators of the Sylow subgroup are *huge* permutations, so GAP gets bored and sticks in a [...] at some point.

This could potentially come up in other situations in dealing with the GAP interface.



---

archive/issue_comments_042566.json:
```json
{
    "body": "Changing keywords from \"sylow_subgoup PSL\" to \"sylow_subgroup PSL\".",
    "created_at": "2009-03-12T05:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42566",
    "user": "https://github.com/aghitza"
}
```

Changing keywords from "sylow_subgoup PSL" to "sylow_subgroup PSL".



---

archive/issue_comments_042567.json:
```json
{
    "body": "Changing component from algebra to interfaces.",
    "created_at": "2009-03-12T05:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42567",
    "user": "https://github.com/aghitza"
}
```

Changing component from algebra to interfaces.



---

archive/issue_comments_042568.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-12T05:37:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42568",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_042569.json:
```json
{
    "body": "A doctest to confirm that this is fixed.",
    "created_at": "2012-01-07T03:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42569",
    "user": "https://github.com/orlitzky"
}
```

A doctest to confirm that this is fixed.



---

archive/issue_comments_042570.json:
```json
{
    "body": "Attachment [sage-trac_5491.patch](tarball://root/attachments/some-uuid/ticket5491/sage-trac_5491.patch) by @orlitzky created at 2012-01-07 03:09:13\n\nThis is already fixed. I created a doctest to test that,\n\n```\nPSL(10,2).sylow_subgroup(7)\n```\n\ndoes not crash.",
    "created_at": "2012-01-07T03:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42570",
    "user": "https://github.com/orlitzky"
}
```

Attachment [sage-trac_5491.patch](tarball://root/attachments/some-uuid/ticket5491/sage-trac_5491.patch) by @orlitzky created at 2012-01-07 03:09:13

This is already fixed. I created a doctest to test that,

```
PSL(10,2).sylow_subgroup(7)
```

does not crash.



---

archive/issue_comments_042571.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-01-07T03:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42571",
    "user": "https://github.com/orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_042572.json:
```json
{
    "body": "Is that a positive review, or are you still working on it?",
    "created_at": "2012-02-25T20:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42572",
    "user": "https://github.com/orlitzky"
}
```

Is that a positive review, or are you still working on it?



---

archive/issue_comments_042573.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-02-25T23:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42573",
    "user": "https://github.com/dkrenn"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042574.json:
```json
{
    "body": "Replying to [comment:7 mjo]:\n> Is that a positive review, or are you still working on it?\n\nNo, it wasn't. I waited for answers in [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8499ccf849b7833a/2c3678a00cd47447?show_docid=2c3678a00cd47447&pli=1) since one of the patchbots produced a \"failed\".\n\nNow everything should be fine.",
    "created_at": "2012-02-25T23:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42574",
    "user": "https://github.com/dkrenn"
}
```

Replying to [comment:7 mjo]:
> Is that a positive review, or are you still working on it?

No, it wasn't. I waited for answers in [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/8499ccf849b7833a/2c3678a00cd47447?show_docid=2c3678a00cd47447&pli=1) since one of the patchbots produced a "failed".

Now everything should be fine.



---

archive/issue_comments_042575.json:
```json
{
    "body": "Ok, thanks!",
    "created_at": "2012-02-25T23:27:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42575",
    "user": "https://github.com/orlitzky"
}
```

Ok, thanks!



---

archive/issue_events_012846.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-03-04T21:19:59Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5491#event-12846"
}
```



---

archive/issue_comments_042576.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-03-04T21:19:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5491",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5491#issuecomment-42576",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
