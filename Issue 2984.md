# Issue 2984: ITANIUM (RHEL 5) -- turn off all unaligned access messages

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-21 03:37:37

Assignee: mabshoff


```
20:30 < wstein|afk> See this page: http://kbase.redhat.com/faq/FAQ_105_9111.shtm
20:30 < wstein|afk> It says "These messages are informative only. When any application performs an unaligned 
                    access, the processor traps into the kernel and the kernel emulates the unaligned access. 
                    The program will work correctly however there will be a performance hit, as emulating the 
                    unaligned memory access is a software operation and not a hardware operation."
20:30 < mabshoff> ok
```


This will not be needed once #2209 is done, I hope. 


---

Comment by mabshoff created at 2008-04-21 04:17:20

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-21 04:17:20

Changing component from Cygwin to porting.


---

Comment by mabshoff created at 2008-04-21 04:17:20

I am testing the fix, but this will take a while.

Cheers,

Michael


---

Comment by was created at 2008-04-21 05:36:28

Patch up here:
  http://sage.math.washington.edu/home/was/patches/gap-4.4.10.p7.spkg


---

Comment by mabshoff created at 2008-04-21 06:53:17

Spkg looks good to me, the fix works. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-21 06:53:29

Resolution: fixed


---

Comment by mabshoff created at 2008-04-21 06:53:29

Merged in Sage 3.0.rc1
