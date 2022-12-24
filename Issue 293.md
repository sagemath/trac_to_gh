# Issue 293: nasty memory leak in FAST_SEQ_UNSAFE macro

archive/issues_000293.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  dmharvey@math.harvard.edu\n\nIt appears that `FAST_SEQ_UNSAFE` creates a new reference to the list but never releases it.\n\nIt might be because `PySequence_Fast` returns a new reference, but `PySequence_Fast_ITEMS` doesn't release it.\n\nSee also\n\nhttp://docs.python.org/api/sequence.html\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/293\n\n",
    "created_at": "2007-02-24T16:43:20Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "nasty memory leak in FAST_SEQ_UNSAFE macro",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/293",
    "user": "dmharvey"
}
```
Assignee: somebody

CC:  dmharvey@math.harvard.edu

It appears that `FAST_SEQ_UNSAFE` creates a new reference to the list but never releases it.

It might be because `PySequence_Fast` returns a new reference, but `PySequence_Fast_ITEMS` doesn't release it.

See also

http://docs.python.org/api/sequence.html


Issue created by migration from https://trac.sagemath.org/ticket/293





---

archive/issue_comments_001384.json:
```json
{
    "body": "Replying to [comment:1 was]:\n\nNow that we have fast list indexing, there should be very few instances where we need to use this macro...",
    "created_at": "2007-08-19T00:51:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/293#issuecomment-1384",
    "user": "robertwb"
}
```

Replying to [comment:1 was]:

Now that we have fast list indexing, there should be very few instances where we need to use this macro...



---

archive/issue_comments_001385.json:
```json
{
    "body": "Confirmed.  This is a *major* memory leak\n\n```\n[18:35] <william> indeed!\n[18:35] <william> david harvey is totally right about that memory leak!\n[18:35] <william> Try the following two distinct blocks of code, where m = get_memory_usage\n[18:35] <william> print m()\n[18:35] <william> n = random_matrix(RR, 200) \n[18:35] <william> n.set_immutable()\n[18:35] <william> hash(n)\n[18:35] <william> del n\n[18:35] <william> m()\n[18:35] <william>   -- and --\n[18:35] <william> print m()\n[18:35] <william> n = random_matrix(RR, 200) \n[18:35] <william> n.set_immutable()\n[18:35] <william> del n\n[18:35] <william> m()\n[18:36] <william> The first leaks about 3MB every time.  The second doesn't leak at all.\n[18:36] <robertwb> ouch\n[18:36] <robertwb> yes, it's a new reference (though it may or may not be a new object)\n\n\nprint m()\nn = random_matrix(RR, 200) \nn.set_immutable()\nhash(n)\ndel n\nm()\n```\n",
    "created_at": "2007-08-19T01:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/293#issuecomment-1385",
    "user": "was"
}
```

Confirmed.  This is a *major* memory leak

```
[18:35] <william> indeed!
[18:35] <william> david harvey is totally right about that memory leak!
[18:35] <william> Try the following two distinct blocks of code, where m = get_memory_usage
[18:35] <william> print m()
[18:35] <william> n = random_matrix(RR, 200) 
[18:35] <william> n.set_immutable()
[18:35] <william> hash(n)
[18:35] <william> del n
[18:35] <william> m()
[18:35] <william>   -- and --
[18:35] <william> print m()
[18:35] <william> n = random_matrix(RR, 200) 
[18:35] <william> n.set_immutable()
[18:35] <william> del n
[18:35] <william> m()
[18:36] <william> The first leaks about 3MB every time.  The second doesn't leak at all.
[18:36] <robertwb> ouch
[18:36] <robertwb> yes, it's a new reference (though it may or may not be a new object)


print m()
n = random_matrix(RR, 200) 
n.set_immutable()
hash(n)
del n
m()
```




---

archive/issue_comments_001386.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2007-08-19T01:42:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/293#issuecomment-1386",
    "user": "was"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_001387.json:
```json
{
    "body": "Changing assignee from somebody to robertwb.",
    "created_at": "2007-08-19T01:47:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/293#issuecomment-1387",
    "user": "was"
}
```

Changing assignee from somebody to robertwb.



---

archive/issue_comments_001388.json:
```json
{
    "body": "patch to remove all uses of FAST_SEQ_UNSAFE",
    "created_at": "2007-08-19T07:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/293#issuecomment-1388",
    "user": "robertwb"
}
```

patch to remove all uses of FAST_SEQ_UNSAFE



---

archive/issue_comments_001389.json:
```json
{
    "body": "Attachment [no-FAST_SEQ_UNSAFE.patch](tarball://root/attachments/some-uuid/ticket293/no-FAST_SEQ_UNSAFE.patch) by robertwb created at 2007-08-19 07:54:24",
    "created_at": "2007-08-19T07:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/293#issuecomment-1389",
    "user": "robertwb"
}
```

Attachment [no-FAST_SEQ_UNSAFE.patch](tarball://root/attachments/some-uuid/ticket293/no-FAST_SEQ_UNSAFE.patch) by robertwb created at 2007-08-19 07:54:24



---

archive/issue_comments_001390.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-08-19T07:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/293",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/293#issuecomment-1390",
    "user": "robertwb"
}
```

Resolution: fixed
