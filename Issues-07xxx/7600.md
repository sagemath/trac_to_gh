# Issue 7600: Vertex cover

archive/issues_007600.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  kevin.stueve\n\nAs the title says, this patch implements Graph.vertex_cover.\n\n\nYou could be in need of #7270 and GLPK from http://sagemath.org/packages/optional/glpk-4.38.p4.spkg depending on the version of Sage you are using !!!\n\nIssue created by migration from https://trac.sagemath.org/ticket/7600\n\n",
    "closed_at": "2009-12-19T19:59:11Z",
    "created_at": "2009-12-04T07:49:59Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Vertex cover",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7600",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

CC:  kevin.stueve

As the title says, this patch implements Graph.vertex_cover.


You could be in need of #7270 and GLPK from http://sagemath.org/packages/optional/glpk-4.38.p4.spkg depending on the version of Sage you are using !!!

Issue created by migration from https://trac.sagemath.org/ticket/7600





---

archive/issue_comments_064722.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T07:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64722",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064723.json:
```json
{
    "body": "I've never reviewed a patch before.\n\nWe were just talking about vertex cover in my algorithms class the other day.\n\nThe three problems:\n\n\n1) Does G have a clique of size m or more?\n\n\n2) Is there a vertex cover of size m or less for G?\n\n\n3) Does G contain an independent set of size m or more?\n\n\n\nare all polynomially reducible to each other.\n\nexercise 9, p 403, The Design and Analysis of Algorithms, 2nd Edition\n\nI'm not aware if those other problems are implemented in Sage.  If not, maybe a ticket should be created.\n\n3048\t          As vertex cover is a `NP`-complete problem\n\nIMO, would be better with the word \"an\" in place of \"a\".\n\nKevin Stueve",
    "created_at": "2009-12-09T04:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64723",
    "user": "https://trac.sagemath.org/admin/accounts/users/kevin.stueve"
}
```

I've never reviewed a patch before.

We were just talking about vertex cover in my algorithms class the other day.

The three problems:


1) Does G have a clique of size m or more?


2) Is there a vertex cover of size m or less for G?


3) Does G contain an independent set of size m or more?



are all polynomially reducible to each other.

exercise 9, p 403, The Design and Analysis of Algorithms, 2nd Edition

I'm not aware if those other problems are implemented in Sage.  If not, maybe a ticket should be created.

3048	          As vertex cover is a `NP`-complete problem

IMO, would be better with the word "an" in place of "a".

Kevin Stueve



---

archive/issue_comments_064724.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-09T08:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64724",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064725.json:
```json
{
    "body": "Hello !!!!\n\nYou are right, these three are reducible to each other ! Actually, Sage already has an algorithm for 1) and 3) through Cliquer, which is way more efficient that LinearProgramming... I will immediately add several lines to the patch to let it use Cliquer by default, and use LP if the users wants it ( and this way we can control the respective values of the two algorithms ) :-)\n\nThank you very much for your remark, this should speed up the algorithm amazingly ! :-)\n\nNathann",
    "created_at": "2009-12-09T08:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64725",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!!

You are right, these three are reducible to each other ! Actually, Sage already has an algorithm for 1) and 3) through Cliquer, which is way more efficient that LinearProgramming... I will immediately add several lines to the patch to let it use Cliquer by default, and use LP if the users wants it ( and this way we can control the respective values of the two algorithms ) :-)

Thank you very much for your remark, this should speed up the algorithm amazingly ! :-)

Nathann



---

archive/issue_comments_064726.json:
```json
{
    "body": "Done ! Thank you very much for your help ! :-)\nBesides, as the algorithm Cliquer does not require GLPK or CBC, there is a way for everybody to compute a vertex cover now :-)\n\nNathann",
    "created_at": "2009-12-09T08:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64726",
    "user": "https://github.com/nathanncohen"
}
```

Done ! Thank you very much for your help ! :-)
Besides, as the algorithm Cliquer does not require GLPK or CBC, there is a way for everybody to compute a vertex cover now :-)

Nathann



---

archive/issue_comments_064727.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-09T08:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64727",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064728.json:
```json
{
    "body": "oops:\n\n```\nsage: vc2 = g.vertex_cover(algorithm=\"Cliquer\")\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n\n/Users/rlmill/.sage/temp/rlm_book.local/98560/_Users_rlmill__sage_init_sage_0.py in <module>()\n\n/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in vertex_cover(self, algorithm, value_only, log)\n   3325                 return self.order()-len(independent)\n   3326             else:\n-> 3327                 return set(g.vertices()).difference(set(independent))\n   3328 \n   3329         elif algorithm==\"MILP\":\n\nUnboundLocalError: local variable 'g' referenced before assignment\n```",
    "created_at": "2009-12-15T17:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64728",
    "user": "https://github.com/rlmill"
}
```

oops:

```
sage: vc2 = g.vertex_cover(algorithm="Cliquer")
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)

/Users/rlmill/.sage/temp/rlm_book.local/98560/_Users_rlmill__sage_init_sage_0.py in <module>()

/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in vertex_cover(self, algorithm, value_only, log)
   3325                 return self.order()-len(independent)
   3326             else:
-> 3327                 return set(g.vertices()).difference(set(independent))
   3328 
   3329         elif algorithm=="MILP":

UnboundLocalError: local variable 'g' referenced before assignment
```



---

archive/issue_comments_064729.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T17:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64729",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064730.json:
```json
{
    "body": "Attachment [trac_7600.patch](tarball://root/attachments/some-uuid/ticket7600/trac_7600.patch) by @nathanncohen created at 2009-12-16 01:27:06",
    "created_at": "2009-12-16T01:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64730",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7600.patch](tarball://root/attachments/some-uuid/ticket7600/trac_7600.patch) by @nathanncohen created at 2009-12-16 01:27:06



---

archive/issue_comments_064731.json:
```json
{
    "body": "fixed !",
    "created_at": "2009-12-16T01:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64731",
    "user": "https://github.com/nathanncohen"
}
```

fixed !



---

archive/issue_comments_064732.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T01:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64732",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064733.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T03:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64733",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064734.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T19:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64734",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_018057.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-19T19:59:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7600#event-18057"
}
```



---

archive/issue_events_018058.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-20T07:43:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "milestone": "sage-4.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7600#event-18058"
}
```
