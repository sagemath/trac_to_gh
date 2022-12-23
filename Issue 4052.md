# Issue 4052: [with patch; needs review] readline spkg doesn't build under OpenBSD

Issue created by migration from https://trac.sagemath.org/ticket/4052

Original creator: anakha

Original creation time: 2008-09-03 19:01:06

Assignee: anakha

The spkg-install script looks for the library file libreadline.so, but under OpenBSD, no symbolic link is made and the only file that appears is libreadline.so.5.2.

The attached patch is a little hack to allow successful completion on OpenBSD, but if there is a better and more general method available, please inform me.


---

Attachment


---

Comment by mabshoff created at 2008-09-03 19:16:50

Patch looks good to me.

Note that an updated spkg should have an updated entry in SPKG.txt. Not all spkgs have an SPKG.txt, but in that case one should add them.

Cheers,

Michael


---

Attachment

The new patch adds an entry to the SPKG.txt file.

Also is there special procedure to bump the patch version of a spkg?


---

Comment by mabshoff created at 2008-09-03 19:38:01

Replying to [comment:2 anakha]:
> The new patch adds an entry to the SPKG.txt file.

Thanks.

> Also is there special procedure to bump the patch version of a spkg?

You need to rename the directory to the updated patchlevel and then recreate the spkg. There is nothing more to it :)

Feel free to create spkgs, but please do not attach them to trac, put post a link. A diff would still be appreciated to make the review process easier.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-04 01:39:19

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc0/readline-5.2.p4.spkg

contains the fixes.


---

Comment by mabshoff created at 2008-09-04 01:39:28

Merged in Sage 3.1.2.rc0


---

Comment by mabshoff created at 2008-09-04 01:39:28

Resolution: fixed
