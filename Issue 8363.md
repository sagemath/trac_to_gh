# Issue 8363: cddlib-094f.p4 has a useless check for mpir which breaks on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/8363

Original creator: drkirkby

Original creation time: 2010-02-25 15:31:56

Assignee: drkirkby

CC:  jsp

spkg/install/deps shows that cddlib depends on mpir


```
$(INST)/$(CDDLIB): $(BASE) $(INST)/$(MPIR)
        $(SAGE_SPKG) $(CDDLIB) 2>&1
```


but for some reason someone has added a check in cddlib's spkg-install. This seems a bit pointless, but is causing a breakage on Solaris


```
# We depend on mpir, make sure it is installed (GMP fork)
MPIR_VERSION=`cd $SAGE_ROOT/spkg/standard/; ./newest_version mpir`
if [ $? -ne 0 ]; then
    echo "Failed to find mpir.  Please install the mpir spkg"
    exit 1
fi
```


They do not even export MPIR_VERSION, so it is a useless bit of code that is breaking on Solaris. 

Also, currently cddlib will not build on 64-bit Solaris, due to the normal check that the platform is OS X: 


```
if [ `uname` = "Darwin" ] && [ "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="$CFLAGS -m64 "; export CFLAGS
fi
```


Both these issues are easily resolved. A patch and updated .spkg will follow shortly. 

Dave 




---

Attachment

Mercurial patch


---

Comment by drkirkby created at 2010-02-25 16:34:42

Updated package with changes to allow to work fully on Solaris.


---

Comment by drkirkby created at 2010-02-25 16:35:11

Changing status from new to needs_review.


---

Attachment


---

Comment by jsp created at 2010-02-25 17:20:42

Please put a link to the spkg in the ticket. An attachment does not work.

Jaap


---

Comment by jsp created at 2010-02-25 17:35:15

On hawk:


```
ld: fatal: file /usr/local/lib/libgmp.so: wrong ELF class: ELFCLASS32
ld: fatal: file processing errors. No output written to .libs/scdd_gmp
collect2: ld returned 1 exit status
make[1]: *** [scdd_gmp] Error 1
make[1]: Leaving directory `/export/home/jaap/sage_port/sage-4.3.2.alpha1/spkg/build/cddlib-094f.p5/src/src-gmp'
make: *** [all-recursive] Error 1
Error building cddlib


```

In my VirtualBox:

```
libtool: link: gcc -m64 -o .libs/scdd_gmp simplecdd.o  -L/usr/local/lib -L/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib ../lib-src-gmp/.libs/libcddgmp.so /export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/libgmp.so /usr/local/lib/libgmp.so -R/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib -R/usr/local/lib
ld: fatal: recording name conflict: file `/export/home/jaap/Downloads/sage-4.3.3.alpha1/local/lib/libgmp.so' and file `/usr/local/lib/libgmp.so' provide identical dependency names: libgmp.so.3  (possible multiple inclusion of the same file)
ld: fatal: file processing errors. No output written to .libs/scdd_gmp
collect2: ld returned 1 exit status
make[1]: *** [scdd_gmp] Error 1
make[1]: Leaving directory `/export/home/jaap/Downloads/sage-4.3.3.alpha1/spkg/build/cddlib-094f.p5/src/src-gmp'
make: *** [all-recursive] Error 1
Error building cddlib


```


So I think this ticket needs work.

Jaap


---

Comment by drkirkby created at 2010-02-25 22:47:31

Em, looks like multiple inclusion of the same libraries. I'm not sure how to solve this. I'll take a look - perhaps there is a configure option to select what library gets linked. 

dave


---

Comment by drkirkby created at 2010-02-26 01:27:26

Thinking about this ticket, it does fix what the title says it does. In other words, it removes the useless but broken check for mpir. 

I don't believe the removal of the OS X restriction for a 64-bit build can do any harm and its failure to work probably has more to do with the multiple inclusion of libraries. 

As such, I believe this should get a positive review. 

The fact it does not build on OpenSolaris is another issue. 

Dave


---

Comment by mvngu created at 2010-03-01 02:31:45

Packages should not be attached to tickets. Instead, provide a URL to the spkg. David's updated spkg is available at

http://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p5.spkg


---

Comment by drkirkby created at 2010-03-01 16:25:54

Changing priority from major to blocker.


---

Comment by drkirkby created at 2010-03-01 16:25:54

Updating to blocker, as this is essential for a successful Solaris build, which with care should build and pass all doc tests.


---

Comment by mvngu created at 2010-03-02 13:35:38

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 13:35:38

I'm happy with the changes in `cddlib-094f.p5.spkg`.


---

Comment by drkirkby created at 2010-03-02 14:09:12

Thank you Minh. I don't know what I was thinking when I attached the package to the trac ticket. Perhaps I thought it was so small - not sure. Anyway, I will not do it again. 

Thank you for the positive review. 

I've opened another ticket, #8419, to resolve the issue which Jaap found - i.e. cddlib is not building as 64-bit on OpenSolaris.


---

Comment by mvngu created at 2010-03-02 23:35:57

Merged [cddlib-094f.p5.spkg](http://sage.math.washington.edu/home/mvngu/spkg/standard/cddlib/cddlib-094f.p5.spkg) in the standard spkg repository.


---

Comment by mvngu created at 2010-03-02 23:35:57

Resolution: fixed
