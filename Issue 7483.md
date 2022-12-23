# Issue 7483: notebook: weird pointless line

Issue created by migration from https://trac.sagemath.org/ticket/7483

Original creator: was

Original creation time: 2009-11-17 22:28:15

Assignee: boothby

In worksheet.py (at the end of `start_next_comp(self)`) in sagenb we have these lines:

```
        self.__comp_is_running = True
        'exec _support_.preparse(base64.b64decode("%s"))'%base64.b64encode(input)
        self.sage().execute(input, os.path.abspath(self.data_directory()))
```


That 'exec ' line in the middle is just sitting there making a string that is just discareded!?!?


---

Comment by was created at 2009-11-17 22:33:15

I think I meant

```
input = 'exec _support_.preparse(base64.b64decode("%s"))'%base64.b64encode(input)
```

and to get rid of preparsing input at all done by the server.  In fact, I know for a fact I implemented things that way so that this wouldn't be broken:

```
implicit_multiplication(True)
///
Traceback (most recent call last):
...
NotImplementedError: Implicit multiplication not implemented for the notebook.
```


But now it seems to be broken again. 

I can only conclude that a serious mismerge or mangling has occurred to the code I originally wrote, since I definitely had the above working in an earlier version of sagenb.  

Hence, this ticket.


---

Comment by was created at 2009-11-17 23:53:25

Changing type from defect to enhancement.


---

Comment by was created at 2009-11-18 00:35:05

apply to the sagenb spkg


---

Attachment

apply to the core sage library


---

Comment by was created at 2009-11-18 00:35:52

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2009-11-18 00:38:47

So the attached patch moves all the preparsing from the notebook server to the worksheet process.   I had thought I had made this change long ago, but I definitely hadn't.  It's *extremely* important from a security/robustness/speed/flexibility point of view.  Why?  Because it means the possibly time consuming and definitely _dangerous_ preparsing work gets pushed off to the worksheet processes, which will often be running on some remote virtual machines.  That's what we want!

This patch also makes it so the following are now fully supported in the notebook.  Note that they both used to not work at all:

   * implicit_multiplication -- turning on and off implicit multiplication

   * preparser -- turning on and off the preparser


---

Comment by was created at 2009-11-18 03:38:38

I've put a new sagenb spkg with just this patch (and the one from 7483) here:

   http://wstein.org/home/wstein/patches/sagenb/sagenb-0.4.3.p1.spkg


---

Comment by mpatel created at 2009-11-18 06:36:44

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2009-11-18 06:36:44

The Selenium test results are unchanged in FF3.5.5 on Linux.  

`make ptest` on sage.math passes.


---

Comment by mpatel created at 2009-11-18 07:25:50

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2009-11-18 07:25:50

It seems that `load` and `save` are now broken in the notebook.

Were `attach` and `detach` already broken in the notebook?


---

Comment by was created at 2009-11-22 00:04:15

> It seems that load and save are now broken in the notebook.
> Were attach and detach already broken in the notebook?

No, this broke them.  I'll fix the problem now.


---

Comment by was created at 2009-11-22 00:10:56

Clarification: load and save still work on .sage files, but don't work on .py. This is related to #4474.  But I'll fix it here now, hopefully.


---

Comment by was created at 2009-11-22 08:21:21

OK, I went a bit crazy and spent 8 hours completely rewriting and unifying and refactoring all the load/save/attach code.  This is at #7514.  With that, the above mentioned issued is gone.


---

Comment by was created at 2009-11-22 08:21:21

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2009-12-10 03:50:44

Positive review, once #7514 passes.

Should we also move "docbrowser" generation to a worksheet process?


---

Comment by was created at 2009-12-10 18:28:56

> Should we also move "docbrowser" generation to a worksheet process? 

Definitely!  The more that is done by worksheet processes, the better -- for scalability, security, etc.  Every spec of work done by the server is a potential speed and security problem.  The more that can be offloaded to worksheets, the better.


---

Comment by mpatel created at 2010-01-01 07:29:53

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-03 22:31:45

I've merged the sagelib patch in 4.3.1.alpha0


---

Comment by was created at 2010-01-04 06:34:13

I've merged this into sagenb-0.4.8.


---

Comment by was created at 2010-01-04 06:34:13

Resolution: fixed
