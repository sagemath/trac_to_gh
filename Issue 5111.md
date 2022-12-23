# Issue 5111: axiom --> fricas

Issue created by migration from https://trac.sagemath.org/ticket/5111

Original creator: was

Original creation time: 2009-01-27 20:33:05

Assignee: was

Change axiom.py to fricas.py and the axiom command to fricas.  

This is more logical since the doctests test fricas not axiom.  Also, this has been specifically requested by Tim Daly -- the trademark owner on the name Axiom -- and I think it is best to respect his request.


---

Comment by was created at 2009-02-18 04:32:42

Changing priority from major to blocker.


---

Comment by was created at 2009-02-18 04:40:14

It's been brought up that this may be a bad idea, since after all we still have an axiom interface.  The purpose of this ticket is this:

  * gather results from discussion and possible voting
  * decide what if any change to make
  * make said change


---

Comment by was created at 2009-02-18 04:44:55


```
20:41 < wstein> On the other hand, if Tim Daly really is the trademark owner of axiom, can't he
20:41 < wstein> just tell us we can't use the name and that is that?
20:41 < cwitty> I don't think so.
20:41 < cwitty> He can tell us we can't call our product axiom.
20:42 < cwitty> He can probably tell us we can't call fricas axiom, which is closer to what we're doing.
20:43 < mhansen> cwitty: We're actually just calling whatever "axiom" command happens to be on the system.
```



---

Attachment


---

Comment by mhansen created at 2009-02-19 17:41:34

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-19 17:41:34

Changing assignee from was to mhansen.


---

Comment by mhansen created at 2009-02-19 17:41:34

Note that this applies on top of the ReST patches so it should not go in until those are in.

Also, this patch includes the changes found in #4036.


---

Comment by mhansen created at 2009-02-19 17:42:30

Also, all of the axiom() commands pass tests with the January 2009 release of Axiom.


---

Comment by bpage created at 2009-02-23 17:11:55

Mike,

I do not understand the reference to "ReST patches". Are these in or out of sage-3.3? Bottom line: Can your patch be applied directly to sage-3.3?

Bill.


---

Comment by mabshoff created at 2009-02-23 17:42:57

Replying to [comment:6 bpage]:
> Mike,

Hi Bill,

> I do not understand the reference to "ReST patches". Are these in or out of sage-3.3? Bottom line: Can your patch be applied directly to sage-3.3?

No. The ReST patches are about 35 tickets work of documentation fixes that will go into 3.4. It will be out before the weekend, so you might want to wait until then to play with this. Note that 3.4.alpha0 ought in about 24 hours ought to contain all the ReST patches, so that might be something you could use for review.

Cheers,

Michael

> Bill.


---

Comment by bpage created at 2009-02-25 05:39:22

Mike,

Thanks. I have successfully applied this patch to sage-3.4.alpha0 and have just begun testing. I noticed however that patch returned the warning:

patching file sage/structure/sage_object.pyx
Hunk #1 succeeded at 305 (offset 7 lines)

So I guess there has already by some code drift.

The first bug I noticed was that

  ./sage -fricas

does not start a FriCAS session.

  ./sage -axiom

however still starts FriCAS even though /usr/local/axiom has been replaced with a dummy script.

I guess this command line processing must be done in some other part of sage?

Regards,
Bill Page.


---

Comment by bpage created at 2009-02-25 17:36:02

Mike,

On my Debian 5.0 (Lenny) x86 system I have not been able to compile recent versions of Axiom from source using the instructions here:

  http://axiom.axiom-developer.org/axiom-website/download.html

I get build errors early in the process. What did you use to get the "January 2009 release of Axiom" referred to in your tests?

After installing the binary version of Axiom via

```
  apt-get install axiom
```

I do get the older "2005" version of Axiom which does seem to run ok (known problems with Hyperdoc etc. notwithstanding). However this version seems to have pexpect synchronization problems.

```
  sage: axiom('1+1')

  sage:
```

returns no visible result, while

```
  sage: fricas('1+1')
  2
  sage:
```

behaves as expected.

I think the problem is probably caused by the differences in readline behavior under gcl and/or minor differences in the initial prompts. I am not sure how to handle this so long as we depend on an externally installed version of Axiom. If Sage is going to continue to support Axiom as an option, perhaps some effort needs to be given to creating an optional Axiom spkg ... (Don't look at me! :-). Otherwise, I would not be against getting rid of the 'axiom' function all together.

On this same subject: What consideration, if any, has been given to providing a similar interface for OpenAxiom? Does anyone want this?

Regards,
Bill Page.


---

Comment by mhansen created at 2009-02-25 17:43:07

Replying to [comment:9 bpage]:
> Mike,
> 
> On my Debian 5.0 (Lenny) x86 system I have not been able to compile recent versions of Axiom from source using the instructions here:
> 
>   http://axiom.axiom-developer.org/axiom-website/download.html
> 
> I get build errors early in the process. What did you use to get the "January 2009 release of Axiom" referred to in your tests?

I just used the binary found here: http://www.axiom-developer.org/axiom-website/downloads/axiom-ubuntu64-jan2009-bin.tgz


> 
> After installing the binary version of Axiom via
> {{{
>   apt-get install axiom
> }}}
> I do get the older "2005" version of Axiom which does seem to run ok (known problems with Hyperdoc etc. notwithstanding). However this version seems to have pexpect synchronization problems.

Yes, this is not too surprising.

> I think the problem is probably caused by the differences in readline behavior under gcl and/or minor differences in the initial prompts. I am not sure how to handle this so long as we depend on an externally installed version of Axiom. If Sage is going to continue to support Axiom as an option, perhaps some effort needs to be given to creating an optional Axiom spkg ... (Don't look at me! :-). Otherwise, I would not be against getting rid of the 'axiom' function all together.

I think Camm is updating the version of Axiom in Debian.  It'd be silly not to have some support since it's very little extra work.

> On this same subject: What consideration, if any, has been given to providing a similar interface for OpenAxiom? Does anyone want this?

I don't know -- I don't really use this software.  It should be pretty trivial to add support for.


---

Attachment


---

Comment by bpage created at 2009-02-26 00:07:41

Here is a patch (trac_5111b.patch) that disables readline support for Axiom. With this change the axiom interface now works for me.

Also, I discovered that I was able to compile Axiom from the January 2009 source tarball. I still have a problem compiling the git or cvs head version on Debian 5.0.

Re: Axiom binaries on Debian instead of an spkg. Is there any other case in Sage where an interface is provided from something that is not available for install as an spkg? I thought this might be a Sage policy.


---

Comment by mhansen created at 2009-02-26 00:13:49

Replying to [comment:11 bpage]:
> Here is a patch (trac_5111b.patch) that disables readline support for Axiom. With this change the axiom interface now works for me.

Cool!  Thanks for the fixes (and typo catches).

> Re: Axiom binaries on Debian instead of an spkg. Is there any other case in Sage where an interface is provided from something that is not available for install as an spkg? I thought this might be a Sage policy.

Yeah, there are plenty of things like that.  For example, all of the proprietary math software interfaces :-)

--Mike


---

Comment by cwitty created at 2009-04-19 04:09:28

I did a fairly fast skim of the code (I didn't study it), and tested the axiom interface on my computer (against an old version of axiom).  A couple of doctests failed with slightly different printing than expected (probably because the axiom version was old; the answer was correct, only the printing was wrong), but almost all of them passed.

Positive review (apply both patches).


---

Comment by mabshoff created at 2009-04-24 01:00:23

Merged both patches in Sage 3.4.2.alpha0.

Cheers,

Michael


---

Comment by mabshoff created at 2009-04-24 01:00:23

Resolution: fixed
