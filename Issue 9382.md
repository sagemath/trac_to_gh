# Issue 9382: atlas not respecting SAGE_FAT_BINARY on i686 systems

Issue created by migration from https://trac.sagemath.org/ticket/9382

Original creator: mariah

Original creation time: 2010-06-29 20:18:14

Assignee: Mariah Lenox

atlas on i686 systems (x86-Linux) is
not respecting SAGE_FAT_BINARY.

The attached mercurial patch adds
i686 to the list of other architectures
(i386, x86_64) that respect SAGE_FAT_BINARY.


---

Attachment


---

Comment by mariah created at 2010-06-29 20:18:46

Changing status from new to needs_review.


---

Comment by was created at 2010-07-06 13:17:27

Very likely positive review -- just need Robert Miller to try it on some 32-bit linux box.


---

Comment by rlm created at 2010-07-09 09:38:13

Changing status from needs_review to needs_work.


---

Comment by rlm created at 2010-07-09 09:38:13

I get an error installing atlas with this patch:

```
Host system
uname -a:
Linux cicero 2.6.32.12-115.fc12.i686.PAE #1 SMP Fri Apr 30 20:14:08 UTC 2010 i686 i686 i386 GNU/Linux
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: i686-redhat-linux
Configured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre --enable-libgcj-multifile --enable-java-maintainer-mode --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --disable-libjava-multilib --with-ppl --with-cloog --with-tune=generic --with-arch=i686 --build=i686-redhat-linux
Thread model: posix
gcc version 4.4.4 20100630 (Red Hat 4.4.4-10) (GCC) 
****************************************************
Platform detected to be 32 bits
system_atlas.py:6: DeprecationWarning: os.popen2 is deprecated.  Use the subprocess module.
  fortran = os.popen2(os.environ['SAGE_LOCAL']+'/bin/'+'which_fortran')[1].read()
./spkg-install-script: line 119: syntax error near unexpected token `}'
./spkg-install-script: line 119: `}'
Failed to build ATLAS.

real    0m0.326s
user    0m0.129s
sys     0m0.122s
sage: An error occurred while installing atlas-3.8.3.p13
```


Looking at the patch, do I see a mismatched single quote?


---

Comment by jhpalmieri created at 2010-07-10 03:31:03

> Looking at the patch, do I see a mismatched single quote?

That's what it looks like to me.  What if you just delete the quote?  Replace

```
if [ "`uname -p`" = "i386" -o "'`uname -p`" = "i686" -o `uname -p`" = "x86_64" ]; then 
```

with

```
if [ "`uname -p`" = "i386" -o "`uname -p`" = "i686" -o `uname -p`" = "x86_64" ]; then 
```

(no single quote before the second ``uname...``).


---

Comment by rlm created at 2010-07-11 21:05:58

The third uname then has a mismatched double quote.


---

Comment by mariah created at 2010-07-15 17:45:07

Apologies for my silly error.  Here is a revised patch [9382.patch](http://boxen.math.washington.edu/home/mariah/spkgs/9382.patch) and the corresponding spkg [atlas-3.8.3.p13.spkg](http://boxen.math.washington.edu/mariah/spkgs/atlas-3.8.3.p13.spkg).


---

Comment by mariah created at 2010-07-15 17:45:07

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2010-11-09 03:03:58

A similar problem has been noticed in Arch Linux: https://bugs.archlinux.org/task/21592


```
18:44 < td123> hello
18:45 < td123> it seems that when building sage, it doesn't respect the 
               SAGE_FAT_BINARY='yes' option because I built sage with that 
               option on a corei7 for x86 and someone kept getting illegal 
               instruction on a pentium 3
18:45 < td123> when I looked through the logs, it seemed that atlas (among 
               possibly others) were building with processort specific 
               optimizations
18:48 < td123> I'm the packager for archlinux :) 
http://repos.archlinux.org/wsvn/community/sage-mathematics/trunk/PKGBUILD is 
               the package source
```



---

Comment by wjp created at 2010-12-06 18:03:42

Changing status from needs_review to needs_work.


---

Comment by wjp created at 2010-12-06 18:03:42

`uname -p` on linux returns a textual description of the CPU for me, not a canonical architecture name. It looks like this may have to be `uname -m` on Linux.

On the other hand, on solaris it looks like `uname -p` is correct.

As `td123` on IRC suggested, maybe we should just check both the results of `-m` and `-p` for these values?


---

Comment by wjp created at 2011-01-08 23:30:04

Changing status from needs_work to needs_review.


---

Comment by wjp created at 2011-01-08 23:30:04

I've done that:

http://www.math.leidenuniv.nl/~wpalenst/sage/atlas-3.8.3.p17.spkg

http://www.math.leidenuniv.nl/~wpalenst/sage/9382_atlas_i686_fat.patch


---

Comment by vbraun created at 2011-01-09 17:26:04

Willem: which machine and which uname outputs are you referring to in comment 8?

Instead of hacking around the current atlas build script, I think it would be a good point to switch to my rewritten atlas spkg at #10226 that detects the configuration in a much cleaner way.


---

Comment by wjp created at 2011-01-09 17:29:34

Nearly every linux machine I've tried, with a few exceptions where `uname -m` and `uname -p` give the same output.

Example (a 64 bit Gentoo machine):


```
mira: ~ > uname -m
x86_64
mira: ~ > uname -p
Intel(R) Xeon(R) CPU X3220 @ 2.40GHz
```



---

Comment by ddrake created at 2011-01-11 02:11:40

updated version of previous patches


---

Attachment

Replying to [comment:6 mariah]:
> Apologies for my silly error.  Here is a revised patch [9382.patch](http://boxen.math.washington.edu/home/mariah/spkgs/9382.patch)

That patch has another tiny error: it has "`uname-p`" (no space between "uname" and "-p"). I just uploaded a patch to this ticket in which I fixed that problem. However, there are other problems: on Ubuntu, it seems that `uname -p` returns "unknown" and `uname -m` returns the architecture name that we want. I've tried this on several 32-bit and 64-bit (i.e., i686 and x86_64) computers, on Ubuntu 8.04, 10.04, and 10.10 and they all behave the same. So we will need to use "-m" to correctly detect this on Ubuntu.


---

Comment by ddrake created at 2011-01-11 02:17:09

Changing status from needs_review to needs_work.


---

Comment by wjp created at 2011-01-11 02:37:00

You're looking at an old version of the patch. The most up to date one is the SPKG in comment #9.

Also, #10226 (which also needs review) might supersede this patch.


---

Comment by wjp created at 2011-01-11 02:37:00

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2011-01-11 03:30:46

Replying to [comment:14 wjp]:
> Also, #10226 (which also needs review) might supersede this patch.

It does, and I think we should work on that ticket and close this one when #10226 gets merged.


---

Comment by leif created at 2011-08-03 07:07:37

Replying to [comment:15 ddrake]:
> Replying to [comment:14 wjp]:
> > Also, #10226 (which also needs review) might supersede this patch.
> 
> It does, and I think we should work on that ticket and close this one when #10226 gets merged.

I currently don't know whether the new (_Python_ install script) ATLAS spkg from #10226 supports `SAGE_FAT_BINARY` as desired, but for the record:

 * `uname -p` isn't portable (it may return "`unknown`" even on Linuces), one should use `uname -m` instead.

 * Rather than having (btw. incomplete)

```sh
    if [ ... -o ... -o ... -o ... ]; then ...
```

 one should use

```sh
    case "`uname -m`" in
      i[3456]86|i86pc)
        ...
        ;;
      amd64|x86_64)
        ...
        ;;
      ia64) # Itanium
        ...
        ;;
      # etc.
    esac
```

 instead, which is not only more readable, but also more robust (and portable w.r.t. broken / buggy `test` commands).


---

Comment by vbraun created at 2011-08-03 09:04:02

For the record, the updated ATLAS spkg from #10226 uses the `$UNAME` environment variable (which Sage sets) if available, and python's portable `platform.system()` otherwise:


```python
try:
    conf['system'] = os.environ['UNAME']
except KeyError:
    conf['system'] = platform.system()
```

Also there is some support for `SAGE_FAT_BINARY`:

```python
    if os.environ.get('SAGE_FAT_BINARY', 'no') == 'yes' and conf['Intel?']:
        print 'Sage "fat" binary mode set: Building SSE2 only Hammer binary'
        print 'NOTE: This can result in a Sage that is significantly slower at certain numerical'
        print 'linear algebra since full FAT binary support has not been implemented yet.'
        arch = 'HAMMER'
        isa_ext = ('SSE2', 'SSE1')
```

Though I'm not sure if anybody ever verified that ATLAS, with these settings, indeed does not use any more advanced isa extensions.


---

Comment by vbraun created at 2011-08-03 09:07:31

Oops we are talking about `uname -m`. For this, I'm using `platform.machine()`:

```python
conf['Intel?'] = (platform.machine() in ('i386', 'i486', 'i586', 'i686', 'x86_64', 
                                         'AMD64', 'i86pc'))
conf['IA64?']   = (platform.processor() == 'ia64')
conf['PPC?']   = (platform.processor() == 'powerpc')
conf['SPARC?'] = (platform.processor() == 'sparc')
```



---

Comment by leif created at 2011-08-03 10:25:52

Replying to [comment:17 vbraun]:
> Though I'm not sure if anybody ever verified that ATLAS, with these settings, indeed does not use any more advanced isa extensions.

Regarding that a) the notion of "fat" binaries is misleading (because "fat" originally refers to *different* code for different [flavours of] processors in the *same* binary / executable), and b) there's neither a definition nor a consistent practice of what ISA subsets Sage uses if `SAGE_FAT_BINARY=yes`, I think we can then close this ticket.

If someone complains, we can always change the behaviour of the affected spkg(s); with the exception of AFAIK very rare `SIGILL` reports for binary distributions Mariah seems to be the only one who actually regularly tests this feature.

We could of course over time collect what different spkgs do, on a wiki page, though.

(For most packages and binary distributions adding `-march=...` or `-mcpu=...` to `CFLAGS` -- or configuring GCC to default to these -- should be sufficient anyway; building binary Sage distributions on less advanced processors is another way.)


---

Comment by vbraun created at 2011-08-03 10:46:57

I agree and will set this ticket to positive review.

Since it is hard/impossible to tell the gcc flags from the compiled binary, I think we should eventually move the `SAGE_FAT_BINARY` support into the compilerwrapper. It would be easy for the compilerwrapper to set the desired `-march` / `-mtune` flags consistently for each binary that we build. 

PS: `-mcpu` is a deprecated synonym for `-mtune`.

Release manager: this ticket is fixed by #10226 and can be closed.


---

Comment by vbraun created at 2011-08-03 10:46:57

Changing status from needs_review to positive_review.


---

Comment by leif created at 2011-08-03 11:45:05

Replying to [comment:20 vbraun]:
> PS: `-mcpu` is a deprecated synonym for `-mtune`.

Nope, `-mcpu` selects the instruction set, while `-mtune` only affects timing-specific choices (selection or reordering of instructions of that subset); `-march=foo` is equivalent to `-mcpu=foo -mtune=foo`. (I don't think that's changed recently, though `configure` supports `--with-arch-NN=...` and `--with-tune-NN=...`, NN in {32, 64}.)

----

Should we cc Jeroen and delete the ticket from the wishlist wiki page?


---

Comment by vbraun created at 2011-08-03 11:53:10

Well http://gcc.gnu.org/onlinedocs/gcc-4.6.1/gcc/i386-and-x86_002d64-Options.html#i386-and-x86_002d64-Options says:

```
-mcpu=cpu-type
    A deprecated synonym for -mtune. 
```

The instruction set is selected with `-march`. 

We should remove the ticket from the wishlist. Jeroen will close this ticket when he gets around to it, no need to contact him.


---

Comment by leif created at 2011-08-03 12:17:57

Replying to [comment:22 vbraun]:
>

```
-mcpu=cpu-type
    A deprecated synonym for -mtune. 
```

Maybe a long-lasting typo (at least since GCC 4.3.3, to be reported upstream ;-) ). Sections on other architectures describe the [IMHO] correct meaning. Or it has been inconsistent for x86 from the beginning, and therefore been deprecated.


---

Comment by vbraun created at 2011-08-03 12:34:56

I don't see any consistency across architectures:

  * x86 has `-march` and `-mtune`==`-mcpu`
  * ARM has `-march` and `-mtune`==`-mcpu` (except perhaps with fewer possible values??)
  * MIPS has `-march` and `-mtune` but not `-mcpu`
  * PowerPC does not have `-march`, but supports `-mtune` and `-mcpu`

There is a ton of dead architectures, but I don't think they have any up-to-date interface.


---

Comment by jdemeyer created at 2011-08-03 14:43:14

Resolution: duplicate
