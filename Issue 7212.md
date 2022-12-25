# Issue 7212: [with patch, needs review] steenrod algebra multiplication bug

archive/issues_007212.json:
```json
{
    "body": "Assignee: tbd\n\nFrom sage-support:\n\n```\nI have Sage 4.1.1 install on a server, and I run the following code, \nwhich outputs the following error: \nsage: A3=SteenrodAlgebra(3) \nsage: A3.P(36,6)*A3.P(27,9,81) \n--------------------------------------------------------------------------- \nKeyError                                  Traceback (most recent call \nlast) \n/home/user_bob/<ipython console> in <module>() \n/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/structure/ \nelement.so in sage.structure.element.RingElement.__mul__ (sage/ \nstructure/element.c:9956)() \n/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/structure/ \nelement.so in sage.structure.element.RingElement._mul_ (sage/structure/ \nelement.c:10021)() \n/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/ \nsteenrod_algebra_element.pyc in _mul_(self, other) \n    925                         new_dict = milnor_multiplication \n(mono1, mono2) \n    926                     else: \n--> 927                         new_dict = milnor_multiplication_odd \n(mono1, mono2, p=p) \n    928                     for new_mono in new_dict: \n    929                         if result.has_key(new_mono): \n/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/ \nsteenrod_milnor_multiplication_odd.pyc in milnor_multiplication_odd \n(m1, m2, p) \n    225                     t = tuple(diagonal[:i+1]) \n    226                     if result.has_key((e,t)): \n--> 227                         result[(e,t)] = F(coeff + result[t]) \n    228                     else: \n    229                         result[(e,t)] = F(coeff) \nKeyError: (26, 8, 86) \n```\nThis is because of a simple bug: instead of `result[t]`, it should be `result[(e,t)]`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7212\n\n",
    "created_at": "2009-10-14T19:12:43Z",
    "labels": [
        "component: algebra",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review] steenrod algebra multiplication bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7212",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

From sage-support:

```
I have Sage 4.1.1 install on a server, and I run the following code, 
which outputs the following error: 
sage: A3=SteenrodAlgebra(3) 
sage: A3.P(36,6)*A3.P(27,9,81) 
--------------------------------------------------------------------------- 
KeyError                                  Traceback (most recent call 
last) 
/home/user_bob/<ipython console> in <module>() 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/structure/ 
element.so in sage.structure.element.RingElement.__mul__ (sage/ 
structure/element.c:9956)() 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/structure/ 
element.so in sage.structure.element.RingElement._mul_ (sage/structure/ 
element.c:10021)() 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/ 
steenrod_algebra_element.pyc in _mul_(self, other) 
    925                         new_dict = milnor_multiplication 
(mono1, mono2) 
    926                     else: 
--> 927                         new_dict = milnor_multiplication_odd 
(mono1, mono2, p=p) 
    928                     for new_mono in new_dict: 
    929                         if result.has_key(new_mono): 
/usr/local/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/ 
steenrod_milnor_multiplication_odd.pyc in milnor_multiplication_odd 
(m1, m2, p) 
    225                     t = tuple(diagonal[:i+1]) 
    226                     if result.has_key((e,t)): 
--> 227                         result[(e,t)] = F(coeff + result[t]) 
    228                     else: 
    229                         result[(e,t)] = F(coeff) 
KeyError: (26, 8, 86) 
```
This is because of a simple bug: instead of `result[t]`, it should be `result[(e,t)]`.


Issue created by migration from https://trac.sagemath.org/ticket/7212





---

archive/issue_comments_059732.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-14T21:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7212#issuecomment-59732",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059733.json:
```json
{
    "body": "Attachment [trac_7212-steenrod.patch](tarball://root/attachments/some-uuid/ticket7212/trac_7212-steenrod.patch) by @jasongrout created at 2009-10-14 21:20:35",
    "created_at": "2009-10-14T21:20:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7212#issuecomment-59733",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac_7212-steenrod.patch](tarball://root/attachments/some-uuid/ticket7212/trac_7212-steenrod.patch) by @jasongrout created at 2009-10-14 21:20:35



---

archive/issue_comments_059734.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-14T21:50:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7212#issuecomment-59734",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_059735.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T08:52:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7212",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7212#issuecomment-59735",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017087.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T08:52:13Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7212",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7212#event-17087"
}
```
