# Issue 2719: bitset is completely broken on os x 10.4 G5

archive/issues_002719.json:
```json
{
    "body": "Assignee: cwitty\n\n\n```\nFERMAT -- os x 10.4 g5 -- has interesting failures here in the \nnew bitset code:\n          sage -t  devel/sage-main/sage/misc/misc_c.pyx\n\n    sage: test_bitset('00101', '01110', 4)\nExpected:\n    a 00101\n    a.size 5\n    a.limbs 1\n    b 01110\n    a.check(n)   True\n    a.set(n)     00101\n    a.unset(n)   00100\n    a.set_to(n)  00101\n    a.flip(n)    00100\n    a.is_zero()  False\n    a.eq(b)      False\n    a.cmp(b)     1\n    a.copy()     00101\n    r.zero()     00000\n    not a        11010\n    a and b      00100\n    a or b       01111\n    a xor b      01011\n    a.rshift(n)  10000\n    a.lshift(n)  00000\n    a.first()           2\n    a.next(n)           4\n    a.first_diff(b)     1\n    a.next_diff(b, n)   4\n    a.hamming_weight()  2\n    a.hamming_weight_sparse()  2\nGot:\n    a 00101\n    a.size 5\n    a.limbs 1\n    b 01110\n    a.check(n)   True\n    a.set(n)     00101\n    a.unset(n)   00100\n    a.set_to(n)  00101\n    a.flip(n)    00100\n    a.is_zero()  False\n    a.eq(b)      True\n    a.cmp(b)     1\n    a.copy()     00000\n    r.zero()     00000\n    not a        11010\n    a and b      00100\n    a or b       01111\n    a xor b      01011\n    a.rshift(n)  10000\n    a.lshift(n)  00000\n    a.first()           2\n    a.next(n)           4\n    a.first_diff(b)     1\n    a.next_diff(b, n)   4\n    a.hamming_weight()  2\n    a.hamming_weight_sparse()  2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2719\n\n",
    "created_at": "2008-03-29T16:30:06Z",
    "labels": [
        "misc",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "bitset is completely broken on os x 10.4 G5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2719",
    "user": "was"
}
```
Assignee: cwitty


```
FERMAT -- os x 10.4 g5 -- has interesting failures here in the 
new bitset code:
          sage -t  devel/sage-main/sage/misc/misc_c.pyx

    sage: test_bitset('00101', '01110', 4)
Expected:
    a 00101
    a.size 5
    a.limbs 1
    b 01110
    a.check(n)   True
    a.set(n)     00101
    a.unset(n)   00100
    a.set_to(n)  00101
    a.flip(n)    00100
    a.is_zero()  False
    a.eq(b)      False
    a.cmp(b)     1
    a.copy()     00101
    r.zero()     00000
    not a        11010
    a and b      00100
    a or b       01111
    a xor b      01011
    a.rshift(n)  10000
    a.lshift(n)  00000
    a.first()           2
    a.next(n)           4
    a.first_diff(b)     1
    a.next_diff(b, n)   4
    a.hamming_weight()  2
    a.hamming_weight_sparse()  2
Got:
    a 00101
    a.size 5
    a.limbs 1
    b 01110
    a.check(n)   True
    a.set(n)     00101
    a.unset(n)   00100
    a.set_to(n)  00101
    a.flip(n)    00100
    a.is_zero()  False
    a.eq(b)      True
    a.cmp(b)     1
    a.copy()     00000
    r.zero()     00000
    not a        11010
    a and b      00100
    a or b       01111
    a xor b      01011
    a.rshift(n)  10000
    a.lshift(n)  00000
    a.first()           2
    a.next(n)           4
    a.first_diff(b)     1
    a.next_diff(b, n)   4
    a.hamming_weight()  2
    a.hamming_weight_sparse()  2
```


Issue created by migration from https://trac.sagemath.org/ticket/2719





---

archive/issue_comments_018746.json:
```json
{
    "body": "Attachment [2719-bitsets.patch](tarball://root/attachments/some-uuid/ticket2719/2719-bitsets.patch) by robertwb created at 2008-03-29 18:18:54",
    "created_at": "2008-03-29T18:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2719#issuecomment-18746",
    "user": "robertwb"
}
```

Attachment [2719-bitsets.patch](tarball://root/attachments/some-uuid/ticket2719/2719-bitsets.patch) by robertwb created at 2008-03-29 18:18:54



---

archive/issue_comments_018747.json:
```json
{
    "body": "fix endianness issues (thanks to cwitty for pointing this out)",
    "created_at": "2008-03-29T18:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2719#issuecomment-18747",
    "user": "robertwb"
}
```

fix endianness issues (thanks to cwitty for pointing this out)



---

archive/issue_comments_018748.json:
```json
{
    "body": "It works.",
    "created_at": "2008-03-29T18:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2719#issuecomment-18748",
    "user": "was"
}
```

It works.



---

archive/issue_comments_018749.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-29T18:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2719#issuecomment-18749",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018750.json:
```json
{
    "body": "Merged in Sage 2.11.rc0",
    "created_at": "2008-03-29T18:47:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2719",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2719#issuecomment-18750",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.rc0
