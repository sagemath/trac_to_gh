# Issue 1731: SAge mac app

Issue created by migration from https://trac.sagemath.org/ticket/1731

Original creator: was

Original creation time: 2008-01-09 06:54:44

Assignee: mabshoff

From NASA:


```
Hi,

Thanks for Sage - it's awesome. I need to convince my coworkers to
switch from their proprietary programs to Sage.

I've attached a little script that uses the Platypus program
(http://www.sveinbjorn.org/software) to bundle the sage directory
into a clickable Mac application. It has some code to update the
SAGE_ROOT variable so that things still work if a user drags the
program around.

My code is public domain, so feel free to use it if you like it.
```



---

Attachment


---

Comment by mabshoff created at 2008-02-10 10:40:26

Some more info from http://groups.google.com/group/sage-devel/t/c181f8ccde549cdd:

```
 rpmuller@gmail.com     	
View profile
	 More options Feb 9, 3:20 am
From: "rpmul...@gmail.com" <rpmul...@gmail.com>
Date: Fri, 8 Feb 2008 18:20:32 -0800 (PST)
Local: Sat, Feb 9 2008 3:20 am
Subject: Mac-like application for Sage on Mac
Reply | Reply to author | Forward | Print | Individual message | Show original | Remove | Report this message | Find messages by this author
I remember reading somewhere when I downloaded a version of Sage that
the program was soliciting help from mac-experts in making the binary
version of Sage a little more mac-like.

I'm certainly not a mac expert. However, I got Sage working through a
mac-like icon using the Platypus program (http://www.sveinbjorn.org/
platypus). There's a good article here (http://www.tuaw.com/2007/05/08/
platypus-create-mac-binaries-from-ruby-perl-shell-scripts-et/) about
how to use the program here. But it's kinda nice. Among other
programs, the Gimp.app program uses Sage for it's Mac application
bundle.

I created a shell script that looks like this:

#!/bin/sh
cat > startsage << EOF
notebook()
EOF
/Users/rmuller/Programs/sage-2.10/sage < sage

and had Platypus run it, putting the output into a text window. This
runs the notebook() function and the twisted server, and pops open the
browser with the Sage notebook.

The drawback is that the script needs to know the path to my sage
installation. I think that the workaround to this is to actually put
the entire Sage installation in the folder that Platypus creates for
the application. OS X applications on the Mac are actually folders
(unix directories).

Does this sound like it would be useful to the Sage community if I
could get it working? 
```



---

Comment by mabshoff created at 2008-02-15 23:36:02

Please check out http://wiki.sagemath.org/SageMacApplication for more information on the whole "Sage Application on OSX" issue.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-30 06:27:42

In https://groups.google.com/group/sage-support/t/9bff2799e1ae4885 Greg Landweber suggested:

```
You don't need any fancy droplets or applets. You can just use the
following AppleScript to activate Sage (take this script and save it
as an AppleScript application, then put it in the same directory as
the "sage" UNIX executable):

tell application "Finder"
        set myFolder to container of (path to me) as string
end tell

tell application "Terminal"
        activate
        do script (POSIX path of myFolder) & "sage"
end tell

If on the other hand you want to start the notebook and don't need the
terminal window in front, you can use the following AppleScript to
open a terminal window in the background and start Sage in notebook
mode:

tell application "Finder"
        set myFolder to container of (path to me) as string
end tell

tell application "Terminal"
        do script (POSIX path of myFolder) & "sage --notebook"
end tell

What else did you folks have in mind in terms of Mac OS X integration?

-- Greg 
```


Cheers,

Michael


---

Comment by malb created at 2009-01-22 22:34:24

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2009-02-08 03:20:23

Resolution: fixed


---

Comment by mabshoff created at 2009-02-08 03:20:23

Fixed via #4817. Improvement should be done on top of that codebase.

Cheers,

Michael
