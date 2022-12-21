# Issue 8347: Test the positivity of the real part of a number field element

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-02-24 15:40:31

Assignee: davidloeffler

CC:  sage-combinat

Keywords: test, positivity, real

test if an element of a number field is positive or negative. 

Especially for real element of a CyclotomicField, we need this test for theory representation of complex reflection groups.


---

Attachment


---

Comment by nborie created at 2010-02-24 15:42:52

Changing status from new to needs_review.


---

Comment by nborie created at 2010-02-24 16:16:27

I am clearly not a speciallist for this kind of job. There is two propositions to solve this problem. The second one comes after some remarks from some guys at Sage Days 20....


---

Attachment


---

Comment by nborie created at 2010-02-24 20:35:15

Here comes a third version which say True if an algebraic complex number is a real positive and False otherwise. (Another suggest from another people....)

Feel free to give some advises about :
- the name of this method
- the test (usable not only in Coxeter Group theory)
- the way to implement this
- ....


---

Comment by zimmerma created at 2010-02-25 14:23:25

should one test all 3 patches, or only the last one?


---

Comment by zimmerma created at 2010-02-25 14:23:25

Changing status from needs_review to needs_info.


---

Comment by nborie created at 2010-02-25 15:59:38

Changing status from needs_info to needs_review.


---

Comment by nborie created at 2010-02-25 15:59:38

Hi Paul,

This is a question of design. As Nicolas Thiery and Jean Michel got a look on the two first propositions, they ask me to do the third one. You can just look the two first and confirm the disign was not the better... But if you want to test, just test the last one which seems to be the better solution (No error and just True/Flase answering...).

So, just review the third patch.

Thanks for all.


---

Comment by zimmerma created at 2010-02-25 18:20:18

I've reviewed the 3rd patch.

I noticed a few typos: `dependant` should be `dependent`, `embendding` should be
`embedding`.

Also I don't understand why `long time` since the tests are fast.

Finally a test is missing with a `None` result (apparently the last test should return None
instead of False).


---

Comment by zimmerma created at 2010-02-25 18:20:18

Changing status from needs_review to needs_work.


---

Comment by nborie created at 2010-02-26 08:51:28

I removed the # long time guards. I changed the description of the ticket and I changed the doc of the function (It now does what it is described in the doc... (I hope so...)). I configured my emacs with aspell (It is really time to do it!!!!!). I am very very very sorry to have presented a so much horrible work on the trac. Feel free to scold me very loudly! I hope you didn't lose too much time on that...


---

Comment by nborie created at 2010-02-26 08:51:28

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2010-02-26 13:33:36

Small documentation suggestion:

 - First state what the function does mathematically
 - Then give the algorithm, and mention that the result is guaranteed to be correct, and that this is achieved by increasing the approximation order until the decision can be taken. It would be nice to include a complexity result (given the order of a root, and the size of the rational coefficient, one should be able to give an upper bound on the required approximation order)

Thanks for your useful work on this!


---

Comment by zimmerma created at 2010-02-28 19:34:11

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-02-28 19:34:11

another problem:

```
sage: K.<a> = QuadraticField(-3)
sage: (a-a).is_real_positive() 
...
TypeError: Unable to convert number to real interval.
```


Paul


---

Attachment


---

Comment by nborie created at 2010-02-28 20:18:28

Changing status from needs_work to needs_review.


---

Comment by nborie created at 2010-02-28 20:18:28

I tryed to improve the doc according the advises of Nicolas. I also fix the problem that Paul pointed.


---

Comment by zimmerma created at 2010-03-01 17:01:08

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-03-01 17:01:08

I am ok with the new patch.

For the release manager: apply only `test_positivity_cyclotomic_field_3-nb.patch`.


---

Comment by nborie created at 2010-03-01 17:55:51

Thanks a lot for your patience and multireview.


---

Comment by mvngu created at 2010-03-03 14:34:01

Merged [test_positivity_cyclotomic_field_3-nb.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8347/test_positivity_cyclotomic_field_3-nb.patch).



Nicolas: you should put a sensible commit message in your patch, together with the ticket number.


---

Comment by mvngu created at 2010-03-03 14:34:01

Resolution: fixed
