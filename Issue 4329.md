# Issue 4329: class numbers of non-maximal orders -- should return NotImplementedError for now

archive/issues_004329.json:
```json
{
    "body": "Assignee: was\n\nThis is just wrong (and easy to fix):\n\n```\nsage: R = ZZ[3*sqrt(-3)]\nsage: R.class_number??\nType:           instancemethod\nBase Class:     <type 'instancemethod'>\nString Form:    <bound method AbsoluteOrder.class_number of Order in Number Field in a with defining polynomial x^2 + 27>\nNamespace:      Interactive\nFile:           /home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/number_field/order.py\nDefinition:     R.class_number(self, proof=None)\nSource:\n    def class_number(self, proof=None):\n        \"\"\"\n        EXAMPLES:\n            sage: ZZ[2^(1/3)].class_number()\n            1\n            sage: ZZ[sqrt(-23)].class_number()\n            3\n        \"\"\"\n        return self.number_field().class_number(proof=proof)   \n```\n\n\nFor a non-maximal order, the class_number (and class group) commands should return NotImplementedError, rather than give a wrong or meaningless answer.\n\nTo fix this, all you have to do is make these function raise NotImplementedError, except in the case of the maximal order.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4329\n\n",
    "created_at": "2008-10-20T13:36:36Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "class numbers of non-maximal orders -- should return NotImplementedError for now",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4329",
    "user": "was"
}
```
Assignee: was

This is just wrong (and easy to fix):

```
sage: R = ZZ[3*sqrt(-3)]
sage: R.class_number??
Type:           instancemethod
Base Class:     <type 'instancemethod'>
String Form:    <bound method AbsoluteOrder.class_number of Order in Number Field in a with defining polynomial x^2 + 27>
Namespace:      Interactive
File:           /home2/sage/build/sage-3.1.4/local/lib/python2.5/site-packages/sage/rings/number_field/order.py
Definition:     R.class_number(self, proof=None)
Source:
    def class_number(self, proof=None):
        """
        EXAMPLES:
            sage: ZZ[2^(1/3)].class_number()
            1
            sage: ZZ[sqrt(-23)].class_number()
            3
        """
        return self.number_field().class_number(proof=proof)   
```


For a non-maximal order, the class_number (and class group) commands should return NotImplementedError, rather than give a wrong or meaningless answer.

To fix this, all you have to do is make these function raise NotImplementedError, except in the case of the maximal order.

Issue created by migration from https://trac.sagemath.org/ticket/4329





---

archive/issue_comments_031751.json:
```json
{
    "body": "Attachment [sage-4329.patch](tarball://root/attachments/some-uuid/ticket4329/sage-4329.patch) by shumow created at 2008-11-15 02:13:05\n\nCode looks good.\nConfirmed that it worked.\nConfirmed that it passes tests.",
    "created_at": "2008-11-15T02:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4329#issuecomment-31751",
    "user": "shumow"
}
```

Attachment [sage-4329.patch](tarball://root/attachments/some-uuid/ticket4329/sage-4329.patch) by shumow created at 2008-11-15 02:13:05

Code looks good.
Confirmed that it worked.
Confirmed that it passes tests.



---

archive/issue_comments_031752.json:
```json
{
    "body": "Replying to [comment:2 shumow]:\n> Code looks good.\n> Confirmed that it worked.\n> Confirmed that it passes tests.\n\nIs that a positive review?\n\nCheers,\n\nMichael",
    "created_at": "2008-11-15T02:21:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4329#issuecomment-31752",
    "user": "mabshoff"
}
```

Replying to [comment:2 shumow]:
> Code looks good.
> Confirmed that it worked.
> Confirmed that it passes tests.

Is that a positive review?

Cheers,

Michael



---

archive/issue_comments_031753.json:
```json
{
    "body": "Replying to [comment:3 mabshoff]:\n> Replying to [comment:2 shumow]:\n> > Code looks good.\n> > Confirmed that it worked.\n> > Confirmed that it passes tests.\n> \n> Is that a positive review?\n> \nAffirmative",
    "created_at": "2008-11-15T08:31:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4329#issuecomment-31753",
    "user": "shumow"
}
```

Replying to [comment:3 mabshoff]:
> Replying to [comment:2 shumow]:
> > Code looks good.
> > Confirmed that it worked.
> > Confirmed that it passes tests.
> 
> Is that a positive review?
> 
Affirmative



---

archive/issue_comments_031754.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-15T09:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4329#issuecomment-31754",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_031755.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-15T09:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4329",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4329#issuecomment-31755",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.rc1
