# Issue 4090: polybori-0.5rc1.p4 fails to build on OSX 10.4

Issue created by migration from https://trac.sagemath.org/ticket/4090

Original creator: mabshoff

Original creation time: 2008-09-09 18:39:40

Assignee: mabshoff

CC:  polybori

Georg S. Weber reported that polybori-0.5.rc1.p4 fails to build with

```
/usr/bin/libtool: unknown option character `d' in: -dylib_install_name 
Usage: /usr/bin/libtool -static [-] file [...] [-filelist 
listfile[,dirname]] [-arch_only arch] [-sacLT] 
Usage: /usr/bin/libtool -dynamic [-] file [...] [-filelist 
listfile[,dirname]] [-arch_only arch] [-o output] [-install_name name] 
[-compatibility_version #] [-current_version #] [-seg1addr 0x#] [- 
segs_read_only_addr 0x#] [-segs_read_write_addr 0x#] [-seg_addr_table 
<filename>] [-seg_addr_table_filename <file_system_path>] [-all_load] 
[-noall_load] 
scons: *** [polybori/libpolybori-0.5.0.dylib.0.0.0] Error 1 
scons: building terminated because of errors. 
Error building PolyBoRi. 
```



---

Comment by GeorgSWeber created at 2008-09-09 21:27:38

I could create a polybori-0.5rc.p5.spkg that builds on an Intel PowerBook with OS X 10.4 / Xcode 2.4.1, after noticing that the build error is related to enhance dynamic libs with version information.
But all dynamic libs are eliminated for Sage 3.1.2 anyway, so we don't have to care.

Unfortunately, I have no acquaintance with neither hg nor patch and friends.

Fortunately, all one has to do is uncomment two lines around line # 432 in the file

.../spkg/standard/polybori-0.5rc.p5/patches/SConstruct

which read originally:

#if env['PLATFORM']=="darwin":
#    slib=env.LoadableModule


and which I patched to give the four lines:

#uncommented for OS X 10.4 / Xcode 2.4.1
if env['PLATFORM']=="darwin":
    slib=env.LoadableModule
#end of modification for OS X 10.4 / Xcode 2.4.1


(The build of the Sage core didn't finish yet, but I have to sleep now.)


---

Comment by GeorgSWeber created at 2008-09-09 21:30:16

Oops.
Strange formatting, I see why you need patch files and the like.
Just do a search for "slib" in that file, it is then obvious which two consecutive lines to uncomment.


---

Comment by mabshoff created at 2008-09-10 02:56:51

The fix suggested by Georg works on OSX 10.4, but I will test it some more on other platforms. spkg coming up.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-10 03:08:37

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-09-10 03:08:37

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.1.2/rc2/polybori-0.5rc.p5.spkg

implements the fix Georg suggested and adds a bunch of explanation why we are disabling the option.

Builds fine on OSX 10.4 and 10.5.

Cheers,

Michael


---

Comment by rlm created at 2008-09-10 03:11:44

> Builds fine on OSX 10.4 and 10.5.
> 
> Cheers,
> 
> Michael

I am trusting mabshoff on this-- the package looks good.


---

Comment by mabshoff created at 2008-09-10 03:12:22

Resolution: fixed


---

Comment by mabshoff created at 2008-09-10 03:12:22

Merged in Sage 3.1.2.rc2
