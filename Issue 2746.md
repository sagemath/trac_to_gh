# Issue 2746: [with patch; needs review] Support for writing test-related files in SAGE_TESTDIR

archive/issues_002746.json:
```json
{
    "body": "Assignee: failure\n\nI've attached my changeset that causes all writes that occur when running doctests to be written inside SAGE_TESTDIR.\n\nOne thing I'm uncertain about is what should happen with the line\n\"cat $SAGE_TESTLOG >> $SAGE_ROOT/test.log\".\n\nAt the moment, I leave it in, and there's an error at the end of the block of tests.  I would recommend removing it and just making $SAGE_ROOT/test.log be a symlink to $SAGE_ROOT/tmp/test.log in the default SAGE install.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2746\n\n",
    "created_at": "2008-04-01T01:23:11Z",
    "labels": [
        "doctest coverage",
        "major",
        "enhancement"
    ],
    "title": "[with patch; needs review] Support for writing test-related files in SAGE_TESTDIR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2746",
    "user": "tabbott"
}
```
Assignee: failure

I've attached my changeset that causes all writes that occur when running doctests to be written inside SAGE_TESTDIR.

One thing I'm uncertain about is what should happen with the line
"cat $SAGE_TESTLOG >> $SAGE_ROOT/test.log".

At the moment, I leave it in, and there's an error at the end of the block of tests.  I would recommend removing it and just making $SAGE_ROOT/test.log be a symlink to $SAGE_ROOT/tmp/test.log in the default SAGE install.

Issue created by migration from https://trac.sagemath.org/ticket/2746





---

archive/issue_comments_018870.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-01T01:49:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2746#issuecomment-18870",
    "user": "tabbott"
}
```

Attachment



---

archive/issue_comments_018871.json:
```json
{
    "body": "There is a small reject due to #2621 having been merged, but after resolving the merge conflict both patches apply cleanly. I am doing some more extensive testing before giving this a positive review, but so far things look good.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T09:17:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2746#issuecomment-18871",
    "user": "mabshoff"
}
```

There is a small reject due to #2621 having been merged, but after resolving the merge conflict both patches apply cleanly. I am doing some more extensive testing before giving this a positive review, but so far things look good.

Cheers,

Michael



---

archive/issue_comments_018872.json:
```json
{
    "body": "Attachment\n\ncheck if SAGE_TEST is not empty",
    "created_at": "2008-04-03T10:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2746#issuecomment-18872",
    "user": "mabshoff"
}
```

Attachment

check if SAGE_TEST is not empty



---

archive/issue_comments_018873.json:
```json
{
    "body": "If SAGE_TEST is empty things go wrong. I have attached a patch that fixes the issue. Positive review since this is useful \"as-is\". A couple suggestions for a follow up patch:\n \n* make sure that SAGE_TEST is writable\n* delete the .doctest file once the doctest finishes\n* document SAGE_TEST :)\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T10:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2746#issuecomment-18873",
    "user": "mabshoff"
}
```

If SAGE_TEST is empty things go wrong. I have attached a patch that fixes the issue. Positive review since this is useful "as-is". A couple suggestions for a follow up patch:
 
* make sure that SAGE_TEST is writable
* delete the .doctest file once the doctest finishes
* document SAGE_TEST :)

Cheers,

Michael



---

archive/issue_comments_018874.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T10:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2746#issuecomment-18874",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018875.json:
```json
{
    "body": "Merged all three patches in Sage 3.0.alpah1",
    "created_at": "2008-04-03T10:35:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2746#issuecomment-18875",
    "user": "mabshoff"
}
```

Merged all three patches in Sage 3.0.alpah1
