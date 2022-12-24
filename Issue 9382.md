# Issue 9382: atlas not respecting SAGE_FAT_BINARY on i686 systems

archive/issues_009382.json:
```json
{
    "body": "Assignee: Mariah Lenox\n\natlas on i686 systems (x86-Linux) is\nnot respecting SAGE_FAT_BINARY.\n\nThe attached mercurial patch adds\ni686 to the list of other architectures\n(i386, x86_64) that respect SAGE_FAT_BINARY.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9382\n\n",
    "created_at": "2010-06-29T20:18:14Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "title": "atlas not respecting SAGE_FAT_BINARY on i686 systems",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9382",
    "user": "mariah"
}
```
Assignee: Mariah Lenox

atlas on i686 systems (x86-Linux) is
not respecting SAGE_FAT_BINARY.

The attached mercurial patch adds
i686 to the list of other architectures
(i386, x86_64) that respect SAGE_FAT_BINARY.

Issue created by migration from https://trac.sagemath.org/ticket/9382





---

archive/issue_comments_089173.json:
```json
{
    "body": "Attachment [atlas-i686-FAT.patch](tarball://root/attachments/some-uuid/ticket9382/atlas-i686-FAT.patch) by mariah created at 2010-06-29 20:18:46",
    "created_at": "2010-06-29T20:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89173",
    "user": "mariah"
}
```

Attachment [atlas-i686-FAT.patch](tarball://root/attachments/some-uuid/ticket9382/atlas-i686-FAT.patch) by mariah created at 2010-06-29 20:18:46



---

archive/issue_comments_089174.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-29T20:18:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89174",
    "user": "mariah"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089175.json:
```json
{
    "body": "Very likely positive review -- just need Robert Miller to try it on some 32-bit linux box.",
    "created_at": "2010-07-06T13:17:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89175",
    "user": "was"
}
```

Very likely positive review -- just need Robert Miller to try it on some 32-bit linux box.



---

archive/issue_comments_089176.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-07-09T09:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89176",
    "user": "rlm"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089177.json:
```json
{
    "body": "I get an error installing atlas with this patch:\n\n```\nHost system\nuname -a:\nLinux cicero 2.6.32.12-115.fc12.i686.PAE #1 SMP Fri Apr 30 20:14:08 UTC 2010 i686 i686 i386 GNU/Linux\n****************************************************\n****************************************************\nCC Version\ngcc -v\nUsing built-in specs.\nTarget: i686-redhat-linux\nConfigured with: ../configure --prefix=/usr --mandir=/usr/share/man --infodir=/usr/share/info --with-bugurl=http://bugzilla.redhat.com/bugzilla --enable-bootstrap --enable-shared --enable-threads=posix --enable-checking=release --with-system-zlib --enable-__cxa_atexit --disable-libunwind-exceptions --enable-gnu-unique-object --enable-languages=c,c++,objc,obj-c++,java,fortran,ada --enable-java-awt=gtk --disable-dssi --enable-plugin --with-java-home=/usr/lib/jvm/java-1.5.0-gcj-1.5.0.0/jre --enable-libgcj-multifile --enable-java-maintainer-mode --with-ecj-jar=/usr/share/java/eclipse-ecj.jar --disable-libjava-multilib --with-ppl --with-cloog --with-tune=generic --with-arch=i686 --build=i686-redhat-linux\nThread model: posix\ngcc version 4.4.4 20100630 (Red Hat 4.4.4-10) (GCC) \n****************************************************\nPlatform detected to be 32 bits\nsystem_atlas.py:6: DeprecationWarning: os.popen2 is deprecated.  Use the subprocess module.\n  fortran = os.popen2(os.environ['SAGE_LOCAL']+'/bin/'+'which_fortran')[1].read()\n./spkg-install-script: line 119: syntax error near unexpected token `}'\n./spkg-install-script: line 119: `}'\nFailed to build ATLAS.\n\nreal    0m0.326s\nuser    0m0.129s\nsys     0m0.122s\nsage: An error occurred while installing atlas-3.8.3.p13\n```\n\n\nLooking at the patch, do I see a mismatched single quote?",
    "created_at": "2010-07-09T09:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89177",
    "user": "rlm"
}
```

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

archive/issue_comments_089178.json:
```json
{
    "body": "> Looking at the patch, do I see a mismatched single quote?\n\nThat's what it looks like to me.  What if you just delete the quote?  Replace\n\n```\nif [ \"`uname -p`\" = \"i386\" -o \"'`uname -p`\" = \"i686\" -o `uname -p`\" = \"x86_64\" ]; then \n```\n\nwith\n\n```\nif [ \"`uname -p`\" = \"i386\" -o \"`uname -p`\" = \"i686\" -o `uname -p`\" = \"x86_64\" ]; then \n```\n\n(no single quote before the second ``uname...``).",
    "created_at": "2010-07-10T03:31:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89178",
    "user": "jhpalmieri"
}
```

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

archive/issue_comments_089179.json:
```json
{
    "body": "The third uname then has a mismatched double quote.",
    "created_at": "2010-07-11T21:05:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89179",
    "user": "rlm"
}
```

The third uname then has a mismatched double quote.



---

archive/issue_comments_089180.json:
```json
{
    "body": "Apologies for my silly error.  Here is a revised patch [9382.patch](http://boxen.math.washington.edu/home/mariah/spkgs/9382.patch) and the corresponding spkg [atlas-3.8.3.p13.spkg](http://boxen.math.washington.edu/mariah/spkgs/atlas-3.8.3.p13.spkg).",
    "created_at": "2010-07-15T17:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89180",
    "user": "mariah"
}
```

Apologies for my silly error.  Here is a revised patch [9382.patch](http://boxen.math.washington.edu/home/mariah/spkgs/9382.patch) and the corresponding spkg [atlas-3.8.3.p13.spkg](http://boxen.math.washington.edu/mariah/spkgs/atlas-3.8.3.p13.spkg).



---

archive/issue_comments_089181.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-15T17:45:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89181",
    "user": "mariah"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089182.json:
```json
{
    "body": "A similar problem has been noticed in Arch Linux: https://bugs.archlinux.org/task/21592\n\n\n```\n18:44 < td123> hello\n18:45 < td123> it seems that when building sage, it doesn't respect the \n               SAGE_FAT_BINARY='yes' option because I built sage with that \n               option on a corei7 for x86 and someone kept getting illegal \n               instruction on a pentium 3\n18:45 < td123> when I looked through the logs, it seemed that atlas (among \n               possibly others) were building with processort specific \n               optimizations\n18:48 < td123> I'm the packager for archlinux :) \nhttp://repos.archlinux.org/wsvn/community/sage-mathematics/trunk/PKGBUILD is \n               the package source\n```\n",
    "created_at": "2010-11-09T03:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89182",
    "user": "ddrake"
}
```

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

archive/issue_comments_089183.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-06T18:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89183",
    "user": "wjp"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089184.json:
```json
{
    "body": "`uname -p` on linux returns a textual description of the CPU for me, not a canonical architecture name. It looks like this may have to be `uname -m` on Linux.\n\nOn the other hand, on solaris it looks like `uname -p` is correct.\n\nAs `td123` on IRC suggested, maybe we should just check both the results of `-m` and `-p` for these values?",
    "created_at": "2010-12-06T18:03:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89184",
    "user": "wjp"
}
```

`uname -p` on linux returns a textual description of the CPU for me, not a canonical architecture name. It looks like this may have to be `uname -m` on Linux.

On the other hand, on solaris it looks like `uname -p` is correct.

As `td123` on IRC suggested, maybe we should just check both the results of `-m` and `-p` for these values?



---

archive/issue_comments_089185.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-08T23:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89185",
    "user": "wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089186.json:
```json
{
    "body": "I've done that:\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/atlas-3.8.3.p17.spkg\n\nhttp://www.math.leidenuniv.nl/~wpalenst/sage/9382_atlas_i686_fat.patch",
    "created_at": "2011-01-08T23:30:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89186",
    "user": "wjp"
}
```

I've done that:

http://www.math.leidenuniv.nl/~wpalenst/sage/atlas-3.8.3.p17.spkg

http://www.math.leidenuniv.nl/~wpalenst/sage/9382_atlas_i686_fat.patch



---

archive/issue_comments_089187.json:
```json
{
    "body": "Willem: which machine and which uname outputs are you referring to in comment 8?\n\nInstead of hacking around the current atlas build script, I think it would be a good point to switch to my rewritten atlas spkg at #10226 that detects the configuration in a much cleaner way.",
    "created_at": "2011-01-09T17:26:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89187",
    "user": "vbraun"
}
```

Willem: which machine and which uname outputs are you referring to in comment 8?

Instead of hacking around the current atlas build script, I think it would be a good point to switch to my rewritten atlas spkg at #10226 that detects the configuration in a much cleaner way.



---

archive/issue_comments_089188.json:
```json
{
    "body": "Nearly every linux machine I've tried, with a few exceptions where `uname -m` and `uname -p` give the same output.\n\nExample (a 64 bit Gentoo machine):\n\n\n```\nmira: ~ > uname -m\nx86_64\nmira: ~ > uname -p\nIntel(R) Xeon(R) CPU X3220 @ 2.40GHz\n```\n",
    "created_at": "2011-01-09T17:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89188",
    "user": "wjp"
}
```

Nearly every linux machine I've tried, with a few exceptions where `uname -m` and `uname -p` give the same output.

Example (a 64 bit Gentoo machine):


```
mira: ~ > uname -m
x86_64
mira: ~ > uname -p
Intel(R) Xeon(R) CPU X3220 @ 2.40GHz
```




---

archive/issue_comments_089189.json:
```json
{
    "body": "updated version of previous patches",
    "created_at": "2011-01-11T02:11:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89189",
    "user": "ddrake"
}
```

updated version of previous patches



---

archive/issue_comments_089190.json:
```json
{
    "body": "Attachment [9382.patch](tarball://root/attachments/some-uuid/ticket9382/9382.patch) by ddrake created at 2011-01-11 02:16:57\n\nReplying to [comment:6 mariah]:\n> Apologies for my silly error.  Here is a revised patch [9382.patch](http://boxen.math.washington.edu/home/mariah/spkgs/9382.patch)\n\nThat patch has another tiny error: it has \"`uname-p`\" (no space between \"uname\" and \"-p\"). I just uploaded a patch to this ticket in which I fixed that problem. However, there are other problems: on Ubuntu, it seems that `uname -p` returns \"unknown\" and `uname -m` returns the architecture name that we want. I've tried this on several 32-bit and 64-bit (i.e., i686 and x86_64) computers, on Ubuntu 8.04, 10.04, and 10.10 and they all behave the same. So we will need to use \"-m\" to correctly detect this on Ubuntu.",
    "created_at": "2011-01-11T02:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89190",
    "user": "ddrake"
}
```

Attachment [9382.patch](tarball://root/attachments/some-uuid/ticket9382/9382.patch) by ddrake created at 2011-01-11 02:16:57

Replying to [comment:6 mariah]:
> Apologies for my silly error.  Here is a revised patch [9382.patch](http://boxen.math.washington.edu/home/mariah/spkgs/9382.patch)

That patch has another tiny error: it has "`uname-p`" (no space between "uname" and "-p"). I just uploaded a patch to this ticket in which I fixed that problem. However, there are other problems: on Ubuntu, it seems that `uname -p` returns "unknown" and `uname -m` returns the architecture name that we want. I've tried this on several 32-bit and 64-bit (i.e., i686 and x86_64) computers, on Ubuntu 8.04, 10.04, and 10.10 and they all behave the same. So we will need to use "-m" to correctly detect this on Ubuntu.



---

archive/issue_comments_089191.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2011-01-11T02:17:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89191",
    "user": "ddrake"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089192.json:
```json
{
    "body": "You're looking at an old version of the patch. The most up to date one is the SPKG in comment #9.\n\nAlso, #10226 (which also needs review) might supersede this patch.",
    "created_at": "2011-01-11T02:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89192",
    "user": "wjp"
}
```

You're looking at an old version of the patch. The most up to date one is the SPKG in comment #9.

Also, #10226 (which also needs review) might supersede this patch.



---

archive/issue_comments_089193.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-11T02:37:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89193",
    "user": "wjp"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089194.json:
```json
{
    "body": "Replying to [comment:14 wjp]:\n> Also, #10226 (which also needs review) might supersede this patch.\n\nIt does, and I think we should work on that ticket and close this one when #10226 gets merged.",
    "created_at": "2011-01-11T03:30:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89194",
    "user": "ddrake"
}
```

Replying to [comment:14 wjp]:
> Also, #10226 (which also needs review) might supersede this patch.

It does, and I think we should work on that ticket and close this one when #10226 gets merged.



---

archive/issue_comments_089195.json:
```json
{
    "body": "Replying to [comment:15 ddrake]:\n> Replying to [comment:14 wjp]:\n> > Also, #10226 (which also needs review) might supersede this patch.\n> \n> It does, and I think we should work on that ticket and close this one when #10226 gets merged.\n\nI currently don't know whether the new (*Python* install script) ATLAS spkg from #10226 supports `SAGE_FAT_BINARY` as desired, but for the record:\n\n* `uname -p` isn't portable (it may return \"`unknown`\" even on Linuces), one should use `uname -m` instead.\n\n* Rather than having (btw. incomplete)\n\n```sh\n    if [ ... -o ... -o ... -o ... ]; then ...\n```\n\n one should use\n\n```sh\n    case \"`uname -m`\" in\n      i[3456]86|i86pc)\n        ...\n        ;;\n      amd64|x86_64)\n        ...\n        ;;\n      ia64) # Itanium\n        ...\n        ;;\n      # etc.\n    esac\n```\n\n instead, which is not only more readable, but also more robust (and portable w.r.t. broken / buggy `test` commands).",
    "created_at": "2011-08-03T07:07:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89195",
    "user": "leif"
}
```

Replying to [comment:15 ddrake]:
> Replying to [comment:14 wjp]:
> > Also, #10226 (which also needs review) might supersede this patch.
> 
> It does, and I think we should work on that ticket and close this one when #10226 gets merged.

I currently don't know whether the new (*Python* install script) ATLAS spkg from #10226 supports `SAGE_FAT_BINARY` as desired, but for the record:

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

archive/issue_comments_089196.json:
```json
{
    "body": "For the record, the updated ATLAS spkg from #10226 uses the `$UNAME` environment variable (which Sage sets) if available, and python's portable `platform.system()` otherwise:\n\n\n```python\ntry:\n    conf['system'] = os.environ['UNAME']\nexcept KeyError:\n    conf['system'] = platform.system()\n```\n\nAlso there is some support for `SAGE_FAT_BINARY`:\n\n```python\n    if os.environ.get('SAGE_FAT_BINARY', 'no') == 'yes' and conf['Intel?']:\n        print 'Sage \"fat\" binary mode set: Building SSE2 only Hammer binary'\n        print 'NOTE: This can result in a Sage that is significantly slower at certain numerical'\n        print 'linear algebra since full FAT binary support has not been implemented yet.'\n        arch = 'HAMMER'\n        isa_ext = ('SSE2', 'SSE1')\n```\n\nThough I'm not sure if anybody ever verified that ATLAS, with these settings, indeed does not use any more advanced isa extensions.",
    "created_at": "2011-08-03T09:04:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89196",
    "user": "vbraun"
}
```

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

archive/issue_comments_089197.json:
```json
{
    "body": "Oops we are talking about `uname -m`. For this, I'm using `platform.machine()`:\n\n```python\nconf['Intel?'] = (platform.machine() in ('i386', 'i486', 'i586', 'i686', 'x86_64', \n                                         'AMD64', 'i86pc'))\nconf['IA64?']   = (platform.processor() == 'ia64')\nconf['PPC?']   = (platform.processor() == 'powerpc')\nconf['SPARC?'] = (platform.processor() == 'sparc')\n```\n",
    "created_at": "2011-08-03T09:07:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89197",
    "user": "vbraun"
}
```

Oops we are talking about `uname -m`. For this, I'm using `platform.machine()`:

```python
conf['Intel?'] = (platform.machine() in ('i386', 'i486', 'i586', 'i686', 'x86_64', 
                                         'AMD64', 'i86pc'))
conf['IA64?']   = (platform.processor() == 'ia64')
conf['PPC?']   = (platform.processor() == 'powerpc')
conf['SPARC?'] = (platform.processor() == 'sparc')
```




---

archive/issue_comments_089198.json:
```json
{
    "body": "Replying to [comment:17 vbraun]:\n> Though I'm not sure if anybody ever verified that ATLAS, with these settings, indeed does not use any more advanced isa extensions.\n\nRegarding that a) the notion of \"fat\" binaries is misleading (because \"fat\" originally refers to **different** code for different [flavours of] processors in the **same** binary / executable), and b) there's neither a definition nor a consistent practice of what ISA subsets Sage uses if `SAGE_FAT_BINARY=yes`, I think we can then close this ticket.\n\nIf someone complains, we can always change the behaviour of the affected spkg(s); with the exception of AFAIK very rare `SIGILL` reports for binary distributions Mariah seems to be the only one who actually regularly tests this feature.\n\nWe could of course over time collect what different spkgs do, on a wiki page, though.\n\n(For most packages and binary distributions adding `-march=...` or `-mcpu=...` to `CFLAGS` -- or configuring GCC to default to these -- should be sufficient anyway; building binary Sage distributions on less advanced processors is another way.)",
    "created_at": "2011-08-03T10:25:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89198",
    "user": "leif"
}
```

Replying to [comment:17 vbraun]:
> Though I'm not sure if anybody ever verified that ATLAS, with these settings, indeed does not use any more advanced isa extensions.

Regarding that a) the notion of "fat" binaries is misleading (because "fat" originally refers to **different** code for different [flavours of] processors in the **same** binary / executable), and b) there's neither a definition nor a consistent practice of what ISA subsets Sage uses if `SAGE_FAT_BINARY=yes`, I think we can then close this ticket.

If someone complains, we can always change the behaviour of the affected spkg(s); with the exception of AFAIK very rare `SIGILL` reports for binary distributions Mariah seems to be the only one who actually regularly tests this feature.

We could of course over time collect what different spkgs do, on a wiki page, though.

(For most packages and binary distributions adding `-march=...` or `-mcpu=...` to `CFLAGS` -- or configuring GCC to default to these -- should be sufficient anyway; building binary Sage distributions on less advanced processors is another way.)



---

archive/issue_comments_089199.json:
```json
{
    "body": "I agree and will set this ticket to positive review.\n\nSince it is hard/impossible to tell the gcc flags from the compiled binary, I think we should eventually move the `SAGE_FAT_BINARY` support into the compilerwrapper. It would be easy for the compilerwrapper to set the desired `-march` / `-mtune` flags consistently for each binary that we build. \n\nPS: `-mcpu` is a deprecated synonym for `-mtune`.\n\nRelease manager: this ticket is fixed by #10226 and can be closed.",
    "created_at": "2011-08-03T10:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89199",
    "user": "vbraun"
}
```

I agree and will set this ticket to positive review.

Since it is hard/impossible to tell the gcc flags from the compiled binary, I think we should eventually move the `SAGE_FAT_BINARY` support into the compilerwrapper. It would be easy for the compilerwrapper to set the desired `-march` / `-mtune` flags consistently for each binary that we build. 

PS: `-mcpu` is a deprecated synonym for `-mtune`.

Release manager: this ticket is fixed by #10226 and can be closed.



---

archive/issue_comments_089200.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-03T10:46:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89200",
    "user": "vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089201.json:
```json
{
    "body": "Replying to [comment:20 vbraun]:\n> PS: `-mcpu` is a deprecated synonym for `-mtune`.\n\nNope, `-mcpu` selects the instruction set, while `-mtune` only affects timing-specific choices (selection or reordering of instructions of that subset); `-march=foo` is equivalent to `-mcpu=foo -mtune=foo`. (I don't think that's changed recently, though `configure` supports `--with-arch-NN=...` and `--with-tune-NN=...`, NN in {32, 64}.)\n\n----\n\nShould we cc Jeroen and delete the ticket from the wishlist wiki page?",
    "created_at": "2011-08-03T11:45:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89201",
    "user": "leif"
}
```

Replying to [comment:20 vbraun]:
> PS: `-mcpu` is a deprecated synonym for `-mtune`.

Nope, `-mcpu` selects the instruction set, while `-mtune` only affects timing-specific choices (selection or reordering of instructions of that subset); `-march=foo` is equivalent to `-mcpu=foo -mtune=foo`. (I don't think that's changed recently, though `configure` supports `--with-arch-NN=...` and `--with-tune-NN=...`, NN in {32, 64}.)

----

Should we cc Jeroen and delete the ticket from the wishlist wiki page?



---

archive/issue_comments_089202.json:
```json
{
    "body": "Well http://gcc.gnu.org/onlinedocs/gcc-4.6.1/gcc/i386-and-x86_002d64-Options.html#i386-and-x86_002d64-Options says:\n\n```\n-mcpu=cpu-type\n    A deprecated synonym for -mtune. \n```\n\nThe instruction set is selected with `-march`. \n\nWe should remove the ticket from the wishlist. Jeroen will close this ticket when he gets around to it, no need to contact him.",
    "created_at": "2011-08-03T11:53:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89202",
    "user": "vbraun"
}
```

Well http://gcc.gnu.org/onlinedocs/gcc-4.6.1/gcc/i386-and-x86_002d64-Options.html#i386-and-x86_002d64-Options says:

```
-mcpu=cpu-type
    A deprecated synonym for -mtune. 
```

The instruction set is selected with `-march`. 

We should remove the ticket from the wishlist. Jeroen will close this ticket when he gets around to it, no need to contact him.



---

archive/issue_comments_089203.json:
```json
{
    "body": "Replying to [comment:22 vbraun]:\n>\n\n```\n-mcpu=cpu-type\n    A deprecated synonym for -mtune. \n```\n\nMaybe a long-lasting typo (at least since GCC 4.3.3, to be reported upstream ;-) ). Sections on other architectures describe the [IMHO] correct meaning. Or it has been inconsistent for x86 from the beginning, and therefore been deprecated.",
    "created_at": "2011-08-03T12:17:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89203",
    "user": "leif"
}
```

Replying to [comment:22 vbraun]:
>

```
-mcpu=cpu-type
    A deprecated synonym for -mtune. 
```

Maybe a long-lasting typo (at least since GCC 4.3.3, to be reported upstream ;-) ). Sections on other architectures describe the [IMHO] correct meaning. Or it has been inconsistent for x86 from the beginning, and therefore been deprecated.



---

archive/issue_comments_089204.json:
```json
{
    "body": "I don't see any consistency across architectures:\n\n* x86 has `-march` and `-mtune`==`-mcpu`\n* ARM has `-march` and `-mtune`==`-mcpu` (except perhaps with fewer possible values??)\n* MIPS has `-march` and `-mtune` but not `-mcpu`\n* PowerPC does not have `-march`, but supports `-mtune` and `-mcpu`\n\nThere is a ton of dead architectures, but I don't think they have any up-to-date interface.",
    "created_at": "2011-08-03T12:34:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89204",
    "user": "vbraun"
}
```

I don't see any consistency across architectures:

* x86 has `-march` and `-mtune`==`-mcpu`
* ARM has `-march` and `-mtune`==`-mcpu` (except perhaps with fewer possible values??)
* MIPS has `-march` and `-mtune` but not `-mcpu`
* PowerPC does not have `-march`, but supports `-mtune` and `-mcpu`

There is a ton of dead architectures, but I don't think they have any up-to-date interface.



---

archive/issue_comments_089205.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2011-08-03T14:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9382",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9382#issuecomment-89205",
    "user": "jdemeyer"
}
```

Resolution: duplicate
