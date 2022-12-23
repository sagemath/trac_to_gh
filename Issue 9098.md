# Issue 9098: gap buillds 32-bit on OpenSolaris when SAGE64=yes

archive/issues_009098.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  jsp\n\ngap is building as a 32-bit application:\n\n```\nconfig.status: creating gac\nconfig.status: creating Makefile\nconfig.status: creating config.h\n( cd bin/i386-pc-solaris2.11-gcc ; make CC='gcc' )\nmake[3]: Entering directory `/export/home/drkirkby/sage-4.4.2/spkg/build/gap-4.4.12.p3/src/bin/i386-pc-solaris2.11-gcc'\ngcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o ariths.o -c ../../src/ariths.c\ngcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o blister.o -c ../../src/blister.c\n```\n\n\nAlthough it builds, the binaries are 32-bit:\n\n\n```\ndrkirkby@hawk:~/sage-4.4.2$ find . -exec file {} \\; | grep 32-bit\n./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/objcftl.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/saveload.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/listoper.o:\tELF 32-bit LSB relocatable 80386 Version 1\n./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/read.o:\tELF 32-bit LSB relocatable 80386 Version 1\n```\n\n\nThere's nothing in spkg-install to add the -m64 flag on any operating system, so I doubt this ever built as a 64-bit application on OS X. \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/9098\n\n",
    "created_at": "2010-05-31T01:02:38Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "title": "gap buillds 32-bit on OpenSolaris when SAGE64=yes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9098",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  jsp

gap is building as a 32-bit application:

```
config.status: creating gac
config.status: creating Makefile
config.status: creating config.h
( cd bin/i386-pc-solaris2.11-gcc ; make CC='gcc' )
make[3]: Entering directory `/export/home/drkirkby/sage-4.4.2/spkg/build/gap-4.4.12.p3/src/bin/i386-pc-solaris2.11-gcc'
gcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o ariths.o -c ../../src/ariths.c
gcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o blister.o -c ../../src/blister.c
```


Although it builds, the binaries are 32-bit:


```
drkirkby@hawk:~/sage-4.4.2$ find . -exec file {} \; | grep 32-bit
./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/objcftl.o:	ELF 32-bit LSB relocatable 80386 Version 1
./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/saveload.o:	ELF 32-bit LSB relocatable 80386 Version 1
./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/listoper.o:	ELF 32-bit LSB relocatable 80386 Version 1
./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/read.o:	ELF 32-bit LSB relocatable 80386 Version 1
```


There's nothing in spkg-install to add the -m64 flag on any operating system, so I doubt this ever built as a 64-bit application on OS X. 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/9098





---

archive/issue_comments_084534.json:
```json
{
    "body": "Note, there is a note in spkg-install that one has to unset CXXFLAGS and CFLAGS otherwise gap does not like it. Hence this one could be problematic. We many need to alter the flags with a sed script, or something like that.",
    "created_at": "2010-06-14T17:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9098#issuecomment-84534",
    "user": "drkirkby"
}
```

Note, there is a note in spkg-install that one has to unset CXXFLAGS and CFLAGS otherwise gap does not like it. Hence this one could be problematic. We many need to alter the flags with a sed script, or something like that.



---

archive/issue_comments_084535.json:
```json
{
    "body": "Having looked at this more, I decided to ignore all the warnings in spkg-install, but only make the needed changes on Solaris. Hence the changes will not add '-m64' on OS X, FreeBSD or any other system apart from Solaris and OpenSolaris. \n\nThe revised .spkg may be found here. \n\nhttp://boxen.math.washington.edu/home/kirkby/patches/gap-4.4.12.p4.spkg\n\nThe changes have been checked on the following systems. In each case, it was verified that gap worked.\n* Linux (64-bit)\n* OpenSolaris x64 (64-bit)\n* Solaris 10 SPARC (32-bit)\n* Solaris 10 SPARC (64-bit)\n\nSee below for further details of tests. \n == Linux (sage.math.washington.edu) ==\n\n```\ngcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o iostream.o -c ../../src/iostream.c\ngcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o float.o -c ../../src/float.c\ngcc -Wall -g -O2  -g -export-dynamic  -o gap ariths.o blister.o bool.o c_meths1.o c_type1.o c_oper1.o c_filt1.o c_random.o calls.o code.o compiler.o compstat.o costab.o cyclotom.o dt.o dteval.o exprs.o finfield.o funcs.o gap.o gasman.o gvars.o integer.o intrprtr.o listfunc.o listoper.o lists.o objcftl.o objects.o objfgelm.o objpcgel.o objscoll.o objccoll.o opers.o permutat.o plist.o precord.o range.o rational.o read.o records.o saveload.o scanner.o sctable.o set.o stats.o streams.o string.o sysfiles.o system.o tietze.o vars.o vecgf2.o vec8bit.o vector.o vecffe.o weakptr.o iostream.o float.o   -lm    -ldl \nmake[1]: Leaving directory `/home/kirkby/sage-4.4.3/spkg/build/gap-4.4.12.p4/src/bin/x86_64-unknown-linux-gnu-gcc'\nchmod +x bin/gap.sh\nif ! grep darwin sysinfo.gap ; then ( cd bin/x86_64-unknown-linux-gnu-gcc ; strip gap) ; fi\n\nreal\t1m3.882s\nuser\t0m47.790s\nsys\t0m7.500s\nSuccessfully installed gap-4.4.12.p4\nNow cleaning up tmp files.\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing gap-4.4.12.p4.spkg\nkirkby@sage:~/sage-4.4.3$ uname -a\nLinux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux\n```\n\n\n == OpenSolaris 64-bit 06/2009 ('hawk' a Sun Ultra 27) ==\n\n```\nmake[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha0/spkg/build/gap-4.4.12.p4/src/bin/i386-pc-solaris2.11-gcc'\nchmod +x bin/gap.sh\nif ! grep darwin sysinfo.gap ; then ( cd bin/i386-pc-solaris2.11-gcc ; strip gap) ; fi\n\nreal\t0m35.057s\nuser\t0m30.127s\nsys\t0m4.371s\nSuccessfully installed gap-4.4.12.p4\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n/export/home/drkirkby/sage-4.4.4.alpha0/spkg/build/gap-4.4.12.p4\nMaking Sage/Python scripts relocatable...\nMaking script relocatable\nFinished installing gap-4.4.12.p4.spkg\n```\n\nWe can see there is a 64-bit executable\n\n```\ndrkirkby@hawk:~/sage-4.4.4.alpha0$ find . -name gap\n./spkg/standard/gap-4.4.12.p4/patches/gap\n./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/gap\n./local/bin/gap\n./data/extcode/gap\n./data/extcode/.hg/data/gap\n```\n\n\nAlthough I do not know how to call gap from Sage, the program runs at the command line and is at least able to calculate something. \n\n```\ndrkirkby@hawk:~/sage-4.4.4.alpha0$ ./local/bin/gap\nSet the environment variable SAGE_ROOT.\ndrkirkby@hawk:~/sage-4.4.4.alpha0$ export SAGE_ROOT=.\ndrkirkby@hawk:~/sage-4.4.4.alpha0$ ./local/bin/gap\n    \n            #########           ######         ###########           ###  \n         #############          ######         ############         ####  \n        ##############         ########        #############       #####  \n       ###############         ########        #####   ######      #####  \n      ######         #         #########       #####    #####     ######  \n     ######                   ##########       #####    #####    #######  \n     #####                    ##### ####       #####   ######   ########  \n     ####                    #####  #####      #############   ###  ####  \n     #####     #######       ####    ####      ###########    ####  ####  \n     #####     #######      #####    #####     ######        ####   ####  \n     #####     #######      #####    #####     #####         #############\n      #####      #####     ################    #####         #############\n      ######     #####     ################    #####         #############\n      ################    ##################   #####                ####  \n       ###############    #####        #####   #####                ####  \n         #############    #####        #####   #####                ####  \n          #########      #####          #####  #####                ####  \n                                                                          \n     Information at:  http://www.gap-system.org\n     Try '?help' for help. See also  '?copyright' and  '?authors'\n    \n   Loading the library. Please be patient, this may take a while.\nGAP4, Version: 4.4.12 of 17-Dec-2008, i386-pc-solaris2.11-gcc -m64\ngap> 10^20 + 1;\n100000000000000000001\ngap> \n```\n\n\n## Solaris 10 (SPARC) 32-bit ('redstart' a Sun Blade 1000)\nOn a SPARC in 32-bit mode (the only Solaris system which works fully with Sage), we can see that gap builds ok. \n\n```\n.o vec8bit.o vector.o vecffe.o weakptr.o iostream.o float.o   -lm    \nmake[1]: Leaving directory `/export/home/drkirkby/32/sage-4.4.3/spkg/build/gap-4.4.12.p4/src/bin/sparc-sun-solaris2.10-gcc'\nchmod +x bin/gap.sh\nif ! grep darwin sysinfo.gap ; then ( cd bin/sparc-sun-solaris2.10-gcc ; strip gap) ; fi\n/bin/sh: !: not found\n\nreal    5m15.428s\nuser    4m42.147s\nsys     0m26.935s\nSuccessfully installed gap-4.4.12.p4\nNow cleaning up tmp files.\nrm: Cannot remove any directory in the path of the current working directory\n```\n\nAgain, gap can be seen to work, but this time in 32-bit mode.\n\n```\ndrkirkby@redstart:~/32/sage-4.4.3$ export SAGE_ROOT .\n-bash: export: `.': not a valid identifier\ndrkirkby@redstart:~/32/sage-4.4.3$ export SAGE_ROOT=.\ndrkirkby@redstart:~/32/sage-4.4.3$ local/bin/gap\n    \n            #########           ######         ###########           ###  \n         #############          ######         ############         ####  \n        ##############         ########        #############       #####  \n       ###############         ########        #####   ######      #####  \n      ######         #         #########       #####    #####     ######  \n     ######                   ##########       #####    #####    #######  \n     #####                    ##### ####       #####   ######   ########  \n     ####                    #####  #####      #############   ###  ####  \n     #####     #######       ####    ####      ###########    ####  ####  \n     #####     #######      #####    #####     ######        ####   ####  \n     #####     #######      #####    #####     #####         #############\n      #####      #####     ################    #####         #############\n      ######     #####     ################    #####         #############\n      ################    ##################   #####                ####  \n       ###############    #####        #####   #####                ####  \n         #############    #####        #####   #####                ####  \n          #########      #####          #####  #####                ####  \n                                                                          \n     Information at:  http://www.gap-system.org\n     Try '?help' for help. See also  '?copyright' and  '?authors'\n    \n   Loading the library. Please be patient, this may take a while.\nGAP4, Version: 4.4.12 of 17-Dec-2008, sparc-sun-solaris2.10-gcc\ngap> 12+2;\n14\ngap> \n```\n\n## Solaris 10 (SPARC) 64-bit ('redstart' a Sun Blade 1000)\nAlthough little effort has been put into a 64-bit port to Solaris 10 on SPARC, changes made to build OpenSolaris x64 will usually benefit Solaris 10 on SPARC too. We can see gap builds 64-bit. \n\n```\ndrkirkby@redstart:~/32/sage-4.4.3$ export SAGE_ROOT=.\ndrkirkby@redstart:~/32/sage-4.4.3$ local/bin/gap\n    \n            #########           ######         ###########           ###  \n         #############          ######         ############         ####  \n        ##############         ########        #############       #####  \n       ###############         ########        #####   ######      #####  \n      ######         #         #########       #####    #####     ######  \n     ######                   ##########       #####    #####    #######  \n     #####                    ##### ####       #####   ######   ########  \n     ####                    #####  #####      #############   ###  ####  \n     #####     #######       ####    ####      ###########    ####  ####  \n     #####     #######      #####    #####     ######        ####   ####  \n     #####     #######      #####    #####     #####         #############\n      #####      #####     ################    #####         #############\n      ######     #####     ################    #####         #############\n      ################    ##################   #####                ####  \n       ###############    #####        #####   #####                ####  \n         #############    #####        #####   #####                ####  \n          #########      #####          #####  #####                ####  \n                                                                          \n     Information at:  http://www.gap-system.org\n     Try '?help' for help. See also  '?copyright' and  '?authors'\n    \n   Loading the library. Please be patient, this may take a while.\nGAP4, Version: 4.4.12 of 17-Dec-2008, sparc-sun-solaris2.10-gcc -m64\ngap>  s8 := Group( (1,2), (1,2,3,4,5,6,7,8) );\nGroup([ (1,2), (1,2,3,4,5,6,7,8) ])\ngap> a8 := DerivedSubgroup( s8 );\nGroup([ (1,2,3), (2,3,4), (2,4)(3,5), (2,6,4), (2,4)(5,7), (2,8,6,4)(3,5) ])\ngap> Size( a8 ); IsAbelian( a8 ); IsPerfect( a8 );\n20160\nfalse\ntrue\ngap> \n```\n\nWe can see that the binary created is indeed 64-bit:\n\n\n```\ndrkirkby@redstart:~/32/sage-4.4.3$ file ./local/bin/gap\n./local/bin/gap:        executable shell script\ndrkirkby@redstart:~/32/sage-4.4.3$ file ./local/lib/gap-4.4.12/bin/sparc-sun-solaris2.10-gcc/gap\n./local/lib/gap-4.4.12/bin/sparc-sun-solaris2.10-gcc/gap:       ELF 64-bit MSB executable SPARCV9 Version 1, dynamically linked, not stripped, no debugging information available\ndrkirkby@redstart:~/32/sage-4.4.3$ \n```\n",
    "created_at": "2010-06-14T21:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9098#issuecomment-84535",
    "user": "drkirkby"
}
```

Having looked at this more, I decided to ignore all the warnings in spkg-install, but only make the needed changes on Solaris. Hence the changes will not add '-m64' on OS X, FreeBSD or any other system apart from Solaris and OpenSolaris. 

The revised .spkg may be found here. 

http://boxen.math.washington.edu/home/kirkby/patches/gap-4.4.12.p4.spkg

The changes have been checked on the following systems. In each case, it was verified that gap worked.
* Linux (64-bit)
* OpenSolaris x64 (64-bit)
* Solaris 10 SPARC (32-bit)
* Solaris 10 SPARC (64-bit)

See below for further details of tests. 
 == Linux (sage.math.washington.edu) ==

```
gcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o iostream.o -c ../../src/iostream.c
gcc -I. -I../.. -DCONFIG_H -Wall -g -O2  -o float.o -c ../../src/float.c
gcc -Wall -g -O2  -g -export-dynamic  -o gap ariths.o blister.o bool.o c_meths1.o c_type1.o c_oper1.o c_filt1.o c_random.o calls.o code.o compiler.o compstat.o costab.o cyclotom.o dt.o dteval.o exprs.o finfield.o funcs.o gap.o gasman.o gvars.o integer.o intrprtr.o listfunc.o listoper.o lists.o objcftl.o objects.o objfgelm.o objpcgel.o objscoll.o objccoll.o opers.o permutat.o plist.o precord.o range.o rational.o read.o records.o saveload.o scanner.o sctable.o set.o stats.o streams.o string.o sysfiles.o system.o tietze.o vars.o vecgf2.o vec8bit.o vector.o vecffe.o weakptr.o iostream.o float.o   -lm    -ldl 
make[1]: Leaving directory `/home/kirkby/sage-4.4.3/spkg/build/gap-4.4.12.p4/src/bin/x86_64-unknown-linux-gnu-gcc'
chmod +x bin/gap.sh
if ! grep darwin sysinfo.gap ; then ( cd bin/x86_64-unknown-linux-gnu-gcc ; strip gap) ; fi

real	1m3.882s
user	0m47.790s
sys	0m7.500s
Successfully installed gap-4.4.12.p4
Now cleaning up tmp files.
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gap-4.4.12.p4.spkg
kirkby@sage:~/sage-4.4.3$ uname -a
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux
```


 == OpenSolaris 64-bit 06/2009 ('hawk' a Sun Ultra 27) ==

```
make[1]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha0/spkg/build/gap-4.4.12.p4/src/bin/i386-pc-solaris2.11-gcc'
chmod +x bin/gap.sh
if ! grep darwin sysinfo.gap ; then ( cd bin/i386-pc-solaris2.11-gcc ; strip gap) ; fi

real	0m35.057s
user	0m30.127s
sys	0m4.371s
Successfully installed gap-4.4.12.p4
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
/export/home/drkirkby/sage-4.4.4.alpha0/spkg/build/gap-4.4.12.p4
Making Sage/Python scripts relocatable...
Making script relocatable
Finished installing gap-4.4.12.p4.spkg
```

We can see there is a 64-bit executable

```
drkirkby@hawk:~/sage-4.4.4.alpha0$ find . -name gap
./spkg/standard/gap-4.4.12.p4/patches/gap
./local/lib/gap-4.4.12/bin/i386-pc-solaris2.11-gcc/gap
./local/bin/gap
./data/extcode/gap
./data/extcode/.hg/data/gap
```


Although I do not know how to call gap from Sage, the program runs at the command line and is at least able to calculate something. 

```
drkirkby@hawk:~/sage-4.4.4.alpha0$ ./local/bin/gap
Set the environment variable SAGE_ROOT.
drkirkby@hawk:~/sage-4.4.4.alpha0$ export SAGE_ROOT=.
drkirkby@hawk:~/sage-4.4.4.alpha0$ ./local/bin/gap
    
            #########           ######         ###########           ###  
         #############          ######         ############         ####  
        ##############         ########        #############       #####  
       ###############         ########        #####   ######      #####  
      ######         #         #########       #####    #####     ######  
     ######                   ##########       #####    #####    #######  
     #####                    ##### ####       #####   ######   ########  
     ####                    #####  #####      #############   ###  ####  
     #####     #######       ####    ####      ###########    ####  ####  
     #####     #######      #####    #####     ######        ####   ####  
     #####     #######      #####    #####     #####         #############
      #####      #####     ################    #####         #############
      ######     #####     ################    #####         #############
      ################    ##################   #####                ####  
       ###############    #####        #####   #####                ####  
         #############    #####        #####   #####                ####  
          #########      #####          #####  #####                ####  
                                                                          
     Information at:  http://www.gap-system.org
     Try '?help' for help. See also  '?copyright' and  '?authors'
    
   Loading the library. Please be patient, this may take a while.
GAP4, Version: 4.4.12 of 17-Dec-2008, i386-pc-solaris2.11-gcc -m64
gap> 10^20 + 1;
100000000000000000001
gap> 
```


## Solaris 10 (SPARC) 32-bit ('redstart' a Sun Blade 1000)
On a SPARC in 32-bit mode (the only Solaris system which works fully with Sage), we can see that gap builds ok. 

```
.o vec8bit.o vector.o vecffe.o weakptr.o iostream.o float.o   -lm    
make[1]: Leaving directory `/export/home/drkirkby/32/sage-4.4.3/spkg/build/gap-4.4.12.p4/src/bin/sparc-sun-solaris2.10-gcc'
chmod +x bin/gap.sh
if ! grep darwin sysinfo.gap ; then ( cd bin/sparc-sun-solaris2.10-gcc ; strip gap) ; fi
/bin/sh: !: not found

real    5m15.428s
user    4m42.147s
sys     0m26.935s
Successfully installed gap-4.4.12.p4
Now cleaning up tmp files.
rm: Cannot remove any directory in the path of the current working directory
```

Again, gap can be seen to work, but this time in 32-bit mode.

```
drkirkby@redstart:~/32/sage-4.4.3$ export SAGE_ROOT .
-bash: export: `.': not a valid identifier
drkirkby@redstart:~/32/sage-4.4.3$ export SAGE_ROOT=.
drkirkby@redstart:~/32/sage-4.4.3$ local/bin/gap
    
            #########           ######         ###########           ###  
         #############          ######         ############         ####  
        ##############         ########        #############       #####  
       ###############         ########        #####   ######      #####  
      ######         #         #########       #####    #####     ######  
     ######                   ##########       #####    #####    #######  
     #####                    ##### ####       #####   ######   ########  
     ####                    #####  #####      #############   ###  ####  
     #####     #######       ####    ####      ###########    ####  ####  
     #####     #######      #####    #####     ######        ####   ####  
     #####     #######      #####    #####     #####         #############
      #####      #####     ################    #####         #############
      ######     #####     ################    #####         #############
      ################    ##################   #####                ####  
       ###############    #####        #####   #####                ####  
         #############    #####        #####   #####                ####  
          #########      #####          #####  #####                ####  
                                                                          
     Information at:  http://www.gap-system.org
     Try '?help' for help. See also  '?copyright' and  '?authors'
    
   Loading the library. Please be patient, this may take a while.
GAP4, Version: 4.4.12 of 17-Dec-2008, sparc-sun-solaris2.10-gcc
gap> 12+2;
14
gap> 
```

## Solaris 10 (SPARC) 64-bit ('redstart' a Sun Blade 1000)
Although little effort has been put into a 64-bit port to Solaris 10 on SPARC, changes made to build OpenSolaris x64 will usually benefit Solaris 10 on SPARC too. We can see gap builds 64-bit. 

```
drkirkby@redstart:~/32/sage-4.4.3$ export SAGE_ROOT=.
drkirkby@redstart:~/32/sage-4.4.3$ local/bin/gap
    
            #########           ######         ###########           ###  
         #############          ######         ############         ####  
        ##############         ########        #############       #####  
       ###############         ########        #####   ######      #####  
      ######         #         #########       #####    #####     ######  
     ######                   ##########       #####    #####    #######  
     #####                    ##### ####       #####   ######   ########  
     ####                    #####  #####      #############   ###  ####  
     #####     #######       ####    ####      ###########    ####  ####  
     #####     #######      #####    #####     ######        ####   ####  
     #####     #######      #####    #####     #####         #############
      #####      #####     ################    #####         #############
      ######     #####     ################    #####         #############
      ################    ##################   #####                ####  
       ###############    #####        #####   #####                ####  
         #############    #####        #####   #####                ####  
          #########      #####          #####  #####                ####  
                                                                          
     Information at:  http://www.gap-system.org
     Try '?help' for help. See also  '?copyright' and  '?authors'
    
   Loading the library. Please be patient, this may take a while.
GAP4, Version: 4.4.12 of 17-Dec-2008, sparc-sun-solaris2.10-gcc -m64
gap>  s8 := Group( (1,2), (1,2,3,4,5,6,7,8) );
Group([ (1,2), (1,2,3,4,5,6,7,8) ])
gap> a8 := DerivedSubgroup( s8 );
Group([ (1,2,3), (2,3,4), (2,4)(3,5), (2,6,4), (2,4)(5,7), (2,8,6,4)(3,5) ])
gap> Size( a8 ); IsAbelian( a8 ); IsPerfect( a8 );
20160
false
true
gap> 
```

We can see that the binary created is indeed 64-bit:


```
drkirkby@redstart:~/32/sage-4.4.3$ file ./local/bin/gap
./local/bin/gap:        executable shell script
drkirkby@redstart:~/32/sage-4.4.3$ file ./local/lib/gap-4.4.12/bin/sparc-sun-solaris2.10-gcc/gap
./local/lib/gap-4.4.12/bin/sparc-sun-solaris2.10-gcc/gap:       ELF 64-bit MSB executable SPARCV9 Version 1, dynamically linked, not stripped, no debugging information available
drkirkby@redstart:~/32/sage-4.4.3$ 
```




---

archive/issue_comments_084536.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-06-14T21:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9098#issuecomment-84536",
    "user": "drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_084537.json:
```json
{
    "body": "Attachment\n\nMercurial patch which enables gap to build 64-bit on Solaris 10 and OpenSolaris",
    "created_at": "2010-06-14T21:13:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9098#issuecomment-84537",
    "user": "drkirkby"
}
```

Attachment

Mercurial patch which enables gap to build 64-bit on Solaris 10 and OpenSolaris



---

archive/issue_comments_084538.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-14T22:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9098#issuecomment-84538",
    "user": "jsp"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_084539.json:
```json
{
    "body": "I can confirm, this effects only 64-bit on Solaris (10 and OpenSolaris).\n\nI'll give it a positive review.\n\nJaap",
    "created_at": "2010-06-14T22:21:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9098#issuecomment-84539",
    "user": "jsp"
}
```

I can confirm, this effects only 64-bit on Solaris (10 and OpenSolaris).

I'll give it a positive review.

Jaap



---

archive/issue_comments_084540.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-25T15:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9098",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9098#issuecomment-84540",
    "user": "rlm"
}
```

Resolution: fixed
