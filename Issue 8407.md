# Issue 8407: word paths isometries + improve construction

Issue created by migration from https://trac.sagemath.org/ticket/8407

Original creator: slabbe

Original creation time: 2010-03-01 13:09:35

Assignee: slabbe

CC:  abmasse

1. Add a function that returns the isometries of word paths on the square grid.

2. Improve the construction of word path parent : creation from 2*n letters and n vectors now works (it takes the opposite of vectors).


---

Comment by slabbe created at 2010-03-01 13:17:55

Changing status from new to needs_review.


---

Comment by abmasse created at 2010-03-01 22:12:40

These functions are really interesting ! I can't wait to use them. However, here are some comments:

1. I think this patch is a good occasion to add functions such as `rotate()` and `reflects()` (with pertinent parameters) that compute ONE rotated or reflected version of the path instead of all EIGHT at the same time. This wouldn't be too long to do and then your function `isometries()` could call them.

2. I don't understand why you use the parameter `reversal`. If I understand it well, it is the word reversal operator, which can be geometrically interpreted as performing a rotation of angle pi (of the path) together with an orientation reversal of the path. It seems more natural to me that the parameter `reversal` correspond simply to the orientation reversal rather than to the word reversal.

3. I noticed that you do not use the word "self" while documenting, but you use "path" or other similar words. I'm not sure which one is a good practice, but I think it is better to use the first one (I'm really not sure about it, so maybe you can correct me).

What do you think ?


---

Comment by abmasse created at 2010-03-21 21:17:30

Changing status from needs_review to needs_work.


---

Comment by abmasse created at 2010-03-21 21:17:30

Just noticed I should have set this ticket to "needs work". Done.


---

Comment by slabbe created at 2010-04-11 15:15:05

I removed one of the objectives of the ticket related to isometries. Indeed, I need this function for another problem so I think its use will be more understood in context. So that is why I removed this part from this ticket. I will create a new ticket for it soon.


---

Attachment


---

Comment by slabbe created at 2010-04-11 15:18:32

Changing status from needs_work to needs_review.


---

Comment by ncohen created at 2010-04-24 11:06:23

Applies fine, does it job :-)

Thank you for your work !

Nathann


---

Comment by ncohen created at 2010-04-24 11:06:23

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 05:21:10

Resolution: fixed
