# Issue 157: Integers(2**31)(5) hangs on 32-bit  (fine on 64-bit, but something else is probably broken there)

archive/issues_000157.json:
```json
{
    "body": "Assignee: @robertwb\n\n\n```\nHi William,\n \nSAGE is great!  Long live SAGE!  Now a bug report \n \nIntegers(2**31)(5) hangs on my Linux box.\n \nBug information: Integers(2**30)(5) works, Integers(2**31-1)(5) works, but\nthere's an ugly range after 2**31.  The offending code is in\ninteger_mod.pyx, but I can't debug it much further.  Here's a gdb\nbacktrace, which looks a little sparse:\n \nbash-2.05b$ ./sage -gdb\n--------------------------------------------------------\n--------------------------------------------------------\n \n/grad/sone/ncalexan/software/sage-1.4/local/bin/sage-gdb-pythonstartup\nGNU gdb Red Hat Linux (6.0post-0.20040223.19rh)\nCopyright 2004 Free Software Foundation, Inc.\nGDB is free software, covered by the GNU General Public License, and you are\nwelcome to change it and/or distribute copies of it under certain conditions.\nType \"show copying\" to see the conditions.\nThere is absolutely no warranty for GDB.  Type \"show warranty\" for details.\nThis GDB was configured as \"i386-redhat-linux-gnu\"...Using host\nlibthread_db library \"/lib/tls/libthread_db.so.1\".\n \n[Thread debugging using libthread_db enabled]\n[New Thread -1208072704 (LWP 7971)]\nPython 2.5 (r25:51908, Oct 16 2006, 11:48:58)\n[GCC 3.3.3 20040412 (Red Hat Linux 3.3.3-7)] on linux2\nType \"help\", \"copyright\", \"credits\" or \"license\" for more information.\nDetaching after fork from child process 7996.\n \nsage: Integers(2**31)(5)\n \nProgram received signal SIGFPE, Arithmetic exception.\n[Switching to Thread -1208072704 (LWP 7971)]\n0x0038ff14 in __gmp_exception ()\n   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3\n(gdb) bt\n#0  0x0038ff14 in __gmp_exception ()\n   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3\n#1  0xb7faf46c in ?? ()\n#2  0xb2ca95ac in ?? ()\n#3  0x003ba2e0 in ?? ()\n   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3\n#4  0x0038ff5f in __gmp_divide_by_zero ()\n   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3\n#5  0x00000002 in ?? ()\n#6  0xb2ca95ac in ?? ()\n#7  0x003ba2e0 in ?? ()\n   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3\n#8  0x0039b2bd in __gmpz_fdiv_ui ()\n   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3\n#9  0xb7faf46c in ?? ()\n#10 0xb2ca95ac in ?? ()\n#11 0x00000000 in ?? ()\n \nMachine information:\n \nIt hangs under my Linux box:\n \n$ uname -a\nLinux tumor 2.6.10-1.9_FC2 #1 Thu Jan 13 17:54:57 EST 2005 i686 i686 i386\nGNU/Linux\n \nBut works fine on the SAGE notebook hosted at modular and works fine on\nSAGE 1.3.7 on my Mac OS X G4 Powerbook.\n \nSage information:  Fails under two versions, both built from source:\n \nbash-2.05b$ ./sage\n--------------------------------------------------------\n--------------------------------------------------------\n \nand\n \nbash-2.05b$ ./sage\n--------------------------------------------------------\n--------------------------------------------------------\n \nThanks for the great work on SAGE, it is now my CAS of choice.\nNick Alexander\n \nPS.  A question: how does @func_persist work, meaning where does it get\ntranslated and into what code.  Is this mechanism general and used\nelsewhere?\n }}}\n\nIssue created by migration from https://trac.sagemath.org/ticket/157\n\n",
    "created_at": "2006-10-27T20:40:07Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "Integers(2**31)(5) hangs on 32-bit  (fine on 64-bit, but something else is probably broken there)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/157",
    "user": "@williamstein"
}
```
Assignee: @robertwb


```
Hi William,
 
SAGE is great!  Long live SAGE!  Now a bug report 
 
Integers(2**31)(5) hangs on my Linux box.
 
Bug information: Integers(2**30)(5) works, Integers(2**31-1)(5) works, but
there's an ugly range after 2**31.  The offending code is in
integer_mod.pyx, but I can't debug it much further.  Here's a gdb
backtrace, which looks a little sparse:
 
bash-2.05b$ ./sage -gdb
--------------------------------------------------------
--------------------------------------------------------
 
/grad/sone/ncalexan/software/sage-1.4/local/bin/sage-gdb-pythonstartup
GNU gdb Red Hat Linux (6.0post-0.20040223.19rh)
Copyright 2004 Free Software Foundation, Inc.
GDB is free software, covered by the GNU General Public License, and you are
welcome to change it and/or distribute copies of it under certain conditions.
Type "show copying" to see the conditions.
There is absolutely no warranty for GDB.  Type "show warranty" for details.
This GDB was configured as "i386-redhat-linux-gnu"...Using host
libthread_db library "/lib/tls/libthread_db.so.1".
 
[Thread debugging using libthread_db enabled]
[New Thread -1208072704 (LWP 7971)]
Python 2.5 (r25:51908, Oct 16 2006, 11:48:58)
[GCC 3.3.3 20040412 (Red Hat Linux 3.3.3-7)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
Detaching after fork from child process 7996.
 
sage: Integers(2**31)(5)
 
Program received signal SIGFPE, Arithmetic exception.
[Switching to Thread -1208072704 (LWP 7971)]
0x0038ff14 in __gmp_exception ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
(gdb) bt
#0  0x0038ff14 in __gmp_exception ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#1  0xb7faf46c in ?? ()
#2  0xb2ca95ac in ?? ()
#3  0x003ba2e0 in ?? ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#4  0x0038ff5f in __gmp_divide_by_zero ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#5  0x00000002 in ?? ()
#6  0xb2ca95ac in ?? ()
#7  0x003ba2e0 in ?? ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#8  0x0039b2bd in __gmpz_fdiv_ui ()
   from /grad/sone/ncalexan/software/sage-1.4/local/lib/libgmp.so.3
#9  0xb7faf46c in ?? ()
#10 0xb2ca95ac in ?? ()
#11 0x00000000 in ?? ()
 
Machine information:
 
It hangs under my Linux box:
 
$ uname -a
Linux tumor 2.6.10-1.9_FC2 #1 Thu Jan 13 17:54:57 EST 2005 i686 i686 i386
GNU/Linux
 
But works fine on the SAGE notebook hosted at modular and works fine on
SAGE 1.3.7 on my Mac OS X G4 Powerbook.
 
Sage information:  Fails under two versions, both built from source:
 
bash-2.05b$ ./sage
--------------------------------------------------------
--------------------------------------------------------
 
and
 
bash-2.05b$ ./sage
--------------------------------------------------------
--------------------------------------------------------
 
Thanks for the great work on SAGE, it is now my CAS of choice.
Nick Alexander
 
PS.  A question: how does @func_persist work, meaning where does it get
translated and into what code.  Is this mechanism general and used
elsewhere?
 }}}

Issue created by migration from https://trac.sagemath.org/ticket/157





---

archive/issue_comments_000706.json:
```json
{
    "body": "Attachment [modint64-bound.diff](tarball://root/attachments/some-uuid/ticket157/modint64-bound.diff) by @robertwb created at 2006-10-27 20:52:18\n\nLower bound on 64-bit integer_mod and (now working) example in doctest",
    "created_at": "2006-10-27T20:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/157#issuecomment-706",
    "user": "@robertwb"
}
```

Attachment [modint64-bound.diff](tarball://root/attachments/some-uuid/ticket157/modint64-bound.diff) by @robertwb created at 2006-10-27 20:52:18

Lower bound on 64-bit integer_mod and (now working) example in doctest



---

archive/issue_comments_000707.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-27T20:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/157#issuecomment-707",
    "user": "@robertwb"
}
```

Resolution: fixed



---

archive/issue_comments_000708.json:
```json
{
    "body": "GMP doesn't have mpz_t --> long long functions, so it can only deal with the first 32 bits of the integer on 32 bit platforms. At most I need the 33rd bit, so this patch lowers the bound to use gmp in these cases.\n\nThe lower bound (2^31-1) is only a factor of sqrt(2) lower than the highest possible bound (sqrt(2^63-1)) for this class, so this does not affect efficency a very large of a range.\n\nThe crash was a div by zero error--gmp was trying to compute 5 mod 0.",
    "created_at": "2006-10-27T20:56:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/157",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/157#issuecomment-708",
    "user": "@robertwb"
}
```

GMP doesn't have mpz_t --> long long functions, so it can only deal with the first 32 bits of the integer on 32 bit platforms. At most I need the 33rd bit, so this patch lowers the bound to use gmp in these cases.

The lower bound (2^31-1) is only a factor of sqrt(2) lower than the highest possible bound (sqrt(2^63-1)) for this class, so this does not affect efficency a very large of a range.

The crash was a div by zero error--gmp was trying to compute 5 mod 0.
