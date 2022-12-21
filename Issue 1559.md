# Issue 1559: repeated loading of cython file with home on NFS

Issue created by migration from Trac.

Original creator: wjp

Original creation time: 2007-12-18 16:43:02

Assignee: was

When loading a .spyx file with 'load' from the sage: prompt, Sage builds an .so file in ~/.sage/temp/HOST/PID/spyx/FILE/. Before doing this, it tries to unlink all files in that directory. (Search for 'unlink' in sage/misc/cython.py)

When performing the same 'load' again (e.g., while writing/debugging the .spyx file), the previous .so file is deleted, but since it is still held open by python, this causes an .nfs0000... file to appear in the build directory, since my $HOME is mounted over NFS. (This is how the NFS client of Linux works, I assume.)

The third time I do this 'load', it'll try to unlink the .nfs0000... file and fail, since you can't delete such files. This causes the load to fail with "[Errno 16] Device or resource busy".


I'm not sure what the cleanest way of fixing this would be. Two possible solutions that I can think of are explicitly checking for files starting with '.nfs', or ignoring 'device or resource busy' errors while unlinking.




---

Comment by wjp created at 2007-12-18 21:17:12

After discussion with cwitty and mabshoff on IRC:

other solutions include using a directory in /tmp for these temporary files, or
using a new filename for each new module. Something like this last solution might also be necessary for a future Windows port, where it's not possible to delete .dll's that are still in use, as mentioned by mabshoff.


---

Comment by ncalexan created at 2008-01-19 22:12:40

I hate the idea of checking for .nfs files -- that doesn't scale.  I say ignore non-catastrophic errors.

Better still, make it easy to set the temp directory -- so the user can set the temp director to /tmp or something that makes sense.


---

Comment by was created at 2008-01-31 04:54:38

From recreating this ticket (as a dupe, since I never saw it), since it didn't get fixed for a long time:

When

```
 sage: load filename.spyx
```

is done repeatedly on a specific single file filename.spyx, after about 3-4
tries Sage tries to delete some files.  On some NFS mounted filesystems, there
are lock files, and these can't be deleted for permissions reasons.  Instead of 
sage gracefully continuing on it fails at this point, and bombs out.  This makes
loading cython files fail henceforth, making spyx files completely useless.

The fix is probably just to put a try/except block around any code that deletes files that is related to attaching and loading [s]pyx files.

Deleting the temp files is completely not needed -- it's just to save disk space. They'll be cleaned up by the sage-cleaner at some point anyways.


---

Comment by mabshoff created at 2008-03-14 16:35:19

Resolution: duplicate


---

Comment by mabshoff created at 2008-03-14 16:35:19

This is a dupe of #2449.


---

Comment by mabshoff created at 2008-03-14 16:35:47

Ehh, this is a dupe of 2499 - butterfinger ;)
