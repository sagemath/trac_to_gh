# Issue 5178: [with patch; needs review] change LLL_gram to work with Gram matrices with not-necessarily integer entries

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-04 18:23:08

Assignee: was

CC:  boothby craigcitro cremona kohel mabshoff malb ncalexan slelievre tornaria was

This patch changes LLL_gram to work with Gram matrices with not-necessarily integer entries.  Also it fixes several "non-optimal" coding issues both in the old implementation and the doctests.  For example, instead of computing U.det() to determine if the unimodular A has det -1 or 1, we just compute A.change_ring(GF(3)).det(), which is much faster. 

Changing LLL_gram to work for nonintegral gram matrices is critical for applications to computing class groups for the course I'm teaching right now.


---

Attachment


---

Comment by was created at 2009-02-05 05:47:57

Gonzalo Tornaria sent this review in email to me:

```
Looks good to me.

However, it seems pari is hanging when using lllgram() on some
matrices with rational or integer entries; maybe indefinite or
semidefinite matrices are the issue.
Moreover, sage hangs badly on this...

E.g.

sage: pari("[1,1;1,1/2]").qflllgram()

(it also hangs when running equivalent command from gp, Ctrl-C stops
gp but not sage).
[equivalent command = qflllgram([1,1,1,1/2])

However, using 0.5 instead of 1/2 works ok.

Seems a bug in pari, but it was not exposed in sage's LLL_gram() before.

Gonzalo
```


He does point out that bad things can happen, but that the bugs are in PARI, not the new code attached to this patch.


---

Comment by boothby created at 2009-02-06 06:28:04

I reported the bug upstream.  Is Gonzalo's +1 good enough?  I'm not really comfortable with LLL enough to sign off on this.


---

Comment by boothby created at 2009-02-06 17:38:33

Email from Bill Allombert in response to the bug:


```
Hello,
This problem does not occurs with PARI 2.4.3.
This seems to be another instance of bug #505 which was fixed in
PARI 2.4.1 as

 1- qflll / qflllgram (t_MAT with t_FRAC entries) would not reduce to
    the integer case (--> insufficient precision, SEGV) [#505]

The fix should probably be backported.

Thanks for your bug report,
Bill
```



---

Comment by mabshoff created at 2009-02-06 20:41:42

So, it this a positive review then? 

Nick did ping me last night about updating to pari 2.4.3svn sources and it seems that we don't really have a choice any more. But this issue should be raised on sage-nt I guess.

Cheers,

Michael


---

Comment by ncalexan created at 2009-06-04 21:43:20

Can we get some movement on this?  I don't think an updated pari is happening anytime soon but it would be nice to close this.


---

Comment by craigcitro created at 2009-06-20 08:49:03

This looks good. The only objection I have is that the documentation isn't correctly formatted for sphinx -- in particular, the various sections of the docstring (like `EXAMPLES`) should have a double colon, and there should be more blank lines to get things to format correctly. Also, one or two more examples with noninteger entries in the docstring wouldn't hurt, if you're already there. Maybe something from a class group computation, even if it requires `# long`?


---

Comment by boothby created at 2011-06-23 23:47:46

Just got an email from Bill Allombert regarding this bug:


```
Hello,
PARI 2.5.0-stable was released with a fix for this problem,
closing this report.

Thanks for using our bug tracking system,
Cheers,
Bill.
```



---

Comment by boothby created at 2011-06-23 23:48:23

Resolution: fixed


---

Comment by boothby created at 2011-06-24 03:40:27

oops, didn't realize changing the "upstream" field would close the ticket


---

Comment by boothby created at 2011-06-24 03:40:27

Changing status from closed to new.


---

Comment by boothby created at 2011-06-24 03:40:27

Resolution changed from fixed to 


---

Comment by boothby created at 2011-06-24 03:40:42

Changing status from new to needs_review.


---

Comment by boothby created at 2011-06-24 03:40:49

Changing status from needs_review to needs_work.


---

Comment by slelievre created at 2020-09-18 09:58:05

Changing status from needs_work to needs_review.


---

Comment by slelievre created at 2020-09-18 09:58:05

Changing keywords from "" to "LLL, Gram".


---

Comment by slelievre created at 2020-09-18 09:58:05

Turned the 2009 patch into a branch based on Sage 9.2.beta12.

Please review.
----
New commits:


---

Comment by malb created at 2020-09-18 10:18:04

Looks good to me


---

Comment by malb created at 2020-09-18 10:18:04

Changing status from needs_review to positive_review.


---

Comment by slelievre created at 2020-09-18 10:21:07

Replying to [comment:6 craigcitro]:
> This looks good. The only objection I have is that the documentation
> isn't correctly formatted for sphinx -- in particular, the various
> sections of the docstring (like `EXAMPLES`) should have a double colon,
> and there should be more blank lines to get things to format correctly.

Addressed in the branch.

> Also, one or two more examples with noninteger entries in the
> docstring wouldn't hurt, if you're already there. Maybe something
> from a class group computation, even if it requires `# long`?

I agree. William, would you have a few examples from your course?

Since Martin already gave positive review (thanks!),
adding examples could be done in a follow-up ticket.


---

Comment by slelievre created at 2020-09-18 10:36:03

Possible follow-up improvements:

- Add optional parameter `force_orientation_preserving=True`.
  Setting it to `False` when calling the method would skip
  the last part (that checks whether the determinant is 1 or -1
  and changes the sign of the last column in case it is -1)
  and save some time.

- Maybe PARI has an option to force returning a determinant 1
  transformation matrix? If so, use it.

- Add cross-references in the documentation to/from any similar
  methods, e.g. provided by fplll.


---

Comment by vbraun created at 2020-09-23 21:27:57

Resolution: fixed


---

Comment by slelievre created at 2020-09-28 10:07:31

Follow-up at #30678.
