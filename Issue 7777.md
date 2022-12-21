# Issue 7777: Implement SymmetricFunctions(QQ).inject_shorthands()

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2009-12-27 22:29:20

Assignee: sage-combinat

CC:  sage-combinat jbandlow

Keywords: symmetric functions, inject

The title says it all. Depends on #7776


---

Comment by nthiery created at 2009-12-27 22:36:24

Beware: patch written and tested on Sage 4.2, not 4.3.


---

Comment by nthiery created at 2009-12-27 22:36:24

Changing status from new to needs_review.


---

Comment by jbandlow created at 2010-01-07 15:11:06

Although I haven't tested it yet, I'm in principle very happy with the 'green' part of the patch.  Could you say a little about the 'red' part?  What's being deleted from the 'introspect' files and why?


---

Attachment


---

Comment by jbandlow created at 2010-01-09 02:42:34

Changing status from needs_review to positive_review.


---

Comment by jbandlow created at 2010-01-09 02:42:34

Looks good to me (on top of 7776). Thanks for this, Nicolas!


---

Comment by rlm created at 2010-01-13 09:53:25

Changing status from positive_review to needs_work.


---

Comment by rlm created at 2010-01-13 09:53:25


```
The following tests failed:

        sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed
```



---

Comment by nthiery created at 2010-01-13 11:57:30

Replying to [comment:4 rlm]:
> {{{
> The following tests failed:
> 
>         sage -t -long devel/sage-main/sage/combinat/sf/sf.py # 10 doctests failed
> }}}

Thanks for the report. I did not manage yet to reproduce yet (I am downloading 4.3.1.alpha).
Could you send me a copy of the log? Was 7776 applied?

Cheers


---

Comment by rlm created at 2010-01-13 12:01:01

I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...


---

Comment by rlm created at 2010-01-13 12:01:01

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-01-13 12:01:14

Changing status from needs_review to positive_review.


---

Comment by nthiery created at 2010-01-13 12:16:42

Replying to [comment:6 rlm]:
> I had gotten too sleepy! Sorry, I didn't notice the dependency (it is 4am here now)...

:-)

We really should be using a ticket dependency plugin like:
http://trac-hacks.org/wiki/MasterTicketsPlugin.

Have a good night!


---

Comment by rlm created at 2010-01-14 01:45:05

Resolution: fixed
