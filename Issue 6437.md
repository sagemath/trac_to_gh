# Issue 6437: polybori assumes the linker is the GNU one, so breaks if Sun linker is used.

Issue created by migration from https://trac.sagemath.org/ticket/6437

Original creator: drkirkby

Original creation time: 2009-06-28 03:07:24

Assignee: tbd

polybori-0.5rc.p7/patches/

DefaultBuild = Default
if distribute or rpm_generation or deb_generation:
    def DefaultBuild(arg):
        return arg

defaultenv = Environment()

def sonameprefix(env):
    if env['PLATFORM']=="darwin":
        return "-Wl,-dylib_install_name -Wl,"
    else:
        return '-Wl,-soname,'


It needs modifying if the OS is Solaris and the linker is not GNU, but I don't know how to do it. 





---

Comment by drkirkby created at 2009-06-28 23:10:44

Changing component from algebra to solaris.


---

Comment by drkirkby created at 2009-06-28 23:10:44

Changing status from new to assigned.


---

Comment by drkirkby created at 2009-06-28 23:10:44

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-06-28 23:10:44

I've now got this fixed, thanks in no small part to the help of Arnaud Bergeron, as my python skills are next to useless. 


The patch is here. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/

Since the SConstruct file has been patched many times, I also created a diff from the last version (p7).

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/SConstruct-diff-from-p7.patch

since a patch from the original source is very large. 


I will have gcc 4.4.0 using the Sun linker and assembler on t2 very soon. so perhaps someone can review it.


---

Comment by drkirkby created at 2009-06-28 23:10:44

Changing keywords from "" to "solaris GNUism sun linker".


---

Comment by drkirkby created at 2009-06-28 23:13:38

FWIW, the actual code which decided on what flags to use is below. 

```
def sonameprefix(env):
    print ("Checking for the operating system and linker, to find appropiate flags for the linker.")
    if env['PLATFORM']=="darwin":
        return "-Wl,-dylib_install_name -Wl,"
    elif env['PLATFORM']=="sunos":
        # if GNU in os.system('ld --version 2>&1 /dev/null '):
        if os.system('ld --version > /dev/null 2>&1 ') == 0  :
           print ("You are using the GNU linker on Solaris. Linker flag set to -soname")
           print ("Genererally, the Sun linker is recked to be better on Solaris")
           print ("but Sage has been built using the GNU linker")
           return '-Wl,-soname'  # GNU linker on Solaris
        else:
           print ("You are using the Sun linker on Solaris. Linker flag set to -h")
           return '-Wl,-h'       # Sun linker on Solaris
    else:
        return '-Wl,-soname,'    # Everything else, including linux

```



---

Comment by mvngu created at 2009-07-14 07:57:16

Ticket #2999 is related to this.


---

Comment by PolyBoRi created at 2009-07-14 08:29:48

Thanks to mvngu for pointing us here. The patch will be included in the next release of PolyBoRi.
Best regards,
  Alexander


---

Comment by mvngu created at 2009-07-15 16:06:48

Replying to [comment:1 drkirkby]:
> I've now got this fixed, thanks in no small part to the help of Arnaud Bergeron, as my python skills are next to useless. 
> 
> 
> The patch is here. 
> 
> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/
> 
> Since the SConstruct file has been patched many times, I also created a diff from the last version (p7).
> 
> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/SConstruct-diff-from-p7.patch
> 
> since a patch from the original source is very large. 
After uncompressing polybori-0.5rc.p9.spkg, I see a junk file:

```
[mvngu@sage polybori-0.5rc.p9]$ hg st
M SPKG.txt
M patches/SConstruct
M patches/custom.py
? patches/SConstruct.p7
```

namely `patches/SConstruct.p7`. If you've patched the relevant scripts/build files, can you please remove the junk files? Afterwards, if you're not comfortable with checking in changes using Mercurial, I can deal with that.


---

Comment by mvngu created at 2009-07-15 19:11:24

Updated spkg at

http://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg

I've removed the junk file and checked in all changes in the name of David Kirkby. I've also fixed a minor typo. I have restarted building Sage 4.1 from scratch on t2 with the following updated spkg's:

 1. `pari-2.3.3.p1.spkg` #6445 
 1. `ntl-5.4.2.p9.spkg` #6380
 1. `zn_poly-0.9.p1.spkg` #6443
 1. `polybori-0.5rc.p9.spkg` this ticket


---

Comment by mvngu created at 2009-07-24 00:36:15

David: I'm not sure how to deal with this one, since ticket #6528 contains the latest updated PolyBori SPKG. If the SPKG at #6528 also contains the fixes mentioned on this ticket, then this ticket can be closed as a duplicate of #6528. If not, then we shouldn't have two PolyBori SPKG's with the same name but patched differently.


---

Comment by mvngu created at 2009-07-24 00:53:39

Resolution: duplicate


---

Comment by mvngu created at 2009-07-24 00:53:39

OK, I see that the SPKG at #6528 also fixes the linker issue reported on this ticket. So I'm closing this ticket as a duplicate of #6528. Please correct me if I'm wrong.
