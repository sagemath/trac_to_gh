# Issue 5182: Strange Symmetrica segfault

archive/issues_005182.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  @jbandlow sage-combinat\n\nKeywords: symmetrica\n\nThis is from sagenb running sage 3.3.alpha3:\n\n\n```\nsage: dd = { Partition([1]) : 1 } ; ee = { Partition([1]) : int(1) } ; s = SFASchur(QQ)\nsage: (s._from_dict(dd), s._from_dict(ee)) # This is fine\n(s[1], s[1])\nsage: 1 * s._from_dict(dd) # This is fine\ns[1]\nsage: 1 * s._from_dict(ee) # This fails\nException exceptions.TypeError: 'cannot convert a (= 1) to OP' in\n'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored\nfunction: mult(1) \npython: \ufffd73x\ufffd\ufffd\nConnection to localhost closed.\n```\n\n\n\nThis is a low priority for me, since the obvious workaround is not to put 'int's in this kind of dictionary, but I wanted to report it.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5182\n\n",
    "created_at": "2009-02-04T22:49:42Z",
    "labels": [
        "combinatorics",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Strange Symmetrica segfault",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5182",
    "user": "@jbandlow"
}
```
Assignee: @mwhansen

CC:  @jbandlow sage-combinat

Keywords: symmetrica

This is from sagenb running sage 3.3.alpha3:


```
sage: dd = { Partition([1]) : 1 } ; ee = { Partition([1]) : int(1) } ; s = SFASchur(QQ)
sage: (s._from_dict(dd), s._from_dict(ee)) # This is fine
(s[1], s[1])
sage: 1 * s._from_dict(dd) # This is fine
s[1]
sage: 1 * s._from_dict(ee) # This fails
Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in
'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
function: mult(1) 
python: �73x��
Connection to localhost closed.
```



This is a low priority for me, since the obvious workaround is not to put 'int's in this kind of dictionary, but I wanted to report it.

Issue created by migration from https://trac.sagemath.org/ticket/5182





---

archive/issue_comments_039743.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-05-06T14:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5182#issuecomment-39743",
    "user": "@jbandlow"
}
```

Changing priority from minor to major.



---

archive/issue_comments_039744.json:
```json
{
    "body": "Replying to [ticket:5182 jbandlow]:\n> This is from sagenb running sage 3.3.alpha3:\n> \n> {{{\n> sage: dd = { Partition([1]) : 1 } ; ee = { Partition([1]) : int(1) } ; s = SFASchur(QQ)\n> sage: (s._from_dict(dd), s._from_dict(ee)) # This is fine\n> (s[1], s[1])\n> sage: 1 * s._from_dict(dd) # This is fine\n> s[1]\n> sage: 1 * s._from_dict(ee) # This fails\n> Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in\n> 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored\n> function: mult(1) \n> python: \ufffd73x\ufffd\ufffd\n> Connection to localhost closed.\n> }}}\n> \n> \n> This is a low priority for me, since the obvious workaround is not to put 'int's in this kind of dictionary, but I wanted to report it.\n\nUpdate in sage-4.4.  This bug can occur without using private methods.\n\n```\nsage: sage: s = SymmetricFunctions(QQ).schur()\nsage: sage: s.sum_of_terms([ (Partition([i]), i) for i in range(3) ])\ns[1] + 2*s[2]\nsage: sage: s.sum_of_terms([ (Partition([i]), i) for i in range(3) ]) * 1\nException TypeError: 'cannot convert a (= 1) to OP' in 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored\nfunction: mult_bruch(2) not definied for object type:\nkind of object is empty-object\npython: function: mult_bruch(2) not definied for object type:\n: Operation not permitted\n```\n\n\nThis is a segfault and exits sage.",
    "created_at": "2010-05-06T14:03:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5182#issuecomment-39744",
    "user": "@jbandlow"
}
```

Replying to [ticket:5182 jbandlow]:
> This is from sagenb running sage 3.3.alpha3:
> 
> {{{
> sage: dd = { Partition([1]) : 1 } ; ee = { Partition([1]) : int(1) } ; s = SFASchur(QQ)
> sage: (s._from_dict(dd), s._from_dict(ee)) # This is fine
> (s[1], s[1])
> sage: 1 * s._from_dict(dd) # This is fine
> s[1]
> sage: 1 * s._from_dict(ee) # This fails
> Exception exceptions.TypeError: 'cannot convert a (= 1) to OP' in
> 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
> function: mult(1) 
> python: �73x��
> Connection to localhost closed.
> }}}
> 
> 
> This is a low priority for me, since the obvious workaround is not to put 'int's in this kind of dictionary, but I wanted to report it.

Update in sage-4.4.  This bug can occur without using private methods.

```
sage: sage: s = SymmetricFunctions(QQ).schur()
sage: sage: s.sum_of_terms([ (Partition([i]), i) for i in range(3) ])
s[1] + 2*s[2]
sage: sage: s.sum_of_terms([ (Partition([i]), i) for i in range(3) ]) * 1
Exception TypeError: 'cannot convert a (= 1) to OP' in 'sage.libs.symmetrica.symmetrica._op_schur_general_dict' ignored
function: mult_bruch(2) not definied for object type:
kind of object is empty-object
python: function: mult_bruch(2) not definied for object type:
: Operation not permitted
```


This is a segfault and exits sage.



---

archive/issue_comments_039745.json:
```json
{
    "body": "These errors do not occur with sage 4.6.2.",
    "created_at": "2011-03-14T18:59:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5182#issuecomment-39745",
    "user": "@jbandlow"
}
```

These errors do not occur with sage 4.6.2.



---

archive/issue_comments_039746.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-03-14T21:43:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5182#issuecomment-39746",
    "user": "@mwhansen"
}
```

Resolution: invalid
