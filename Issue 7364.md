# Issue 7364: Implement eulerian orientation of a graph

archive/issues_007364.json:
```json
{
    "body": "Assignee: @rlmill\n\nImplement a method in Graph returning a DiGraph which corresponds to an eulerian orientation of the graph.\n\nAn eulerian orientation of an eulerian graph is an orientation such that d^+ = d^- = d/2 for any vertex.\n\nIf the graph is not eulerian, this method should return a DiGraph such that d^+ + d^- = d and | d^+ - d^- | <= 1\n\nNathann\n\nIssue created by migration from https://trac.sagemath.org/ticket/7364\n\n",
    "created_at": "2009-10-31T20:48:07Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Implement eulerian orientation of a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7364",
    "user": "https://github.com/nathanncohen"
}
```
Assignee: @rlmill

Implement a method in Graph returning a DiGraph which corresponds to an eulerian orientation of the graph.

An eulerian orientation of an eulerian graph is an orientation such that d^+ = d^- = d/2 for any vertex.

If the graph is not eulerian, this method should return a DiGraph such that d^+ + d^- = d and | d^+ - d^- | <= 1

Nathann

Issue created by migration from https://trac.sagemath.org/ticket/7364





---

archive/issue_comments_061592.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T10:57:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61592",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061593.json:
```json
{
    "body": "Hi Nathann\n\nPatch looks good. All tests passed! I'm ready to put a Positive review.\n\nHowever, I'm not a graph expert so I've no idea how clever is the algorithm.\nSo maybe it should be reviewed by a graph expert. Speaking about clever algorithm, if the complexity is known and in particular if it's known to be optimal or not, it could be a good idea to put a \"..note:\" in the doc giving this information. Of course the preceding remarks apply to any graph algorithm (and even to any algorithm). So maybe you want to put a positive review anyway.\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-22T18:40:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61593",
    "user": "https://github.com/hivert"
}
```

Hi Nathann

Patch looks good. All tests passed! I'm ready to put a Positive review.

However, I'm not a graph expert so I've no idea how clever is the algorithm.
So maybe it should be reviewed by a graph expert. Speaking about clever algorithm, if the complexity is known and in particular if it's known to be optimal or not, it could be a good idea to put a "..note:" in the doc giving this information. Of course the preceding remarks apply to any graph algorithm (and even to any algorithm). So maybe you want to put a positive review anyway.

Cheers,

Florent



---

archive/issue_comments_061594.json:
```json
{
    "body": "From the \"complexity\" point of view, this algorithm is linear in the number of edges in the graph, so I think it could be filed as \"optimal\".\n\nFrom the \"practical\" point of view, I do not think it would be easy to improve, though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...\n\nI am sending a mail to sage-devel about your great idea of a general \"Complexity\" note in algorithms.\n\nNathann",
    "created_at": "2009-11-22T19:08:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61594",
    "user": "https://github.com/nathanncohen"
}
```

From the "complexity" point of view, this algorithm is linear in the number of edges in the graph, so I think it could be filed as "optimal".

From the "practical" point of view, I do not think it would be easy to improve, though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...

I am sending a mail to sage-devel about your great idea of a general "Complexity" note in algorithms.

Nathann



---

archive/issue_comments_061595.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> ... though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...\n\nYou should use Sage's c_graphs directly: this will eliminate Python noise without forcing you to use pure C. Check out `sage/graphs/graph_fast.pyx` for an example...",
    "created_at": "2009-11-22T19:55:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61595",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:7 ncohen]:
> ... though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...

You should use Sage's c_graphs directly: this will eliminate Python noise without forcing you to use pure C. Check out `sage/graphs/graph_fast.pyx` for an example...



---

archive/issue_comments_061596.json:
```json
{
    "body": "Sorry, I should have pointed you to `sage/graphs/trees.pyx` for a good example. It all starts with either\n`from sage.graphs.base.sparse_graph cimport SparseGraph`\nor\n`from sage.graphs.base.dense_graph cimport DenseGraph`",
    "created_at": "2009-11-22T20:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61596",
    "user": "https://github.com/rlmill"
}
```

Sorry, I should have pointed you to `sage/graphs/trees.pyx` for a good example. It all starts with either
`from sage.graphs.base.sparse_graph cimport SparseGraph`
or
`from sage.graphs.base.dense_graph cimport DenseGraph`



---

archive/issue_comments_061597.json:
```json
{
    "body": "Replying to [comment:7 ncohen]:\n> From the \"complexity\" point of view, this algorithm is linear in the number of edges in the graph, so I think it could be filed as \"optimal\".\n> \n> From the \"practical\" point of view, I do not think it would be easy to improve, though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...\n\nIf the complexity is optimal, going from python to C will only improve the speed by a constant factor. Be sure it's really worth it before spending to much time. I'm a little extreme on this, but is it worth spending hours of researchears time, where we can spend money for a faster computer ? ;-)\n\nNote: this does *not* mean I'm not trying to improve the speed of my code ! It only means that a good algorithm is an slow language is much better than a bad algorithm in a fast language. When needed the first is much easier to improve. I'm generally reluctant towards premature optimization.  \n\nCheers,\n\nFlorent",
    "created_at": "2009-11-23T00:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61597",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:7 ncohen]:
> From the "complexity" point of view, this algorithm is linear in the number of edges in the graph, so I think it could be filed as "optimal".
> 
> From the "practical" point of view, I do not think it would be easy to improve, though I am more and more thinking about trying to write such methods in C rather than in Python... Most of the time in these algorithms is spent on Python considerations rather than on actual Graph computations...

If the complexity is optimal, going from python to C will only improve the speed by a constant factor. Be sure it's really worth it before spending to much time. I'm a little extreme on this, but is it worth spending hours of researchears time, where we can spend money for a faster computer ? ;-)

Note: this does *not* mean I'm not trying to improve the speed of my code ! It only means that a good algorithm is an slow language is much better than a bad algorithm in a fast language. When needed the first is much easier to improve. I'm generally reluctant towards premature optimization.  

Cheers,

Florent



---

archive/issue_comments_061598.json:
```json
{
    "body": "To Robert : Thank you very much !!!! I'll definitely give it a look ! But you make it sound like I would then have to work on a new graph rather than use the Python one ! In this case, I do not really need to create a new graph but I would like the functions \"get an edge coming out of this vertex\" and \"tell me where it goes\" to be extremely fast... When will the default Sage Graph the be C ones ?\n\nTo Florent : I'm aware this only means changing a \"factor\", but I am living among computer scientists who find it extremely hard to stop thinking like \"it is NP-complete : there is no algooorithm to solve it\". And I swear I did not forget the word \"polynomial\". At some point I also wanted to write an algorithm ion Sage to compute the crossign number of a graph. Bruce Reed published a Linear Time algorithm for this problem, using Graph Minor theory. The result is a (2<sup>2</sup>2<sup>2</sup>2<sup>2</sup>2^2.... ) * n algorithm which no one can implement, even less use. That's why I prefer mentionning the \"two\". Besides, one of the reasons people in my lab keep from really switching to Sage is that they currently use Java, which is way faster. ( of course they have less algorithms, of course they miss many things, but Still, it is faster )\n\nI'll update this patch today !\n\nNathann",
    "created_at": "2009-11-23T06:57:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61598",
    "user": "https://github.com/nathanncohen"
}
```

To Robert : Thank you very much !!!! I'll definitely give it a look ! But you make it sound like I would then have to work on a new graph rather than use the Python one ! In this case, I do not really need to create a new graph but I would like the functions "get an edge coming out of this vertex" and "tell me where it goes" to be extremely fast... When will the default Sage Graph the be C ones ?

To Florent : I'm aware this only means changing a "factor", but I am living among computer scientists who find it extremely hard to stop thinking like "it is NP-complete : there is no algooorithm to solve it". And I swear I did not forget the word "polynomial". At some point I also wanted to write an algorithm ion Sage to compute the crossign number of a graph. Bruce Reed published a Linear Time algorithm for this problem, using Graph Minor theory. The result is a (2<sup>2</sup>2<sup>2</sup>2<sup>2</sup>2^2.... ) * n algorithm which no one can implement, even less use. That's why I prefer mentionning the "two". Besides, one of the reasons people in my lab keep from really switching to Sage is that they currently use Java, which is way faster. ( of course they have less algorithms, of course they miss many things, but Still, it is faster )

I'll update this patch today !

Nathann



---

archive/issue_comments_061599.json:
```json
{
    "body": "I actually wrote 2<sup>{2</sup>{2<sup>{2</sup>{2^{...}}}}*n.",
    "created_at": "2009-11-23T07:00:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61599",
    "user": "https://github.com/nathanncohen"
}
```

I actually wrote 2<sup>{2</sup>{2<sup>{2</sup>{2^{...}}}}*n.



---

archive/issue_comments_061600.json:
```json
{
    "body": "My god. I wrote what is called a \"tower of exponentials\". :-p",
    "created_at": "2009-11-23T07:01:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61600",
    "user": "https://github.com/nathanncohen"
}
```

My god. I wrote what is called a "tower of exponentials". :-p



---

archive/issue_comments_061601.json:
```json
{
    "body": "This patch should suit you :-)\n\nNathann",
    "created_at": "2009-11-23T12:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61601",
    "user": "https://github.com/nathanncohen"
}
```

This patch should suit you :-)

Nathann



---

archive/issue_comments_061602.json:
```json
{
    "body": "Replying to [comment:14 ncohen]:\n> This patch should suit you :-)\n\nI'm really sorry to bother you again:\n\n> This algorithm has complexity `O(m)`.\n\nIs this a standard in graph theory to call 'm' the number of ??? Actually what ? Edge, Vertex or sum of Both... Maybe this is obvious but better explicit than implicit ;-)\n\nI promiss I'll give you a positive review after that !",
    "created_at": "2009-11-23T15:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61602",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:14 ncohen]:
> This patch should suit you :-)

I'm really sorry to bother you again:

> This algorithm has complexity `O(m)`.

Is this a standard in graph theory to call 'm' the number of ??? Actually what ? Edge, Vertex or sum of Both... Maybe this is obvious but better explicit than implicit ;-)

I promiss I'll give you a positive review after that !



---

archive/issue_comments_061603.json:
```json
{
    "body": "Done ! :-)",
    "created_at": "2009-11-23T15:35:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61603",
    "user": "https://github.com/nathanncohen"
}
```

Done ! :-)



---

archive/issue_comments_061604.json:
```json
{
    "body": "Attachment [trac_7364.patch](tarball://root/attachments/some-uuid/ticket7364/trac_7364.patch) by @nathanncohen created at 2009-11-23 15:35:38",
    "created_at": "2009-11-23T15:35:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61604",
    "user": "https://github.com/nathanncohen"
}
```

Attachment [trac_7364.patch](tarball://root/attachments/some-uuid/ticket7364/trac_7364.patch) by @nathanncohen created at 2009-11-23 15:35:38



---

archive/issue_comments_061605.json:
```json
{
    "body": "Ok ! Ready to go !",
    "created_at": "2009-11-23T16:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61605",
    "user": "https://github.com/hivert"
}
```

Ok ! Ready to go !



---

archive/issue_comments_061606.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-23T16:33:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61606",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061607.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-29T05:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7364",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7364#issuecomment-61607",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
