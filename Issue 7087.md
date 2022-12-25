# Issue 7087: doctest failure in databases/sloane.py

archive/issues_007087.json:
```json
{
    "body": "Assignee: tbd\n\nKeywords: sloane doctest internet\n\nIf doctesting optional tests with option \"internet\", the sloane_find command returns a result different from what's in the file:\n\n```\nFile \"/home/drake/sage-4.1.2.alpha4/devel/sage-main/sage/databases/sloane.py\", line 44:\n    sage: sloane_find([1,2,3,4,5], 2)      # optional - internet\nExpected:\n    Searching Sloane's online database...\n    [[27, 'The natural numbers. Also called the whole numbers, the counting numbers or the positive integers.', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]], [961, 'Prime powers p^k (p prime, k &gt;= 0).', [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37, 41, 43, 47, 49, 53, 59, 61, 64, 67, 71, 73, 79, 81, 83, 89, 97, 101, 103, 107, 109, 113, 121, 125, 127, 128, 131, 137, 139, 149, 151, 157, 163, 167, 169, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227]]]\nGot:\n    Searching Sloane's online database...\n    [[27, 'The natural numbers. Also called the whole numbers, the counting numbers or the positive integers.', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]], [7953, 'Digital sum (i.e. sum of digits) of n.', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15]]]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7087\n\n",
    "created_at": "2009-10-01T02:29:25Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "doctest failure in databases/sloane.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7087",
    "user": "https://github.com/dandrake"
}
```
Assignee: tbd

Keywords: sloane doctest internet

If doctesting optional tests with option "internet", the sloane_find command returns a result different from what's in the file:

```
File "/home/drake/sage-4.1.2.alpha4/devel/sage-main/sage/databases/sloane.py", line 44:
    sage: sloane_find([1,2,3,4,5], 2)      # optional - internet
Expected:
    Searching Sloane's online database...
    [[27, 'The natural numbers. Also called the whole numbers, the counting numbers or the positive integers.', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]], [961, 'Prime powers p^k (p prime, k &gt;= 0).', [1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37, 41, 43, 47, 49, 53, 59, 61, 64, 67, 71, 73, 79, 81, 83, 89, 97, 101, 103, 107, 109, 113, 121, 125, 127, 128, 131, 137, 139, 149, 151, 157, 163, 167, 169, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227]]]
Got:
    Searching Sloane's online database...
    [[27, 'The natural numbers. Also called the whole numbers, the counting numbers or the positive integers.', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]], [7953, 'Digital sum (i.e. sum of digits) of n.', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 8, 9, 10, 11, 12, 13, 14, 15]]]
```


Issue created by migration from https://trac.sagemath.org/ticket/7087





---

archive/issue_comments_058468.json:
```json
{
    "body": "change doctest to just test length, add a new doctest that should only return one result",
    "created_at": "2009-10-01T02:46:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7087#issuecomment-58468",
    "user": "https://github.com/dandrake"
}
```

change doctest to just test length, add a new doctest that should only return one result



---

archive/issue_comments_058469.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-10-01T02:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7087#issuecomment-58469",
    "user": "https://github.com/dandrake"
}
```

Changing status from new to assigned.



---

archive/issue_comments_058470.json:
```json
{
    "body": "Changing assignee from tbd to @dandrake.",
    "created_at": "2009-10-01T02:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7087#issuecomment-58470",
    "user": "https://github.com/dandrake"
}
```

Changing assignee from tbd to @dandrake.



---

archive/issue_comments_058471.json:
```json
{
    "body": "Attachment [trac_7087.patch](tarball://root/attachments/some-uuid/ticket7087/trac_7087.patch) by @dandrake created at 2009-10-01 02:49:22\n\nThe text around the offending doctest is talking about the number of results returned, so I changed the doctest to just test the number of results. I also added a new doctest that tests a sequence that should only ever return one result -- [the first bits of A137443](http://www.research.att.com/~njas/sequences/A137443) are quite unlikely to show up in another sequence.",
    "created_at": "2009-10-01T02:49:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7087#issuecomment-58471",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_7087.patch](tarball://root/attachments/some-uuid/ticket7087/trac_7087.patch) by @dandrake created at 2009-10-01 02:49:22

The text around the offending doctest is talking about the number of results returned, so I changed the doctest to just test the number of results. I also added a new doctest that tests a sequence that should only ever return one result -- [the first bits of A137443](http://www.research.att.com/~njas/sequences/A137443) are quite unlikely to show up in another sequence.



---

archive/issue_comments_058472.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-10-01T08:40:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7087#issuecomment-58472",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_events_007309.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-10-15T10:03:00Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7087",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7087#event-7309"
}
```



---

archive/issue_comments_058473.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T10:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7087",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7087#issuecomment-58473",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
