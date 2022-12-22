# Issue 3761: don't allow a sage binary to run if the processor instruction set doesn't support everything that was on the machine where sage was built

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-08-02 20:06:01

Assignee: cwitty

Having this in sage-support nearly *every day* is getting really old:


```
i get to install sage in my xubuntu (ubuntu with xfce) but when i try
to do a simple plot, i get this error message

xinelo`@`chacal:~/packages/sage-3.0.5-i686-Linux$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
The SAGE install tree may have moved.
Regenerating Python.pyo and .pyc files that hardcode the install PATH
(
it at most a few minutes)...
Please do not interrupt this.
Setting permissions of DOT_SAGE directory so only you can read and
writ
| SAGE Version 3.0.5, Release Date: 2008-07-11                       |
| Type notebook() for the GUI, and license() for information.        |
ILLEGAL INSTRUCTION...
someone can help me?
thanks
```


I propose that on linux systems when the script that
does the "The SAGE install tree may have moved." stuff is run,
Sage also does this:

```
sage`@`modular:~$ cat /proc/cpuinfo |grep flags|tail -1
flags           : fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 syscall nx mmxext lm 3dnowext 3dnow up
```

and if there are any flags that were on the system where sage was -bdist'd, but which aren't on the current machine, then a big message that this binary won't work is displayed.




---

Attachment


---

Comment by malb created at 2008-08-10 13:14:50

The patch contains functions without doctests. Though, it might be a bit hard to add doctests since the result is random-ish, they should be there and marked `random`.


---

Comment by mabshoff created at 2008-08-10 18:41:17

The patch looks nice and I disagree with malb about the doctests since this is the scripts repo. But what should be added is the automatic generation of $SAGE_ROOT/local/lib/sage-flags.txt of -bdist since otherwise the flags file will not exist (unless created my moving the install), so it will not be really useful.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 00:27:28

Actually: Why would the flags file be rewritten when the Sage install was moved? That would mean that after each install on the new target machine the file would be written and the test would always pass, not fixing the problem at all.

We should write the file *once* after building Sage, i.e. the creation should be part of the build process. Even -upgrade should not change the flags since -upgrade might only build parts of Sage, i.e. not upgrading ATLAS during -upgrade would still cause problems.

Cheers,

Michael


---

Comment by mvngu created at 2008-10-27 04:00:13

For the patch *scripts-3761.patch*, here are some possible documentation fixes:



1.

```
-moved make sure the location and processor flags files are
+moved, make sure the location and processor flags files are
```

So after applying that diff, you'd get this documentation snippet:

```
"""
Check whether or not this install of Sage moved.  If it hasn't 
moved, make sure the location and processor flags files are 
written. 
""" 
```

I know I'm nit-picking, but the second sentence is rather long. Leaving out the extra comma won't change what you're trying to say with that sentence. But it can take some time for readers (including yours truly) to figure out what you're saying. I think the extra comma would make it easier to read your documentation.



2.

```
-# On a system without /proc/cpuinfo, so don't bother In
+# On a system without /proc/cpuinfo, so don't bother. In
```



---

Comment by was created at 2008-11-09 23:46:12

I've made no changes to this patch.  Michael has refused to give it a positive review, since he claims (in the review above and in person) that the flags file is deleted and rewritten whenever the install moves.   However, he's wrong.   I just read the code and there is exactly *one* place that the flags file is written:

```
        16          # Write the flags file if it isn't there. 
 	17	    if not os.path.exists(flags_file): 
 	18	        write_flags_file() 
```

Since flags_file is never deleted, and is only written when the flags_file doesn't exist, it can't be deleted or overwritten when the install moves.   So I don't see what the problem is.

William


---

Comment by GeorgSWeber created at 2008-11-10 22:25:15

Hi William,
>I just read the code and there is exactly *one* place that the flags file is written
yeah, but that might be too late. Take the following use case:

- unpack a Sage src distribution

- type "make" in the SAGE_ROOT directory

- type "./sage -bdist Test" in that directory

and you get a binary distribution which lacks the flags_file, rendering its introduction pretty useless.

The whole point is that the "sage-location" script, where the flags file is written, is never called in the above sequence.

Michaels first post says implicitly he would like to have the "sage-bdist" script call "sage-location" (say right at its start). His second post says he would like to have "sage-location" being called somewhere in the build process started by "make", say in the script "spkg/install" right after the line "time make -f standard/deps $1" near the end.

IMHO it would be a good idea to do both. I give a positive review to this ticket provided these two trivial one-liners are added.

(Someone actually should have tested the case of moving such a protected Sage distro from one Linux system to another Linux system where the new protection mechanism barfs about missing flags. I can't do it myself because currently I have only very limited access to some Linux system. OTOH, the worst thing to happen is that we get "false positives". This is the current situation, so there ... let's include this code until someone has a better solution.)

Cheers,

gsw


---

Comment by was created at 2008-11-11 19:55:59

> and you get a binary distribution which lacks the flags_file, rendering its 
> introduction pretty useless.

> The whole point is that the "sage-location" script, where the flags file 
> is written, is never called in the above sequence. 

Wrong?  The step

```
  - type "make" in the SAGE_ROOT directory
```

at some point involves running Sage, and once Sage is run the sage-location script gets called. 

William


---

Comment by mabshoff created at 2008-11-11 20:53:47

Mhh:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.2.rc1/local/bin$ patch -p1 < scripts-3761.patch\?format\=raw 
patching file sage-location
Hunk #1 FAILED at 2.
Hunk #2 FAILED at 130.
2 out of 2 hunks FAILED -- saving rejects to file sage-location.rej
```


Cheers,

Michael


---

Attachment


---

Comment by was created at 2008-11-12 03:51:38

I posted a rebased patch.  Let me know if there are any problems.


---

Comment by GeorgSWeber created at 2008-11-12 09:25:49

>>     and you get a binary distribution which lacks the flags_file, rendering its >>introduction pretty useless.
>>
>>    The whole point is that the "sage-location" script, where the flags file is >>written, is never called in the above sequence.
>
>Wrong? The step

```
  - type "make" in the SAGE_ROOT directory
```

>at some point involves running Sage, and once Sage is run the sage-location script gets called.
>
>William

I was sure I checked that this was not the case, i.e. Sage itself was not started during the "make" run ... I'll double check it again with Sage 3.2.rc0 as soon as I get home this evening. Thanks for rebasing the patch!

Cheers, gsw


---

Comment by GeorgSWeber created at 2008-11-12 22:12:39

Begging your pardon, but I just did:

```
susanne-webers-computer:~/Public/sage georgweber$ tar -xf sage-3.2.rc0.tar
susanne-webers-computer:~/Public/sage georgweber$ cd sage-3.2.rc0
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ make
.
.
SAGE build/upgrade complete!
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt
ls: local/lib/*.txt: No such file or directory
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls ../sage-3.2.alpha2/local/lib/*.txt
../sage-3.2.alpha2/local/lib/sage-current-location.txt
```

So Sage cannot have been called during the "make" run, otherwise the "sage-location" script would have been called.

(The last two lines show that I did run Sage at least once with my former Sage 3.2.alpha2 copy.)

I intend to post another ticket with the trivial one-liner patch I proposed in a minute, but before I do that, I just have to check whether my potential fix for trac #4500 works, that I have created, while waiting for the "make" run to complete.


---

Comment by GeorgSWeber created at 2008-11-13 00:16:49

No other ticket because I don't know how to post a patch for the file "spkg-install" in the spkg "sage_scripts-3.2.rc0".

But the patch I had in mind is trivial: Just add one line at the end of this script with "sage-location" (actually a call) on it, thus calling the "sage-location" script once during installation, at a time where we definitely know it exists.

Michael, William, what do you think?

Cheers, gsw


---

Comment by was created at 2008-11-13 01:31:31

> But the patch I had in mind is trivial: Just add one line 
> at the end of this script with "sage-location" (actually a 
> call) on it, thus calling the "sage-location" script once 
> during installation, at a time where we definitely know it exists.
> Michael, William, what do you think?
> Cheers, gsw 

Since sage_scripts is basically the first thing installed during the sage build from source process, I'm worried that won't work.  In fact, it definitely won't on some systems, because the first line of sage-location is:

```/usr/bin/env sage.bin
```


I'm surprised that sage is never run during "make"; it certainly used to be run, which resulted in some complaints (since people building as root were annoyed that /root got modified).   That said, you're right and I'm glad you pointed this out!! It not being run never broke the sage-location stuff for me, since my scripts to build the Sage binaries always do "make check" before making the binary (a very good idea!), and that of course runs Sage.   I mean, in my opinion it would be really dumb to ever do "sage -bdist" without once starting Sage, since you could be building a binary that certainly doesn't work. 

What about adding a line to sage-bdist to run Sage once?  And even checking that the run actually worked, since that's a good test, and refusing to make the bdist if Sage won't even run. 

 -- William


---

Comment by was created at 2008-11-13 01:32:29

apply this after the scripts patch above.  This makes sure that "sage -bdist" runs Sage at least once before building the bdist.


---

Attachment

I attached a patch that makes sure sage runs right when one does "sage -bdist".


---

Comment by GeorgSWeber created at 2008-11-13 09:34:34

Agreed, positive review.

`@`Michael: I have access to a Sage installation only in ~ 10 hours from now on, so I could only "code-review" the PART2 - patch. I don't think there is much space for a typo in it to break it for a trivial reason, but one never knows. Please either wait half a day, I do intend do see that "alive and working" with my own eyes, or just test it out yourself. ("rm $SAGE_ROOT/local/lib/*.txt" and then "sage -bdist" ...)

Cheers, gsw


---

Comment by GeorgSWeber created at 2008-11-13 20:19:04

Sigh.

Anything that isn't tested will not work. QED.

Several issues remain, to show just two:

```
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt
ls: local/lib/*.txt: No such file or directory
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ./sage -bdist
** MISSING VERSION NUMBER! ** 
Sage works!
Usage: /Users/georgweber/Public/sage/sage-3.2.rc0/local/bin/sage-bdist <SAGE_VERSION> <SAGE_ROOT>
susanne-webers-computer:~/Public/sage/sage-3.2.rc0 georgweber$ ls local/lib/*.txt
ls: local/lib/*.txt: No such file or directory
```

Apart from the annoying fact that the fat error message is displayed, and then the job continues and calls ' sage -c "print 'Sage works!'" ' nevertheless, this latter command does not seem to call "sage-location" ... and we're trapped in the "make" run behaviour again.

It is pretty obvious who to heal the "Part2" patch for sage-bdist, and now I'll turn things round: this time I'm really going to that myself, and then let somebody else review it :-)


---

Comment by GeorgSWeber created at 2008-11-13 20:41:03

apply this after the scripts patch above. This makes sure that "sage -bdist" runs Sage at least once before building the bdist. Hopefully now really ...


---

Attachment

OK, here we go:

I give the "sage-location" patch of William a positive review (apply only the rebased one) pending an epsilon --- a PART2 patch is needed.

I give the "sage-bdist" PART2 patch of William a negative review (reason: see my post above).

I kindly ask for my own "sage-bdist" PART2fixed patch (to be applied together with the first patch) to be reviewed, so yet another of the thousands of tickets can finally be closed in O(1) time --- on a positive review of this Part2fixed patch, the remaining epsilon is supplied, thus giving the ticket as such a positive review.

Cheers, gsw

(goes off and fetches a beer)


---

Comment by was created at 2008-11-13 23:39:52

I agree that my original patch didn't work, but that was because of a bug in sage-sage.   Your patch scripts-3761-PART2fixed-bdist.patch just programs around that bug instead of fixing it.    The bug is that `sage -c "..."` doesn't run sage-location.  This came up when I was fixing #4515, so the first patch there fixes this bug.  After applying that patch (the first at #4515), one should apply the following:

```
scripts-3761-3.2.alpha3.patch
scripts-3761-PART2-bdist.patch
```



---

Comment by was created at 2008-11-14 00:34:58

> Cheers, gsw
> (goes off and fetches a beer) 

If I recall correctly, last time we had a beer together it was non-alcoholic :-)


---

Comment by GeorgSWeber created at 2008-11-14 22:16:22

OK, I'm fine with he redefinition of "epsilon" to mean "sage-4515-sage_c_bug.patch".

Since I just gave the entire #4515 a positive review, next try:

Positive review for this ticket (Wiliams two patches) pending the prior inclusion of #4515.

`@`William: I couldn't possibly make it to Loria (nice photos of you all, by the way!), but I surely do intend to attend some SD xy. Anyway, hope to see you again!

Cheers, gsw


---

Comment by mabshoff created at 2008-11-15 04:58:21

Resolution: fixed


---

Comment by mabshoff created at 2008-11-15 04:58:21

Merged scripts-3761-3.2.alpha3.patch and scripts-3761-PART2-bdist.patch in Sage 3.2.rc1
