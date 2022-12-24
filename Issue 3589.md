# Issue 3589: numerical noise -- number_field.py

archive/issues_003589.json:
```json
{
    "body": "Assignee: failure\n\n\n```\nsage -t  devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/home/mariah/sage/sage-3.0.4.alpha2-x86-Linux-fc8/tmp/number_field.py\",\nline 3630:\n   sage: K.embeddings(CC)\nExpected:\n   [\n   Ring morphism:\n     From: Number Field in a with defining polynomial x^3 - 2\n     To:   Complex Field with 53 bits of precision\n     Defn: a |--> -0.629960524947436 - 1.09112363597172*I,\n   Ring morphism:\n     From: Number Field in a with defining polynomial x^3 - 2\n     To:   Complex Field with 53 bits of precision\n     Defn: a |--> -0.629960524947436 + 1.09112363597172*I,\n   Ring morphism:\n     From: Number Field in a with defining polynomial x^3 - 2\n     To:   Complex Field with 53 bits of precision\n     Defn: a |--> 1.25992104989487\n   ]\nGot:\n   [\n   Ring morphism:\n     From: Number Field in a with defining polynomial x^3 - 2\n     To:   Complex Field with 53 bits of precision\n     Defn: a |--> -0.629960524947437 - 1.09112363597172*I,\n   Ring morphism:\n     From: Number Field in a with defining polynomial x^3 - 2\n     To:   Complex Field with 53 bits of precision\n     Defn: a |--> -0.629960524947437 + 1.09112363597172*I,\n   Ring morphism:\n     From: Number Field in a with defining polynomial x^3 - 2\n     To:   Complex Field with 53 bits of precision\n     Defn: a |--> 1.25992104989487\n   ]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3589\n\n",
    "created_at": "2008-07-07T20:31:16Z",
    "labels": [
        "doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.4",
    "title": "numerical noise -- number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3589",
    "user": "@williamstein"
}
```
Assignee: failure


```
sage -t  devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/home/mariah/sage/sage-3.0.4.alpha2-x86-Linux-fc8/tmp/number_field.py",
line 3630:
   sage: K.embeddings(CC)
Expected:
   [
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947436 - 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947436 + 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> 1.25992104989487
   ]
Got:
   [
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947437 - 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> -0.629960524947437 + 1.09112363597172*I,
   Ring morphism:
     From: Number Field in a with defining polynomial x^3 - 2
     To:   Complex Field with 53 bits of precision
     Defn: a |--> 1.25992104989487
   ]
```


Issue created by migration from https://trac.sagemath.org/ticket/3589





---

archive/issue_comments_025363.json:
```json
{
    "body": "This is all mine!\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T20:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25363",
    "user": "mabshoff"
}
```

This is all mine!

Cheers,

Michael



---

archive/issue_comments_025364.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-07-07T20:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25364",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_025365.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-07-07T20:33:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25365",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_025366.json:
```json
{
    "body": "Attachment [sage-3589.patch](tarball://root/attachments/some-uuid/ticket3589/sage-3589.patch) by @williamstein created at 2008-07-07 21:54:23",
    "created_at": "2008-07-07T21:54:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25366",
    "user": "@williamstein"
}
```

Attachment [sage-3589.patch](tarball://root/attachments/some-uuid/ticket3589/sage-3589.patch) by @williamstein created at 2008-07-07 21:54:23



---

archive/issue_comments_025367.json:
```json
{
    "body": "Looks good. Would it be safer to kill a few more digits, just to prevent having a similar ticket at some point?",
    "created_at": "2008-07-07T21:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25367",
    "user": "@craigcitro"
}
```

Looks good. Would it be safer to kill a few more digits, just to prevent having a similar ticket at some point?



---

archive/issue_comments_025368.json:
```json
{
    "body": "Replying to [comment:3 craigcitro]:\n> Looks good. Would it be safer to kill a few more digits, just to prevent having a similar ticket at some point?\n\nNo, we should only kill the digits needed, not any more. Otherwise numeric stability would go out the window :)\n\nCheers,\n\nMichael",
    "created_at": "2008-07-07T21:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25368",
    "user": "mabshoff"
}
```

Replying to [comment:3 craigcitro]:
> Looks good. Would it be safer to kill a few more digits, just to prevent having a similar ticket at some point?

No, we should only kill the digits needed, not any more. Otherwise numeric stability would go out the window :)

Cheers,

Michael



---

archive/issue_comments_025369.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-07-07T22:35:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25369",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_025370.json:
```json
{
    "body": "Merged in Sage 3.0.4.rc0",
    "created_at": "2008-07-07T23:00:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3589",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3589#issuecomment-25370",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.rc0
