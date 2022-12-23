# Issue 329: add md5sums for spkgs

Issue created by migration from https://trac.sagemath.org/ticket/329

Original creator: was

Original creation time: 2007-03-22 05:43:18

Assignee: was

CC:  ohanar


```
I've noticed that sage has problems with the integrity of sage-
packages.

Supose that you have patially donwload a file, but for whatever reason
it gets truncated.
Then sage won't check its integrity before installing.

I would sugest adding to each file an md5 sum (or perhaps better a gpg
signtaure, but this could be difficult since we need anybody to be
able to build their own sage packages)
[in a file like package-name.spkg.md5 or package-name.spkg.signature]
and make sage chek this md5sum is correct.
[and if not, download it again]

[Most linux distributions do this somehow, for example Gentoo keeps
md5sums in the manifiests in the portage tree, I think that a good
model also would be Debian. For each package, Debian sources consists
of 3 files:

- package.dsc: a description and the md5sum of the
package.orig.tar.gz, and package.diff.gz for checking the integrity of
the package
- packages.orig.tar.gz: the pristine sources from the upstream author
- the .diff.gz with the modifications specific to debian

(by keeping separated the upstream sources, and the Debian
modifications, Debian makes clear which modifications are specific to
Debian)

I think that sage could adopt a similar aproach for their packages

best regards,
Pablo
```



---

Comment by pdenapo created at 2007-10-15 14:08:48

Changing status from new to assigned.


---

Comment by pdenapo created at 2007-10-15 14:08:48

II'll try to implement this myself.


---

Comment by pdenapo created at 2007-10-15 14:08:48

Changing assignee from was to pdenapo.


---

Comment by was created at 2007-10-23 00:59:00


```
> I think you can easily make tar-archives that contain a checksum, if
> you agree on some extremely mild file naming convention for such a
> checksum (i.e., the archive is not allowed to contain a filename that
> clashes with the file that stores the checksum). Of course, the key is
> that when you add something to the archive, the file changes, so the
> plain md5sum of the total archive changes. You have to md5sum
> something that is easily extracted and independent of the later added
> md5sum. The options -O (dump to stdout), -r (append file) and --
> exclude provide the necessary features for tar.
>
> Procedure for storing a checksum in a tar archive:
> ----------------------------------
> (tar xf file.tar --exclude md5sum.check -O; \
>     tar tvf file.tar --exclude md5sum.check ) | md5sum > md5sum.check
>
> tar -rf file.tar md5sum.check
> ----------------------------------
>
> Procedure for checking that the stored sum agrees with the computed
> one:
> ----------------------------------
> tar xf file.tar md5sum.check -O > storedcheck
> (tar xf file.tar --exclude md5sum.check -O; \
>     tar tvf file.tar --exclude md5sum.check ) | md5sum > computedcheck
>
> cmp storedcheck computedcheck
> ----------------------------------
>
> Note that we need to include the directory listing information as
> well, because the output of -O does not include file names
> (i.e., one could move files around and still have the same checksum)
>
> If it is ever decided that .spkgs should be signed, then you could
> include a .gpg-file via the same procedure.
>

I really like this idea a lot!  It's vastly better -- I think
-- from a usability point of view than having
to constantly pass around .spkg's and .md5 files together.
It will just work 100% automatically and transparently to users,
once we modify some scripts in local/bin/sage-*.

While we're at it, we should make the following work:

1)
  sage -unpkg packagename-version.spkg

which just does tar jxvf and does the above consistency checks.
I suggest sage -unpkg, since making a package is "sage -pkg".
Another option would be "sage -extract blah.spkg", or even
"sage -x blah.spkg".    Please note, sage spkg's can be either
bzip2'd or not, so that has to be taken account of.

2)

  sage -i packagename-version

where packagename-version is the name of a *directory*, does
sage -pkg on the directory, then installs it.
```



---

Comment by khorton created at 2009-05-19 20:44:09

It would be useful to somehow also have a way to check the integrity of tarballs for the whole sage install - i.e. the 200 MB tarball for each sage release.  Twice in the last month I've gotten bitten by build failures caused by corrupted tarballs.  It would have been nice to know the tarball was bad before investing the time to wait for the build + time to troubleshoot the failure.

One option would be to use tar.gz format to distribute sage releases.  There would be no reduction in file size, as most of the tarball consists of already compressed sources, but there would be detection if the tarball had somehow gotten corrupted.  The time required to compress and extract the tarballs is trivial - my 5 year old PPC PowerBook gzips the 200 MB sage tarball in about a minute, and extracts it in less than 30 seconds. 

Rather than trying to reinvent the wheel for spkg formats, it may be worthwhile to consider simply using gzip format.


---

Comment by ddrake created at 2009-06-02 05:04:40

Replying to [comment:4 khorton]:
> Rather than trying to reinvent the wheel for spkg formats, it may be worthwhile to consider simply using gzip format.

Right now, spkgs are just renamed .tar.bz2 files. How does using gzip instead of bzip2 give us corruption detection? Both gzip and bzip2 have `--test` flags; does gzip's test work better?


---

Comment by drkirkby created at 2010-02-22 04:28:06

I think the point made by khorton about using gzip is that if the tar file was gzipped, then gzip would verify the integrity of download, whereas tar does not. 

'md5sum' is not part of POSIX and so you can't assume any 'md5sum' command will exist. Some systems call it 'md5', others 'md5sum'. On some cut-down versions of Linux, I doubt any such command would exist. 

On Solaris I use

```
$ digest -a md5 foobar.c
```


('digest' is part of OpenSSL)

One could use 'cksum' instead of md5. 

http://www.opengroup.org/onlinepubs/009695399/utilities/cksum.html

That will give the same result on any platform, and will always be called cksum. It's *only* a 32-bit number, so one can not be quite as sure as with md5 the file is undamaged, but the probability of a file being corrupted while the output from 'cksum' remains the same is very small. 

Note the 'sum' command can not be used, as that is implementation dependant. But you can be sure cksum will exist on any half-reasonable operating system and that the output will be portable across all platforms. 

Dave


---

Comment by ddrake created at 2010-03-07 07:13:19

Replying to [comment:7 drkirkby]:
> One could use 'cksum' instead of md5. 

I just experimented with this a bit and it seems like a reasonable idea. I propose we use cksum, and if someone gets an invalid spkg that passes the cksum test, we can then think about using something a bit more powerful.

One tiny problem is that cksum on Solaris doesn't produce precisely the same output as on Linux or OS X; it uses a tab character instead of space. (Reading the POSIX spec, this seems to be a minor violation; it looks like you are supposed to use spaces.)

Anyway, we could "normalize" the output by using, say, awk:

```
tar stuff | cksum | awk '{print $1, $2}'
```

which should print out the two fields separated by a space. That works on Linux (Ubuntu 8.04 and 9.10), OS X (bsd.math), Solaris (t2.math), and Cygwin. POSIX says [
http://www.opengroup.org/onlinepubs/009695399/utilities/awk.html default OFS for awk is a space], so we should be safe.

I propose we use cksum instead of md5sum, along with a bit of awk as above. While cksum may not be as strong as md5 sums, it does include the file size, which I suspect would catch a large majority of download errors. I also propose we standardize the filenames and put "spkgname.cksum" into the tarball and output to spkgname.computed.cksum and spkgname.stored.cksum.

Along with the new spkg/md5 (or, I suppose, spkg/cksum) directory proposed at comment:35:ticket:8306, I think we might have something usable and workable for this ticket.


---

Comment by drkirkby created at 2010-03-07 11:05:16

I've not checked in detail, but assuming the 32-bit numbers are randomly distributed for all files, the probability of an undetected error is less than 2.4 x 10^-10. My assumption about 'randomly distributed' may be incorrect - a job for you mathematicians if you are so motivated! But 'cksum' was designed for this specific use. POSIX says even deliberate deception is difficult, though probably not impossible. 

Having looked at the POSIX spec, I agree the use of a tab rather than a space is a violation, and so should be reportedto Oracle, who bought Sun. I'll do that, though it is low on my list of priorities. The combination of 'cksum' with 'awk' seems good to me. 

Dave


---

Comment by ddrake created at 2010-03-08 11:57:58

add spkg/cksum directory; apply to repo in spkg/base


---

Comment by ddrake created at 2010-03-08 12:27:33

Changing status from new to needs_review.


---

Attachment

I've uploaded two patches which add in support for using cksum to do spkg integrity verification. There's a new sage-spkg-integrity-check script which gets called by sage-spkg, and a convenience script, sage-add-integrity-check-to-spkg, which can be used to easily add the required cksum file to a spkg. Once you have a built spkg, you can just do

```
sage-add-integrity-check-to-spkg foo.spkg
```

and the correct file gets added in.

I've done some simple testing and it seems to work properly. One test is to apply these patches, make a source tarball, and then deliberately truncate the file and see if things fail. (I think an aborted download is a common way to get invalid spkg files.) One can also corrupt a spkg file to see if it's detected.

Once these scripts are in, we can easily go through all the spkgs in the optional and experimental repos and add in integrity checks for them.

Right now, a missing cksum file is not considered an error, but that can be changed easily. Doing cksum verifications for every spkg in 4.3.4.alpha0 takes a bit under 6 minutes on my computer. If that seems too long, it would be easy to add in an environment variable (and document it! See #8263) that would turn these verifications off.

Please review!


---

Comment by drkirkby created at 2010-03-08 13:40:54

Hi, 
I'm really tied up today, so don't have chance to start applying patches and testing this. But I looked at the source quickly and made a few comments. 

*b/sage-add-integrity-check-to-spkg*

 * Line 1: I thought all scripts were supposed to start with #!/usr/bin/env bash 
 * Line 8 if [ "$1" = "$SPKGNAME" ] . A more portable test is if [ "x$1" = "xPKGNAME" ]. It's not essential in modern versions of bash, but is a good habit to get into. 
 * Line 16-25. It would appear to me that the assumption is made that if bzip2 returns with a non-zero exit code, then it must be a tar file. It could be a corrupted .spkg file, where the .spkg is a tar file. 
 * It does not appear to me that the exit code of tar is checked. 
 * Line 27, would 'cp' be faster/more appropriate than cat? It is on my system, but perhaps not on more modern systems. 
 * Is there a need for line 27 at all? Could line 29 not have $1 rather than $SPKGNAME.tar? 'tar' does not require that the file have the extension .tar. 
 * You might want to investigate if the 'file' command would save a lot of work, as that will tell you if the file is a tar file or a bzip2 compressed file. 

* b/sage-spkg-integrity-check*

 * Lines 13 and 19. A minor point, but a more portable test for if [ "$foobar" = "" ]  is if [ -z "$foobar"  ]. I personlly try to use things that are as portable of possible, so I don't get caught out if I use a system which does not conform to the way most shells work. 
 * Line 63. I think it would be better to say "$0 appears to be corrupted, as the checksum is not what is expected. Expected <what you expect> got <what you got> 

*General*

I think you might speed this up by avoiding some of the 'cat' commands. For example, 


```
file.tar < tar xf -
```

can be faster than 

``` 
cat file.tar | tar xf
```

as you don't need to invoke cat at all. Do a Google on "useless use of cat". 

Since you mention speed as a possible issue, any attempt that could be made to avoid copying files, or cat'ing files unnecessarily should help speed things up a lot. Other points are more minor


---

Comment by ddrake created at 2010-03-09 07:20:05

Replying to [comment:11 drkirkby]:
> *b/sage-add-integrity-check-to-spkg*
> 
>  * Line 1: I thought all scripts were supposed to start with #!/usr/bin/env bash 

On Ubuntu, /bin/sh is actually dash, which aims for POSIX compliance. I often use /bin/sh to make sure that I avoid bashisms. Although if we are assuming that bash is available, perhaps we might as well use that.

>  * Line 8 if [ "$1" = "$SPKGNAME" ] . A more portable test is if [ "x$1" = "xPKGNAME" ]. It's not essential in modern versions of bash, but is a good habit to get into. 

Sounds good.

>  * Line 16-25. It would appear to me that the assumption is made that if bzip2 returns with a non-zero exit code, then it must be a tar file. It could be a corrupted .spkg file, where the .spkg is a tar file. 

This script is intended to be used when preparing spkg files for review, so if you've just made the spkg file and it's already corrupted, that will get caught in review. 

>  * Line 27, would 'cp' be faster/more appropriate than cat? It is on my system, but perhaps not on more modern systems. 

I suspect that cp would be faster for plain tar files, but since bzip2 doesn't have a way to specify the output file name, I chose the current method. 

>  * Is there a need for line 27 at all? Could line 29 not have $1 rather than $SPKGNAME.tar? 'tar' does not require that the file have the extension .tar. 
>  * You might want to investigate if the 'file' command would save a lot of work, as that will tell you if the file is a tar file or a bzip2 compressed file.

I've switched the script to using 'file', which should be faster.

Line 29 could use $1 if we changed the options to tar appropriately ("xf" or "jxf"), but in any case, we need an uncompressed tar archive to do the append.

> * b/sage-spkg-integrity-check*
> 
>  * Lines 13 and 19. A minor point, but a more portable test for if [ "$foobar" = "" ]  is if [ -z "$foobar"  ]. I personlly try to use things that are as portable of possible, so I don't get caught out if I use a system which does not conform to the way most shells work.

Fixed.

>  * Line 63. I think it would be better to say "$0 appears to be corrupted, as the checksum is not what is expected. Expected <what you expect> got <what you got> 

Good idea.


> *General*
> 
> I think you might speed this up by avoiding some of the 'cat' commands. For example,

I found a way to avoid shell redirection altogether in that instance.

> Do a Google on "useless use of cat". 

I like the advice "stop piping cats" :)  Although for simple things, I like using cat and a pipe, since I can easily visualize the data moving from left to right.

With the above changes, testing all the spkgs in 4.3.4.alpha0 now takes about 4:33 on my computer.


---

Comment by ddrake created at 2010-03-09 07:58:18

apply to sage_scripts repo


---

Attachment

Tar on OS X does not like "-O" at the end. I forgot to check the "overwrite attachment" button; please ignore trac_329_sage_scripts.2.patch.


---

Comment by ddrake created at 2010-03-10 01:34:47

Current patch has sage-spkg actually check the exit code to see if the spkg passed the checksum test.

I should add that I've modified my proposal above ever so slightly; the checksum file in the spkg is now named "spkgname-version.downloaded.cksum" (e.g., atlas-4.0.3.p2.downloaded.cksum) to make clear where it came from; the computed checksums are named similarly, but "computed" instead of "downloaded".


---

Comment by ddrake created at 2010-03-10 03:22:02

Hrm, the output of "`tar tvf`" is not very consistent:

On t2.math, GNU tar 1.17:

```
drwxr-xr-x mvngu/mvngu       0 2010-01-24 08:12 atlas-3.8.3.p11/
drwxr-xr-x mvngu/mvngu       0 2009-06-21 18:31 atlas-3.8.3.p11/ATLAS-build/
drwxr-xr-x mvngu/mvngu       0 2010-01-24 07:41 atlas-3.8.3.p11/patches/
-rw-r--r-- mvngu/mvngu    8944 2009-01-01 19:41 atlas-3.8.3.p11/patches/PM32SSE2.tgz
```


On bsd.math, BSD tar 2.6.2:

```
drwxr-xr-x  0 mvngu  mvngu       0 Jan 24 08:12 atlas-3.8.3.p11/
drwxr-xr-x  0 mvngu  mvngu       0 Jun 21  2009 atlas-3.8.3.p11/ATLAS-build/
drwxr-xr-x  0 mvngu  mvngu       0 Jan 24 07:41 atlas-3.8.3.p11/patches/
-rw-r--r--  0 mvngu  mvngu    8944 Jan  1  2009 atlas-3.8.3.p11/patches/PM32SSE2.tgz
```


On an Ubuntu 9.10 machine, GNU tar 1.22:

```
drwxr-xr-x mvngu/mvngu       0 2010-01-25 01:12 atlas-3.8.3.p11/
drwxr-xr-x mvngu/mvngu       0 2009-06-22 10:31 atlas-3.8.3.p11/ATLAS-build/
drwxr-xr-x mvngu/mvngu       0 2010-01-25 00:41 atlas-3.8.3.p11/patches/
-rw-r--r-- mvngu/mvngu    8944 2009-01-02 12:41 atlas-3.8.3.p11/patches/PM32SSE2.tgz
```


So I think we need to drop the "v" and just do "tf" (with a "j" if necessary for bzipped spkgs). This eliminates the file sizes and modification times from the checksum, but I think our test will still be pretty reliable, and I don't know a good way to normalize the verbose file listing. (For example, observe that tar is printing the file modification times using the local timezone -- my machine is UTC+9, and in January, bsd.math and t2.math are both UTC-8.)

I'll try to upload a new patch shortly.


---

Comment by ddrake created at 2010-03-14 09:09:40

apply to sage_scripts repo


---

Attachment

New patch fixes adds a "then" which should follow an "elif" in sage-spkg.

Also, I once again uploaded a mis-named patch. Please ignore trac_329.patch; only attachment:trac_329_sage_scripts.patch and attachment:trac_329_spkg_base.patch are necessary.


---

Comment by drkirkby created at 2010-03-15 00:03:43

I think the message below is a bit confusing. I created a package and added the checksum. The package can be found here. 

http://boxen.math.washington.edu/home/kirkby/optional/openmpi-1.4.1/openmpi-1.4.1.spkg

But when I try to check the integrity with "sage-spkg-integrity-check", the script reports "No integrity checksum stored in openmpi-1.4.1.spkg, skipping integrity check.". The check in in the package though. 



```
sage subshell$ cksum openmpi-1.4.1.spkg
1602272063      6575256 openmpi-1.4.1.spkg
/export/home/drkirkby/sage-4.3.4.alpha1/spkg/optional/openmpi-1.4.1
sage subshell$ sage-add-integrity-check-to-spkg openmpi-1.4.1.spkg                        
Adding integrity verification checksum to openmpi-1.4.1.spkg...
checksum of openmpi-1.4.1.spkg is 2771621513 49876645.
/export/home/drkirkby/sage-4.3.4.alpha1/spkg/optional/openmpi-1.4.1
sage subshell$ sage-spkg-integrity-check                 
/export/home/drkirkby/sage-4.3.4.alpha1/spkg/optional/openmpi-1.4.1
sage subshell$ cksum openmpi-1.4.1.spkg
463207792       6575325 openmpi-1.4.1.spkg
/export/home/drkirkby/sage-4.3.4.alpha1/spkg/optional/openmpi-1.4.1
sage subshell$ sage-spkg-integrity-check openmpi-1.4.1.spkg
Verifying integrity of openmpi-1.4.1.spkg.../export/home/drkirkby/sage-4.3.4.alpha1/local/bin/sage-spkg-integrity-check: line 41: /export/home/drkirkby/sage-4.3.4.alpha1/spkg/cksum/openmpi-1.4.1.downloaded.cksum: No such file or directory
No integrity checksum stored in openmpi-1.4.1.spkg, skipping integrity check.
```


If I want someone to review that package, what should I give them - just the link to the spkg, or give them the contents of openmpi-1.4.1.cksum too? 

Dave


---

Comment by ddrake created at 2010-03-15 01:27:25

The problem is with...

Replying to [comment:18 drkirkby]:
> {{{
> Verifying integrity of openmpi-1.4.1.spkg.../export/home/drkirkby/sage-4.3.4.alpha1/local/bin/sage-spkg-integrity-check: line 41: /export/home/drkirkby/sage-4.3.4.alpha1/spkg/cksum/openmpi-1.4.1.downloaded.cksum: No such file or directory
> }}}

The script stores the cksum files in the directory SAGE_ROOT/spkg/cksum, and that directory doesn't exist for you. I'll upload another patch in a moment, or you can work around that by just creating that directory.

> If I want someone to review that package, what should I give them - just the link to the spkg, or give them the contents of openmpi-1.4.1.cksum too? 

You should be able to just give them a link to the spkg.


---

Comment by drkirkby created at 2010-06-22 23:33:01

I've applied this patch. Can you tell me how I'm supposed to add an update package to Sage now? Can you create sometime small like pexpect-2.0.p5.spkg and pexpect-2.0.p6.spkg, where one is corrupted so I can see this in action? 

I can't say I understand what is supposed to happen. I obviously understand the principle of a checksum, but I'm not sure how I'm supposed to use this in Sage. 

Yours, rather confused!

Dave


---

Comment by drkirkby created at 2010-06-23 00:07:41

I think what this ticket needs to make it easier to review are:

1) Clear instructions how to create a .spkg with the checksum information. 
2) Clear instructions how to apply such a .spkg to Sage
3) An example on the web of a valid .spkg with the checksum. 
4) An example on the web of a corrupted .spkg 

Whilst I understand what a checksum is, and proposed using the portable 'cksum' I'm very confused about how I'm supposed to use this is Sage. 

Dave


---

Comment by drkirkby created at 2010-07-24 21:32:08

Any comments on this anyone? It would be nice to get this 3-year old ticket reviewed, though I'm not able to do so without some more input from others. 

Dave


---

Comment by ddrake created at 2010-07-26 05:20:30

Replying to [comment:22 drkirkby]:
> Any comments on this anyone? It would be nice to get this 3-year old ticket reviewed, though I'm not able to do so without some more input from others. 

I'll work on examples for you to test with. Stay tuned.


---

Comment by ddrake created at 2010-07-26 05:47:16

For testing, naturally you need to start by applying attachment:trac_329_sage_scripts.patch.

To create a .spkg with checksum information: take any existing .spkg file, and use the sage-add-integrity-check-to-spkg script:

```
sage-add-integrity-check-to-spkg foo.spkg
```

You needn't run that in a "Sage shell"; it only uses ordinary system-wide utilities. That will add the checksum information into the .spkg file.

To test that the checksum information works, try installing http://sage.math.washington.edu/home/drake/trac329/pexpect-99.0.spkg which has correct checksum information. Then try http://sage.math.washington.edu/home/drake/trac329/pexpect-100.0.spkg which doesn't. (You'll see that I just put the word "bad" into the correct checksum.)

Hopefully the suspicious version numbers prevent anyone from actually using those .spkg files (although they install a perfectly working version of pexpect).

The installation should work for the "99" spkg and  fail for "100" spkg. Look for "Verifying integrity of ...pexpect-99.0.spkg..." lines.


---

Comment by drkirkby created at 2010-08-02 14:42:31

I get a problem here. After changing to $SAGE_LOCAL/bin, then using hg push, I get:

drkirkby`@`hawk:~/sage-4.5.1/local/bin$ hg push
abort: repository /space/rlm/sage-4.1.rc1/local/bin not found!


Why its looking for a 4.1.rc1 directory in a 4.5.1 bit of Sage, I don't know. 

What's way to import this patch from within Sage? I tend to use 'hg' outside, but this is failing here for me. 

Dave


---

Comment by ddrake created at 2010-10-21 03:36:08

Replying to [comment:25 drkirkby]:
> I get a problem here. After changing to $SAGE_LOCAL/bin, then using hg push, I get:
> 
> drkirkby`@`hawk:~/sage-4.5.1/local/bin$ hg push
> abort: repository /space/rlm/sage-4.1.rc1/local/bin not found!
> 
> Why its looking for a 4.1.rc1 directory in a 4.5.1 bit of Sage, I don't know.

It's looking for a directory that Robert Miller (rlm) created, probably on sage.math. My guess is that somewhere inside the Mercurial repository, it stored some information about where it came from, and is using that information.

You use `hg push` when you want to push changesets to another repository; in this case, you don't want to do that. I'm guessing you want to use `hg import` and then possibly `hg update` to update the working directory.


---

Comment by jhpalmieri created at 2011-08-16 17:07:27

Some comments:

 - to my surprise, this still applies cleanly to Sage 4.7.1.

 - I think that on OS X 10.4 (which we still support?), and perhaps other platforms, bash is version 2, which may not support the `PIPESTATUS` array.  This is the reason for the `pipestatus` script in SAGE_ROOT/spkg/, and maybe you should use that instead in `sage-spkg-integrity-check`.

 - I wonder if having `sage-spkg-integrity-check` as a separate script is a good idea.  That is, when you run `sage-spkg`, the spkg file is unpacked, producing the `cksum` file and the build directory.  Since they're both there, you can check them — no need to unpack the tar file twice, once to check integrity, and a second time to build.

 - Should `sage-add-integrity-check-to-spkg` be used in the `sage-pkg` script for building spkgs?  That way any new spkgs get a cksum file automatically.  Maybe this could be the default, and you could disable it with a command-line flag (or yet another Sage environment variable).

 - I think that the cksum file in SAGE_ROOT/spkg/build should be deleted:

```diff
diff --git a/sage-spkg b/sage-spkg
--- a/sage-spkg
+++ b/sage-spkg
@@ -407,9 +419,14 @@ if [ $? -eq 0 ]; then
             cd "$SAGE_PACKAGES/build/"
             rm -rf "$SAGE_PACKAGES/build/$PKG_NAME"
         fi
+        rm -f "$SAGE_PACKAGES/build/$PKG_NAME.cksum"
     else
         echo "You can safely delete the temporary build directory"
         echo "$SAGE_PACKAGES/build/$PKG_NAME"
+       if [ -f "$SAGE_PACKAGES/build/$PKG_NAME.cksum" ]; then
+           echo "and the checksum file"
+           echo "$SAGE_PACKAGES/build/$PKG_NAME.cksum"
+       fi
     fi
 
 else
```

 If we use the `cksum` directory, the same could be true for any valid cksums; files with failed integrity checks could be retained.

 - My preference for echo statements is to have them start with capital letters, and perhaps be complete sentences; for example:

```diff
diff --git a/sage-add-integrity-check-to-spkg b/sage-add-integrity-check-to-spkg
--- a/sage-add-integrity-check-to-spkg
+++ b/sage-add-integrity-check-to-spkg
@@ -30,7 +30,7 @@ fi
 tar tf $SPKGNAME.tar --exclude $SPKGNAME.cksum; } | \
 cksum | awk '{print $1, $2}' > $SPKGNAME.cksum
 
-echo "checksum of $1 is `cat $SPKGNAME.cksum`."
+echo "The checksum of $1 is `cat $SPKGNAME.cksum`."
 
 tar rf $SPKGNAME.tar $SPKGNAME.cksum
 
diff --git a/sage-spkg b/sage-spkg
--- a/sage-spkg
+++ b/sage-spkg
@@ -247,7 +247,7 @@ then
     exit 1
 elif [ $STATUS = 2 ]
 then
-    echo no integrity checksum found for $PKG_SRC, continuing.
+    echo No integrity checksum found for $PKG_SRC, continuing.
 elif [ $STATUS = 3 ]
 then
     echo $0: something strange happened while checking integrity of $PKG_SRC, exiting.
```


By the way, there is other work on sage-spkg going on at #4949, so one of these might need to be rebased on top of the other one, if either one ever gets a positive review...


---

Comment by ddrake created at 2011-08-18 04:46:40

apply only this patch to the scripts repo.


---

Attachment


---

Comment by ddrake created at 2011-08-18 04:55:46

Replying to [comment:27 jhpalmieri]:
>  - to my surprise, this still applies cleanly to Sage 4.7.1.

I'm a bit surprised too.

>  - I think that on OS X 10.4 (which we still support?), and perhaps other platforms, bash is version 2, which may not support the `PIPESTATUS` array.  This is the reason for the `pipestatus` script in SAGE_ROOT/spkg/, and maybe you should use that instead in `sage-spkg-integrity-check`.

Changed to use the `pipestatus` script.

>  - I wonder if having `sage-spkg-integrity-check` as a separate script is a good idea.  That is, when you run `sage-spkg`, the spkg file is unpacked, producing the `cksum` file and the build directory.  Since they're both there, you can check them — no need to unpack the tar file twice, once to check integrity, and a second time to build.

This sounds like a good idea. I can implement that, but it would require some coordination with the other tickets touching `sage-spkg`.

>  - Should `sage-add-integrity-check-to-spkg` be used in the `sage-pkg` script for building spkgs?  That way any new spkgs get a cksum file automatically.  Maybe this could be the default, and you could disable it with a command-line flag (or yet another Sage environment variable).

Definitely! In fact, if the checksums are not added automatically, no one will ever use them. So we should certainly add this into `sage-pkg`. But perhaps we should get the functionality merged first.

>  - I think that the cksum file in SAGE_ROOT/spkg/build should be deleted:

Sure. I added your suggestion.

>  - My preference for echo statements is to have them start with capital letters, and perhaps be complete sentences; for example:

I added these changes too.

> By the way, there is other work on sage-spkg going on at #4949, so one of these might need to be rebased on top of the other one, if either one ever gets a positive review...

Right now there's a minor conflict with the patch at #4949. Very simple to rebase.


---

Comment by jhpalmieri created at 2011-09-10 01:42:34

Changing priority from minor to major.


---

Comment by jhpalmieri created at 2011-09-10 01:42:34

I'm working on testing this, but it looks good so far.  I'm attaching a patch to go on top of yours, which does the following:

 * add some error checks and error messages

 * echo some error messages to stderr instead of stdout

 * automatically add a checksum in sage-pkg

 * replace "if DIR does not exist, mkdir DIR" by "mkdir -p DIR"

 * quoted some environment variables

What do you think?


---

Attachment

scripts repo


---

Comment by leif created at 2011-09-10 03:54:24

To me this looks a bit like reinventing the wheel, or overkill.

The only tarball we _may_ really need checksums for is the source (or binary) distribution tarball, and perhaps also `prereq-*.tar`, which is contained in the former. MD5 sums (and perhaps other checksums) are already provided on the download sites, which a user can easily check, though we _could_ in addition do some "sanity" check, e.g. when running the prereq script, or earlier in / from the top-level Makefile.

All other tarballs, mostly spkgs I think, can be packed with `bzip2`, which provides proper checksums (also CRCs for each "block" btw.), i.e., automatically creates them, and checks them upon extraction / decompression.

The only (standard) spkg that is a _plain_ `tar` file is the odd Fortran spkg, just because it contains already compressed data (binary executables and/or other tarballs).

So the only change we'd have to make, IMHO, is to make `sage -pkg` (more precisely, `sage -pkg_nc`) _always_ use `bzip2`, or, even better, `gzip` (available "everywhere", or, more precisely, _already a prerequisite_ for Sage), but in the case of `_nc` pass `-1` to it, which uses less sophisticated and therefore fast compression,  leading to a [checksummed] `[.tar].bz2` file / spkg with almost the same size.

(If we used `gzip`, we'd have to make slight changes to `sage-spkg`, since it currently just tries to use `bunzip2` for decompression, and if that fails, retries direct extraction with plain `tar x ...`.)

With `-1`, for the current Fortran spkg I get

```sh
$ du -b fortran-20100629.spkg*
34560000	fortran-20100629.spkg
34721464	fortran-20100629.spkg.bz2
34456814	fortran-20100629.spkg.gz
```

and for the current Sage source tarball, I get

```sh
$ du -b sage-4.7.2.alpha2.tar*
337633280	sage-4.7.2.alpha2.tar
338068743	sage-4.7.2.alpha2.tar.bz2 # for reference only
335605749	sage-4.7.2.alpha2.tar.gz
```


Compression and decompression with GNU zip happens almost instantly.

Note that the GNU zip-compressed files are in both cases actually even _smaller_, which of course isn't always the case. (An increase by about 0.5% may be possible, at least with `bzip2`.)

Unfortunately, unlike e.g. `zip` (which should be available "everywhere", too), neither `gzip` nor `bzip2` support `-0`, which really just stores the file, adding only the small archive header, which contains meta data, including the checksums we want.


---

Comment by was created at 2011-09-10 04:09:17

I really like the idea to use bzip2 for checksums.


---

Comment by leif created at 2011-09-10 04:39:07

Replying to [comment:32 was]:
> I really like the idea to use bzip2 for checksums.

As mentioned, `gzip` is (much) faster in this case (`-1`), and is already a prerequisite.

Both use CRC-32 only though, but for each block (100-900 KB for `bzip2`).

Also, any reasonable transport protocol does apply integrity check (error detection / correction), so only aborted transmissions (or defective harddisks / memory) could cause corrupted files / tarballs.


---

Comment by jhpalmieri created at 2011-09-10 16:13:48

Given the workaround for OS X at the beginning of sage-pkg (see #2522), I would be tempted to avoid the Python tarfile module and rewrite the "tar_file" function as follows:

```diff
diff --git a/sage-pkg b/sage-pkg
--- a/sage-pkg
+++ b/sage-pkg
@@ -17,28 +17,18 @@ def tar_file(dir, no_compress=False):
         # workaround OS X issue -- see trac #2522
         COPYFILE_DISABLE = True
         os.environ['COPYFILE_DISABLE'] = 'true'
-        if no_compress:
-            cmd = "tar -cf %s.spkg %s" % (dir, dir)
-        else:
-            cmd = "tar -cf - %s | bzip2 > %s.spkg" % (dir, dir)
-        try:
-            check_call(cmd, shell=True)
-        except CalledProcessError:
-            print "Package creation failed."
-            sys.exit(1)
+    if no_compress:
+        # Compress the tar file using gzip with the lowest compression
+        # level, to add checksum information.
+        compression = "gzip -1"
     else:
-        import tarfile
-        if no_compress:
-            mode = "w"
-        else:
-            mode = "w:bz2"
-        try:
-            tar = tarfile.open("%s.spkg" % dir, mode=mode)
-            tar.add(dir, exclude=lambda f: f == ".DS_Store")
-            tar.close()
-        except tarfile.TarError:
-            print "Package creation failed."
-            sys.exit(1)
+        compression = "bzip2"
+    cmd = "tar -cf - %s | %s > %s.spkg" % (dir, compression, dir)
+    try:
+        check_call(cmd, shell=True)
+    except CalledProcessError:
+        print "Package creation failed."
+        sys.exit(1)
 
 def main():
     import re
```

Otherwise, if we work with Python modules on non-Darwin systems, we have to create a temporary tar file (using tempfile, say), then gzip it, then remove the tar file.  The code is simpler and easier to maintain if we use the same approach on all platforms.


---

Comment by leif created at 2011-09-10 17:49:17

Replying to [comment:34 jhpalmieri]:
> ... rewrite the "tar_file" function as follows:

s/`compression`/`compressor`/

I'd suggest to make a `tar` "feature test" (w.r.t. `-j`) to avoid the explicit pipe if possible.

Maybe same for `-z`, but this also needs a way to pass `-1` to `gzip`.


---

Comment by leif created at 2011-09-10 17:51:56

P.S.:

```
bsdtar: manipulate archive files
First option must be a mode specifier:
  -c Create  -r Add/Replace  -t List  -u Update  -x Extract
Common Options:
  -b #  Use # 512-byte records per I/O block
  -f <filename>  Location of archive (default /dev/st0)
  -v    Verbose
  -w    Interactive
Create: bsdtar -c [options] [<file> | <dir> | @<archive> | -C <dir> ]
  <file>, <dir>  add these items to archive
  -z, -j, -J, --lzma  Compress archive with gzip/bzip2/xz/lzma
  --format {ustar|pax|cpio|shar}  Select archive format
  --exclude <pattern>  Skip files that match pattern
  -C <dir>  Change to <dir> before processing remaining files
  @<archive>  Add entries from <archive> to output
List: bsdtar -t [options] [<patterns>]
  <patterns>  If specified, list only entries that match
Extract: bsdtar -x [options] [<patterns>]
  <patterns>  If specified, extract only entries that match
  -k    Keep (don't overwrite) existing files
  -m    Don't restore modification times
  -O    Write entries to stdout, don't restore to disk
  -p    Restore permissions (including ACLs, owner, file flags)
bsdtar 2.8.0 - libarchive 2.8.0
```


So it's compatible with (recent) GNU `tar`s w.r.t. compression.


---

Comment by leif created at 2011-09-10 17:59:32

P.P.S.:

  ENVIRONMENT 


       The environment variable `GZIP` can hold a set of default options for `gzip`.
       These options are interpreted first and can be overwritten by  explicit  command line parameters.  For example:

```
for sh:    GZIP="-8v --name"; export GZIP
```



---

Comment by jhpalmieri created at 2011-09-10 18:26:21

We distribute bzip2 with Sage, so I don't think we can assume that it's available on the system.  Does "tar -j" require bzip2 be installed on the system, or will it use a locally installed version (e.g. in SAGE_ROOT/local/bin)?  Otherwise, is there a quick way to test whether "tar -j" will work?


---

Comment by was created at 2011-09-10 18:35:35

Replying to [comment:38 jhpalmieri]:
> We distribute bzip2 with Sage, so I don't think we can assume that it's available on the system.  

Older tars don't have a -j option, so you'll see lines like this in the sage-* scripts in local/bin:

```
    tar -cf - %s | bzip2 > %s.spkg

and

    bunzip2 -c "$PKG_SRC" 2>/dev/null | tar Ofx${UNTAR_VERBOSE} - $PKG_NAME/SAGE.txt 2>/dev/null
```


Evidently, most of 

William


---

Comment by leif created at 2011-09-10 19:14:33

Replying to [comment:38 jhpalmieri]:
> We distribute bzip2 with Sage, so I don't think we can assume that it's available on the system.

? We can assume that Sage's `bzip2` is built when `sage -pkg[nc] ...` is invoked.

> Does "tar -j" require bzip2 be installed on the system, or will it use a locally installed version (e.g. in SAGE_ROOT/local/bin)?

`tar` just calls `execve()`, so the first compressor (e.g. `bzip2`) found along `PATH` will be run, which should be Sage's in the case of `b[un]zip2`.




> Otherwise, is there a quick way to test whether "tar -j" will work?

We could test the version numbers of GNU and BSD `tar` (others aren't officially supported AFAIK).


```sh
    tar cjf /dev/null /dev/null 1>/dev/null 2>&1 || fail
```

works with both GNU and BSD `tar`, i.e., `tar` returns 0 if `-j` is supported, a non-zero value otherwise.


---

Comment by leif created at 2011-09-10 19:24:02

Replying to [comment:40 leif]:
> We could test the version numbers of GNU and BSD `tar` (others aren't officially supported AFAIK).

And presumably also some [recent] version of Sun's `tar`.

>

```sh
    tar cjf /dev/null /dev/null 1>/dev/null 2>&1 || fail
```


Someone could test the above on [Open]Solaris.


---

Comment by jhpalmieri created at 2011-09-10 19:38:37

On Solaris or OpenSolaris, we require GNU tar (according to our installation guide), so this should work.

But as William says, do we need to support older versions of tar which don't support the "-j" flag?


---

Comment by leif created at 2011-09-10 19:55:32

Replying to [comment:42 jhpalmieri]:
> But as William says, do we need to support older versions of tar which don't support the "-j" flag?

Well, I suggested we should actually test its capabilities; I wouldn't blindly rely on `-z` or `-j` being supported.

I don't think we have to support dead old _GNU_ `tar` versions which don't support both; for BSD `tar` I'd say the minimal version we can currently require is the one shipped with MacOS X 10.4.


---

Comment by was created at 2011-09-10 19:57:05

Replying to [comment:42 jhpalmieri]:
> On Solaris or OpenSolaris, we require GNU tar (according to our installation guide), so this should work.
> 
> But as William says, do we need to support older versions of tar 
> which don't support the "-j" flag?

In 2005 when I wrote the first scripts, it was a good idea!  Now, it's not very important... That said, it seems writing scripts that do not use -j isn't hard  at all, so why require it?


---

Comment by leif created at 2011-09-10 20:15:15

Replying to [comment:44 was]:
> Replying to [comment:42 jhpalmieri]:
> > On Solaris or OpenSolaris, we require GNU tar (according to our installation guide), so this should work.
> > 
> > But as William says, do we need to support older versions of tar 
> > which don't support the "-j" flag?
> 
> In 2005 when I wrote the first scripts, it was a good idea!  Now, it's not very important...

GNU `tar` supports `-j` since version 1.13.18, released October 29th 2000. (`-z` is of course supported much longer.)

> That said, it seems writing scripts that do not use -j isn't hard  at all, so why require it?

Because it's easier (to read and write) ;-) and we avoid the usual trouble with the exit status of pipes, which wouldn't be a problem at all if we could rely on `bash` version >=3.0, but there's still MacOS X 10.4... (<flame>and its users are unable to install a more recent version</flame>) 8/

In case we explicitly support some BSD `tar` version which _doesn't_ support `-j`, we should have a fallback. Otherwise I would just issue an error message if `-j` (or `-z`) isn't supported, recommending to install some contemporary version.


---

Comment by leif created at 2011-09-10 20:27:22

P.S.:

In case we _have to_ use a pipe, we shouldn't do

```python
    subprocess.call("foo | bar", shell=True)
```

but create the pipe and _two_ subprocesses from Python instead.


---

Comment by jhpalmieri created at 2011-09-10 22:50:28

What's wrong with using a pipe in `subprocess.call`?


---

Comment by leif created at 2011-09-10 23:31:31

Replying to [comment:47 jhpalmieri]:
> What's wrong with using a pipe in `subprocess.call`?

The same issue we have in shell scripts. If `foo` fails, `bar` might still return 0, so we wouldn't notice the failure.

If we relied on `bash` >=3.0, we could use

```python
    subprocess.call(["bash", "-c", "set -o pipefail; foo | bar"]) # no shell=True
```

but that's IMHO ugly (and we currently cannot anyway).

So it's better (or safer) to create the pipe from Python, such that we get the exit codes of both subprocesses.


---

Comment by jhpalmieri created at 2011-09-19 22:33:04

Regarding the patch from #2522: any advice on how to test it?  I'm not sure how to create a resource fork for a file, to be stored in `._FILENAME`.  Here's what I've seen so far:

 - I created a directory with one file, "Makefile".  I used the "Get Info" menu item from the Finder to change the default application for this file.
 - From the shell, I created a tar file from this directory.  I unpacked it someplace else, and it remembered the change to the default application for the file.
 - From the shell, I did `export COPYFILE_DISABLE=1` and proceeded as in the previous step.  Then it didn't remember the change to the default application.  So far so good, except I don't know where that information was stored.
 - When using the tarfile module in Python, regardless of whether `COPYFILE_DISABLE` has been set, it doesn't remember the change.  So can we bypass the patch from #2522 by just using the Python tarfile module?

Note that the setting of `COPYFILE_DISABLE` doesn't tell tar to ignore files like `.DS_Store`: those are copied over regardless.


---

Comment by jdemeyer created at 2012-04-02 10:25:59

Changing priority from major to minor.


---

Comment by jdemeyer created at 2012-04-02 10:25:59

Changing component from packages to scripts.


---

Comment by jdemeyer created at 2012-04-02 10:25:59

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2012-04-02 10:25:59

This obviously needs to be rebased (in particular, you should support gzip).

Also: why have a script which changes a spkg file directly?  If you want to do this, just edit `sage-pkg`.


---

Comment by kcrisman created at 2013-03-21 16:34:29

>  - I think that on OS X 10.4 (which we still support?), and perhaps other platforms, bash is version 2, which may not support the `PIPESTATUS` array.  This is the reason for the `pipestatus` script in SAGE_ROOT/spkg/, and maybe you should use that instead in `sage-spkg-integrity-check`.

Not that I am very invested in this ticket, but according to [this link](http://wiki.bash-hackers.org/scripting/bashchanges) bash 2.0 does support this.  My oldest such computer has bash 2.05b.0(1) release.

```
student$ echo $HISTCMD
502
student$ echo $PIPESTATUS
0
student$ echo $FOO

student$
```

And other examples after an actual used pipe seemed to work properly.

That doesn't mean there couldn't be some other reason for the `pipestatus` script, of course, still having to do with older bashes.


---

Comment by kcrisman created at 2013-03-21 16:44:35

However, `set -o pipefail` is indeed illegal before bash 3.0 (tested it to be sure).  But one could use `PIPESTATUS` for that, presumably?

```
 GNU tar was included as the standard system tar in
     FreeBSD beginning with FreeBSD 1.0.
```

OS X 10.4 still has it as GNU tar, obtained by FreeBSD from NetBSD; OS X 10.7 has it just as FreeBSD tar since apparently it was reimplemented.  Anyway, all of these (Mac, FreeBSD) should probably have the -j flag.  Would Solaris be the only one that doesn't per standard?


---

Comment by jdemeyer created at 2013-03-27 07:49:59

I hate to say this, but what's the point of spkg checksums _inside an spkg_? To me, it looks pointless to add a checksum within the file that you're checksumming.


---

Comment by nbruin created at 2013-03-27 07:57:42

Replying to [comment:53 jdemeyer]:
> I hate to say this, but what's the point of spkg checksums _inside an spkg_? To me, it looks pointless to add a checksum within the file that you're checksumming.
For detecting download corruption it's quite useful. Basically all error detecting and correcting codes are based on sending the "checksum" together with the data.


---

Comment by jdemeyer created at 2013-03-27 15:55:46

Replying to [comment:54 nbruin]:
> For detecting download corruption it's quite useful. Basically all error detecting and correcting codes are based on sending the "checksum" together with the data.
Yes, but I doubt this checksum is meant to be used for checking for bit errors. Even the ticket description talks about truncated files, which would almost certainly mean that the checksum cannot be extracted. If the spkg file can be extracted without errors, it is extremely unlikely that it got corrupted, I think that's a good enough check.

Therefore, I would consider closing this as "wontfix".


---

Comment by robertwb created at 2013-04-11 07:51:08

Changing status from needs_work to needs_review.


---

Comment by robertwb created at 2013-04-11 07:51:08

I implemented this for the new git layout: https://github.com/sagemath/sage/pull/1


---

Comment by ohanar created at 2013-04-15 01:43:59

From the discussion on the pull request, Robert made it sound like this is a blocker for releasing 6.0 -- so I'm marking this as such.


---

Comment by ohanar created at 2013-04-15 01:43:59

Changing priority from minor to blocker.


---

Comment by ohanar created at 2013-04-15 01:43:59

Changing status from needs_review to positive_review.


---

Comment by ohanar created at 2013-04-15 01:47:16

Jeroen, if you don't mind, I'd like to mark this as fixed and merge the changes into the git repository.


---

Comment by jdemeyer created at 2013-04-15 06:49:52

In fact, I do mind very much, I'll post my reasons to the sage-git list.


---

Comment by vbraun created at 2013-12-16 17:00:47

Resolution: fixed


---

Comment by vbraun created at 2013-12-16 17:00:47

Since this is implemented in sage-git I'll go ahead and mark this as duplicate. If anybody objects feel free to tell me what you want me to do with this ticket.
