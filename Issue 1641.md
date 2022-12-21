# Issue 1641: Make ATLAS restart build on tolerance error

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-12-30 18:47:05

Assignee: mabshoff

When the ATLAS build fails due to tolerance errors we can restart the build by restarting the build process via "make". We should do it a set number of times, i.e. 5 and then finally fail. I have hit the problem repeatedly while building in a VMWare machine and have little to no control to prevent the issue from happening. 

Cheers,

Michael


---

Comment by mabshoff created at 2007-12-31 10:24:00

Changing status from new to assigned.


---

Comment by mabshoff created at 2009-02-20 13:40:29

This ought to be fixed via #5311.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 20:59:46

Resolution: fixed


---

Comment by mabshoff created at 2009-02-20 20:59:46

Fixed via #5311. This can probably be improved upon, but we will open another ticket once we get to this point.

Cheers,

Michael


---

Comment by was created at 2009-02-21 03:38:52

Resolution changed from fixed to 


---

Comment by was created at 2009-02-21 03:38:52

REFEREE REPORT:

 * There is a typo "Restartig build for the first time"

 * This patch doesn't work.  I tried this on my vmware farm and what happens is that you restart part of the build that fails, but other parts also fail later.  

 * I wonder if it would be better to simply wrap the whole spkg-install in a repeat timer instead of each little bit.  I.e., put the current spkg-install in another file, say spkg-install-script and then make spkg-install try to run spkg-install-script, then wait some amount of time, and try again up to n times.


---

Comment by was created at 2009-02-21 03:38:52

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-02-21 05:04:17

Replying to [comment:5 was]:
> REFEREE REPORT:
> 
>  * There is a typo "Restartig build for the first time"

Ok.

>  * This patch doesn't work.  I tried this on my vmware farm and what happens is that you restart part of the build that fails, but other parts also fail later.  

The failures you reported are unrelated to this script: For example the ubuntu64.out failure for 3.3.rc3:

```
<SNIP>
ATLAS install complete.  Examine 
<SNIP>
Finished building ATLAS
<SNIP>
make[3]: [install_lib] Error 1 (ignored)
make[3]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/atlas-3.8.3/ATLAS-build'
make[2]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/atlas-3.8.3/ATLAS-build'
ATLAS failed to build because your system is too heavily loaded to obtain accurate timing.
Please restart the build by typing make, when the load on your system has decreased.
```

 
So ATLAS did finish tuning and some other error was triggered after the "make install" target, so this is not this tickets fault. 

>  * I wonder if it would be better to simply wrap the whole spkg-install in a repeat timer instead of each little bit.  I.e., put the current spkg-install in another file, say spkg-install-script and then make spkg-install try to run spkg-install-script, then wait some amount of time, and try again up to n times. 

If you do that you will not reuse the tuning info, but start the tune from scratch each time. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-21 05:17:22

Ok, I figured it out I think: on debian32 this happens: 



```
   STAGE 2-1-5: GEMV TUNE 
make -f Makefile INSTALL_LOG/dMVRES pre=d 2>&1 | ./xatlas_tee 
INSTALL_LOG/dMVTUNE.LOG 
make[3]: *** [build] Error 255 
make[3]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/ 
atlas-3.8.3/ATLAS-build' 
make[2]: *** [build] Error 2 
make[2]: Leaving directory `/space/wstein/farm/sage-3.3.rc3/spkg/build/ 
atlas-3.8.3/ATLAS-build' 
ATLAS failed - round 1 - sleeping  5 minutes 
```

Then the restart kicks in and finishes the build. 

```
Restartig build for the first time 
make[2]: Entering directory `/space/wstein/farm/sage-3.3.rc3/spkg/ 
build/atlas-3.8.3/ATLAS-build' 
make -f Make.top build 
make[3]: Entering directory `/space/wstein/farm/sage-3.3.rc3/spkg/ 
build/atlas-3.8.3/ATLAS-build' 
cd bin/ ; make xatlas_install 
<SNIP> 
```


Because at some point there was  a failure the makefile errors out at 
the very end even though it all worked. So the script you wrote is 
likely to hit the same bug unless you completely clean out the ATLAS 
build directory. 

The fix here is to figure out which file causes the tuning failure 
message in the end and to get rid of it before restart. 

Thoughts? 

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-21 06:28:15

The latest spkg is at:

http://sage.math.washington.edu/home/was/patches/atlas-3.8.3.p0.spkg

Two things need fixing:

 * spkg-install claims up to 10 tries, but max_tries is set to 5 :)
 * SPKG.txt overwrites my 3.8.3 entry, but William's changes need to be 3.8.3.p0:

```
-=== atlas-3.8.3 (Michael Abshoff, Januar 2nd, 2009) ===
- * rebase against latest upstream (#5311)
- * make ATLAS automatically restart build on tolerance error (#1641)
+=== atlas-3.8.3 (William Stein, February 20, 2009) ===
+ * implement up to 5 auto-restarts with random timeouts. 
```


The 3.8.3 entry also needs to be dated February 20th, but that was my bug.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-21 07:03:24

The bug in my 3.8.3.spkg was actually not killing error* in ATLAS's build directory on restart:

```
cd $CUR/ATLAS-build
if [ -f error* ]; then
   echo "ATLAS failed to build because your system is too heavily loaded to obtain accurate timing."
   echo "Please restart the build by typing make, when the load on your system has decreased."
   exit 1
fi
```


That error message is wrong by the way since not every failure is due to timing issues - even though these days for ATLAS 99.9% of the time an error indicates a tolerance failure. 

I still think an incremental restart is better than start from scratch, i.e. think of being two hours into a tune on Sparc or Itanium and it blows up. I have made this #5328.


---

Comment by was created at 2009-02-21 08:58:39

I think the new spkg at 

http://sage.math.washington.edu/home/was/patches/atlas-3.8.3.p0.spkg

addresses all of the above comments.


---

Comment by mabshoff created at 2009-02-21 09:06:49

Positive review. All my concerns have been addressed. 

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-21 09:42:13

Resolution: fixed


---

Comment by mabshoff created at 2009-02-21 09:42:13

Merged in Sage 3.3.final.

Cheers,

Michael
