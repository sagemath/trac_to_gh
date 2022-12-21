# Issue 9948: Add major index (generating polynomial) for the category of finite permutation groups

Issue created by migration from Trac.

Original creator: nborie

Original creation time: 2010-09-19 16:49:15

Assignee: nborie

CC:  sage-combinat nthiery

Keywords: major, index, generating, polynomial, permutation

In the spirit of factorization of the code, add a method major_index for parents/elements inheriting from FinitePrmutationGoups()


```
sage: DihedralGroup(5).major_index()
q^10 + q^9 + q^8 + q^7 + q^6 + q^4 + q^3 + q^2 + q + 1
sage: PermutationGroup([This is the Trac macro ** that was inherited from the migration called with arguments (1,2,3,4,5))](https://trac.sagemath.org/wiki/WikiMacros#-macro)).major_index()
q^4 + q^3 + q^2 + q + 1
sage: SymmetricGroup(3).major_index()
q^3 + 2*q^2 + 2*q + 1
sage: TransitiveGroup(5,3).major_index()
q^10 + q^9 + 2*q^8 + 2*q^7 + 3*q^6 + 2*q^5 + 3*q^4 + 2*q^3 + 2*q^2 + q + 1
```



---

Comment by nborie created at 2010-09-19 17:08:06

Changing status from new to needs_review.


---

Attachment


---

Attachment

I've added a review patch which fixes a few minor things.  Other than that, it looks good to me.  Do you want to fold the patches together, put the new one up, and I can give it positive review?


---

Comment by nborie created at 2010-11-28 15:52:46

Yes, I definitely agree with yours corrections. But before finalizing this ticket, we need some informations. Nicolas told me that it is not really reasonable to implement this feature in this category. We don't really know if major index is defined for any Finite Permutation Group. Let's discuss this on sage-combinat-devel.

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/38a0e71e61ca6231

Thank you very much Mike for your patch, I also should have open this discussion earlier. Sorry for that...


---

Comment by nborie created at 2010-11-28 15:52:46

Changing status from needs_review to needs_info.


---

Comment by nborie created at 2011-01-19 09:49:12

Changing status from needs_info to needs_review.


---

Comment by nborie created at 2011-01-19 09:49:12

After discussions, I realized that it is reasonable to define major_index only for the symmetric group. So I moved the method in the proper place. I also integrated all remarks and code corrections from the patch of Mike.

For Buildbot / reviewer / ... :

apply trac_9949_major_index_final-nb.patch

It is now ready for review.


---

Comment by jbandlow created at 2011-02-02 19:39:00

Hi Nicolas,

If this only applies to symmetric groups, shouldn't it just return


```
sage.combinat.q_analogues.q_factorial(n)
```

?

This would be much more efficient than enumerating over the group.


---

Comment by jbandlow created at 2011-02-02 19:39:00

Changing status from needs_review to needs_info.


---

Comment by nborie created at 2011-02-02 20:09:00

Hy Jason

You are definitely right! I didn't know this module about q_analogues. I am going to change it and just make major_cycle point to the right q_analogue. As q_analogues is not imported by default, this ticket will just consist in building a shortcut...

Thanks for having regarded this!


---

Attachment


---

Comment by nborie created at 2011-02-16 17:57:11

Changing status from needs_info to needs_review.


---

Comment by nborie created at 2011-02-16 17:57:11

I update the patch after your last comment Jason. At the end, this method is just a shortcut pointing to the q-analogue of factorial n. As q_analogues are not imported by default and calling SymmetricGroup(n).major_index() seems natural, I think it is good like this.


---

Comment by jbandlow created at 2011-03-14 18:50:46

This looks good.  Thanks, Nicolas.


---

Comment by jbandlow created at 2011-03-14 18:50:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-07 13:50:47

Please change the commit message of the patches to something meaningful.  Make sure the ticket number appears on the first line of the commit message.


---

Comment by jdemeyer created at 2011-04-07 13:50:47

Changing status from positive_review to needs_work.


---

Comment by nthiery created at 2011-04-07 13:59:35

Changing status from needs_work to positive_review.


---

Comment by nthiery created at 2011-04-07 14:00:01

Replying to [comment:10 jdemeyer]:
> Please change the commit message of the patches to something meaningful.  Make sure the ticket number appears on the first line of the commit message.

Oops, I should have caught this. Fixed!


---

Comment by jdemeyer created at 2011-04-07 14:08:31

Changing status from positive_review to needs_info.


---

Comment by jdemeyer created at 2011-04-07 14:08:31

May I assume that the description is wrong and that *three* patches need to be applied?


---

Comment by nthiery created at 2011-04-07 14:10:03

Really final version, with ticket number


---

Attachment


---

Comment by nthiery created at 2011-04-07 14:18:23

Changing status from needs_info to needs_review.


---

Comment by nthiery created at 2011-04-07 14:18:23

Replying to [comment:14 jdemeyer]:
> May I assume that the description is wrong and that *three* patches need to be applied?

Sorry, I uploaded the wrong file from the sage-combinat queue, which probably caused the confusion. I confirm that only the advertised patch shall be applied.

Thanks!


---

Comment by nthiery created at 2011-04-07 14:18:30

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-04-07 14:48:16

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2011-04-07 14:48:16

Replying to [comment:16 nthiery]:
> I confirm that only the advertised patch shall be applied.

This statement is a non-trivial change to the ticket and needs to be reviewed (since your patch is only a subset of the previous patches).


---

Comment by jdemeyer created at 2011-04-07 14:48:23

Changing status from needs_work to needs_review.


---

Comment by nthiery created at 2011-04-07 15:00:22

Replying to [comment:18 jdemeyer]:
> Replying to [comment:16 nthiery]:
> > I confirm that only the advertised patch shall be applied.
> 
> This statement is a non-trivial change to the ticket and needs to be reviewed (since your patch is only a subset of the previous patches).

Sorry if there is any confusion, but the reduction to a subset dates back from 7 weeks ago, and was already given a positive review by Jason Bandlow. I only changed the patch header from trac_9949_major_index_final-nb.patch. So I think it should be positive review.

Do you mind setting it back if we are now on the same line?


---

Comment by jbandlow created at 2011-04-07 15:07:54

Changing status from needs_review to positive_review.


---

Comment by jbandlow created at 2011-04-07 15:07:54

I confirm that Nicolas Thiery's changes were only to the header of the patch previously given a positive review by me.  I am resetting the status to positive review.  My apologies for missing the incomplete commit message in my first review.


---

Comment by jbandlow created at 2011-04-07 15:16:16

To be sure I am clear, the ticket description is correct:

Apply only trac_9949_major_index_really_final-nb.patch


---

Comment by jdemeyer created at 2011-04-07 19:54:40

I understand everything now, but bear in mind that it is very important to write in the *ticket description* which patches have to be applied if it's not obvious.  If it weren't for the missing commit message, I would have merged all three patches instead of only the last one (and we would never have known that we did something wrong).


---

Comment by nborie created at 2011-04-08 06:26:37

Sorry for all of that,

It is a 7 weeks old patch and despite I read sage-devel (and advises in sage-devel like the use of hg qrefresh -e and other patch submitting procedures), I didn't have the reflex of checking all my submitted patch to verify they are conforms. It is not the first time I am making this mistake. Sorry, I will try to be very very conscientious the next time.

And I am on the way checking all I already put in trac the last months...

Thanks for your help to all of you.


---

Comment by jdemeyer created at 2011-04-08 12:59:02

Resolution: fixed
