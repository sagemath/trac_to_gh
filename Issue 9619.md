# Issue 9619: b-coloring of a graph

Issue created by migration from https://trac.sagemath.org/ticket/9619

Original creator: lsampaio

Original creation time: 2010-07-28 07:49:02

Assignee: jason, ncohen, rlm

CC:  ncohen

This patch adds the function b_coloring, which computes a b-coloring with the maximum number of colors. Here are some explanations from the function's help :

    Given a proper coloring of a graph G and a color class C such that none of its vertices have neighbors in all the other color classes, one can eliminate color class C by assigning distinct colors to each of its elements.
    
    One can repeat this procedure until a coloring is obtained where every color class contains one vertex with neighbors in all the other color classes. We call such a vertex a b-vertex. So, one can define a b-coloring as a proper coloring where each color class has a b-vertex, a vertex with neighbors in all the other colors.
    
    The worst-case behaviour of this procedure for eliminating color classes is the b-chromatic number of G (denoted \chi_b(G)): the maximum k such that G admits a b-coloring with k colors.

Leonardo


---

Comment by lsampaio created at 2010-07-28 08:32:32

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-07-28 09:17:37

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

Comment by ncohen created at 2010-07-28 09:17:37

Changing status from needs_review to needs_work.


---

Comment by lsampaio created at 2010-08-12 10:02:31

Changing status from needs_work to needs_review.


---

Comment by lsampaio created at 2010-08-12 10:02:31

Hi Nathann,
  I've the corrections you proposed, thank you. 
  Concerning the constraint

`p.add_constraint(Sum(color[v][i] - is_used[i] for v in g.vertices()), max = 0) `

  it is necessary because we only require that if is_used[i] then there is a b-vertex with color i. But it could happen that a vertex v is such that c[v][j] = 1, is_used[j] = 0 and j such that there are no b-vertices in it.

  About the examples, I believe they are ok for the b-coloring, even if they're not interesting for the Grundy number. The point is that the P_5 is a simples example where b(G) = m(G), and the Petersen graph is relatively hard to calculate by hand, and it is an interesting example where b(G) < m(G) (usually the other examples have many vertices with same neighborhood to force b(G) < m(G)).


---

Comment by ncohen created at 2010-08-13 06:08:22

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-08-13 06:08:22

>   it is necessary because we only require that if is_used[i] then there is a b-vertex with color i. But it could happen that a vertex v is such that c[v][j] = 1, is_used[j] = 0 and j such that there are no b-vertices in it.

The list just above ensures that if `is_used[i]` is set to 1, then there is at least one vertex colored with `i`. Beside, it is already an equivalence as you are maximizing the sum of the is_used. If any of them can be set to 1, it will, even without this constraint !

>   About the examples, I believe they are ok for the b-coloring, even if they're not interesting for the Grundy number. The point is that the P_5 is a simples example where b(G) = m(G), and the Petersen graph is relatively hard to calculate by hand, and it is an interesting example where b(G) < m(G) (usually the other examples have many vertices with same neighborhood to force b(G) < m(G)).

Ok !

I also noticed something wrong in the doc, sorry for mentionning it this late : check out how the definition f `m(G)` is displayed... Probably just a typo in the LaTeX string.

Short of these, everything is perfect ! The next version is the final one `:-)` 

Nathann


---

Comment by lsampaio created at 2010-09-27 13:04:40

Changing status from needs_work to needs_review.


---

Comment by lsampaio created at 2010-09-27 13:04:40

Here is the (I suppose final) version of the patch. I made the changes in the constraints as sugested by Nathann and also corrected some mistakes in the documentation.


---

Comment by ncohen created at 2010-09-27 14:09:23

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-09-27 14:09:23

I didn't think I would live to see it `:-D`

Thanksssssssssssssssssssssssssss !!!!

Nathann


---

Comment by mpatel created at 2010-09-28 11:16:14

Could someone update the commit string of the patch so its first line is a < 80 (or so) character summary of the changes that includes the ticket number, then restore the positive review?  Additional lines are no problem, of course.


---

Comment by mpatel created at 2010-09-28 11:16:14

Changing status from positive_review to needs_work.


---

Comment by lsampaio created at 2010-09-28 13:45:37

ticket 9619: function for the b-chromatic number of a graph (with corrections)


---

Attachment

Updated !


---

Comment by lsampaio created at 2010-09-28 13:46:01

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-09-29 08:39:38

Resolution: fixed
