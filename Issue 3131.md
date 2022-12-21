# Issue 3131: README.txt: update recommendations for dev work with binaries

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-08 12:47:56

Assignee: tba


```
Aside from all the other issues: You should *always* rebuild the Sage
library of a binary build before running clone. Otherwise each clone
requires a complete rebuild. Aside from that it is *highly*
recommended to build from source if you are developing since mixing
and matching different compiler releases [even on OSX] can lead to odd
results, i.e. Heisenbugs and segfaults.
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-05-08 12:53:45

Changing assignee from tba to mabshoff.


---

Comment by mabshoff created at 2008-05-08 12:53:45

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-08 12:53:45

Maybe this should go into "Section 7.1 of the Sage Programming Guide" instead.

Cheers,

Michael


---

Comment by aapitzsch created at 2014-08-13 22:02:15

This became invalid when we switched to git.


---

Comment by aapitzsch created at 2014-08-13 22:02:15

Changing status from new to needs_review.


---

Comment by kcrisman created at 2014-08-14 13:45:20

Hmm, good point!  I just saw this too.  Are there any instructions we need to give people about how to develop with binaries?  (Such as, you really need to build from scratch.)  Maybe this is already in the much-underused installation guide...


---

Comment by kcrisman created at 2014-08-14 13:45:20

Changing status from needs_review to needs_info.


---

Comment by jdemeyer created at 2014-08-14 13:48:11

Replying to [comment:7 kcrisman]:
> Are there any instructions we need to give people about how to develop with binaries?  (Such as, you really need to build from scratch.)
Exactly: "don't do it" is the best advice you can give.


---

Comment by kcrisman created at 2014-08-15 05:05:47

Changing status from needs_info to needs_work.


---

Comment by kcrisman created at 2014-08-15 05:05:47

Then what I would say is to make this really loud somewhere correct.  The problem is that some stuff in the install guide should really be in the developer guide, as there isn't much about `sage -b` anywhere in there as far as I can tell (maybe in the git sections?).


---

Comment by kcrisman created at 2014-11-20 15:28:43

Changing keywords from "" to "beginner".


---

Comment by mmezzarobba created at 2015-01-28 15:34:46

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2015-01-28 17:04:29

Why would this be wontfix?  Have we already said very loudly "don't do it"?


---

Comment by kcrisman created at 2015-01-28 17:04:29

Changing status from positive_review to needs_info.


---

Comment by mmezzarobba created at 2015-01-28 18:07:31

Changing status from needs_info to needs_work.


---

Comment by mmezzarobba created at 2015-01-28 18:07:31

Replying to [comment:12 kcrisman]:
> Why would this be wontfix?  Have we already said very loudly "don't do it"?

Oops, sorry, I had the same reaction as you about this becoming meaningless with the switch to git, and I did not notice the recent discussion.


---

Comment by jdemeyer created at 2015-01-28 19:36:35

Replying to [comment:12 kcrisman]:
> Have we already said very loudly "don't do it"?
Is there a reason why people shouldn't do it? Since when did we stop supporting developing with binaries?


---

Comment by kcrisman created at 2015-01-28 19:39:52

*You* said it!  comment:8
> Exactly: "don't do it" is the best advice you can give.
If not, then we should say just what prereqs and problems might be necessary/arise.


---

Comment by jdemeyer created at 2015-01-28 19:48:05

Funny :-)

Maybe there is a good reason that I currently cannot think of.


---

Comment by kcrisman created at 2015-01-28 19:57:01

Well, the obvious reason is that people keep trying to do it and then failing because they don't have gcc or some other prereq, or because of some hard-coded paths that screw things up from the buildbot.  However, maybe saying that people need to be extra-special careful in that event is enough...?


---

Comment by kcrisman created at 2016-02-25 03:31:38

So, where do we say "don't do this", if at all?


---

Comment by btdhall created at 2016-06-25 23:23:57

On the index of the Developer's Guide (http://doc.sagemath.org/html/en/developer/index.html) it mentions needing the source code which implies that you can't develop from only a binary.

I think that should be sufficient but maybe we need to **direct users in README.md to "read the Developer's Guide"** if they would like to contribute. This is already the advice given in the "Development" link on the main website (http://www.sagemath.org/development.html) as well as the contributing FAQ (http://doc.sagemath.org/html/en/faq/faq-contribute.html) where it also says to "...grab a copy of the Sage source...".

So, if anything, we can **change the wording in the Developer's Guide to be less suggestive** since that's where all roads to getting started in development should lead.


---

Comment by btdhall created at 2016-06-26 00:14:46

Changing priority from major to minor.


---

Comment by btdhall created at 2016-06-26 00:14:46

Changing assignee from mabshoff to btdhall.


---

Comment by btdhall created at 2016-07-02 15:48:47

Changing status from needs_work to needs_review.


---

Comment by btdhall created at 2016-07-02 15:48:47

New commits:


---

Comment by paulmasson created at 2016-07-07 01:59:13

`@`btdhall while you're touching this file, there are two occurrences of `sagemath.org/doc/` and two occurrences of `www.sagemath.org/doc/` that should all be changed to `doc.sagemath.org/html/en/`.

I've been trying to help Harald Schilly to get Google to stop indexing the old documentation location and it doesn't help if it's there on the default [GitHub](GitHub) page.


---

Comment by git created at 2016-07-07 03:04:38

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by paulmasson created at 2016-07-07 03:18:28

Looks good. Thanks!


---

Comment by paulmasson created at 2016-07-07 03:18:28

Changing status from needs_review to positive_review.


---

Comment by btdhall created at 2016-07-07 03:42:53

Replying to [comment:26 paulmasson]:
> Looks good. Thanks!
No problem.

While we're on the topic, the errata ([http://wiki.sagemath.org/errata](http://wiki.sagemath.org/errata)) links to an empty wiki page but I couldn't find the proper location. Let me know if you have a suggestion for fixing it.


---

Comment by vbraun created at 2016-07-08 07:09:33

Resolution: fixed
