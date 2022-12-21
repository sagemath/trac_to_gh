# Issue 3360: Upgarde sympow to the 1.019 release

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-04 15:51:07

Assignee: mabshoff

CC:  slelievre @timokau saraedum isuruf arojas mjo embray dimpase tscrim

Sympow 1.019 is already upstream in Debian, so let's upgrade.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-02 04:55:47

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-03-02 04:55:47

The latest release is 1.023 at

 http://magma.maths.usyd.edu.au/~watkins/sympow.tar.bz2
 http://magma.maths.usyd.edu.au/~watkins/sympow.src.tar.bz2

Cheers,

Michael


---

Comment by slelievre created at 2018-04-20 20:26:59

Changing keywords from "" to "upgrade, sympow".


---

Comment by fbissey created at 2018-04-20 22:07:22

Didn't realise there was a newer version. Considering sympow's code, an upgrade can only be an improvement.


---

Comment by slelievre created at 2018-06-02 09:57:33

See also #25099 "Add DESTDIR support for sympow".


---

Comment by saraedum created at 2018-06-14 10:35:29

sympow 1.023 segfaults (in Debian) on some inputs that used to work with 1.018

```
$ sympow -analrank -curve "[0,1,1,-2,0]"
sympow 1.023 RELEASE (Debian 1.023-8)  (c) Mark Watkins --- see README and COPYING for details
Minimal model of curve  is [0,1,1,-2,0]
At 389: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
Conductor is 389
sp 1: Conductor at 389 is 1+0, root number is -1
sp 1: Euler factor at 389 is 1-1*x
1st sym power conductor is 389, global root number is 1
NT 1d0: 43
Maximal number of terms is 43
0.0E+00
Done with small primes 1049
Segmentation fault (core dumped)
```



---

Comment by saraedum created at 2018-06-14 12:02:40

This is essentially a known bug: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=863919. I submitted a patch for it on salsa: https://salsa.debian.org/science-team/sympow/merge_requests/1.


---

Comment by @timokau created at 2018-07-13 19:16:30

In an effort to update the sympow package in nix, I contacted the debian maintainer (Jerome Benoit).

He told me that he really did receive their tarball in a private email (how did you guys manage to find that file on his homepage?). He also told me that "the upstream author is responsive (and he did not have a GIT because the code was written before the GIT revolution)".

Debian adds sage's patches and some more[1], as for example the bug fix saraedum mentions. It seems like Debian effectively became the new upstream of this package. I asked the maintainer if he had considered making it official and forking it, which he declined.

[1] https://salsa.debian.org/science-team/sympow/tree/master/debian/patches


---

Comment by saraedum created at 2018-07-13 19:27:08

Replying to [comment:12 gh-timokau]:
> He told me that he really did receive their tarball in a private email (how did you guys manage to find that file on his homepage?).
In my case: I wrote a private email to the sympow author and he told me about the URL.

> He also told me that "the upstream author is responsive (and he did not have a GIT because the code was written before the GIT revolution)".
> Debian adds sage's patches and some more[1], as for example the bug fix saraedum mentions. It seems like Debian effectively became the new upstream of this package. I asked the maintainer if he had considered making it official and forking it, which he declined.
> 
> [1] https://salsa.debian.org/science-team/sympow/tree/master/debian/patches
I was in correspondence with the sympow author about the recent segfault patch. Afterwards I proposed to move the project to github and basically take over maintenance but I have not heard back for a while since then.


---

Comment by @jgmbenoit created at 2018-07-13 19:42:15

Is the URL still valid ?
Otherwise, after all, I may also consider to maintain a fork of sympow.


---

Comment by @timokau created at 2018-07-13 21:22:26

sympow still seems to be hosted at that URL. Its just not advertised anywhere. But there are still all those semi-mandatory patches flying around that should probably be upstreamed. Having the project in some public version control would be great.


---

Comment by slelievre created at 2018-07-14 03:56:36

My notes about the url at
https://trac.sagemath.org/ticket/25099#comment:13
still hold. Public version control of the original code
and the existing extra patches would definitely help,
as well as a home page for the project.


---

Comment by @jgmbenoit created at 2018-07-15 04:59:07

I am on my way to fork sympow on gitlab. My concern will be only the unix part (read not the mathematical part) in view to harmonize related patches and integration in unix systems.
Notes: My time being counted and limited, it would be question of weekends, rather of days.


---

Comment by @timokau created at 2018-07-15 09:28:14

Great! Thank you for doing that.


---

Comment by @jgmbenoit created at 2018-07-21 06:48:05

I have just rendered public my fork at [GitLab](GitLab): https://gitlab.com/rezozer/forks/sympow
Please test and report !


---

Comment by @timokau created at 2018-07-23 13:05:55

Updating from 1.018.1, this breaks the sage testsuite (looks like pretty much all the sympow interaction is broken):


```
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/lfunctions/sympow.py  # 13 doctests failed
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/modular/abvar/abvar.py  # 1 doctest failed
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/modular/hecke/submodule.py  # 1 doctest failed
sage -t --long /nix/store/7bi7v0bxwrcs5f510i1d54qqd5jqqj2r-sage-src-8.2/src/sage/schemes/elliptic_curves/ell_rational_field.py  # 17 doctests failed
```


Probably just some minor change in output formatting that breaks the parser. Before I investigate further, this is presumably already fixed on Debian? Julian do you know the cause?


---

Comment by @timokau created at 2018-07-23 13:06:52

`@`gh-jgmbenoit does the original author know about the fork? Has he said anything about it?


---

Comment by @jgmbenoit created at 2018-07-23 13:38:41

`@`saraedum I am not surprised that it breaks the sage testsuite because the patched version runs more like any regular program. In fact it must break the sage related code itself: see the section [SYMPOW Data set](https://gitlab.com/rezozer/forks/sympow#sympow-data-setup) up for details.
Otherwise, since it works on Debian, I guess it was fixed there. But I am not the one who did the fix.
So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you.


---

Comment by @jgmbenoit created at 2018-07-23 13:47:48

Replying to [comment:21 gh-timokau]:
> `@`gh-jgmbenoit does the original author know about the fork? Has he said anything about it?

I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back.


---

Comment by @timokau created at 2018-07-23 14:30:47

> So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you. 

That's why I added saraedum (Julian Rüdth). I was under the impression that he is the Debian maintainer. Is he not?

> I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back. 

Great. Please keep me posted (for example by posting here) in case you get feedback. It would be nice to be able to add that note to the update.


---

Comment by @jgmbenoit created at 2018-07-23 14:49:54

Replying to [comment:24 gh-timokau]:
> > So you want to check the Debian patches. Feel free to send email to the Debian Sage Team: the person who did it may guide you. 
> 
> That's why I added saraedum (Julian Rüdth). I was under the impression that he is the Debian maintainer. Is he not?
> 
> > I sent an email to the upstream author just before I announced here my intention to fork it. So, far I got no feed back. 
> 
> Great. Please keep me posted (for example by posting here) in case you get feedback. It would be nice to be able to add that note to the update.

It is a team work. To my knowledge, Julian is a new comer. Whatever, it was certainly fix a long time given that I wrote the Debian patches a long time ago, at least before that Stretch was frozen.
Concerning Sage on Debian, the best is to send an email to the dedicated list:

debian-science-sagemath _at_ alioth-lists.debian.net


---

Comment by @timokau created at 2018-07-23 15:24:35

I cross-posted to that mailing list and sage-packaging: https://groups.google.com/forum/#!topic/sage-packaging/B3yTZ8eIbwM


---

Comment by @timokau created at 2018-07-23 15:25:59

By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.


---

Comment by @jgmbenoit created at 2018-07-23 16:13:00

Replying to [comment:27 gh-timokau]:
> By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.

GitLab allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit


---

Comment by @jgmbenoit created at 2018-07-23 16:14:24

Replying to [comment:26 gh-timokau]:
> I cross-posted to that mailing list and sage-packaging: https://groups.google.com/forum/#!topic/sage-packaging/B3yTZ8eIbwM

Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware.


---

Comment by @timokau created at 2018-07-23 16:21:12

Replying to [comment:28 gh-jgmbenoit]:
> Replying to [comment:27 gh-timokau]:
> > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.
> 
> [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit

Can that be nested further or is subgroup the limit?

> Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. 

Were they? I haven't received a reply yet (besides that my post is awaiting approval).


---

Comment by @jgmbenoit created at 2018-07-23 16:31:44

Replying to [comment:30 gh-timokau]:
> Replying to [comment:28 gh-jgmbenoit]:
> > Replying to [comment:27 gh-timokau]:
> > > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.
> > 
> > [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit
> 
> Can that be nested further or is subgroup the limit?

it can be nested further. I do not know the limit.

> 
> > Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. 
> 
> Were they? 

at least, I am :-)

 I haven't received a reply yet (besides that my post is awaiting approval).

Be patient, it is summer time.


---

Comment by @timokau created at 2018-07-23 16:38:37

Replying to [comment:31 gh-jgmbenoit]:
> Replying to [comment:30 gh-timokau]:
> > Replying to [comment:28 gh-jgmbenoit]:
> > > Replying to [comment:27 gh-timokau]:
> > > > By the way what is the `forks` in the URL to your repo? Does gitlab allow subfolders or something? I'm asking because I never saw that before (always only `owner/repo`) and our infrastructure currently doesn't support fetching source from such a subfolder.
> > > 
> > > [GitLab](GitLab) allows one to create groups and subgroups: rezozer is a group , forks a subgroup, sympow a project. My [GitLab](GitLab) webpage is https://gitlab.com/jgmbenoit
> > 
> > Can that be nested further or is subgroup the limit?
> 
> it can be nested further. I do not know the limit.

Alright, thanks.


> 
> > 
> > > Thanks, I should do it. Anyway, I guess that the Debian maintainer for sympow was aware. 
> > 
> > Were they? 
> 
> at least, I am :-)
> 
>  I haven't received a reply yet (besides that my post is awaiting approval).
> 
> Be patient, it is summer time.

Of course :) I must've misunderstood your message, I thought you were referring to a reply to that email.


---

Comment by @timokau created at 2018-07-27 14:44:17

Okay turns out I just messed up packaging. Its not strictly relevant for this ticket and I thought about just emailing you, but maybe the sage package upgrade will run into the same problems.

So nix installs every package in its own prefix. That means sympow would go into `/nix/store/some-sympow-specific-folder-name/`. Only the sympow files would be in that folder.

I'm currently achieving that by setting the install flag `DESTDIR=$out` ($out pointing to that sympow directory). However when launching an example from the README, it fails because it looks for the `new_data` script in `/usr/local/lib/sympow`. That script is in `$out/usr/local/lib/sympow`. Here's the error:


```
$ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Minimal model of curve  is [1,-1,0,4,3]
At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
Conductor is 10351
P02L not found in param_data file
Will compute data mesh file for `2'
Make data for  symmetric power 2
/bin/sh: /usr/local/lib/sympow/new_data: No such file or directory
**ERROR** [FAILED]
May be tried with 'sympow -new_data `2'
```


In the README I see that I can set the `SYMPOW_PKGLIBDIR` environment variable (although that shouldn't be necessary). After doing that, I get


```
$ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Running the new_data script for -sp 2
Making the datafiles for -sp 2

**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Rewarping param_data file /home/timo/.sympow/datafiles/param_data
Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Removing any old data files
removed '/home/timo/.sympow/datafiles/P02HM.txt'
removed '/home/timo/.sympow/datafiles/P02HS.txt'
removed '/home/timo/.sympow/datafiles/P02LM.txt'
removed '/home/timo/.sympow/datafiles/P02LS.txt'
Running the gp script

**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
***   at top-level: coeffs(0)
***                 ^---------
***   not a function in function call
***   at top-level: coeffE(1)
***                 ^---------
***   not a function in function call
***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
***   at top-level: coeffs(0)
***                 ^---------
***   not a function in function call
***   at top-level: coeffO(1)
***                 ^---------
***   not a function in function call

**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Trimming the data files
trimmed `/home/timo/.sympow/datafiles/P02HM.txt'
trimmed `/home/timo/.sympow/datafiles/P02HS.txt'
trimmed `/home/timo/.sympow/datafiles/P02LM.txt'
trimmed `/home/timo/.sympow/datafiles/P02LS.txt'
**WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
Rewarping param_data file /home/timo/.sympow/datafiles/param_data
Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
Finished with -sp 2
**ERROR** P02L not found in param_data file in second round
sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
Minimal model of curve  is [1,-1,0,4,3]
At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
Conductor is 10351
P02L not found in param_data file
Will compute data mesh file for `2'
Has computed data mesh file for `2'
```


Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters. pari is included in the build dependencies.

Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package. Otherwilse I'll just take some from the README, but having them included in the package is better of course.


---

Comment by @jgmbenoit created at 2018-07-27 18:46:03

Replying to [comment:33 gh-timokau]:
> Okay turns out I just messed up packaging. Its not strictly relevant for this ticket

I guess it would be a relevant ticket for the fork.

 and I thought about just emailing you, but maybe the sage package upgrade will run into the same problems.
> 
> So nix installs every package in its own prefix. That means sympow would go into `/nix/store/some-sympow-specific-folder-name/`. Only the sympow files would be in that folder.
> 
> I'm currently achieving that by setting the install flag `DESTDIR=$out` ($out pointing to that sympow directory). However when launching an example from the README, it fails because it looks for the `new_data` script in `/usr/local/lib/sympow`. That script is in `$out/usr/local/lib/sympow`. Here's the error:
> 
> {{{
> $ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
> sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Minimal model of curve  is [1,-1,0,4,3]
> At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> Conductor is 10351
> P02L not found in param_data file
> Will compute data mesh file for `2'
> Make data for  symmetric power 2
> /bin/sh: /usr/local/lib/sympow/new_data: No such file or directory
> **ERROR** [FAILED]
> May be tried with 'sympow -new_data `2'
> }}}
> 
> In the README I see that I can set the `SYMPOW_PKGLIBDIR` environment variable (although that shouldn't be necessary

it is why it is written that they are meant mainly for development and debugging purpose

Here you are misusing PREFIX, VARPREFIX, and DESTDIR (see below)

). After doing that, I get
> 
> {{{
> $ result/bin/sympow -sp 2p16 -curve "[1,2,3,4,5]"
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Running the new_data script for -sp 2
> Making the datafiles for -sp 2
> 
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Rewarping param_data file /home/timo/.sympow/datafiles/param_data
> Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Removing any old data files
> removed '/home/timo/.sympow/datafiles/P02HM.txt'
> removed '/home/timo/.sympow/datafiles/P02HS.txt'
> removed '/home/timo/.sympow/datafiles/P02LM.txt'
> removed '/home/timo/.sympow/datafiles/P02LS.txt'
> Running the gp script
> 
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> ***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
> ***   at top-level: coeffs(0)
> ***                 ^---------
> ***   not a function in function call
> ***   at top-level: coeffE(1)
> ***                 ^---------
> ***   not a function in function call
> ***   error opening input file: `/usr/local/share/sympow/standard1.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard2.gp'.
> ***   error opening input file: `/usr/local/share/sympow/standard3.gp'.
> ***   at top-level: coeffs(0)
> ***                 ^---------
> ***   not a function in function call
> ***   at top-level: coeffO(1)
> ***                 ^---------
> ***   not a function in function call
> 
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Trimming the data files
> trimmed `/home/timo/.sympow/datafiles/P02HM.txt'
> trimmed `/home/timo/.sympow/datafiles/P02HS.txt'
> trimmed `/home/timo/.sympow/datafiles/P02LM.txt'
> trimmed `/home/timo/.sympow/datafiles/P02LS.txt'
> **WARNING** failed to create data bin package cache folder /var/cache/sympow/datafiles/le64
> Rewarping param_data file /home/timo/.sympow/datafiles/param_data
> Left with 0 entries in param_data file /home/timo/.sympow/datafiles/param_data
> Finished with -sp 2
> **ERROR** P02L not found in param_data file in second round
> sympow 2.023.2 RELEASE  (c) Mark Watkins --- see README and COPYING for details
> Minimal model of curve  is [1,-1,0,4,3]
> At 11: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> At 941: Inertia Group is  C1 MULTIPLICATIVE REDUCTION
> Conductor is 10351
> P02L not found in param_data file
> Will compute data mesh file for `2'
> Has computed data mesh file for `2'
> }}}
> 
> Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.

DESTDIR is mainly meant for packaging in custom Makefile (not for testing)

To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.

The patches I brought from Debian are meant to ease integration in Unix for maintainers and users (compare to the original version): DESTDIR, PREFIX, and VARPREFIX have the customary meaning.

Basically you cannot test in DESTDIR unless you set correctly the environment variables because
PREFIXed  paths are hard coded.

 pari is included in the build dependencies.
> 
> Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.

The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.


> Otherwilse I'll just take some from the README, but having them included in the package is better of course.


---

Comment by @timokau created at 2018-07-28 12:36:34

Replying to [comment:34 gh-jgmbenoit]:
> Replying to [comment:33 gh-timokau]:
> > ...
> > Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.
> 
> DESTDIR is mainly meant for packaging in custom Makefile (not for testing)
> 
> To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.

Right, `DESTDIR` was a leftover from the old way to package sympow. Using `PREFIX` instead fixes the issue.

Thank you.

> > Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.
> 
> The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.

Yes, install checks is exactly what I'd want. To catch issues like this early. I assumed the sage interface was at fault, even though it was just faulty packaging. So after installation (which at least for nix is the same as packaging; the installation result can just be put in an archive and distributed), something like autotools `make installcheck` would be what I want.


What is the difference between `/var/cache/sympow` and `~/.sympow`? When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?


---

Comment by @jgmbenoit created at 2018-07-28 17:09:22

Replying to [comment:35 gh-timokau]:
> Replying to [comment:34 gh-jgmbenoit]:
> > Replying to [comment:33 gh-timokau]:
> > > ...
> > > Am I doing something wrong or is that an issue with the `Configure` script? I'm executing `./Configure` without parameters.
> > 
> > DESTDIR is mainly meant for packaging in custom Makefile (not for testing)
> > 
> > To do what you want, I guess that you have to set up PREFIX (and maybe VARPREFIX) as it is done with customary Makefile.
> 
> Right, `DESTDIR` was a leftover from the old way to package sympow. Using `PREFIX` instead fixes the issue.
> 
> Thank you.
> 
> > > Also in case you find the time, it would be great if you could add a handful of test cases. I see that you already have some tests in the debian package.
> > 
> > The test in debian/tests are not meant to run at building time but once sympow is installed; they are CI tests. I am considering to write a test script for checking at building in view to migrate to autotools.
> 
> Yes, install checks is exactly what I'd want. To catch issues like this early. I assumed the sage interface was at fault, even though it was just faulty packaging. So after installation (which at least for nix is the same as packaging; the installation result can just be put in an archive and distributed), something like autotools `make installcheck` would be what I want.
> 
> 
> What is the difference between `/var/cache/sympow` and `~/.sympow`?

/var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
1] /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
2] /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.


~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER when the clear version whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
Behind this, there is a community policy: we can reuse data computed by other users.

The data in HOME/.sympow are autoritative over the one system-wide ones,
and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.

My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).

If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.

Having said that, it is okay to distributed no precomputed data.

My point is that some examples or tests in the literature may depend on the historical data,
so having them can speed up tests and keep the end users cool.
I strongly suggest to distribute the historical precomputed data (and the Sage ones).





 When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?

Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.

Jerome


---

Comment by @timokau created at 2018-07-29 13:17:55

Replying to [comment:36 gh-jgmbenoit]:
> Replying to [comment:35 gh-timokau]:
> > What is the difference between `/var/cache/sympow` and `~/.sympow`?
> 
> /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
>
> * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
>
> * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.

Dependant on the exact CPU model or just x86/aarch, 32/64 bits?


> ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
> Behind this, there is a community policy: we can reuse data computed by other users.
> 
> The data in HOME/.sympow are autoritative over the one system-wide ones,
> and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
> over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.
> 
> My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).
> 
> If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.

If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?


> Having said that, it is okay to distributed no precomputed data.

I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.


> I strongly suggest to distribute the historical precomputed data (and the Sage ones).

So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`? It looks like the debian package still calls gp manually. So that'd be


```
for data in 1d0 2 2d0h 3d0 3d1 4; do
	sympow -new_data "$data"
done
```


But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?

>  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?
> 
> Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.

Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.


---

Comment by @jgmbenoit created at 2018-07-29 15:05:41

Replying to [comment:37 gh-timokau]:
> Replying to [comment:36 gh-jgmbenoit]:
> > Replying to [comment:35 gh-timokau]:
> > > What is the difference between `/var/cache/sympow` and `~/.sympow`?
> > 
> > /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
> >
> > * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
> >
> > * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.
> 
> Dependant on the exact CPU model or just x86/aarch, 32/64 bits?

endianness



> 
> 
> > ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
> > Behind this, there is a community policy: we can reuse data computed by other users.
> > 
> > The data in HOME/.sympow are autoritative over the one system-wide ones,
> > and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
> > over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.
> > 
> > My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).
> > 
> > If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.
> 
> If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?

yes but just to write the binary data, which the binary version of the clean data:
1] so whoever write it, the output must be the same ;
2] any USER can bypass them by writting their own clean file in HOME/.sympow 
3] any USER can remove them;
4] if faulty binary are set, we can trace back the faulty USER ;
5] the superuser can create a specific group.



> 
> 
> > Having said that, it is okay to distributed no precomputed data.
> 
> I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.
> 
He does not: he will get a warning message, but sympow will continue.
The USER can pass the -quiet option to silence the warnings.
No warning will not be ideal: the user must be aware if the set up is not correct.

> 
> > I strongly suggest to distribute the historical precomputed data (and the Sage ones).
> 
> So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`?

There is no such file but a script in debian/adhoc/job which is called at packaging time 
and which complete the original armd.sh . I could merge them, but I will not because it will touch
the math part (what I want to avoid).


 It looks like the debian package still calls gp manually. So that'd be
> 
> {{{
> for data in 1d0 2 2d0h 3d0 3d1 4; do
> 	sympow -new_data "$data"
> done
> }}}

But it is not.


A debian centric patch is applies to add the extra data: debain/patches/debianization.patch 
At packaging time, besides the original script armd.sh , the script debian/adhoc/job/sympow-new_data.job  is launched : those scripts call gp (and not sympow).

> 
> But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?

see above



> 
> >  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?
> > 
> > Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.
> 
> Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.

so it is a warning (an not an ERROR message followed but an exit(-1)): I would consider it as a feature but not as a bug.
In fact, a couple of checks are performed to detect a corrupted folder set up and avoid surprises . 


The bug is in the installation process:
the correct privileges must be encoded in Configure : I will try to fix this the next week-end .
And in the README.md file: I should document better this part.

For now, to silent this warning, just set the right privilege or pass the option  -quiet : no will be write if /usr/share/sympow/datafiles is empty .

Let me know if you think that a mechanism must be implemented to avoid this warning message.

Jerome


---

Comment by @jgmbenoit created at 2018-07-29 15:11:57

> But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?

This is the behaviour of the original source, hence the patch.


---

Comment by @timokau created at 2018-07-29 17:11:26

Replying to [comment:38 gh-jgmbenoit]:
> Replying to [comment:37 gh-timokau]:
> > Replying to [comment:36 gh-jgmbenoit]:
> > > Replying to [comment:35 gh-timokau]:
> > > > What is the difference between `/var/cache/sympow` and `~/.sympow`?
> > > 
> > > /var/cache/sympow/datafiles/ goes in pair with /usr/share/sympow/datafiles/ :
> > >
> > > * /usr/share/sympow/datafiles/ contains data files in clear which are assumed to be manage at the superuser scale (basically a set of precomputed data installed at installation time);
> > >
> > > * /var/cache/sympow/datafiles/le64 contains the associated binaries (which are architecture dependent) that are not distributed but computed on the fly when necessary by the first user.
> > 
> > Dependant on the exact CPU model or just x86/aarch, 32/64 bits?
> 
> endianness

So would it be reasonable to pre-compute and distribute all the /var/cache data?

> > > ~/.sympow/datafiles/ will contain data files (clear versions and binaries) generated by USER whenever the clear version is not readable in  /usr/share/sympow/datafiles/ .
> > > Behind this, there is a community policy: we can reuse data computed by other users.
> > > 
> > > The data in HOME/.sympow are autoritative over the one system-wide ones,
> > > and The data in SYMPOW_CACHEDIR and SYMPOW_CACHEDIR/sympow are authoritative
> > > over the ones in HOME/.sympow . Nothing special here from a UNIX user point of view.
> > > 
> > > My aim was to keep the spirit of the original version. Some data were distributed to avoid the user some maneuvers and to wait a while (at this glorious time, computers were extremely slow and the users have to run GP themselves: thanks to Intel and its competitors and to my patches, this time is over and we can now enjoy the full power of SYMPOW).
> > > 
> > > If you look the code, for the right to read or write, something inspired by openssh code was implemented (I do not remember the details, but I remember that I tested it heavily). For Debian, beside the historical data, extra data are provided (and guessed that I took the list from Sage (must be double checked)). We can image to provide more data. You can find the job and a script to generate jobs in the material provided by Debian. These data are computed at packaging time, somehow it is also a `check'.
> > 
> > If I read the debian post install scripts correctly, doesn't everybody just have r+w access to the /var/cache directory?
> 
> yes but just to write the binary data, which the binary version of the clean data:
> 1] so whoever write it, the output must be the same ;
> 2] any USER can bypass them by writting their own clean file in HOME/.sympow 
> 3] any USER can remove them;
> 4] if faulty binary are set, we can trace back the faulty USER ;
> 5] the superuser can create a specific group.
> 
> > 
> > 
> > > Having said that, it is okay to distributed no precomputed data.
> > 
> > I'm not having any problems with the /usr/share precomputed data. What isn't ideal is that the user needs runtime write-access to the /var/cache directory.
> > 
> He does not: he will get a warning message, but sympow will continue.
> The USER can pass the -quiet option to silence the warnings.
> No warning will not be ideal: the user must be aware if the set up is not correct.

And then sympow will fall back to `~/.sympow` and behave exactly as usual?

> > > I strongly suggest to distribute the historical precomputed data (and the Sage ones).
> > 
> > So basically running `sympow -new_data` with all the arguments listed in debians `precomputed_data-lisof_parameter.data`?
> 
> There is no such file but a script in debian/adhoc/job which is called at packaging time 
> and which complete the original armd.sh . I could merge them, but I will not because it will touch
> the math part (what I want to avoid).
> 
> 
>  It looks like the debian package still calls gp manually. So that'd be
> > 
> > {{{
> > for data in 1d0 2 2d0h 3d0 3d1 4; do
> > 	sympow -new_data "$data"
> > done
> > }}}
> 
> But it is not.
> 
> 
> A debian centric patch is applies to add the extra data: debain/patches/debianization.patch 
> At packaging time, besides the original script armd.sh , the script debian/adhoc/job/sympow-new_data.job  is launched : those scripts call gp (and not sympow).

So what does the debian version do differntly?

> > But that tries to access HOME/.sympow. So you're generating user-level cache files at install time?
> 
> see above

Does that mean I should use the debian scripts if I want to distribute the cached binaries?

> > >  When is which one used? Is it possible to disable the global cache in favor of the user one? The readme talks about "precomputed" for `/var` and "user computed" for `~/.sympow`. Does that mean runtime write access to `VARPREFIX` is not actually necessary?
> > > 
> > > Just cleanup /usr/share/sympow/datafiles/ to let the  possibility to superuser to provide system wide data.
> > 
> > Even after deleting that, sympow still gives a warning about not being able to write to /var/cache/sympow.
> 
> so it is a warning (an not an ERROR message followed but an exit(-1)): I would consider it as a feature but not as a bug.
> In fact, a couple of checks are performed to detect a corrupted folder set up and avoid surprises . 

I would disagree. If I understand correctly the shared cache is only really useful in the nowadays nieche case where a lot of users use the same sympow instance on one PC. And even then it will not have a huge impact because computing power is usually sufficient. Not having the shared state makes things easier to reason about and in general global state is annoying to deal with for packaging.

> The bug is in the installation process:
> the correct privileges must be encoded in Configure : I will try to fix this the next week-end .

What do you mean by that?

> And in the README.md file: I should document better this part.
> 
> For now, to silent this warning, just set the right privilege or pass the option  -quiet : no will be write if /usr/share/sympow/datafiles is empty .

Does `-quiet` have any other effects besides surpressing that message?

> Let me know if you think that a mechanism must be implemented to avoid this warning message.

To make my motivations mroe clear: In nix, every package lives in an immutable subfolder of /nix/store after installation. The name of that subfolder contains a hash describing the recipe used to build the package and all its dependencies. That has a lot of advantages. Two relevant examples:

- packages can be installed with user privileges. That is because installing a package only downlaods a couple of archives and unpacks that at /nix/store. It does not in any way affect other users. The issue with /var here is that we'd need superuser privileges at install time. Also nix doesn't even have the concept of install time scripts, so I'd have to do some ugly hack like creating a wrapper for sympow that sets up the /var folder on first use.

- multiple versions of a package can be installed side-by-side. For example different users may have different versions of sympow. Again, global state is difficult in this situation.

So if it is not strictly necessary, I'd like to either

- avoid the global cache and use the user cache instead or

- pre-populate the cache at build time. The cache dir would then be read-only at runtime.

It sounds like currently I can kind of do the first option by writing a wrapper for sympow that always passes the `-quiet` option. Of course it would be nicer to just disable the shared state through a ./Configure option and even nicer to use option two instead.

Am I misunderstanding this?

Thank you again for not only taking the time to improve the state of the singular package, but also patiently explaining the details to me :)


---

Comment by vdelecroix created at 2018-08-03 19:20:18

update milestone 8.3 -> 8.4


---

Comment by @timokau created at 2018-08-26 20:33:10

`@`gh-jgmbenoit ping


---

Comment by @jgmbenoit created at 2018-08-27 03:58:24

pong !

Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.

You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.

((Is it that hard to read C source file ?))


---

Comment by @timokau created at 2018-08-27 10:21:00

Replying to [comment:43 gh-jgmbenoit]:
> Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.
> 
> You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.

That is the only blocking issue, but it would still be better to be able to pre-compute the global cache at build time instead of lazily computing it at runtime. You didn't respond to all of my questions, which is understandable considering what a monster of message that was. So I'll summarize:

- could the global cache reasonably be pre-computed at build time?
- does sympow without a global cache behave exatly as usual, just computing the cache per-user instead?
- if the debian/adhoc/job file to pre-compute some data is recommended, I would prefer if you would include it in sympow proper. However I understand your reservations about touching the math.

> ((Is it that hard to read C source file ?))

Honestly yes, the sympow code is very hard to read for me. Its a mix of very non-standard formatting, a lack of comments and my limited C and domain knowledge. That is why I'm glad that you have taken up the maintenance.

I'll try a `-quiet` wrapper for now.


---

Comment by @jgmbenoit created at 2018-08-27 11:03:41

Replying to [comment:44 gh-timokau]:
> Replying to [comment:43 gh-jgmbenoit]:
> > Does -quiet have any other effects besides surpressing that message?  NO. Once again, the custom GNU/Linux behaviour are followed.
> > 
> > You only issue is that there is a Warning message: I guess it is not necessary to write a wrapper for that. Second, I guess sympow is mainly used by Sage, which acts as wrapper.
> 
> That is the only blocking issue, but it would still be better to be able to pre-compute the global cache at build time instead of lazily computing it at runtime. You didn't respond to all of my questions, which is understandable considering what a monster of message that was. So I'll summarize:
> 
> - could the global cache reasonably be pre-computed at build time?

No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.

> - does sympow without a global cache behave exatly as usual, just computing the cache per-user instead?

Yes. 

> - if the debian/adhoc/job file to pre-compute some data is recommended, I would prefer if you would include it in sympow proper. However I understand your reservations about touching the math.

I plan to incorporated them latter: the issue is now time.

> 
> > ((Is it that hard to read C source file ?))
> 
> Honestly yes, the sympow code is very hard to read for me. Its a mix of very non-standard formatting, a lack of comments and my limited C and domain knowledge. That is why I'm glad that you have taken up the maintenance.
> 
> I'll try a `-quiet` wrapper for now.

I would forget it and spend my time else where.

I plan to change the verbosity level of this message (once I have time before me).

Jerome


---

Comment by @timokau created at 2018-08-27 14:44:16

Replying to [comment:45 gh-jgmbenoit]:
> Replying to [comment:44 gh-timokau]:
> > - could the global cache reasonably be pre-computed at build time?
> 
> No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.

I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.

> > I'll try a `-quiet` wrapper for now.
> 
> I would forget it and spend my time else where.
> 
> I plan to change the verbosity level of this message (once I have time before me).

Well it seems to break sages parsing, so I'll need to add that wrapper. After that sages tests still fail. I'm now trying to update sages spkg first to find out if thats a quirk with nix's build system or a parsing issue.
However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:


```
import sys
import platform

if sys.byteorder == "little":
    endian = "le"
else:
    endian = "be"

bits = platform.architecture()[0][:-3]

# for example "le64" or "be32"
print(endian + bits)
```


Is that correct?


---

Comment by @jgmbenoit created at 2018-08-27 15:35:36

Replying to [comment:46 gh-timokau]:
> Replying to [comment:45 gh-jgmbenoit]:
> > Replying to [comment:44 gh-timokau]:
> > > - could the global cache reasonably be pre-computed at build time?
> > 
> > No for security reasons: those files are binary files: for security matter you want to avoid to distribute binary files. Anyway, their computation time is very short: the hard part is contained in the corresponding clear data.
> 
> I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.

the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,
namely as a suspicious file.

On my box:

$ file ~/.sympow/datafiles/le64/P014M.bin

gives

$ /home/jgmb/.sympow/datafiles/le64/P014M.bin: data

For any regular binary files, file(1) should be able to identified.


> 
> > > I'll try a `-quiet` wrapper for now.
> > 
> > I would forget it and spend my time else where.
> > 
> > I plan to change the verbosity level of this message (once I have time before me).
> 
> Well it seems to break sages parsing, so I'll need to add that wrapper. After that sages tests still fail. I'm now trying to update sages spkg first to find out if thats a quirk with nix's build system or a parsing issue.


This is indeed an issue.


> However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:
> 
> {{{
> import sys
> import platform
> 
> if sys.byteorder == "little":
>     endian = "le"
> else:
>     endian = "be"
> 
> bits = platform.architecture()[0][:-3]
> 
> # for example "le64" or "be32"
> print(endian + bits)
> }}}
> 
> Is that correct?


it looks correct.


---

Comment by @timokau created at 2018-08-27 23:26:54

New commits:


---

Comment by git created at 2018-08-27 23:27:49

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by @timokau created at 2018-08-27 23:29:09

New commits:


---

Comment by @timokau created at 2018-08-27 23:29:09

Changing status from new to needs_review.


---

Comment by @timokau created at 2018-08-27 23:31:10

Replying to [comment:47 gh-jgmbenoit]:
> Replying to [comment:46 gh-timokau]:
> > I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.
> 
> the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,
> namely as a suspicious file.

Why is a binary data file any more suspicious than a binary executable?

> 
> > However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:
> > 
[...]
> 
> 
> it looks correct.

I've implemented it. Its really a shame sagemath doesn't provide autotools by default.


---

Comment by @timokau created at 2018-08-27 23:32:42

Points for reviewers to focus on I'm not sure about:

- this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.
- it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.


---

Comment by @jgmbenoit created at 2018-08-28 03:34:19

Replying to [comment:51 gh-timokau]:
> Replying to [comment:47 gh-jgmbenoit]:
> > Replying to [comment:46 gh-timokau]:
> > > I don't understand what you mean. The `sympow` binary is also a distributed binary file. The data would be computed in the build script just as the executables would be. Any user could verify that by building it themselves.
> > 
> > the data are stored as binary, so the data binary file can be detected as an arbitrary binary file,
> > namely as a suspicious file.
> 
> Why is a binary data file any more suspicious than a binary executable?

A binary executable is recognized as such by file(1): so it recognisable as such.


> 
> > 
> > > However while packaging the spkg I've hit another issue: the `./Configure` script now relies on autotools to generate the endian tuple. autotools apparently is an "experimental" package that currently isn't included in the sage distribution by default. I would replace it by this python script:
> > > 
> [...]
> > 
> > 
> > it looks correct.
> 
> I've implemented it. Its really a shame sagemath doesn't provide autotools by default.


---

Comment by @timokau created at 2018-08-28 16:34:15

Replying to [comment:53 gh-jgmbenoit]:
> Replying to [comment:51 gh-timokau]:
> > Why is a binary data file any more suspicious than a binary executable?
> 
> A binary executable is recognized as such by file(1): so it recognisable as such.

Why does that matter? I don't understand why an executable that is recognized as such is any less suspicious or security relevant than a binary data file. The executable is arguably more security relevant.


---

Comment by embray created at 2019-03-25 10:56:15

Ticket retargeted after milestone closed (if you don't believe this ticket is appropriate for the Sage 8.8 release please retarget manually)


---

Comment by embray created at 2019-07-03 11:37:56

Moving tickets from the Sage 8.8 milestone that have been actively worked on in the last six months to the next release milestone (optimistically).


---

Comment by embray created at 2019-12-30 14:48:17

Ticket retargeted after milestone closed


---

Comment by mkoeppe created at 2020-04-01 13:46:04

Replying to [comment:51 gh-timokau]:
> I've implemented it. Its really a shame sagemath doesn't provide autotools by default.

Autotools are supposed to be run by maintainers at "make dist" time, not at installation time


---

Comment by mkoeppe created at 2020-04-01 13:49:13

What are other distributions doing about sympow? 

Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true


---

Comment by mkoeppe created at 2020-04-01 14:34:11

Changing status from needs_review to needs_work.


---

Comment by @jgmbenoit created at 2020-04-01 15:15:43

Replying to [comment:60 mkoeppe]:
> Replying to [comment:51 gh-timokau]:
> > I've implemented it. Its really a shame sagemath doesn't provide autotools by default.
> 
> Autotools are supposed to be run by maintainers at "make dist" time, not at installation time 

This is true.

I have just tried to refresh my memory about:
basically the Autotools part jsut run some c code: so I guess that we can replace it with a C source.


---

Comment by @jgmbenoit created at 2020-04-01 15:22:59

Replying to [comment:61 mkoeppe]:
> What are other distributions doing about sympow? 

What do you mean ?

> 
> Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true

I have just seen the merge request on gitlab. Next week I might be on vacation, I will a look then.


---

Comment by mkoeppe created at 2020-04-01 15:30:39

Replying to [comment:64 gh-jgmbenoit]:
> Replying to [comment:61 mkoeppe]:
> > What are other distributions doing about sympow? 

conda-forge, arch, etc. are packaging sage and the packages they need. Just wondering whether they are using the fork, and how they have adjusted the sage interface and doctests if necessary.


---

Comment by isuruf created at 2020-04-01 15:34:58

`conda-forge` switched to debian's fork more than a year ago.


---

Comment by @timokau created at 2020-04-01 15:46:08

nixpkgs is using the fork as well. I've switched it over here: https://github.com/NixOS/nixpkgs/commit/5e58c5f900e51c4dd89de8a4518c5bb13581f3c6

No patches to sage were necessary to pass the test suite. I still added a patch that puts the cache directory under the `.sage` directory though: https://github.com/NixOS/nixpkgs/commit/9ef44b34316cb47c0bda49f05c57ca2ea6c96816


---

Comment by mkoeppe created at 2020-04-01 15:53:44

Anything missing on this ticket other than rebasing?


---

Comment by @timokau created at 2020-04-01 17:15:27

Replying to [comment:52 gh-timokau]:
> Points for reviewers to focus on I'm not sure about:
> 
> - this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.
> - it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.

This is probably still relevant. Other than that, I don't remember. I won't continue working on this for now, so anybody else should feel free to pick this up.


---

Comment by @jgmbenoit created at 2020-04-17 06:38:30

Replying to [comment:63 gh-jgmbenoit]:
> Replying to [comment:60 mkoeppe]:
> > Replying to [comment:51 gh-timokau]:
> > > I've implemented it. Its really a shame sagemath doesn't provide autotools by default.
> > 
> > Autotools are supposed to be run by maintainers at "make dist" time, not at installation time 
> 
> This is true.
> 
> I have just tried to refresh my memory about:
> basically the Autotools part jsut run some c code: so I guess that we can replace it with a C source.

In version 2.023.6, the autotools dependency was discarded: the endianess is now determine via a C program. Please check it on exotic architectures if you can, and let me know if any issue arises.


---

Comment by @jgmbenoit created at 2020-04-17 06:41:01

Replying to [comment:64 gh-jgmbenoit]:
> Replying to [comment:61 mkoeppe]:
> > What are other distributions doing about sympow? 
> 
> What do you mean ?
> 
> > 
> > Running into compilation errors on Fedora-32 (gcc 10) - https://github.com/mkoeppe/sage/runs/546662577?check_suite_focus=true
> 
> I have just seen the merge request on gitlab. Next week I might be on vacation, I will a look then.
I applied the patch in version 2.023.6 .


---

Comment by mjo created at 2020-05-12 19:05:35

Replying to [comment:69 gh-timokau]:
> Replying to [comment:52 gh-timokau]:
> > Points for reviewers to focus on I'm not sure about:
> > 
> > - this creates a `SAGE_LOCAL/var/cache` folder. There is no precedence for that.
> > - it also creates a `.sympow` folder in the user's home directory at runtime. Not sure if that was already the case before.
> 
> This is probably still relevant. Other than that, I don't remember. I won't continue working on this for now, so anybody else should feel free to pick this up.


If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do. And given that this is binary data and the quality of the code, I'm not sure that it's wise to share the cache among a "sympow" group anywhere else. So FWIW I would leave it at the default.


---

Comment by mjo created at 2020-05-15 14:12:55

Replying to [comment:74 mjo]:
> 
> If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.

Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`. I'm not sure what to do about that one; a wrapper or launcher script (that overrides that directory and uses something under `$HOME`) is the only way I've been able to make it work so far. More details eventually on https://gitlab.com/rezozer/forks/sympow/-/issues/3


---

Comment by mjo created at 2020-05-16 12:46:31

Replying to [comment:75 mjo]:
> Replying to [comment:74 mjo]:
> > 
> > If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.
> 
> Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`.

This is true, but turns out to not be a problem. The fork tries to use the directory under `VARPREFIX`, and if that doesn't work, it falls back to using `$HOME/.sympow` for that data as well. The only "problem" with that is that a warning is displayed to the user if he runs sympow by hand.

So, the sage SPKG should leave `VARPREFIX` alone. In Gentoo I'm going to patch out the expected warning (see the gitlab issue), and that may make sense for sage as well since `/var` will not generally be writable by whoever is running sage. The data will ultimately get stored under `$HOME/.sympow`, and that's what we want in the SPKG.


---

Comment by @timokau created at 2020-05-18 16:26:15

Replying to [comment:75 mjo]:
> Replying to [comment:74 mjo]:
> > 
> > If sage-the-distribution still supports multi-user installs, that location will generally not be writable. The default of `$HOME/.sympow` is probably the best you can do.
> 
> Actually, there are two different cache directories to worry about. The one that defaults to `$HOME/.sympow` is different from the one that goes under `VARPREFIX`. I'm not sure what to do about that one; a wrapper or launcher script (that overrides that directory and uses something under `$HOME`) is the only way I've been able to make it work so far. More details eventually on https://gitlab.com/rezozer/forks/sympow/-/issues/3

There was already quite a bit of discussion about this issue here, see the posts following this message: #3360#comment:35

For nixpkgs, I decided to use a wrapper instead of a patch: https://github.com/NixOS/nixpkgs/blob/962f93c46b1eaaedbc118c06adfd439ce341a0db/pkgs/development/libraries/science/math/sympow/default.nix#L44


---

Comment by mkoeppe created at 2020-06-14 20:00:38

Changing priority from major to critical.


---

Comment by git created at 2020-07-05 17:47:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2020-07-05 17:51:23

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2020-07-05 17:53:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mkoeppe created at 2020-07-05 17:56:38

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-07-05 17:57:08

Builds on macOS, haven't tested anything else yet.


---

Comment by git created at 2020-07-05 18:34:30

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mkoeppe created at 2020-07-06 02:53:52

Tests run at https://github.com/mkoeppe/sage/actions/runs/158805080


---

Comment by mkoeppe created at 2020-07-06 12:31:23


```
  [sympow-2.023.6]     File "/usr/lib/python3.6/urllib/request.py", line 1952, in http_error
  [sympow-2.023.6]       return self.http_error_default(url, fp, errcode, errmsg, headers)
  [sympow-2.023.6]     File "/cygdrive/d/a/sage/sage/build/bin/../sage_bootstrap/download/transfer.py", line 107, in http_error_default
  [sympow-2.023.6]       raise DownloadError(errcode, errmsg, url)
  [sympow-2.023.6]   OSError: [Errno socket error] [Errno 403] Forbidden: '//gitlab.com/rezozer/forks/sympow/-/archive/v2.023.6/sympow-v2.023.6.tar.gz'
  [sympow-2.023.6]   
```



---

Comment by dimpase created at 2020-07-06 14:29:01

Replying to [comment:92 mkoeppe]:
> {{{
>   [sympow-2.023.6]     File "/usr/lib/python3.6/urllib/request.py", line 1952, in http_error
>   [sympow-2.023.6]       return self.http_error_default(url, fp, errcode, errmsg, headers)
>   [sympow-2.023.6]     File "/cygdrive/d/a/sage/sage/build/bin/../sage_bootstrap/download/transfer.py", line 107, in http_error_default
>   [sympow-2.023.6]       raise DownloadError(errcode, errmsg, url)
>   [sympow-2.023.6]   OSError: [Errno socket error] [Errno 403] Forbidden: '//gitlab.com/rezozer/forks/sympow/-/archive/v2.023.6/sympow-v2.023.6.tar.gz'
>   [sympow-2.023.6]   
> }}}

the link works from the browser for me.


---

Comment by mkoeppe created at 2020-07-06 21:18:00

https://gitlab.com/gitlab-org/gitlab-runner/-/issues/3230


---

Comment by mkoeppe created at 2020-07-07 03:17:14

Tests using a temporary github url at https://github.com/mkoeppe/sage/actions/runs/160116395


---

Comment by mkoeppe created at 2020-07-07 16:07:59

`ubuntu-trusty-minimal` (https://github.com/mkoeppe/sage/runs/844024596):

```
gcc version 4.8.4 (Ubuntu 4.8.4-2ubuntu1~14.04.4) 
****************************************************
Package 'sympow' is currently not installed
No legacy uninstaller found for 'sympow'; nothing to do
CFLAGS for SYMPOW: -fno-fast-math -mfpmath=sse -Dx86 -ffp-contract=on 
The double precision of your FPU is 53 bits.
CFLAGS for SYMPOW:  -std=gnu11 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH 
The double precision of your FPU is 53 bits.
config/endiantuple.c:6:2: error: #error "require C11 or higher"
 #error "require C11 or higher"
  ^
Error: the command below failed:
gcc config/endiantuple.c -o config/endiantuple
********************************************************************************
Error configuring SYMPOW
```

Likewise on `debian-jessie-minimal`, `linuxmint-17-minimal`.


---

Comment by mkoeppe created at 2020-07-07 16:08:07

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2020-07-08 18:30:08

This is now https://gitlab.com/rezozer/forks/sympow/-/issues/4


---

Comment by git created at 2020-07-08 18:31:58

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2020-07-08 18:34:45

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by git created at 2020-07-08 19:07:57

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mkoeppe created at 2020-07-08 19:11:00

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-07-08 19:12:05

Tests run at https://github.com/mkoeppe/sage/pull/41/checks?check_run_id=851182060


---

Comment by mkoeppe created at 2020-07-09 18:13:43

(comment for the wrong ticket)


---

Comment by mkoeppe created at 2020-07-09 18:13:58

Changing status from needs_review to needs_work.


---

Comment by mkoeppe created at 2020-07-09 18:14:46

Changing status from needs_work to needs_review.


---

Comment by mkoeppe created at 2020-07-09 18:14:46

Tests look OK. Ready for review


---

Comment by dimpase created at 2020-07-09 20:20:31

do you test with gcc10?


---

Comment by mkoeppe created at 2020-07-09 20:22:09

Haven't yet. I trust upstream there


---

Comment by mkoeppe created at 2020-07-09 20:24:43

We can reuse #30067 as a GCC 10 upgrade test ticket


---

Comment by mkoeppe created at 2020-07-09 20:25:27

or #29456


---

Comment by git created at 2020-07-10 07:50:42

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mkoeppe created at 2020-07-10 17:49:32

Replying to [comment:111 mkoeppe]:
> or #29456

GCC10 testing is happening on #29456 now.


---

Comment by mkoeppe created at 2020-07-10 17:49:57

But this ticket does not need to wait for it -- ready for review.


---

Comment by mkoeppe created at 2020-07-14 22:35:14

`sympow` builds OK on all platforms (including with gcc 10 for `fedora-32-minimal`) at https://github.com/mkoeppe/sage/actions/runs/168165380

However, I see many test failures in sagelib that seem related to `sympow` in `fedora-32-standard` (https://github.com/mkoeppe/sage/runs/867731204) -- where `sympow` comes from the system after #29673!

```
**********************************************************************
File "src/sage/lfunctions/sympow.py", line 225, in sage.lfunctions.sympow.Sympow.modular_degree
Failed example:
    sympow.modular_degree(EllipticCurve('11a'))
Exception raised:
    Traceback (most recent call last):
      File "/sage/local/lib/python3.7/site-packages/sage/doctest/forker.py", line 707, in _run
        self.compile_and_execute(example, compiler, test.globs)
      File "/sage/local/lib/python3.7/site-packages/sage/doctest/forker.py", line 1132, in compile_and_execute
        exec(compiled, globs)
      File "<doctest sage.lfunctions.sympow.Sympow.modular_degree[0]>", line 1, in <module>
        sympow.modular_degree(EllipticCurve('11a'))
      File "/sage/local/lib/python3.7/site-packages/sage/lfunctions/sympow.py", line 241, in modular_degree
        raise RuntimeError("failed to compute modular degree")
    RuntimeError: failed to compute modular degree
----------------------------------------------------------------------
sage -t src/sage/lfunctions/sympow.py  # 10 doctests failed
sage -t src/sage/modular/abvar/abvar.py  # 1 doctest failed
sage -t src/sage/modular/hecke/submodule.py  # 1 doctest failed
sage -t src/sage/schemes/elliptic_curves/ell_rational_field.py  # 14 doctests failed
----------------------------------------------------------------------
```



---

Comment by mkoeppe created at 2020-07-14 22:48:11

Replying to [comment:116 mkoeppe]:
> I see many test failures in sagelib that seem related to `sympow` in `fedora-32-standard` (https://github.com/mkoeppe/sage/runs/867731204) -- where `sympow` comes from the system after #29673!

I have opened #30147 (Fix `spkg-configure.m4` for `sympow`) for this.

The present ticket is ready for review.


---

Comment by dimpase created at 2020-07-17 22:59:23

lgtm


---

Comment by dimpase created at 2020-07-17 22:59:23

Changing status from needs_review to positive_review.


---

Comment by mkoeppe created at 2020-07-17 23:35:38

Thanks.


---

Comment by vbraun created at 2020-07-22 22:39:25

I'm getting lots of errors of the form:

```
**********************************************************************
File "src/sage/schemes/elliptic_curves/ell_rational_field.py", line 3845, in sage.schemes.elliptic_curves.ell_rational_field.EllipticCurve_rational_field.congruence_number
Failed example:
    E.modular_degree()
Expected:
    16
Got:
    **WARNING** failed to create data bin package cache folder /home/buildbot/slave/sage_git/build/local/var/cache/sympow/datafiles/le64
    16
**********************************************************************
```



---

Comment by vbraun created at 2020-07-22 22:39:25

Changing status from positive_review to needs_work.


---

Comment by mkoeppe created at 2020-07-22 22:42:50

on what machine


---

Comment by mjo created at 2020-07-23 00:17:32

That "error" is expected, in general, and shouldn't be output at the default verbosity (in my opinion). I already patched it:

https://gitweb.gentoo.org/repo/gentoo.git/plain/sci-mathematics/sympow/files/sympow-2.023.6-no-pkgdatafilesbindir-warnings.patch

The discussion is here,

https://gitlab.com/rezozer/forks/sympow/-/issues/3

if you want to ask upstream about including it.


---

Comment by mkoeppe created at 2020-07-23 00:56:40

Let's just include your patch on this ticket


---

Comment by git created at 2020-07-23 01:06:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mkoeppe created at 2020-07-23 01:06:40

Changing status from needs_work to needs_review.


---

Comment by dimpase created at 2020-07-26 22:22:00

over to the bots


---

Comment by dimpase created at 2020-07-26 22:22:00

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2020-07-29 19:55:43

Changing status from positive_review to needs_work.


---

Comment by vbraun created at 2020-07-29 19:55:43


```
make[5]: Entering directory '/home/release/Sage/local/var/tmp/sage/build/sympow-2.023.6/src'
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o fpu.o fpu.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o analrank.o analrank.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o analytic.o analytic.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o compute.o compute.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o compute2.o compute2.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o help.o help.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o conductors.o conductors.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o disk.o disk.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap.o ec_ap.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap_bsgs.o ec_ap_bsgs.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o ec_ap_large.o ec_ap_large.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o eulerfactors.o eulerfactors.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o factor.o factor.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o generate.o generate.c
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o init_curve.o init_curve.c
generate.c: In function 'new_data':
generate.c:234:32: error: 'GP' undeclared (first use in this function)
  234 |  execlp(SH,SH,newdatascript,SH,GP,ARGS,NULL);}
      |                                ^~
generate.c:234:32: note: each undeclared identifier is reported only once for each function it appears in
gcc   -O3  -std=gnu17 -fno-fast-math -mfpmath=sse -ffp-contract=on -DFPUCONTROLH   -c -o main.o main.c
make[5]: *** [Makefile:39: generate.o] Error 1
```



---

Comment by mkoeppe created at 2020-07-29 20:02:08

on what machine


---

Comment by git created at 2020-07-29 21:34:10

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mkoeppe created at 2020-07-29 21:35:21

Tests run at https://github.com/mkoeppe/sage/actions/runs/187726088


---

Comment by mkoeppe created at 2020-07-30 17:21:55

Builds correctly on all platforms.


---

Comment by mkoeppe created at 2020-07-30 17:21:55

Changing status from needs_work to positive_review.


---

Comment by vbraun created at 2020-07-30 23:25:19

Fedora 32 x86_64 for the record


---

Comment by mkoeppe created at 2020-07-31 00:14:27

Replying to [comment:133 vbraun]:
> Fedora 32 x86_64 for the record
Thanks. Works fine on both `fedora-32-minimal` and `fedora-32-standard` (see above link). Would need more information about the system where it fails.


---

Comment by vbraun created at 2020-08-03 22:59:15

Still doesn't work. My build log has a

```
which: no gp in (/home/release/Sage/build/bin:/home/release/Sage/src/bin:/home/release/Sage/local/bin:/home/release/Sage/build/bin:/home/release/Sage/src/bin:/home/release/Sage/local/bin:/home/release/.local/bin:/home/release/opt/bin:/usr/share/Modules/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/release/.composer/vendor/bin)
*WARNING*: Could not find gp --- will not be able to build new_data
```

thats not in yours;  Build race with pari/gp? Seems like this would explain the `error: 'GP' undeclared`


---

Comment by vbraun created at 2020-08-03 22:59:15

Changing status from positive_review to needs_work.


---

Comment by mkoeppe created at 2020-08-03 23:02:44

Yes, seems like we may need to add pari as a dependency


---

Comment by git created at 2020-08-03 23:04:53

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by mkoeppe created at 2020-08-03 23:05:17

Changing status from needs_work to needs_review.


---

Comment by vbraun created at 2020-08-07 19:05:26

Resolution: fixed
