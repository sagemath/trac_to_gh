# Issue 9609: Remove unnecessary files from spkg/standard

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-07-27 07:28:42

Assignee: GeorgSWeber

CC:  ddrake

[Dan Drake wrote on sage-release](https://groups.google.com/group/sage-release/browse_thread/thread/b6fd67d4d4543129/9e68e7105e23ab29#9e68e7105e23ab29):

```
In SAGE_ROOT/spkg/standard, with 4.5.alpha0, I see:

$ ls | grep -v spkg
total 303320
-rw-r--r-- 1 drake drake       43 Jun 28 09:36 README.txt
-rw-r--r-- 1 drake drake    18614 Jul 25 20:52 deps
-rw-r--r-- 1 drake drake      163 Jun 28 09:36 libdist_filelist
-rwxr-xr-x 1 drake drake     1571 Jun 28 09:36 newest_version*
-rw-r--r-- 1 drake drake      977 Jun 28 09:36 notes.txt
-rw-r--r-- 1 drake drake      383 Jun 28 09:36 numeric-24.2.txt

The files libdist_filelist, notes.txt, and numeric-24.2.txt seem like leftover notes that. Can I delete them? 
```


The files `libdist_filelist`, `notes.txt`, and `numeric-24.2.txt` [have been removed from Sage 4.5.2.alpha1](https://groups.google.com/group/sage-release/browse_thread/thread/9455213e89f94692):

```
The second unreviewed change is the deletion of several extra files in spkg/standard, as I mentioned in https://groups.google.com/group/sage-release/t/b6fd67d4d4543129. In the unlikely case that those files were important or necessary, we can just copy them from the alpha0 tarball. 
```


This ticket is for reviewing the change.


---

Comment by mpatel created at 2010-07-27 08:33:42

Possibly related:

```sh
$ cd SAGE_LOCAL/bin
$ grep libdist *
sage-libdist:libdist_filelist = open('%s/spkg/standard/libdist_filelist'%r
sage-libdist:    if len(ext) > 1 and not name_without_version in libdist_filelist:
sage-libdist:This is the readme for sage-libdist, which is the
sage-libdist:libdist = 'sage-libdist%s'%r[i:]
sage-libdist:if os.path.exists(libdist):
sage-libdist:    os.system('rm -rf %s'%libdist)
sage-libdist:os.system('mv %s %s'%(r,libdist))
sage-libdist:os.system('tar -cvf %s.tar %s'%(libdist,libdist))
sage-libdist:os.system('rm -rf %s'%libdist)
sage-sage:   "$SAGE_ROOT"/local/bin/sage-libdist sage-$2.tar
sage-sdist:cp -p $PKGDIR/$STD/libdist_filelist $TMP/$PKGDIR/$STD/
```

But I can't investigate further right now.


---

Comment by jhpalmieri created at 2010-07-27 15:21:41

As part of the file "sage-sage":

```
   echo "sage -ldist currently disabled"
   echo "To work on it, remove the exit after this message in SAGE_ROOT/local/bin/sage-sage"
```

So sage-libdist is not currently active.  I think that we should keep the file libdist_filelist just in case.  In my opinion, the other two files can be removed, but I don't know their history.  You might ping William about this.


---

Comment by jhpalmieri created at 2010-07-27 15:50:44

Also, as mpatel points out: the script sage-sdist tries to copy libdist_filelist, so that may break with this file missing.


---

Comment by ddrake created at 2010-07-28 01:22:47

Okay, it looks like we should put libdist_filelist back in (and then, in my opinion, find out why it's there and if possible, open a ticket for removing it and the parts of the scripts that reference it).

The numeric-24.2.txt is a short description of a Python module that we don't ship. Even if we did include it, I can see no reason why such a file should be kept in spkg/standard.

notes.txt refers to the sage_c_lib package, which no longer exists, and to a very outdated version of linbox. The libtool information in that file should be kept in the linbox spkg and/or put on the wiki.

I think we can resolve this ticket by just putting libdist_filelist back.


---

Comment by jhpalmieri created at 2010-07-28 02:18:06

Sounds good to me.  We can always recover the other files from an old tarball if we ever need them.


---

Comment by jhpalmieri created at 2010-07-28 02:18:06

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-07-28 02:18:14

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-29 04:53:56

I'm including 4.5.2.alpha0's `spkg/standard/libdist_filelist` in 4.5.2.rc0.


---

Comment by mpatel created at 2010-07-29 04:53:56

Resolution: fixed
