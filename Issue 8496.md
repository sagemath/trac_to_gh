# Issue 8496: Implement canonical heights for elliptic curves over number fields

Issue created by migration from Trac.

Original creator: robertwb

Original creation time: 2010-03-11 08:14:07

Assignee: cremona




---

Attachment


---

Comment by robertwb created at 2010-03-11 08:17:22

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-03-11 10:24:43

Very good. I was hoping that someone would implemented it soon ! Thanks a lot.

I will have a look at it. (And add more documentation to it : You normalised the height to be independent of the base field, which is one of the two possible normalisations, and it should be documented)


---

Comment by cremona created at 2010-03-11 10:30:02

Excellent -- I will look at it too.  I have implemented this more than once, so know the algorithm well.

Any reason not to use ticket #360 which has been patiently waiting for 3 years?


---

Comment by wuthrich created at 2010-03-11 10:53:04

The patch did not apply to 4.3.4.alpha1.

`Hunk #4 FAILED at 1687`

A rebase is needed.


---

Comment by robertwb created at 2010-03-11 18:15:39

Hmm... #360 looks like it's also about implementing height bounds as well, which I also plan to do if no one beats me to it, but don't want to wait up to get this in. 

I'll have to get ahold of an alpha to try and rebase it (and document the normalization choice).


---

Comment by was created at 2010-03-12 01:35:31

I noticed in the docstrings that you specify INPUT variables like this:

```
        1824         INPUT:: 
        1825	            v - a non-archimedean place of the base field of the curve, 
 	1826	                or None, in which case the total nonarchimedian contribution 
 	1827	                is returned 
 	1828	         
 	1829	            prec - working precision, or None in which case the height  
 	1830	                is returned symbolically 
```


I don't think this is so nice in Sphinx, since it is just preformated.  The vast majority of docstrings are formatted like as a list:


```
        1824            INPUT:
        1825	            - ``v`` - a non-archimedean place of the base field of the curve, 
 	1826	              or None, in which case the total nonarchimedian contribution 
 	1827	              is returned 
 	1828	         
 	1829	            - ``prec`` - working precision, or None in which case the height  
 	1830	              is returned symbolically 
```


Note that:
   
  * only one colon after "INPUT"
  * a dash at the start of each line
  * the indentation is two spaces after the dash.


---

Comment by was created at 2010-03-12 01:35:31

Changing assignee from cremona to was.


---

Comment by wuthrich created at 2010-03-12 09:33:09

Is there a reason the 0 is returned in QQ ?

I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.


---

Comment by robertwb created at 2010-03-12 10:02:18

Replying to [comment:7 wuthrich]:
> Is there a reason the 0 is returned in QQ ?

For consistency with the original code, and for speed (not that it should matter much). 

> I will later modify this, because I will need the exp() of the local heights for non-archimedean primes as an element in QQ, if I want to implement the p-adic heights over number fields.

You can do exp of an element of QQ just fine.


---

Comment by wuthrich created at 2010-03-12 10:09:23

Replying to [comment:8 robertwb]:
> You can do exp of an element of QQ just fine. 

Sure, that is not what I meant. I will put all your code of `nonarchimedian_local_height` into a helper function that returns r and Nv and then the main function will only take log. So that in the p-adic case I can take p-adic logs of the rational Nv.

But don't worry I will do that when I will implement p-adic height. It was only to remind myself that I should do that.


---

Comment by cremona created at 2010-03-13 15:12:46

The code looks ok to me (I spotted one mis-spelling of Silverman!), and I checked that the results agree with magma, but I'll leave the formal review to Chris who has started and wants to add to the documentation.


---

Comment by wuthrich created at 2010-03-15 15:24:15

exported against 4.3.4.alpha1


---

Attachment

I have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write "THE BSD formula", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?

I deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.

By the way the diff of our two patches comes mainly from converting tabs to spaces.


---

Comment by robertwb created at 2010-03-15 19:07:16

Replying to [comment:11 wuthrich]:
> I have put up a rebased patch with a few minor changes. But I have not included yet the documentation on the normalization. You write "THE BSD formula", but there is not a unique standard way of stating the conjecture, I fear. Also the question is whether or not you divide the height pairing by two or not. Could you clarify this ?

OK, I have expanded the normalization section, borrowing heavily from the explanation found in John Cremona's book. 

> I deleted the assumption that E was defined over Q. I don't think you will need that. Maybe it is needed that the model is integral, but I do not see where you would require the curve to be defined over Q. Please correct me if I am wrong.

Yes, you are correct. (There are examples to this effect.) 

> By the way the diff of our two patches comes mainly from converting tabs to spaces.

They were not of my doing, but thanks for expunging them.


---

Comment by robertwb created at 2010-03-15 19:08:21

Rebased and updated, apply only this patch.


---

Comment by cremona created at 2010-03-15 20:33:06

Changing status from needs_review to positive_review.


---

Attachment

New patch applies fine to 4.3.4.alpha1, and all tests in sage/schemes/elliptic_curves pass (tested both 32 and 64 bit).  Good!


---

Comment by jhpalmieri created at 2010-04-17 04:13:39

This doesn't apply cleanly to Sage 4.4.alpha0; apparently it conflicts with a patch merged into that.  Please rebase it, and we'll try hard to get it into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-17 04:13:39

Changing status from positive_review to needs_work.


---

Attachment


---

Comment by robertwb created at 2010-04-17 19:29:44

OK, rebased. It looks like it was just deleting some tabs that someone else also deleted, which was easy to fix.


---

Comment by robertwb created at 2010-04-17 19:29:44

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2010-04-17 19:30:12

Changing status from needs_review to positive_review.


---

Comment by robertwb created at 2010-04-17 19:30:12

I'm remarking this as positive review as there was no content change in the rebase.


---

Comment by jhpalmieri created at 2010-04-19 05:16:32

Merged "8496-rebased-4.4.alpha0.patch" into 4.4.alpha1.


---

Comment by jhpalmieri created at 2010-04-19 05:16:32

Resolution: fixed
