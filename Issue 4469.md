# Issue 4469: Sage 3.2.a3: output ordering randomness in sage/rings/number_field/number_field.py

archive/issues_004469.json:
```json
{
    "body": "Assignee: tbd\n\neno:\n\n```\nsage -t  devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/home/wstein/eno/sage-3.2.alpha3/tmp/number_field.py\", line 1025:\n    sage: [phi(k.0^2) for phi in v]\nExpected:\n    [2.97572074038...,\n     -2.40889943716 + 1.90254105304*I,\n     -2.40889943716 - 1.90254105304*I,\n     0.921039066973 + 3.07553311885*I,\n     0.921039066973 - 3.07553311885*I]\nGot:\n    [2.97572074038, \n     -2.40889943716 + 1.90254105304*I, \n     -2.40889943716 - 1.90254105304*I, \n     0.921039066973 - 3.07553311885*I, \n     0.921039066973 + 3.07553311885*I]\n**********************************************************************\n```\n\ncicero:\n\n```\nsage -t  devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/home/wstein/cicero/build/sage-3.2.alpha3/tmp/number_field.py\", line 1032:\n    sage: K.complex_embeddings() \nExpected:\n    [\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 + 2\n      To:   Complex Double Field \n      Defn: a |--> -1.25992104989...,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 + 2\n      To:   Complex Double Field\n      Defn: a |--> 0.629960524947 - 1.09112363597*I,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 + 2\n      To:   Complex Double Field\n      Defn: a |--> 0.629960524947 + 1.09112363597*I\n    ]\nGot:\n    [\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 + 2\n      To:   Complex Double Field\n      Defn: a |--> -1.25992104989 + 2.77555756156e-16*I,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 + 2      To:   Complex Double Field\n      Defn: a |--> 0.629960524947 + 1.09112363597*I,\n    Ring morphism:\n      From: Number Field in a with defining polynomial x^3 + 2\n      To:   Complex Double Field\n      Defn: a |--> 0.629960524947 - 1.09112363597*I\n    ]\n**********************************************************************\n```\n\nmenas:\n\n```\nsage -t  devel/sage/sage/rings/number_field/number_field.py \n**********************************************************************\nFile \"/home/wstein/menas/build/sage-3.2.alpha3/tmp/number_field.py\", line 1025:\n    sage: [phi(k.0^2) for phi in v]\nExpected:\n    [2.97572074038...,\n     -2.40889943716 + 1.90254105304*I,\n     -2.40889943716 - 1.90254105304*I,\n     0.921039066973 + 3.07553311885*I,\n     0.921039066973 - 3.07553311885*I]\nGot:\n    [2.97572074038, \n     -2.40889943716 + 1.90254105304*I, \n     -2.40889943716 - 1.90254105304*I, \n     0.921039066973 - 3.07553311885*I, \n     0.921039066973 + 3.07553311885*I]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4469\n\n",
    "created_at": "2008-11-08T20:18:58Z",
    "labels": [
        "algebra",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "Sage 3.2.a3: output ordering randomness in sage/rings/number_field/number_field.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4469",
    "user": "mabshoff"
}
```
Assignee: tbd

eno:

```
sage -t  devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/home/wstein/eno/sage-3.2.alpha3/tmp/number_field.py", line 1025:
    sage: [phi(k.0^2) for phi in v]
Expected:
    [2.97572074038...,
     -2.40889943716 + 1.90254105304*I,
     -2.40889943716 - 1.90254105304*I,
     0.921039066973 + 3.07553311885*I,
     0.921039066973 - 3.07553311885*I]
Got:
    [2.97572074038, 
     -2.40889943716 + 1.90254105304*I, 
     -2.40889943716 - 1.90254105304*I, 
     0.921039066973 - 3.07553311885*I, 
     0.921039066973 + 3.07553311885*I]
**********************************************************************
```

cicero:

```
sage -t  devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/home/wstein/cicero/build/sage-3.2.alpha3/tmp/number_field.py", line 1032:
    sage: K.complex_embeddings() 
Expected:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field 
      Defn: a |--> -1.25992104989...,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> 0.629960524947 - 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> 0.629960524947 + 1.09112363597*I
    ]
Got:
    [
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> -1.25992104989 + 2.77555756156e-16*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2      To:   Complex Double Field
      Defn: a |--> 0.629960524947 + 1.09112363597*I,
    Ring morphism:
      From: Number Field in a with defining polynomial x^3 + 2
      To:   Complex Double Field
      Defn: a |--> 0.629960524947 - 1.09112363597*I
    ]
**********************************************************************
```

menas:

```
sage -t  devel/sage/sage/rings/number_field/number_field.py 
**********************************************************************
File "/home/wstein/menas/build/sage-3.2.alpha3/tmp/number_field.py", line 1025:
    sage: [phi(k.0^2) for phi in v]
Expected:
    [2.97572074038...,
     -2.40889943716 + 1.90254105304*I,
     -2.40889943716 - 1.90254105304*I,
     0.921039066973 + 3.07553311885*I,
     0.921039066973 - 3.07553311885*I]
Got:
    [2.97572074038, 
     -2.40889943716 + 1.90254105304*I, 
     -2.40889943716 - 1.90254105304*I, 
     0.921039066973 - 3.07553311885*I, 
     0.921039066973 + 3.07553311885*I]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/4469





---

archive/issue_comments_032995.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-16T08:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-32995",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_032996.json:
```json
{
    "body": "This has gone away in 3.2.rc1. I am not sure which patch is responsible here.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-16T08:58:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-32996",
    "user": "mabshoff"
}
```

This has gone away in 3.2.rc1. I am not sure which patch is responsible here.

Cheers,

Michael



---

archive/issue_comments_032997.json:
```json
{
    "body": "These problems pop up with gcc 4.3.2 and the system compiler on the given system does not show the problem. Reopened.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-16T21:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-32997",
    "user": "mabshoff"
}
```

These problems pop up with gcc 4.3.2 and the system compiler on the given system does not show the problem. Reopened.

Cheers,

Michael



---

archive/issue_comments_032998.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-11-16T21:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-32998",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_032999.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-11-16T21:07:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-32999",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_033000.json:
```json
{
    "body": "Attachment [trac-4469.patch](tarball://root/attachments/some-uuid/ticket4469/trac-4469.patch) by craigcitro created at 2008-11-18 09:31:42",
    "created_at": "2008-11-18T09:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-33000",
    "user": "craigcitro"
}
```

Attachment [trac-4469.patch](tarball://root/attachments/some-uuid/ticket4469/trac-4469.patch) by craigcitro created at 2008-11-18 09:31:42



---

archive/issue_comments_033001.json:
```json
{
    "body": "Patch simply adds `#random`. The real underlying bug is that we don't have a consistent ordering on elements in `CDF`: see #4544 for a discussion of this issue.",
    "created_at": "2008-11-18T09:32:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-33001",
    "user": "craigcitro"
}
```

Patch simply adds `#random`. The real underlying bug is that we don't have a consistent ordering on elements in `CDF`: see #4544 for a discussion of this issue.



---

archive/issue_comments_033002.json:
```json
{
    "body": "Looks good.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-18T09:35:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-33002",
    "user": "mabshoff"
}
```

Looks good.

Cheers,

Michael



---

archive/issue_comments_033003.json:
```json
{
    "body": "Merged in Sage 3.2.rc2",
    "created_at": "2008-11-18T18:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-33003",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc2



---

archive/issue_comments_033004.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-18T18:18:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4469",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4469#issuecomment-33004",
    "user": "mabshoff"
}
```

Resolution: fixed
