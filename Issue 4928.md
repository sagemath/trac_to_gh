# Issue 4928: Create Sage 3.2.3 release notes

archive/issues_004928.json:
```json
{
    "body": "Assignee: mabshoff\n\nAs the summary says :)\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/4928\n\n",
    "created_at": "2009-01-02T23:16:37Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Create Sage 3.2.3 release notes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4928",
    "user": "mabshoff"
}
```
Assignee: mabshoff

As the summary says :)

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/4928





---

archive/issue_comments_037387.json:
```json
{
    "body": "Please comment on needed fixes.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-10T01:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37387",
    "user": "mabshoff"
}
```

Please comment on needed fixes.

Cheers,

Michael



---

archive/issue_comments_037388.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-01-10T01:16:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37388",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_037389.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-10T01:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37389",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_037390.json:
```json
{
    "body": "Only one remark:\n\nIn the introductory text, it is said \"... 71 Open Source Packages ...\". The count of spkgs is beyond 90 (93 I think), but that is not a one-to-one relation, of course.\n\nIs that number \"71\" to be updated? (If it should, but is not going to be updated, that would be still fine for me.)",
    "created_at": "2009-01-13T08:21:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37390",
    "user": "GeorgSWeber"
}
```

Only one remark:

In the introductory text, it is said "... 71 Open Source Packages ...". The count of spkgs is beyond 90 (93 I think), but that is not a one-to-one relation, of course.

Is that number "71" to be updated? (If it should, but is not going to be updated, that would be still fine for me.)



---

archive/issue_comments_037391.json:
```json
{
    "body": "> The count of spkgs is beyond 90 (93 I think), but that is \n> not a one-to-one relation, of course.\n\nwstein`@`sage:~/sage/spkg/standard$ ls *.spkg |wc -l\n88\n\nBut I'm not convinced every spkg counts as an \"open source package\".  Are any of these spkg's \"open source packages\":\n\nelliptic_curves-0.1.spkg\nexamples-3.2.3.spkg\nextcode-3.2.3.spkg\n\nDefinitely 71 should increase though, e.g., since new spkg's like docutils-0.5.spkg have been added to sage since I computed that 71 number.",
    "created_at": "2009-01-13T14:51:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37391",
    "user": "was"
}
```

> The count of spkgs is beyond 90 (93 I think), but that is 
> not a one-to-one relation, of course.

wstein`@`sage:~/sage/spkg/standard$ ls *.spkg |wc -l
88

But I'm not convinced every spkg counts as an "open source package".  Are any of these spkg's "open source packages":

elliptic_curves-0.1.spkg
examples-3.2.3.spkg
extcode-3.2.3.spkg

Definitely 71 should increase though, e.g., since new spkg's like docutils-0.5.spkg have been added to sage since I computed that 71 number.



---

archive/issue_comments_037392.json:
```json
{
    "body": "I have checked and 3.2.3 has 89 spkgs. Of those six are not \n\n```\ndoc\nelliptic_curves\nexamples\nextcode\nscripts\npolytopes_db\n```\n\nOpen source projects IMHO. So let's use the number 83 for now.\n\nI am attaching a final version of the release notes shortly.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T04:49:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37392",
    "user": "mabshoff"
}
```

I have checked and 3.2.3 has 89 spkgs. Of those six are not 

```
doc
elliptic_curves
examples
extcode
scripts
polytopes_db
```

Open source projects IMHO. So let's use the number 83 for now.

I am attaching a final version of the release notes shortly.

Cheers,

Michael



---

archive/issue_comments_037393.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-19T04:57:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37393",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_037394.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-19T05:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37394",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037395.json:
```json
{
    "body": "Merged in Sage 3.2.3 - a little late, but it is finally in :)\n\nCheers,\n\nMichael",
    "created_at": "2009-01-19T05:10:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4928",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4928#issuecomment-37395",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.3 - a little late, but it is finally in :)

Cheers,

Michael
