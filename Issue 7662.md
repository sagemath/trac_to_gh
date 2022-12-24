# Issue 7662: Chordal Graphs

archive/issues_007662.json:
```json
{
    "body": "Assignee: rlm\n\nCreate a module for chordal graphs :\n\n* Perfect elimination order ( use 7541 )\n* Move is-chordal in this module\n* Polynomial-time algorithms for\n     * Vertex coloring\n     * Max clique/stable\n* MaxBFS\n* BFS*\n\nIssue created by migration from https://trac.sagemath.org/ticket/7662\n\n",
    "created_at": "2009-12-11T14:27:34Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Chordal Graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7662",
    "user": "ncohen"
}
```
Assignee: rlm

Create a module for chordal graphs :

* Perfect elimination order ( use 7541 )
* Move is-chordal in this module
* Polynomial-time algorithms for
     * Vertex coloring
     * Max clique/stable
* MaxBFS
* BFS*

Issue created by migration from https://trac.sagemath.org/ticket/7662





---

archive/issue_comments_065604.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-06-06T11:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65604",
    "user": "ncohen"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_065605.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-02T12:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65605",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065606.json:
```json
{
    "body": "You should define what a \"perfect elimination order\" and a \"hole\" are in the documentation.\n\n\n```\nsage -t -long ./sage/graphs/generic_graph.py\n**********************************************************************\nFile \"/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py\", line 8758:\n    sage: (_, peo) = g.is_chordal(certificate = True)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/rlmill/sage-4.6/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/rlmill/sage-4.6/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/rlmill/sage-4.6/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_135[7]>\", line 1, in <module>\n        (_, peo) = g.is_chordal(certificate = True)###line 8758:\n    sage: (_, peo) = g.is_chordal(certificate = True)\n      File \"/home/rlmill/sage-4.6/local/lib/python/site-packages/sage/graphs/generic_graph.py\", line 8854, in is_chordal\n        return True, peo_copy\n    NameError: global name 'peo_copy' is not defined\n**********************************************************************\nFile \"/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py\", line 8759:\n    sage: for v in peo:\n          if not g.subgraph(g.neighbors(v)).is_clique():\n               print \"This should never happen !\"\n          g.delete_vertex(v)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/rlmill/sage-4.6/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/rlmill/sage-4.6/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/rlmill/sage-4.6/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_135[8]>\", line 1, in <module>\n        for v in peo:###line 8759:\n    sage: for v in peo:\n    NameError: name 'peo' is not defined\n**********************************************************************\n```\n",
    "created_at": "2010-11-10T12:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65606",
    "user": "rlm"
}
```

You should define what a "perfect elimination order" and a "hole" are in the documentation.


```
sage -t -long ./sage/graphs/generic_graph.py
**********************************************************************
File "/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py", line 8758:
    sage: (_, peo) = g.is_chordal(certificate = True)
Exception raised:
    Traceback (most recent call last):
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_135[7]>", line 1, in <module>
        (_, peo) = g.is_chordal(certificate = True)###line 8758:
    sage: (_, peo) = g.is_chordal(certificate = True)
      File "/home/rlmill/sage-4.6/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 8854, in is_chordal
        return True, peo_copy
    NameError: global name 'peo_copy' is not defined
**********************************************************************
File "/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py", line 8759:
    sage: for v in peo:
          if not g.subgraph(g.neighbors(v)).is_clique():
               print "This should never happen !"
          g.delete_vertex(v)
Exception raised:
    Traceback (most recent call last):
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_135[8]>", line 1, in <module>
        for v in peo:###line 8759:
    sage: for v in peo:
    NameError: name 'peo' is not defined
**********************************************************************
```




---

archive/issue_comments_065607.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-10T12:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65607",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_065608.json:
```json
{
    "body": "Hello ! I added a short definition of what a hole is (a cycle of length at least 4), and replaced peo_copy by peo (sorry for that `O_o`).\n\nWhat about my `Such an ordering is called a Perfect Elimination Order` ? Would you like something more formal instead ?\n\nNathann",
    "created_at": "2010-11-15T14:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65608",
    "user": "ncohen"
}
```

Hello ! I added a short definition of what a hole is (a cycle of length at least 4), and replaced peo_copy by peo (sorry for that `O_o`).

What about my `Such an ordering is called a Perfect Elimination Order` ? Would you like something more formal instead ?

Nathann



---

archive/issue_comments_065609.json:
```json
{
    "body": "Changing status from needs_work to needs_info.",
    "created_at": "2010-11-15T14:55:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65609",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_info.



---

archive/issue_comments_065610.json:
```json
{
    "body": "Replying to [comment:5 ncohen]:\n> What about my `Such an ordering is called a Perfect Elimination Order` ? Would you like something more formal instead ?\n\nI'm not sure whether this is enough. Imagine a user who knows what the definition of chordal is, but not much else. You still want the documentation for this function to make sense to that user. Granted, it is not Sage's job to educate people about all of mathematics, but it certainly should be able to make clear what the input and output of each function is. Perhaps in this case it could do a better job of informing the user of what it is returning.\n\nAs long as you say what an elimination order is, then I think that's enough, but right now it is an undefined term.",
    "created_at": "2010-11-26T10:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65610",
    "user": "rlm"
}
```

Replying to [comment:5 ncohen]:
> What about my `Such an ordering is called a Perfect Elimination Order` ? Would you like something more formal instead ?

I'm not sure whether this is enough. Imagine a user who knows what the definition of chordal is, but not much else. You still want the documentation for this function to make sense to that user. Granted, it is not Sage's job to educate people about all of mathematics, but it certainly should be able to make clear what the input and output of each function is. Perhaps in this case it could do a better job of informing the user of what it is returning.

As long as you say what an elimination order is, then I think that's enough, but right now it is an undefined term.



---

archive/issue_comments_065611.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-11-26T10:37:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65611",
    "user": "rlm"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_065612.json:
```json
{
    "body": "Attachment [trac_7662.patch](tarball://root/attachments/some-uuid/ticket7662/trac_7662.patch) by ncohen created at 2010-11-26 11:19:46\n\nWhat about this one, then ?\n\nIt was a good idea to explain it... I quite liked writing it `:-)`\n\nNathann",
    "created_at": "2010-11-26T11:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65612",
    "user": "ncohen"
}
```

Attachment [trac_7662.patch](tarball://root/attachments/some-uuid/ticket7662/trac_7662.patch) by ncohen created at 2010-11-26 11:19:46

What about this one, then ?

It was a good idea to explain it... I quite liked writing it `:-)`

Nathann



---

archive/issue_comments_065613.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-26T11:19:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65613",
    "user": "ncohen"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_065614.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-26T16:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65614",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065615.json:
```json
{
    "body": "Much better! :)",
    "created_at": "2010-11-26T16:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65615",
    "user": "rlm"
}
```

Much better! :)



---

archive/issue_comments_065616.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-12T06:31:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7662",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7662#issuecomment-65616",
    "user": "jdemeyer"
}
```

Resolution: fixed
