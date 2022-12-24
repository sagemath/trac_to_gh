# Issue 2621: parallell doctest: concurrency problem when creating .doctest directories

archive/issues_002621.json:
```json
{
    "body": "Assignee: gfurnish\n\nWhen parallel doctesting a clean, i.e. never before doctested, tree there are concurrency issues when creating the .doctest directory:\n\n```\nTraceback (most recent call last):\n  File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/bin/sage-doctest\", line 427, in <module>\n    test_file(argv[1])\n  File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/bin/sage-doctest\", line 321, in test_file\n    os.makedirs(\".doctest\")\n  File \"/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/os.py\", line 172, in makedirs\n    mkdir(name, mode)\nOSError: [Errno 17] File exists: '.doctest'\n```\n\nThe above is just a scary message and doesn't affect the operation of the doctests. Creating all the .doctest directories before starting to run the doctests would fix the problem.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/2621\n\n",
    "created_at": "2008-03-20T23:36:40Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "parallell doctest: concurrency problem when creating .doctest directories",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2621",
    "user": "mabshoff"
}
```
Assignee: gfurnish

When parallel doctesting a clean, i.e. never before doctested, tree there are concurrency issues when creating the .doctest directory:

```
Traceback (most recent call last):
  File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/bin/sage-doctest", line 427, in <module>
    test_file(argv[1])
  File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/bin/sage-doctest", line 321, in test_file
    os.makedirs(".doctest")
  File "/scratch/mabshoff/release-cycle/sage-2.11.alpha1/local/lib/python2.5/os.py", line 172, in makedirs
    mkdir(name, mode)
OSError: [Errno 17] File exists: '.doctest'
```

The above is just a scary message and doesn't affect the operation of the doctests. Creating all the .doctest directories before starting to run the doctests would fix the problem.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/2621





---

archive/issue_comments_017998.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-20T23:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2621#issuecomment-17998",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017999.json:
```json
{
    "body": "Attachment [trac_2621.patch](tarball://root/attachments/some-uuid/ticket2621/trac_2621.patch) by gfurnish created at 2008-03-20 23:41:00",
    "created_at": "2008-03-20T23:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2621#issuecomment-17999",
    "user": "gfurnish"
}
```

Attachment [trac_2621.patch](tarball://root/attachments/some-uuid/ticket2621/trac_2621.patch) by gfurnish created at 2008-03-20 23:41:00



---

archive/issue_comments_018000.json:
```json
{
    "body": "Patch looks good to me. Positive review ;)\n\nCheers,\n\nMichael",
    "created_at": "2008-03-21T00:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2621#issuecomment-18000",
    "user": "mabshoff"
}
```

Patch looks good to me. Positive review ;)

Cheers,

Michael



---

archive/issue_comments_018001.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-21T00:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2621#issuecomment-18001",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018002.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-21T00:05:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2621",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2621#issuecomment-18002",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha1
