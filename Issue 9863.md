# Issue 9863: Error building PIL on RHEL Server 5.5

Issue created by migration from https://trac.sagemath.org/ticket/9864

Original creator: mpatel

Original creation time: 2010-09-07 06:52:51

Assignee: GeorgSWeber

CC:  mvngu timdumol

Minh Nguyen reported this about building a trial "final" 4.5.3 (essentially the same as 4.5.3.rc0) on rosemary.math, which is an Intel(R) Xeon(R) CPU X7460 `@` 2.66GHz system running RedHat Enterprise Linux (RHEL) Server 5.5

```
building '_imaging' extension
gcc -pthread -shared build/temp.linux-x86_64-2.6/_imaging.o build/temp.linux-x86
_64-2.6/decode.o build/temp.linux-x86_64-2.6/encode.o build/temp.linux-x86_64-2.
6/map.o build/temp.linux-x86_64-2.6/display.o build/temp.linux-x86_64-2.6/outlin
e.o build/temp.linux-x86_64-2.6/path.o build/temp.linux-x86_64-2.6/libImaging/Ac
cess.o build/temp.linux-x86_64-2.6/libImaging/Antialias.o build/temp.linux-x86_6
4-2.6/libImaging/Bands.o build/temp.linux-x86_64-2.6/libImaging/BitDecode.o buil
d/temp.linux-x86_64-2.6/libImaging/Blend.o build/temp.linux-x86_64-2.6/libImagin
g/Chops.o build/temp.linux-x86_64-2.6/libImaging/Convert.o build/temp.linux-x86_
64-2.6/libImaging/ConvertYCbCr.o build/temp.linux-x86_64-2.6/libImaging/Copy.o b
uild/temp.linux-x86_64-2.6/libImaging/Crc32.o build/temp.linux-x86_64-2.6/libIma
ging/Crop.o build/temp.linux-x86_64-2.6/libImaging/Dib.o build/temp.linux-x86_64
-2.6/libImaging/Draw.o build/temp.linux-x86_64-2.6/libImaging/Effects.o build/te
mp.linux-x86_64-2.6/libImaging/EpsEncode.o build/temp.linux-x86_64-2.6/libImagin
g/File.o build/temp.linux-x86_64-2.6/libImaging/Fill.o build/temp.linux-x86_64-2
.6/libImaging/Filter.o build/temp.linux-x86_64-2.6/libImaging/FliDecode.o build/
temp.linux-x86_64-2.6/libImaging/Geometry.o build/temp.linux-x86_64-2.6/libImagi
ng/GetBBox.o build/temp.linux-x86_64-2.6/libImaging/GifDecode.o build/temp.linux
-x86_64-2.6/libImaging/GifEncode.o build/temp.linux-x86_64-2.6/libImaging/HexDec
ode.o build/temp.linux-x86_64-2.6/libImaging/Histo.o build/temp.linux-x86_64-2.6
/libImaging/JpegDecode.o build/temp.linux-x86_64-2.6/libImaging/JpegEncode.o bui
ld/temp.linux-x86_64-2.6/libImaging/LzwDecode.o build/temp.linux-x86_64-2.6/libI
maging/Matrix.o build/temp.linux-x86_64-2.6/libImaging/ModeFilter.o build/temp.l
inux-x86_64-2.6/libImaging/MspDecode.o build/temp.linux-x86_64-2.6/libImaging/Ne
gative.o build/temp.linux-x86_64-2.6/libImaging/Offset.o build/temp.linux-x86_64
-2.6/libImaging/Pack.o build/temp.linux-x86_64-2.6/libImaging/PackDecode.o build
/temp.linux-x86_64-2.6/libImaging/Palette.o build/temp.linux-x86_64-2.6/libImagi
ng/Paste.o build/temp.linux-x86_64-2.6/libImaging/Quant.o build/temp.linux-x86_6
4-2.6/libImaging/QuantHash.o build/temp.linux-x86_64-2.6/libImaging/QuantHeap.o 
build/temp.linux-x86_64-2.6/libImaging/PcdDecode.o build/temp.linux-x86_64-2.6/l
ibImaging/PcxDecode.o build/temp.linux-x86_64-2.6/libImaging/PcxEncode.o build/t
emp.linux-x86_64-2.6/libImaging/Point.o build/temp.linux-x86_64-2.6/libImaging/R
ankFilter.o build/temp.linux-x86_64-2.6/libImaging/RawDecode.o build/temp.linux-
x86_64-2.6/libImaging/RawEncode.o build/temp.linux-x86_64-2.6/libImaging/Storage
.o build/temp.linux-x86_64-2.6/libImaging/SunRleDecode.o build/temp.linux-x86_64
-2.6/libImaging/TgaRleDecode.o build/temp.linux-x86_64-2.6/libImaging/Unpack.o b
uild/temp.linux-x86_64-2.6/libImaging/UnpackYCC.o build/temp.linux-x86_64-2.6/li
bImaging/XbmDecode.o build/temp.linux-x86_64-2.6/libImaging/XbmEncode.o build/te
mp.linux-x86_64-2.6/libImaging/ZipDecode.o build/temp.linux-x86_64-2.6/libImagin
g/ZipEncode.o -L/usr/local/lib -L/home/wstein/mvngu/sage-4.5.3/local/lib -L/usr/
lib -L/home/wstein/mvngu/sage-4.5.3/local/lib -ljpeg -lz -lpython2.6 -o build/li
b.linux-x86_64-2.6/_imaging.so
gcc -O3 -g -fPIC -I. -I/home/wstein/mvngu/sage-4.5.3/local/include -I/home/wstei
n/mvngu/sage-4.5.3/local/include  -DHAVE_CONFIG_H -c omList.c
/usr/bin/ld: skipping incompatible /usr/lib/libjpeg.so when searching for -ljpeg
/usr/bin/ld: /usr/local/lib/libpython2.6.a(abstract.o): relocation R_X86_64_32 a
gainst `a local symbol' can not be used when making a shared object; recompile w
ith -fPIC
/usr/local/lib/libpython2.6.a: could not read symbols: Bad value
collect2: ld returned 1 exit status
error: command 'gcc' failed with exit status 1
Error building PIL: 'Error installing PIL'

real    0m10.654s
user    0m8.426s
sys     0m2.141s
sage: An error occurred while installing pil-1.1.6.p2
```

The full build log is [here](http://wiki.sagemath.org/devel/BuildFarm/sage-4.5.3?action=AttachFile&do=get&target=rosemary.math-build.log.bz2).


---

Comment by drkirkby created at 2010-09-07 08:45:44

I would triple-check that all objects are built with position independent code (PIC), using the -fPIC option. There are three problems with PIC.

 * Libraries built without PIC run a bit more slowly. 
 * You can often get away without compiling PIC
 * Building shared libraries often works if one does not use PIC.

Because of this, sometimes people don't build PIC code. The GNU manual implies you should, but is not very clear about it. The Sun linker manual is absolutely clear - shared libraries should be built with PIC. 

I've also found that some libraries that should be position independent, do not appear to do so according to the link editor. See #9840 

I know of 2 possible issues that can arise. 

 * If the objects are compiled with -fPIC, but there's assembly code that is not  position independent then the resulting library may not work reliably. 
 * If shared libraries are created with the wrong options, which is the case with #9833, though only Solaris will be affected, as the options are only wrong on Solaris. 

but there are others. 

I'm aware of three libraries which show problems related to this on Solaris or OpenSolaris in 64-bit mode, but two of them might be an issue on all platforms. 

 * PolyBori 
 * Cliquer (will only affect Solaris or OpenSolaris)
 * ECL

If the system has the `elfdump` command, you might try this:


```
$ elfdump -d ./build/libecl.so |  grep TEXTREL
```


At least on Solaris, that should produce no output. If it does, it indicates a problem with the library. 

Dave


---

Comment by drkirkby created at 2010-09-07 08:47:19

`libecl.so` was just an example - do this on *all* libraries.


---

Comment by drkirkby created at 2010-09-07 08:50:32

I just noticed something else - this is using the wrong python:


```
/usr/local/lib/libpython2.6.a: could not read symbols: Bad value
```


I've seen this problem before - see #9209. In fact, perhaps this should be marked as a duplicate of #9209. 

Dave


---

Comment by AlexGhitza created at 2010-09-07 14:06:21

Here is another data point: I just built 4.5.3 from scratch on a machine
running RHEL Server 5.5, and had no problems whatsoever; also longtests
passed.  Here are the specs:


```
 [aghitza@soleil sage-4.5.3]$ uname -a
 Linux soleil.ms.unimelb.edu.au 2.6.18-194.11.3.el5 #1 SMP Mon Aug 23 15:51:38 EDT 2010 x86_64 x86_64 x86_64 GNU/Linux

 [aghitza@soleil sage-4.5.3]$ cat /etc/issue
 Red Hat Enterprise Linux Server release 5.5 (Tikanga)
 Kernel \r on an \m

 [aghitza@soleil sage-4.5.3]$ gcc -v
 Using built-in specs.
 Target: x86_64-redhat-linux
 Configured with: ../configure --prefix=/usr --mandir=/usr/share/man 
 --infodir=/usr/share/info --enable-shared --enable-threads=posix 
 --enable-checking=release --with-system-zlib --enable-__cxa_atexit 
 --disable-libunwind-exceptions --enable-libgcj-multifile 
 --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk 
 --disable-dssi --enable-plugin 
 --with-java-home=/usr/lib/jvm/java-1.4.2-gcj-1.4.2.0/jre 
 --with-cpu=generic --host=x86_64-redhat-linux
 Thread model: posix
 gcc version 4.1.2 20080704 (Red Hat 4.1.2-48)

 [aghitza@soleil ~]$ which python
 /usr/bin/python

 [aghitza@soleil ~]$ python
 Python 2.4.3 (#1, Jun 11 2009, 14:09:37) 
 [GCC 4.1.2 20080704 (Red Hat 4.1.2-44)] on linux2
 Type "help", "copyright", "credits" or "license" for more information.
 >>> 
```

 
Note in particular that the machine does have Python installed independently of Sage, but that did not seem to cause problems.


---

Comment by drkirkby created at 2010-09-07 14:13:45

Replying to [comment:5 AlexGhitza]:
> Here is another data point: I just built 4.5.3 from scratch on a machine
> running RHEL Server 5.5, and had no problems whatsoever; also longtests
> passed.  Here are the specs:
> 
> {{{
>  [aghitza`@`soleil sage-4.5.3]$ uname -a
>  Linux soleil.ms.unimelb.edu.au 2.6.18-194.11.3.el5 #1 SMP Mon Aug 23 15:51:38 EDT 2010 x86_64 x86_64 x86_64 GNU/Linux
> 
>  [aghitza`@`soleil sage-4.5.3]$ cat /etc/issue
>  Red Hat Enterprise Linux Server release 5.5 (Tikanga)
>  Kernel \r on an \m
> 
>  [aghitza`@`soleil sage-4.5.3]$ gcc -v
>  Using built-in specs.
>  Target: x86_64-redhat-linux
>  Configured with: ../configure --prefix=/usr --mandir=/usr/share/man 
>  --infodir=/usr/share/info --enable-shared --enable-threads=posix 
>  --enable-checking=release --with-system-zlib --enable-__cxa_atexit 
>  --disable-libunwind-exceptions --enable-libgcj-multifile 
>  --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk 
>  --disable-dssi --enable-plugin 
>  --with-java-home=/usr/lib/jvm/java-1.4.2-gcj-1.4.2.0/jre 
>  --with-cpu=generic --host=x86_64-redhat-linux
>  Thread model: posix
>  gcc version 4.1.2 20080704 (Red Hat 4.1.2-48)
> 
>  [aghitza`@`soleil ~]$ which python
>  /usr/bin/python
> 
>  [aghitza`@`soleil ~]$ python
>  Python 2.4.3 (#1, Jun 11 2009, 14:09:37) 
>  [GCC 4.1.2 20080704 (Red Hat 4.1.2-44)] on linux2
>  Type "help", "copyright", "credits" or "license" for more information.
>  >>> 
> }}}
>  
> Note in particular that the machine does have Python installed independently of Sage, but that did not seem to cause problems.


Note however that 
 * The above example
 * My Solaris failure on #9209
 * The Redhat Linux failure I link to on #9209 -  http://groups.google.com/group/sage-devel/browse_thread/thread/37a67ce63e68d55b?hl=en-GB

*all* had the directory `/usr/local/lib/libpython2.6.a` involved. 

I suspect there might be some packages which look under /usr/local/lib, before whatever is specific in Sage. 

Dave


---

Comment by AlexGhitza created at 2010-09-07 14:20:28

And I can confirm that `/usr/local/lib` doesn't have any Python libraries in it on the machine I tested.


---

Comment by drkirkby created at 2010-09-07 17:58:12

Another, somewhat related issue is #9551. In that case, Sage tried to write to `/usr/lib/python2.4/site-packages/` on `t2.math.washington.edu` despite I'd tried to build Sage under my home directory. 

I think any assumption that having the first python in the path being `$SAGE_LOCAL/bin/python` will mean Sage will *never* try to do anything with python outside `$SAGE_ROOT` is rather flawed. That assumption would seem to be valid 99% of the time, but there are the odd exceptions. I wish I could pin down what causes these rare exceptions. 

Another assumption that is sometimes flawed, is that having a library in `$SAGE_LOCAL/lib` will mean the same library anywhere else will always be ignored and not present any conflicts with the library in Sage. The fact the `iconv` library can't be installed reliably on Fedora and OpenSuse (see #8567) is one example of that. 

One possible hack to solve this PIL issue might be to change any occurrence of `/usr/local` in any PIL file to `/some/stupid/junk/path`. If that does not work, we could consider changing any occurances of `/usr/local` in the Python package to `/some/stupid/junk/path`. 

Dave


---

Comment by drkirkby created at 2010-09-07 18:01:43

Should this be a blocker for releasing 4.5.3? It's a pretty serious issue when copies of python in /usr/local are sometimes screwing up building Sage on two supported platforms (Solaris 10 and Redhat Linux).


---

Comment by drkirkby created at 2010-09-07 18:02:21

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-09-07 21:58:58

I've changed the milestone to 4.6, as I'll release 4.5.3 later today.


---

Comment by leif created at 2010-09-07 23:44:23


```
... -L/usr/local/lib -L/home/wstein/mvngu/sage-4.5.3/local/lib -L/usr/lib ...
```

is obviously wrong.


---

Comment by drkirkby created at 2010-09-08 00:51:52

Replying to [comment:12 leif]:
> {{{
> ... -L/usr/local/lib -L/home/wstein/mvngu/sage-4.5.3/local/lib -L/usr/lib ...
> }}}
> is obviously wrong.

Yes. 

There's some things in `patches/setup.py` which look odd to me, though since I don't know what SAGE_BINARY_BUILD is, I can't say for sure. 


```
       #
        # add standard directories

        if not SAGE_BINARY_BUILD:
            add_directory(library_dirs, "/usr/local/lib")
            add_directory(include_dirs, "/usr/local/include")

            add_directory(library_dirs, "/usr/lib")
            add_directory(include_dirs, "/usr/include")

        #
```


I think they should be removed from the pil package.


---

Comment by mpatel created at 2010-09-08 01:10:32

From the [Installation Guide](http://www.sagemath.org/doc/installation/source.html#environment-variables):

 SAGE_BINARY_BUILD - used by the pil package. If set to “yes”, then force Sage to use the versions of libjpeg, libtiff and libpng from $SAGE_ROOT/local/lib. Otherwise, allow the use of the system’s versions of these libraries.


---

Comment by leif created at 2010-09-08 01:50:32

I'm pretty sure we can simply delete the _first occurrence_ of

```python
            add_directory(library_dirs, "/usr/local/lib")
            # FIXME: check /opt/stuff directories here?
```

Who knows if at all the indentation is correct? The comment *below* apparently refers to the (closed) `elif`-Darwin branch. `/usr/local/lib` is added _again_ later (in the code, in the snippet Dave gave above), *after* `SAGE_LOCAL/lib` and `/usr/lib`, but since it's already in the path, the Sage directory ends up in the middle.


---

Comment by leif created at 2010-09-08 02:33:22

Btw, `s/2008/2009/` in the changelog for p1 and p2. ;-)


---

Comment by leif created at 2010-09-08 18:52:08

Replying to [comment:2 drkirkby]:
>  * Libraries built without PIC run a bit more slowly.

I guess you meant _"*with* PIC"_ (`-fpic` or `-fPIC`). (In general that depends on the architecture, and how the code is used.)

> I'm aware of three libraries which show problems related to this on Solaris or OpenSolaris in 64-bit mode, but two of them might be an issue on all platforms. 

>  * PolyBori

Did you report _that_, too? (Ticket?)
 
> If the system has the `elfdump` command, you might try this:
> 

```
$ elfdump -d ./build/libecl.so |  grep TEXTREL
```


There's also `nm`, binutils' `objdump`, and `readelf`.


---

Comment by drkirkby created at 2010-09-08 19:22:59

Replying to [comment:17 leif]:
> Replying to [comment:2 drkirkby]:
> >  * Libraries built without PIC run a bit more slowly.
> 
> I guess you meant _"*with* PIC"_ (`-fpic` or `-fPIC`). (In general that depends on the architecture, and how the code is used.)

Yes, I did. 

> > I'm aware of three libraries which show problems related to this on Solaris or OpenSolaris in 64-bit mode, but two of them might be an issue on all platforms. 
> 
> >  * PolyBori
> 
> Did you report _that_, too? (Ticket?)

Yes, I created a ticket yesterday. Alexander Dreyer is already working on it - see #9872 
  
Dave


---

Comment by mpatel created at 2010-09-11 22:29:57

Georg Weber [has suggested on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/4dbd239d7e9d7b0c/d409f9a25b8891fd#d409f9a25b8891fd) that we set `SAGE_BINARY_BUILD='yes'` by default.  Thoughts?


---

Comment by drkirkby created at 2010-09-11 22:51:25

Replying to [comment:19 mpatel]:
> Georg Weber [has suggested on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/4dbd239d7e9d7b0c/d409f9a25b8891fd#d409f9a25b8891fd) that we set `SAGE_BINARY_BUILD='yes'` by default.  Thoughts?

*Defiantly not.* 

The problem here is PIL looking for things in /usr/local. This is happening during the build process. I don't see how this is going to help this problem. The reason for looking for things in `/usr/local` needs to be resolved. Adding options like 


```
$ export SAGE_INCLUDE_pil_greatest-ever-library=/usr/local/greatest-ever-library
```


would be OK by me. Forcing `SAGE_BINARY_BUILD=yes` is not the answer IMHO. 

Dave


---

Comment by leif created at 2010-09-11 23:05:11

Replying to [comment:19 mpatel]:
> Georg Weber [has suggested on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/4dbd239d7e9d7b0c/d409f9a25b8891fd#d409f9a25b8891fd) that we set `SAGE_BINARY_BUILD='yes'` by default.  Thoughts?

As far as I understand this, one has to (manually) copy the build system's respective shared libraries into `$SAGE_LOCAL/lib` (_before_ building PIL) anyhow to make this effective. (Probably some headers into `$SAGE_LOCAL/include`, too.) So enabling `SAGE_BINARY_BUILD` by default (where?) doesn't make much sense to me.


---

Comment by niles created at 2010-09-24 15:23:13

Replying to [comment:21 leif]:
> Replying to [comment:19 mpatel]:
> > Georg Weber [has suggested on sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/4dbd239d7e9d7b0c/d409f9a25b8891fd#d409f9a25b8891fd) that we set `SAGE_BINARY_BUILD='yes'` by default.  Thoughts?
> 
> As far as I understand this, one has to (manually) copy the build system's respective shared libraries into `$SAGE_LOCAL/lib` (_before_ building PIL) anyhow to make this effective. (Probably some headers into `$SAGE_LOCAL/include`, too.) So enabling `SAGE_BINARY_BUILD` by default (where?) doesn't make much sense to me.

Maybe, as with [SAGE_PIL_NOTK](http://www.sagemath.org/doc/installation/source.html), sage should set `SAGE_BINARY_BUILD='yes'` if building PIL fails.


---

Comment by mpatel created at 2010-10-09 05:38:46

Are there any comments about the proposal by Niles?


---

Comment by timdumol created at 2010-10-09 13:49:47

Niles' suggestion seems optimal, however I do not have enough time at the moment (this week and the next) to think hard about it.


---

Comment by mpatel created at 2010-10-18 02:06:12

For what it's worth, in Tachyon's `spkg-install`, there's an example of retrying an spkg installation after an initial failure:

```sh
if [ $UNAME = "Linux" ]; then
    GCCVERSION=`gcc -dumpversion`
    case $GCCVERSION in
      4.2.4* | 4.3*)
        export GCCFIX="-fno-crossjumping -fno-reorder-blocks";;
      *);;
    esac
    make linux-thr
    if [ $? -ne 0 ]; then
        echo "Maybe your system is 64-bit; trying again."
        if [ `uname -m` = "ia64" ]; then
          echo "ia64"
          make linux-ia64-thr
        else
          echo "64-bit arch"
          make linux-64-thr
        fi
    fi
    finished
fi
```

(If it's possible to avoid doing this with Tachyon, we can open a new ticket for it.)


---

Comment by mpatel created at 2010-10-19 02:20:22

I'm changing the milestone to 4.6.1.  Of course, the next release manager is welcome to change the priority.


---

Comment by mpatel created at 2010-11-12 08:39:48

I've added a [RHEL 5.5 builder on Jon Hanke's machine rosemary](http://build.sagemath.org/sage/builders/RHEL%205.5-64%20(rosemary)).  The zeroth build [failed on PIL](http://build.sagemath.org/sage/builders/RHEL%205.5-64%20(rosemary)/builds/0/steps/shell_2/logs/pil).


---

Comment by mpatel created at 2010-11-25 12:15:38

Replying to [comment:15 leif]:
> I'm pretty sure we can simply delete the _first occurrence_ of


```python
            add_directory(library_dirs, "/usr/local/lib")
            # FIXME: check /opt/stuff directories here?
```


If I comment out this `add_directory` line, PIL builds successfully on rosemary.  The doctests that didn't pass previously -- in `plot/plot3d/base.pyx` -- now pass.

Does anyone see a reason to keep this line for any platform?  Has it not caused problems on other systems, because the systems haven't had a `/usr/local/lib/libpython2.6.a`?


> Who knows if at all the indentation is correct? The comment *below* apparently refers to the (closed) `elif`-Darwin branch. `/usr/local/lib` is added _again_ later (in the code, in the snippet Dave gave above), *after* `SAGE_LOCAL/lib` and `/usr/lib`, but since it's already in the path, the Sage directory ends up in the middle.

Indeed, with the original line, I get

```python
['/usr/local/lib', '/home/buildbot/build/sage/rosemary-1/rosemary_full/build/sage-4.6.1.alpha2/local/lib', '/usr/lib']  # library_dirs
['libImaging', '/home/buildbot/build/sage/rosemary-1/rosemary_full/build/sage-4.6.1.alpha2/local/include', '/usr/local/include', '/usr/include']  # include_dirs
```

but without it, I get

```python

['/home/buildbot/build/sage/rosemary-1/rosemary_full/build/sage-4.6.1.alpha2/local/lib', '/usr/local/lib', '/usr/lib']  # library_dirs
['libImaging', '/home/buildbot/build/sage/rosemary-1/rosemary_full/build/sage-4.6.1.alpha2/local/include', '/usr/local/include', '/usr/include']  # include_dirs
```



---

Comment by leif created at 2010-11-25 13:50:03

Replying to [comment:28 mpatel]:
> Replying to [comment:15 leif]:
> > I'm pretty sure we can simply delete the _first occurrence_ of
> 

```python
            add_directory(library_dirs, "/usr/local/lib")
            # FIXME: check /opt/stuff directories here?
```

> 
> If I comment out this `add_directory` line, PIL builds successfully on rosemary.  The doctests that didn't pass previously -- in `plot/plot3d/base.pyx` -- now pass.
> 
> Does anyone see a reason to keep this line for any platform?  Has it not caused problems on other systems, because the systems haven't had a `/usr/local/lib/libpython2.6.a`?

Yes please, can you create a patch such that we can close this ticket after month of deep thinking?

If new failures occur, we can open another ticket (I'm hopefully not cc'ed on ;-) ).

----

I'm wondering if I should open a ticket for changing `SAGE_PIL_NOTK` to `SAGE_PIL_NO_TK`...


---

Comment by mpatel created at 2010-11-26 10:10:53

Fix `library_dirs` order.  Use patch.  SPKG patch.


---

Comment by mpatel created at 2010-11-26 11:14:12

Changing status from new to needs_review.


---

Attachment

I've added a spkg link to the description and attached an SPKG patch.  The main changes:

 * Comment out the `/usr/local/lib` line [comment:15 pointed out by Leif].
 * Use `patch` to apply the patch.

The package installs successfully and the long doctests pass for me on bsd (OSX 10.6-32), eno (Fedora 13-64), hawk (OpenSolaris 06.2009-32), redhawk (Ubuntu 10-64), rosemary (RHEL 5.5-64), and sage.math (Ubuntu 8-64).


---

Comment by jdemeyer created at 2010-11-28 15:17:33

Changing status from needs_review to needs_work.


---

Comment by jdemeyer created at 2010-11-28 15:17:33

Thanks for the work on this ticket, I will do some more testing

About using `patch`: for sake of consistency, please follow the following instructions from [http://trac.sagemath.org/sage_trac/ticket/9419#comment:5](http://trac.sagemath.org/sage_trac/ticket/9419#comment:5):

```
1) create a directory pil-1.1.6.p2
2) cd pil-1.1.6.p2
3) put upstream source inpil-1.1.6.p2/src
For every ISSUE which needs to be patched, do the following:
    4) cp -pr src src.patched
    5) edit src.patched to fix ISSUE.
    6) diff -ur src src.patched >patches/ISSUE.patch
    7) rm -r src.patched
```


To apply the patches in `spkg-install`:

```
1) cd src
2) patch -p1 <../patches/ISSUE.patch
```



---

Comment by leif created at 2010-11-29 16:49:40

Replying to [comment:31 jdemeyer]:
> About using `patch`: for sake of consistency, please follow the following instructions from [http://trac.sagemath.org/sage_trac/ticket/9419#comment:5](http://trac.sagemath.org/sage_trac/ticket/9419#comment:5)...

Well, #9419 is not even in "needs review" state. I'm not sure if your method is the only desirable one; it at least lacks how we should document patches.

IMHO Mitesh's way is as appropiate here.


---

Comment by jdemeyer created at 2010-11-29 20:23:58

New package works fine on 64-bit Gentoo Linux, 32-bit Gentoo Linux, 32-bit OS X PPC.  So from a functionality point of view, this package gets a positive review from me.  I don't think I'm able to review the actual code though.


---

Comment by Koen created at 2010-11-30 15:56:49

I'm having issues with PIL 1.1.6p2 (the release version) not finding its JPEG libraries. These are located in /usr/lib64 on CentOS 5.5 / OpenSuse, however the default library path only considers /usr/lib. Adding /usr/lib64 as a library path fixes the problem in my stand-alone PIL build. I'm not quite sure how to patch the setup.py in SAGE to add this path by default.

The following part of the log shows the problem (or the lack of a jpeg_decoder function in PIL.Image.core)

--------------------------------------------------------------------
PIL 1.1.6 BUILD SUMMARY
--------------------------------------------------------------------
version       1.1.6
platform      linux2 2.6.4 (r264:75706, Oct  4 2010, 14:47:23)
              [GCC 4.3.4]
--------------------------------------------------------------------
*** TKINTER support not available
*** JPEG support not available
--- ZLIB (PNG/ZIP) support ok
--- FREETYPE2 support ok
--------------------------------------------------------------------


---

Comment by leif created at 2010-11-30 16:51:05

Replying to [comment:34 Koen]:
> I'm having issues with PIL 1.1.6p2 (the release version) not finding its JPEG libraries. These are located in /usr/lib64 on CentOS 5.5 / OpenSuse, however the default library path only considers /usr/lib. Adding /usr/lib64 as a library path fixes the problem in my stand-alone PIL build. I'm not quite sure how to patch the setup.py in SAGE to add this path by default.

Well, we should just check if `/usr/lib64` (and `/usr/local/lib64`) exist, and if so, add these *instead of* `/usr/lib` etc., unless `realpath("/usr/lib64") == realpath("/usr/lib")`. (We may also check we're really on a 64-bit system, too, though the presence of `/usr/lib64` should normally indicate that.)

Note that on other (64-bit) Linuces (e.g. Debian), `/usr/lib64` is a symbolic link to `/usr/lib`, while on Fedora etc. `/usr/lib` is a synonym of `/usr/lib32` (like on 32-bit systems).


---

Comment by leif created at 2010-11-30 17:31:52

Just noticed our `src/` isn't vanilla upstream:

```sh
~/Sage/spkgs$ diff -ur upstream/Imaging-1.1.6/ pil-1.1.6.p3/src/
Only in pil-1.1.6.p3/src/: ff
diff -ur upstream/Imaging-1.1.6/setup.py pil-1.1.6.p3/src/setup.py
--- upstream/Imaging-1.1.6/setup.py	2006-12-03 12:37:29.000000000 +0100
+++ pil-1.1.6.p3/src/setup.py	2010-11-26 10:39:04.000000000 +0100
@@ -90,6 +90,9 @@
 except ImportError:
     _tkinter = None
 
+# Force None, so don't build tk -- this helps on some platforms.
+_tkinter = None
+
 def add_directory(path, dir, where=None):
     if dir and os.path.isdir(dir) and dir not in path:
         if where is None:
```


(p3's `ff` is some left-over diff file.)


---

Comment by drkirkby created at 2010-11-30 17:37:20

Replying to [comment:35 leif]:
> Replying to [comment:34 Koen]:
> > I'm having issues with PIL 1.1.6p2 (the release version) not finding its JPEG libraries. These are located in /usr/lib64 on CentOS 5.5 / OpenSuse, however the default library path only considers /usr/lib. Adding /usr/lib64 as a library path fixes the problem in my stand-alone PIL build. I'm not quite sure how to patch the setup.py in SAGE to add this path by default.
> 
> Well, we should just check if `/usr/lib64` (and `/usr/local/lib64`) exist, and if so, add these *instead of* `/usr/lib` etc., unless `realpath("/usr/lib64") == realpath("/usr/lib")`. (We may also check we're really on a 64-bit system, too, though the presence of `/usr/lib64` should normally indicate that.

> I'm having issues with PIL 1.1.6p2 (the release version) not finding its JPEG libraries. These are located in /usr/lib64 on CentOS 5.5 / OpenSuse, however the default library path only considers /usr/lib. Adding /usr/lib64 as a library path fixes the problem in my stand-alone PIL build. I'm not quite sure how to patch the setup.py in SAGE to add this path by default.

Is it essential to have the JPEG libraries? If not, then they should be excluded when `SAGE_FAT_BINARY=yes`, otherwise we risk breakages if people install a Sage binary on a system without these libraries. 

I'm puzzled why it should be necessary to so add `/usr/lib64`. Has someone mis-configured the system? 

On every system that I know, that is able to build both 32-bit and 64-bit libraries, the runtime lnker will always search for the 64-bit ones when building 64-bit code. On Solaris the 64-bit libraries are in `/usr/lib/sparcv9` or `/usr/lib/amd64`, depending on the CPU type. But the run time linker knows that, and will search for them:One never needs to put `/usr/lib/sparcv9` or `/usr/lib/amd64` in any sort of PATH (LD_LIBRARY_PATH etc). 


```
-bash-3.00$ crle    

Default configuration file (/var/ld/ld.config) not found
  Default Library Path (ELF):   /lib:/usr/lib  (system default)
  Trusted Directories (ELF):    /lib/secure:/usr/lib/secure  (system default)
-bash-3.00$ crle -64

Default configuration file (/var/ld/64/ld.config) not found
  Default Library Path (ELF):   /lib/64:/usr/lib/64  (system default)
  Trusted Directories (ELF):    /lib/secure/64:/usr/lib/secure/64  (system default)
-bash-3.00$ 
```


It's a complely different matter in directories like `/usr/local/lib/sparcv9` since the run time linker does not to search there. 

I know this is true on HP-UX too. 

On AIX, the libraries are in an archives containing both 32-bit and 64-bit libraries in the same archive. But again, the run-time linker knows how to find them. 

Clearly if the system is mis-configured, we should not work around the problem. 

I think we should ascertain if someone has mis-configured the system before proceeding to patch Sage

Dave


---

Comment by leif created at 2010-11-30 18:44:54

Replying to [comment:37 drkirkby]:
> I'm puzzled why it should be necessary to so add `/usr/lib64`. Has someone mis-configured the system? ;
> 
> On every system that I know, that is able to build both 32-bit and 64-bit libraries, the runtime lnker will always search for the 64-bit ones when building 64-bit code. [...]

Perhaps a look at `setup.py` answers some of your questions... ;-)

(And no, the Linux system having 64-bit libraries [only] in `/usr/lib64` is not "misconfigured", see above. We had to add a similar patch to PARI's graphics detection for the same reason btw.)


---

Comment by drkirkby created at 2010-11-30 21:00:48

Replying to [comment:38 leif]:

> (And no, the Linux system having 64-bit libraries [only] in `/usr/lib64` is not "misconfigured", 

I was not saying having the 64-bit libraries only in /usr/lib64 was mis-configured - I would expect that. What I question is why the 64-bit libraries are not found. I would have thought the operating system would have been configured so linking them would find them, without one needing to specify a path. Clearly if the libraries are in a non-standard place, then I would expect it, but not when they are in the standard


---

Comment by Koen created at 2010-11-30 21:37:07

It's because the PIL setup.py is trying to be smart: it creates its own list of search paths for includes & libs, and when it cannot find jpeglib.h in the includes or libjpeg.so in the libraries search paths, it will disable its own JPEG support. However, it does not check a common place for 64-bit Linuxes (which are not Debian-based), so right now it is too eager in disabling JPEG support.
Note that SciPy uses PIL to read JPEG images, so not having it working is quite annoying.


---

Comment by leif created at 2010-12-01 00:28:17

Replying to [comment:40 Koen]:
> It's because the PIL setup.py is trying to be smart: it creates its own list of search paths for includes & libs, and when it cannot find jpeglib.h in the includes or libjpeg.so in the libraries search paths, it will disable its own JPEG support. However, it does not check a common place for 64-bit Linuxes (which are not Debian-based), so right now it is too eager in disabling JPEG support.
> Note that SciPy uses PIL to read JPEG images, so not having it working is quite annoying.

Yep. If we don't fix that (here), you could still create symbolic links in `SAGE_LOCAL/{include,lib}`; then PIL should find them as well.

(If we build binary distributions (with e.g. JPEG support enabled), we have to manually _copy_ the system's respective libraries and headers to `SAGE_LOCAL/...` anyway.)


---

Comment by leif created at 2010-12-01 00:44:02

Replying to [comment:41 leif]:
> If we don't fix that (here), you could still create symbolic links in `SAGE_LOCAL/{include,lib}`; then PIL should find them as well.

P.S.: PIL 1.1.7 adds a `find_include_file()` function, but still won't find a library in `/usr/lib64`, so I think we should fix that, not sure if on this ticket though.


---

Comment by leif created at 2010-12-01 03:29:00

I've uploaded a slightly modified p3 spkg:

*http://spkg-upload.googlecode.com/files/pil-1.1.6.p3.spkg*

*md5sum:* `5453cd4356f1cfa9e1c097b0f7dcc609  pil-1.1.6.p3.spkg`

(`src/` is now vanilla -> patch rebased; some clean-up, additions to `SPKG.txt`.)

Does *not* fix the `.../lib64` issue; this should IMHO go onto another ticket.


---

Comment by leif created at 2010-12-01 03:29:00

Changing status from needs_work to needs_review.


---

Comment by leif created at 2010-12-01 03:31:00

SPKG patch, based on Mitesh's p3. Upstream now vanilla, some clean-up.


---

Attachment


---

Comment by leif created at 2010-12-01 03:53:58

Replying to [comment:43 leif]:
> Does *not* fix the `.../lib64` issue; this should IMHO go onto another ticket.

I've opened http://trac.sagemath.org/sage_trac/ticket/10359 to address that issue.


---

Comment by jdemeyer created at 2010-12-02 13:05:00

Changing keywords from "" to "pil spkg".


---

Comment by jdemeyer created at 2010-12-05 11:57:01

Resolution: fixed


---

Comment by jdemeyer created at 2010-12-05 11:57:01

Positive review implicit by #10359.


---

Comment by mpatel created at 2010-12-07 02:31:52

Thanks, Leif!
