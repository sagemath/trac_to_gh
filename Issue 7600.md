# Issue 7600: Vertex cover

archive/issues_007600.json:
```json
{
    "body": "Assignee: rlm\n\nCC:  kevin.stueve\n\nAs the title says, this patch implements Graph.vertex_cover.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7600\n\n",
    "created_at": "2009-12-04T07:49:59Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "Vertex cover",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7600",
    "user": "ncohen"
}
```
Assignee: rlm

CC:  kevin.stueve

As the title says, this patch implements Graph.vertex_cover.

Issue created by migration from https://trac.sagemath.org/ticket/7600





---

archive/issue_comments_064838.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-04T07:51:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64838",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_064839.json:
```json
{
    "body": "I've never reviewed a patch before.\n\nWe were just talking about vertex cover in my algorithms class the other day.\n\nThe three problems:\n\n\n1) Does G have a clique of size m or more?\n\n\n2) Is there a vertex cover of size m or less for G?\n\n\n3) Does G contain an independent set of size m or more?\n\n\n\nare all polynomially reducible to each other.\n\nexercise 9, p 403, The Design and Analysis of Algorithms, 2nd Edition\n\nI'm not aware if those other problems are implemented in Sage.  If not, maybe a ticket should be created.\n\n3048\t          As vertex cover is a `NP`-complete problem\n\nIMO, would be better with the word \"an\" in place of \"a\".\n\nKevin Stueve",
    "created_at": "2009-12-09T04:48:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64839",
    "user": "kevin.stueve"
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

archive/issue_comments_064840.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-09T08:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64840",
    "user": "ncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064841.json:
```json
{
    "body": "Hello !!!!\n\nYou are right, these three are reducible to each other ! Actually, Sage already has an algorithm for 1) and 3) through Cliquer, which is way more efficient that LinearProgramming... I will immediately add several lines to the patch to let it use Cliquer by default, and use LP if the users wants it ( and this way we can control the respective values of the two algorithms ) :-)\n\nThank you very much for your remark, this should speed up the algorithm amazingly ! :-)\n\nNathann",
    "created_at": "2009-12-09T08:11:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64841",
    "user": "ncohen"
}
```

Hello !!!!

You are right, these three are reducible to each other ! Actually, Sage already has an algorithm for 1) and 3) through Cliquer, which is way more efficient that LinearProgramming... I will immediately add several lines to the patch to let it use Cliquer by default, and use LP if the users wants it ( and this way we can control the respective values of the two algorithms ) :-)

Thank you very much for your remark, this should speed up the algorithm amazingly ! :-)

Nathann



---

archive/issue_comments_064842.json:
```json
{
    "body": "Done ! Thank you very much for your help ! :-)\nBesides, as the algorithm Cliquer does not require GLPK or CBC, there is a way for everybody to compute a vertex cover now :-)\n\nNathann",
    "created_at": "2009-12-09T08:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64842",
    "user": "ncohen"
}
```

Done ! Thank you very much for your help ! :-)
Besides, as the algorithm Cliquer does not require GLPK or CBC, there is a way for everybody to compute a vertex cover now :-)

Nathann



---

archive/issue_comments_064843.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-09T08:33:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64843",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064844.json:
```json
{
    "body": "oops:\n\n```\nsage: vc2 = g.vertex_cover(algorithm=\"Cliquer\")\n---------------------------------------------------------------------------\nUnboundLocalError                         Traceback (most recent call last)\n\n/Users/rlmill/.sage/temp/rlm_book.local/98560/_Users_rlmill__sage_init_sage_0.py in <module>()\n\n/Users/rlmill/sage-4.3.rc0/local/lib/python2.6/site-packages/sage/graphs/graph.pyc in vertex_cover(self, algorithm, value_only, log)\n   3325                 return self.order()-len(independent)\n   3326             else:\n-> 3327                 return set(g.vertices()).difference(set(independent))\n   3328 \n   3329         elif algorithm==\"MILP\":\n\nUnboundLocalError: local variable 'g' referenced before assignment\n```\n",
    "created_at": "2009-12-15T17:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64844",
    "user": "rlm"
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

archive/issue_comments_064845.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-15T17:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64845",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_064846.json:
```json
{
    "body": "Attachment [trac_7600.patch](tarball://root/attachments/some-uuid/ticket7600/trac_7600.patch) by ncohen created at 2009-12-16 01:27:06",
    "created_at": "2009-12-16T01:27:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64846",
    "user": "ncohen"
}
```

Attachment [trac_7600.patch](tarball://root/attachments/some-uuid/ticket7600/trac_7600.patch) by ncohen created at 2009-12-16 01:27:06



---

archive/issue_comments_064847.json:
```json
{
    "body": "fixed !",
    "created_at": "2009-12-16T01:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64847",
    "user": "ncohen"
}
```

fixed !



---

archive/issue_comments_064848.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-12-16T01:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64848",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_064849.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-16T03:26:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64849",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_064850.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-19T19:59:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7600#issuecomment-64850",
    "user": "mhansen"
}
```

Resolution: fixed
