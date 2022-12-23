# Issue 626: error building libcsage.so on some machines

Issue created by migration from https://trac.sagemath.org/ticket/626

Original creator: was

Original creation time: 2007-09-09 05:12:41

Assignee: craigcitro




---

Comment by was created at 2007-09-09 05:13:28


```
[21:57] <mabshoff_> But I started with PPC around 3 am.
[21:57] <wstein> craigcitro -- look at install.log
[21:57] <wstein> The build is really really simple.
[21:57] <mabshoff_> I wanted to debug the LinBox det on PPC problem.
[21:57] <wstein> i'm pretty sore from camping in a tent, then hiking, then
[21:57] <craigcitro> which build?
[21:58] <wstein> accidently falling down into a mountain pool when slipping in water...
[21:58] <craigcitro> eek
[21:58] <mabshoff_> :)
[21:58] <wstein> craigcitro -- install.lgo
[21:58] <wstein> install.log
[21:58] <craigcitro> in which directory? i'm currently looking at two different ones. ;)
[21:58] <wstein> Any of them.
[21:58] <craigcitro> but ntl_wrap.os isn't getting built there
[21:58] <wstein> Just look at SAGE_ROOT/install/log
[21:58] <mabshoff_> I will probably sleep for a litte while, but I will be back.
[21:58] <wstein> SAGE_ROOT/install.log
[21:58] <wstein> cool, cu.
[21:59] <craigcitro> enjoy mabshoff
[21:59] <mabshoff_> If Yi needs any input on DSage write me an email.
[21:59] <mabshoff_> That way we can merge PPC 32 Linux in 2.8.4.1 or whatever.
[21:59] <craigcitro> wstein: are you saying ntl_wrap.os is getting rebuilt and i'm just not seeing it?
[21:59] <mabshoff_> ok, cu in about 8-10 yours :)
[21:59] *** mabshoff_ is now known as mabshoff|away.
[22:00] <craigcitro> i'm just not sure why you're telling me to look at install.log
[22:00] <craigcitro> i was saying as fact that ntl_wrap.os isn't getting built
[22:00] <craigcitro> and that's the file that has the stack_chk symbol in it
[22:00] <wstein> because you can see *precisely* what lines gcc gets to build stuff.
[22:01] <craigcitro> which is how it's making it into libcsage.so
[22:01] <craigcitro> yeah, i'm looking at it right now
[22:01] <craigcitro> or, at least, it isn't getting built on mabshoff's faulty installs
[22:01] <wstein> interesting.
[22:02] <craigcitro> i think that's the problem
[22:02] <wstein> I wonder if we're just including a prebuilt version or something idiotic...
[22:02] <craigcitro> that's exactly what's happening
[22:02] <craigcitro> it's the copy that's shipping with 2.8.4-tar
[22:02] <wstein> ah ha!
[22:02] <wstein> ick.
[22:02] <craigcitro> and it has this crappy symbol in it
[22:02] <craigcitro> which then makes things go wonky
[22:02] <wstein> makes perfect sense.
[22:03] <wstein> Maybe scons rebuilds the file on other architectures, too.
[22:03] <craigcitro> so let's take that out of sage-2.8.4.tar ... or, better yet, do a scons -c first
[22:03] <wstein> yep!!!
[22:03] <wstein> It gets rebuilt on my intel mac box.
[22:03] <wstein> i.e., this line is in install.log
[22:03] <craigcitro> nods, lemme check on my machine
[22:03] <wstein> g++ -o ntl_wrap.os -c -fPIC -I/Users/was/sage-2.8.4.rc1/local/include -I/Users/was/sage-2.8.4.rc1/local/include/python2.5 -I/Users/was/sage-2.8.4.rc1/local/include/NTL ntl_wrap.cpp
[22:04] <wstein> it's not scons's fault. 
[22:04] <wstein> it's not gmp.
[22:04] <wstein> it's us being dumb.
[22:04] <craigcitro> grin yep
[22:04] <craigcitro> well, it's us not understanding scons
[22:04] <wstein> where I guess us = you, or me, or joel.
[22:04] <craigcitro> this is in spirit the same problem we were having with branch switching
[22:04] <craigcitro> we want to tell it to force rebuilds of lots of stuff
[22:04] <craigcitro> and we just aren't.
[22:05] <wstein> craigcitro -- i have to go now.
[22:05] <wstein> But you've totally solved the problem I think.
[22:05] <wstein> Great work!!!
[22:05] <craigcitro> grin thanks
[22:05] <craigcitro> so is the best fix just removing it from the tar?
[22:05] <wstein> And for now, I bet "sage -ba" will fix people's problems, since it does force a scons rebuild.
[22:05] <craigcitro> or also forcing rebuild?
[22:05] <craigcitro> nods
[22:05] <wstein> Please please post on sage-devel tonight.
[22:05] <craigcitro> scons -c in that directory works, too
[22:05] <wstein> got to go.
[22:05] <craigcitro> nods i will
[22:05] <wstein> by.
```



---

Comment by was created at 2007-09-09 14:56:49

Resolution: fixed


---

Comment by was created at 2007-09-09 14:56:49

I've fixed this for sage-2.8.4.1 (with much help from Craig Citro).

William
