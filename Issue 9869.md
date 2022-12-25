# Issue 9869: Clean up Cliquer's Makefile and spkg-install

archive/issues_009869.json:
```json
{
    "body": "Assignee: GeorgSWeber\n\nCC:  @nathanncohen mvngu\n\nThe `Makefile` and `spkg-install` for Cliquer could do with a lot of cleaning up. Some examples of the problems are:\n\n* There are flags set for the C++ and Fortran compilers, though the code is only C. \n* There's code to check for a mix of Sun and GNU compilers, when better tests now exists as `$SAGE_LOCAL/bin/testcc.sh`\n* Lots of unnecessary environment variables are set. \n* Many, many other problems. \n\n**None of these issues are currently causing any problems, but should be resolved at some point**\n\nIssue created by migration from https://trac.sagemath.org/ticket/9870\n\n",
    "created_at": "2010-09-07T21:20:38Z",
    "labels": [
        "component: build",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.2",
    "title": "Clean up Cliquer's Makefile and spkg-install",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9869",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: GeorgSWeber

CC:  @nathanncohen mvngu

The `Makefile` and `spkg-install` for Cliquer could do with a lot of cleaning up. Some examples of the problems are:

* There are flags set for the C++ and Fortran compilers, though the code is only C. 
* There's code to check for a mix of Sun and GNU compilers, when better tests now exists as `$SAGE_LOCAL/bin/testcc.sh`
* Lots of unnecessary environment variables are set. 
* Many, many other problems. 

**None of these issues are currently causing any problems, but should be resolved at some point**

Issue created by migration from https://trac.sagemath.org/ticket/9870





---

archive/issue_comments_097330.json:
```json
{
    "body": "Changing assignee from GeorgSWeber to @nexttime.",
    "created_at": "2010-09-09T02:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97330",
    "user": "https://github.com/nexttime"
}
```

Changing assignee from GeorgSWeber to @nexttime.



---

archive/issue_comments_097331.json:
```json
{
    "body": "To tranquilize Dave :-)\n\nI've made several comments at tickets related to Cliquer, e.g. #9833 and #9871.\n\nI think this should then be a follow-up of #9871, despite the numbers.",
    "created_at": "2010-09-09T02:24:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97331",
    "user": "https://github.com/nexttime"
}
```

To tranquilize Dave :-)

I've made several comments at tickets related to Cliquer, e.g. #9833 and #9871.

I think this should then be a follow-up of #9871, despite the numbers.



---

archive/issue_comments_097332.json:
```json
{
    "body": "Changing component from build to linear programming.",
    "created_at": "2010-09-15T09:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97332",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from build to linear programming.



---

archive/issue_comments_097333.json:
```json
{
    "body": "Hello !\n\n> There is one technical question you can however answer. Do we need the binary file \"cl\" so it can be executed from the command line, or is the library libcliquer.so sufficient?\n\nNo, the cl file is not used, and this is precisely what the Sage code included in cliquer is useful for : directly calling the library's functions with a Graph object using the Graph structure it expects to find, without having to create an ugly temporary file to call the executable on it `:-)`\n\nNathann",
    "created_at": "2010-09-15T11:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97333",
    "user": "https://github.com/nathanncohen"
}
```

Hello !

> There is one technical question you can however answer. Do we need the binary file "cl" so it can be executed from the command line, or is the library libcliquer.so sufficient?

No, the cl file is not used, and this is precisely what the Sage code included in cliquer is useful for : directly calling the library's functions with a Graph object using the Graph structure it expects to find, without having to create an ugly temporary file to call the executable on it `:-)`

Nathann



---

archive/issue_comments_097334.json:
```json
{
    "body": "Leif, you were keen to take ownership of this. Has anything happened with it? \n\nDave",
    "created_at": "2010-11-07T00:19:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97334",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Leif, you were keen to take ownership of this. Has anything happened with it? 

Dave



---

archive/issue_comments_097335.json:
```json
{
    "body": "I ask once again. Any chance of you sorting this out Leif, since you wanted to take ownership of it. \n\nDave",
    "created_at": "2011-03-23T15:09:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97335",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I ask once again. Any chance of you sorting this out Leif, since you wanted to take ownership of it. 

Dave



---

archive/issue_comments_097336.json:
```json
{
    "body": "See #11227 for another issue with cliquer, unrelated to this ticket.",
    "created_at": "2011-04-25T17:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97336",
    "user": "https://github.com/jdemeyer"
}
```

See #11227 for another issue with cliquer, unrelated to this ticket.



---

archive/issue_comments_097337.json:
```json
{
    "body": "Changing component from linear programming to packages: standard.",
    "created_at": "2014-01-16T13:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97337",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from linear programming to packages: standard.



---

archive/issue_comments_097338.json:
```json
{
    "body": "I'll tackle this.",
    "created_at": "2014-01-16T13:34:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97338",
    "user": "https://github.com/jdemeyer"
}
```

I'll tackle this.



---

archive/issue_comments_097339.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-01-16T14:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97339",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097340.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-16T14:41:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97340",
    "user": "https://github.com/jdemeyer"
}
```

New commits:



---

archive/issue_comments_097341.json:
```json
{
    "body": "Don't know why trac was not able to merge the branch as I encountered no conflicts when merging it.\n\nI've made a few changes to make the script more like the \"new\" scripts as described in the dev guide, you may not be happy with them and are very welcome to change them back.\nOtherwise let's positively review this ticket.\n\nAnyway, I'm going to autotoolify cliquer, post it in a follow-up ticket and suggest it upstream.\nThe Makefile is just too awful right now.\n----\nNew commits:",
    "created_at": "2014-02-20T16:13:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97341",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

Don't know why trac was not able to merge the branch as I encountered no conflicts when merging it.

I've made a few changes to make the script more like the "new" scripts as described in the dev guide, you may not be happy with them and are very welcome to change them back.
Otherwise let's positively review this ticket.

Anyway, I'm going to autotoolify cliquer, post it in a follow-up ticket and suggest it upstream.
The Makefile is just too awful right now.
----
New commits:



---

archive/issue_comments_097342.json:
```json
{
    "body": "I've sent an email upstream about the possibility of releasing an official version including some of the Debian's patches (http://anonscm.debian.org/gitweb/?p=debian-science/packages/cliquer.git;a=tree;f=debian/patches;hb=HEAD) and an autotoolified build system.",
    "created_at": "2014-02-20T16:28:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97342",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

I've sent an email upstream about the possibility of releasing an official version including some of the Debian's patches (http://anonscm.debian.org/gitweb/?p=debian-science/packages/cliquer.git;a=tree;f=debian/patches;hb=HEAD) and an autotoolified build system.



---

archive/issue_comments_097343.json:
```json
{
    "body": "I think `set -e` is a good thing and should be used more. So I reverted that change.",
    "created_at": "2014-02-21T06:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97343",
    "user": "https://github.com/jdemeyer"
}
```

I think `set -e` is a good thing and should be used more. So I reverted that change.



---

archive/issue_comments_097344.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-02-21T06:03:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97344",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009999.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-02-22T06:45:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9869#event-9999"
}
```



---

archive/issue_comments_097345.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-02-22T06:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97345",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_097346.json:
```json
{
    "body": "FYI, upstream has nicely answered my questions.\nThey don't really mind cliquer being distributed in different forms in various places and don't plan on releasing any new upstream version \"in the next ten years or so (or ever?)\".",
    "created_at": "2014-02-24T13:30:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9869",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9869#issuecomment-97346",
    "user": "https://trac.sagemath.org/admin/accounts/users/jpflori"
}
```

FYI, upstream has nicely answered my questions.
They don't really mind cliquer being distributed in different forms in various places and don't plan on releasing any new upstream version "in the next ten years or so (or ever?)".
