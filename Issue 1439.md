# Issue 1439: (EASY) make install_package('...') through the notebook far less verbose

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-09 20:06:02

Assignee: was

CC:  was

Background:


```
On Dec 9, 2007 1:00 PM, root <daly`@`axiom-developer.org> wrote:
> >The main plus of this packaging for sage is that it builds from
> >source quickly (in a few minutes) using precompiled clisp files.
> 
> Well, on my 2Ghz machine with 2 Gig of memory running VMWare and
> using the sage vmware image (but upgrading the VM to have 1G memory)
> I started the package-install at 3:30am this morning. It is now
> 2:10pm and the build is still "in-process". They are heavy things,
> your minutes :-)

On a 1.8Ghz opteron (sagemath.org) it takes 18 minutes (I just tested 
the install).   I am completely baffled that it would take > 11 hours to
install into vmware under windows.  I'll look into that next time I get a
chance to use windows (in my office).   Thanks for reporting the problem. 

> Likely a portion of the problem is due to starting the package-install
> from the notebook. I'm running native windows and sage in the VM and
> connecting thru the browser.

That is very likely the problem.  The output of installing packages through
the notebook is way too verbose, so this is in fact a likely source of
the problem (which could be remedied).   Better would be to login as "manage"
and type "sage -i fricas-0.3.1".  

> I suspect a lot of CPU is going into running jsMath to redraw the
> output page. The Fricas build has a lot of output (which could be
> suppressed during package-install) and jsMath is not fast. Axiom
> has a NOISE variable in the Makefiles to suppress most output.

Excellent. 

> You might consider a note suggesting that installs be done from
> inside the virtual machine rather than thru the notebook interface.

Better would be to fix things so they work through the notebook well.

```


The fix would likely be to execute the update command, but pipe everything
to a file, and include a link to that file in the output (so one can look
at it and press refresh in the browser to test status).  




---

Comment by was created at 2007-12-10 07:08:24

This confirms my hypothesis...


```
Well,per your request, I logged in to the Sage VM and did
 sage -f fricas-0.3.1
simply hangs. However,
 sage -f axiom4sage-0.3.1
succeeds and shows a total time of
 real 18m42
or, if I include network time
 real 19.6
which is about the wall-clock time.

So there appears to be a suggestion that it might
be a good idea to do package installs directly rather
than thru the notebook interface. Potentially this
could be due to the large amount of screen output.

Apparently the package rename didn't work.

```



---

Comment by mabshoff created at 2008-02-16 01:38:15

This is related to #2174.

Cheers,

Michael


---

Comment by timdumol created at 2010-01-18 00:56:58

Doesn't seem to be a problem anymore. Close?


---

Comment by timdumol created at 2010-01-19 03:16:50

Works with sagenb-0.6


---

Comment by timdumol created at 2010-01-19 03:16:50

Resolution: fixed
