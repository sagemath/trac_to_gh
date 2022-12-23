# Issue 7246: digraph.DeBruijn in graph_generators

archive/issues_007246.json:
```json
{
    "body": "Assignee: rlm\n\nThis patch adds the DeBruijn digraph to the ( still very short ) list of digraphs generators.\n\nMore information here : http://en.wikipedia.org/wiki/De_Bruijn_graph\n\nI found no way to define automatically a layout for this graph. If you have an idea, do not hesitate to tell me :-)\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7246\n\n",
    "created_at": "2009-10-19T07:00:16Z",
    "labels": [
        "graph theory",
        "major",
        "enhancement"
    ],
    "title": "digraph.DeBruijn in graph_generators",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7246",
    "user": "ncohen"
}
```
Assignee: rlm

This patch adds the DeBruijn digraph to the ( still very short ) list of digraphs generators.

More information here : http://en.wikipedia.org/wiki/De_Bruijn_graph

I found no way to define automatically a layout for this graph. If you have an idea, do not hesitate to tell me :-)

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7246





---

archive/issue_comments_060161.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-10-19T07:00:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7246#issuecomment-60161",
    "user": "ncohen"
}
```

Attachment



---

archive/issue_comments_060162.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-19T07:00:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7246#issuecomment-60162",
    "user": "ncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060163.json:
```json
{
    "body": "Dear Nathann, I just reviewed your code and made some modifications (see patch). I mostly used some possibilities offered by the word code in sage (e.g. * instead of concatenation and Words(n,1) for words of length one). Tell me if you agree with those modifications.\n\nThe output when k=0 was broken (vertices of length one were appearing). Although it could not be supported (return an error), I think it may be defined using multiedges and hence the \"Each vertex has exactly n incoming and n outgoing edges\" statement stays true. The wiki page doesn't talk about k=0...... \n\nI am giving a positive review to your patch pending a solution for the case k=0. Can you review my patch?",
    "created_at": "2009-10-19T11:29:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7246#issuecomment-60163",
    "user": "slabbe"
}
```

Dear Nathann, I just reviewed your code and made some modifications (see patch). I mostly used some possibilities offered by the word code in sage (e.g. * instead of concatenation and Words(n,1) for words of length one). Tell me if you agree with those modifications.

The output when k=0 was broken (vertices of length one were appearing). Although it could not be supported (return an error), I think it may be defined using multiedges and hence the "Each vertex has exactly n incoming and n outgoing edges" statement stays true. The wiki page doesn't talk about k=0...... 

I am giving a positive review to your patch pending a solution for the case k=0. Can you review my patch?



---

archive/issue_comments_060164.json:
```json
{
    "body": "Attachment\n\nI think your patch is perfect, including the case k=0... I did not think about empty words, though it can not hurt :-)\n\nPositive review !\n\nNathann",
    "created_at": "2009-10-19T16:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7246#issuecomment-60164",
    "user": "ncohen"
}
```

Attachment

I think your patch is perfect, including the case k=0... I did not think about empty words, though it can not hurt :-)

Positive review !

Nathann



---

archive/issue_comments_060165.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-10-19T16:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7246#issuecomment-60165",
    "user": "ncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060166.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-21T07:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7246",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7246#issuecomment-60166",
    "user": "mhansen"
}
```

Resolution: fixed
