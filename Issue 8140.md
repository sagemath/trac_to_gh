# Issue 8140: words.CharacteristicSturmianWord does not do what it says

Issue created by migration from Trac.

Original creator: slabbe

Original creation time: 2010-01-31 23:52:08

Assignee: sage-combinat

CC:  abmasse

The doc of `words.CharacteristicSturmianWord` says :


```
INPUT:
-  ``cf`` - an iterator outputting integers (thought of as a
               continued fraction)
```


But it does not do what it says. In fact the following 


```
sage: cf = CFF(1/golden_ratio^2)
sage: words.CharacteristicSturmianWord(cf)
word: 0010001001000100010010001001000100010010...
```


should output the same as


```
sage: words.FibonacciWord()
word: 0100101001001010010100100101001001010010...
```




---

Comment by slabbe created at 2010-02-01 00:15:23

Changing status from new to needs_review.


---

Attachment


---

Comment by slabbe created at 2010-02-01 21:05:23

I just uploaded the patch : I corrected a sphinx warning. I hope it will not create conflicts if Alexandre started a review...


---

Comment by abmasse created at 2010-02-03 14:48:31

I reviewed this patch and made the following minor modifications, mostly in the documentation:
- I gave three different equivalent definitions of characteristic Sturmian word as presented in the Lothaire book.
- I changed the name of the variable `cf` for `slope` in the characteristic Sturmian.
- I modified the NotImplementedError raised by the three functions by a ValueError. It seems more appropriate since values of slope are in general assumed to be in (0,1). Sébastien, if you still insist on keeping NotImplementedError, I would put a different message, something like "not implemented for values out of (0,1)"
- I made other minor changes and updated the examples in consequence.
All tests passed, the code seems good and correct the problem mentionned in this ticket. The doc is alright too.


---

Attachment

Few minor changes -- I let Sébastien check if he approves the changes


---

Attachment

Applies over the two precedent patches.


---

Comment by slabbe created at 2010-02-04 17:30:10

I agree with your changes. I fix the doc (the irrationality of alpha is necessary for the lower and upper mechanical word to be equal). I also added `rename_keyword` of the `cf` argument that you removed for backward compatibility.

I give a positive review to Alexandre's changes. Alexandre, I let you change the status of the ticket to positive review if you agree with my two patches.


---

Comment by slabbe created at 2010-02-04 17:32:06

Full name in those boxes helps the release managers when writing the release notes.


---

Comment by abmasse created at 2010-02-04 21:51:36

Rechecked the three functions after applying all three patches and everything looks fine. All tests passed, the doc built with Sphinx looks alright too and I agree with the last minor changes of Sébastien. Positive review as well !
Thanks for the info about the full names in the boxes, I wasn't sure what to do about that.


---

Comment by abmasse created at 2010-02-04 21:51:36

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-10 14:32:51

The commit string for the third patch is not sufficiently descriptive.  I've refreshed it in my queue for 4.3.3.alpha0: `#8140: Added rename_keyword for the cf argument`.  Please let me know if this is not good enough!


---

Comment by slabbe created at 2010-02-10 14:41:06

Replying to [comment:7 mpatel]:
> The commit string for the third patch is not sufficiently descriptive.  I've refreshed it in my queue for 4.3.3.alpha0: `#8140: Added rename_keyword for the cf argument`.  Please let me know if this is not good enough!

It is perfect (sorry, I forgot to write the description).


---

Comment by mpatel created at 2010-02-11 14:47:41

Resolution: fixed
