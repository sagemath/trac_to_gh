# Issue 9395: new doctest for french book about Sage

Issue created by migration from https://trac.sagemath.org/ticket/9395

Original creator: zimmerma

Original creation time: 2010-06-30 13:14:12

Assignee: mvngu

CC:  was cremona ylchapuy

The attached patch includes a new doctest for a book (in french) some
people are writing about Sage (see the README file for the list of
authors).

This book will be available under a CC-by-sa license.

This patch contains only the doctests for one chapter (about number
theory). Some more doctests will follow, one per chapter, but we
already submit that one to see if some things need to be fixed.

This doctest was tested successfully with Sage 4.4.2 under Fedora 12.


---

Comment by zimmerma created at 2010-06-30 13:21:06

I found no way so that the `%timeit ...` or `time ...` lines are tested, thus I've added
`# not tested`. If somebody knows how to do so that in `%timeit a = b + c` at least the
instruction `a = b + c` is performed, please tell me.


---

Comment by zimmerma created at 2010-06-30 13:21:06

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-06-30 13:25:16

Changing status from needs_review to needs_work.


---

Comment by mvngu created at 2010-06-30 13:25:16

You don't need to put your doctests inside a function. I think it's much simpler to put your doctests inside a docstring. See the files under tests/ in the Sage library for examples. You should also consider giving your book's directory name a more descriptive name. Something like "number_theory_zimmermann", not just "sagebook". Or do you envision the directory "sagebook" to contain doctests of books that leverage the Sage doctesting framework? In that case, see [this script](http://www.bitbucket.org/mvngu/textract) for a proof of concept for automatic extraction of Sage code and doctesting the extracted code. That script has been tested on this [Sage book](http://code.google.com/p/factor-book/).


---

Comment by zimmerma created at 2010-06-30 14:10:40

Replying to [comment:3 mvngu]:

the new patch addresses your remarks.

Paul


---

Comment by zimmerma created at 2010-06-30 14:10:40

Changing status from needs_work to needs_review.


---

Attachment

table of contents of the book


---

Comment by zimmerma created at 2010-07-01 08:52:16

current version of chapter on number theory


---

Attachment

The version 1.0 of the book has now appeared, and is available from
http://www.loria.fr/~zimmerma/sagebook.html. Any feedback is most welcome!


---

Comment by zimmerma created at 2010-07-12 11:10:47

Yann, please could you review this? What you have to do (William please correct me if needed):

1) [optional] check the content of the numbertheory.py file matches the corresponding chapter of the book. I write "optional" since this should be our (the authors of the book) responsability.

2) check the new doctests pass with the latest Sage version (we used 4.4.4)

Paul


---

Comment by was created at 2010-07-12 20:07:52

Replying to [comment:6 zimmerma]:
> Yann, please could you review this? What you have to do (William please correct me if needed):

Sounds good to me. 

I've been advertising your book to all the French people I meet in Paris, e.g., at Euroscipy, and also to Bernandi at Jussieu today (he's one of the original PARI guys).


---

Comment by zimmerma created at 2010-07-12 21:12:12

Replying to [comment:7 was]:
> I've been advertising your book to all the French people I meet in Paris, e.g., at Euroscipy, and also to Bernandi at Jussieu today (he's one of the original PARI guys).
thanks, some people of my lab who were at Euroscipy indeed told me today that they heard of our book there!
Paul


---

Comment by ylchapuy created at 2010-08-15 21:03:24

Replying to [comment:6 zimmerma]:
> Yann, please could you review this? What you have to do (William please correct me if needed):
> 
> 1) [optional] check the content of the numbertheory.py file matches the corresponding chapter of the book. I write "optional" since this should be our (the authors of the book) responsability.
> 
> 2) check the new doctests pass with the latest Sage version (we used 4.4.4)
> 
> Paul

Sorry for the delay.
All tests passed with Sage 4.5.2.

Regarding the `timeit` issue, you could change 

```
    sage: %timeit (a^e) # not tested
```

for

```
    sage: timeit('a^e') # random
```


(and also `# long` for some of them).

I put it to `need info` for now, but feel free either to change this and ask me for a review (I'll be faster this time) or don't change anything and give a positive review.

 Yann


---

Comment by ylchapuy created at 2010-08-15 21:03:24

Changing status from needs_review to needs_info.


---

Comment by zimmerma created at 2010-09-01 16:09:32

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-09-01 16:09:32

thank you Yann for your comments. I attach a new patch taking them into account. I left the
last `time r=...` as `not tested` since I do not know how to make it work, without
changing `time` into `timeit`, which would be not coherent with the book.

Paul


---

Attachment


---

Comment by ylchapuy created at 2010-09-01 17:31:00

apply on top of trac_9395.patch


---

Attachment

Everything is still ok for me. I added 'long time' to the longest tests, this reduces the time for normal testing to 12 seconds on my computer compared to 67 for the long version.

Paul, if you agree with my reviewer's patch, you can give this ticket a positive review.

       Yann


---

Comment by zimmerma created at 2010-09-01 19:29:50

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-09-01 19:29:50

> Paul, if you agree with my reviewer's patch, you can give this ticket a positive review. 

yes I agree.
Paul


---

Comment by mpatel created at 2010-09-05 03:30:23

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-09-05 03:30:23

Could someone please update both patches with more descriptive commit strings (and change the status back to "positive review")?


---

Comment by zimmerma created at 2010-09-06 18:51:34

Replying to [comment:13 mpatel]:
> Could someone please update both patches with more descriptive commit strings (and change the status back to "positive review")?

done with a combined patch (apply only that one). Is that what you wanted?

Paul


---

Comment by mpatel created at 2010-09-06 21:42:07

I apologize for not being clearer.  The first line of the commit string for each patch to be merged should start with the ticket number and contain a short description of what the patch does.  This line should be < 80 characters in length.

For example: `#9395: Number theory doctests for French book about Sage` and `#9395: Reviewer patch: tag longest tests as long`.

The reason for these policies is so that `hg log` and `hg log filename.py` tell us what a changeset did and which Sage trac ticket we can consult for background.

Of course, extra lines are welcome and may help to explain details to a reviewer or someone who uses `hg log -p`.

Could you update the just first line of the combined patch?


---

Comment by zimmerma created at 2010-09-07 08:13:24

apply only this patch


---

Attachment

> Could you update the just first line of the combined patch? 

done.
Paul


---

Comment by zimmerma created at 2010-09-07 08:14:04

Changing status from needs_work to positive_review.


---

Comment by mpatel created at 2010-09-15 10:40:52

Resolution: fixed


---

Attachment

Update `MANIFEST.in` and `setup.py` with new file and directory


---

Comment by mpatel created at 2010-09-17 02:59:26

I've added a release manager's patch that ensures the files added here are included in a new Sage source distribution.


---

Comment by mpatel created at 2010-09-19 21:38:20

Ticket #9951, about a missing `__init__.py` file, follows up on this ticket.
