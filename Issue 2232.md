# Issue 2232: Bug in 'digits' function for Integers

archive/issues_002232.json:
```json
{
    "body": "Assignee: somebody\n\nThis works\n\n```\nsage: 1.digits(16,'0123456789abcdef')\n['1']\nsage: 2.digits(16,'0123456789abcdef')\n['2']\n```\nbut this don't\n\n```\nsage: 0.digits(16,'0123456789abcdef')\n[]\n```\n\nThe problem exists for all bases. The '0'-value is never returned.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2232\n\n",
    "created_at": "2008-02-20T14:11:38Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "Bug in 'digits' function for Integers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2232",
    "user": "https://github.com/m-r-k"
}
```
Assignee: somebody

This works

```
sage: 1.digits(16,'0123456789abcdef')
['1']
sage: 2.digits(16,'0123456789abcdef')
['2']
```
but this don't

```
sage: 0.digits(16,'0123456789abcdef')
[]
```

The problem exists for all bases. The '0'-value is never returned.

Issue created by migration from https://trac.sagemath.org/ticket/2232





---

archive/issue_events_005313.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-02-20T16:27:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "milestone": "sage-2.10.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2232#event-5313"
}
```



---

archive/issue_comments_014751.json:
```json
{
    "body": "I agree that this is a bug since we have symbols to represent zero so we should use them.",
    "created_at": "2008-02-20T16:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14751",
    "user": "https://github.com/malb"
}
```

I agree that this is a bug since we have symbols to represent zero so we should use them.



---

archive/issue_comments_014752.json:
```json
{
    "body": "This might be relevant to #2170 (or the other way around)",
    "created_at": "2008-02-20T16:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14752",
    "user": "https://github.com/robertwb"
}
```

This might be relevant to #2170 (or the other way around)



---

archive/issue_comments_014753.json:
```json
{
    "body": "I'm supposing that the poster of this bug wants:\n\n```\nsage: 0.digits(16,'0123456789abcdef')\n['0']\n```\n\nI do not like that.  I think one should use str for this (witness 2.10.2's current operation):  \n\n```\nsage: 0.str(10)\n'0'\nsage: f=0.str(10)\nsage: [c for c in f]\n['0']\n```\n\nI don't think that what I suggested is a perfect analog for what may have desired, but I don't like the inconsistency that this desired \"fix\" introduces for digits.",
    "created_at": "2008-03-01T16:41:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14753",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I'm supposing that the poster of this bug wants:

```
sage: 0.digits(16,'0123456789abcdef')
['0']
```

I do not like that.  I think one should use str for this (witness 2.10.2's current operation):  

```
sage: 0.str(10)
'0'
sage: f=0.str(10)
sage: [c for c in f]
['0']
```

I don't think that what I suggested is a perfect analog for what may have desired, but I don't like the inconsistency that this desired "fix" introduces for digits.



---

archive/issue_comments_014754.json:
```json
{
    "body": "This example above (base=16) is from the docstring.\nYou're right that you should use \".str\" if you just want to get the string representation of a number in a given base.\n\nBut the digits function can do more. It can take any indexable object as source for the digits.\nSo i think this is really a bug which should be fixed, because this \n\n```\nsage: 0.digits(11,'pleasefixme')\n```\nshould return\n\n```\n['p']\n```",
    "created_at": "2008-03-02T10:53:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14754",
    "user": "https://github.com/m-r-k"
}
```

This example above (base=16) is from the docstring.
You're right that you should use ".str" if you just want to get the string representation of a number in a given base.

But the digits function can do more. It can take any indexable object as source for the digits.
So i think this is really a bug which should be fixed, because this 

```
sage: 0.digits(11,'pleasefixme')
```
should return

```
['p']
```



---

archive/issue_comments_014755.json:
```json
{
    "body": "I see that there is some precedent for agreeing that this is a bug:\n\n```\nsage: 0.ndigits()\n1\n```\nGiven my opinion that this bug is invalid, I would also want to change ndigits.  While on the subject of digits and ndigits, I think it is really awful that their default bases are not the same.",
    "created_at": "2008-03-03T19:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14755",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I see that there is some precedent for agreeing that this is a bug:

```
sage: 0.ndigits()
1
```
Given my opinion that this bug is invalid, I would also want to change ndigits.  While on the subject of digits and ndigits, I think it is really awful that their default bases are not the same.



---

archive/issue_comments_014756.json:
```json
{
    "body": "Attachment [digits__bugfix_and_adds_padto.patch](tarball://root/attachments/some-uuid/ticket2232/digits__bugfix_and_adds_padto.patch) by @m-r-k created at 2008-04-04 08:58:05\n\nThe patches fixes the issue and adds a padto-parameter,\n\nsee discussion [http://groups.google.com/group/sage-devel/browse_thread/thread/f9d7b5016e237b22](http://groups.google.com/group/sage-devel/browse_thread/thread/f9d7b5016e237b22)",
    "created_at": "2008-04-04T08:58:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14756",
    "user": "https://github.com/m-r-k"
}
```

Attachment [digits__bugfix_and_adds_padto.patch](tarball://root/attachments/some-uuid/ticket2232/digits__bugfix_and_adds_padto.patch) by @m-r-k created at 2008-04-04 08:58:05

The patches fixes the issue and adds a padto-parameter,

see discussion [http://groups.google.com/group/sage-devel/browse_thread/thread/f9d7b5016e237b22](http://groups.google.com/group/sage-devel/browse_thread/thread/f9d7b5016e237b22)



---

archive/issue_comments_014757.json:
```json
{
    "body": "With-out applying and running the code, I have some comments.\n\n 1) I do not like the change in semantics when the digits are passed in.  I think that is way too arbitrary.  Essentially, you are overriding the default to padto when digits are passed in and making it default padto=1.\n\n 2) The \"zero = 0\" in the snippet below will create a python int with 0 -- it should be a sage int.  Use the_integer_ring._zero_element\n\n```\n \nif digits is None: \n    zero = 0           # value for padding \nelse: \n    zero = digits[0]   # value for padding \n```\n\n 3) Could you also in this patch change ndigits so it returns 0 for 0?  I think that accurately reflects the will of sage-devel and fits in this patch nicely.\n\nThanks for coding this patch up!",
    "created_at": "2008-04-04T11:18:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14757",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

With-out applying and running the code, I have some comments.

 1) I do not like the change in semantics when the digits are passed in.  I think that is way too arbitrary.  Essentially, you are overriding the default to padto when digits are passed in and making it default padto=1.

 2) The "zero = 0" in the snippet below will create a python int with 0 -- it should be a sage int.  Use the_integer_ring._zero_element

```
 
if digits is None: 
    zero = 0           # value for padding 
else: 
    zero = digits[0]   # value for padding 
```

 3) Could you also in this patch change ndigits so it returns 0 for 0?  I think that accurately reflects the will of sage-devel and fits in this patch nicely.

Thanks for coding this patch up!



---

archive/issue_comments_014758.json:
```json
{
    "body": "Attachment [fix_for_digits_patch_and_bugfix_for_ndigits.patch](tarball://root/attachments/some-uuid/ticket2232/fix_for_digits_patch_and_bugfix_for_ndigits.patch) by @m-r-k created at 2008-04-04 11:38:04\n\nthe second (additional) patch takes care of jbmohler's remarks.",
    "created_at": "2008-04-04T11:38:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14758",
    "user": "https://github.com/m-r-k"
}
```

Attachment [fix_for_digits_patch_and_bugfix_for_ndigits.patch](tarball://root/attachments/some-uuid/ticket2232/fix_for_digits_patch_and_bugfix_for_ndigits.patch) by @m-r-k created at 2008-04-04 11:38:04

the second (additional) patch takes care of jbmohler's remarks.



---

archive/issue_comments_014759.json:
```json
{
    "body": "I applied both patches, checked it out a bit and give a positive review.",
    "created_at": "2008-04-04T12:49:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14759",
    "user": "https://trac.sagemath.org/admin/accounts/users/jbmohler"
}
```

I applied both patches, checked it out a bit and give a positive review.



---

archive/issue_events_005314.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-04T18:14:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2232#event-5314"
}
```



---

archive/issue_comments_014760.json:
```json
{
    "body": "Doctests pass. Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-04T18:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14760",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Doctests pass. Merged in Sage 3.0.alpha1



---

archive/issue_comments_014761.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-04T18:14:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2232",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2232#issuecomment-14761",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
