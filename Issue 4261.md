# Issue 4261: sympow Configure fails to handle aliases

Issue created by migration from https://trac.sagemath.org/ticket/4261

Original creator: wjp

Original creation time: 2008-10-10 09:43:01

Assignee: mabshoff

CC:  dkohel

The sympow Configure script has a `whichexe` function to determine which `rm`, `grep`, etc to call that effectively does `RM=`which rm``. If `rm` is an alias (e.g., aliased to `rm -i`), this fails.




---

Comment by wjp created at 2008-10-10 12:52:00

Forgot to mention: this was reported by David Kohel in Nancy during SD10.


---

Attachment


---

Comment by mabshoff created at 2008-10-13 09:45:10

This will be fixed in 3.1.3 :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 16:40:55

Sorry that this didn't make it into 3.1.3/4. But I will attempt to get this into 3.2.

Cheers,

Michael


---

Comment by was created at 2008-11-28 05:33:26

REFEREE REPORT:

1. It does not fail is rm is an alias.  It gives the original executable with an exact path. 

```
teragon-2:sympow-1.018.1.p5 wstein$ alias rm="rm -i"
teragon-2:sympow-1.018.1.p5 wstein$ which rm
/bin/rm
teragon-2:sympow-1.018.1.p5 wstein$ RM=`which rm`
teragon-2:sympow-1.018.1.p5 wstein$ echo $RM
/bin/rm
```


So I totally don't get what the problem is.  The above patch would have the effect of making it so the scripts would annoyingly suddenly actually *be* interactive if one has aliased rm to "rm -i".

So from my point of view, it looks like this patch introduces a bug instead of fixing one.

2. This patch would replace all the absolute paths to programs to their names, thus completely removing whatever "upstream's" point was in having those variables.  That's suspicious.

So I'm dubious.


---

Comment by mabshoff created at 2008-11-28 05:38:40

The behavior of "alias" might be shell dependent which might contribute to the problem here. This was initially reported by David Kohel, so let's CC him.

Cheers,

Michael


---

Comment by was created at 2008-11-28 06:05:44


```
Hi,

Based on Mark's remark below, I give #4261 a positive review, since it does
in fact do just what Mark suggests below.

William

On Thu, Nov 27, 2008 at 9:57 PM, Mark Watkins <watkins@maths.usyd.edu.au> wrote:
> William Stein wrote:
>> Do you guy's have any comments on this:
>>    http://trac.sagemath.org/sage_trac/ticket/4261
>> I'm tempted to mark it invalid, but maybe I'm missing the point.
>
> I think I agree that the problem is with the shell-version of alias.
>
> I was only trying to make something that would be more likely to work than
> the simple /bin/rm, etc., but it seems that I failed. Probably it is safe to
> just use $RM=rm (same with $CP, $TAR, $MKDIR, $TOUCH) in the Makefile and
> hope the user has a sufficient path. Also, echo might be shell-dependent.
>
> I think some buildutils simply tree-search the path and/or the
> whole directory structure, but I didn't want to attempt that.
>
> ===
> Mark Watkins
> watkins@maths.usyd.edu.au
>



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org

```



---

Comment by mabshoff created at 2008-11-30 09:00:19

This is going into 3.2.1.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 01:03:47

Wjp's fixes have been merged into 

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/sympow-1.018.1.p6.spkg

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-01 01:04:03

Merged in Sage 3.2.1.rc1


---

Comment by mabshoff created at 2008-12-01 01:04:03

Resolution: fixed
