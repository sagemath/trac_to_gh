# Issue 5560: [with patch, needs review] NTL interface missing wrappers for vec_GF2 type and GF2X::MinPolySeq

archive/issues_005560.json:
```json
{
    "body": "Assignee: @rhinton\n\nCC:  @malb\n\nI want to use the `GF2X::MinPolySeq` function from my Cython application in Sage, but the function declaration and input data type, vec_GF2, are not included in the current NTL interface shim.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5560\n\n",
    "created_at": "2009-03-18T16:38:46Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, needs review] NTL interface missing wrappers for vec_GF2 type and GF2X::MinPolySeq",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5560",
    "user": "https://github.com/rhinton"
}
```
Assignee: @rhinton

CC:  @malb

I want to use the `GF2X::MinPolySeq` function from my Cython application in Sage, but the function declaration and input data type, vec_GF2, are not included in the current NTL interface shim.


Issue created by migration from https://trac.sagemath.org/ticket/5560





---

archive/issue_comments_043186.json:
```json
{
    "body": "malb, is there a good way to handle the C++ overloading?  For example, in the patch I commented out one of the `put` methods (and I'm not sure if I picked the right one).",
    "created_at": "2009-03-18T16:43:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5560#issuecomment-43186",
    "user": "https://github.com/rhinton"
}
```

malb, is there a good way to handle the C++ overloading?  For example, in the patch I commented out one of the `put` methods (and I'm not sure if I picked the right one).



---

archive/issue_comments_043187.json:
```json
{
    "body": "You'd have to define two functions:\n\n\n```\nvoid  (*put_G \"put\") (long i, GF2_c a)\nvoid  (*put_l \"put\") (long i, long a)\n```\n\n\nand tell it that they are pointing to the same thing ('put')",
    "created_at": "2009-03-18T20:44:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5560#issuecomment-43187",
    "user": "https://github.com/malb"
}
```

You'd have to define two functions:


```
void  (*put_G "put") (long i, GF2_c a)
void  (*put_l "put") (long i, long a)
```


and tell it that they are pointing to the same thing ('put')



---

archive/issue_comments_043188.json:
```json
{
    "body": "Attachment [trac_5560_ntl_vec_GF2_MinPolySeq.patch](tarball://root/attachments/some-uuid/ticket5560/trac_5560_ntl_vec_GF2_MinPolySeq.patch) by @rhinton created at 2009-03-23 18:01:27\n\nI split out the two cases into put_GF2 and put_long.  Anything other suggestions for positive review? :-)",
    "created_at": "2009-03-23T18:01:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5560#issuecomment-43188",
    "user": "https://github.com/rhinton"
}
```

Attachment [trac_5560_ntl_vec_GF2_MinPolySeq.patch](tarball://root/attachments/some-uuid/ticket5560/trac_5560_ntl_vec_GF2_MinPolySeq.patch) by @rhinton created at 2009-03-23 18:01:27

I split out the two cases into put_GF2 and put_long.  Anything other suggestions for positive review? :-)



---

archive/issue_comments_043189.json:
```json
{
    "body": "Patch looks good and doesn't add any run-able code anyway.",
    "created_at": "2009-03-25T11:29:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5560#issuecomment-43189",
    "user": "https://github.com/malb"
}
```

Patch looks good and doesn't add any run-able code anyway.



---

archive/issue_comments_043190.json:
```json
{
    "body": "Merged in Sage 3.4.1.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-25T23:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5560#issuecomment-43190",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael



---

archive/issue_comments_043191.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-25T23:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5560",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5560#issuecomment-43191",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
