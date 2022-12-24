# Issue 6393: Jacobi sums incorrect when exactly one chacater is trivial

archive/issues_006393.json:
```json
{
    "body": "Assignee: tbd\n\nExample:\n\n\n```\nsage: G=DirichletGroup(5); X=G.list(); Y=X[0]; Z=X[1] \nsage: # Y is trivial and Z is quartic\nsage: sum([Y(x)*Z(1-x) for x in IntegerModRing(5)])\n -1\nsage: # The value -1 above is the correct value of the Jacobi sum J(Y, Z).\nsage: Y.jacobi_sum(Z);    Z.jacobi_sum(Y)\n0\n0\nsage: #The 0 values above are incorrect values of J(Y, Z).\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6393\n\n",
    "created_at": "2009-06-24T11:33:13Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "Jacobi sums incorrect when exactly one chacater is trivial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6393",
    "user": "wdj"
}
```
Assignee: tbd

Example:


```
sage: G=DirichletGroup(5); X=G.list(); Y=X[0]; Z=X[1] 
sage: # Y is trivial and Z is quartic
sage: sum([Y(x)*Z(1-x) for x in IntegerModRing(5)])
 -1
sage: # The value -1 above is the correct value of the Jacobi sum J(Y, Z).
sage: Y.jacobi_sum(Z);    Z.jacobi_sum(Y)
0
0
sage: #The 0 values above are incorrect values of J(Y, Z).
```


Issue created by migration from https://trac.sagemath.org/ticket/6393





---

archive/issue_comments_051366.json:
```json
{
    "body": "Attachment [trac_6393-jacobi-sum.patch](tarball://root/attachments/some-uuid/ticket6393/trac_6393-jacobi-sum.patch) by wdj created at 2009-06-24 14:41:07\n\napplies to 4.0.2.rc3 passes sage -testall",
    "created_at": "2009-06-24T14:41:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51366",
    "user": "wdj"
}
```

Attachment [trac_6393-jacobi-sum.patch](tarball://root/attachments/some-uuid/ticket6393/trac_6393-jacobi-sum.patch) by wdj created at 2009-06-24 14:41:07

applies to 4.0.2.rc3 passes sage -testall



---

archive/issue_comments_051367.json:
```json
{
    "body": "Changing component from algebra to modular forms.",
    "created_at": "2009-06-24T14:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51367",
    "user": "wdj"
}
```

Changing component from algebra to modular forms.



---

archive/issue_comments_051368.json:
```json
{
    "body": "Changing assignee from tbd to craigcitro.",
    "created_at": "2009-06-24T14:42:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51368",
    "user": "wdj"
}
```

Changing assignee from tbd to craigcitro.



---

archive/issue_comments_051369.json:
```json
{
    "body": "Looks good to me, and doctests pass. I'm surprised this went so long without being spotted.",
    "created_at": "2009-07-14T19:36:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51369",
    "user": "davidloeffler"
}
```

Looks good to me, and doctests pass. I'm surprised this went so long without being spotted.



---

archive/issue_comments_051370.json:
```json
{
    "body": "BTW, in the course of reviewing this I've realised that our Jacobi sum algorithm is absurdly slow, vastly slower than calculating the sums directly! I've just opened #6534 for this.",
    "created_at": "2009-07-14T19:56:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51370",
    "user": "davidloeffler"
}
```

BTW, in the course of reviewing this I've realised that our Jacobi sum algorithm is absurdly slow, vastly slower than calculating the sums directly! I've just opened #6534 for this.



---

archive/issue_comments_051371.json:
```json
{
    "body": "I'm about to upload a patch at #6534 which totally changes the way we calculate Jacobi sums, thus superseding this patch somewhat. I've made sure that it takes into account the issue you raised here.",
    "created_at": "2009-07-14T20:18:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51371",
    "user": "davidloeffler"
}
```

I'm about to upload a patch at #6534 which totally changes the way we calculate Jacobi sums, thus superseding this patch somewhat. I've made sure that it takes into account the issue you raised here.



---

archive/issue_comments_051372.json:
```json
{
    "body": "Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(",
    "created_at": "2009-07-16T16:33:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51372",
    "user": "mvngu"
}
```

Just to let people know, this has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(



---

archive/issue_comments_051373.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-16T21:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51373",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_051374.json:
```json
{
    "body": "See #6613 for a follow up to this ticket.",
    "created_at": "2009-07-24T14:40:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6393",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6393#issuecomment-51374",
    "user": "mvngu"
}
```

See #6613 for a follow up to this ticket.
