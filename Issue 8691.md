# Issue 8691: Implement Plain Change algorithm in cython

archive/issues_008691.json:
```json
{
    "body": "Assignee: sage-combinat\n\nCC:  rlm\n\nThe implementation is already done, I just need a ticket number.\n\nMy fix for #8655 will depend on this.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8691\n\n",
    "created_at": "2010-04-15T06:19:19Z",
    "labels": [
        "combinatorics",
        "major",
        "bug"
    ],
    "title": "Implement Plain Change algorithm in cython",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8691",
    "user": "boothby"
}
```
Assignee: sage-combinat

CC:  rlm

The implementation is already done, I just need a ticket number.

My fix for #8655 will depend on this.

Issue created by migration from https://trac.sagemath.org/ticket/8691





---

archive/issue_comments_079174.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-15T22:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79174",
    "user": "boothby"
}
```

Attachment



---

archive/issue_comments_079175.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-15T22:03:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79175",
    "user": "boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_079176.json:
```json
{
    "body": "Hi Tom,\n\nThis looks very good ! Thanks for this. I've only one concerns: from the name, I would never guess what it does. I'm not sure to have a better name but I think we should ask for better proposal on the mailing lists.",
    "created_at": "2010-04-15T22:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79176",
    "user": "hivert"
}
```

Hi Tom,

This looks very good ! Thanks for this. I've only one concerns: from the name, I would never guess what it does. I'm not sure to have a better name but I think we should ask for better proposal on the mailing lists.



---

archive/issue_comments_079177.json:
```json
{
    "body": "> This looks very good ! Thanks for this. I've only one concerns: from the name, I would never guess what it does. I'm not sure to have a better name but I think we should ask for better proposal on the mailing lists. \n\nSorry for the double answer. Is you algorithm different from \nhttp://en.wikipedia.org/wiki/Steinhaus\u2013Johnson\u2013Trotter_algorithm\nIf not this is maybe a good name.",
    "created_at": "2010-04-15T22:28:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79177",
    "user": "hivert"
}
```

> This looks very good ! Thanks for this. I've only one concerns: from the name, I would never guess what it does. I'm not sure to have a better name but I think we should ask for better proposal on the mailing lists. 

Sorry for the double answer. Is you algorithm different from 
http://en.wikipedia.org/wiki/Steinhaus–Johnson–Trotter_algorithm
If not this is maybe a good name.



---

archive/issue_comments_079178.json:
```json
{
    "body": "Oops, turns out that freeing a call to `malloc(0)` is a bad idea.",
    "created_at": "2010-04-16T20:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79178",
    "user": "boothby"
}
```

Oops, turns out that freeing a call to `malloc(0)` is a bad idea.



---

archive/issue_comments_079179.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-16T20:31:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79179",
    "user": "boothby"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_079180.json:
```json
{
    "body": "replaces previous",
    "created_at": "2010-04-28T22:05:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79180",
    "user": "boothby"
}
```

replaces previous



---

archive/issue_comments_079181.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-04-28T22:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79181",
    "user": "boothby"
}
```

Attachment



---

archive/issue_comments_079182.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-28T22:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79182",
    "user": "boothby"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_079183.json:
```json
{
    "body": "replaces all previous",
    "created_at": "2010-05-21T21:33:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79183",
    "user": "boothby"
}
```

replaces all previous



---

archive/issue_comments_079184.json:
```json
{
    "body": "Attachment\n\nUpdated version has changed the filename, and removed reference implementation because there's a better one in `sage/graphs/genus.pyx`.",
    "created_at": "2010-05-21T21:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79184",
    "user": "boothby"
}
```

Attachment

Updated version has changed the filename, and removed reference implementation because there's a better one in `sage/graphs/genus.pyx`.



---

archive/issue_comments_079185.json:
```json
{
    "body": "I think the usual convention here is to have Python functions that can test low-level C functions. It would also check input, etc...",
    "created_at": "2010-05-21T21:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79185",
    "user": "rlm"
}
```

I think the usual convention here is to have Python functions that can test low-level C functions. It would also check input, etc...



---

archive/issue_comments_079186.json:
```json
{
    "body": "apply on top of v3",
    "created_at": "2010-05-22T03:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79186",
    "user": "boothby"
}
```

apply on top of v3



---

archive/issue_comments_079187.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-05-22T03:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79187",
    "user": "boothby"
}
```

Changing priority from major to minor.



---

archive/issue_comments_079188.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-05-22T03:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79188",
    "user": "boothby"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_079189.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-22T03:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79189",
    "user": "boothby"
}
```

Attachment



---

archive/issue_comments_079190.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-25T23:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79190",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_079191.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2010-05-25T23:48:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79191",
    "user": "rlm"
}
```

Looks good to me.



---

archive/issue_comments_079192.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:04:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8691",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8691#issuecomment-79192",
    "user": "mhansen"
}
```

Resolution: fixed
