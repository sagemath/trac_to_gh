# Issue 1465: the maple interface is broken in some configurations

archive/issues_001465.json:
```json
{
    "body": "Assignee: @williamstein\n\nG Edgar reported that on his mac the maple interface fails miserably to work at all.\nOn sage.math it works perfectly.  On my laptop (osx10.5.1 w/ maple 11) it does NOT work now. \n\nOn my laptop:\n\n```\nsage: maple.eval('2+2')\n'read \"/Users/was/.sage//temp/D_69_91_158_192.dhcp4.washington.edu/10242//i'\n```\n\n\nGerald Edgar:\n\n```\n13> sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.8.15, Release Date: 2007-12-03                      |\n| Type notebook() for the GUI, and license() for information.        |\nsage: maple.eval('2+2')\nEnd Of File (EOF) in read_nonblocking(). Empty string style platform.\n<pexpect.spawn instance at 0x9466378>\nversion: 2.0 ($Revision: 1.151 $)\ncommand: /Applications/sage-2.8.15-osx10.4-ppc-PowerMacintosh-Darwin/\nlocal/bin/maple\nargs: ['/Applications/sage-2.8.15-osx10.4-ppc-PowerMacintosh-Darwin/\nlocal/bin/maple', '-t']\npatterns:\n   #-->\nbuffer (last 100 chars):\nbefore (last 100 chars):\nafter: <class 'pexpect.EOF'>\nmatch: None\nmatch_index: None\nexitstatus: None\nflag_eof: 1\npid: 16993\nchild_fd: 3\ntimeout: 30\ndelimiter: <class 'pexpect.EOF'>\nlogfile: None\nmaxread: 100\nsearchwindowsize: None\ndelaybeforesend: 0\n#-->quit;\nbytes used=487432, alloc=393144, time=0.03\n---------------------------------------------------------------------------\n<type 'exceptions.RuntimeError'>          Traceback (most recent call\nlast)\n...\n   465         with gc_disabled():\n\n<type 'exceptions.RuntimeError'>: Unable to start maple\nsage: maple.eval('2+2')\n'read \"/Users/edgar/.sage//temp/dizzy.math.ohio_state.edu/16989//\ninterface/'\nsage: maple.eval('2+2')\n''\nsage: maple.eval('2+2')\n'4'\nsage:\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1465\n\n",
    "created_at": "2007-12-12T01:02:13Z",
    "labels": [
        "component: interfaces",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "the maple interface is broken in some configurations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1465",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

G Edgar reported that on his mac the maple interface fails miserably to work at all.
On sage.math it works perfectly.  On my laptop (osx10.5.1 w/ maple 11) it does NOT work now. 

On my laptop:

```
sage: maple.eval('2+2')
'read "/Users/was/.sage//temp/D_69_91_158_192.dhcp4.washington.edu/10242//i'
```


Gerald Edgar:

```
13> sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.15, Release Date: 2007-12-03                      |
| Type notebook() for the GUI, and license() for information.        |
sage: maple.eval('2+2')
End Of File (EOF) in read_nonblocking(). Empty string style platform.
<pexpect.spawn instance at 0x9466378>
version: 2.0 ($Revision: 1.151 $)
command: /Applications/sage-2.8.15-osx10.4-ppc-PowerMacintosh-Darwin/
local/bin/maple
args: ['/Applications/sage-2.8.15-osx10.4-ppc-PowerMacintosh-Darwin/
local/bin/maple', '-t']
patterns:
   #-->
buffer (last 100 chars):
before (last 100 chars):
after: <class 'pexpect.EOF'>
match: None
match_index: None
exitstatus: None
flag_eof: 1
pid: 16993
child_fd: 3
timeout: 30
delimiter: <class 'pexpect.EOF'>
logfile: None
maxread: 100
searchwindowsize: None
delaybeforesend: 0
#-->quit;
bytes used=487432, alloc=393144, time=0.03
---------------------------------------------------------------------------
<type 'exceptions.RuntimeError'>          Traceback (most recent call
last)
...
   465         with gc_disabled():

<type 'exceptions.RuntimeError'>: Unable to start maple
sage: maple.eval('2+2')
'read "/Users/edgar/.sage//temp/dizzy.math.ohio_state.edu/16989//
interface/'
sage: maple.eval('2+2')
''
sage: maple.eval('2+2')
'4'
sage:
```


Issue created by migration from https://trac.sagemath.org/ticket/1465





---

archive/issue_comments_009404.json:
```json
{
    "body": "I get the same error (OS X 10.5.5, Sage 3.2). I first noticed it when I tried to include Maple in my integration tests. Trying the same thing:\n\n```\nmaple.eval('2+2')\n'read \"/Users/tjlahey/.sage//temp/Cameron.local/61581//interface//tmp61581\"'\n```\n",
    "created_at": "2008-11-27T02:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1465#issuecomment-9404",
    "user": "https://github.com/tjl"
}
```

I get the same error (OS X 10.5.5, Sage 3.2). I first noticed it when I tried to include Maple in my integration tests. Trying the same thing:

```
maple.eval('2+2')
'read "/Users/tjlahey/.sage//temp/Cameron.local/61581//interface//tmp61581"'
```




---

archive/issue_comments_009405.json:
```json
{
    "body": "See Ticket #12295.",
    "created_at": "2013-02-16T17:30:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1465#issuecomment-9405",
    "user": "https://trac.sagemath.org/admin/accounts/users/migeruhito"
}
```

See Ticket #12295.



---

archive/issue_comments_009406.json:
```json
{
    "body": "I think that we should close this one in favor of #12295 and #2120, both of which already have a patch (I'm not sure if they conflict or are orthogonal).",
    "created_at": "2013-04-16T21:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1465#issuecomment-9406",
    "user": "https://github.com/kcrisman"
}
```

I think that we should close this one in favor of #12295 and #2120, both of which already have a patch (I'm not sure if they conflict or are orthogonal).



---

archive/issue_comments_009407.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-04-16T21:22:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1465#issuecomment-9407",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_009408.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-04-16T21:22:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1465#issuecomment-9408",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_001616.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-04-17T07:36:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1465",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1465#event-1616"
}
```



---

archive/issue_comments_009409.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2013-04-17T07:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1465",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1465#issuecomment-9409",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
