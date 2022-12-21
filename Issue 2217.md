# Issue 2217: splitting field function for number fields

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-02-20 03:50:21

Assignee: was

CC:  abrochard


```
I agree that this would be a useful funtion to have.  I would call it
splitting_field() with a description similar to that of root_field() 

...

In the meantim you should be able to work with what is available as follows:

sage: QQx.<x>=QQ[]
sage: f=(x^2-2)*(x^2-3)
sage: F=NumberField([p for p,n in f.factor()],'a')
sage: F2=F.absolute_field('b')
sage: F2.structure()

(Isomorphism from Number Field in b with defining polynomial x^4 -
10*x^2 + 1 to Number Field in a0 with defining polynomial x^2 - 3 over
its base field,
 Isomorphism from Number Field in a0 with defining polynomial x^2 - 3
over its base field to Number Field in b with defining polynomial x^4
- 10*x^2 + 1)

Here F is first defined as a relative extension, with generators a0,a1
satisfying the equations:

sage: a0,a1=F.gens()
sage: a0^2, a1^2
(3, 2)

then F2 is the associated absolute field, with F2.structure() giving
maps from each of these into the other.

sage: F2toF, FtoF2=F2.structure()
sage: FtoF2(a0)
-1/2*b^3 + 11/2*b
sage: FtoF2(a0).minpoly()
x^2 - 3
sage: FtoF2(a1)
-1/2*b^3 + 9/2*b
sage: FtoF2(a1).minpoly()
x^2 - 2


```


See the thread at http://groups.google.com/group/sage-devel/browse_thread/thread/32fe12de12d5f6a5/c91753b5e65fe7b9#c91753b5e65fe7b9


---

Comment by cwitty created at 2008-02-21 03:24:23

Note that this approach does not give the splitting field.  It gives a field containing at least one root of each factor of the original polynomial, but that still might not be the splitting field.

Later in the thread mentioned above, I give a technique using internals of qqbar which I believe does give the splitting field (perhaps inefficiently).


---

Comment by davidloeffler created at 2009-07-20 19:58:56

Changing component from number theory to number fields.


---

Comment by davidloeffler created at 2009-07-20 19:58:56

Changing assignee from was to davidloeffler.


---

Comment by jdemeyer created at 2011-11-10 16:08:35

Add splitting_field() function


---

Attachment


---

Comment by roed created at 2012-09-17 05:20:52

Jeroen, what is the status of the patch here?


---

Comment by jdemeyer created at 2012-09-17 06:34:04

I totally forgot about this.  I might be good to revisit this.


---

Comment by jdemeyer created at 2012-09-17 06:51:38

I originally had plans for some speed-ups, but since the code works fine, I guess it can be reviewed.


---

Comment by jdemeyer created at 2012-09-17 06:51:38

Changing status from new to needs_review.


---

Comment by mmanes created at 2013-03-01 04:48:52

Changing status from needs_review to needs_work.


---

Comment by mmanes created at 2013-03-01 04:48:52

I ran all standard tests, and everything passed.

I was trying to test functionality, but I'm confused by the differences file.  All of the old examples seem to work, and none of the new ones work.

In the first example, I get:



```
sage: G = NumberField(x^3 - x - 1,'a').galois_closure('b').galois_group(); G

Galois group of Number Field in b with defining polynomial x^6 - 14*x^4
+ 20*x^3 + 49*x^2 - 140*x + 307
```



The expected output seems to have been changed _from_ this result to 



```
Number Field in b with defining polynomial x^6 - 6*x^4 + 9*x^2 + 23 
```



These fields are isomorphic, but I've tried the example on three machines, and all of them give the first thing as the output.

Similarly, the second example doesn't work:



```
sage: G.subgroup([ G(1), G([(1,2,3),(4,5,6)]), G([(1,3,2),(4,6,5)]) ]) 

Traceback (click to the left of this block for traceback)
...
TypeError: permutation [(1, 2, 3), (4, 5, 6)] not in Galois group of
Number Field in b with defining polynomial x^6 - 14*x^4 + 20*x^3 +
49*x^2 - 140*x + 307

```


But the original example (now deleted) does work:



```
sage: G.subgroup([ G(1), G([(1,5,2),(3,4,6)]), G([(1,2,5),(3,6,4)])])

Subgroup [(), (1,5,2)(3,4,6), (1,2,5)(3,6,4)] of Galois group of Number
Field in b with defining polynomial x^6 - 14*x^4 + 20*x^3 + 49*x^2 -
140*x + 307

```



---

Attachment

here is a patch to correct the failing doctest

let us see if the bot is happy

apply 2217_splitting_field.patch​ trac_2217_correction.patch​


---

Comment by chapoton created at 2013-08-21 09:38:33

ok, the bot is happy. Now the ticket needs review.


---

Comment by chapoton created at 2013-08-21 09:38:33

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2013-12-31 09:49:12

I am about to test and review this, which will also involve converting the patches to a git branch.  And rebasing, since the patches do not apply cleanly to the develop branch 
(6.1.beta2).


---

Comment by jdemeyer created at 2013-12-31 10:05:44

Hang on John, I was planning to do that and make some simplifications also.


---

Comment by cremona created at 2013-12-31 10:36:05

Replying to [comment:14 jdemeyer]:
> Hang on John, I was planning to do that and make some simplifications also.

I did not see this comment until after I had finished, so I may have been wasting my time.  I had to apply the changes manually since I could not get the patches to apply.  Shall I still upload my new branch?  I have a commit which includes both the patches and passes all tests -- but have not yet started the real review process, i.e. reading the code.


---

Comment by jdemeyer created at 2013-12-31 10:47:03

Replying to [comment:15 cremona]:
> Shal I still upload by new branch?
Of course you should. My point was mainly that I wanted to make some changes to my patch, so you should wait to review it.


---

Comment by cremona created at 2013-12-31 10:50:31

New commits:


---

Comment by cremona created at 2013-12-31 10:52:37

OK, so here is a branch which implements your two patches.  I will not do any more until asked, and hope that this will save you effort!  I also hope that this will not hide your genuine authorship of the new code.


---

Comment by jdemeyer created at 2014-01-02 11:15:30

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2014-01-02 23:27:46

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2014-01-02 23:41:06

New commits:


---

Comment by jdemeyer created at 2014-01-02 23:41:06

Changing status from needs_review to needs_work.


---

Comment by git created at 2014-01-02 23:51:44

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2014-01-02 23:52:30

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2014-01-03 09:20:27

I am looking at your new commits.  At first I assumed that your commits were based on mine uploaded earlier, but when pulling yours on top of mine failed I guessed the truth.  This is of course fine -- except that some people might now argue otherwise:  during the time when my commit was attached to this ticket, it is possible that other people pulled it and based further work, new tickets etc, all on my unreviewed commit.  That would have been stupid of them, but some of the comments on the recent sage-devel thread make it clear that git purists would never so this.  I won't tell anyone if you do not! ;)


---

Comment by jdemeyer created at 2014-01-03 09:36:53

Replying to [comment:26 cremona]:
> during the time when my commit was attached to this ticket, it is possible that other people pulled it and based further work, new tickets etc, all on my unreviewed commit.
I absolutely understand your point, but I think I indicated that this was work in progress so I felt it was safe to "rewrite history". Now that it's `needs_review`, I will no longer rewrite history.

Concerning authorship: I did indeed reset the author name back to myself (`git commit --amend --author Demeyer`), and that's already rewriting history.


---

Comment by cremona created at 2014-01-03 09:55:18

Understood.  I am happy (and quite impressed!) with the new code and am just testing, using the verbose option so I can see what is happening.


---

Comment by git created at 2014-01-03 10:43:29

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2014-01-03 10:56:32

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by cremona created at 2014-01-03 10:58:25

Still needs-review or will you be making more commits?!


---

Comment by cremona created at 2014-01-03 11:16:43

Code looks very good, and I am happy with the results of testing.  I have looked at the commits on branch u/jdemeyer/ticket/2217 up to commit c50eb3e...


---

Comment by cremona created at 2014-01-03 11:16:43

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2014-01-03 11:33:34

Thanks, I didn't expect such a quick review.

Am I allowed to add more examples/doctests?


---

Comment by cremona created at 2014-01-03 11:59:52

Replying to [comment:33 jdemeyer]:
> Thanks, I didn't expect such a quick review.
> 
> Am I allowed to add more examples/doctests?

Of course!  I think there are already a lot of examples, which I liked.  If you are going to make some more changes I would be happy to look at them, so I'll now mark the ticket as needs work, and when you are ready put it back to needs review.  While you are at it, the description of the class containing a pair (polynomial, degree multiple) is slightly confusing since it refers to other polynomials in the class, whereas you actually deal with lists of instances of these.


I am currently working on another branch so the next review will not be so quick!


---

Comment by cremona created at 2014-01-03 11:59:52

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2014-01-03 12:28:07

Replying to [comment:34 cremona]:
> I am currently working on another branch so the next review will not be so quick!
In that case, perhaps I prefer to leave this ticket and continue on a new ticket. Sorry for the mess.


---

Comment by jdemeyer created at 2014-01-03 12:28:07

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-01-05 02:56:53

Resolution: fixed
