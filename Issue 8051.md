# Issue 8051: SageNB 0.7

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-24 18:53:29

Assignee: was

New spkg.


---

Comment by mpatel created at 2010-01-25 04:40:15

If it's possible, I'd like to get into 0.7.1 as many of the now remaining "needs review" tickets as we can.  I'm rebasing these now.


---

Comment by mpatel created at 2010-01-25 04:40:15

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-25 07:35:06

Replying to [comment:2 mpatel]:
> If it's possible, I'd like to get into 0.7.1 as many of the now remaining "needs review" tickets as we can.  I'm rebasing these now.
Here's a possible queue:

```
trac_7784-hgignore_update.patch
trac_5712-interrupt-notification.5.patch
trac_6069-missing_pub_ws.2.patch
trac_8038-email_plus_addressing_v2.patch
trac_7506-notebook_object-documentation.2.patch
trac_693-spawn_notebook.3.patch
trac_5177-delete-cell-dirs.3.patch
```



---

Comment by mpatel created at 2010-01-27 05:40:28

Changing assignee from was to mpatel.


---

Comment by mpatel created at 2010-01-30 05:50:21

I just noticed that long `'eval'` docstrings are truncated.  I'll add a reviewer patch to #3083.


---

Comment by robert.marik created at 2010-01-31 20:14:22

All tickets got positive review and have been merged. So what should be reviewed in this ticket?

I installed the spkg, seems to work fine (but I did not test everything), is this enough to give positive review?

btw: the link from description "says" http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg but it points to http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.1.spkg


---

Comment by mvngu created at 2010-01-31 23:12:09

Replying to [comment:9 robert.marik]:
> All tickets got positive review and have been merged. So what should be reviewed in this ticket?

You need to make sure that you can successfully install the updated spkg.





> I installed the spkg, seems to work fine (but I did not test everything), is this enough to give positive review?

I would say, all doctests must pass as well. In any case, if you can't run all doctests after installing the updated spkg, I can do that. A correct link to the updated spkg is

http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.2.spkg


---

Comment by mvngu created at 2010-01-31 23:25:37

I don't understand why the spkg is not managed by Mercurial:

```
[mvngu`@`mod sagenb-0.7.2]$ hg st
abort: There is no Mercurial repository here (.hg not found)!
```

The file `spkg-install` should have its executable bits on:

```
[mvngu`@`mod sagenb-0.7.2]$ ls -g spkg-install
-rw-r--r-- 1 mvngu 348 2010-01-30 16:37 spkg-install
```

And `SPKG.txt` is very sketchy about update details.


---

Comment by mpatel created at 2010-01-31 23:29:54

I suggest

 * Checking that the package installs and the notebook runs.
 * Checking the repo for unchecked-in changes, queued patches, etc.
 * Checking that the claimed merged tickets appear in `hg log`.
 * Running the doctests: `sage -t -sagenb`.

Ideally, you should run the SageNB Selenium tests, too.  But they require special extra setup.  I'll make simplifying that setup a separate ticket.

Thanks for pointing out the link error.  I've updated it.


---

Comment by mpatel created at 2010-01-31 23:34:38

The repository is in `sagenb-0.7.2/src/sagenb`.  We auto-generate the package with `sagenb-0.7.2/src/sagenb/spkg-dist`.

I suggest that I make a separate ticket to update SPKG.txt.

See #7784 about

```
$ hg stat
? release_notes.txt
? setup.cfg
```



---

Comment by mpatel created at 2010-01-31 23:38:54

Replying to [comment:13 mpatel]:
> I suggest that I make a separate ticket to update SPKG.txt.

Or I can do this here later today.


---

Comment by mpatel created at 2010-01-31 23:39:58

I'll fix the `spkg-install` problem, too.


---

Comment by mpatel created at 2010-02-01 03:44:55

Please see #7784 for the changes.  If/when that ticket gets a positive review, I'll create SageNB 0.7.3 and post it here.


---

Comment by mpatel created at 2010-02-01 04:34:56

By the way, it seems that for the near future, I may be the only very active SageNB developer.  I'd be _very_ happy to be proved (proven?) wrong!  There are many tasks to complete --- there are several cool new notebook features to implement.  It's not possible for me to cover them all, and I'd like to avoid stalling ongoing development.

To this end, I'll try to make it easier for Sage developers to review notebook tickets or make other contributions.  Please let me know what would help.  For example, I can make experimental spkgs that contain the latest patches in the queue.  Those who wish just to test the cumulative changes can install the package with `sage -f sagenb-*.spkg`.  But reviewers can also open the spkg, pop / push patches, and comment on specific ticket(s).  In either case, we'll get useful information about how the notebook behaves in a wider gamut of browser-OS combinations.  We'll also get more end user feedback.


---

Comment by acleone created at 2010-02-01 05:43:38

Experimental spkgs would be good.  I think the best way to get more testing/review would be a good guide to applying patches, testing spkgs, etc.

Is there a mailing list or wiki page for coordinating development effort?


---

Comment by mvngu created at 2010-02-01 05:54:43

Replying to [comment:18 acleone]:
> Is there a mailing list or wiki page for coordinating development effort?

A relevant mailing is [sage-devel](http://groups.google.com/group/sage-devel). Most of the time, that list receives high volume traffic on development discussion. For coordinating release effort, the [sage-release](http://groups.google.com/group/sage-release) mailing list is appropriate. Some effort is underway to expand the Sage documentation with information to help beginners getting started with Sage development. The relevant tickets are:

 1. #8108: Expand the Sage Developer Guide for newcomers
 1. #6987: reorganize section on producing patches with Mercurial
 1. #8079: Better documentation for patching spgk's
 1. #8104: developer's guide for making spkgs should specify that patches need to be version controlled
 1. #3882: explain in the programming guide why spkg source patches should be applied by copying entire files
 1. #7944: update Developers' Guide to reflect new process for working on tickets


---

Comment by mpatel created at 2010-02-01 05:58:46

Both [sage-devel](http://groups.google.com/group/sage-devel) and [sage-notebook](http://groups.google.com/group/sage-notebook) are good places.  I suppose we should move this discussion to sage-notebook.

One source for ideas is [SageTasks](http://wiki.sagemath.org/devel/SageTasks), but it may be getting old.

Addendum: Of course, we should also try to attract energetic developers who'd contribute fresh ideas, techniques, etc., to the SageNB project.


---

Comment by mpatel created at 2010-02-01 06:10:45

While I'm here, I'd also like to suggest using `alpha.sagenb.org` or creating `ouch.sagenb.org` to test a bleeding-edge SageNB.  This could be a notebook with all positively reviewed patches applied or, more interestingly, an experimental spkg.

We could also set up a corresponding repository, different from http://boxen.math.washington.edu:8100/, to which to push experimental features and from which to backport what works.  A potential problem here is that Mercurial changesets are immutable.  But we might not care about keeping the history of this repository clean.

Just some thoughts.


---

Comment by robert.marik created at 2010-02-02 18:49:36

Installs fine, works fine with jsmath image fonts, tests paseed, cannot check the rest, since I have probably old hg in my Debian Linux

```
sage`@`um-bc107:~/sagenb-0.7.2/src/sagenb$ hg log
abort: requirement 'fncache' not supported!
sage`@`um-bc107:~/sagenb-0.7.2/src/sagenb$ hg status
abort: requirement 'fncache' not supported!
```


Can someone finish testing? I think that this is very important ticket and nice sage notebook is important to attract new users (and new developers). Thank you for working on it.


---

Comment by mpatel created at 2010-02-02 22:02:32

If you have a spare moment, please review #7784, which is "blocking" this ticket.

You can use `sage -hg` instead of `hg`.


---

Comment by mpatel created at 2010-02-03 02:31:27

Minh -- Even with #8036, it's very likely the PDF reference manual won't build with this spkg, owing to #7249's Unicode doctests.  I'm not sure what we should do about this.


---

Comment by mvngu created at 2010-02-03 02:36:27

Replying to [comment:24 mpatel]:
> Minh -- Even with #8036, it's very likely the PDF reference manual won't build with this spkg, owing to #7249's Unicode doctests.  I'm not sure what we should do about this.

The release deadline for Sage 4.3.2 is Saturday 06th February 2010, which means there's not much time for sorting out failures when building the PDF version of the reference manual. I think [sagenb-0.7.3.spkg](http://boxen.math.washington.edu/home/mpatel/trac/8051/sagenb-0.7.3.spkg) needs to wait for after Sage 4.3.2 is done.


---

Comment by mpatel created at 2010-02-03 09:28:49

Please see #8167.  If/when that ticket gets a positive review, I'll make 0.7.4...


---

Comment by mpatel created at 2010-02-05 00:59:37

I've posted SageNB 0.7.4 for review.


---

Comment by robert.marik created at 2010-02-05 08:34:36

Thanks for the update. But now I have too many sage notebooks

```
[marik`@`um-bc107 ../lib/python/site-packages]$ pwd
/opt/sage/local/lib/python/site-packages
[marik`@`um-bc107 ../lib/python/site-packages]$ ls -ld sagenb*
drwxr-xr-x 4 marik marik 4096  1. úno 17.16 sagenb-0.6-py2.6.egg
drwxr-xr-x 4 marik marik 4096  2. úno 19.33 sagenb-0.7.2-py2.6.egg
drwxr-xr-x 4 marik marik 4096  5. úno 09.13 sagenb-0.7.4-py2.6.egg
```


How do I know, which one is actually used? Jsmath image fonts failed to install intro correct directory. Should the old sage notebook be removed, first? Should this be tested on fresh install only?


---

Comment by mpatel created at 2010-02-05 09:20:18

We install the sagenb package with [setuptools](http://peak.telecommunity.com/DevCenter/setuptools) ([PyPI](http://pypi.python.org/pypi/setuptools)), which updates `SAGE_LOCAL/lib/python/site-packages/easy-install.pth`.  This file contains paths prepended to `sys.path` on startup.

You can query the installed version with


```python
sage: from sagenb.misc.misc import SAGENB_VERSION
sage: SAGENB_VERSION
```

which is essentially


```python
sage: from pkg_resources import Requirement, working_set
sage: w = working_set.find(Requirement.parse('sagenb'))
sage: w.version
```

Moreover, `w.location` gives the install directory.

I'm checking the fonts now...


---

Comment by acleone created at 2010-02-05 09:35:47

sagenb 0.7.4 installed correctly for me.  All doc and selenium tests passed.  Still problems building the PDF docs but Ihaven't applied any of the unicode patches (using vanilla sage-4.3.2.alpha1).


---

Comment by mpatel created at 2010-02-05 09:42:46

On the fonts: What is the output of

```sh
egrep "Copying jsMath image"\|"Installed.*sagenb" $SAGE_ROOT/install.log 
```

?


---

Comment by mpatel created at 2010-02-05 10:24:01

Replying to [comment:30 acleone]:
> sagenb 0.7.4 installed correctly for me.  All doc and selenium tests passed.  Still problems building the PDF docs but Ihaven't applied any of the unicode patches (using vanilla sage-4.3.2.alpha1).
Positive review?


---

Comment by acleone created at 2010-02-05 12:56:29


```
$ egrep "Copying jsMath image"\|"Installed.*sagenb" ~/sage-dev/sage-4.3.2.alpha1/install.log
Installed /home/alex/sage-dev/sage-4.3.2.alpha1/local/lib/python2.6/site-packages/sagenb-0.6-py2.6.egg
```

Strange.


```
sage: from sagenb.misc.misc import SAGENB_VERSION
sage: SAGENB_VERSION
'0.7.4'
```


Here's how I installed: 

1. `make` on an unmodified 4.3.2.alpha1 

2. 

```
$ tar -jxvf sagenb-0.7.4.spkg
$ cd sagenb-0.7.4/src/sagenb/
$ sage -python setup.py develop
```

3. Tested with `sage -t -sagenb` 

4. Selenium tests with `sage -python sagenb/testing/run_tests.py` 

5. Checking the PDF build with `sage -docbuild all pdf`


---

Comment by mpatel created at 2010-02-05 13:03:04

I think this is OK, because the `SAGE_LOCAL/bin/sage-spkg` script invoked by `sage -f` updates `SAGE_ROOT/install.log` but the `sage -python setup.py` commands do not.


---

Comment by acleone created at 2010-02-05 13:16:57

The "Use image fonts" option is disabled (greyed out) in jsMath - is this a problem?

`jsMath v3.6c (Unicode fonts)`


---

Comment by mpatel created at 2010-02-05 13:22:28

Are the image fonts installed?  In `twist.py`, we set the boolean

```python
jsmath_image_fonts = is_package_installed("jsmath-image-fonts")
```

which propagates to `jsmath.js`.  This should enable the option if the spkg is installed.  But the fonts need to be installed in the right place...


---

Comment by acleone created at 2010-02-05 13:26:11

Ok then, LGTM.


---

Comment by acleone created at 2010-02-05 13:26:11

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-02-06 18:16:18

I decided to try something random to see if I was running the right notebook.  So I tried #3154 first, and it appears that it is *NOT* fixed by this notebook upgrade.  Other things I tried are fixed though.


---

Comment by was created at 2010-02-06 18:16:18

Remove assignee mpatel.


---

Comment by mpatel created at 2010-02-06 19:42:19

It turns out that I merged #4217, not #3154, into SageNB 0.7.  I didn't notice that #4217's commit string was copied from #3154 by mistake.  I used `hg log` to make the list of merged tickets in the description.


---

Comment by mpatel created at 2010-02-10 09:34:55

Resolution: fixed
