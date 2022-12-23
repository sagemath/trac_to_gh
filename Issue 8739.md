# Issue 8739: Addition of Kolakoski word

Issue created by migration from https://trac.sagemath.org/ticket/8739

Original creator: abmasse

Original creation time: 2010-04-21 17:20:15

Assignee: sage-combinat

CC:  slabbe tmonteil

Keywords: Kolakoski, words

The Kolakoski words are important in combinatorics on words and there are many interesting conjectures that one would like to solve using Sage.

This ticket intends to add a constructor of such words.

By definition, the Kolakoski word is the infinite word `K = 22112122...` fixed under the `Delta` operator. The `Delta` of a word is simply the word describing its runs. For instance, if `w = 122112 = 1^1 2^2 1^2 2^1`, then `Delta(w) = 1221`. One can see that over the alphabet '{1,2}', the unique words fixed by `Delta` are `K` and `1K`. Moreover, this notion is naturally generalized to any alphabet `{a,b}` where `a` and `b` are two distinct positive integers.




---

Comment by abmasse created at 2010-04-21 17:20:51

I'll upload a patch very soon.


---

Attachment

Adds a generator of the Kolakoski sequences


---

Comment by abmasse created at 2010-04-23 15:03:31

Needs review !


---

Comment by abmasse created at 2010-04-23 15:03:31

Changing status from new to needs_review.


---

Comment by ncohen created at 2010-04-24 10:07:28

Looks nice ! :-)

Several remarks though, that I do not dare implement myself :

* You specify in the private function `_KolakoskiWord_iterator` that the alphabet must be composed of two positive integers, but not in `KolakoskiWord`. Are the users supposed to know they should not use anything else ? (honest question, Words are not my field at all even if I can understand the construction :-) )

* You write `current_letter = bar(w[-1])`, thus accessing the -1'th element. What about writing `current_letter = bar(current_letter)` at the end of the loop ?

* You maintain a variable named `current_run`, and keep in memory a list of letters you already used (`w[:current_run]`). Wouldn't it be easier to forget about the current run variable, and just use your list as a queue with append() and pop(0) operations ? :-)

As I did not know the construction, I thought a bit about how I would write the algorithm and could not find any way to do it without keeping a lot of things in memory, what your `w` variable actually contains. Do you know if there exists a way to get rid of it ? I'm just being curious :-)

Nathann


---

Comment by ncohen created at 2010-04-24 10:07:28

Changing status from needs_review to needs_info.


---

Comment by abmasse created at 2010-04-24 15:01:50

Replying to [comment:3 ncohen]:
> Looks nice ! :-)
> 
> Several remarks though, that I do not dare implement myself :
> 
> * You specify in the private function `_KolakoskiWord_iterator` that the alphabet must be composed of two positive integers, but not in `KolakoskiWord`. Are the users supposed to know they should not use anything else ? (honest question, Words are not my field at all even if I can understand the construction :-) )
> 
You're right, I forgot to document it in the main function. 

> * You write `current_letter = bar(w[-1])`, thus accessing the -1'th element. What about writing `current_letter = bar(current_letter)` at the end of the loop ?
> 

Right again. I think I did it to avoid initializing `current_letter` in the basis, but this is less readable and we're not sure if `w[-1]` is performed in constant time. Is it ?

> * You maintain a variable named `current_run`, and keep in memory a list of letters you already used (`w[:current_run]`). Wouldn't it be easier to forget about the current run variable, and just use your list as a queue with append() and pop(0) operations ? :-)
>

Once again right. When I first wrote the function, I did as you say, but there was a mistake I couldn't solve. Then I simplified by keeping the complete prefix of the word, but now that it is working, it shouldn't be hard to modify.
 
> As I did not know the construction, I thought a bit about how I would write the algorithm and could not find any way to do it without keeping a lot of things in memory, what your `w` variable actually contains. Do you know if there exists a way to get rid of it ? I'm just being curious :-)
> 

I feel it would be hard, but I don't have any proof. On the other hand, I can get rid of all values of `w` that have already been read by the `current_run` cursor, as you mentionned above.

> Nathann

Thank you for your comment. I'll upload a new patch soon.


---

Comment by abmasse created at 2010-04-24 15:01:50

Changing status from needs_info to needs_work.


---

Comment by ncohen created at 2010-04-24 15:05:27

I couldn't tell you whether it is performed in constant time, but even if it is, from the point of view of complexity, I expect bar(your variable) to be faster than using a dictionnary's structure :-)

I'll ask google whether there is anything around about generating this word without needing an increasing amount of memory :-)

Nathann


---

Comment by abmasse created at 2010-11-14 03:08:07

Applies on top of the main patch


---

Comment by abmasse created at 2010-11-14 03:09:53

Changing status from needs_work to needs_review.


---

Attachment

I uploaded a patch that applies on top of the main one. It takes into account the three points mentionned by Nathann above. Needs review again! (Sorry for the seven months delay)


---

Attachment

Applies over the precedent 2 patches


---

Comment by slabbe created at 2010-11-14 06:08:36

I just added a new patch which applies on the two precedent. All tests passed. Documentation builds fine. The Kolakoski word satisfies its definition for prefixes up to 100000.

To me it is a positive review. I let Alexandre change the status of the ticket to positive review if he agrees with my changes.

Maybe Nathann wants to take a look?


---

Comment by abmasse created at 2010-11-14 16:38:35

Hi Sébastien and Nathann!

Thank you for the review. I agree with Sébastien's changes. I retested all of it on sage-4.6 and all tests still pass. I also took a look at the documentation, which builds fine and is clearer than before. I'll wait for Nathann to see if he agrees with both our modifications and if he's satisfied with my answers to his comments.


---

Comment by ncohen created at 2010-11-16 06:56:58

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2010-11-16 06:56:58

Hello !! 

Same result for me : all is nice on the doctest's side, and the documentation has no fault that I could spot `:-)`... Nothing to add for the code either, and so this patch is good to go `:-)`

Nathann


---

Comment by jdemeyer created at 2011-01-12 06:31:50

Resolution: fixed


---

Comment by tmonteil created at 2011-01-27 23:22:57

Hi,

since the Kolakoski sequence can also be seen as a sequence of integers, it appears in Sloane : http://oeis.org/A000002

Hence, it could be a good idea to integrate this in `sage/combinat/sloane_functions.py` and create the class A000002.
