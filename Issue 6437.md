# Issue 6437: polybori assumes the linker is the GNU one, so breaks if Sun linker is used.

archive/issues_006437.json:
```json
{
    "body": "Assignee: tbd\n\npolybori-0.5rc.p7/patches/\n\nDefaultBuild = Default\nif distribute or rpm_generation or deb_generation:\n    def DefaultBuild(arg):\n        return arg\n\ndefaultenv = Environment()\n\ndef sonameprefix(env):\n    if env['PLATFORM']==\"darwin\":\n        return \"-Wl,-dylib_install_name -Wl,\"\n    else:\n        return '-Wl,-soname,'\n\n\nIt needs modifying if the OS is Solaris and the linker is not GNU, but I don't know how to do it. \n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6437\n\n",
    "created_at": "2009-06-28T03:07:24Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "polybori assumes the linker is the GNU one, so breaks if Sun linker is used.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6437",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
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




Issue created by migration from https://trac.sagemath.org/ticket/6437





---

archive/issue_comments_051571.json:
```json
{
    "body": "Changing component from algebra to solaris.",
    "created_at": "2009-06-28T23:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51571",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to solaris.



---

archive/issue_comments_051572.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-06-28T23:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51572",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to assigned.



---

archive/issue_comments_051573.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-06-28T23:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51573",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_051574.json:
```json
{
    "body": "I've now got this fixed, thanks in no small part to the help of Arnaud Bergeron, as my python skills are next to useless. \n\n\nThe patch is here. \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/\n\nSince the SConstruct file has been patched many times, I also created a diff from the last version (p7).\n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/SConstruct-diff-from-p7.patch\n\nsince a patch from the original source is very large. \n\n\nI will have gcc 4.4.0 using the Sun linker and assembler on t2 very soon. so perhaps someone can review it.",
    "created_at": "2009-06-28T23:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51574",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I've now got this fixed, thanks in no small part to the help of Arnaud Bergeron, as my python skills are next to useless. 


The patch is here. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/

Since the SConstruct file has been patched many times, I also created a diff from the last version (p7).

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/SConstruct-diff-from-p7.patch

since a patch from the original source is very large. 


I will have gcc 4.4.0 using the Sun linker and assembler on t2 very soon. so perhaps someone can review it.



---

archive/issue_comments_051575.json:
```json
{
    "body": "Changing keywords from \"\" to \"solaris GNUism sun linker\".",
    "created_at": "2009-06-28T23:10:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51575",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing keywords from "" to "solaris GNUism sun linker".



---

archive/issue_comments_051576.json:
```json
{
    "body": "FWIW, the actual code which decided on what flags to use is below. \n\n```\ndef sonameprefix(env):\n    print (\"Checking for the operating system and linker, to find appropiate flags for the linker.\")\n    if env['PLATFORM']==\"darwin\":\n        return \"-Wl,-dylib_install_name -Wl,\"\n    elif env['PLATFORM']==\"sunos\":\n        # if GNU in os.system('ld --version 2>&1 /dev/null '):\n        if os.system('ld --version > /dev/null 2>&1 ') == 0  :\n           print (\"You are using the GNU linker on Solaris. Linker flag set to -soname\")\n           print (\"Genererally, the Sun linker is recked to be better on Solaris\")\n           print (\"but Sage has been built using the GNU linker\")\n           return '-Wl,-soname'  # GNU linker on Solaris\n        else:\n           print (\"You are using the Sun linker on Solaris. Linker flag set to -h\")\n           return '-Wl,-h'       # Sun linker on Solaris\n    else:\n        return '-Wl,-soname,'    # Everything else, including linux\n\n```\n",
    "created_at": "2009-06-28T23:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51576",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

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

archive/issue_comments_051577.json:
```json
{
    "body": "Ticket #2999 is related to this.",
    "created_at": "2009-07-14T07:57:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51577",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Ticket #2999 is related to this.



---

archive/issue_comments_051578.json:
```json
{
    "body": "Thanks to mvngu for pointing us here. The patch will be included in the next release of PolyBoRi.\nBest regards,\n  Alexander",
    "created_at": "2009-07-14T08:29:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51578",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
}
```

Thanks to mvngu for pointing us here. The patch will be included in the next release of PolyBoRi.
Best regards,
  Alexander



---

archive/issue_comments_051579.json:
```json
{
    "body": "Replying to [comment:1 drkirkby]:\n> I've now got this fixed, thanks in no small part to the help of Arnaud Bergeron, as my python skills are next to useless. \n> \n> \n> The patch is here. \n> \n> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/\n> \n> Since the SConstruct file has been patched many times, I also created a diff from the last version (p7).\n> \n> http://sage.math.washington.edu/home/kirkby/Solaris-fixes/polybori/SConstruct-diff-from-p7.patch\n> \n> since a patch from the original source is very large. \nAfter uncompressing polybori-0.5rc.p9.spkg, I see a junk file:\n\n```\n[mvngu@sage polybori-0.5rc.p9]$ hg st\nM SPKG.txt\nM patches/SConstruct\nM patches/custom.py\n? patches/SConstruct.p7\n```\n\nnamely `patches/SConstruct.p7`. If you've patched the relevant scripts/build files, can you please remove the junk files? Afterwards, if you're not comfortable with checking in changes using Mercurial, I can deal with that.",
    "created_at": "2009-07-15T16:06:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51579",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_051580.json:
```json
{
    "body": "Updated spkg at\n\nhttp://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg\n\nI've removed the junk file and checked in all changes in the name of David Kirkby. I've also fixed a minor typo. I have restarted building Sage 4.1 from scratch on t2 with the following updated spkg's:\n\n1. `pari-2.3.3.p1.spkg` #6445 \n2. `ntl-5.4.2.p9.spkg` #6380\n3. `zn_poly-0.9.p1.spkg` #6443\n4. `polybori-0.5rc.p9.spkg` this ticket",
    "created_at": "2009-07-15T19:11:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51580",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Updated spkg at

http://sage.math.washington.edu/home/mvngu/patch/polybori-0.5rc.p9.spkg

I've removed the junk file and checked in all changes in the name of David Kirkby. I've also fixed a minor typo. I have restarted building Sage 4.1 from scratch on t2 with the following updated spkg's:

1. `pari-2.3.3.p1.spkg` #6445 
2. `ntl-5.4.2.p9.spkg` #6380
3. `zn_poly-0.9.p1.spkg` #6443
4. `polybori-0.5rc.p9.spkg` this ticket



---

archive/issue_comments_051581.json:
```json
{
    "body": "David: I'm not sure how to deal with this one, since ticket #6528 contains the latest updated PolyBori SPKG. If the SPKG at #6528 also contains the fixes mentioned on this ticket, then this ticket can be closed as a duplicate of #6528. If not, then we shouldn't have two PolyBori SPKG's with the same name but patched differently.",
    "created_at": "2009-07-24T00:36:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51581",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

David: I'm not sure how to deal with this one, since ticket #6528 contains the latest updated PolyBori SPKG. If the SPKG at #6528 also contains the fixes mentioned on this ticket, then this ticket can be closed as a duplicate of #6528. If not, then we shouldn't have two PolyBori SPKG's with the same name but patched differently.



---

archive/issue_comments_051582.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-07-24T00:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51582",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: duplicate



---

archive/issue_comments_051583.json:
```json
{
    "body": "OK, I see that the SPKG at #6528 also fixes the linker issue reported on this ticket. So I'm closing this ticket as a duplicate of #6528. Please correct me if I'm wrong.",
    "created_at": "2009-07-24T00:53:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6437",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6437#issuecomment-51583",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

OK, I see that the SPKG at #6528 also fixes the linker issue reported on this ticket. So I'm closing this ticket as a duplicate of #6528. Please correct me if I'm wrong.
