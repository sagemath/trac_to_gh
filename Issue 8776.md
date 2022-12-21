# Issue 8776: notebook: sage notebook undo doesn't really work, due to not enough (=no) automatic snapshots, or other bugs

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-04-27 04:38:16

Assignee: jason, was

CC:  kcrisman schymans cremona

I think Cremona's email says it best:

```
For the first time, I just tried using the "Undo" function on a
worksheet since I had messed something up.  But all the revisions I
was offered, even those from a day ago, look the same as the current
version!

This is 4.3.5 running on a 64-bit ubuntu server.

I have found it very useful that my students can work on something in
a worksheet owned by them, and then share it with me, so that when
they come to see me to talk about it we can go through it in detail on
my own computer at our meeting.  (This is really a fantastic feature).
 But just now I was having a look at a student's worksheet the day
before our meeting, and made some changed to it which I later
regretted and tried to revert.  Without success....

Any suggestions welcome!

John Cremona
```



---

Comment by timdumol created at 2010-09-10 03:54:50

Depends on #9428. Fixes the given issue.


---

Attachment

Depends on #9428. Rebase on new #9428. Replaces previous version.


---

Comment by kcrisman created at 2011-10-11 15:56:51

Will it be relatively easy to remove the dependency on #9428?  I would imagine so.  Also, this has been reported upstream at [this link](http://code.google.com/p/sagenb/issues/detail?id=59).


---

Comment by schymans created at 2011-10-12 07:24:05

Maybe it was a stupid thing to try, but the patch does not apply to sage 4.7.1. Here is the output I get:


```
sage: hg_sage.apply("/home/uname/Downloads/sage/trac_8776-sagenb-undo.2.patch")
cd "/home/uname/Programs/sage-test/devel/sage" && hg status
cd "/home/uname/Programs/sage-test/devel/sage" && hg status
cd "/home/uname/Programs/sage-test/devel/sage" && hg import   "/home/uname/Downloads/sage/trac_8776-sagenb-undo.2.patch"
applying /home/uname/Downloads/sage/trac_8776-sagenb-undo.2.patch
internal patcher failed
please report details to http://mercurial.selenic.com/bts/
or mercurial`@`selenic.com
/home/uname/Programs/sage-test/local/bin/patch: **** Only garbage was found in the patch input.
abort: patch command failed: exited with status 512
```


Is this a problem with mercurial as suggested in the output, or with the patch under the current sage?

Cheers
Stan


---

Comment by kcrisman created at 2011-10-12 12:31:38

?  What is `/home/uname/Downloads`?    

Oh, I see what happened.  You applied the file you found at [http://trac.sagemath.org/sage_trac/attachment/ticket/8776/trac_8776-sagenb-undo.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8776/trac_8776-sagenb-undo.2.patch), but it turns out that is really an HTML file.  What you want is the *raw* patch, which is at [http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8776/trac_8776-sagenb-undo.2.patch](http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8776/trac_8776-sagenb-undo.2.patch).  That is the little "download" graphic next to the name of the patch in the list of attachments to this ticket.  You might as well try this one, though I doubt it will apply either :)  But it's worth trying!


---

Comment by schymans created at 2011-10-13 08:14:59

Thanks, Jason!

I did as you said and the result was as predicted: the patch failed to apply, but maybe for the wrong reasons again. Does the following error message help?


```
sage: hg_sage.apply("/home/uname/Downloads/sage/trac_8776-sagenb-undo.2.patch")
applying /home/uname/Downloads/sage/trac_8776-sagenb-undo.2.patch
unable to find 'sagenb/notebook/worksheet.py' for patching
3 out of 3 hunks FAILED -- saving rejects to file sagenb/notebook/worksheet.py.rej
abort: patch failed to apply
cd "/home/uname/Programs/sage-test/devel/sage" && hg status
cd "/home/uname/Programs/sage-test/devel/sage" && hg status
cd "/home/uname/Programs/sage-test/devel/sage" && hg import   "/home/uname/Downloads/sage/trac_8776-sagenb-undo.2.patch"

```

/home/uname/Programs/sage-test is my sage directory, in which I created a clone called sage-test. I tried to apply the patch to the clone, which should be in /home/uname/Programs/sage-test/devel/sage-test/..., but there is indeed no worksheet.py.

I found worksheet.py in ~/Programs/sage-test/devel/sagenb/sagenb/notebook/ (note the nested sagenb/sagenb/), whereas the directory ~/Programs/sage-test/devel/sage-test/sagenb/notebook/ in my sandbox only contains worksheet.py.rej. There is also no ~/Programs/sage-test/devel/sage-test/sagenb/sagenb/, so the clone does not seem to have the same directory structure as the original. Anyway, even if I try to apply the patch to the main branch, I get the same error message, probably because it is looking in devel/sagenb/notebook/ and not in devel/sagenb/sagenb/notebook/. I'm confused.


---

Comment by kcrisman created at 2011-10-13 13:36:15

> Thanks, Jason!

This is kcrisman :)

> I did as you said and the result was as predicted: the patch failed to apply, but maybe for the wrong reasons again. Does the following error message help?

Yes, because you didn't follow my instructions exactly ;-) though those were on the sage-notebook list, not this ticket.

 * Log in to a command line Sage.
 * type *exactly* the following:

```
hg_sagenb.import_patch("http://trac.sagemath.org/sage_trac/raw-attachment/ticket/8776/trac_8776-sagenb-undo.2.patch")
```

   and see what happens.  

Note the "hg_sagenb" instead of "hg_sage".  We moved a lot of stuff outside of the devel/sage/ directory into the devel/sagenb directory a while ago, so this is necessary.  Hopefully this will at least give a more informative message.  Thanks for trying it out - you're on your way to becoming a Sage developer!


---

Comment by schymans created at 2011-10-13 14:15:28

I still don't understand why downloading the raw patch and then patching did not work, whereas using the link did, but thanks for the explicit tip, kcrisman! Here is the output:


```
applying /home/uname/.sage/temp/cname/14067/tmp_0.patch
patching file sagenb/notebook/worksheet.py
Hunk #3 succeeded at 1986 with fuzz 2 (offset -8 lines).

```

Does this imply that the patch is applied now? If it does, then it also implies that the patch does not solve the issue of identical snapshots, as they are still all identical if I create a few while making changes to a worksheet.


---

Comment by kcrisman created at 2011-10-13 14:30:23

Yes, the patch should be applied.  However, you may still have to build Sage again.  Do the following (this is also in the devel instructions).

 * Quit Sage.
 * Instead of calling Sage however you usually do (e.g., 
{{{ 
/path/to/sage
}}}
   do 

```
/path/to/sage -br
```

 * Now open the notebook from within Sage again (e.g, with 

```
sage: notebook()
```

   and see what happens.  I give no guarantees!  But at least it's worth trying.


---

Comment by schymans created at 2011-10-13 14:59:57

I already rebuilt it using ./sage -b (as suggested in the devel instructions), but I tried again using ./sage -br. No change, all snapshots are still identical. 

Is it normal that sage-0.0.0-py2.6.egg-info is re-built every time, or does it imply that the patch was not fully applied and lingers somewhere in the queue? Is there a way to check from within sage that the new code is actually used? E.g. by typing "sagenb-undo??" or something along these lines?


---

Comment by kcrisman created at 2011-10-13 15:19:02

Changing status from new to needs_review.


---

Comment by kcrisman created at 2011-10-13 15:19:02

Replying to [comment:10 schymans]:
> I already rebuilt it using ./sage -b (as suggested in the devel instructions), but I tried again using ./sage -br. No change, all snapshots are still identical. 

Okay, good to know.  I assume that you are referring to snapshots "created" _after_ the time you applied the patch; obviously, previous snapshots wouldn't magically change!

> Is it normal that sage-0.0.0-py2.6.egg-info is re-built every time, or does it imply that the patch was not fully applied and lingers somewhere in the queue? Is there a way to check from within sage that the new code is actually used? E.g. by typing "sagenb-undo??" or something along these lines?

No, this is actually what is supposed to happen.   I wouldn't worry about whether the code is used; that's the job of those writing patches :)


---

Comment by kcrisman created at 2011-10-13 15:19:19

Changing status from needs_review to needs_work.


---

Comment by schymans created at 2011-10-13 20:44:52

To be precise, whenever I create a new snapshot, before or after applying the patch, all snapshots indeed magically change and become identical to the most recent one.


---

Comment by schymans created at 2012-05-24 13:26:10

Sage 5.0 is out and magically the milestone for this ticket has changed from 5.0 to 5.1. This bug is really annoying to me and in fact the button "Undo" and the "Revisions" are grossly misleading, as they lure the user into a false sense of security. Does anyone have an idea where to look for the problem and how it could be solved?


---

Comment by kcrisman created at 2014-09-18 16:33:17

I have reported this at https://github.com/sagemath/sagenb/issues/236 - eventually I should go sift through the Google code bug reports too.  But this is one of the very few things I think really makes the notebook unusable for certain people - it's fine for most of my and other more casual needs, but without revision control at the very least we can have revisions that actually work!

That said, I don't know that the current code here will have anything useful with the flask notebook - but who knows?


---

Comment by kcrisman created at 2014-09-18 18:03:27

Big news - the problem is not that the snapshots aren't there, but rather that the snapshot actually unpacked must always be the last one.  All your revisions are there!  We just have to figure out why the correct snapshots aren't being shown.  And I think I know why...


---

Comment by kcrisman created at 2014-12-10 18:20:25

This has now been merged in sagenb inside Sage, 0.11.0 I believe.


---

Comment by kcrisman created at 2014-12-10 18:20:25

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2014-12-11 18:35:56

Resolution: fixed
