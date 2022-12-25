# Issue 9896: pari-2.4.3.svn-12577 fails to build on itanium with gcc 4.5.1

archive/issues_009896.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @jdemeyer\n\nOn the skynet machines cleo (ia64-Linux-rhel) and iras (ia64-Linux-suse), each using gcc 4.5.1, the PARI spkg in 4.6.alpha0 fails to build:\n\n```\ngcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -I. -I../src/headers -fPIC -o mpqs.o ../src/modules/mpqs.c\n../src/modules/krasner.c: In function 'GetRamifiedPol': \n../src/modules/krasner.c:878:1: error: unrecognizable insn: \n(insn:TI 7910 7861 7937 509 (parallel [ \n            (set (reg:DI 134 f6) \n                (asm_operands:DI (\"xma.hu %0 = %2, %3, f0 \n        ;; \n        xma.l %1 = %2, %3, f0\") (\"=&f\") 0 [ \n                        (reg:DI 135 f7) \n                        (reg/v:DI 130 f2 [orig:1756 pmodg ] [1756]) \n                    ] \n                     [ \n                        (asm_input:DI (\"f\") (null):0) \n                        (asm_input:DI (\"f\") (null):0) \n                    ] \n                     [] ../src/modules/krasner.c:878)) \n            (set (reg:DI 135 f7) \n                (asm_operands:DI (\"xma.hu %0 = %2, %3, f0 \n        ;; \n        xma.l %1 = %2, %3, f0\") (\"=f\") 1 [ \n                        (reg:DI 135 f7) \n                        (reg/v:DI 130 f2 [orig:1756 pmodg ] [1756]) \n                    ] \n                     [ \n                        (asm_input:DI (\"f\") (null):0) \n                        (asm_input:DI (\"f\") (null):0) \n                    ] \n                     [] ../src/modules/krasner.c:878)) \n        ]) -1 (nil)) \n../src/modules/krasner.c:878:1: internal compiler error: in \nget_attr_first_insn, at config/ia64/itanium2.md:1909 \nPlease submit a full bug report, \nwith preprocessed source if appropriate. \nSee <http://gcc.gnu.org/bugs.html> for instructions. \nmake[3]: *** [krasner.o] Error 1\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/9897\n\n",
    "created_at": "2010-09-11T06:08:39Z",
    "labels": [
        "component: packages: standard",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "pari-2.4.3.svn-12577 fails to build on itanium with gcc 4.5.1",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9896",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: tbd

CC:  @nexttime @jdemeyer

On the skynet machines cleo (ia64-Linux-rhel) and iras (ia64-Linux-suse), each using gcc 4.5.1, the PARI spkg in 4.6.alpha0 fails to build:

```
gcc  -c -O3 -Wall -fno-strict-aliasing -fomit-frame-pointer  -O3 -g   -I. -I../src/headers -fPIC -o mpqs.o ../src/modules/mpqs.c
../src/modules/krasner.c: In function 'GetRamifiedPol': 
../src/modules/krasner.c:878:1: error: unrecognizable insn: 
(insn:TI 7910 7861 7937 509 (parallel [ 
            (set (reg:DI 134 f6) 
                (asm_operands:DI ("xma.hu %0 = %2, %3, f0 
        ;; 
        xma.l %1 = %2, %3, f0") ("=&f") 0 [ 
                        (reg:DI 135 f7) 
                        (reg/v:DI 130 f2 [orig:1756 pmodg ] [1756]) 
                    ] 
                     [ 
                        (asm_input:DI ("f") (null):0) 
                        (asm_input:DI ("f") (null):0) 
                    ] 
                     [] ../src/modules/krasner.c:878)) 
            (set (reg:DI 135 f7) 
                (asm_operands:DI ("xma.hu %0 = %2, %3, f0 
        ;; 
        xma.l %1 = %2, %3, f0") ("=f") 1 [ 
                        (reg:DI 135 f7) 
                        (reg/v:DI 130 f2 [orig:1756 pmodg ] [1756]) 
                    ] 
                     [ 
                        (asm_input:DI ("f") (null):0) 
                        (asm_input:DI ("f") (null):0) 
                    ] 
                     [] ../src/modules/krasner.c:878)) 
        ]) -1 (nil)) 
../src/modules/krasner.c:878:1: internal compiler error: in 
get_attr_first_insn, at config/ia64/itanium2.md:1909 
Please submit a full bug report, 
with preprocessed source if appropriate. 
See <http://gcc.gnu.org/bugs.html> for instructions. 
make[3]: *** [krasner.o] Error 1
```

Issue created by migration from https://trac.sagemath.org/ticket/9897





---

archive/issue_comments_098209.json:
```json
{
    "body": "This is clearly a gcc bug.",
    "created_at": "2010-09-19T08:32:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98209",
    "user": "https://github.com/jdemeyer"
}
```

This is clearly a gcc bug.



---

archive/issue_comments_098210.json:
```json
{
    "body": "With cleo's default GCC 4.1.2 20080704 (Red Hat 4.1.2-44), which I \"enabled\" by not sourcing `/usr/local/skynet_bash_profile` in `~/.bash_profile`, a standalone build succeeds but some tests fail:\n\n```\n$ tar xjf pari-2.4.3.svn-12577.p5.spkg\n$ cd pari-2.4.3.svn-12577.p5/src\n$ ./Configure --graphic=none\n$ make test-all\n[...]\n* Testing zn    for gp-sta..TIME=7      for gp-dyn..TIME=3\n+++ [BUG] Total bench for gp-sta is 496414\n+++ [BUG] Total bench for gp-dyn is 554345\n\nPROBLEMS WERE NOTED. The following files list them in diff format:\nDirectory: /home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64\n        ellglobalred-sta.dif\n        ellsea-sta.dif\n        galois-sta.dif\n        ellglobalred-dyn.dif\n        ellsea-dyn.dif\n        galois-dyn.dif\nmake[1]: *** [test-all] Error 1\nmake[1]: Leaving directory `/home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64'\nmake: *** [test-all] Error 2\n```\nI've put copies of these .dif files [here](http://sage.math.washington.edu/home/mpatel/trac/9897/).  But I get the same failures on sage.math.",
    "created_at": "2010-09-25T10:46:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98210",
    "user": "https://github.com/qed777"
}
```

With cleo's default GCC 4.1.2 20080704 (Red Hat 4.1.2-44), which I "enabled" by not sourcing `/usr/local/skynet_bash_profile` in `~/.bash_profile`, a standalone build succeeds but some tests fail:

```
$ tar xjf pari-2.4.3.svn-12577.p5.spkg
$ cd pari-2.4.3.svn-12577.p5/src
$ ./Configure --graphic=none
$ make test-all
[...]
* Testing zn    for gp-sta..TIME=7      for gp-dyn..TIME=3
+++ [BUG] Total bench for gp-sta is 496414
+++ [BUG] Total bench for gp-dyn is 554345

PROBLEMS WERE NOTED. The following files list them in diff format:
Directory: /home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64
        ellglobalred-sta.dif
        ellsea-sta.dif
        galois-sta.dif
        ellglobalred-dyn.dif
        ellsea-dyn.dif
        galois-dyn.dif
make[1]: *** [test-all] Error 1
make[1]: Leaving directory `/home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64'
make: *** [test-all] Error 2
```
I've put copies of these .dif files [here](http://sage.math.washington.edu/home/mpatel/trac/9897/).  But I get the same failures on sage.math.



---

archive/issue_comments_098211.json:
```json
{
    "body": "Replying to [comment:3 mpatel]:\n> With cleo's default GCC 4.1.2 20080704 (Red Hat 4.1.2-44), which I \"enabled\" by not sourcing `/usr/local/skynet_bash_profile` in `~/.bash_profile`, a standalone build succeeds but some tests fail:\n> \n\n{{{\n...\nPROBLEMS WERE NOTED. The following files list them in diff format:\nDirectory: /home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64\n        ellglobalred-sta.dif\n        ellsea-sta.dif\n        galois-sta.dif\n        ellglobalred-dyn.dif\n        ellsea-dyn.dif\n        galois-dyn.dif\n...\n}}}\n> I've put copies of these .dif files [here](http://sage.math.washington.edu/home/mpatel/trac/9897/).  But I get the same failures on sage.math.\n\n\nThese 2*3 tests *must* fail, because they depend on data files which aren't (yet) present / installed at that point. (We don't ship the ellglobalred data at all since it's 14 MB, and therefore patch `config/get_tests`.)",
    "created_at": "2010-09-25T13:09:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98211",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:3 mpatel]:
> With cleo's default GCC 4.1.2 20080704 (Red Hat 4.1.2-44), which I "enabled" by not sourcing `/usr/local/skynet_bash_profile` in `~/.bash_profile`, a standalone build succeeds but some tests fail:
> 

{{{
...
PROBLEMS WERE NOTED. The following files list them in diff format:
Directory: /home/mpatel/cleo/pari-2.4.3.svn-12577.p5/src/Olinux-ia64
        ellglobalred-sta.dif
        ellsea-sta.dif
        galois-sta.dif
        ellglobalred-dyn.dif
        ellsea-dyn.dif
        galois-dyn.dif
...
}}}
> I've put copies of these .dif files [here](http://sage.math.washington.edu/home/mpatel/trac/9897/).  But I get the same failures on sage.math.


These 2*3 tests *must* fail, because they depend on data files which aren't (yet) present / installed at that point. (We don't ship the ellglobalred data at all since it's 14 MB, and therefore patch `config/get_tests`.)



---

archive/issue_comments_098212.json:
```json
{
    "body": "(You could temporarily patch `src/config/get_tests` with `patches/get_tests.patch`, run `src/Configure` with also e.g. `--prefix=/tmp/pari` and `make install-data` before running `make test-all`. I'm not sure if you also have to `make gp` and `make install` before running `make install-data`.)",
    "created_at": "2010-09-25T13:32:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98212",
    "user": "https://github.com/nexttime"
}
```

(You could temporarily patch `src/config/get_tests` with `patches/get_tests.patch`, run `src/Configure` with also e.g. `--prefix=/tmp/pari` and `make install-data` before running `make test-all`. I'm not sure if you also have to `make gp` and `make install` before running `make install-data`.)



---

archive/issue_comments_098213.json:
```json
{
    "body": "Replying to [comment:5 leif]:\n> I'm not sure if you also have to `make gp` and `make install` before running `make install-data`.\n\n\nYou don't need to do that, i.e you can simply run `make install-data && make test-all` after copying `patches/files/get_tests` to `src/config` and configuring with some temporary installation directory.",
    "created_at": "2010-09-25T13:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98213",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:5 leif]:
> I'm not sure if you also have to `make gp` and `make install` before running `make install-data`.


You don't need to do that, i.e you can simply run `make install-data && make test-all` after copying `patches/files/get_tests` to `src/config` and configuring with some temporary installation directory.



---

archive/issue_comments_098214.json:
```json
{
    "body": "Are there any plans to report this upstream to gcc?",
    "created_at": "2010-10-02T08:26:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98214",
    "user": "https://github.com/jdemeyer"
}
```

Are there any plans to report this upstream to gcc?



---

archive/issue_comments_098215.json:
```json
{
    "body": "The problem above seems very similar to [this one](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31684).",
    "created_at": "2010-10-02T08:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98215",
    "user": "https://github.com/qed777"
}
```

The problem above seems very similar to [this one](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31684).



---

archive/issue_comments_098216.json:
```json
{
    "body": "Replying to [comment:8 mpatel]:\n> The problem above seems very similar to [this one](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31684).\n\nExcept that was marked as \"RESOLVED FIXED\" back in January 2008. Another bug report should be created. The gcc developers require the preprocessed file - see http://gcc.gnu.org/bugs/\n\nAs another matter, it would be good if the Pari developers could add a test target that tests everything except those parts of Pari needing the extra databases, which are not part of the main Pari distribution. Someone here probably knows the best person to ask. That is not a bug as such, but a request for an enhancement. If that was done, it would remove the need for a patch in Sage. \n\nDave",
    "created_at": "2010-10-02T10:30:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98216",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:8 mpatel]:
> The problem above seems very similar to [this one](http://gcc.gnu.org/bugzilla/show_bug.cgi?id=31684).

Except that was marked as "RESOLVED FIXED" back in January 2008. Another bug report should be created. The gcc developers require the preprocessed file - see http://gcc.gnu.org/bugs/

As another matter, it would be good if the Pari developers could add a test target that tests everything except those parts of Pari needing the extra databases, which are not part of the main Pari distribution. Someone here probably knows the best person to ask. That is not a bug as such, but a request for an enhancement. If that was done, it would remove the need for a patch in Sage. 

Dave



---

archive/issue_comments_098217.json:
```json
{
    "body": "Replying to [comment:9 drkirkby]:\n> As another matter, it would be good if the Pari developers could add a test target that tests everything except those parts of Pari needing the extra databases, which are not part of the main Pari distribution. Someone here probably knows the best person to ask. That is not a bug as such, but a request for an enhancement. If that was done, it would remove the need for a patch in Sage. \n\n\nI have posed the question at [http://pari.math.u-bordeaux.fr/archives/pari-dev-1010/msg00000.html](http://pari.math.u-bordeaux.fr/archives/pari-dev-1010/msg00000.html)",
    "created_at": "2010-10-02T17:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98217",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:9 drkirkby]:
> As another matter, it would be good if the Pari developers could add a test target that tests everything except those parts of Pari needing the extra databases, which are not part of the main Pari distribution. Someone here probably knows the best person to ask. That is not a bug as such, but a request for an enhancement. If that was done, it would remove the need for a patch in Sage. 


I have posed the question at [http://pari.math.u-bordeaux.fr/archives/pari-dev-1010/msg00000.html](http://pari.math.u-bordeaux.fr/archives/pari-dev-1010/msg00000.html)



---

archive/issue_comments_098218.json:
```json
{
    "body": "Sage 4.6.alpha3 [compiles on cleo with the default compiler](http://build.sagemath.org/sage/builders/cleo%20full/builds/11) (gcc version 4.1.2 20080704 (Red Hat 4.1.2-44) and passes the tests (except for known blockers).\n\nWith the default on iras (gcc version 4.1.2 20070115 (prerelease) (SUSE Linux)), I had problems installing Python (see #10082), IPython, PolyBoRi, and R.  I don't know which of these, if any, stems from the build configuration.",
    "created_at": "2010-10-09T05:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98218",
    "user": "https://github.com/qed777"
}
```

Sage 4.6.alpha3 [compiles on cleo with the default compiler](http://build.sagemath.org/sage/builders/cleo%20full/builds/11) (gcc version 4.1.2 20080704 (Red Hat 4.1.2-44) and passes the tests (except for known blockers).

With the default on iras (gcc version 4.1.2 20070115 (prerelease) (SUSE Linux)), I had problems installing Python (see #10082), IPython, PolyBoRi, and R.  I don't know which of these, if any, stems from the build configuration.



---

archive/issue_comments_098219.json:
```json
{
    "body": "Changing priority from blocker to critical.",
    "created_at": "2010-10-09T05:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98219",
    "user": "https://github.com/qed777"
}
```

Changing priority from blocker to critical.



---

archive/issue_comments_098220.json:
```json
{
    "body": "Can we isolate a possible test case from `krasner.c`?",
    "created_at": "2010-10-09T05:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98220",
    "user": "https://github.com/qed777"
}
```

Can we isolate a possible test case from `krasner.c`?



---

archive/issue_comments_098221.json:
```json
{
    "body": "Replying to [comment:13 mpatel]:\n> Can we isolate a possible test case from `krasner.c`?\n\n\nI'm willing to have a look at it if somebody can arrange access for me to a machine with this problem.",
    "created_at": "2010-10-09T07:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98221",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:13 mpatel]:
> Can we isolate a possible test case from `krasner.c`?


I'm willing to have a look at it if somebody can arrange access for me to a machine with this problem.



---

archive/issue_comments_098222.json:
```json
{
    "body": "Replying to [comment:14 jdemeyer]:\n> Replying to [comment:13 mpatel]:\n> > Can we isolate a possible test case from `krasner.c`?\n\n> \n> I'm willing to have a look at it if somebody can arrange access for me to a machine with this problem.\n\n\nI'm not sure about whether William is in charge of the Skynet cluster, but he can ask the Skynet administrator Mariah Lenox to give you an account.",
    "created_at": "2010-10-09T07:56:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98222",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:14 jdemeyer]:
> Replying to [comment:13 mpatel]:
> > Can we isolate a possible test case from `krasner.c`?

> 
> I'm willing to have a look at it if somebody can arrange access for me to a machine with this problem.


I'm not sure about whether William is in charge of the Skynet cluster, but he can ask the Skynet administrator Mariah Lenox to give you an account.



---

archive/issue_comments_098223.json:
```json
{
    "body": "Confirmed, even with vanilla PARI 2.4.3.\nCompiling with -O2 instead of -O3 works.",
    "created_at": "2010-10-15T08:51:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98223",
    "user": "https://github.com/jdemeyer"
}
```

Confirmed, even with vanilla PARI 2.4.3.
Compiling with -O2 instead of -O3 works.



---

archive/issue_comments_098224.json:
```json
{
    "body": "Could it be related to this: http://gcc.gnu.org/bugzilla/show_bug.cgi?id=43603",
    "created_at": "2010-10-15T09:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98224",
    "user": "https://github.com/jdemeyer"
}
```

Could it be related to this: http://gcc.gnu.org/bugzilla/show_bug.cgi?id=43603



---

archive/issue_comments_098225.json:
```json
{
    "body": "Minimal testcase exhibiting the bug",
    "created_at": "2010-10-16T12:38:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98225",
    "user": "https://github.com/jdemeyer"
}
```

Minimal testcase exhibiting the bug



---

archive/issue_comments_098226.json:
```json
{
    "body": "Attachment [krasner.i](tarball://root/attachments/some-uuid/ticket9897/krasner.i) by @qed777 created at 2010-10-16 22:50:38\n\nCool.  Thanks!",
    "created_at": "2010-10-16T22:50:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98226",
    "user": "https://github.com/qed777"
}
```

Attachment [krasner.i](tarball://root/attachments/some-uuid/ticket9897/krasner.i) by @qed777 created at 2010-10-16 22:50:38

Cool.  Thanks!



---

archive/issue_comments_098227.json:
```json
{
    "body": "Replying to [comment:16 jdemeyer]:\n> Confirmed, even with vanilla PARI 2.4.3.\n> Compiling with -O2 instead of -O3 works.\n\n\nI've successfully built 4.6.alpha3 on cleo and iras with `SAGE_DEBUG=yes`, which turns off `-O3` for at least PARI.",
    "created_at": "2010-10-17T05:50:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98227",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:16 jdemeyer]:
> Confirmed, even with vanilla PARI 2.4.3.
> Compiling with -O2 instead of -O3 works.


I've successfully built 4.6.alpha3 on cleo and iras with `SAGE_DEBUG=yes`, which turns off `-O3` for at least PARI.



---

archive/issue_comments_098228.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2010-12-10T14:15:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98228",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate



---

archive/issue_events_024933.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-10T14:15:12Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9896#event-24933"
}
```



---

archive/issue_events_024934.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-12-10T14:15:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9896#event-24934"
}
```



---

archive/issue_comments_098229.json:
```json
{
    "body": "Isn't that overkill to use (and wait for) #10572 rather than adding three lines in spkg-install to pass -O2 on ia64 and some GCC versions?\nI just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.\n(This just made me think the problem on Cygwin with ECL and GCC 4.6.3 (but not 4.7.2) reported at http://gcc.gnu.org/bugzilla/show_bug.cgi?id=52061 which I encountered as well could be dealt with by just dropping the optimizaiton level.)",
    "created_at": "2013-03-01T10:09:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98229",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Isn't that overkill to use (and wait for) #10572 rather than adding three lines in spkg-install to pass -O2 on ia64 and some GCC versions?
I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.
(This just made me think the problem on Cygwin with ECL and GCC 4.6.3 (but not 4.7.2) reported at http://gcc.gnu.org/bugzilla/show_bug.cgi?id=52061 which I encountered as well could be dealt with by just dropping the optimizaiton level.)



---

archive/issue_comments_098230.json:
```json
{
    "body": "Replying to [comment:23 jpflori]:\n> I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.\n\nAre you really sure it's the same bug? What happens when you compile [attachment:krasner.i] with `-O3`?\n\nI would prefer to fix the `spkg/install` script which detects GCC versions and decides whether or not to build GCC.",
    "created_at": "2013-03-06T12:34:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98230",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:23 jpflori]:
> I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.

Are you really sure it's the same bug? What happens when you compile [attachment:krasner.i] with `-O3`?

I would prefer to fix the `spkg/install` script which detects GCC versions and decides whether or not to build GCC.



---

archive/issue_comments_098231.json:
```json
{
    "body": "Replying to [comment:24 jdemeyer]:\n> Replying to [comment:23 jpflori]:\n> > I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.\n\n> Are you really sure it's the same bug? What happens when you compile [attachment:krasner.i] with `-O3`?\nIt happens when compiling krasner.c so I think its the same bug, see http://trac.sagemath.org/sage_trac/ticket/10508#comment:319.\n> \n> I would prefer to fix the `spkg/install` script which detects GCC versions and decides whether or not to build GCC.",
    "created_at": "2013-03-14T17:00:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98231",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Replying to [comment:24 jdemeyer]:
> Replying to [comment:23 jpflori]:
> > I just encountered the same bug two years later with the default GCC 4.4.5 installed there and that Sage accepted.

> Are you really sure it's the same bug? What happens when you compile [attachment:krasner.i] with `-O3`?
It happens when compiling krasner.c so I think its the same bug, see http://trac.sagemath.org/sage_trac/ticket/10508#comment:319.
> 
> I would prefer to fix the `spkg/install` script which detects GCC versions and decides whether or not to build GCC.



---

archive/issue_comments_098232.json:
```json
{
    "body": "See #14378.",
    "created_at": "2013-03-29T04:07:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9896",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9896#issuecomment-98232",
    "user": "https://github.com/jdemeyer"
}
```

See #14378.
