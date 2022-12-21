# Issue 2: Notebook locking

Issue created by migration from Trac.

Original creator: wstein@gmail.com

Original creation time: 2006-09-11 04:04:32

Assignee: somebody

Currently it is possible to run two SAGE notebooks on the same directory,
which is potentially VERY VERY bad.  It would be better if when a SAGE
notebook server starts up it checks for the presence of a lock file.  This
file would contain the pid of a running SAGE notebook process -- if the file
and that process exist, then the notebook won't start.  When the notebook
finishes it should delete that lock file. 


---

Comment by justin@mac.com created at 2006-09-11 16:26:49

A thought: PIDs live in a fairly small space, so it might be worth doing some kind of check to verify that the process corresponding to the PID is a SAGE notebook process.

Alternate approach: instead of just bailing, ask the user whether to continue (and remove the existing lock file), or quit.  That puts the burden on the user instead of the programmer, but the results may be better.


---

Comment by boothby created at 2006-09-14 21:24:25

Rather than keep a PID, a more robust solution would be to write the URL to the notebook in the lockfile.  Upon startup, the server would send a request to that URL -- if there's already a running server, just return.

If we also stored the PID, we could attempt to kill nonresponsive servers.


---

Comment by nbruin created at 2007-01-24 05:29:15

One could end up with an NFS filesystem and notebooks running on distinct machines. If the port listened on is only a local one on machine A then sending a request from machine B will not confirm that the process is still running.

This is a bad thing to happen, but not unlikely if someone has sage installed in their homedir and moves from machine A to machine B.


---

Comment by mabshoff created at 2007-08-23 11:01:54

Changing component from basic arithmetic to notebook.


---

Comment by mabshoff created at 2007-08-23 11:01:54

Changing assignee from somebody to boothby.


---

Comment by was created at 2007-08-24 05:30:56

This was fixed decades ago!


---

Comment by was created at 2007-08-24 05:30:56

Resolution: fixed
