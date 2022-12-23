# Issue 9026: Issues preventing 64-bit builds on various flavors of Solaris.

Issue created by migration from https://trac.sagemath.org/ticket/9026

Original creator: drkirkby

Original creation time: 2010-05-24 00:14:01

Assignee: drkirkby

CC:  dimpase jsp mvngu jhpalmieri robertw was

The following is list of the issues that are currently preventing Sage build on either

 * OpenSolaris (aka Solaris 11) on Intel/AMD x64. (e.g. 'disk')
 * Solaris 10 on Intel/AMD (e.g. 'fulva')
 * Solaris 10 on SPARC (e.g. 't2')

The list can be added as new problems are found, making what William calls a 'metaticket' 

Please put 
 * "yes" if the trac ticket is known, or one might reasonably expect it to cause a problem on a particular platform.
 * "no" if one knows the problem does not exist on that platform, or one reasonably expect it will not be an issue. 
 * "unknow" if one can not determine if it will be an issue. 

Although OpenSolaris can run on the SPARC platform, very few people run it, so there is little to be gained by tracking issues on that platform. (David Kirkby does not have OpenSolaris installed on any of his SPARC systems)



---

Comment by jhpalmieri created at 2010-07-12 23:09:15

As part of this project, we should update the "supported platforms" information, wherever it appears.  For example, in the installation guide, it says

```
Complete compilation of Sage is currently not supported on Solaris
```

According to the "search_doc" function, the main occurrences of the string "Solaris" are in the file "devel/sage/doc/en/installation/source.rst", so that's the only part of the docs that we need to fix.  The file SAGE_ROOT/README.txt says that Solaris on sparc is officially supported, but not Solaris on x86_64.  I'm guessing that this is still accurate.  There are probably assorted wiki pages about supported platforms, too. In any case, it would be good to maintain a single official list of supported platforms, instead of having conflicting information in different locations.


---

Comment by drkirkby created at 2010-07-13 00:07:33

Replying to [comment:24 jhpalmieri]:
> As part of this project, we should update the "supported platforms" information, wherever it appears.  For example, in the installation guide, it says
> {{{
> Complete compilation of Sage is currently not supported on Solaris
> }}}
> According to the "search_doc" function, the main occurrences of the string "Solaris" are in the file "devel/sage/doc/en/installation/source.rst", so that's the only part of the docs that we need to fix.  The file SAGE_ROOT/README.txt says that Solaris on sparc is officially supported, but not Solaris on x86_64.  I'm guessing that this is still accurate. 

Yes, that is still true. 

> There are probably assorted wiki pages about supported platforms, too. In any case, it would be good to maintain a single official list of supported platforms, instead of having conflicting information in different locations.

I agree, though that is a different issue to this ticket, which is for build problems on 64-bit Solaris. The supported platforms issue needs resolving for Solaris, as it does for Linux, OS X and Windows. I created  #9487 to cover this.

Dave


---

Comment by drkirkby created at 2010-08-02 22:22:10

John, 
I see you updated the table to include #9358. Note however note the comments above.

Please put
    * "yes" if the trac ticket is known, or one might reasonably expect it to cause a problem on a particular platform.
    * "no" if one knows the problem does not exist on that platform, or one reasonably expect it will not be an issue.
    * "unknown" if one can not determine if it will be an issue. 

So the znpoly issue should have a "yes" in the first column. I've also tried to keep them in order of trac number, though that's not a big deal. 

Perhaps changing "yes" -> Bug and No->OK might be sensible, as I can see this could be confusing. That would be trivial to change with a sed script. What do you think of that, or can you think of a better, less confusing solution? 

Dave


---

Comment by jhpalmieri created at 2010-08-02 22:47:35

Well, znpoly builds fine on t2, so shouldn't there be a "no" in the first column?  It has problems 64-bit on t2, so "yes" in the second column.  The third column is the only one I should probably change, to "unknown", since I don't know how znpoly behaves on OpenSolaris.  Maybe you know about that, though?


---

Comment by jhpalmieri created at 2010-08-02 22:48:31

Oh, I see the whole ticket is 64-bit specific.  Never mind.


---

Comment by drkirkby created at 2010-08-02 23:37:31

Replying to [comment:30 jhpalmieri]:
> Oh, I see the whole ticket is 64-bit specific.  Never mind.

We could add a couple of columns, for 32-bit OpenSolaris and 32-bit Solaris 10 x86. I wanted to avoid having. Obviously the title would need changing, but that is no big deal. What do you think to that - put them all on one ticket?


---

Comment by drkirkby created at 2010-08-02 23:39:10

Replying to [comment:31 drkirkby]:
> Replying to [comment:30 jhpalmieri]:
> > Oh, I see the whole ticket is 64-bit specific.  Never mind.
> 
> We could add a couple of columns, for 32-bit OpenSolaris and 32-bit Solaris 10 x86. I wanted to avoid having.

I did not finish that sentence. Just forget it. It seems to me adding a couple of columns might be sensible. 

Dave


---

Comment by mkoeppe created at 2020-04-01 14:09:35

Should be closed as outdated.


---

Comment by mkoeppe created at 2020-04-01 14:09:35

Changing status from new to needs_review.


---

Comment by dimpase created at 2020-04-01 14:10:23

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-01 14:48:46

Resolution: invalid


---

Comment by chapoton created at 2020-04-01 14:48:46

agreed
