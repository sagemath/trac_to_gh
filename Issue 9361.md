# Issue 9361: Maxima timeout when creating tab completion list on Mac PPC

Issue created by migration from https://trac.sagemath.org/ticket/9361

Original creator: kcrisman

Original creation time: 2010-06-28 18:24:34

Assignee: tbd

CC:  georgsweber kcrisman

This has been reported on more than one Mac running OSX 10.4 Tiger.

```
> 
> ----------------------------------------------------------------------
> The following tests failed:
> 
>         sage -t  -long
> "rro/sage-4.4.4.alpha1/devel/sage/sage/interfaces/maxima.py" #
> Killed/crashed
```

This is due to the commands in this file which create the tab completion list for use with Sage's Maxima; for some reason even when done 'by hand' they often time out, and since they happen a few different times in this file it will nearly always time out (even with huge `SAGE_TIMEOUT` set)


---

Comment by kcrisman created at 2010-06-29 13:27:51

See also [this](http://groups.google.com/group/sage-devel/browse_thread/thread/12bfb14d71db9f9e) thread on sage-devel for some indication of how to track it down, perhaps via #4180.


---

Comment by kcrisman created at 2011-01-14 18:27:44

Update: on [this release discussion](http://groups.google.com/group/sage-release/browse_thread/thread/188794c32e110ae2/bc276a98c20d714a) it seems that Macintel does not have this issue anymore:

```

> Georg, I know your processor is faster than mine, but how long did the 
> Maxima interface test take? 


Cough, cough, 
not so really long, snippet from "testlong.log": 
sage -t  -long -force_lib "devel/sage/sage/interfaces/maxima.py" 
         [39.7 s] 
There seems to be some strange thing ongoing ... 
```

But it still times out at whatever one chooses on PPC.


---

Comment by jdemeyer created at 2012-01-13 15:01:44

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2012-01-13 15:01:44

Changing priority from minor to critical.


---

Attachment


---

Comment by kcrisman created at 2012-01-13 19:52:37

How did this change from minor to critical?  There is nothing wrong with tab completion on that platform AFAIR, just this timeout.  

Are there any problems we might expect from this change, such as interrupts not working as quickly for Maxima on other (newer) platforms?


---

Comment by jdemeyer created at 2012-01-13 22:58:08

Replying to [comment:5 kcrisman]:
> How did this change from minor to critical?
I think a patch which adds a new platform to the list of completely supported platforms warrants being "critical".  But that's just my opinion.

> There is nothing wrong with tab completion on that platform AFAIR, just this timeout.
That's why I changed the ticket title.  I guess somebody discovered the timeout in `maxima.py` and somehow mistakenly assumed it was because of TAB completion.  Or, in an earlier version there was a problem was TAB-completion on OS X 10.4 which is now fixed.

> Are there any problems we might expect from this change, such as interrupts not working as quickly for Maxima on other (newer) platforms?
Assuming that interrupts in Maxima are implemented properly (admittedly, a big "if"), there should not be any change in existing behaviour.  If the interrupt works properly, the changed timeout doesn't matter.

This patch does not change the interrupt behaviour of Maxima itself, it only changes how often Sage sends interrupts to Maxima.  On OS X 10.4, Maxima can be interrupted, it is just slow, which makes Sage think that something is wrong.


---

Comment by kcrisman created at 2012-01-15 01:37:02

> > How did this change from minor to critical?
> I think a patch which adds a new platform to the list of completely supported platforms warrants being "critical".  But that's just my opinion.
> 
> > There is nothing wrong with tab completion on that platform AFAIR, just this timeout.
> That's why I changed the ticket title.  I guess somebody discovered the timeout in `maxima.py` and somehow mistakenly assumed it was because of TAB completion.  Or, in an earlier version there was a problem was TAB-completion on OS X 10.4 which is now fixed.

I see, the answer to both are the same.  I should clarify: as far as I could determine when I filed this ticket, it was precisely the tab-completion doctest which caused the timeout, but not because tab-completion didn't work, it just didn't doctest well.  Hence the minor and mention of tabs.

> > Are there any problems we might expect from this change, such as interrupts not working as quickly for Maxima on other (newer) platforms?
> Assuming that interrupts in Maxima are implemented properly (admittedly, a big "if"), there should not be any change in existing behaviour.  If the interrupt works properly, the changed timeout doesn't matter.
> 
> This patch does not change the interrupt behaviour of Maxima itself, it only changes how often Sage sends interrupts to Maxima.  On OS X 10.4, Maxima can be interrupted, it is just slow, which makes Sage think that something is wrong.

Right.

I'll try this when I get a chance - which won't be immediately, still recovering from SD35.5 and an accident incurred during that time.


---

Comment by kcrisman created at 2012-01-17 15:25:31

Dumb question: why the nested try/except instead of two excepts?  Is one better than the other in this case?

Perhaps just uninformed question: In expect.py, we send `'quit;\n'+chr(3)`, but here you only send `chr(3)` (end of text character, says wikipedia).  Does that matter?  I'd think Maxima would like to hear quit, perhaps, but maybe it really just needs this special character to know to quit a computation.

----

```
sage -t  "devel/sage/sage/interfaces/maxima.py"             
         [241.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 242.5 seconds
```

So that is a good sign... first time I've had that in years!


---

Comment by jdemeyer created at 2012-01-17 15:54:20

Replying to [comment:8 kcrisman]:
> Dumb question: why the nested try/except instead of two excepts?  Is one better than the other in this case?
> 
> Perhaps just uninformed question: In expect.py, we send `'quit;\n'+chr(3)`, but here you only send `chr(3)` (end of text character, says wikipedia).
In maxima, "quit;" doesn't really do anything.  You just get

```
(%i1) quit;
(%o1)                                quit
```

In don't understand why `expect.py` sends `quit;` when it needs to interrupt.  Since it doesn't do anything in Maxima, I omitted it.

And `chr(3)` is `CTRL-C`, in other words: the interrupt character.


---

Comment by kcrisman created at 2012-01-17 16:16:59

> > Perhaps just uninformed question: In expect.py, we send `'quit;\n'+chr(3)`, but here you only send `chr(3)` (end of text character, says wikipedia).
> In don't understand why `expect.py` sends `quit;` when it needs to interrupt.  Since it doesn't do anything in Maxima, I omitted it.
> 
> And `chr(3)` is `CTRL-C`, in other words: the interrupt character.
Great, and I found a few sites that document this to some extent.  It seems that (historically) this was not universal.  Anyway.

I haven't tried this on any other computers.  How could I test this from the command line of Sage?  Presumably with Ctrl-C... that seems to work properly, sometimes I even see the new code in the traceback if I do it at the right time :)

Is that enough for positive review?


---

Comment by jdemeyer created at 2012-01-18 11:33:01

Replying to [comment:10 kcrisman]:
> Is that enough for positive review?
I guess that's up to your judgement really.

As for testing it: try using Sage to call Maxima commands and then interrupt that.  But it seems that's would you did, and you didn't manage to break anything.  That's a good sign.

Of course, interrupts are always a bit playing with fire, so I wouldn't be very surprised if this patch broke something in a non-obvious way.


---

Comment by kcrisman created at 2012-01-19 02:10:11

Well, I've tested it on Intel Mac as well and I get different errors but interrupting still seems to work.   It's nontrivial to find things that I can interrupt fast enough!  

There was one weird thing that happened when I repeatedly interrupted and/or let finish the computation

```
sage: y = function('y', x)
sage: desolve(sqrt(y)*diff(y,x)+e^(y)+cos(x)-sin(x+y)==0,y,contrib_ode=True)
```

from the documentation.  This is _not_ tested, because it just raises an error (Maxima can't solve it), but in one session I was able to really confuse ECL and kept getting an unbound INFLAG error.  But then I tried to get this again in the next session and, try as I might, I couldn't get it.

So I think this is at least as robust as our previous one.   Or one could compromise with three interrupts and not infinitely many :)

So let's say positive review.

----

Incidentally, you might find this amusing.

```
sage: maxima.eval('factorial(100000)')
'282422940796034787429342157802453551847749492609122485057891808654297...
sage: maxima.eval('factorial(100001)')
'100001!'
```



---

Comment by kcrisman created at 2012-01-19 02:10:11

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-01-20 08:37:11

Resolution: fixed
