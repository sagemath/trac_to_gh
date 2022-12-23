# Issue 7617: include sagetex as a standard spkg

Issue created by migration from https://trac.sagemath.org/ticket/7617

Original creator: was

Original creation time: 2009-12-07 22:20:37

Assignee: tbd

CC:  ddrake jhpalmieri

sagetex has been voted in to be a standard sage spkg. 

the official maintainer for the "next few years" is Dan Drake.


---

Comment by ddrake created at 2009-12-08 02:57:21

I don't know if this should be a separate ticket for the upgrade, but the current spkg on the website is 2.1.1, but I have a spkg for version 2.2.1 prepared: http://sage.math.washington.edu/home/drake/code/sage/st/sagetex-2.2.1.spkg


---

Comment by was created at 2009-12-08 07:37:30

Changing status from new to needs_review.


---

Comment by was created at 2009-12-08 07:42:43

Hi,

I'm curious how users will even *know* to do this:

```
:To use SageTeX, both Sage and LaTeX need to know about it. If you have
installed this spkg, then Sage knows about SageTeX; now you need to make
LaTeX aware of it. The easiest thing to do is to ...
```


the only reason I know to do the things listed there so I can use SageTex is because I happen to have looked in the spkg after installing it and was looking at SPKG.txt.   When this package is standard in Sage, how will users know how to use and set it up?  Binaries won't even include that SPKG.txt file, since SAGE binaries don't include the contents of any spkg files. 

One solution, which I think would be extremely appropriate, is for you to add a new section to the Sage tutorial explaining how to use and get going with SageTex.  It's such a killer feature, that I think this is reasonable and worth it.    Let's make SageTex one of the centerpieces of Sage!


---

Comment by was created at 2009-12-08 07:42:43

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-12-08 07:47:34

Hi,

Why not make all this config stuff automatic?

"For Linux/Unix users, do

```
  cp -r $SAGE_ROOT/local/share/texmf/ $HOME/texmf/
```

For OS X users with MacTeX:

```
  cp -r $SAGE_ROOT/local/share/texmf/ $HOME/Library/texmf/
```

After you've copied over the necessary files, you'll need to update
TeX's database so that it can find them. Run "`texhash $HOME/texmf`"
(replace the texmf directory as appropriate) to do this."

I don't think the above is as easy as it could be...  I like to make things really easy, e.g., setting up a twisted webserver to server the Sage notebook app is `notebook()`.


---

Comment by ddrake created at 2009-12-08 08:20:04

Replying to [comment:6 was]:
> Why not make all this config stuff automatic?
> 
> "For Linux/Unix users, do
> {{{
>   cp -r $SAGE_ROOT/local/share/texmf/ $HOME/texmf/
> }}}
> For OS X users with MacTeX:
> {{{
>   cp -r $SAGE_ROOT/local/share/texmf/ $HOME/Library/texmf/
> }}}
> After you've copied over the necessary files, you'll need to update
> TeX's database so that it can find them. Run "`texhash $HOME/texmf`"
> (replace the texmf directory as appropriate) to do this."

One problem that I see is that there are different TeX distributions, and not all of them may automatically look in home directories for a texmf/ tree. Some users may also not want the default installation of Sage (which will now install SageTeX) to create those directories and files in their $HOME. 

> I don't think the above is as easy as it could be...  I like to make things really easy, e.g., setting up a twisted webserver to server the Sage notebook app is `notebook()`.

I agree, it's not very simple, but we are now interacting not only with Sage (which is a large software system) but with TeX, another large -- and quite different -- software system. And unlike Sage, a TeX installation is supposed to be very stable and work the same way for a long, long time -- so I'm guessing we could run into very old systems.

I'll look and see if there's a reasonably effective way to autodetect if $HOME/texmf will get picked up by TeX. I also like the idea of putting some basic installation instructions and pointers to the rest of the documentation into the tutorial.


---

Comment by ddrake created at 2009-12-08 08:35:44

Replying to [comment:7 ddrake]:
> And unlike Sage, a TeX installation is supposed to be very stable and work the same way for a long, long time

Oops, I don't mean to say that Sage isn't supposed to be stable! Just that TeX moves very slowly, in stark contrast to Sage.


---

Comment by was created at 2009-12-09 14:12:14

I see your points above.  I would like to see some specific plan though for making how to install SageTex be clearly documented with Sage (e.g., via the tutorial).  Otherwise, I don't understand how any non-super-advanced-and-lucky-user will figure out how to use it.


---

Comment by was created at 2009-12-09 14:13:41

Hi,

I've updated the optional sagetex spkg, since I tried it and it looks OK.

William


---

Comment by ddrake created at 2009-12-11 09:31:09

a draft of additions to the installation guide


---

Attachment

I've attached a draft of what we might add to the installation guide to help users, well, install SageTeX. I'd also like to add something to the reference manual, as users might after installation want to use SageTeX and not think of "installing" anything new (since their friends will tell them it's included in Sage). Mostly, I think we need to put pointers to the SageTeX documentation in several places. Where else should we mention it in the documentation?


---

Attachment

additions to the installation guide and tutorial


---

Comment by ddrake created at 2009-12-22 08:26:01

The attached patch (attachment:trac_7617.patch) adds instructions and basic help for installing and using SageTeX to the installation guide and tutorial.


---

Comment by ddrake created at 2009-12-22 08:26:01

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2009-12-23 00:54:16

I'm also going to change the section of the SageTeX documentation that discusses installation, since obviously that will now be different. That will involve a new spkg. Can/Should that be part of this ticket, or should it be a different one?


---

Comment by was created at 2009-12-24 20:15:00

Changing priority from major to critical.


---

Comment by was created at 2009-12-24 20:15:00

I've just read through all the patches and they look excellent.  I didn't test that the sphinx is valid or that the sagetex example actually works.  If somebody verifies that, then positive review. 

> Can/Should that be part of this ticket, or should it be a different one? 

It would make sense to make it part of this one. 

I'm changing the priority on this to critical for sage-4.3.1. 

 -- William


---

Comment by mhansen created at 2009-12-27 18:44:28

The markup in the patch looks good.


---

Comment by mhansen created at 2009-12-27 18:44:28

Changing status from needs_review to positive_review.


---

Attachment

additions to the installation guide and tutorial


---

Comment by ddrake created at 2009-12-28 08:36:42

Hrm, how can I switch this back to "needs review"? I added a bit on using TEXINPUTS.

I'm working on a new spkg that will have an updated installation section.


---

Comment by AlexGhitza created at 2009-12-28 09:31:18

Changing status from positive_review to needs_work.


---

Comment by AlexGhitza created at 2009-12-28 09:31:45

You have to make it "needs work" first.


---

Comment by AlexGhitza created at 2009-12-28 09:31:45

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2009-12-30 07:02:01

Thanks for the help, Alex. Along with the patch attachment:trac_7617.2.patch, I have a new spkg that reflects the new status as a standard spkg, available from http://sagenb.kaist.ac.kr/~drake/sagetex-2.2.3.spkg. Those two things need review.


---

Comment by jhpalmieri created at 2010-01-21 04:04:28

A few comments: overall, the documentation patch is good, but unfortunately it needs to be rebased.  Since you have to do that, I wonder if, in the reference manual, the file sagetex.rst needs to be in the new directory "other", or whether it should just be in the top ref manual directory.  Not a big deal.

Also, is it worth mentioning in the documentation that if you have several copies of sagetex.sty lying around, you need to make sure that the most recent one gets read first?  I just ran into this problem because I had installed an old version a while ago which was shadowing the more recent one.  Again, not a big deal, and if you think this should be done but don't want to bother now, it can be delayed to another ticket.

For a future version of sagetex, should sagetex print its version each time you latex the file, so that users can see what version is actually being used?

The spkg looks good, and seems to indicate in the right places that it's now a standard spkg.  Does anything else need to be checked?


---

Comment by jhpalmieri created at 2010-01-21 04:04:28

Changing status from needs_review to needs_work.


---

Comment by ddrake created at 2010-01-22 00:45:39

Replying to [comment:21 jhpalmieri]:
> A few comments: overall, the documentation patch is good, but unfortunately it needs to be rebased.  Since you have to do that, I wonder if, in the reference manual, the file sagetex.rst needs to be in the new directory "other", or whether it should just be in the top ref manual directory.  Not a big deal.

I'll put it in the "other" directory. I just guessed when I put sagetex.rst where it is.

> Also, is it worth mentioning in the documentation that if you have several copies of sagetex.sty lying around, you need to make sure that the most recent one gets read first?  I just ran into this problem because I had installed an old version a while ago which was shadowing the more recent one.  Again, not a big deal, and if you think this should be done but don't want to bother now, it can be delayed to another ticket.

I'll add a bit about this. It's one of the biggest problems with SageTeX.

> For a future version of sagetex, should sagetex print its version each time you latex the file, so that users can see what version is actually being used?

I've thought about some kind of mechanism that would check for version mismatch, but don't have any easily-implementable ideas at the moment. I think this would be best in another ticket.

> The spkg looks good, and seems to indicate in the right places that it's now a standard spkg.  Does anything else need to be checked?

I don't think so. If you can install the spkg, follow the TeX installation directions, and successfully use it on a document, I think it's good to go.

I have 4.3.1 compiled, so I'll rebase and adjust the documentation, and open a ticket for the version mismatch stuff.


---

Comment by ddrake created at 2010-01-22 00:50:25

The "detect version mismatch ticket" is #8035.


---

Attachment

additions to the installation guide and tutorial, v3. apply only this.


---

Comment by ddrake created at 2010-01-22 05:29:47

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-01-22 05:29:47

I've uploaded a new version of the documentation patch. It should apply to 4.3.1.

For the reference manual, I've kept sagetex.rst in the new "other" directory; when I put it in the root reference manual directory, Sphinx would try to look up a module named "sagetex" in the Sage library, get really confused, and overwrite sagetex.rst. I found that that didn't happen when I had the file in the "other" directory. If there's a better way to do this, let me know.

I added some text to the installation guide warning about having stale copies of sagetex.sty around.


---

Comment by jhpalmieri created at 2010-01-22 06:12:43

Looks good to me.  I guess the next thing to do is to add commands to TeXShop, Auc-TeX, etc., so they can easily run sage on the appropriate file...  :)


---

Comment by jhpalmieri created at 2010-01-22 06:12:43

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-01-22 06:18:30

See #8037 for a related ticket.


---

Comment by mvngu created at 2010-01-24 23:37:51

Just a minor comment: The spkg [sagetex-2.2.3.spkg](http://sagenb.kaist.ac.kr/~drake/sagetex-2.2.3.spkg) consists of SageTeX plus an MD5 check sum file `md5sum.check`, both compressed as `sagetex-2.2.3.spkg`. During the installation process, `sagetex-2.2.3.spkg` is uncompressed to `SAGE_PACKAGES/build/` and then installed, so that `SAGE_PACKAGES/build/` contains both `sagetex-2.2.3` and `md5sum.check`. After the installation is successful, the directory `SAGE_PACKAGES/build/sagetex-2.2.3/` is deleted, but `md5sum.check` still lingers under `SAGE_PACKAGES/build/`.

Is `md5sum.check` meant to be a realization of the ideas at #329 specifically for the SageTeX spkg?


---

Comment by ddrake created at 2010-01-25 00:17:10

Replying to [comment:27 mvngu]:
> Is `md5sum.check` meant to be a realization of the ideas at #329 specifically for the SageTeX spkg?

Yes. I was trying to be ahead of the curve and get my spkg compatible right away...but nothing has happened with that. Should I just remove that?


---

Comment by mvngu created at 2010-01-25 00:41:26

Replying to [comment:28 ddrake]:
> Should I just remove that?

No, I think you can leave the MD5 check sum file as is for now as a realization of the ideas at #329. The SageTeX spkg is the only package implementing the integrity check ideas at #329. I find the verification instructions at #329 to be very helpful, which make me think about an idea for implementing a patch to automatically verify the check sum in an spkg. But if other spkg's in the future also have a file named `md5sum.check`, it can be difficult to know which check file belongs to which package (because they're all given the same name). But if each spkg has its own integrity check file named, say, `spkg-name.md5` then `SAGE_PACKAGES/build` would be inundated with MD5 sum files (unless you delete them upon successful verification).


---

Comment by ddrake created at 2010-01-25 08:35:46

Replying to [comment:29 mvngu]:
> But if other spkg's in the future also have a file named `md5sum.check`, it can be difficult to know which check file belongs to which package (because they're all given the same name). But if each spkg has its own integrity check file named, say, `spkg-name.md5` then `SAGE_PACKAGES/build` would be inundated with MD5 sum files (unless you delete them upon successful verification).

Using the spkg name sounds like a good idea. I think verifying file integrity is important enough, and the number of files created small enough, so that having all those files in SAGE_PACKAGES/build worth it.


---

Comment by mvngu created at 2010-01-29 17:46:18

updated deps for SageTeX


---

Attachment

differences between deps in Sage 4.3.2.alpha0 and updated deps; don't apply


---

Attachment

updated install for SageTeX


---

Attachment

differences between install in Sage 4.3.2.alpha0 and updated install; don't apply


---

Comment by mvngu created at 2010-01-29 17:49:48

I have attached newer versions of the files `deps` and `install`, updated to take account of SageTeX being a standard spkg.


---

Comment by mvngu created at 2010-01-31 00:02:41

Resolution: fixed


---

Comment by mvngu created at 2010-01-31 00:02:41

Merged in this order: 

 1. [trac_7617.3.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/7617/trac_7617.3.patch) in the Sage library
 1. [install](http://trac.sagemath.org/sage_trac/attachment/ticket/7617/install) under `SAGE_ROOT/spkg/`
 1. [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/7617/deps) under `SAGE_ROOT/spkg/standard/`
 1. [sagetex-2.2.3.spkg](http://sagenb.kaist.ac.kr/~drake/sagetex-2.2.3.spkg) in the standard spkg repository


---

Comment by mvngu created at 2010-02-01 18:14:47

See #8144 for a follow-up to this ticket.


---

Comment by drkirkby created at 2010-03-07 13:20:15

Replying to [comment:29 mvngu]:
> No, I think you can leave the MD5 check sum file as is for now as a realization of the ideas at #329. The SageTeX spkg is the only package implementing the integrity check ideas at #329. 

Note I commented on #329 that I believe 'cksum' is better than md5, since

 * The command to compute an md5 checksum is called by different names on different systems. 'md5' and 'md5sum' are two I've come across. On Solaris one has to use 'digest -a md5 filename'
 * I suspect on some cut-down Linux distros, no such command exits - it is not part of POSIX. 
 * In contrast, 'cksum' is specified by POSIX, it is portable across all platforms as POSIX specifies the algorithm, and further that whilst not quite such a good test as 'md5', the probability of getting a false result is less than 2.4 x 10^-10.
