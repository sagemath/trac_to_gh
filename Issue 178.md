# Issue 178: Sage()._get() does not return the correct result in some instances

Issue created by migration from https://trac.sagemath.org/ticket/178

Original creator: yi

Original creation time: 2006-12-08 01:17:31

Assignee: boothby

Keywords: Sage() expect Pexpect

sage: P = Sage()
sage: P._send('factor(2^250-1)')
sage: P._get()
(True, 'factor(2^250-1)\r\n251\r\n')
sage: P._get()
(False, '')
sage: 

The output from factor(2^250-1) should be:
sage: factor(2^250-1)
3 * 11 * 31 * 251 * 601 * 1801 * 4051 * 229668251 * 269089806001 * 4710883168879506001 * 5519485418336288303251

Any idea why it is dropping off chars left and right?


---

Comment by was created at 2006-12-08 01:31:33

Resolution: fixed


---

Comment by was created at 2006-12-08 01:31:33

Input to Sage() is *not* preparsed -- you have to do it.  So 2^250 - 1
is actually just 251!!  It's "2 xor 250 minus 1".
