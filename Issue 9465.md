# Issue 9465: Update to FriCAS 1.1.0

Issue created by migration from Trac.

Original creator: hemmecke

Original creation time: 2010-07-09 12:39:04

Assignee: AlexGhitza

CC:  hemmecke rws

The earliear upgrade is in http://trac.sagemath.org/sage_trac/ticket/9354
Also look at http://trac.sagemath.org/sage_trac/ticket/6517
for more information.

http://sage.math.washington.edu/home/hemmecke/pub/fricas-1.1.0.spkg

http://sage.math.washington.edu/home/hemmecke/pub/fricasaldor-1.1.0.spkg

fricasaldor might not properly work on 64 bit machines or might not work at all.


---

Comment by hemmecke created at 2010-07-09 12:39:39

Changing status from new to needs_review.


---

Comment by AlexGhitza created at 2010-09-02 11:02:38

Changing component from algebra to packages.


---

Comment by dimpase created at 2012-01-23 05:30:00

Would you like to make an spkg with current Fricas?
I'll make sure to review it, etc.
Thanks!


---

Comment by dimpase created at 2012-01-23 05:32:13

for the record, fricas-1.0.9 spkg fails to install in Sage 4.8 on x86_64 Linux (Debian).


---

Comment by dimpase created at 2012-01-23 05:32:13

Changing status from needs_review to needs_work.


---

Comment by hemmecke created at 2012-01-26 23:26:36

Why are you considering 1.0.9? Above you find a link to 1.1.0. and
FriCAS progressed to 1.1.5.

However, in 1.1.5 the aldor-interface is broken. It's already fixed in trunk,
but I tend to wait till 1.1.6 is released in order to produce a new spkg.

Furthermore, quickly browsing over my spkg generation scripts, tells me,
that I will have to fix some small issues.

BTW, is it still required that FriCAS for Sage must use ECL and not SBCL?

Ralf


---

Comment by dimpase created at 2012-01-28 10:23:23

Replying to [comment:5 hemmecke]:
> Why are you considering 1.0.9? Above you find a link to 1.1.0. and
> FriCAS progressed to 1.1.5.

I was just pointing out that an upgrade is needed badly.


> 
> However, in 1.1.5 the aldor-interface is broken. It's already fixed in trunk,
> but I tend to wait till 1.1.6 is released in order to produce a new spkg.
> 
> Furthermore, quickly browsing over my spkg generation scripts, tells me,
> that I will have to fix some small issues.
> 
> BTW, is it still required that FriCAS for Sage must use ECL and not SBCL?

Was it ever required? I guess it was never assumed that SBCL is installed on the system, so by default
FriCAS can fall back on ECL provided by Sage.
(This would need a trivial adjustment of the spkg-install, I suppose).

On the other hand a fast interface to FriCAS would need an embeddable Lisp, and ECL fits this bill.

Dima
 

> 
> Ralf


---

Comment by jdemeyer created at 2014-11-13 13:57:51

Changing component from packages: standard to packages: experimental.


---

Comment by chapoton created at 2014-12-06 15:00:01

Changing keywords from "" to "fricas".


---

Comment by vdelecroix created at 2014-12-06 15:22:35

Hi,

Could we ship the last version ?

```
November 24, 2014 -- FriCAS 1.2.4 released.
```


Vincent


---

Comment by vdelecroix created at 2014-12-06 15:49:03

I wrote the spkg-install and it at least compile on my computer... If anybody want to test it
 - download the source tarball `fricas-1.2.4-full.tar.bz2`, move it to `$SAGE_ROOT/upstream` and rename it `fricas-1.2.4.tar.bz2`
 - switch to the git branch provided here
 - run `sage -i fricas` and then `make` (from `$SAGE_ROOT`)

I am currently trying to see whether the interface is not broken...

Vincent


---

Comment by git created at 2014-12-06 15:49:47

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by vdelecroix created at 2014-12-06 15:53:15

Changing status from needs_work to needs_review.


---

Comment by vdelecroix created at 2014-12-06 15:54:59

Looks like it work -> needs review.


---

Comment by chapoton created at 2014-12-06 16:41:23

I have added a few '#optional - fricas' so that the tests pass both with '-optional=fricas' and without, in 'interfaces/fricas.py'
----
New commits:


---

Comment by chapoton created at 2014-12-06 16:45:02

Looks good to me. If somebody else can confirm, this seems to be good to go.


---

Comment by rws created at 2014-12-06 16:56:29

Wow, fricas has Puiseux series. Builds fine. Passes all tests in `interfaces`, `rings`, and `structure`.


---

Comment by rws created at 2014-12-06 16:56:29

Changing status from needs_review to positive_review.


---

Comment by hemmecke created at 2014-12-06 17:23:23

1. See also http://fricas.github.io

2. What exactly is the problem with fricas-aldor on 64bit machines?

3. Meanwhile Aldor is under the Apache License 2.0. So fricas-aldor could even install Aldor. Or there should be another spkg that installs Aldor and fricas-aldor might trigger installation of Aldor, if it is not already there.


---

Comment by vdelecroix created at 2014-12-06 17:28:29

Replying to [comment:24 hemmecke]:
> 1. See also http://fricas.github.io

The documentation is much nicer there... why the project is both on sourceforge and github ?

> 2. What exactly is the problem with fricas-aldor on 64bit machines?

No idea... I have to try, where the source code is available ?

> 3. Meanwhile Aldor is under the Apache License 2.0. So fricas-aldor could even install Aldor. Or there should be another spkg that installs Aldor and fricas-aldor might trigger installation of Aldor, if it is not already there.

I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.

Vincent


---

Comment by hemmecke created at 2014-12-06 18:47:34

Replying to [comment:25 vdelecroix]:
> The documentation is much nicer there... why the project is both on sourceforge and github ?

The project is officially on sourceforge and still under SVN. :-( But since I think git is tremendously better, I created a life mirror at github.
See https://sites.google.com/site/hemmecke/fricas-svn#fricas-devel for details.
I'd be happy if FriCAS switched completely to git, but that's not a big issue with mainly only Waldek and me commiting to the code base.
 
> > 2. What exactly is the problem with fricas-aldor on 64bit machines?
> 
> No idea... I have to try, where the source code is available ?

Source code of what?

Aldor: https://github.com/pippijn/aldor
fricas-aldor spkg: ummmm.... I used to have a hg repo somewhere on my sagemath account, but don't know what the computer is that I have to login. I would then try to convert it to git and put it to github.

> I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.

Please do that and put me into the CC. I'm currently a little unfamiliar with Sage development.


---

Comment by vdelecroix created at 2014-12-06 20:03:28

Replying to [comment:26 hemmecke]:
> Replying to [comment:25 vdelecroix]:
>  
> > > 2. What exactly is the problem with fricas-aldor on 64bit machines?
> > 
> > No idea... I have to try, where the source code is available ?
> 
> Source code of what?
> 
> Aldor: https://github.com/pippijn/aldor
> fricas-aldor spkg: ummmm.... I used to have a hg repo somewhere on my sagemath account, but don't know what the computer is that I have to login. I would then try to convert it to git and put it to github.

It would be better to have a link to a stable release with a version number (i.e. "an official tarball"). Otherwise we need to artificially create one.

> > I guess it is safer to have separated packages. This ticket will be closed and contain only the fricas update. But we might open others for aldor/fricas-aldor.
> 
> Please do that and put me into the CC. I'm currently a little unfamiliar with Sage development.

To create packages the documentation is very well written: http://sagemath.org/doc/developer/packaging.html (I might help for that step). Then there is the second step of having an interface within sage (I have very little experience with that).

Vincent


---

Comment by chapoton created at 2014-12-07 11:30:05

See #9427 for a follow-up ticket on integration.


---

Comment by vbraun created at 2014-12-11 17:31:43

No $`@`#$ sourceforge links the next time, please.


---

Comment by vbraun created at 2014-12-12 12:29:56

Resolution: fixed


---

Comment by jdemeyer created at 2015-06-06 09:30:51

FYI: optional doctests don't pass, so the package was moved to experimental.
