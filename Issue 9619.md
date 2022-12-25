# Issue 9619: b-coloring of a graph

archive/issues_009619.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @nathanncohen\n\nThis patch adds the function b_coloring, which computes a b-coloring with the maximum number of colors. Here are some explanations from the function's help :\n\n    Given a proper coloring of a graph G and a color class C such that none of its vertices have neighbors in all the other color classes, one can eliminate color class C by assigning distinct colors to each of its elements.\n    \n    One can repeat this procedure until a coloring is obtained where every color class contains one vertex with neighbors in all the other color classes. We call such a vertex a b-vertex. So, one can define a b-coloring as a proper coloring where each color class has a b-vertex, a vertex with neighbors in all the other colors.\n    \n    The worst-case behaviour of this procedure for eliminating color classes is the b-chromatic number of G (denoted \\chi_b(G)): the maximum k such that G admits a b-coloring with k colors.\n\nLeonardo\n\nIssue created by migration from https://trac.sagemath.org/ticket/9619\n\n",
    "created_at": "2010-07-28T07:49:02Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6",
    "title": "b-coloring of a graph",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9619",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```
Assignee: jason, ncohen, rlm

CC:  @nathanncohen

This patch adds the function b_coloring, which computes a b-coloring with the maximum number of colors. Here are some explanations from the function's help :

    Given a proper coloring of a graph G and a color class C such that none of its vertices have neighbors in all the other color classes, one can eliminate color class C by assigning distinct colors to each of its elements.
    
    One can repeat this procedure until a coloring is obtained where every color class contains one vertex with neighbors in all the other color classes. We call such a vertex a b-vertex. So, one can define a b-coloring as a proper coloring where each color class has a b-vertex, a vertex with neighbors in all the other colors.
    
    The worst-case behaviour of this procedure for eliminating color classes is the b-chromatic number of G (denoted \chi_b(G)): the maximum k such that G admits a b-coloring with k colors.

Leonardo

Issue created by migration from https://trac.sagemath.org/ticket/9619





---

archive/issue_comments_093013.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-28T08:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93013",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093014.json:
```json
{
    "body": "Hello !!!\n\nIt's nice to be reviewing your first patch !\n\nWell, a few comments about the documentation :\n\nUnless you define what is a \"maximum\" b-coloring, the first line of the doc does not make sense (I understaned what you mean, but it has to be rephrased to be correct). Then it is 'a', not 'the', as there may be many. Then this b-cloring may not exist if k is less than Chi, so maybe you should even add \"if possible\".\n\nby assigning distinct colors to each of its elements => assigning the mising color in its neighborhood\n\nThe second paragraph is not clear, perhaps you should first defie what a b-vertex is, then rephrase the whole section.\n\nDefine what you mean by \"worst case\" -> I know what it means, but then again I know what b-coloring is.\n\nNOTE : Instead of copying what I wrote for he Grundy method, perhaps you should mention your degree-based bound, to say that it can be assumed to be optimal if it reaches this bound (which is less than the max degree of course). \n\nWhat the hell is this ?\n\n\n```\np.add_constraint(Sum(color[v][i] - is_used[i] for v in g.vertices()), max = 0) \n```\n\n\nIn the following \n\n```\np.set_objective(Sum(is_used[i] for i in xrange(k))) \n```\n\n\nclasses = xrange(k)\n\nAnd I think that's all there is ! By the way, if you know of a good b-coloring-specific example to add in the Examples section... I didn't have any inspiration for the Grundy number ;-)\n\nNathann",
    "created_at": "2010-07-28T09:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93014",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!!

It's nice to be reviewing your first patch !

Well, a few comments about the documentation :

Unless you define what is a "maximum" b-coloring, the first line of the doc does not make sense (I understaned what you mean, but it has to be rephrased to be correct). Then it is 'a', not 'the', as there may be many. Then this b-cloring may not exist if k is less than Chi, so maybe you should even add "if possible".

by assigning distinct colors to each of its elements => assigning the mising color in its neighborhood

The second paragraph is not clear, perhaps you should first defie what a b-vertex is, then rephrase the whole section.

Define what you mean by "worst case" -> I know what it means, but then again I know what b-coloring is.

NOTE : Instead of copying what I wrote for he Grundy method, perhaps you should mention your degree-based bound, to say that it can be assumed to be optimal if it reaches this bound (which is less than the max degree of course). 

What the hell is this ?


```
p.add_constraint(Sum(color[v][i] - is_used[i] for v in g.vertices()), max = 0) 
```


In the following 

```
p.set_objective(Sum(is_used[i] for i in xrange(k))) 
```


classes = xrange(k)

And I think that's all there is ! By the way, if you know of a good b-coloring-specific example to add in the Examples section... I didn't have any inspiration for the Grundy number ;-)

Nathann



---

archive/issue_comments_093015.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-28T09:17:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93015",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093016.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-08-12T10:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93016",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093017.json:
```json
{
    "body": "Hi Nathann,\n  I've the corrections you proposed, thank you. \n  Concerning the constraint\n\n`p.add_constraint(Sum(color[v][i] - is_used[i] for v in g.vertices()), max = 0) `\n\n  it is necessary because we only require that if is_used[i] then there is a b-vertex with color i. But it could happen that a vertex v is such that c[v][j] = 1, is_used[j] = 0 and j such that there are no b-vertices in it.\n\n  About the examples, I believe they are ok for the b-coloring, even if they're not interesting for the Grundy number. The point is that the P_5 is a simples example where b(G) = m(G), and the Petersen graph is relatively hard to calculate by hand, and it is an interesting example where b(G) < m(G) (usually the other examples have many vertices with same neighborhood to force b(G) < m(G)).",
    "created_at": "2010-08-12T10:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93017",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Hi Nathann,
  I've the corrections you proposed, thank you. 
  Concerning the constraint

`p.add_constraint(Sum(color[v][i] - is_used[i] for v in g.vertices()), max = 0) `

  it is necessary because we only require that if is_used[i] then there is a b-vertex with color i. But it could happen that a vertex v is such that c[v][j] = 1, is_used[j] = 0 and j such that there are no b-vertices in it.

  About the examples, I believe they are ok for the b-coloring, even if they're not interesting for the Grundy number. The point is that the P_5 is a simples example where b(G) = m(G), and the Petersen graph is relatively hard to calculate by hand, and it is an interesting example where b(G) < m(G) (usually the other examples have many vertices with same neighborhood to force b(G) < m(G)).



---

archive/issue_comments_093018.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-13T06:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93018",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_093019.json:
```json
{
    "body": ">   it is necessary because we only require that if is_used[i] then there is a b-vertex with color i. But it could happen that a vertex v is such that c[v][j] = 1, is_used[j] = 0 and j such that there are no b-vertices in it.\n\nThe list just above ensures that if `is_used[i]` is set to 1, then there is at least one vertex colored with `i`. Beside, it is already an equivalence as you are maximizing the sum of the is_used. If any of them can be set to 1, it will, even without this constraint !\n\n>   About the examples, I believe they are ok for the b-coloring, even if they're not interesting for the Grundy number. The point is that the P_5 is a simples example where b(G) = m(G), and the Petersen graph is relatively hard to calculate by hand, and it is an interesting example where b(G) < m(G) (usually the other examples have many vertices with same neighborhood to force b(G) < m(G)).\n\nOk !\n\nI also noticed something wrong in the doc, sorry for mentionning it this late : check out how the definition f `m(G)` is displayed... Probably just a typo in the LaTeX string.\n\nShort of these, everything is perfect ! The next version is the final one `:-)` \n\nNathann",
    "created_at": "2010-08-13T06:08:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93019",
    "user": "https://github.com/nathanncohen"
}
```

>   it is necessary because we only require that if is_used[i] then there is a b-vertex with color i. But it could happen that a vertex v is such that c[v][j] = 1, is_used[j] = 0 and j such that there are no b-vertices in it.

The list just above ensures that if `is_used[i]` is set to 1, then there is at least one vertex colored with `i`. Beside, it is already an equivalence as you are maximizing the sum of the is_used. If any of them can be set to 1, it will, even without this constraint !

>   About the examples, I believe they are ok for the b-coloring, even if they're not interesting for the Grundy number. The point is that the P_5 is a simples example where b(G) = m(G), and the Petersen graph is relatively hard to calculate by hand, and it is an interesting example where b(G) < m(G) (usually the other examples have many vertices with same neighborhood to force b(G) < m(G)).

Ok !

I also noticed something wrong in the doc, sorry for mentionning it this late : check out how the definition f `m(G)` is displayed... Probably just a typo in the LaTeX string.

Short of these, everything is perfect ! The next version is the final one `:-)` 

Nathann



---

archive/issue_comments_093020.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-27T13:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93020",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_093021.json:
```json
{
    "body": "Here is the (I suppose final) version of the patch. I made the changes in the constraints as sugested by Nathann and also corrected some mistakes in the documentation.",
    "created_at": "2010-09-27T13:04:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93021",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Here is the (I suppose final) version of the patch. I made the changes in the constraints as sugested by Nathann and also corrected some mistakes in the documentation.



---

archive/issue_comments_093022.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-27T14:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93022",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093023.json:
```json
{
    "body": "I didn't think I would live to see it `:-D`\n\nThanksssssssssssssssssssssssssss !!!!\n\nNathann",
    "created_at": "2010-09-27T14:09:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93023",
    "user": "https://github.com/nathanncohen"
}
```

I didn't think I would live to see it `:-D`

Thanksssssssssssssssssssssssssss !!!!

Nathann



---

archive/issue_comments_093024.json:
```json
{
    "body": "Could someone update the commit string of the patch so its first line is a < 80 (or so) character summary of the changes that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.",
    "created_at": "2010-09-28T11:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93024",
    "user": "https://github.com/qed777"
}
```

Could someone update the commit string of the patch so its first line is a < 80 (or so) character summary of the changes that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.



---

archive/issue_comments_093025.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-28T11:16:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93025",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_093026.json:
```json
{
    "body": "ticket 9619: function for the b-chromatic number of a graph (with corrections)",
    "created_at": "2010-09-28T13:45:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93026",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

ticket 9619: function for the b-chromatic number of a graph (with corrections)



---

archive/issue_comments_093027.json:
```json
{
    "body": "Attachment [trac_9619.patch](tarball://root/attachments/some-uuid/ticket9619/trac_9619.patch) by lsampaio created at 2010-09-28 13:46:01\n\nUpdated !",
    "created_at": "2010-09-28T13:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93027",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Attachment [trac_9619.patch](tarball://root/attachments/some-uuid/ticket9619/trac_9619.patch) by lsampaio created at 2010-09-28 13:46:01

Updated !



---

archive/issue_comments_093028.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2010-09-28T13:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93028",
    "user": "https://trac.sagemath.org/admin/accounts/users/lsampaio"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_093029.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-09-29T08:39:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9619",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9619#issuecomment-93029",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed
