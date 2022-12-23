# Issue 1601: issue with noclobber and building sage

Issue created by migration from https://trac.sagemath.org/ticket/1601

Original creator: was

Original creation time: 2007-12-27 01:16:55

Assignee: cwitty


```

 > Hi, William,
 >
 > I have had trouble getting the most recent versions of sage to
 > compile.  (This is Mac OS X 10.4.11, gcc 4.0.1, 5367.)  My problem
 > started with 2.8.15, and continued with 2.9.  Eventually, I found out
 > that something (I can't figure out what just yet) is returning the
 > string "noclobber", which in turn is being passed along as an argument
 > to local/bin/sage-spkg.
 >
 > After the line
 >
 >     PKG_BASE=`echo "$PKG_NAME" | sed -e "s/-.*//"`
 >
 > I added
 >
 >     if [ $PKG_SRC == "noclobber" ]; then
 >       exit 0
 >     fi
 >
 > which cleared up the problem; otherwise, sage tries (and obviously
 > fails) to compile noclobber.spkg.
 >
 > I wish that I had the time to track down which environment variable or
 > alias is causing the problem.  This has something to do with
 > redirecting output, and specifically 2>&1 as an option to some
 > command.  I never quite worked out where the problem is, and I don't
 > think that my work-around could be harmful, so I suggest that you
 > include it in the next release.--Rob
 >

Hi,

I found out that I had the line "set noclobber" in both my .bashrc and
.bash_profile files.  Removing that cleared up the problem.  I have no
clue why I ever put added the line in the first place, nor why it
would have caused a problem.--Rob
```



---

Comment by mabshoff created at 2008-02-18 17:07:29


```
[17:47] <mabshoff> wstein-2190: Who is "Rob" from #1601?
[17:47] <wstein-2190> Rob Gross; a number theorist at Boston College.
```



---

Comment by mabshoff created at 2008-02-18 17:58:46

Changing assignee from cwitty to mabshoff.


---

Comment by mabshoff created at 2008-02-18 17:58:46

Changing status from new to assigned.


---

Attachment


---

Comment by mabshoff created at 2008-02-18 21:28:36

Resolution: fixed


---

Comment by mabshoff created at 2008-02-18 21:28:36

Merged in Sage 2.10.2.alpha1
