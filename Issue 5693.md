# Issue 5693: sloane_sequence -- very confusing error message

archive/issues_005693.json:
```json
{
    "body": "Assignee: cwitty\n\nThe \"sloan_sequence\" command fails on every input I give it, whereas sloan_find works fine!\n\n```\nsage: sloane_sequence(prime_range(100))\nSearching Sloane's online database...\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/wstein/.sage/temp/teragon.local/4529/_Users_wstein__sage_init_sage_0.py in <module>()\n\n/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/databases/sloane.pyc in sloane_sequence(number)\n    302     results = sloane_find('id:A%s'%number)\n    303     if len(results) == 0:\n--> 304         raise ValueError, \"sequence '%s' not found\"%number\n    305     return results[0]\n    306 \n\nValueError: sequence '[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]' not found\nsage: print sloane_find(prime_range(100))\nSearching Sloane's online database...\n[[40, 'The prime numbers.', [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, \n```\n\n\nDoh -- on checking the docs it appears that sloane_sequence takes a sequence number... and it just happens to be perfectly fine letting that \"number\" be a list.  Much better type checking would save a lot of confusion.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5693\n\n",
    "created_at": "2009-04-06T17:00:21Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "sloane_sequence -- very confusing error message",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5693",
    "user": "@williamstein"
}
```
Assignee: cwitty

The "sloan_sequence" command fails on every input I give it, whereas sloan_find works fine!

```
sage: sloane_sequence(prime_range(100))
Searching Sloane's online database...
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/wstein/.sage/temp/teragon.local/4529/_Users_wstein__sage_init_sage_0.py in <module>()

/Users/wstein/build/sage-3.4/local/lib/python2.5/site-packages/sage/databases/sloane.pyc in sloane_sequence(number)
    302     results = sloane_find('id:A%s'%number)
    303     if len(results) == 0:
--> 304         raise ValueError, "sequence '%s' not found"%number
    305     return results[0]
    306 

ValueError: sequence '[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]' not found
sage: print sloane_find(prime_range(100))
Searching Sloane's online database...
[[40, 'The prime numbers.', [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 
```


Doh -- on checking the docs it appears that sloane_sequence takes a sequence number... and it just happens to be perfectly fine letting that "number" be a list.  Much better type checking would save a lot of confusion.

Issue created by migration from https://trac.sagemath.org/ticket/5693





---

archive/issue_comments_044510.json:
```json
{
    "body": "To test the attached patch, apply it, then do\n\n\n```\n ./sage -t --only_optional=internet devel/sage/sage/databases/sloane.py \n```\n\n\nand\n\n\n\n```\n ./sage -t devel/sage/sage/databases/sloane.py \n```\n",
    "created_at": "2009-04-06T17:07:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5693#issuecomment-44510",
    "user": "@williamstein"
}
```

To test the attached patch, apply it, then do


```
 ./sage -t --only_optional=internet devel/sage/sage/databases/sloane.py 
```


and



```
 ./sage -t devel/sage/sage/databases/sloane.py 
```




---

archive/issue_comments_044511.json:
```json
{
    "body": "Attachment [trac_5693.patch](tarball://root/attachments/some-uuid/ticket5693/trac_5693.patch) by @williamstein created at 2009-04-06 17:08:17",
    "created_at": "2009-04-06T17:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5693#issuecomment-44511",
    "user": "@williamstein"
}
```

Attachment [trac_5693.patch](tarball://root/attachments/some-uuid/ticket5693/trac_5693.patch) by @williamstein created at 2009-04-06 17:08:17



---

archive/issue_comments_044512.json:
```json
{
    "body": "Patch is ok for me.\n\nSo a positive review.\n\nJaap",
    "created_at": "2009-04-06T17:49:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5693#issuecomment-44512",
    "user": "@jaapspies"
}
```

Patch is ok for me.

So a positive review.

Jaap



---

archive/issue_comments_044513.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-09T09:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5693#issuecomment-44513",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.1.rc2.

Cheers,

Michael



---

archive/issue_comments_044514.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-09T09:52:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5693",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5693#issuecomment-44514",
    "user": "mabshoff"
}
```

Resolution: fixed
