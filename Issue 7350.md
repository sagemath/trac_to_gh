# Issue 7350: notebook (sagenb); implement a more secure multi-computer server model

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-29 16:53:40

Assignee: boothby


```
When the notebook server evaluates an input cell, the following now happens:

    (1) The notebook server writes the code to be evaluated to
/tmp/randomstuff/code.py (or something like that).
    (2) The worksheet process (which is being controlled over ssh)
changes its current directory to /tmp/randomstuff, which is world
writable.
    (3) The code is run which produces output, including output to
stdout and the creation of files (e.g., images).
    (4) The output is copied back to the private notebook server's
directory, which is *not* world writable.  Unfortunately, some of this
directory is world-readable right now, only because of the DATA
directories.
   (5) The tmp/randomstuff directory is deleted.

As you can see, the vandal-style damage that a user can do is vastly
more limited now.   It used to be the case that any user could delete
any files of any other user that happened to have been created by the
same worksheet process.  Now, even if the server pool has only one
account, there is only a very tiny window of opportunity for the user
to do something malicious (i.e., right when another user is evaluating
some code, maybe the code.py file could be changed, or the output
files be deleted).   Moreover, the worksheet process can be setup so
it only has write permissions on /tmp/ (i.e., don't give them a home
directory), and /tmp/ can be made a RAM disk.

In the near future I'll also fully support the worksheet processes
running on several completely separate virtual machines, which NSF
mount various /tmp directories, say /tmp0, /tmp1, /tmp2, etc.
Worksheet processes could then be assigned on a round-robin basis to
the virtual machines round-robin, and the virtual machines (and
corresponding /tmp) can be reset to their default state once per hour
(say).    Moreover, I can add a feature so in step (4) above, any file
beyond a certain size is flagged and not copied (instead, replaced by
a warning).    Morever, the server could limit the total maximum
number of worksheets a given user has to some hard coded limit.

I think the above design would mostly mitigate successfully against
every malicious attack I've personally heard of on the notebook.
Obviously, somebody could do something nasty to one machine for up to
one hour, but that's it.   The design scales well, in that even if n
users are trying to factor huge numbers (i.e., a seriously CPU bound
computation), the machine on which the notebook server runs is not
slowed down at all by this, since all computations run on a different
machine.    I would also imagine that adding or removing machines from
the pool could be done dynamically without having to restart the
notebook server.

If one removes support for the DATA directory, then the requires of
having a shared NFS /tmp directory could be removed, which would
significantly increase flexibility.  (I only mean that there could be
a way to start the notebook server without the DATA functionality, but
with more flexible worksheet processes, not that DATA would be gone in
any other modes.)

The above design would be complementary to everything currently
available -- i.e., it doesn't require changing any existing setups, if
you don't want to.

CREDIT: Martin Albrecht, Yoav Aner, and I came up with the above
design with  over dinner in Barcelona this summer.
```



---

Comment by boothby created at 2020-03-29 02:12:30

Resolution: invalid


---

Comment by boothby created at 2020-03-29 02:12:30

Closing deprecated notebook tickets
