# Issue 803: Tests for what kind of an element something is should test the parent

archive/issues_000803.json:
```json
{
    "body": "Assignee: somebody\n\nCalls like:\n\n```\nalgebras/algebra_order.py:        elif isinstance(x, RingElement) and x in self.base_ring():\nalgebras/algebra_order_ideal.py:        elif isinstance(x, RingElement) and x in self.base_ring():\nalgebras/free_algebra_quotient_element.py:        elif isinstance(x, RingElement) and not isinstance(x, AlgebraElement) and x in R:\nrings/infinity.py:        elif isinstance(x, RingElement) or isinstance(x, (int,long,float,complex)):\nrings/infinity.py:        elif isinstance(x, RingElement):\n```\n\n\nshould actually be checking to see if the parents are of the appropriate type.  The element types are not always reliable: parents more accurately reflect the mathematical structure (mostly because they can have multiple inheritance).\n\nThere may be more instances in addition to those above (I just ran `search_src(\"isinstance(x, RingElement)\")`)\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/803\n\n",
    "created_at": "2007-10-03T08:13:00Z",
    "labels": [
        "component: basic arithmetic",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Tests for what kind of an element something is should test the parent",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/803",
    "user": "https://github.com/roed314"
}
```
Assignee: somebody

Calls like:

```
algebras/algebra_order.py:        elif isinstance(x, RingElement) and x in self.base_ring():
algebras/algebra_order_ideal.py:        elif isinstance(x, RingElement) and x in self.base_ring():
algebras/free_algebra_quotient_element.py:        elif isinstance(x, RingElement) and not isinstance(x, AlgebraElement) and x in R:
rings/infinity.py:        elif isinstance(x, RingElement) or isinstance(x, (int,long,float,complex)):
rings/infinity.py:        elif isinstance(x, RingElement):
```


should actually be checking to see if the parents are of the appropriate type.  The element types are not always reliable: parents more accurately reflect the mathematical structure (mostly because they can have multiple inheritance).

There may be more instances in addition to those above (I just ran `search_src("isinstance(x, RingElement)")`)



Issue created by migration from https://trac.sagemath.org/ticket/803





---

archive/issue_comments_004823.json:
```json
{
    "body": "I'm dubious:\n\n>\n\nMy immediate thought when looking at #803 is that it is the wrong\nidea in the first place.  If I had looked at #803 before\nnow I would have considered marking it \"invalid\".\n\nThere are individual instances that involve \"isinstance\" that were\nperhaps badly written.  E.g., the first example:\n\n```\n        elif isinstance(x, RingElement) and x in self.base_ring():\n            return True\n```\n\nHere I think the original author (David Kohel) may have written\nthis at a time when \"in\" could raise an exception if x isn't\na RingElement.  That's no longer the case, so in this particular\nexample the right fix is I think to put:\n\n```\n        elif x in self.base_ring():\n            return True\n```\n\nIn probably hundreds of other cases the use of isinstance in\nSage is exactly right.  In some cases it could be improved,\nbut how will depend in each case on understanding the code.",
    "created_at": "2008-02-25T05:37:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/803#issuecomment-4823",
    "user": "https://github.com/williamstein"
}
```

I'm dubious:

>

My immediate thought when looking at #803 is that it is the wrong
idea in the first place.  If I had looked at #803 before
now I would have considered marking it "invalid".

There are individual instances that involve "isinstance" that were
perhaps badly written.  E.g., the first example:

```
        elif isinstance(x, RingElement) and x in self.base_ring():
            return True
```

Here I think the original author (David Kohel) may have written
this at a time when "in" could raise an exception if x isn't
a RingElement.  That's no longer the case, so in this particular
example the right fix is I think to put:

```
        elif x in self.base_ring():
            return True
```

In probably hundreds of other cases the use of isinstance in
Sage is exactly right.  In some cases it could be improved,
but how will depend in each case on understanding the code.



---

archive/issue_comments_004824.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-13T14:54:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/803#issuecomment-4824",
    "user": "https://github.com/mezzarobba"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_004825.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-14T09:38:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/803#issuecomment-4825",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_004826.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2015-04-14T23:05:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/803",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/803#issuecomment-4826",
    "user": "https://github.com/vbraun"
}
```

Resolution: wontfix
