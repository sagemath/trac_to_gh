# Issue 1657: make a build-from-source version of jmol spkg

archive/issues_001657.json:
```json
{
    "body": "Assignee: mabshoff\n\nThis is very important.\n\n\n```\nOn Jan 2, 2008 11:23 AM, Robert Bradshaw <robertwb@math.washington.edu> wrote:\n> In principle, all one would need is javac (and the java runtime\n> binaries). If they're going to be using java at all, they'll have that.\n>\n> It looks like they use the ant build tool which is a nice make system\n> for java. http://ant.apache.org/ For those interested in building the\n> java components from source, we could make an .spkg for this too (if\n> they don't have it already). I used ant for the java3d stuff too.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1657\n\n",
    "created_at": "2008-01-02T19:08:00Z",
    "labels": [
        "packages: standard",
        "critical",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "make a build-from-source version of jmol spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1657",
    "user": "was"
}
```
Assignee: mabshoff

This is very important.


```
On Jan 2, 2008 11:23 AM, Robert Bradshaw <robertwb@math.washington.edu> wrote:
> In principle, all one would need is javac (and the java runtime
> binaries). If they're going to be using java at all, they'll have that.
>
> It looks like they use the ant build tool which is a nice make system
> for java. http://ant.apache.org/ For those interested in building the
> java components from source, we could make an .spkg for this too (if
> they don't have it already). I used ant for the java3d stuff too.
```


Issue created by migration from https://trac.sagemath.org/ticket/1657





---

archive/issue_comments_010541.json:
```json
{
    "body": "Changing assignee from mabshoff to tkosan.",
    "created_at": "2008-01-02T21:46:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10541",
    "user": "tkosan"
}
```

Changing assignee from mabshoff to tkosan.



---

archive/issue_comments_010542.json:
```json
{
    "body": "Changing assignee from tkosan to mabshoff.",
    "created_at": "2008-01-02T23:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10542",
    "user": "tkosan"
}
```

Changing assignee from tkosan to mabshoff.



---

archive/issue_comments_010543.json:
```json
{
    "body": "I have jmol building/installing from source, but in the interest of\nsaving time I am not going to go through the last step of making an\nactual spkg out of it because I have not done this before and it will\nprobably take me some time to get it right.\n\nHere is a .zip file that contains the files needed to create a spkg:\n\nhttp://sage.math.washington.edu/home/tkosan/misc/jmol-11.5.2.spkg-src.zip",
    "created_at": "2008-01-02T23:10:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10543",
    "user": "tkosan"
}
```

I have jmol building/installing from source, but in the interest of
saving time I am not going to go through the last step of making an
actual spkg out of it because I have not done this before and it will
probably take me some time to get it right.

Here is a .zip file that contains the files needed to create a spkg:

http://sage.math.washington.edu/home/tkosan/misc/jmol-11.5.2.spkg-src.zip



---

archive/issue_comments_010544.json:
```json
{
    "body": "Fortunately, we don't need signing because we're using the unsigned version of the applets. \n\nAlso, there are several dependancies that are simply provided as jars. These need to be built from source as well prior to building jmol. See COPYRIGHT.txt",
    "created_at": "2008-01-03T10:08:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10544",
    "user": "robertwb"
}
```

Fortunately, we don't need signing because we're using the unsigned version of the applets. 

Also, there are several dependancies that are simply provided as jars. These need to be built from source as well prior to building jmol. See COPYRIGHT.txt



---

archive/issue_comments_010545.json:
```json
{
    "body": "jmol-11.5.2-src.spkg is ready for testing:\n\nhttp://sage.math.washington.edu/home/tkosan/misc/jmol-11.5.2-src-v2.spkg\n\nThe following packages needed to be included in the source version in order to remove any dependencies on binaries:\n\nbcmail\nbcprov\ncommons-cli   \ncommons-logging \ncommons-lang  \njmol-acme  \nservletapi\nitext            \nnetscape   \nvecmath-objectclub",
    "created_at": "2008-01-11T18:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10545",
    "user": "tkosan"
}
```

jmol-11.5.2-src.spkg is ready for testing:

http://sage.math.washington.edu/home/tkosan/misc/jmol-11.5.2-src-v2.spkg

The following packages needed to be included in the source version in order to remove any dependencies on binaries:

bcmail
bcprov
commons-cli   
commons-logging 
commons-lang  
jmol-acme  
servletapi
itext            
netscape   
vecmath-objectclub



---

archive/issue_comments_010546.json:
```json
{
    "body": "I looked at it an tried it out and it works great for me (after deleting the \"-v2\" from the filename). \n\nSomeone on a system with a minimal java install (Java + ant) should try it out too. \n\n- Robert",
    "created_at": "2008-01-11T20:54:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10546",
    "user": "robertwb"
}
```

I looked at it an tried it out and it works great for me (after deleting the "-v2" from the filename). 

Someone on a system with a minimal java install (Java + ant) should try it out too. 

- Robert



---

archive/issue_comments_010547.json:
```json
{
    "body": "Builds fine on sage.math after installing the Java SE 6 JDK (the standard one, for 64-bit Linux) and `ant`. Upgrading my copy of Sage to try it out...",
    "created_at": "2008-01-12T02:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10547",
    "user": "robertwb"
}
```

Builds fine on sage.math after installing the Java SE 6 JDK (the standard one, for 64-bit Linux) and `ant`. Upgrading my copy of Sage to try it out...



---

archive/issue_comments_010548.json:
```json
{
    "body": "Works great on sage.math as well. Looks ready to include (as an optional spkg).",
    "created_at": "2008-01-13T06:39:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10548",
    "user": "robertwb"
}
```

Works great on sage.math as well. Looks ready to include (as an optional spkg).



---

archive/issue_comments_010549.json:
```json
{
    "body": "I put the spkg in the optional spkg repo and mirrored it out.",
    "created_at": "2008-01-15T02:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10549",
    "user": "mabshoff"
}
```

I put the spkg in the optional spkg repo and mirrored it out.



---

archive/issue_comments_010550.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-15T02:58:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1657",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1657#issuecomment-10550",
    "user": "mabshoff"
}
```

Resolution: fixed
