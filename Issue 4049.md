# Issue 4049: Don't use the -i option to tar as it does not exist on most BSDs

Issue created by migration from Trac.

Original creator: anakha

Original creation time: 2008-09-03 17:59:15

Assignee: cwitty

While trying to compile sage under OpenBSD, the first problem I encountered was that it could not extract the spkgs because it passes the -i option to tar which is not recognized.  

After reading the description of the meaning of that option on a linux man page:

 `--ignore-zeros'
 `-i'
      With this option, `tar' will ignore zeroed blocks in the archive,
      which normally signals EOF. 

And additional information about what is a zero block:

 Normally, `tar' stops reading when it encounters a block of zeros
 between file entries (which usually indicates the end of the archive).
 `--ignore-zeros' (`-i') allows `tar' to completely read an archive
 which contains a block of zeros before the end (i.e. a damaged archive,
 or one which was created by concatenating several archives together).

I concluded that unless some spkgs are created by concatenating several tar archives together this option can be safely removed.

If there is a consensus to keep the option, I could always make a new patch 


---

Comment by anakha created at 2008-09-03 18:03:35

About the new patch, I meant a new patch that only removes the option on systems where it is not supported.


---

Comment by mabshoff created at 2008-09-03 18:10:25

Changing assignee from cwitty to anakha.


---

Attachment

Patch looks good to me. Positive review.

One general problem with Sage is that we depend on gnumake and gtar in a couple places. The shell scripts we use also assume GNUisms in a couple places, but I would be more than happy to get those wiped out.

For now I would suggest copying gmake into $SAGE_LOCAL/bin and rename it make. You should also treat gld and gas the same way for now.

Cheers,

Michael


---

Comment by anakha created at 2008-09-03 18:21:42

Until now, the regular make has not given me any errors.  I had to install bash though.  I will try to use the native system binaries as much as possible and only revert to the gnu ones if it fails too much.

Otherwise, expect more reports like this one to remove GNUisms where it makes sense.


---

Comment by mabshoff created at 2008-09-03 18:26:39

Replying to [comment:3 anakha]:
> Until now, the regular make has not given me any errors.  I had to install bash though.  I will try to use the native system binaries as much as possible and only revert to the gnu ones if it fails too much.
> 
> Otherwise, expect more reports like this one to remove GNUisms where it makes sense.

freetype and eclib for now require gmake. We use bash for now and do not really plan to switch to a pure sh env since sh on Solaris is pretty broken. At least on FreeBSD the default location of bash is in /usr/local/bin and all shebangs of the scripts should not hard code the /bin/bash location.

We should continue this discussion on sage-devel though :)

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 00:31:38

Merged in Sage 3.1.2.rc0 - and I merged the patch into both repos, i.e. spkg/base, too.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 00:31:38

Resolution: fixed
