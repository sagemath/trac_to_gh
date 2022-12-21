# Issue 1465: the maple interface is broken in some configurations

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-12-12 01:02:13

Assignee: was

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



---

Comment by tjlahey created at 2008-11-27 02:03:13

I get the same error (OS X 10.5.5, Sage 3.2). I first noticed it when I tried to include Maple in my integration tests. Trying the same thing:

```
maple.eval('2+2')
'read "/Users/tjlahey/.sage//temp/Cameron.local/61581//interface//tmp61581"'
```



---

Comment by migeruhito created at 2013-02-16 17:30:22

See Ticket #12295.


---

Comment by kcrisman created at 2013-04-16 21:22:15

I think that we should close this one in favor of #12295 and #2120, both of which already have a patch (I'm not sure if they conflict or are orthogonal).


---

Comment by kcrisman created at 2013-04-16 21:22:15

Changing status from new to needs_review.


---

Comment by kcrisman created at 2013-04-16 21:22:46

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-04-17 07:36:26

Resolution: duplicate
