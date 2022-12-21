# Issue 7184: [with patch, needs review] Implement counting of spanning trees for graphs and digraphs

Issue created by migration from Trac.

Original creator: AJonsson

Original creation time: 2009-10-10 17:59:38

Assignee: rlm

CC:  boothby

This patch allows us to count the number of spanning trees in a simple graph, as well as the spanning out-trees from a user-defined root node in a digraph.

Method used: Kirchhoff's matrix tree theorem [1] and the Laplacian matrix for the simple graphs, and a variation of the same [2] in the directed case.


[1] http://en.wikipedia.org/wiki/Kirchhoff%27s_theorem
[2] corollary 4.4 in http://books.google.se/books?id=vbxdqhDKOSYC&printsec=frontcover&hl=en&source=gbs_navlinks_s


---

Comment by AJonsson created at 2009-10-10 18:00:46

count spanning trees of graphs


---

Attachment


---

Comment by AJonsson created at 2009-10-10 18:05:43

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-10-18 12:16:29

Here is a new patch based on yours, plus some modifications :
    * I was not able at first to apply your patch, as it was based on an old version of Sage. This new version is now based on 4.1.2.rc0.
    * I fixed some docstrings :
          * you set "math" mode with this sign : ` 
            ( exemple : `x^2` )
          * you set "sage" mode with this sign : `` 
            ( exemple : ``graph.am()`` )
    * I renamed the function from spanning_trees to spanning_tree_count as the first seemed to imply an iterator over spanning_trees
    * Some details concerning the root_vertex too. Many graphs have vertices not among integers but among strings, or tuples, etc. Besides, it is not necessary to enumerate all the vertices to get the first one :
      {{{
      v=G.vertices()[0]
      }}}
      You can also do :
      {{{
      v=G.vertex_iterator().next()
      }}}
    * You had to modify the adjacency matrix to fit the definition used in your references. This was perfectly fine, but also meant there was an error in the definition of ``kirchhoff_matrix`` for directed graph. This patch fixes this, plus some docstrings error in the kirchhoff_matrix function.

Short of these details, you algorithm works fine, thank you for having sent this patch !!

If you agree with this nex patch I am sending, you can set this ticket to positive_review

Thanks !

Nathann

Algorithm is OK, both for Graphs and Digraphs. You had to re-define


---

Comment by ncohen created at 2009-10-18 12:18:29

Ooops, sorry for the last line, which was not meant to be included in my message. Besides, I meant that you had to redefine the kirchhoff matrix, not the adjacency matrix.. Sorry :-)


---

Comment by boothby created at 2009-10-18 17:10:02

Ncohen, you've broken kirchhoff_matrix.  According to the definition, row-sums of the Kirchhoff matrix should be zero.  Here's the doctest before you changed it:

```
sage: G = DiGraph({1:{1:2,2:3}, 2:{1:4}}, weighted=True,sparse=True) 
sage: G.laplacian_matrix() 
[ 3 -3] 
[-4  4] 
```

here, the row-sums are zero.

But you actually had to change the doctest to make the code pass,

```
sage: G = DiGraph({1:{1:2,2:3}, 2:{1:4}}, weighted=True,sparse=True) 
sage: G.laplacian_matrix() 
[ 4 -3] 
[-4  3] 
```

but the row-sums aren't zero!  Don't break math to make code work!


---

Comment by boothby created at 2009-10-18 17:10:12

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2009-10-18 17:42:25

Hello !!

Yes, I indeed changed the docstring because I thought this was a bug in kirchoff_matrix. As it is written in the patch I sent, the definition of kirchhoff matrix perfectly matches the definition from http://en.wikipedia.org/wiki/Laplacian_matrix
Two differences : the kirchhoff matrix can be defined when the graph is a DiGraph. 
    * In this case, as defined ( for example ) in the book AJonsson is mentionning, the diagonal values should be set to the indegree of each vertex ( and not their out-degree as it is currenty the case ). He has, in his own code, to change manually the values from the returned kirchhoff_matrix, which I felt was not right if the kirchhoff_matrix function was "correctly" defined ( "correctly" here means : according to this book ).
    * In this docstring, you test your code against a special graph, as it has loops. As you see, the definition from wikipedia does not include the case where the graph includes loops. The definition from the book AJonsson mentions in his docstring ( I have it as a pdf file and can send it to you if you like ) produces the output of the functions kirchoff_matrix when my patch is applied.

I honestly thought this was just a bug happening in special cases ( DiGraph + loops ), and checked several times the definition. Could you tell me which one you used ? 

Sorry for the trouble. In added you in Cc uniquely to avoid unnoticed changes like this. Oh, and btw, I ran sage -testall to be sure this modifications broke no part of Sage. 

Nathann


---

Comment by AJonsson created at 2009-10-19 19:48:00

Hello Nathann,
thanks for your review. I agree with your changes and have made an updated patch against sage 4.1.2. I did some more testing and noticed that the code for digraphs could easily be crashed by adding string-labeled vertices, so added a type check for that.


As for the Laplacian matrix, I left the current function alone since I saw the following on wikipedia: "In the case of directed graphs, either the indegree or the outdegree might be used [for the diagonal values], depending on the application." At the present only the out-degree is used in sage, but it would of course be possible to make it a user option at creation of the Laplacian matrix if in- or out-degrees are to be used.


---

Comment by AJonsson created at 2009-10-19 19:48:00

Changing status from needs_work to needs_review.


---

Comment by AJonsson created at 2009-10-19 19:49:27

built against sage 4.1.2, extra typecheck


---

Attachment

Considering the view Tom Boothby had of my little modification of kirchhoff_matrix, it may be better not to touch it for the moment in this patch. If as you say, the two different ways are used, the best option would be to modify kirchhoff_matrix as you say, to let the user choose its own definition. ( the problem with the loops still remains, though, but we do not really care about it in this special application ).

I am still worried about what you said considering Strings, though. If as you say, your code can be broken if vertices are strings, then you did not really solve your problem by taking this into account, as vertices can actually be of any immutable type. See for example patch #7246 where vertices are defined as Words ( which is a totally independent Sage object ). This does not fit in the integer case, nor in the String case.

If I make no mistake remembering what is written in the book you mentioned, they also talk of a different way to compute the number of out-trees : you do not add this special vertex, but just consider the kirchhoff matrix of the first graph, then add 1 to the vertex you want to take as root. It is ( I think ) an easier way to define your matrix in this case, without having to consider these types.. You just have to deal with the matrix ! ( I'm sorry I can not write this patch myself now, I do not have the correct tools on the computer I use and have some urgent work to get done until tomorrow... :-) )

Nathann


---

Comment by ncohen created at 2009-10-19 20:19:48

Changing status from needs_review to needs_work.


---

Comment by AJonsson created at 2009-10-20 17:02:54

Changing status from needs_work to needs_review.


---

Comment by AJonsson created at 2009-10-20 17:02:54

Hello Nathann, thanks for pointing me in the right way, I have made a new patch that just increases the diagonal value of the root vertex by 1, which indeed is a simpler solution. As a bonus there is no longer any need to copy the graph, since we no longer do any changes to the original graph in our computations.

Anders


---

Comment by boothby created at 2009-10-21 01:13:37

Nathann, I was wrong!  I've ONLY dealt with Kirchhoff matrices in the context of electrical networks, in which loops are utterly insignificant.  For me, the definition of the Kirchhoff matrix is that the diagonal is the row-sum of the weighted adjacency matrix.  But, the definition you are using appears to be standard, and as noted here, more useful.


---

Comment by ncohen created at 2009-10-21 10:07:16

This patch should satisfy all of us, I hope. It includes the last version of AJonsson's code, and it adds an argument to kirchhoff_matrix so that the user may chose if D is the matrix of indegree or outdegrees.

I added the corresponding documentation to the kirchhoff_matrix function.

I have to mention that the way kirchhoff_matrix is written contains a lot of repetitions because of the possibility of different values for the indegree variable. I thought of other ways to write it to preserve the code, but these ways could have at some point impaired the performances, as checks for the values of the variable indegree could have happened much more often. I write it this way as the function is still very short and this should not be a problem for its maintenance.

Oh, and the patch is based on 4.1.2.rc0

Nathann


---

Comment by AJonsson created at 2009-10-21 12:07:08

Looks fine to me. With your patch applied there is another line in count_spanning_trees that no longer is needed. Apply this patch on top of trac_7184-reviewer.patch to remove that line.


---

Comment by AJonsson created at 2009-10-21 12:08:38

remove unneeded reassignment of all diagonal entries of Kirchhoff matrix


---

Attachment

Sorryyyyyyy !! I had forgotten to edit your function after I edited kirchhoff_matrix !

Here is a new patch removing this line which is now integrated into kirchhoff_matrix. Besides, I wanted to do something about 

```
	            for i in self.vertices():  
	                        M[j,j]=self.in_degree(i)  
	                        if (self.vertices()[j]== root_vertex):  
	                            M[j,j]= M[j,j] + 1  
	                        j= j + 1  
```

With these lines, you are evaluating all the vertices at each look, just to return its jth element. As the vertices do not change, you could have stored the list of vertices in a variable, each time trying to find the jth element of this list ( without listing allt he vertices again ). But with this new patch, you are just getting the index of the vertex you are interested in, and updating the matrix... And with some luck, this patch is the last one :-)


---

Attachment

Looks really nice. I'm fully satisfied with the patch.

Anders


---

Comment by ncohen created at 2009-10-22 08:04:50

Do we both agree on a positive review, then ? ;-)


---

Comment by ncohen created at 2009-10-26 07:03:05

Well, I'll take your "Looks really nice. I'm fully satisfied with the patch" as as an answer :-)


---

Comment by ncohen created at 2009-10-26 07:03:05

Changing status from needs_review to positive_review.


---

Comment by boothby created at 2009-10-26 23:01:30

Changing status from positive_review to needs_work.


---

Comment by boothby created at 2009-10-26 23:01:30

Sorry guys, reviewers need to not touch the code.  Rather... authors can't give the final +1.


---

Comment by boothby created at 2009-10-26 23:01:39

Changing status from needs_work to needs_review.


---

Comment by mhansen created at 2009-12-07 08:47:33

Resolution: fixed


---

Comment by mhansen created at 2009-12-07 08:47:33

Looks good to me.
