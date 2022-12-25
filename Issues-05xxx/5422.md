# Issue 5422: Quadratic forms polynomial

archive/issues_005422.json:
```json
{
    "body": "Assignee: justin\n\nKeywords: quadratic forms\n\nGiven a quadratic form Q over the ring R of dimension n, this returns the polynomial form in n variables over R.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/5422\n\n",
    "closed_at": "2010-11-11T13:01:38Z",
    "created_at": "2009-03-02T19:25:09Z",
    "labels": [
        "component: quadratic forms",
        "trivial"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Quadratic forms polynomial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5422",
    "user": "https://github.com/adeines"
}
```
Assignee: justin

Keywords: quadratic forms

Given a quadratic form Q over the ring R of dimension n, this returns the polynomial form in n variables over R.  

Issue created by migration from https://trac.sagemath.org/ticket/5422





---

archive/issue_comments_041868.json:
```json
{
    "body": "polynomial of a quadratic form patch",
    "created_at": "2009-03-02T19:25:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41868",
    "user": "https://github.com/adeines"
}
```

polynomial of a quadratic form patch



---

archive/issue_comments_041869.json:
```json
{
    "body": "Attachment [11731.patch](tarball://root/attachments/some-uuid/ticket5422/11731.patch) by @williamstein created at 2009-03-16 00:24:02\n\nREFEREE REPORT:\n\n\n* change it to \n\n```\n  EXAMPLES::\n  \n      sage: stuff\n```\nfor the new ReST format.\n\n* Don't hardcode only x, i.e., change this:\n\n```\npolynomial(self):\n```\nto \n\n```\npolynomial(self, names='x'):\n```\n\nYes, \"names\" sounds funny, but is traditional in sage for this.\n\n* Change \"Input:\" and \"Output:\" to be all caps and on their own line, like in the rest of sage. \n\n* This is silly code `[R.gens()[i] for i in range(n)]` because `R.gens()` is almost the same thing.  If you really need a list do `list(R.gens())`.\n\n* This worries me: `(M*V).dot_product(V) `.  Should it be `(V*M).dot_product(V)`?",
    "created_at": "2009-03-16T00:24:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41869",
    "user": "https://github.com/williamstein"
}
```

Attachment [11731.patch](tarball://root/attachments/some-uuid/ticket5422/11731.patch) by @williamstein created at 2009-03-16 00:24:02

REFEREE REPORT:


* change it to 

```
  EXAMPLES::
  
      sage: stuff
```
for the new ReST format.

* Don't hardcode only x, i.e., change this:

```
polynomial(self):
```
to 

```
polynomial(self, names='x'):
```

Yes, "names" sounds funny, but is traditional in sage for this.

* Change "Input:" and "Output:" to be all caps and on their own line, like in the rest of sage. 

* This is silly code `[R.gens()[i] for i in range(n)]` because `R.gens()` is almost the same thing.  If you really need a list do `list(R.gens())`.

* This worries me: `(M*V).dot_product(V) `.  Should it be `(V*M).dot_product(V)`?



---

archive/issue_comments_041870.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-04T21:16:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41870",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041871.json:
```json
{
    "body": "Two things:\nYou need to list 'names' under the input section of the docstring.\nSecondly, you forgot a period in your error message.\n\nOtherwise good :-)",
    "created_at": "2010-11-05T16:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41871",
    "user": "https://github.com/haikona"
}
```

Two things:
You need to list 'names' under the input section of the docstring.
Secondly, you forgot a period in your error message.

Otherwise good :-)



---

archive/issue_comments_041872.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-05T16:22:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41872",
    "user": "https://github.com/haikona"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041873.json:
```json
{
    "body": "Replaces previous patch.",
    "created_at": "2010-11-05T16:40:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41873",
    "user": "https://github.com/haikona"
}
```

Replaces previous patch.



---

archive/issue_comments_041874.json:
```json
{
    "body": "Attachment [trac_5422_quad_form_poly_reviewer.patch](tarball://root/attachments/some-uuid/ticket5422/trac_5422_quad_form_poly_reviewer.patch) by @haikona created at 2010-11-05 16:42:46\n\nDone the docstring updating. A review and we should be good to go.",
    "created_at": "2010-11-05T16:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41874",
    "user": "https://github.com/haikona"
}
```

Attachment [trac_5422_quad_form_poly_reviewer.patch](tarball://root/attachments/some-uuid/ticket5422/trac_5422_quad_form_poly_reviewer.patch) by @haikona created at 2010-11-05 16:42:46

Done the docstring updating. A review and we should be good to go.



---

archive/issue_comments_041875.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-05T16:42:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41875",
    "user": "https://github.com/haikona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041876.json:
```json
{
    "body": "After the error message had the grammer fixed (a period was added) the doctest needed that as well.  This is fixed in the current patch.",
    "created_at": "2010-11-05T18:38:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41876",
    "user": "https://github.com/adeines"
}
```

After the error message had the grammer fixed (a period was added) the doctest needed that as well.  This is fixed in the current patch.



---

archive/issue_comments_041877.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-05T21:41:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41877",
    "user": "https://github.com/haikona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041878.json:
```json
{
    "body": "Please change the commit message of the third patch.  Currently it says \"added a period to the doc test\", but that applies only to the last changes made, not the whole patch.  If a patch *replaces* previous patches, the commit message should be clear by itself.",
    "created_at": "2010-11-07T10:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41878",
    "user": "https://github.com/jdemeyer"
}
```

Please change the commit message of the third patch.  Currently it says "added a period to the doc test", but that applies only to the last changes made, not the whole patch.  If a patch *replaces* previous patches, the commit message should be clear by itself.



---

archive/issue_comments_041879.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-07T10:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41879",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_041880.json:
```json
{
    "body": "I changed the commit message to apply the the whole patch.",
    "created_at": "2010-11-10T06:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41880",
    "user": "https://github.com/adeines"
}
```

I changed the commit message to apply the the whole patch.



---

archive/issue_comments_041881.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-10T06:31:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41881",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041882.json:
```json
{
    "body": "Attachment [trac_5422_quad_form_poly.patch](tarball://root/attachments/some-uuid/ticket5422/trac_5422_quad_form_poly.patch) by @adeines created at 2010-11-10 17:56:58\n\nReplaces previous patch.",
    "created_at": "2010-11-10T17:56:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41882",
    "user": "https://github.com/adeines"
}
```

Attachment [trac_5422_quad_form_poly.patch](tarball://root/attachments/some-uuid/ticket5422/trac_5422_quad_form_poly.patch) by @adeines created at 2010-11-10 17:56:58

Replaces previous patch.



---

archive/issue_comments_041883.json:
```json
{
    "body": "I have fixed the comment to apply to the whole patch.",
    "created_at": "2010-11-10T17:57:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41883",
    "user": "https://github.com/adeines"
}
```

I have fixed the comment to apply to the whole patch.



---

archive/issue_comments_041884.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-10T18:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41884",
    "user": "https://github.com/haikona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041885.json:
```json
{
    "body": "This latest version looks good to me.",
    "created_at": "2010-11-10T18:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41885",
    "user": "https://github.com/haikona"
}
```

This latest version looks good to me.



---

archive/issue_events_012637.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-11T13:01:38Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5422#event-12637"
}
```



---

archive/issue_comments_041886.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-11T13:01:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41886",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_comments_041887.json:
```json
{
    "body": "I have some issues with this patch, which I hope will get fixed in a followup patch:\n\n1. The ReST formatting is wrong for the list of inputs:\n\n```\n        1125\t            -'self' - a quadratic form over a commatitive ring. \n \t1126\t            -'names' - the name of the variables. Digits will be appended to the name for each different canonical \n \t1127\t            variable e.g x1, x2, x3 etc. \n```\nbut it should be\n\n```\n        1125\t            - 'self' - a quadratic form over a commatitive ring. \n \t1126\t            - 'names' - the name of the variables. Digits will be appended to the name for each different canonical \n \t1127\t              variable e.g x1, x2, x3 etc. \n```\n\nNote the space after dash and the matching indention right before \"variable\".\n\n2. I do not like this naked except, and think except: should almost never be used in Python:\n\n```\n        1160\t        try: \n \t1161\t            R = PolynomialRing(self.base_ring(),names,n) \n \t1162\t        except: \n \t1163\t            raise ValueError, 'Can only create polynomial rings over commutative rings.' \n```\nHow do you know that the error in creating the polynomial ring was due to poly ring not working because the ring is not commutative?   I would actually recommend just changing the above to:\n\n```\n                    R = PolynomialRing(self.base_ring(),names,n)\n```\nand completely get rid of the exception.     A proper exception will get raised by the PolynomialRing function itself.",
    "created_at": "2010-11-22T23:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5422",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5422#issuecomment-41887",
    "user": "https://github.com/williamstein"
}
```

I have some issues with this patch, which I hope will get fixed in a followup patch:

1. The ReST formatting is wrong for the list of inputs:

```
        1125	            -'self' - a quadratic form over a commatitive ring. 
 	1126	            -'names' - the name of the variables. Digits will be appended to the name for each different canonical 
 	1127	            variable e.g x1, x2, x3 etc. 
```
but it should be

```
        1125	            - 'self' - a quadratic form over a commatitive ring. 
 	1126	            - 'names' - the name of the variables. Digits will be appended to the name for each different canonical 
 	1127	              variable e.g x1, x2, x3 etc. 
```

Note the space after dash and the matching indention right before "variable".

2. I do not like this naked except, and think except: should almost never be used in Python:

```
        1160	        try: 
 	1161	            R = PolynomialRing(self.base_ring(),names,n) 
 	1162	        except: 
 	1163	            raise ValueError, 'Can only create polynomial rings over commutative rings.' 
```
How do you know that the error in creating the polynomial ring was due to poly ring not working because the ring is not commutative?   I would actually recommend just changing the above to:

```
                    R = PolynomialRing(self.base_ring(),names,n)
```
and completely get rid of the exception.     A proper exception will get raised by the PolynomialRing function itself.
