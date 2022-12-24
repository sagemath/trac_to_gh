# Issue 9451: [with patch, needs work] sieve of atkin

archive/issues_009451.json:
```json
{
    "body": "Assignee: was\n\nCC:  was kevin.stueve robertwb\n\nKeywords: prime, sieve, range\n\nThe goal of this ticket is to efficiently implement the sieve of atkin. This first version is a step in that direction.\n\nPaper on the sieve can be found at http://bit.ly/sieveatkin\n\nDue to the length of the implementation, I moved `prime_range` from `fast_arith` into a new module.\n\nThe current implementation uses 64-bit ints and hits that barrier at input around `2**56`, so I've capped it at `2**52` (in the future I plan to remove this limitation).\n\nI've changed the default algorithm to atkins, since it is nearly as fast as the pari table, but doesn't use as much storage so it is more viable for large input.\n\nDocstrings are incomplete.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9451\n\n",
    "created_at": "2010-07-08T01:31:21Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs work] sieve of atkin",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9451",
    "user": "ohanar"
}
```
Assignee: was

CC:  was kevin.stueve robertwb

Keywords: prime, sieve, range

The goal of this ticket is to efficiently implement the sieve of atkin. This first version is a step in that direction.

Paper on the sieve can be found at http://bit.ly/sieveatkin

Due to the length of the implementation, I moved `prime_range` from `fast_arith` into a new module.

The current implementation uses 64-bit ints and hits that barrier at input around `2**56`, so I've capped it at `2**52` (in the future I plan to remove this limitation).

I've changed the default algorithm to atkins, since it is nearly as fast as the pari table, but doesn't use as much storage so it is more viable for large input.

Docstrings are incomplete.

Issue created by migration from https://trac.sagemath.org/ticket/9451





---

archive/issue_comments_090575.json:
```json
{
    "body": "Attachment [sieve_of_atkin.patch](tarball://root/attachments/some-uuid/ticket9451/sieve_of_atkin.patch) by ohanar created at 2010-07-08 02:02:09\n\nbased on 4.4.4",
    "created_at": "2010-07-08T02:02:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9451#issuecomment-90575",
    "user": "ohanar"
}
```

Attachment [sieve_of_atkin.patch](tarball://root/attachments/some-uuid/ticket9451/sieve_of_atkin.patch) by ohanar created at 2010-07-08 02:02:09

based on 4.4.4



---

archive/issue_comments_090576.json:
```json
{
    "body": "A couple quick things without really looking at the content of the patch:\n\n1) You should probably import prime_range into fast_arith for backward compatibility.\n\n2) You don't need backslashes to continue lines when they're in brackets.\n\n3) You should make the default algorithm `None` and choose it inside of the function.  That way it can choose a different algorithm if the input is outside of the range of atkins.",
    "created_at": "2010-07-08T06:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9451",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9451#issuecomment-90576",
    "user": "mhansen"
}
```

A couple quick things without really looking at the content of the patch:

1) You should probably import prime_range into fast_arith for backward compatibility.

2) You don't need backslashes to continue lines when they're in brackets.

3) You should make the default algorithm `None` and choose it inside of the function.  That way it can choose a different algorithm if the input is outside of the range of atkins.
