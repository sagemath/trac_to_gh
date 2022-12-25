# Issue 7352: Update prereq to version 0.5

archive/issues_007352.json:
```json
{
    "body": "Assignee: tbd\n\nFollowing my recent updates of the code for checking the prerequisites for Sage are present (#7021), here is a further refinement. If implemented the following tickets can be closed. \n\n* #7156 prereq-0.4 has a minor portability issue.\n* #7142 We must check if the version of 'tar' found is gnu tar\n* #7143 We must check if the version of 'make' found is gnu 'make'\n* #7181 We must ensure we have GNU make, not HP-UX or Solaris 'make'\n* #7203 prereq-0.4 does not exit if CC is not gcc, but CXX is g++\n* #7182 HP-UX failure of gfan-0.3.p4 but easier to ensure we have GNU make.\n\nChanges are:\n\n**Changes to configure.ac**\n* Insists that the *configure* script is created using autoconf 2.63 or later.\n* Checks for *latex* and issues a gentle warning if it's not found, but makes it clear that *latex* is not essential. \n* Exits if gcc is not used as the C compiler, but g++ is used as the C++ compiler. (In *prereq-0.4* an error message was generated if *gcc* was used as the C compiler, but *g++* was not used as the C++ compiler). This addresses the other mixture, which I'd overlooked before. \n* Issues a warning that Solaris is unsupported on versions 9 or older. \n  * If sun4c or sun4m hardware is used, the *configure* script reports it is not possible to update to Solaris 10, and so problems might exist. \n  * If other Sun hardware is used, it advises people to update unless they have reasons for needing an old release of Solaris. \n  * Issues a warning that Darwin is too old on 5.x, 5.x.y, 6.x, 6.x.y, 7.x and 7.x.y. It states the oldest version of OS X on which Sage has been built is 10.4 (Tiger). The information about the relationship between Darwin and OS X versions is taken from  [http://en.wikipedia.org/wiki/Darwin_(operating_system)](http://en.wikipedia.org/wiki/Darwin_(operating_system)) \n  * Exits if *bash* can not be found. \n   * Suggests *bash* might be found in /opt/OpenSource/bin/ if the operating system is HP-UX. \n   * Suggests *bash* might be found in /opt/pware/bin if the operating system is AIX. \n  * Checks for *ar*, *strip*, *m4*, *ranlib* and *ld*. \n  \n\n**Changes to prereq-0.5-install**\n* Checks for GNU tar and GNU make on Solaris, making suggestions where they might be found (/usr/sfw/bin) or obtained via source, Blastwave or Sunfreeware. \n* Only uses the *-p* option to *uname* on Solaris. Previously the option was used on all platforms to check for Solaris on SPARC or x86. Since this option is not portable (not part of POSIX), it generated an error on HP-UX. \n* Removed all the checks for programs like *gcc*, *ld* since these were not portable, and always indicated the program was present on Solaris, even if it was not. \n \nThe code may be found here. \n\nhttp://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.5-3rd-try/\n\nNote both files need to be downloaded to $SAGE_ROOT/spkg/base, and the permissions on the script need to be 755. When it is downloaded via the web, the execute permissions will be lost. \n\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7352\n\n",
    "closed_at": "2009-11-20T06:18:35Z",
    "created_at": "2009-10-29T23:17:51Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Update prereq to version 0.5",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7352",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

Following my recent updates of the code for checking the prerequisites for Sage are present (#7021), here is a further refinement. If implemented the following tickets can be closed. 

* #7156 prereq-0.4 has a minor portability issue.
* #7142 We must check if the version of 'tar' found is gnu tar
* #7143 We must check if the version of 'make' found is gnu 'make'
* #7181 We must ensure we have GNU make, not HP-UX or Solaris 'make'
* #7203 prereq-0.4 does not exit if CC is not gcc, but CXX is g++
* #7182 HP-UX failure of gfan-0.3.p4 but easier to ensure we have GNU make.

Changes are:

**Changes to configure.ac**
* Insists that the *configure* script is created using autoconf 2.63 or later.
* Checks for *latex* and issues a gentle warning if it's not found, but makes it clear that *latex* is not essential. 
* Exits if gcc is not used as the C compiler, but g++ is used as the C++ compiler. (In *prereq-0.4* an error message was generated if *gcc* was used as the C compiler, but *g++* was not used as the C++ compiler). This addresses the other mixture, which I'd overlooked before. 
* Issues a warning that Solaris is unsupported on versions 9 or older. 
  * If sun4c or sun4m hardware is used, the *configure* script reports it is not possible to update to Solaris 10, and so problems might exist. 
  * If other Sun hardware is used, it advises people to update unless they have reasons for needing an old release of Solaris. 
  * Issues a warning that Darwin is too old on 5.x, 5.x.y, 6.x, 6.x.y, 7.x and 7.x.y. It states the oldest version of OS X on which Sage has been built is 10.4 (Tiger). The information about the relationship between Darwin and OS X versions is taken from  [http://en.wikipedia.org/wiki/Darwin_(operating_system)](http://en.wikipedia.org/wiki/Darwin_(operating_system)) 
  * Exits if *bash* can not be found. 
   * Suggests *bash* might be found in /opt/OpenSource/bin/ if the operating system is HP-UX. 
   * Suggests *bash* might be found in /opt/pware/bin if the operating system is AIX. 
  * Checks for *ar*, *strip*, *m4*, *ranlib* and *ld*. 
  

**Changes to prereq-0.5-install**
* Checks for GNU tar and GNU make on Solaris, making suggestions where they might be found (/usr/sfw/bin) or obtained via source, Blastwave or Sunfreeware. 
* Only uses the *-p* option to *uname* on Solaris. Previously the option was used on all platforms to check for Solaris on SPARC or x86. Since this option is not portable (not part of POSIX), it generated an error on HP-UX. 
* Removed all the checks for programs like *gcc*, *ld* since these were not portable, and always indicated the program was present on Solaris, even if it was not. 
 
The code may be found here. 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/prereq-0.5-3rd-try/

Note both files need to be downloaded to $SAGE_ROOT/spkg/base, and the permissions on the script need to be 755. When it is downloaded via the web, the execute permissions will be lost. 





Issue created by migration from https://trac.sagemath.org/ticket/7352





---

archive/issue_comments_061474.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-29T23:58:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7352#issuecomment-61474",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061475.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-20T06:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7352#issuecomment-61475",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.



---

archive/issue_comments_061476.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-20T06:18:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7352",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7352#issuecomment-61476",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017402.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-20T06:18:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7352",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7352#event-17402"
}
```
