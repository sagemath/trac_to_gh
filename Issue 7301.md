# Issue 7301: Gale Ryser theorem

Issue created by migration from Trac.

Original creator: ncohen

Original creation time: 2009-10-25 19:44:48

Assignee: mhansen

CC:  sage-combinat

The Gale-Ryser theorem is about filling a matrix with 0 and 1 when you know the number of 0 and 1 in each column and in each row. 

It would not be too much work to write in Sage a function filling a matrix with 0 and 1 when the data is correct, and returning an error otherwise...

More informations there : http://mathworld.wolfram.com/Gale-RyserTheorem.html


---

Comment by ncohen created at 2009-12-03 11:22:50

Changing status from new to needs_review.


---

Comment by ncohen created at 2009-12-03 11:23:15

Here it is ! :-)


---

Comment by wdj created at 2009-12-03 12:16:14

I can review this in a week or two since a colleague here is an expert in that area (and I'll be finished with teaching then:-). 

Is the graph-theoretic analog of this theorem implemented? (The Haval-??? Theorem?)


---

Comment by ncohen created at 2009-12-03 12:27:00

I'm glad to hear it !! This is my second attempt at a contribution to the Combinatorics section, and I hope you will find it useful :-)

The odd thing is that if I knew of the Gale Ryser theorem, I never heard of the theorem you are talking about, when it clearly should be the opposite... Could you tell me what this theorem is about ? I was not able to find it using "haval" on Google, and I am very interested in what it could be :-)

The only direct use I could make of this theorem in Graph Theory is deciding whether there exists a bipartite graph with a given degree sequence... Is that the result you are mentionning ? :-)

And by the way, I only wrote this function for squares matrices when it is not required.. Thinking about bipartite graphs helped me notice :-)

Nathann


---

Comment by wdj created at 2009-12-03 12:53:12

Replying to [comment:4 ncohen]:
> I'm glad to hear it !! This is my second attempt at a contribution to the Combinatorics section, and I hope you will find it useful :-)
> 
> The odd thing is that if I knew of the Gale Ryser theorem, I never heard of the theorem you are talking about, when it clearly should be the opposite... Could you tell me what this theorem is about ? I was not able to find it using "haval" on Google, and I am very interested in what it could be :-)
> 
> The only direct use I could make of this theorem in Graph Theory 
> is deciding whether there exists a bipartite graph with a given 
> degree sequence... Is that the result you are mentionning ? :-)
> 


Yes, I believe that is it. But I think the Haval-??? Theorem generalizes that a bit.


> And by the way, I only wrote this function for squares matrices when it is not required.. Thinking about bipartite graphs helped me notice :-)
> 
> Nathann


---

Comment by ncohen created at 2009-12-04 17:14:31

Now with non-square matrices ;-)


---

Comment by hivert created at 2009-12-07 23:29:32

Hi there,

There is something I don't get in the doc:

```
The Gale Ryser theorem asserts that if `p_1,p_2` are two 
partitions of `n` of respective lengths `k_1,k_2`, then there is 
a binary `k_1\times k_2` matrix `M` such that `p_1` is the vector 
of row sums and `p_2` is the vector of column sums of `M`, if 
and only if `p_2` dominates `p_1`.
```

I suggest that the role of `p_1` and `p_2` are not symmetric... Is this really a "if and only if" ? If you transpose the matrix then the role of `p_1` and `p_2` are exchanged... Or dominate is not the same as dominance order...

Am I definitely confused ???

Florent


---

Comment by ncohen created at 2009-12-07 23:32:28

oopsssssss !!! Would "if and only if the conjugate of p_2 dominates p_1"make you feel better ? :-)

This is what the code does ( and what the theorem says )  :-)

Nathann


---

Comment by wdj created at 2009-12-08 03:50:12

I am not an expert but I do have a colleague who not only wrote his thesis on a related result but claims that the Gale-Ryser theorem was one of the results which inspired him to become a combinatorialist.

He is not satisfied with your implementation. He had problems with the wording of the documentation, though he admitted this was only a minor issue. (For example, "dominated" should be "majorized"...) More important, he believed, was that the only construction implemented was a special one (in particular, Ryser's construction was not implemented). Without being specific, he said that more options should be available to the user, to allow for different types of features/constructions.
(For example, one could allow matrices taken from another subset of numbers, as opposed to just {0,1}.)

He was also hoping to have a construction of the graph-theoretic analog (given a possible degree sequence, construct a graph having that degree sequence). I presume though that, if you decided to implement that, you would create a separate ticket.

Thanks very much for working on this! I know this is a bit vague, so please ask questions and I will ask for more details from my colleague.


---

Comment by hivert created at 2009-12-08 06:13:09

Replying to [comment:10 wdj]:

> He is not satisfied with your implementation. He had problems with the wording of the documentation, though he admitted this was only a minor issue. (For example, "dominated" should be "majorized"...) 

This is clearly a question of community. Those kind of matrix problem arise in the representation theory of Symmetric Groups or in symmetric functions and in this context I've allways seen the order called dominance order. See eg:  Macdonald, I. G. Symmetric Functions and Hall Polynomials, 2nd ed. Oxford, England: Oxford University Press, 1995.

> More important, he believed, was that the only construction implemented was a special one (in particular, Ryser's construction was not implemented). Without being specific, he said that more options should be available to the user, to allow for different types of features/constructions.
> (For example, one could allow matrices taken from another subset of numbers, as opposed to just {0,1}.)

Again in the theory of symmetric function and descent algebra of the symmetric group, it is useful not to give a single solution but to give all of them, without restricting et entries of the matrix to be smaller than one (i.e. any non negative integer). Moreover the order of the input is important so that I'd rather have the input to be composition rather than partition. However I don't know if in this case we need a different enumeration algorithm. You can have a look at  http://mupad-combinat.sourceforge.net/doc/en/combinat/integerMatrices.html
to see what we had in MuPAD-Combinat.
 
> He was also hoping to have a construction of the graph-theoretic analog (given a possible degree sequence, construct a graph having that degree sequence). I presume though that, if you decided to implement that, you would create a separate ticket.
> 
> Thanks very much for working on this! I know this is a bit vague, so please ask questions and I will ask for more details from my colleague.


---

Comment by ncohen created at 2009-12-08 07:48:00

Hello everybody !!! Well, concerning the wording issue, I believe that it is correct in this case, or that at least it depends on communities, especially, when one looks at the code : "the conjugate of p2 dominates p1" is written "p2.conjugate().dominates(p1), so surely I am not the only one to give these definitions to these words :-)

The other issue seems for you to expect more than just a solution : you are both talking about the complete enumeration of the matrices corresponding to these criteria, and through Linear Programming I can olny give you a simple solution, as solvers are not that bright on the enumeration side... Would you happen to have a reference for this algorithm ? I was onnly able to find a proof to show one matrix existed, but nothing about enumerating them. I also have to admit that if writing this function was quick enough because I knew what I needed and how to use it, I may not have enough time available too look for a new ( and possibly long ) algorithm and implement it.

Do you feel like this algorithm is totally useless as it is, or could it be possible to take this function and create a ticket to move it to a enumeration problem ?

Besides, your friend was talking about "different subsets of numbers". Well, I only met this problem for 0-1 matrices and I assume your are not talking about replacing 0 by x and 1 by y... Do you mean that there is a version of this theorem working simultaneously for several types of different variables (with two partitions per type of variable, etc...)  ?? This would interest me very much !!

Thank you for your interest !

Nathann


---

Comment by wdj created at 2009-12-08 13:11:48

No, I think this is a useful patch. Also, I agree that the enumeration problem is a separate ticket. I am not an expert, so to review your patch, which I think is interesting, I am told to read


```
Combinatorial Matrix Theory
by Brualdi and Ryser, Chapter 6

Combinatorial Matrix Classes
By Brualdi (I think this has a whole chapter on A(R,S), the 
set of (0,1)-matrices with prescribed row sums R and col sums S.

Combinatorial Mathematics
By Ryser (has a chapter on A(R,S))
```

They shouldn't take long to read but I don't own these and will 
have to make a trip to the library, which I will try to do tomorrow.
 
I was also told of a very interesting application of the Gale-Ryser
theorem to medical imaging (which you may already know about):


```
Discrete tomography
http://en.wikipedia.org/wiki/Discrete_tomography
```



---

Comment by wdj created at 2009-12-08 13:16:59

Replying to [comment:12 ncohen]:
> Hello everybody !!!  

...

> 
> Besides, your friend was talking about "different subsets of numbers". Well, 
> I only met this problem for 0-1 matrices and I assume your are not talking about 
> replacing 0 by x and 1 by y... Do you mean that there is a version of this theorem 
> working simultaneously for several types of different variables (with two partitions 
> per type of variable, etc...)  ?? This would interest me very much !!
> 


Yes, he indicated that a very simple modification of the construction should 
allow one to construct matrices whose entries are in (say) {0,1, ..., m-1}, 
with give column sums and given row sums if one exists. (Here m > 1 is
a user-supplied integer which is m=2 in your current implementation.)


> Thank you for your interest !
> 
> Nathann


---

Comment by wdj created at 2009-12-10 12:32:14

Nathann:

I have started reading these books and spoken to my colleague again. The book


```
Combinatorial Mathematics
By Ryser (has a chapter on A(R,S))
```

has a construction (due to Ryser) which is in many cases more valuable than the construction implemented (due to Gale). Moreover, the implementation of the construction assumes that the R,S have no
trailing 0's. It seems natural to assume that the user can simply remove any trailing 0's in the input sequence (I thought so myself). However, my colleague assures me that if you could implement the exact same function but allow for trailing 0's then the function would be more useful.

I need to digest the Ryser algorithm better but thought I would post this update FYI.


---

Comment by ncohen created at 2009-12-11 15:19:52

I began to read the chapter six and it is indeed very interesting :-)

I did not get to the point where Ryser enumerates these matrices or speaks about multiple values beyong 0-1..

Thanks !!!

Nathann


---

Comment by wdj created at 2009-12-13 22:53:07

Please see
http://sage.math.washignton.edu/home/wdj/sagefiles/gale-ryser.sage
Hope it helps!


---

Comment by wdj created at 2009-12-13 22:53:55

Replying to [comment:17 wdj]:
> Please see
> http://sage.math.washignton.edu/home/wdj/sagefiles/gale-ryser.sage
> Hope it helps!

Make that http://sage.math.washington.edu/home/wdj/sagefiles/gale-ryser.sage


---

Comment by ncohen created at 2009-12-14 08:29:09

Excellent !!! Well, could you send your code as a patch to replace mine then, as it does not use LP ? :-)

two remarks though : 

    * Perhaps "slider" could be defined inside the gale_ryser function, except if it can be useful in other parts of Sage
    * The order defined on the partitions is equivalent to the the function "dominates" in the Partition class.. In my patch it was written as p2.conjugate().dominates(p1), so it may not be necessary to rewrite it

Great work !! :-)

Nathann


---

Comment by wdj created at 2009-12-14 21:52:27

Replying to [comment:19 ncohen]:
> Excellent !!! Well, could you send your code as a patch to replace mine 
> then, as it does not use LP ? :-)
>


I will submit my code to my colleague, who does not use Sage 
or know how to program (as far as I know) but can read Python:-)

He already said that you have implemented Gale's algorithm, and
I have implemented Ryser. He does not agree that your implementation
should be replaced by mine. Perhaps we make my implementation
the default since it seems "more elementary" than yours? 

More later when I receive his report.

 
> two remarks though : 
> 
>     * Perhaps "slider" could be defined inside the gale_ryser function, 
> except if it can be useful in other parts of Sage
>     * The order defined on the partitions is equivalent to the the 
> function "dominates" in the Partition class.. In my patch it was written 
> as p2.conjugate().dominates(p1), so it may not be necessary to rewrite it
> 
> Great work !! :-)
> 
> Nathann


---

Comment by ncohen created at 2009-12-15 08:27:30

Your is both an algoorithm and a proof, which makes it more interesting than mine. Besides, yours does not require the package GLPK to be installed.. I even doubt my version could be faster so... :-)


---

Comment by ncohen created at 2009-12-15 08:27:30

Changing status from needs_review to needs_work.


---

Comment by wdj created at 2009-12-17 16:23:08

Just an update: My colleague agrees that my implementation is corect. There was a issue because I told him that in my opinion the 
algorithm (due to Ryser) as stated in the literature was imcomplete.
(A loop was missing in the pseudocode.) He also said he proved that my version of the implementation was correct, though he did not write anything down. He also said he had some suggestions for me but did not say what they were.

Now he is grading finals but when he finishes, and I finish with my grading, I'll be able to add the two Gale-Ryser implementations together.


---

Comment by ncohen created at 2009-12-18 08:09:50

Hello !! I just noticed some paper among today's publications that may interest people here :
On the number of matrices and a random matrix with prescribed row and column sums and 0–1 entries

You can get it there :
http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6W9F-4XXNXT2-1&_user=6068170&_rdoc=1&_fmt=&_orig=search&_sort=d&_docanchor=&view=c&_acct=C000016487&_version=1&_urlVersion=0&_userid=6068170&md5=431a8b6346a7a0a472ae72d9d21a5184

Nathann


---

Comment by wdj created at 2009-12-27 23:44:24

Replying to [comment:6 ncohen]:
> Now with non-square matrices ;-)


What does this mean? You still have


```
        if sum(p1) != sum(p2):
            raise ValueError("The two partitions must sum to the same value.")
```



---

Comment by wdj created at 2009-12-28 01:47:37

Replying to [comment:25 wdj]:
> Replying to [comment:6 ncohen]:
> > Now with non-square matrices ;-)
> 
> 
> What does this mean? You still have
> 
> {{{
>         if sum(p1) != sum(p2):
>             raise ValueError("The two partitions must sum to the same value.")
> }}}

Sorry, dumb question.

This is what I should have asked: The condition


```
       if sum(p1) != sum(p2):
            raise ValueError("The two partitions must sum to the same value.")
```

should be replaced by a condition on p1 and the *conjugate* of p2,
shouldn't it?


---

Comment by ncohen created at 2009-12-28 08:05:34

Well, the condition on the domination of p* may be fulfilled while the  two partitions do not sum to the same value, which is clearly necessary, so we need the two conditions to be checked ( and summing the fastest of the two )...

well, actually I thought after out little chat that we should forget about the LP version and implement yours when you will have found the time to write it.

It's up to you ! :-)

Nathann


---

Comment by wdj created at 2009-12-28 18:53:13

apply this patch only to 4.3.


---

Attachment

This passes sage -testall on an ubuntu machine. 

Nathann: Can you please look at this? Please check your LP code, which I modified slightly. Feel free to add a referee's patch (eg, adding an AUTHORS field, which I just noticed I forgot).

It turned out that partition was the wrong place to put it. My colleague who refereed it did not like that the integer vectors were not allowed to have trailing 0's and so that ruled out allowing gale_ryser_theorem to be a method for the Partition class.


---

Comment by wdj created at 2009-12-28 18:57:30

Changing status from needs_work to needs_review.


---

Comment by wdj created at 2010-01-06 20:16:53

In reply to an email Nathann Cohen sent me:

> Several questions about your patch :
>    * Do you think function slider01 is useful by itself in the
> integer_vector class ( and if so, under, should'nt it be renamed to be
> more "explicit", if possible ? ) ? My advice is that it may be better
> to move it *inside* of function fale_ryser_theorem


Python has a mechanism for "private" functions like slider01, so
I renamed it _slider01. I think that is better than hiding it inside
gale_ryser_theorem. Is that okay?


>    * There is one commented line in is_gale_ryser
>    * Why don't you want to use the method Partition.dominates for
> your test in is_gale_ryser ?


I think this will not work, if you want to allow trailing 0's.
Maybe I am missing something?


>    * Why do you say that the LP formulation is Gale's construction ?
> You mean that Gale proved this result using LinearProgramming ? If so,
> do you have access to an electronic version of the text you are citing
> ? I'd be extremely interested in giving it a look... Very few
> theretical results are proved using LP :-)

I was told that by my colleague which is much much more of an expert on
this stuff. I have not read Gale's paper and don't know of an electronic version.


>    * In you docstrings you frequently use $$ for LaTeX expressions.
> As I never saw it anywhere in Sphinx, I do not know whether it works :
> I always use ` instead of $. Is the documentation built correctly this
> way ? I prefer your $ to my usual `, so I'm interested in the
> answer....


I changed all $ to '. Thanks!


>    * I will be running tests to compare the speed of your
> construction of the matrices... I expect your method to be much faster
> than mine, perhaps something about it should be said in the docstrings
>    * I do not know if it is a requirement of Sphinx, but Minh ( who I
> claim is perfection made flesh ) gave me several "needs work" because
> of the way I formatted docstrings for References. What I take for
> model now is the functions citing Cliquer in the graph.py file. The
> document's keys are not integers but "the usual" concatenations of the
> authors'initials and the year, for example [Ryser63] and [Gale57].
> Besides, they appear with a trailing _ when used to cite the paper.
> You are bound to find one if you look for the string "]_" in Sage's
> files ( but you will definitely find them if you look for "Cliquer" in
> sage/graphs/graph.py"


Thank you for the reference! I think the docstrings are okay now.


>    * In gale_ryser_theorem the two :: after EXAMPLES should be
> removed for the generated documentation to be correct. Same thing
> after References, and in slider01. The sign :: is saying to Sphinx
> that what is following is a piece of Sage code. So you should only
> write them when it is the case, for example after EXAMPLES in
> is_gale_ryser. It may be better to generate the documentation to check
> that it is visually correct :-)


Done. Thanks.


>
> I will be keeping an eye on Sage-devel to be kept aware of the next
> alpha release... I tried alpha0 which failed to compile on my computer
> and I am at the moment without any Sage install available ( I have
> sage.math in case of need, though ). I hope it will be available soon
> :-))))))


---

Attachment

seems to apply to 4.3* and test okay. Apply only this patch.


---

Comment by ncohen created at 2010-01-09 11:18:15

I thought you could have sorted the lists, created the corresponding Partition objects, then used the dominates/conjugate methods... Well, it is not that bad a problem anyway :-)
I'll give it a look pretty soon... Sorry for the last two days, I was (against my will) kept away from internet !

Nathann


---

Comment by ncohen created at 2010-01-10 08:56:18

> Python has a mechanism for "private" functions like slider01, so
> I renamed it _slider01. I think that is better than hiding it inside
> gale_ryser_theorem. Is that okay?

Well, do you think slider01 could be used by ither methods ?

> I think this will not work, if you want to allow trailing 0's.
> Maybe I am missing something?
The Gale-Ryser theorem tells you that given two partitions, there is a matrix satisfying the constraints if and only if the domination criterion is checked. Well, the point you made about trailing 0's is that you do not necessarily want the column's sums in your final matrix to be *sorted in decreasing order*. When you have a binary matrix, though, you can modify it by inverting two columns without changin the rows sums, and the columns sum still have the same set of sums. So instead of just taking care of trailing 0, the best may be to take care of non-sorted sequences, which is the general case of the theorem.

> I was told that by my colleague which is much much more of an expert on
> this stuff. I have not read Gale's paper and don't know of an electronic version.
Then the best is to :
    * Cite the reference to justify the names Gale's method and Ryser's method
    * Alternatively, use algorithm="LP" instead of Gale, as we can not say more without references ( plus it gives some enlightenment as to the algorithm used and the complexity )

Nathann


---

Comment by ncohen created at 2010-01-10 08:56:18

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-01-11 11:27:24

New version, after some emails exchanged :

* The function is_gale_ryser does not apply only to "partitions"
anymore, but to any sequence of integers. The purpose of the
Gale-Ryser theorem is to answer whether there exists a matrix with the
given row/column sums, which has nothing to do with Partitions, or
decreasings orders, or zeros, or anything else -- just positive
values. The function is_gale ryser only takes two integer lists as its
arguments, and answers yes if there exists a matrix satisfying the
constraints.

* There is a new section ALGORITHM in is_gale_ryser

* Various fixes in the docstrings

* gale_ryser_theorem has been slightly modified to accept unordered
sequences, and zeros. It involves marking a sorted copy of the list
without the zeros, using the algorithm you implemented, then add the
empty rows/columns and apply the reverse of the permutation applied by
the sorting.

* Your comments made me think again about this definition inside a
definition.... In the end I got convinced it was a very ugly way to
code and do not intend to say anything about it again :-)

Nathann


---

Comment by ncohen created at 2010-01-11 11:27:24

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by ncohen created at 2010-01-11 11:28:49

* THE LATEST PATCH IS NOW trac_7301.patch *


---

Comment by wdj created at 2010-01-11 11:40:26

Thanks Nathann! 

I'll start testing it now.


---

Comment by wdj created at 2010-01-11 15:40:42

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-01-11 15:40:42

applies to 4.3.a9 and 4.3 fine and passes testall except for some presumably unrelated failures on ubuntu 64bit and mac 10.6.2.

Positive review.

Thanks again Nathann!


---

Comment by rlm created at 2010-01-13 08:56:17

David as Author and Nathann as Reviewer? It's not entirely clear to me, so can you fill out those slots for me?


---

Comment by rlm created at 2010-01-13 08:56:17

Resolution: fixed


---

Comment by ncohen created at 2010-01-13 08:59:52

Considering the amount of work from David on this function, it seems fitting :-)
