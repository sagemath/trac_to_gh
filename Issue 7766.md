# Issue 7766: Upgrade optional spkg valgrind to valgrind-3.6.0.svn

Issue created by migration from https://trac.sagemath.org/ticket/7766

Original creator: jsp

Original creation time: 2009-12-25 20:36:30

Assignee: tbd

CC:  timdumol rlm iandrus jpflori kini

Keywords: memory testing

The optional valgrind-3.1.1 did not build in Fedora 12 x86_64

reason: glibc-11 is not supported. Even in the last released stable valgrind-3.5.0

So I downloaded from SVN and made an spkg.

See: [http://sage.math.washington.edu/home/jsp/valgrind-3.6.0.svn.spkg](http://sage.math.washington.edu/home/jsp/valgrind-3.6.0.svn.spkg)

Urgent: we need a maintainer other than me and Michael!

Jaap


---

Comment by jsp created at 2009-12-27 13:56:30

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-01-23 09:02:32

Ticket #7440 has upgraded the optional Valgrind spkg to version 3.5.0. Tim Dumol has agreed to maintain that spkg.


---

Comment by jsp created at 2010-01-23 10:38:02

Replying to [comment:2 mvngu]:
> Ticket #7440 has upgraded the optional Valgrind spkg to version 3.5.0. Tim Dumol has agreed to maintain that spkg.


valgrind-3.5.0 didn't compile with Fedora 12 64 bit.

Jaap


---

Comment by timdumol created at 2010-01-23 21:44:27

It may be worth rebasing this on #7440. `spkg-install` was updated on #7440 to detect Darwin 9.0 as well, on which Valgrind 3.5.0 works on. Also, mabshoff's name should be removed from the package, as per #7738. Feel free to add your own name to the maintainers list as well. Those issues aside, the package seems to work perfectly here. Nice work.


---

Comment by timdumol created at 2010-01-23 21:44:27

Changing status from needs_review to needs_work.


---

Comment by jsp created at 2010-01-23 22:00:50

Replying to [comment:4 timdumol]:
> It may be worth rebasing this on #7440. `spkg-install` was updated on #7440 to detect Darwin 9.0 as well, on which Valgrind 3.5.0 works on. Also, mabshoff's name should be removed from the package, as per #7738. Feel free to add your own name to the maintainers list as well. Those issues aside, the package seems to work perfectly here. Nice work.

Hi Tim,

Would you mind taking over? I'm not a valgrind expert as Michael was.

I have some problems with sage -t on Fedora 12 64 bit on my computer with i7 860 processor. So I tried valgrind. It came up with some issues. See:
[http://trac.sagemath.org/sage_trac/ticket/7773](http://trac.sagemath.org/sage_trac/ticket/7773) 

Jaap


---

Comment by maldun created at 2010-08-28 14:00:44

Is there an option to install the package via SVN or is the spkg-file in the download link really broken?

There are some empty shell script in the package, I repaired it for my self with copying some of the files from valgrind.3,5.0 package, and it worked fine.


---

Comment by iandrus created at 2011-03-23 22:48:11

I created a new spkg from 3.6.1.  Since 3.6.1 works on OS X 10.6, I added support for that as well.  You can find the spkg at http://boxen.math.washington.edu/home/iandrus/valgrind-3.6.1.p0.spkg
I based it off of the spkg at #7440.

One other (perhaps controversial) thing that I did is add suppressions so that starting sage under valgrind and immediately exiting shows no leaks.  I was also using the suppression file provided by python which should probably be installed as part of the python spkg-install.  Some (or many) of these may be actual leaks, but I don't have the expertise to check them all.  Because I don't know if all the suppressions are valid I'm hesitant to mark this as needs_review.


---

Comment by iandrus created at 2011-03-26 01:10:19

I have added `spkg-test` to run valgrind's test suite (which fails for me on OS X 10.6.7).

I created 2 suppression files sage.supp which is the same file as before and sage-liberal.supp which is enough to suppress all the errors caused by sage startup.  When testing you can set `MEMCHECK_FLAGS` to change the suppression file you use.  In #11035 I plan to patch sage-valgrind to be able to switch between the two easily.

The default for the moment is to use the same suppression file as before, so it should be 'safer'.


---

Comment by iandrus created at 2011-03-26 01:10:19

Changing status from needs_work to needs_review.


---

Comment by drkirkby created at 2011-04-27 21:07:56

I changed the title to indicate the ticket now upgrades to 3.6.1 rather than 3.6.0.svn. Personally I think upgrading to svn snapshots is generally a bad idea, as those are less tested than official releases. But I know sometimes its not possible to use a stable release. 

Dave


---

Comment by SimonKing created at 2011-12-25 21:21:01

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2011-12-25 21:21:01

The package does not work for me (on `openSUSE 12.1 "Asparagus"`). It fails with

```
checking for a supported OS... ok (linux-gnu)
checking for the kernel version... unsupported (3.1.0-1.2-desktop)
configure: error: Valgrind works on kernels 2.4, 2.6
error configuring valgrind 3.6.1

real    0m2.260s
user    0m0.347s
sys     0m0.382s
************************************************************************
Error installing package valgrind-3.6.1
************************************************************************
Please email sage-devel (http://groups.google.com/group/sage-devel)
explaining the problem and including the relevant part of the log file
  /home/simon/SAGE/sage-4.8.alpha3/spkg/logs/valgrind-3.6.1.log
```



---

Comment by kini created at 2011-12-25 21:43:14

Yes, this was fixed in 4.7.0. ("275278  valgrind does not build on Linux kernel 3.0.* due to silly" in the changelog). So we apparently need a newer spkg now.


---

Comment by kini created at 2011-12-25 21:45:07

Er, sorry, I meant 3.7.0.


---

Comment by iandrus created at 2012-02-10 17:31:45

I created a new spkg from 3.7.0 which can be found at http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.spkg

I would like to get this reviewed since the current valgrind package is at 3.3.1 and doesn't support OS X or 3.x linux kernels.  I ran some doctests under valgrind on my machine and things worked (well there were lots of leaks, but...).


---

Comment by iandrus created at 2012-02-10 17:31:45

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2012-02-16 15:15:15

I guess that make should be replaced by $MAKE in both spkg-check and spkg-install.

The SAGE_LOCAL logic should also be added to spkg-check.

Some message should be printed if tests fail.

The updated changelog in SPKG.txt is wrong (3.6.1 instead of 3.7.0).

I guess the hg log could contain this ticket number at the beginning (#7766: ...)

Moreover the spkg should be named .... .p0.spkg.

Otherwise it looks fine.

I'll test the package now.


---

Comment by jpflori created at 2012-02-16 15:15:15

Changing status from needs_review to needs_work.


---

Comment by jpflori created at 2012-02-16 15:43:38

It runs fine on my quite common amd64 debian system.


---

Comment by iandrus created at 2012-02-16 21:25:14

Changing status from needs_work to needs_review.


---

Comment by iandrus created at 2012-02-16 21:25:14

Replying to [comment:18 jpflori]:
> I guess that make should be replaced by $MAKE in both spkg-check and spkg-install.

Done.

> The SAGE_LOCAL logic should also be added to spkg-check.

It probably doesn't need it since it will run after spkg-install succeeded, but I added it anyway since it's safer than way.  Is there a way to run the tests of an already installed package?

> Some message should be printed if tests fail.

Done.

> The updated changelog in SPKG.txt is wrong (3.6.1 instead of 3.7.0).

Oops.

> I guess the hg log could contain this ticket number at the beginning (#7766: ...)

Good point.

> Moreover the spkg should be named .... .p0.spkg.

I thought I read that if there were no patches to upstream then we weren't supposed to put the `.p0` on it, but I changed it since I don't really know.

Thanks for taking the time to review this.


---

Comment by iandrus created at 2012-02-16 21:26:49

I forgot to say the updated spkg is at http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.p0.spkg .


---

Comment by jpflori created at 2012-02-16 22:28:13

About the p0, the problem was that the directory inside the archive was named with a p0 but not the spkg itself so sage would not find it after decompression.

So removing the p0 from both might be a better choice :)

For the check I'm not aware of any way to do that without rebuilding the package but I might have missed something. But if the build dir is deleted after installation that might be impossible anyway.


---

Comment by iandrus created at 2012-02-17 07:33:10

Replying to [comment:22 jpflori]:
> About the p0, the problem was that the directory inside the archive was named with a p0 but not the spkg itself so sage would not find it after decompression.
> 
> So removing the p0 from both might be a better choice :)

Oh I see now.  Let me know if you want me to change it.  I don't know how big of a deal having a `.p0` or not is.


---

Comment by jpflori created at 2012-02-24 11:26:38

Could you just post the diff with the previous patch here, "just for review"?

After that, I'll be completely happy with the ticket.


---

Comment by jpflori created at 2012-02-24 11:27:27

Let's also remove the p0, while we are at it.


---

Comment by jpflori created at 2012-02-24 12:02:59

I've made the mentioned changes and some minor other changes. I've also updated the descr/license in the SPKG file.

The updated spkg is at [http://perso.telecom-paristech/~flori/sage/valgrind-3.7.0.spkg](http://perso.telecom-paristech/%7Eflori/sage/valgrind-3.7.0.spkg) 

Ivan: If you don't mind, it may be a good idea to add yourself as a maintainer?

If you do agree, or if you don"t as wel, I'll put this as positive review.


---

Comment by iandrus created at 2012-02-24 15:22:17

Replying to [comment:26 jpflori]:
> I've made the mentioned changes and some minor other changes. I've also updated the descr/license in the SPKG file.
> 
> The updated spkg is at [http://perso.telecom-paristech/~flori/sage/valgrind-3.7.0.spkg](http://perso.telecom-paristech/%7Eflori/sage/valgrind-3.7.0.spkg) 

FWIW I had to add `.fr` to the server to get the spkg.

> Ivan: If you don't mind, it may be a good idea to add yourself as a maintainer?

Yeah, I can be a maintainer.  I took your spkg and added myself as maintainer in SPKG.txt.  New version is at 

http://boxen.math.washington.edu/home/iandrus/valgrind-3.7.0.spkg

Your patches look good BTW.

> If you do agree, or if you don"t as wel, I'll put this as positive review.

Excellent.  Thanks again.


---

Comment by jpflori created at 2012-02-24 16:23:47

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-02-25 16:57:10

Changing status from positive_review to needs_work.


---

Comment by jdemeyer created at 2012-02-25 16:57:10

In `SPKG.txt`, `valgrind_3.7.0` should be `valgrind-3.7.0`


---

Comment by jpflori created at 2012-02-25 18:31:21

Changing status from needs_work to needs_review.


---

Comment by jpflori created at 2012-02-25 18:31:21

I corrected the last version name as well as all the old ones.

Package available at http://perso.telecom-paristech.fr/~flori/sage/valgrind-3.7.0.spkg


---

Attachment

spkg diff, for review only


---

Comment by jdemeyer created at 2012-02-28 12:40:54

*Update the ticket description if you post a new package*


---

Comment by jdemeyer created at 2012-02-28 12:40:54

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-03-03 14:01:52

Resolution: fixed
