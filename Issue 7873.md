# Issue 7873: Fix 'gap' to remove usage of '$RM' and replace wth 'rm'

Issue created by migration from https://trac.sagemath.org/ticket/7873

Original creator: drkirkby

Original creation time: 2010-01-08 18:11:13

Assignee: GeorgSWeber

As agreed here:

http://groups.google.com/group/sage-devel/browse_thread/thread/bd7ae07a1157bead/970aa0dc8fa56ab7?lnk=raot

there is no need to have variables for very basic commands such as 'rm'. Gap relies on the use of $RM, $LN and $MKDIR, which seems a bit pointless. All are standard Unix commands, defined by POSIX. We should not make make use of any special options some versions might use. 

I'm no fan of GNU, but even their coding standards acknowledge one can assume some commands exist, and include all of these. 

http://www.gnu.org/prep/standards/standards.html#Utilities-in-Makefiles

Hence I would replace the use of $LN, $RM and $MKDIR on the spkg-install and anywhere else it may be found in gap. 


---

Comment by drkirkby created at 2010-01-08 20:17:44

patch file to replace $RM with 'rm' and similar


---

Attachment

At a new spkg, which fixes these can found at 

http://boxen.math.washington.edu/home/kirkby/portability/gap-4.4.10.p13/gap-4.4.10.p13.spkg


Dave


---

Comment by drkirkby created at 2010-01-08 20:22:42

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-01-08 20:53:09

Two comments: you've changed "$CP" to "cp" even though $CP is still defined in sage-env.  Does this matter?

Also (and this is not new -- it happens with the old spkg, too): when I install the spkg, I get this at the end:

```
cp: ../../bin is a directory (not copied).
cp: cp: No such file or directory
```

Any ideas why?  Anyway, since gap works, maybe we shouldn't worry about this right now.


---

Comment by drkirkby created at 2010-01-08 21:17:23

Replying to [comment:3 jhpalmieri]:
> Two comments: you've changed "$CP" to "cp" even though $CP is still defined in sage-env.  Does this matter?

No. I looked at that before deciding to replace them, but could see no reason not to in this case. One was a simple copy

```
cp patches/gap_cygwin "$SAGE_LOCAL"/bin/gap
```

the other was recursive, but simply used the POSIX compatible '-r' option. There seemed to be no reason to use any other version of cp in such cases. 

The GNU verison of 'cp' has some non-POSIX options (-a being one of them). Had that be iused in gap, then I would have left the $CP, but in this case, with only a very standard option used, there is no reason not to use whatever version of 'cp' is in the path first. Any 'cp' will work. 

> Also (and this is not new -- it happens with the old spkg, too): when I install the spkg, I get this at the end:
> {{{
> cp: ../../bin is a directory (not copied).
> cp: cp: No such file or directory
> }}}
> Any ideas why?  Anyway, since gap works, maybe we shouldn't worry about this right now.

Looking at the 'cp' (or $CP) command I could not work out what spkg-install was trying to do (I just posted something on sage-devel about it). The code simply makes no sense to me. 

Since 
 * The package functions, despite the errors. 
 * I wanted to do it asap, in case it caused an issue with the sage-env ticket (#7818) 
 * I could not work out what was the intended behavior. 'cp' is used in a way I'd never use it. 
 * There is talk on sage-devel of updating gap

it seemed like it was best left to another day. Like the fact CC and CXX get unset. I think it would be wise to find a way around the issues this creates, but again I did not attempt to fix it. That will certainly present a problem if one tried to use a Sun compiler to build gap. 

I'm not even convinced this will work in 64-bit mode on OS X, as it does not have the SAGE64 stuff which every other spkg-install file has. 

So, overall, the changes I made were only necessary ones, and no others. 

Dave


---

Comment by jhpalmieri created at 2010-01-08 21:25:57

It works for me on OS X 10.6, and the changes are obviously the right ones to make.  Positive review.


---

Comment by jhpalmieri created at 2010-01-08 21:25:57

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-01-08 22:39:20

Thank you very much for the positive review.


---

Comment by rlm created at 2010-01-14 02:39:08

Resolution: fixed
