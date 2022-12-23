# Issue 5773: notebook -- uploading a corrupted worksheet (sws file) results in blank screen (no useful error message)

archive/issues_005773.json:
```json
{
    "body": "Assignee: boothby\n\nCC:  was\n\nI uploaded a corrupted tarball and get a blank screen from the server instead of a useful error.  I also get this in the server logs\n\n```\n2009-04-12 21:12:35-0700 [-] cd \"/Users/wstein/.sage/temp/teragon.local/61279/dir_1\"; tar -jxf \"/Users/wstein/.sage/temp/teragon.local/61279/dir_0/Homework_1____Devon_McMinn.sws\"\n\nbzip2: Data integrity error when decompressing.\n\tInput file = (stdin), output file = (stdout)\n\nIt is possible that the compressed file(s) have become corrupted.\nYou can use the -tvv option to test integrity of such files.\n\nYou can use the `bzip2recover' program to attempt to recover\ndata from undamaged sections of corrupted files.\n\ntar: Child returned status 2\ntar: Error exit delayed from previous errors\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5773\n\n",
    "created_at": "2009-04-13T04:13:46Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "notebook -- uploading a corrupted worksheet (sws file) results in blank screen (no useful error message)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5773",
    "user": "was"
}
```
Assignee: boothby

CC:  was

I uploaded a corrupted tarball and get a blank screen from the server instead of a useful error.  I also get this in the server logs

```
2009-04-12 21:12:35-0700 [-] cd "/Users/wstein/.sage/temp/teragon.local/61279/dir_1"; tar -jxf "/Users/wstein/.sage/temp/teragon.local/61279/dir_0/Homework_1____Devon_McMinn.sws"

bzip2: Data integrity error when decompressing.
	Input file = (stdin), output file = (stdout)

It is possible that the compressed file(s) have become corrupted.
You can use the -tvv option to test integrity of such files.

You can use the `bzip2recover' program to attempt to recover
data from undamaged sections of corrupted files.

tar: Child returned status 2
tar: Error exit delayed from previous errors


```


Issue created by migration from https://trac.sagemath.org/ticket/5773





---

archive/issue_comments_045151.json:
```json
{
    "body": "This is already fixed. Try:\n\n\n```\n\n$ echo '!@#rsfdsagarbage' > foo.sws\n\n```\n\n\nand try uploading it.",
    "created_at": "2010-01-18T04:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5773#issuecomment-45151",
    "user": "timdumol"
}
```

This is already fixed. Try:


```

$ echo '!@#rsfdsagarbage' > foo.sws

```


and try uploading it.



---

archive/issue_comments_045152.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-01-19T03:05:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5773#issuecomment-45152",
    "user": "timdumol"
}
```

Resolution: duplicate



---

archive/issue_comments_045153.json:
```json
{
    "body": "Resolution changed from duplicate to fixed",
    "created_at": "2010-01-19T03:37:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5773",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5773#issuecomment-45153",
    "user": "timdumol"
}
```

Resolution changed from duplicate to fixed
