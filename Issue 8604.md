# Issue 8604: Add a class for factor-enumerable words

Issue created by migration from https://trac.sagemath.org/ticket/8604

Original creator: slabbe

Original creation time: 2010-03-25 12:00:26

Assignee: slabbe

CC:  abmasse jleroy

Add a class for factor-enumerable words, i.e. having an algorithm that enumerates the factor of length n which includes finite words and some family of infinite words. The new file gathers methods (e.g. ``rauzy_graph``) that depends only on the existence of such an algorithm.

It also adds some method about left,right and bi special words:


```
    sage: f = words.FibonacciWord()[:30]
    sage: f.number_of_left_special_factors(7)
    8
```


The new class ``Word_nfactor_enumerable`` inherits from the abstract ``Word_class`` and `FiniteWord_class` now inherits from this ``Word_nfactor_enumerable`` class. Later, inifinite words having a such an algorithm will inherit also from this new class (in some other ticket).


---

Comment by slabbe created at 2010-03-25 12:07:51

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-03-25 12:37:38

Very interesting ! I'll try to review this patch as soon as I have some time.

I took a quick look at it and I have a question, though. Why aren't the iterator functions (on the left special, bispecial and right special factor) public ? Since they are used only in the public functions that return the result as a list, I think it would be better either to make the iterator functions public, or to merge the two functions in one. Unless you've a reason to do so ?


---

Comment by jleroy created at 2010-04-02 12:55:11

Hi Sébastien.

I agree with Alex about the iterators on special factors. The only thing you need is the factor set to define them, right? I will try to review it next week but as I already know what are the functions it would probably be quick.


---

Comment by slabbe created at 2010-04-11 13:32:27

> Very interesting ! I'll try to review this patch as soon as I have some time.

Great!

> I took a quick look at it and I have a question, though. Why aren't the
> iterator functions (on the left special, bispecial and right special factor)
> public ? 

I would not say that they are not public since anybody can use it and access it with tab completion by adding the underscore first.

Well because many of the iterator functions are already hidden this way in sage words. We might want to change this convention. Or maybe, like `factor_iterator`, you think it would be more practicable if those were not hidden as well?

> Since they are used only in the public functions that return the
> result as a list, I think it would be better either to make the iterator
> functions public, or to merge the two functions in one. Unless you've a
> reason to do so ?

I am against merging those two functions in one since both functions can be very usefull in different situations. The only question I see is (I don't like using the word public) :

Do we want the iterator functions of this patch to appear in the default listing of the tab completion on a word?

Sébastien


---

Attachment

Depends on #8429.


---

Comment by slabbe created at 2010-04-13 18:28:22

I just updated the patch. There was issue with the ordering of many list of factors. I added many ``sorted`` which should fix uniformize the results of doctests and not depend on the machine used anymore.


---

Comment by abmasse created at 2010-04-15 21:04:03

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-04-15 21:04:03

Replying to [comment:4 slabbe]:
> > Very interesting ! I'll try to review this patch as soon as I have some time.
> 
> Great!
> 
> > I took a quick look at it and I have a question, though. Why aren't the
> > iterator functions (on the left special, bispecial and right special factor)
> > public ? 
> 
> I would not say that they are not public since anybody can use it and access it with tab completion by adding the underscore first.
> 
> Well because many of the iterator functions are already hidden this way in sage words. We might want to change this convention. Or maybe, like `factor_iterator`, you think it would be more practicable if those were not hidden as well?
>
I understand your point, but I still think that since the class of factor-enumerable words was introduced in particular to deal with infinite words, one will probably need iterators to handle, say, left special factors. For instance, assume I want to enumerate all right special factors of a given Sturmian word. I'll need to use an iterator (the list won't be built since it's infinite). And I would like the function to appear when I hit `TAB` when calling a function on an infinite word.

What I suggest is to remove the underscore character in front of the iterators and even add a warning for the functions `right_special_factors`, etc. that tells the user that this function could not stop. 
 
> > Since they are used only in the public functions that return the
> > result as a list, I think it would be better either to make the iterator
> > functions public, or to merge the two functions in one. Unless you've a
> > reason to do so ?
> 
> I am against merging those two functions in one since both functions can be very usefull in different situations. The only question I see is (I don't like using the word public) :
>
I agree with you on this one, that was a bad idea.
 
> Do we want the iterator functions of this patch to appear in the default listing of the tab completion on a word?
>
I say yes! I know one of your argument about that was that it would reduce the number of functions appearing when you hit `TAB`. On the other hand, there are not so many of them in the case of infinite words.
 
> Sébastien
>


---

Attachment

Applies over the precedent patch


---

Comment by slabbe created at 2010-04-18 19:31:03

Changing status from needs_work to needs_review.


---

Comment by slabbe created at 2010-04-18 19:31:03

I agree with your suggestions. I changed the patch accordingly (see new patch attached).

Needs review!


---

Comment by abmasse created at 2010-06-23 20:03:42

Changing keywords from "" to "Words, factors, enumeration".


---

Comment by abmasse created at 2010-06-23 20:03:42

Hello, Sébastien and Julien !


Sorry about the delay, I've been very busy lately. I retested the patch on sage-4.4.3. All tests passed and the documentation built fine too. Therefore, I'm giving this patch a positive review.


---

Comment by abmasse created at 2010-06-23 20:03:42

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 01:43:16

Resolution: fixed


---

Comment by mpatel created at 2010-07-24 02:49:43

Please see #9589 for doctest failures that may stem from this ticket.
