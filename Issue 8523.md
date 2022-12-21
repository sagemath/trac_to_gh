# Issue 8523: Optional package  p_group_cohomology-1.2 fails to install on Solaris 10 SPARC

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-13 14:44:23

Assignee: tbd

CC:  simonking

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.3.4.alpha1
 * Patch #8509 removing the -o option to grep to allow packages to install. 


 == The problem with the optional  p_group_cohomology-1.2 ==
This looks like being related to #8514, since p_group_cohomology-1.2 needs the gap database. But #8514 seems to be a mess, and might not be easy to sort out. 

```
p_group_cohomology-1.2/spkg-check
p_group_cohomology-1.2/spkg-check-quickly
Finished extraction
****************************************************
Host system
uname -a:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.4.3 (GCC)
****************************************************
Failed to find SmallGroups library.  Please install the database_gap spkg

real    0m0.043s
user    0m0.014s
sys     0m0.028s
sage: An error occurred while installing p_group_cohomology-1.2
```



---

Comment by dimpase created at 2010-03-27 12:27:11

this is not a Solaris-specific bug, but a general one, related to the failure to recognise that database_gap is installed.
This is similar to the situation described in #8236

Please check out 
http://boxen.math.washington.edu/home/dima/packages/p_group_cohomology-1.2.p0.spkg


---

Comment by dimpase created at 2010-03-27 12:27:11

Changing status from new to needs_review.


---

Comment by SimonKing created at 2010-03-27 16:09:13

Changing assignee from tbd to SimonKing.


---

Comment by SimonKing created at 2010-03-27 16:09:13

Hi Dima!

I saw at this ticket when it was created, but I understood from the ticket description that it was not possible to install database_gap.

Are you saying that you can install database_gap, but the install script of the group cohomology package does not recognise it? What did you change to make it recognise database_gap?

I am currently preparing a major upgrade of the group cohomology package. I expect it to be ready in about 2 weeks. Probably it would be easiest to incorporate the necessary  changes in the new version.

What do you think?

Best regards,

Simon


---

Comment by dimpase created at 2010-03-27 16:31:20

Replying to [comment:2 SimonKing]:
> Hi Dima!
> 
> I saw at this ticket when it was created, but I understood from the ticket description that it was not possible to install database_gap.

Hi Simon,

no, it was a Solaris-only problem, on the other patforms it worked just fine.
(and the fix is trivial and available already)

> 
> Are you saying that you can install database_gap, but the install script of the group cohomology package does not recognise it? What did you change to make it recognise database_gap?

well, when did it work last time, with which Sage release?
Probably since then the semantics of the script newest_version that you call in spkg-install has changed.
It MUST be called from SAGE_ROOT/spkg --- if you call it from somewhere else it reports nonsense.

So here is the diff:

```
--- a/spkg-install      Sat Mar 27 03:34:21 2010 -0700
+++ b/spkg-install      Sat Mar 27 04:26:40 2010 -0700
`@``@` -25,13 +25,10 `@``@`
    exit 1
 fi
 
-SMALL_GROUPS=`cd $SAGE_ROOT/spkg/optional/; $SAGE_ROOT/spkg/standard/newest_version database_gap`
+SMALL_GROUPS=`cd $SAGE_ROOT/spkg; $SAGE_ROOT/spkg/standard/newest_version database_gap`
 if [ "$SMALL_GROUPS" = "" ]; then
-    SMALL_GROUPS=`cd $SAGE_ROOT/spkg/installed/; $SAGE_ROOT/spkg/standard/newest_version database_gap`
-    if [ "$SMALL_GROUPS" = "" ]; then
-        echo "Failed to find SmallGroups library.  Please install the database_gap spkg"
+        echo "Failed to find SmallGroups library.  Please install the database_gap spkg, and make sure the corresponding spkg file (or any file with the same name!) is present in spkg/standard"
         exit 1
-    fi
 fi
 
 # test whether we are on an intel mac
```


> 
> I am currently preparing a major upgrade of the group cohomology package. I expect it to be ready in about 2 weeks. Probably it would be easiest to incorporate the necessary  changes in the new version.
> 

well, the fix is trivial, and it's better to have a working version for the next release already...

Dima


---

Comment by SimonKing created at 2010-03-27 16:46:36

Replying to [comment:3 dimpase]:

> well, when did it work last time, with which Sage release?

Starting with an spkg, I installed it in sage-4.3.1 to the least. And calling spkg-install directly is what I do all the time, with the newest sage.

> well, the fix is trivial, and it's better to have a working version for the next release already...

Thank you for the diff. I will change my spkg-install accordingly.

Best regards,

Simon


---

Comment by dimpase created at 2010-03-27 18:37:19

Replying to [comment:4 SimonKing]:
> Replying to [comment:3 dimpase]:
> 
> > well, when did it work last time, with which Sage release?
> 
> Starting with an spkg, I installed it in sage-4.3.1 to the least. And calling spkg-install directly is what I do all the time, with the newest sage.

Simon, 

calling spkg-install directly is certainly NOT the way it is meant to be installed.
It is meant to be installed either from within sage by calling install_package, or by calling
sage -i (or sage -f) at the shell prompt.
If this does not work, 99.9% of the users won't have a clue what to do.

Please check that this works for you now, too.

> 
> > well, the fix is trivial, and it's better to have a working version for the next release already...
> 
> Thank you for the diff. I will change my spkg-install accordingly.

you better just grab the spkg linked above, and tell Minh (and/or the release manager) to upgrade the sagemath.org repository
using this file. There this diff is already applied and the changes reflected in SPKG.txt
and in the Mercurial:
the repository was off in your spkg, I had to do a hg add and a hg commit; I aslo created .hgignore to ignore src/db files (having huge files in hg isn't good, and you have an online database with these, anyway).

This way, I could give it a positive review (pretending you did it all:-)).

Best,
Dima
 
> 
> Best regards,
> 
> Simon


---

Comment by SimonKing created at 2010-03-28 00:58:14

Replying to [comment:5 dimpase]:
> calling spkg-install directly is certainly NOT the way it is meant to be installed.
> It is meant to be installed either from within sage by calling install_package, or by calling
> sage -i (or sage -f) at the shell prompt.

I think we talk about totally different situations. You seem to talk about version 1.2, which is published and should certainly be installable by a user doing sage -i.

But IMO, sage -i is the way to go *only if the package is finished*. I am talking about the yet-to-be-published version 2.0. I am still not finished with all details of the new algorithms and documentation, and it has not being packaged yet.

I will certainly not do sage -i while developing new algorithms. Namely, before doing sage -i, one has to have a spkg. Thus, I would have to do sage -pkg after each tiny little change, 20-50 times a day! That's clumsy! 

Moreover, sage -i should be equivalent to unpacking the spkg (well, it is unpacked since I didn't pack my development version yet) and calling spkg-install (plus, perhaps, spkg-check) in the sage environment. So, if spkg-install works (which it does for me) then sage -i should work as well.

So, testing whether sage -i still works will only be the last step before publishing version 2.0. 

> Please check that this works for you now, too.

You seem to talk about version 1.2. This version _did_ work, on quite a broad range of platforms. I never had the problem that you describe. 

In fact, I just tested (sage 4.3.4 on Opensuse; you said that the problem is not platform specific), and sage -f p_group_cohomology-1.2.spkg (without your changes) came easily beyond the point where the existence of database_gap is tested. Then, I interrupted with Ctrl-C.

So, can you please tell me how I can reproduce the problem that you met?

> you better just grab the spkg linked above, and tell Minh (and/or the release manager) to upgrade the sagemath.org repository
> using this file. There this diff is already applied and the changes reflected in SPKG.txt

I don't plan to re-publish version 1.2, unless I can reproduce the problem. But I will pull it into version 2.0.

> and in the Mercurial:
> the repository was off in your spkg, I had to do a hg add and a hg commit; 

WHAT? 

Sorry for shouting, but certainly the repository was not off. I don't know if you ever did sage -pkg, but it gives an unmistakable warning if the repository is not fine.

That you had to do hg commit is clear. But certainly spkg-install was in the repository. So, why hg add?

> I aslo created .hgignore to ignore src/db files (having huge files in hg isn't good, and you have an online database with these, anyway).

Here I am not so sure, but I thought that I did not include src/db in the repository, for this reason. BTW, the online database does _not_ contain the cohomology rings for the groups of order 64 -- these are only provided by the database in the package. 

> This way, I could give it a positive review (pretending you did it all:-)).

Now I am totally confused.

First of all, I think that this ticket is a "wontfix", because it will soon be superseded by another ticket that I will open when I publish version 2.0.

Moreover, it is about a problem that I can not reproduce.

Then you say you will give a positive review -- to changes that you did yourself?

Best regards,

Simon


---

Comment by SimonKing created at 2010-03-28 03:01:01

Concerning the mercurial repository:

I just verified that SPKG.txt and spkg-install are tracked in the spkg's repository, and that the database for the groups of order 64 is not tracked.

So, I can not reproduce any of the issues that you are reporting.


---

Comment by dimpase created at 2010-03-28 04:02:52

Replying to [comment:7 SimonKing]:
> Concerning the mercurial repository:
> 
> I just verified that SPKG.txt and spkg-install are tracked in the spkg's repository, and that the database for the groups of order 64 is not tracked.
> 
> So, I can not reproduce any of the issues that you are reporting.

Simon,

In http://sagemath.org/packages/optional/p_group_cohomology-1.2.spkg
(do you talk about the same repository?) hg  reports

```
? mtxoriginal/COPYING
? mtxoriginal/README
? mtxoriginal/bin/Makefile
? mtxoriginal/bin/proggy/f1
? mtxoriginal/bin/proggy/f2
[...edited out...]
```

the "?" status means something like "hg does not know about this file; it is there, but I have no clue how to deal with it" which is obviously not what one likes to have, even if sage -spkg
does not complain. Moreover in SPKG.txt you say 

```
Note that most of the code is original. Therefore we included the files from
src into the Mercurial repository.
```

Probably it slipped through when the package was reviewed.

Best,
Dima


---

Comment by dimpase created at 2010-03-28 05:08:13

Replying to [comment:6 SimonKing]:
> Replying to [comment:5 dimpase]:
> > calling spkg-install directly is certainly NOT the way it is meant to be installed.
> > It is meant to be installed either from within sage by calling install_package, or by calling
> > sage -i (or sage -f) at the shell prompt.
> 
> I think we talk about totally different situations. You seem to talk about version 1.2, which is published and should certainly be installable by a user doing sage -i.
> 

Sure, I do talk about 1.2 (and I was baffled by what you wrote). And 1.2 is broken, it does not install on any Sage 4.3.4 I have (as I was busy with updating gap-related spkgs and cvxopt spkg, I have a large supply presently :-)).
For instance, one compiled from source on boxen.math 

```
dima`@`boxen:~/sage/sage-4.3.4/spkg/standard$ ls database_g*
database_gap-4.4.12.p0.spkg
```

ok, so SmallGroups are there, but I cannot install the package (I just copied the canonical 1.2 version to /tmp)

```
../../sage -f /tmp/p_group_cohomology-1.2.spkg
[...]
***************************************************
/bin/ls: cannot access database_gap-*.spkg: No such file or directory
/bin/ls: cannot access database_gap-*.spkg: No such file or directory
Failed to find SmallGroups library.  Please install the database_gap spkg

real	0m0.575s
user	0m0.010s
sys	0m0.020s
sage: An error occurred while installing p_group_cohomology-1.2
```



> But IMO, sage -i is the way to go *only if the package is finished*. I am talking about the yet-to-be-published version 2.0. I am still not finished with all details of the new algorithms and documentation, and it has not being packaged yet.
> 
> I will certainly not do sage -i while developing new algorithms. Namely, before doing sage -i, one has to have a spkg. Thus, I would have to do sage -pkg after each tiny little change, 20-50 times a day! That's clumsy! 
> 
> Moreover, sage -i should be equivalent to unpacking the spkg (well, it is unpacked since I didn't pack my development version yet) and calling spkg-install (plus, perhaps, spkg-check) in the sage environment. So, if spkg-install works (which it does for me) then sage -i should work as well.
> 
> So, testing whether sage -i still works will only be the last step before publishing version 2.0. 
> 
> > Please check that this works for you now, too.
> 
> You seem to talk about version 1.2. This version _did_ work, on quite a broad range of platforms. I never had the problem that you describe. 
> 
> In fact, I just tested (sage 4.3.4 on Opensuse; you said that the problem is not platform specific), and sage -f p_group_cohomology-1.2.spkg (without your changes) came easily beyond the point where the existence of database_gap is tested. Then, I interrupted with Ctrl-C.

Please see above. I don't have access to SUSE systems, but it fails on a range of Ubuntu and Debian Linuxes, as well as on Solaris (Sparc) and on MacOSX 10.5 (PPC), all of these with Sage 4.3.4.
 
> 
> So, can you please tell me how I can reproduce the problem that you met?

Try it on sage.math or boxen.math and see for yourself, if you like.

> 
> > you better just grab the spkg linked above, and tell Minh (and/or the release manager) to upgrade the sagemath.org repository
> > using this file. There this diff is already applied and the changes reflected in SPKG.txt
> 
> I don't plan to re-publish version 1.2, unless I can reproduce the problem. But I will pull it into version 2.0.
> 
> > and in the Mercurial:
> > the repository was off in your spkg, I had to do a hg add and a hg commit; 
> 
> WHAT? 
> 
> Sorry for shouting, but certainly the repository was not off. I don't know if you ever did sage -pkg, but it gives an unmistakable warning if the repository is not fine.
> 
> That you had to do hg commit is clear. But certainly spkg-install was in the repository. So, why hg add?

as I explained in another reply, to bring it in line to what you wrote in SPKG.txt.
By the way, I was pointed out few times by spkg reviewers that having hg-"?"-marked files in the spkg is not good, and they insisted on fixing this.
> 
> > I aslo created .hgignore to ignore src/db files (having huge files in hg isn't good, and you have an online database with these, anyway).
> 
> Here I am not so sure, but I thought that I did not include src/db in the repository, for this reason. BTW, the online database does _not_ contain the cohomology rings for the groups of order 64 -- these are only provided by the database in the package.

OK, sorry about this. 

> 
> > This way, I could give it a positive review (pretending you did it all:-)).
> 
> Now I am totally confused.

My apologies. As usual, the joke is lost in electronic communications... I meant to say I explained it to you all, leaving you almost nothing to figure out, so it would be a breeze to give it a positive review.

> 
> First of all, I think that this ticket is a "wontfix", because it will soon be superseded by another ticket that I will open when I publish version 2.0.
> 
> Moreover, it is about a problem that I can not reproduce.

well, 2.0 is still at least weeks away, and then reviewing, etc etc. Meanwhile there is a broken spkg on the list of optional packages, and the fix is ready. So, please, please, let us fix it, and be done with.

Best,
Dima


---

Comment by SimonKing created at 2010-03-28 10:00:36

Replying to [comment:8 dimpase]:

> Replying to [comment:7 SimonKing]:

  In http://sagemath.org/packages/optional/p_group_cohomology-1.2.spkg (do you talk about the same repository?) hg  reports

```
  ? mtxoriginal/COPYING 
  ? mtxoriginal/README 
  ? mtxoriginal/bin/Makefile 
  ...
```


Ah, now I understand. In fact, these files do not belong into the hg repository, IMO.

The `mtxoriginal/` folder is just a reference to the original `C-MeatAxe`, as it was downloaded from upstream. And if I remember correctly, as a rule of thumb, any SPKG should provide third party code in its original form.

On the other hand, look into the `src/` folder. As a subfolder, you will find another copy of `C-MeatAxe`. This one contains many modifications made by David Green and myself. Since these modifications are, to some extent, original code, I've put it under version control: You will find that this subfolder _is_ in the hg repository.

Changes to third party code should be made transparent, and I thought that if there are many changes then the resulting large diff file would be less transparent than having both versions simultaneously: The version from third party, and our modified version.

Only the code in `src/` is compiled, and it may change when upgrading the package. But the stuff in `mtxoriginal/` is not compiled, and it will not be touched. So, there is no point of putting `mtxoriginall/` under version control.

> Moreover in SPKG.txt you say  ` Note that most of the code is original.  Therefore we included the files from src into the Mercurial repository. `

Exactly. And it also says:


```
The package includes a modified version of the Aachen C-MeatAxe. Since the
changes are major, we included the modified sources into the Mercurial
repository. A MeatAxe version that comes closest to what we started with
is provided in the folder mtxoriginal.
```

I thought this is clear enough.

IIRC, the developer's guide says that the `src/` folder of an SPKG should _not_ be under version control. I asked why, and got the reply that _normally_ it contains third party code that is simply dropped in, so that version control does not make sense.

Here, we have original code, and therefore `src/` is under version control, in contrast to most other SPKGs.

Probably I should better add a `.hgignore`, so that `mtxoriginal/` gets ignored...

Best regards,

Simon


---

Comment by SimonKing created at 2010-03-28 10:17:53

Replying to [comment:9 dimpase]:

Sure, I do talk about 1.2 (and I was baffled by what you wrote). And 1.2 is broken, it does not install on any Sage 4.3.4 I have
Really? OK, then something needs to be done. 

It did compile on several platforms. Personally, I tested Suse linux (two different machines at my university), sage-math, and Intel mac (Darwin). David Joyner and William Stein tested it on various other platforms, like Ubuntu. The issues found there had been sorted out.

 For instance, one compiled from source on boxen.math  

OK, then I  will try to build sage on boxen and see what happens. I'll reply later what happens.

Please see above. I don't have access to SUSE systems, but it fails on a range of Ubuntu and Debian Linuxes, as well as on Solaris (Sparc) and on MacOSX 10.5 (PPC), all of these with Sage 4.3.4.

OK, these had been tested with previous sage versions. So, now the picture becomes clearer: The package became broken by upgrading sage, and I think this is what you said.

> as I explained in another reply, to bring it in line to what you wrote in SPKG.txt. By the way, I was pointed out few times by spkg reviewers that having hg-"?"-marked files in the spkg is not good, and they insisted on fixing this.

See my reply there: These files, I think, do not belong under version control, but making this clear by .hgignore might be a good idea.

> well, 2.0 is still at least weeks away, and then reviewing, etc etc. Meanwhile there is a broken spkg on the list of optional packages, and the fix is ready. So, please, please, let us fix it, and be done with. Best, Dima

Right, that makes sense.

So, I will test on boxen. If successful, I will probably then do the following:

 * Adopt your changes to spkg-install
 * Mention these changes in SPKG.txt
 * Putting mtxoriginal under .hgignore
 * Ask whether this change can be put into the sage repository.

The question is, though: Should this still be p_group_cohomology-1.2, or better p_group_cohomology-1.2.1? And who is giving a positive review? :)

Best regards,

Simon


---

Comment by SimonKing created at 2010-03-28 10:19:54

PS:

Sorry for the strange layout of my previous post. I just see that your post is not marked as a quote. It looked fine in "wysywig".


---

Comment by dimpase created at 2010-03-28 10:24:08

Replying to [comment:10 SimonKing]:
> Replying to [comment:8 dimpase]:
> 
> > Replying to [comment:7 SimonKing]:
> 
>   In http://sagemath.org/packages/optional/p_group_cohomology-1.2.spkg (do you talk about the same repository?) hg  reports
> {{{
>   ? mtxoriginal/COPYING 
>   ? mtxoriginal/README 
>   ? mtxoriginal/bin/Makefile 
>   ...
> }}}
> 
> Ah, now I understand. In fact, these files do not belong into the hg repository, IMO.
> 
> The `mtxoriginal/` folder is just a reference to the original `C-MeatAxe`, as it was downloaded from upstream. And if I remember correctly, as a rule of thumb, any SPKG should provide third party code in its original form.

Right. Indeed, the most sensible thing seems to have .hgignore as follows:

```
mtxoriginal
src/db
```

(and do not forget to "hg add .hgignore", so that "hg status" would not report anything at all)

OK, so my complaint was about "hg status" reporting lots of "?"-marked files, I didn't 
look more carefully what exactly was there --- my guess was it's the entire directory, as also .hgignore file wasn't 
there at all.

Best,

Dima

> Probably I should better add a `.hgignore`, so that `mtxoriginal/` gets ignored...
> 
> Best regards,
> 
> Simon


---

Comment by dimpase created at 2010-03-28 10:38:33

Changing status from needs_review to needs_work.


---

Comment by dimpase created at 2010-03-28 10:38:33

Replying to [comment:11 SimonKing]:
>> Replying to [comment:9 dimpase]:
> >
> > Sure, I do talk about 1.2 (and I was baffled by what you wrote). And 1.2 is broken, it does not install on any Sage 4.3.4 I > > have
> Really? OK, then something needs to be done. 
> 
> It did compile on several platforms. Personally, I tested Suse linux (two different machines at my university), sage-math, and Intel mac (Darwin). David Joyner and William Stein tested it on various other platforms, like Ubuntu. The issues found there had been sorted out.

Apparently since the release of your spkg there was a semantics change in some Sage scripts that now causes us this headache.

> 
>  For instance, one compiled from source on boxen.math  

> OK, then I  will try to build sage on boxen and see what happens. I'll reply later what happens.

there is a ready binary install for sage.math, you can just grab it instead, and try out on sage.math (not on boxen)
http://sage.math.washington.edu/home/release/sage-4.3.4/sage-4.3.4-sage.math.washington.edu-x86_64-Linux.tar.gz
This would be much faster.

> 
> Please see above. I don't have access to SUSE systems, but it fails on a range of Ubuntu and Debian Linuxes, as well as on Solaris (Sparc) and on MacOSX 10.5 (PPC), all of these with Sage 4.3.4.

> OK, these had been tested with previous sage versions. So, now the picture becomes clearer: The package became broken by upgrading sage, and I think this is what you said.

Right.


> So, I will test on boxen. If successful, I will probably then do the following:
> 
>  * Adopt your changes to spkg-install
>  * Mention these changes in SPKG.txt
>  * Putting mtxoriginal under .hgignore
>  * Ask whether this change can be put into the sage repository.
> 
> The question is, though: Should this still be p_group_cohomology-1.2, or better p_group_cohomology-1.2.1?

p_group_cohomology-1.2.p0 seems to be the proper name.


>  And who is giving a positive review? :)

That's a tough one :-)
well, if you do not mention my name in the changes then I won't be a co-author, and will be able to review, IMHO.
We could also ask Dave, the initiator of the ticket...

Best,

Dima

> 
> Best regards,
> 
> Simon


---

Comment by SimonKing created at 2010-03-28 12:42:39

Changing status from needs_work to needs_info.


---

Comment by SimonKing created at 2010-03-28 12:42:39

Hi Dima!

Now I am even more puzzled.

I did precisely the following steps:

 * I copied and unpacked the sage-4.3.4 binary for sage.math on sage.math
 * I started ./sage and waited until it had updated paths. Then I quit sage.
 * I edited ./sage, replacing "......" by the correct value of SAGE_ROOT
 * I started ./sage again, testing it with "2+gap(2)"
 * I did install_package('database_gap') followed by install_package('gap_packages').
 * Then, I did install_package('p_group_cohomology'), and could then do "from pGroupCohomology import CohomologyRing"


It installed fine, there was no error. I think this is how a user is supposed to install things, and so I can still not reproduce the error.

Cheers,

Simon


---

Comment by SimonKing created at 2010-03-28 12:52:13

PS:

Before using the package, I had to do gap_reset_workspace(), quit sage, start it again, and then I did successfully compute some cohomology rings.


---

Comment by dimpase created at 2010-03-28 13:10:59

Replying to [comment:15 SimonKing]:

Hi,

> Now I am even more puzzled.
> 
> I did precisely the following steps:
> 
>  * I copied and unpacked the sage-4.3.4 binary for sage.math on sage.math
>  * I started ./sage and waited until it had updated paths. Then I quit sage.
>  * I edited ./sage, replacing "......" by the correct value of SAGE_ROOT
>  * I started ./sage again, testing it with "2+gap(2)"
>  * I did install_package('database_gap') followed by install_package('gap_packages').
>  * Then, I did install_package('p_group_cohomology'), and could then do "from pGroupCohomology import CohomologyRing"

> 
> It installed fine, there was no error. I think this is how a user is supposed to install things, and so I can still not reproduce the error.
> 

I can confirm that indeed this way it works for me (on boxen with a compiled Sage 4.3.4-version), too.

OK, so it appears to be an inconsistency in the Sage behaviour, when the option -i (or -f) is used to install the package. (AFAIK, these options are not something for experts only, they should work just the same...)

It is, perhaps, a bug in newest_version script.
I'll see if I can find it quickly...

Dima

> Cheers,
> 
> Simon


---

Comment by SimonKing created at 2010-03-28 13:53:27

Replying to [comment:17 dimpase]:
> I can confirm that indeed this way it works for me (on boxen with a compiled Sage 4.3.4-version), too.

That's a big relief!

> It is, perhaps, a bug in newest_version script.
> I'll see if I can find it quickly...

But if one of the two usual ways of installing the package does work, then it might be acceptable to leave it as it is, and then to take care that _both_ ways of installation work for p_group_cohomology-2.0.

What do you think?


---

Comment by dimpase created at 2010-03-28 14:07:01

Replying to [comment:18 SimonKing]:
> Replying to [comment:17 dimpase]:
> > I can confirm that indeed this way it works for me (on boxen with a compiled Sage 4.3.4-version), too.
> 
> That's a big relief!
> 
> > It is, perhaps, a bug in newest_version script.
> > I'll see if I can find it quickly...

I spent an hour trying to sort this out, and my only conclusion is that on a clean and fresh install things work both ways.
Apparently there is a subtle bug that only manifests itself after unsuccessful installs of spkgs, something gets inconsistent...

I propose to mark this ticket as "won't fix", as this is certainly nothing wrong
with this spkg (except that hg inconsistency one can live with, at least if a new spkg release is coming).

Dima


> 
> But if one of the two usual ways of installing the package does work, then it might be acceptable to leave it as it is, and then to take care that _both_ ways of installation work for p_group_cohomology-2.0.
> 
> What do you think?


---

Comment by jhpalmieri created at 2010-03-28 14:44:36

I think the problem is this: if you install "database_gap-4.4.12" by downloading the spkg file and typing

```
sage -i PATH_TO/database_gap-4.4.12.spkg
```

then it is installed, but the spkg file is not copied to SAGE_ROOT/spkg/optional or to SAGE_ROOT/spkg/standard.  There is a placeholder file in SAGE_ROOT/spkg/installed, and this is probably what you should look for to test whether it's installed -- this is what the file SAGE_ROOT/local/bin/sage-spkg does.  Note that after this, if you run "install_package('database_gap')" or "sage -i database_gap-4.4.12.spkg", it says that it's installed.

(If you run "install_package('database_gap')", on the other hand, then Sage downloads the spkg file and puts it in spkg/optional, so your spkg-install file finds it.)


---

Comment by SimonKing created at 2010-03-28 14:46:28

Now that's weird.

I took the spkg-install as you suggested. But the test for the presence of database_gap failed:

```
sage subshell$ ./spkg-install
/bin/ls: cannot access database_gap-*.spkg: No such file or directory
Failed to find SmallGroups library.  Please install the database_gap spkg, and make sure the corresponding spkg file (or any file with the same name!) is present in spkg/standard
```


In other word: For me, the original version works, but the modified version doesn't.

Best regards,

Simon


---

Comment by SimonKing created at 2010-03-28 14:51:50

Replying to [comment:20 jhpalmieri]:
> I think the problem is this: if you install "database_gap-4.4.12" by downloading the spkg file and typing
> {{{
> sage -i PATH_TO/database_gap-4.4.12.spkg
> }}}
> then it is installed, but the spkg file is not copied to SAGE_ROOT/spkg/optional or to SAGE_ROOT/spkg/standard.  There is a placeholder file in SAGE_ROOT/spkg/installed, and this is probably what you should look for to test whether it's installed -- this is what the file SAGE_ROOT/local/bin/sage-spkg does. 


... and this is what I did in my spkg-install (for exactly the reason you explain):

```
SMALL_GROUPS=`cd $SAGE_ROOT/spkg/optional/; $SAGE_ROOT/spkg/standard/newest_version database_gap`
if [ "$SMALL_GROUPS" = "" ]; then
    SMALL_GROUPS=`cd $SAGE_ROOT/spkg/installed/; $SAGE_ROOT/spkg/standard/newest_version database_gap`
    if [ "$SMALL_GROUPS" = "" ]; then
        echo "Failed to find SmallGroups library.  Please install the database_gap spkg"
        exit 1
    fi
fi
```


Cheers,

Simon


---

Comment by jhpalmieri created at 2010-03-28 15:15:48

I have a file "database_gap-4.4.12" in SAGE_ROOT/spkg/installed, and I just did this:

 - run "sage -sh"
 - cd to SAGE_ROOT/spkg/installed
 - run "../standard/newest_version database_gap"

and it didn't find it.  It looks to me like "newest_version" searches for a file ending in ".spkg", and the files in spkg/installed don't match this.  The script SAGE_ROOT/local/bin/sage-spkg does something else to check for installation:

```
if [ -f "$INSTALLED/$PKG_NAME" -a $FORCE -eq 0 ]; then
    echo "sage: $1 is already installed"
    touch "$INSTALLED/$PKG_NAME"
    exit 0
fi
```

where $INSTALLED is SAGE_ROOT/spkg/installed, $PKG_NAME is the name without "spkg", and you could omit "-a $FORCE", I think.


---

Comment by SimonKing created at 2010-03-28 16:41:03

Replying to [comment:23 jhpalmieri]:
> The script SAGE_ROOT/local/bin/sage-spkg does something else to check for installation:
> {{{
> ...
> where $INSTALLED is SAGE_ROOT/spkg/installed, $PKG_NAME is the name without "spkg", and you could omit "-a $FORCE", I think.

Good, I'll check this.

What are the opinions: Can this wait until p_group_cohomology-2.0 is finished (since version 1.2 does work, provided the users install everything the "normal" way)? Or should there been a version 1.2.p0?

Best regards,

Simon


---

Comment by SimonKing created at 2010-03-28 17:03:07

Hi John!

I don't know how it works what you suggested. First of all, $INSTALLED has no value in the sage shell:

```
sage subshell$ echo $INSTALLED

```


Could it be that it is only defined inside `SAGE_ROOT/local/bin/sage-spkg`?

And one problem with this method is that (if I understand correctly) one has to provide the exact version of the package whose existence is being tested. 

But I don't want a method to test for the presence of database_gap-4.4.12 (so that it wouldn't work if database_gap-4.4.10 is installed). I want to test if _any_ version of database_gap is there. 

And I think that this is exactly the purpose of the script `$SAGE_ROOT/spkg/standard/newest_version`.

Cheers,

Simon


---

Comment by dimpase created at 2010-03-28 17:51:13

Replying to [comment:25 SimonKing]:
Hi Simon,

OK, so it seems that I provided a "fix" that does not always work from within Sage, and your original package setup
does not always work with sage -i.

In your case, the safest would be just to call "sage -gap" and see if it has SmallGroups stuff loaded.
E.g. just check that the output of

```
echo "SmallGroup(13,1); quit;" | $SAGE_ROOT/sage -gap -b -T | grep "13"
```

is nonempty.

Best,
Dima


---

Comment by SimonKing created at 2010-03-28 18:19:44

Replying to [comment:26 dimpase]:
> In your case, the safest would be just to call "sage -gap" and see if it has SmallGroups stuff loaded.
> E.g. just check that the output of
> {{{
> echo "SmallGroup(13,1); quit;" | $SAGE_ROOT/sage -gap -b -T | grep "13"
> }}}
> is nonempty.

This is great! It is an ideal solution, in the sense that it tests exactly what is needed. Namely, we actually don't care about the database_gap spkg -- it is alright if the user got his SmallGroups library from a different source.

The change is little. So, I guess I'll create a version 1.2.p0, adding .hgignore, mentioning you in SPKG.txt (I am rewriting it in reverse chronological order, by the way), and change spkg-install; actually, I already tested that it works on my computer.

Probably, if you or Dave are able to install the package with the new spkg-install, then you are entitled to give a positive review, so that the release manager can put it into the repository of optional packages.

Thank you very much!

Simon


---

Comment by jhpalmieri created at 2010-03-28 18:28:13

Replying to [comment:25 SimonKing]:
> Hi John!
> 
> I don't know how it works what you suggested. First of all, $INSTALLED has no value in the sage shell:

> Could it be that it is only defined inside `SAGE_ROOT/local/bin/sage-spkg`?

That's right.

> And one problem with this method is that (if I understand correctly) one has to provide the exact version of the package whose existence is being tested. 

I think that's right, too.  I don't know much about writing shell scripts, but this seems to work:
{{{#!/usr/bin/env bash

INSTALLED="$SAGE_PACKAGES/installed/"
PKG_NAME=`echo "$1" | sed -e "s/\.spkg$//"`
PKG_NAME=`basename "$PKG_NAME"`
PKG_BASE=`echo "$PKG_NAME" | sed -e "s/-.*//"`

cd "$SAGE_PACKAGES/installed"

if [ `echo $PKG_BASE*` ]; then
    echo "sage: $PKG_BASE is already installed"
    exit 0
fi
```

($SAGE_PACKAGES is defined by running "sage -sh".)  This script defines PKG_BASE to be the name of the package without the version number: everything up to the first hyphen or period, whichever comes first.


---

Comment by SimonKing created at 2010-03-28 18:46:03

Hi!

I created a new patch level version, which I was able to install on sage.math by

```
./sage -i http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.2.p0.spkg
```


Changes: 
 - adding .hgignore
 - modifying SPKG.txt (adding this change to the changelog, and putting the changelog in reverse chronological order)
 - modifying spkg-install.

The test for the presence of Small Groups is now

```
SMALL_GROUPS=`echo "SmallGroup(13,1); quit;" | $SAGE_ROOT/sage -gap -b -T | grep "13"`
if [ "$SMALL_GROUPS" = "" ]; then
   echo "It seems that GAP's SmallGroups library is missing."
   echo "One way to install it is by doing"
   echo "    sage: install_package('database_gap')"
   echo "in a Sage session."
   exit 1
fi
```


Note that this is _really_ a test for the Small Groups library, rather than for the database_gap spkg. The error message is a bit more descriptive as well.

hg status does not return question marks.

So, ready for review!

Cheers,

Simon


---

Comment by SimonKing created at 2010-03-28 18:46:03

Changing status from needs_info to needs_review.


---

Comment by dimpase created at 2010-03-29 09:56:10

Replying to [comment:29 SimonKing]:
Hi,

OK, good, I checked that it also works on boxen and Solaris (Sparc)(t2).
On t2 I also tried few things from the package:

```
sage: from pGroupCohomology.dickson import DICKSON
sage: D = DICKSON(3)
sage: d_3_1 = D(3,1)
sage: d_3_1
y0^18*y1^6 + ...
```


I give it a positive review (despite my name mentioned in SPKG, I only contributed an idea for a fix, but I didn't touch the code).

Best,
Dima


---

Comment by dimpase created at 2010-03-29 09:56:10

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2010-03-29 10:21:43

Changing keywords from "" to "recognise database_gap, group cohomology".


---

Comment by SimonKing created at 2010-03-29 10:21:43

Hi Dima!

Fine! Then I change the "keywords", "author" and "reviewer" fields accordingly.

Is it needed to notify a release manager, or are these guys reading any ticket anyway?

Best regards,
Simon


---

Comment by dimpase created at 2010-03-29 10:29:44

Replying to [comment:31 SimonKing]:
> Fine! Then I change the "keywords", "author" and "reviewer" fields accordingly.
> 
> Is it needed to notify a release manager, or are these guys reading any ticket anyway?
> 
 
IMHO they check at least the positively reviewed ones...

Dima


---

Comment by SimonKing created at 2010-03-29 10:37:04

Replying to [comment:32 dimpase]:

> IMHO they check at least the positively reviewed ones...

OK.

To the release manager (for avoiding confusion): The positive review is for the package posted at

  [http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.2.p0.spkg](http://sage.math.washington.edu/home/SimonKing/Cohomology/p_group_cohomology-1.2.p0.spkg)

Simon


---

Comment by jhpalmieri created at 2010-04-20 22:54:47

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-20 22:54:47

Merged 2010/04/20.
