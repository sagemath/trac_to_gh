# Issue 6582: Potential issue in polybori - 0.5rc.p8 and/or  0.5rc.p9

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-07-21 18:55:35

Assignee: tbd

CC:  alexanderdreyer polybori david.kirkby@onetel.net

I believe there is an issue which *may* affect Solaris with polybori 0.5rc.p8, and assuming my patch to .p9 gets positive review, will affect that too, as I have not tried to fix this. 

Here are some notes I put in patches/custom.py



```
# Note, these 'SAGE_DEBUG' linker flags added by someone
# are likely to break if used on Solaris
# with the Sun linker, as -p option to the Sun linker is:
#         [-p auditlib]   identify audit library to accompany this object
# This has not been confirmed, and I don't have time to test it.
# David Kirkby, 21st July 2009. I suggest this is revisited by someone soon.
if os.environ.has_key('SAGE_DEBUG'):
    CPPDEFINES=[]
    CCFLAGS=[" -pg"] + CCFLAGS
    CXXFLAGS=[" -pg"] + CXXFLAGS
    LINKFLAGS=[" -pg"]


```



---

Comment by drkirkby created at 2009-09-28 09:33:04

Another issue, which is this case I am 100% sure about, is that PolyBoRi (as of polybori-0.6.3-20090827.spkg) in sage-4.1.2.alpha4 is that PolyBoRi is sending GNU-specific options to the Sun compiler. See #7034


---

Comment by jdemeyer created at 2012-04-30 10:10:25

Is this still a problem?


---

Comment by AlexanderDreyer created at 2012-04-30 10:56:07

No, it was fixed. For instance, in #12655 for PolyBoRi 0.8.1.


---

Comment by AlexanderDreyer created at 2012-06-25 09:29:23

Changing status from new to needs_review.


---

Comment by AlexanderDreyer created at 2012-06-25 09:29:23

Duplicate of#12655.


---

Comment by AlexanderDreyer created at 2012-06-25 09:29:54

Changing status from needs_review to positive_review.


---

Comment by AlexanderDreyer created at 2012-06-25 09:29:54

Abusing "positive review".


---

Comment by jdemeyer created at 2012-06-25 09:39:07

In such cases, you should set the milestone to "sage-duplicate/invalid/wontfix".


---

Comment by AlexanderDreyer created at 2012-06-25 09:44:39

Replying to [comment:7 jdemeyer]:
> In such cases, you should set the milestone to "sage-duplicate/invalid/wontfix".
Thanks, I'll do so next time.


---

Comment by jdemeyer created at 2012-07-04 07:16:06

Resolution: duplicate
