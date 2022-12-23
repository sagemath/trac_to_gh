# Issue 258: gp2c -- integrate into SAGE

Issue created by migration from https://trac.sagemath.org/ticket/258

Original creator: was

Original creation time: 2007-02-11 20:51:22

Assignee: was

Create a command in SAGE based on the gp2c program of Bill Alombert.

I envision something like this:


```
sage: gp = Gp()   # new instead of gp interacitve interpreter
sage: gp.ceval("""
a block of code
""")
...
   at this point the gp2c translator is called and the resulting
   shared object library is loaded into this instance of gp.
...
sage: gp('code that uses new functions defined in the above block of code')
          resulting code runs faster since it is compiled. 
```


This will give yet another way of writing fast compiled code from interactive/interpreter SAGE. The ways would then be:
   * SageX
   * weave
   * gp2c

The web page for gp2c:

  http://pari.math.u-bordeaux.fr/download.html#gp2c


---

Comment by pdenapo created at 2008-01-08 04:03:22

Changing status from new to assigned.


---

Comment by pdenapo created at 2008-01-08 04:03:22

Changing assignee from was to pdenapo.


---

Comment by pdenapo created at 2008-01-08 04:03:22

I've succeded in creating a gp2c package (for gp2c-0.0.5pl6), that I'm uploading. In order for the script gp2c-run to work, it is needed a miror modification to the pari package so that the file pari.cfg gets installed.

I will try to do the integration with Sage, next (probably more difficult)

I've upload it to

http://pdenapo.googlepages.com/gp2c-0.0.5pl6.spkg

I'm submitting also the correspondig spkg-install file.

Here is my modified pari package:

http://pdenapo.googlepages.com/pari-2.3.3.p1.spkg

I'm submitting also: the patch needed for modifying spkg-install

Note: gp2c uses perl for compilation, if found. It would be possible to pass --with-perl=no
parameter to configure, if we don't want that (and use the precompiled descriptions for pari-2.3)


---

Comment by pdenapo created at 2008-01-08 04:06:13

A patch showing the required modifications to spkg-install in pari package


---

Attachment

spkg-install file for gp2c


---

Attachment

My second version of the attachment corrects a minor bash syntax-error (the packages worked either way, but fails to report an error message if pari.cfg was not there)


---

Comment by pdenapo created at 2008-01-15 15:19:14

By suggestion from MichaelAbshoff (on irc), I've created a unified package for pari
ang gp2c, you can downloaded at

http://pdenapo.googlepages.com/pari-2.3.3.p2.spkg

I agree with him in that his is a better solution since gp2c needs some changes in Pari (installing configuration file), and includes precompiled descriptions for an specific version of pari). 

This new version uses --with-perl=no when compiling gp2c (used precompiled descriptions for pari-2.3)

I also have included a README.Sage file explaning this.


---

Attachment

spkg-install file for the unified pari/gp2c package


---

Comment by pdenapo created at 2008-01-15 15:22:44

Readme file for the unified pari/gp2c package


---

Attachment

I submit a patch for the integration of gp2c into sage

This patch implements two functions for the Gp object:  gp2c_compile_file and gp2c

The first one compiles a file using gp2c-run and load its into the instance 
of the Gp intepreter asociated to the Gp object.
(is like the ceval function proposed in the description at the begining, but I think that
gp2c would be a better name). Also note that you cannot use it to evaluate arbitrary gp
expressions, just to define functions (in a syntax valid for gp2c, for example: avoid C identifiers)

You can use it to do something like:

G=Gp()
G.gp2c('f(x)=2*x')
G.eval('f(2)')
'4'

The second one takes a string, save it to a temporary file and compiles it using 
gp2c_compile_file

The temporary files are deleted when the Gp object is destroyed.

(This patch also generalizes the function delete_tmpfiles() from misc/misc.py
since I need it to delete the temporary files that gp2c patch creates)


---

Attachment

patch: gp2c integration into sage


---

Comment by was created at 2008-01-15 21:55:52

This is a comment *on this ticket* from Bill Allombert, who is the author of gp2c:

```
On Tue, Jan 15, 2008 at 08:34:43AM -0800, William Stein wrote:
> You might have comments about this:
>
> http://trac.sagemath.org/sage_trac/ticket/258

One issue I see is that you can load modules in GP but not unload them.

I do not think it is necessary to merge pari and gp2c. If you install
PARI properly (with make install), you get all the files needed for
compiling GP2C:
$prefix/lib/pari/pari.cfg
$prefix/share/pari/pari.desc
There is no need to change PARI itself, you just need to add a
dependency to GP2C.
Since PARI and GP2C have very different release schedule, merging
them will cause you unnecessary trouble.

Cheers,
Bill.

```



---

Comment by pdenapo created at 2008-01-15 22:44:17

About merging pari and gp2c: is like you prefer, my first idea was to have two separate
packages (my integration patch works with whatever aproach you choose)

Michael told me that integrating them could be better, to have less packages.
(and since if we put gp2c as unstable package, there is no way in which it can trigger a pari 
package update _which would be needed since it expects the pari.cfg to be installed)

However, keeping two separeted packages could make easier to update them when a new 
version of one of them is released, since as Bill says they have a very different release
schedule. Perhaps it is better to follow his advice.

About unloading modules, I don't know if that would be possible. Loading is implemented using
the "install" function in gp, is there a function like uninstall in Gp?


---

Comment by mabshoff created at 2008-02-14 22:46:07

Okay, after some fundamental discussion at SD7 I would now suggest to have individual packages. 

Cheers,

Michael


---

Comment by pdenapo created at 2008-05-27 15:00:19

To use this feature, you need to:

- apply the gp2c-instegration patch to sage. 
- install my pari spkg (which installs pari.cfg, needed for gp2c to compile) and then the gp2c spkg


---

Comment by mabshoff created at 2008-07-07 12:46:44

This has been sitting around for way too long, so let's sort it out soon. I am making myself editor of this ticket.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-07 12:46:44

Changing keywords from "" to "editor_mabshoff".


---

Comment by cremona created at 2008-07-21 19:37:18

I installed this with no problem, tried the examples and some of my own and it seems to work fine.  I only tried one-liners.

I have a lot of gp experience and also some with gp2c.

I think it would be excellent to have this in Sage.  +1


---

Comment by mabshoff created at 2008-08-27 08:19:32

Hi,

I have deleted the spkgs as attachment and instead linked them in the ticket description. I consider John's review a positive one, so I am changing the subject here. But we need a formal vote on sage-devel to get gp2c into the core of Sage.

Cheers,

Michael


---

Comment by ncalexan created at 2009-06-13 23:30:21

I think this is more or less wontfix at this point.


---

Comment by was created at 2009-06-14 07:24:34

> I think this is more or less wontfix at this point. 

The consensus on the mailing list from both very short votes was that gp2c should be an optional spkg.  However, given that nobody but the author of the patch has every requested gp2c functionality for Sage, even once, as far as I know, I don't think there is sufficient demand to justify the maintenance load.  Note that currently there is really no "maintenance load" for optional spkg's, but this *will* change, since I wrote a system for doctesting individual optional spkg's, and I *will* be doctesting sage + official optional spkg's regularly in the near future.  And then every optional spkg will increase the work to do this.

It seems that the best thing to do would be to close this ticket as "wontfix" now, but if some users clamor for gp2c functionality, we reopen it and make it an optional spkg.


---

Comment by was created at 2009-06-14 07:27:32

Resolution: wontfix


---

Comment by cremona created at 2009-06-14 09:50:48

Replying to [comment:15 was]:
> > I think this is more or less wontfix at this point. 
> 
> The consensus on the mailing list from both very short votes was that gp2c should be an optional spkg.  However, given that nobody but the author of the patch has every requested gp2c functionality for Sage, even once, as far as I know, I don't think there is sufficient demand to justify the maintenance load.  Note that currently there is really no "maintenance load" for optional spkg's, but this *will* change, since I wrote a system for doctesting individual optional spkg's, and I *will* be doctesting sage + official optional spkg's regularly in the near future.  And then every optional spkg will increase the work to do this.
> 
> It seems that the best thing to do would be to close this ticket as "wontfix" now, but if some users clamor for gp2c functionality, we reopen it and make it an optional spkg.  

As someone who originally voted for this, let me say that I am happy not to proceed with it.  There are very few gp scripts Sage uses now anyway.  The point about gp2c is that with it you can convert gp functions into pari library functions.  But the best way to do that anyway would be for the gp script's author to do it outside of Sage, as the result is a C program which can be compiled and linked with the pari library and then used in Sage.  There's no need for Sage itself to have gp2c.


---

Comment by jdemeyer created at 2015-07-09 09:14:11

Replying to [comment:17 cremona]:
> There's no need for Sage itself to have gp2c.
Do you still stand by that opinion?

One advantage would be calling GP scripts using the PARI library interface instead of GP.

See also #15809.


---

Comment by jdemeyer created at 2015-07-09 09:15:02

Changing component from interfaces to packages: optional.


---

Comment by jdemeyer created at 2015-07-09 09:15:02

Changing keywords from "editor_mabshoff" to "".


---

Comment by cremona created at 2015-07-09 11:55:14

What I said before is still true for the remaining  gp scripts used in Sage (which will probably reduce further in number soon -- the new lfun stuff in Pari will make ComputeL largely redundant), but as one who currently calls other gp sctiprs from within Sage it would be very good if that could easily be done via gp2c.  I would be happy to test such a set-up.


---

Comment by jdemeyer created at 2015-07-09 12:03:03

Resolution changed from wontfix to 


---

Comment by jdemeyer created at 2015-07-09 12:03:03

Changing status from closed to new.


---

Comment by jdemeyer created at 2015-07-09 12:31:46

There is one testsuite failure, I asked upstream PARI about it. But other than that, the package seems to work fine.
----
New commits:


---

Comment by jdemeyer created at 2015-07-09 12:31:46

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-07-09 12:49:12

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2015-07-09 12:49:12

Bill said I should use the git version of gp2c.


---

Comment by git created at 2015-07-09 12:56:26

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by jdemeyer created at 2015-07-09 12:56:58

Changing status from needs_work to needs_review.


---

Comment by jdemeyer created at 2015-07-09 12:56:58

Added upstream fixes from gp2c git repo, now passes testsuite.


---

Comment by cremona created at 2015-07-09 13:48:07

No time to etst this week, I'm in Oberwolfach, but so is Karim (a few metres from where I sit) so if there issues you would like me to raise with him, let me know.


---

Comment by git created at 2015-07-10 08:11:19

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2015-08-15 11:18:51

I confirm that it passes testsuite on my computer (Debian wheezy amd64).


---

Comment by chapoton created at 2015-08-22 16:51:16

Because there is an obsolete patchbot loop-testing this ticket, I temporarily change its status.


---

Comment by chapoton created at 2015-08-22 16:51:16

Changing status from needs_review to needs_info.


---

Comment by jdemeyer created at 2015-08-23 20:08:02

Changing status from needs_info to needs_review.


---

Comment by jdemeyer created at 2015-08-23 20:08:02

Replying to [comment:32 chapoton]:
> Because there is an obsolete patchbot loop-testing this ticket
Why is that a problem?

This ticket still needs review, despite what the patchbots think about it.


---

Comment by chapoton created at 2015-08-23 20:10:14

Yes, yes, but please, could you update "sage4" ?


---

Comment by vdelecroix created at 2015-10-21 20:09:29

Changing status from needs_review to needs_work.


---

Comment by vdelecroix created at 2015-10-21 20:09:29

Could you give more explanations in `SPKG.txt` about the two patches (`20150326.patch` and `global.patch`).


---

Comment by jdemeyer created at 2015-10-22 07:53:28

I cannot really give much more explanation, these are patches from upstream to fix some issues which came up while testing this ticket. See the two `gp2c` threads on [http://pari.math.u-bordeaux.fr/archives/pari-dev-1507/threads.html](http://pari.math.u-bordeaux.fr/archives/pari-dev-1507/threads.html)

I can instead try to use the upstream git repo without patches. Let me know if you prefer this.


---

Comment by vdelecroix created at 2015-10-22 09:34:12

Changing status from needs_work to positive_review.


---

Comment by vdelecroix created at 2015-10-22 09:34:12

Is "upstream stable + patches" always better than "upstream develop"? Yes.


---

Comment by vbraun created at 2015-10-23 17:28:08

Resolution: fixed
