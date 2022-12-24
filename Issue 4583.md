# Issue 4583: implement "sage -t --only-optional"

archive/issues_004583.json:
```json
{
    "body": "Assignee: mabshoff\n\nI am going to implement exactly one thing for this ticket:\n\nI will add an option\n\n```\n   sage -t --only-optional=comma,separated,list,of,tags file1.py dir ...\n```\n\n\nThis would run every doctest block where at least one line in the block contains \n\n```\n# optional - set of tags that must be subset of those above\n```\n\n\nThe complete block would run, but with any # optional's that don't have tags a subset of the input to sage -t removed. \n\nAlso, there is one special case:\n\n```\nsage -t only-optional\n```\n\nwith no tages.  In this case, every doctest block that contains any # optional's is run.  All others are skipped. \n\nThis design is joint work with Michael Abshoff.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4583\n\n",
    "created_at": "2008-11-22T20:25:48Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "title": "implement \"sage -t --only-optional\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4583",
    "user": "was"
}
```
Assignee: mabshoff

I am going to implement exactly one thing for this ticket:

I will add an option

```
   sage -t --only-optional=comma,separated,list,of,tags file1.py dir ...
```


This would run every doctest block where at least one line in the block contains 

```
# optional - set of tags that must be subset of those above
```


The complete block would run, but with any # optional's that don't have tags a subset of the input to sage -t removed. 

Also, there is one special case:

```
sage -t only-optional
```

with no tages.  In this case, every doctest block that contains any # optional's is run.  All others are skipped. 

This design is joint work with Michael Abshoff.

Issue created by migration from https://trac.sagemath.org/ticket/4583





---

archive/issue_comments_034369.json:
```json
{
    "body": "Attachment [scripts-4583.patch](tarball://root/attachments/some-uuid/ticket4583/scripts-4583.patch) by was created at 2008-11-23 01:57:25\n\napply to the local/bin/ scripts repo.",
    "created_at": "2008-11-23T01:57:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34369",
    "user": "was"
}
```

Attachment [scripts-4583.patch](tarball://root/attachments/some-uuid/ticket4583/scripts-4583.patch) by was created at 2008-11-23 01:57:25

apply to the local/bin/ scripts repo.



---

archive/issue_comments_034370.json:
```json
{
    "body": "Attachment [sage-4583.patch](tarball://root/attachments/some-uuid/ticket4583/sage-4583.patch) by was created at 2008-11-23 01:58:58\n\nthis rolls out using # optional - foo for most of the magma, macaulay2 and mathematica doctests.  It changes a *LOT* of files.  Note -- the optional doctests for those components may not pass (e.g., the magma ones won't), because it is already known that many optional doctests have bitrotted.  Fixing this is the subject of another ticket.  Note, in a few cases I increased doctest coverage, since I saw functions with no doctests at all.",
    "created_at": "2008-11-23T01:58:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34370",
    "user": "was"
}
```

Attachment [sage-4583.patch](tarball://root/attachments/some-uuid/ticket4583/sage-4583.patch) by was created at 2008-11-23 01:58:58

this rolls out using # optional - foo for most of the magma, macaulay2 and mathematica doctests.  It changes a *LOT* of files.  Note -- the optional doctests for those components may not pass (e.g., the magma ones won't), because it is already known that many optional doctests have bitrotted.  Fixing this is the subject of another ticket.  Note, in a few cases I increased doctest coverage, since I saw functions with no doctests at all.



---

archive/issue_comments_034371.json:
```json
{
    "body": "Attachment [sage-4583-part2.patch](tarball://root/attachments/some-uuid/ticket4583/sage-4583-part2.patch) by was created at 2008-11-23 02:20:51",
    "created_at": "2008-11-23T02:20:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34371",
    "user": "was"
}
```

Attachment [sage-4583-part2.patch](tarball://root/attachments/some-uuid/ticket4583/sage-4583-part2.patch) by was created at 2008-11-23 02:20:51



---

archive/issue_comments_034372.json:
```json
{
    "body": "Attachment [scripts-4583-part2.patch](tarball://root/attachments/some-uuid/ticket4583/scripts-4583-part2.patch) by was created at 2008-11-23 02:31:05\n\nthis finishes the only_optional no args case",
    "created_at": "2008-11-23T02:31:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34372",
    "user": "was"
}
```

Attachment [scripts-4583-part2.patch](tarball://root/attachments/some-uuid/ticket4583/scripts-4583-part2.patch) by was created at 2008-11-23 02:31:05

this finishes the only_optional no args case



---

archive/issue_comments_034373.json:
```json
{
    "body": "With the first two Sage repo patches applied I am seeing two issues #4590 and\n\n```\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py\", line 2453:\n    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(pari_group=False)\nExpected:\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1\nGot:\n    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1\n\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T02:55:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34373",
    "user": "mabshoff"
}
```

With the first two Sage repo patches applied I am seeing two issues #4590 and

```
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 2453:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(pari_group=False)
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1

**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_034374.json:
```json
{
    "body": "Attachment [sage-4583-part3.patch](tarball://root/attachments/some-uuid/ticket4583/sage-4583-part3.patch) by mabshoff created at 2008-11-23 03:08:12\n\nsage-4583-part3.patch fixes the above issue with sage/rings/number_field/number_field.py I mentioned above.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T03:08:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34374",
    "user": "mabshoff"
}
```

Attachment [sage-4583-part3.patch](tarball://root/attachments/some-uuid/ticket4583/sage-4583-part3.patch) by mabshoff created at 2008-11-23 03:08:12

sage-4583-part3.patch fixes the above issue with sage/rings/number_field/number_field.py I mentioned above.

Cheers,

Michael



---

archive/issue_comments_034375.json:
```json
{
    "body": "I really like this patch :)\n\nSo far everything I tried works well. The patch seems to expose some small issues like the ones below:\n\n```\nage -t -only-optional=magma devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py\", line 2452:\n    sage: x = polygen(QQ)\nExpected:\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1\nGot nothing\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py\", line 2455:\n    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma\nExpected:\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1\nGot:\n    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.\n    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1\n**********************************************************************\n```\n\nI.e. the last test should depend on Magma and database_gap. But all these little bugs can be addressed via follow up patches, so I am giving this patch a positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-23T03:46:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34375",
    "user": "mabshoff"
}
```

I really like this patch :)

So far everything I tried works well. The patch seems to expose some small issues like the ones below:

```
age -t -only-optional=magma devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 2452:
    sage: x = polygen(QQ)
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got nothing
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/number_field/number_field.py", line 2455:
    sage: NumberField(x^3 + 2*x + 1, 'a').galois_group(algorithm='magma')   # optional - magma
Expected:
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
Got:
    verbose 0 (501: permgroup_named.py, __init__) Warning: Computing with TransitiveGroups requires the optional database_gap package. Please install it.
    Galois group Transitive group number 2 of degree 3 of the Number Field in a with defining polynomial x^3 + 2*x + 1
**********************************************************************
```

I.e. the last test should depend on Magma and database_gap. But all these little bugs can be addressed via follow up patches, so I am giving this patch a positive review.

Cheers,

Michael



---

archive/issue_comments_034376.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-23T04:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34376",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034377.json:
```json
{
    "body": "Merged all five patches in Sage 3.2.1.alpha0",
    "created_at": "2008-11-23T04:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4583",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4583#issuecomment-34377",
    "user": "mabshoff"
}
```

Merged all five patches in Sage 3.2.1.alpha0
