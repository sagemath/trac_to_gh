# Issue 4308: mpc spackage

Issue created by migration from Trac.

Original creator: thevenyp

Original creation time: 2008-10-16 15:27:23

Assignee: mabshoff

I am planning to add arbitrary precision complex numbers using the MPC library
http://www.multiprecision.org/mpc/.

Here is a sage package based
http://www.loria.fr/~thevenyp/mpc-0.5.spkg



---

Comment by mabshoff created at 2008-10-18 12:09:13

I will review the spkg later on today.

Cheers,

Michael


---

Comment by robertwb created at 2008-10-30 21:42:29

Do we have any sage interface code to go with this yet? I know some was produced at Sage days 10. 

Then these extensions should be added based in whether or not this package is installed `sage.misc.package.is_package_installed()`.


---

Comment by mabshoff created at 2008-10-30 23:22:51

Bindings are being written. The spkg should become optional so it is easily buildable from any Sage install. Once/If mpc is standard the mpc.spkg would also become standard.

Cheers,

Michael


---

Comment by AlexGhitza created at 2008-11-22 07:59:12

See #4446 for a patch implementing a partial interface (still work in progress).


---

Comment by was created at 2008-11-27 17:51:21

REFEREE REPORT:

1. There is no .hg repository in the spkg.  You need to

```
$cd mpc-0.5
$ hg init
$ hg add spkg-install spkg-check SPKG.txt
```


2. The SPKG.txt doesn't list anybody or any contact info under "package maintainer". 

3. The SPKG.txt has an empty changelog.  This should at least list exactly which version of upstream is in the src subdirectory.   Typically when refereeing a patch, I like to verify that src/ contains the claimed upstream exactly, since I don't want some virus crap sneaking in.

4. Speaking of crap, the src/src/ subdirectory is full of .o pre-compiled binary object files.  These need to all be deleted.

```
teragon-2:src wstein$ pwd
/Users/wstein/tmp/mpc-0.5/src/src
teragon-2:src wstein$ ls -1 *.o |wc -l
      57
```



---

Comment by thevenyp created at 2008-11-28 17:14:24

Thanks for your review, the spkg has been changed accordingly.

Regards,

Philippe


---

Comment by mabshoff created at 2008-11-30 05:33:44

Hi Philippe,

I have reviewed your updated spkg. A couple comments:

 * Everything looks good, but some minor details I fixed
 * Checked in the changes you added to the repo in your name
 * added a .hgignore and added some small cleanups to spkg-install

I also deleted the attached spkg since large files should not be attached to trac, but linked from some webspace. 

The updated spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.1/rc1/mpc-0.5.p0.spkg

In case you improve/update the mpc.spkg please use that one as a base.

Summary: positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-30 05:35:16

Resolution: fixed


---

Comment by mabshoff created at 2008-11-30 05:35:16

Uploaded to the optional spkg repo.

Cheers,

Michael
