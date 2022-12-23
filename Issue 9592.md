# Issue 9592: Upgrade lcalc to pari 2.4.3

Issue created by migration from https://trac.sagemath.org/ticket/9592

Original creator: jdemeyer

Original creation time: 2010-07-24 11:57:12

Assignee: tbd

CC:  cremona

After upgrading PARI/GP to version 2.4.3 (#9343), lcalc no longer compiles properly.


---

Attachment


---

Comment by jdemeyer created at 2010-07-24 13:10:55

Changing assignee from tbd to jdemeyer.


---

Comment by jdemeyer created at 2010-07-24 13:10:55

New version which works with PARI 2.4.3: [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p1.spkg)

I have also notified the upstream contact Michael Rubinstein and sent him the patch lcalc-newpari.patch


---

Comment by mpatel created at 2010-08-13 11:21:14

The patch level for the new spkg should be 2, since we used p1 for #9665.  This should fix the "already installed" problem reported by John Cremona in [comment:ticket:9343:180 comment 180] at #9343.


---

Comment by leif created at 2010-08-13 11:55:40

Replying to [comment:5 mpatel]:
> The patch level for the new spkg should be 2, since we used p1 for #9665.  This should fix the "already installed" problem reported by John Cremona in [comment:ticket:9343:180 comment 180] at #9343.

Just noticed that, too. :)

There are also post-merge comments at #9665, I don't know if they should be included here or if there's even a new ticket for these.


---

Comment by leif created at 2010-08-13 15:06:45

Jeroen, could you describe in more detail which failure(s) this ticket is intended to fix (including Sage version, operating system, processor etc.)?

John Cremona has successfully installed and tested #9343 (unintentionally) *without* this new spkg, and I've also successfully installed the other to spkgs and applied the patches from #9343 on top of Sage 4.5.3.alpha0 + #9475 and #9717 on Fedora 13 x86 (Pentium 4 Prescott, gcc 4.4.4).

Of course lcalc wasn't (re)built in the above tests. (I'll try that later, currently running `ptestlong` without the lcalc package from here.)


---

Comment by leif created at 2010-08-13 15:35:24

Just for the record: `SPKG.txt` currently lacks a _Dependencies_ section, the package has no `spkg-check`, and `spkg-install` uses `make`, not `$MAKE`...


---

Comment by leif created at 2010-08-13 16:13:18

In addition, it contains at least two or three files that should be deleted: some `*.bak` file, a `*.swap.crap` file and some static library (`*.a`) I think we don't need (correct me if I'm wrong here).

(In case Jeroen's patch here is now obsolete due to a meanwhile newer PARI version at #9343, which John Cremona is currently investigating, we could recycle this ticket to address the above mentioned issues.)


---

Comment by cremona created at 2010-08-13 16:23:26

Updated spkg: [http://www.warwick.ac.uk/staff/J.E.Cremona/lcalc-20100428-1.23.p2.spkg](http://www.warwick.ac.uk/staff/J.E.Cremona/lcalc-20100428-1.23.p2.spkg)

(This version is based on lcalc-20100428-1.23.p1.spkg as merged in 4.5.2)

I made this before seeing the recent comments here.  Feel free to add the Dependencies section etc  -- I will not have time to do that for at least a day.


---

Comment by mpatel created at 2010-08-13 21:31:22

Replying to [comment:6 leif]:
> There are also post-merge comments at #9665, I don't know if they should be included here or if there's even a new ticket for these.

I've added a note at #9665 about this ticket.


---

Comment by drkirkby created at 2010-08-13 23:23:32

I've changed the title and description a bit, to reflect the fact that #9343 is *not* Pari 2.4.3. 

Not even Pari 2.4.2 has ever been released - there is only an alpha of that available. 

Dave


---

Comment by leif created at 2010-08-13 23:31:38

Replying to [comment:12 drkirkby]:
> I've changed the title and description a bit, to reflect the fact that #9343 is *not* Pari 2.4.3. 

You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-)


---

Comment by drkirkby created at 2010-08-14 00:00:39

Replying to [comment:14 leif]:
> Replying to [comment:12 drkirkby]:
> > I've changed the title and description a bit, to reflect the fact that #9343 is *not* Pari 2.4.3. 
> 
> You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-) 
I don't know where it is. In any case, it should not be a .p2, since the current one in Sage is lcalc-20100428-1.23.p0.spkg, to a revision should be called lcalc-20100428-1.23.p1.spkg. 

I hope the 

`gcc -Wa,-W` 

(to suppress warnings from the assembler), has not got back in, as -W is not recognised by the Sun assembler and it creates an error. 

Dave


---

Comment by leif created at 2010-08-14 00:19:05

Replying to [comment:15 drkirkby]:
> Replying to [comment:14 leif]:
> > Replying to [comment:12 drkirkby]:
> > > I've changed the title and description a bit, to reflect the fact that #9343 is *not* Pari 2.4.3. 
> > 
> > You should perhaps have updated the spkg link to point to John Cremona's new p2 spkg, too. ;-) 
> I don't know where it is. In any case, it should not be a .p2, since the current one in Sage is lcalc-20100428-1.23.p0.spkg, to a revision should be called lcalc-20100428-1.23.p1.spkg.

Browser cache issue?

See http://trac.sagemath.org/sage_trac/ticket/9592#comment:10 (where)

and http://trac.sagemath.org/sage_trac/ticket/9592#comment:5 (why).

(lcalc-20100428-1.23.p1.spkg from #9665 was merged into Sage 4.5.2.rc1)


---

Comment by jdemeyer created at 2010-08-14 10:04:56

I removed some .DS_Store and ._.DS_Store files from John's spkg and uploaded the result to [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg)


---

Comment by rishi created at 2010-08-14 12:02:07

I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.


---

Comment by rishi created at 2010-08-14 12:02:07

Changing status from new to needs_review.


---

Comment by rishi created at 2010-08-14 12:32:30

Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.

http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg


---

Comment by leif created at 2010-08-14 12:36:46

Replying to [comment:19 rishi]:
> I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.

Perhaps do some of the clean-up I [suggested above](http://trac.sagemath.org/sage_trac/ticket/9592#comment:8)?

There are further minor things (like the date/version at the top of `spkg-install`; `SAGE_DEBUG=yes` usually disables optimization, unquoted environment variables, etc.).

I wonder if we should add (a) further patch(es) to get rid of some of the annoying warnings (cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:191 ff.), but we probably shouldn't do too much at this ticket.

I'm not sure if Cygwin support is required yet... ;-)


---

Comment by leif created at 2010-08-14 12:39:52

Replying to [comment:20 rishi]:
> Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.
> 
> http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg

Could you upload an spkg patch for your changes (except file deletions) here?

It's a bit more convenient for reviewing and adding further changes...


---

Comment by jdemeyer created at 2010-08-14 12:42:07

Replying to [comment:20 rishi]:
> Following suggestion of Mitesh, I have small some small cleaning up of unnecessary files in patches and few lines in spkg-install over the changes of jdemeyer.
> 
> http://sage.math.washington.edu/home/rishikesh/lcalc/lcalc-20100428-1.23.p2.spkg

I copied your spkg to [http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg](http://cage.ugent.be/~jdemeyer/sage/lcalc-20100428-1.23.p2.spkg) (like this, I don't have to update the descriptions of #9343 and #9592).


---

Attachment

I am not sure what you want to be done. Can you make the changes and attach it here.

Replying to [comment:21 leif]:
> Replying to [comment:19 rishi]:
> > I can see that this spkg does not depend on the upgrade to the new pari. This can be included before the latest version of pari is accepted. In couple of month, I will try to get Mike to use autotools for building. This will eliminate a lot of problems with spkg as of now. I am changing the status to needs review if it is ok with you.
> 
> Perhaps do some of the clean-up I [suggested above](http://trac.sagemath.org/sage_trac/ticket/9592#comment:8)?
> 
> There are further minor things (like the date/version at the top of `spkg-install`; `SAGE_DEBUG=yes` usually disables optimization, unquoted environment variables, etc.).
> 
> I wonder if we should add (a) further patch(es) to get rid of some of the annoying warnings (cf. http://trac.sagemath.org/sage_trac/ticket/9343#comment:191 ff.), but we probably shouldn't do too much at this ticket.
> 
> I'm not sure if Cygwin support is required yet... ;-)


---

Comment by mpatel created at 2010-08-19 11:13:58

Changing priority from major to blocker.


---

Attachment

Complete spkg patch (for reference)


---

Comment by mhansen created at 2010-08-21 18:43:11

I've made an spkg that builds on Cygwin at #9775 based on the one here.  It might make more sense to make any additional changes to the SPKG there.


---

Comment by mpatel created at 2010-09-02 10:14:26

Replying to [comment:27 mhansen]:
> I've made an spkg that builds on Cygwin at #9775 based on the one here.  It might make more sense to make any additional changes to the SPKG there.

See #9845, too.


---

Comment by mpatel created at 2010-09-02 10:29:08

Rishi, do Jeroen's changes look good to you?  If they are, I suggest that we leave further changes for other tickets.


---

Comment by leif created at 2010-09-03 22:52:17

Also, the `dist/` (Debian) directory should be removed, cf. #5903.


---

Comment by mpatel created at 2010-09-04 07:32:55

Replying to [comment:31 leif]:
> Also, the `dist/` (Debian) directory should be removed, cf. #5903.

I suggest that we do this at #9845, unless we otherwise need to update the package here.


---

Comment by leif created at 2010-09-04 09:01:27

Replying to [comment:32 mpatel]:
> Replying to [comment:31 leif]:
> > Also, the `dist/` (Debian) directory should be removed, cf. #5903.
> 
> I suggest that we do this at #9845, unless we otherwise need to update the package here.

Yes; hopefully #9845 gets reviewed soon s.t. this ticket won't get merged at all (positively reviewed though), since the former contains all changes from here.


---

Comment by mpatel created at 2010-09-09 11:06:44

Do we have a positive review here?


---

Comment by leif created at 2010-09-09 12:50:14

Doesn't bother *me*, but should we keep

```sh
# disable Cygwin build for now
if [ "$UNAME" = "CYGWIN" ]; then
#    cp ../../patches/Lcommandline_elliptic.cc .
    echo "Sorry, the lcalc build is currently broken"
    echo 1
fi
```

*?* (In case I by luck have looked at the current `.p2` / its current patches/diffs.)

Fortunately there's a follow-up ticket to address the rest...


---

Comment by mpatel created at 2010-09-10 11:19:02

Is `patches/Lcommandline_elliptic.cc.cygwin.diff` up to date?  Do we still use `patches/Lcommandline_elliptic.cc.cygwin.*`.  Let's do any necessary updates at #9845.


---

Comment by mpatel created at 2010-09-10 11:19:02

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-10 11:19:19

Resolution: fixed
