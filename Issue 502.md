# Issue 502: pexpect -- optimize; maybe update to newest version?

Issue created by migration from https://trac.sagemath.org/ticket/502

Original creator: was

Original creation time: 2007-08-28 21:07:42

Assignee: was

pexpect is at version 2.1, but SAGE uses 2.0.  Investigate why 2.1 is so much slower.
Also, speed everything up more.  Says dropdrive on irc:

```

13:53 < dropdrive> was_: I looked into the pipes being slow thing, and Pexpect is just horrible with large amounts of data
                   (O(n^2)).  I made a fix (O(n)) that reads 6MB/s.  But pexpect will always be slow if you have to call
                   .expect many times (twice per line as it stands), because pexpect slices its buffer every time.
13:55 < dropdrive> was_: So if you read a 4096-byte block from a pipe, and .expect gets called every 80 characters,
                   pexpect will build buffer[80*n:] for n from 1 to 50


```



---

Comment by mabshoff created at 2007-08-31 23:49:05

From dropdrive:

```
Benchmarks with improved Pexpect
================================

sage: n, s = 8, '$sage1'
sage: P = partitions_set(range(n), 3)
sage: timeit p = gap.get(s, use_file=True).replace(r'\n', '')
10 loops, best of 3: 240 ms per loop
sage: timeit q = gap.get(s, use_file=False).replace(r'\n', '')
10 loops, best of 3: 444 ms per loop
sage: timeit r = gap.get(s, use_file='dropdrive')
10 loops, best of 3: 22 ms per loop
sage:

sage: n, s = 10, '$sage1'
sage: P = partitions_set(range(n), 3)
sage: timeit p = gap.get(s, use_file=True).replace(r'\n', '')
10 loops, best of 3: 582 ms per loop
sage: timeit r = gap.get(s, use_file='dropdrive')
10 loops, best of 3: 206 ms per loop
sage:

sage: n, s = 12, '$sage1'
sage: P = partitions_set(range(n), 3)
sage: timeit p = gap.get(s, use_file=True).replace(r'\n', '')
10 loops, best of 3: 1.76 s per loop
sage: timeit r = gap.get(s, use_file='dropdrive')
10 loops, best of 3: 2.08 s per loop
sage:


Intro
##### We improve Pexpect performance when expecting large amounts of
data.  Many interfaces have a maxread of 100000 or higher.
However, os.read (almost?) always returns strings that are 8 KB or
less, though this may be platform-dependent.  So don't think that
increasing maxread will increase performance!

Regardless of version, Pexpect performance is poor when we expect
large amounts of data.  The problem is that the running time of
pexpect.spawn.expect_list is O(N^2) where N is the number of bytes
received, because of os.read (see above).  This is actually
theoretically optimal if we want to "expect" arbitrary regexps.
However, SAGE mostly "expect"s very simple regexps, i.e., prompts
(Expect._prompt).

I have written a variant of pexpect.spawn.expect called
pexpect.spawn.bounded_expect, which takes "bounded patterns": a tuple
(E, B) such that

(1) E is a basestring or regexp and B is an integer, and 

(2) E is never expected to match a string longer than B.

(See docstring for more.)

This is certainly reasonable if we are expecting prompts.  The running
time of pexpect.spawn.bounded_expect is O(N).

Without the call to time.sleep, pexpect.spawn.bounded_expect can
process 30,468,021 bytes (one "expect" call) in 4.63 seconds (wall
time), under Linux on a Xeon 3.0ghz.


time.sleep
==========

Pexpect version 2.1 includes calls to time.sleep between successive
os.read calls.  I think this to get more data per os.read call.


Enhancements
============

Both pexpect.spawn.expect and pexpect.spawn.bounded_expect can be made
faster by implementing a "greedy" version of
pexpect.spawn.read_nonblocking if either of the following hold:

(1) We can bound the size of the "before" string (i.e., not the
"expect" string) on a per-call basis, or

(2) The size of the "after" string is small.

A method greedy_read_nonblocking is included in the patch below.
Off-the-cuff tests show that the speed gain is minimal.  If we really
care about speed then a pure Python expect module isn't the way to go
anyway.


Implementation in SAGE
======================

This patch adds only pexpect.spawn.bounded_expect and three helper
methods to pexpect.spawn in pexpect.py.  The Pexpect module is
otherwise unaffected.  To use in SAGE, I suggest that the calls to
pexpect.spawn.expect that wait for prompts (mostly in
interfaces/expect.py) to be replaced by calls to
pexpect.spawn.bounded_expect.  Interfaces can have a maxpromptlen
attribute, a length such as 100 can be hard-coded in
Expect._eval_line, or some clever way of calculating the prompt length
based on the prompt's regexp.

Ugly demonstration of implementation in SAGE's GAP interface (see
benchmarks for sample use):

In interfaces.gap.Gap:

def get(self, var, use_file=False):
    """
    Get the string representation of the variable var.
    """
    if use_file == 'dropdrive':
        E = self._expect
        E.sendline('Print(%s);' % var)
        E.bounded_expect(('@ngap> @i', 9))
        return ''.join(E.before.split('@J@n')[1:])
    if use_file:
        if os.path.exists(tmp):
            os.unlink(tmp)
        self.eval('PrintTo("%s", %s);'%(tmp,var), strip=False)
        r = open(tmp).read()
        r = r.strip().replace("\\\n","")
        os.unlink(tmp)
        return r
    else:
        return self.eval('%s;'%var, newlines=False)


Patch
##### The below patch is against pexpect.py in Pexpect version 2.1.


--- /tmp/pexpect-2.1/pexpect.py	2006-05-31 23:07:48.000000000 -0400
+++ pexpect.py	2007-08-30 22:01:19.000000000 -0400
 -620,6 +620,36 @@
         # and blocked on some platforms. TCSADRAIN is probably ideal if it worked.
         termios.tcsetattr(self.child_fd, termios.TCSANOW, new)
     
+    def greedy_read_nonblocking(self, timeout=-1, patience=0.001, recover=0.001):
+
+        """Repeatedly yield data read from spawn.read_nonblocking
+        until either (a) the amount of time elapsed is at least
+        <timeout> or (b) a spawn.read_nonblocking call takes longer
+        than than <patience> or time left until timeout.  Set
+        <timeout> to None to make it effectively infinite.  Sleep for
+        <recover> seconds between reads in hopes of getting more data
+        per os.read.
+
+        Performance may depend on finding good values for <patience>
+        and <recover>.
+
+        """
+        if timeout == -1:
+            timeout = self.timeout
+        if timeout is None:
+            timeout = 99999999 # 3.2 years, or, never time out
+        end_time = time.time() + timeout
+        while True:
+            try:
+                yield self.read_nonblocking(self.maxread, min(timeout, patience))
+            except TIMEOUT:
+                break
+            timeout = end_time - time.time()
+            if not timeout > 0:
+                break
+            if recover > 0:
+                time.sleep(recover)
+
     def read_nonblocking (self, size = 1, timeout = -1):
         """This reads at most size characters from the child application.
         It includes a timeout. If the read does not complete within the
 -1148,6 +1178,184 @@
             self.match_index = None
             raise
 
+    def bounded_expect(self, pattern, timeout=-1):
+
+        """Same as spawn.expect, but expect exceptions (TIMEOUT and
+        EOF) and *bounded* patterns.  A bounded pattern is a
+        (basestring, integer) or (regexp, integer) tuple where the
+        pattern is not expected to match a string longer than the
+        integer (e.g. prompts).
+
+        Use this for performance gain if self.before is expected to be
+        large.  This method only searches through newly-received data
+        and not the entire existing buffer, as spawn.expect does.
+        This method also does not suffer from the Python deadly sin of
+        building increasingly longer strings by adding, e.g. s = a + b
+        + c + d + e + f.  (See the line "incoming = incoming + c" in
+        spawn.expect.)
+
+        Sample usage:
+
+        E.bounded_expect([('@ngap> @i', 9), ('>>> ', 4), EOF])
+
+        In the interests of performace, regular patterns are not
+        allowed.
+
+        Unlike spawn.expect, there is no <searchwindowsize> parameter
+        because bounded patterns are, well, bounded.
+
+        """
+        compiled_bounded_pattern_list = list(self._compile_bounded_patterns(pattern))
+        return self._bounded_expect_list(compiled_bounded_pattern_list, timeout)
+
+    def _compile_bounded_patterns(self, patterns):
+
+        """Basically copied from spawn.compile_pattern_list, but
+        written as an iterator.  The end-user shouldn't use this!
+
+        """
+        try:
+            len(patterns)
+        except TypeError:
+            patterns = [patterns]
+        else:
+            if len(patterns) == 2 \
+                    and isinstance(patterns[0], (basestring, type(re.compile('')))) \
+                    and isinstance(patterns[1], int):
+                patterns = [patterns]
+
+        compile_flags = re.DOTALL
+        if self.ignorecase:
+            compile_flags = compile_flags | re.IGNORECASE
+
+        num_bounded = 0
+        for p in patterns:
+            if p in (EOF, TIMEOUT):
+                yield p
+            else:
+                try:
+                    if len(p) == 2:
+                        num_bounded += 1
+                        yield (re.compile(p[0], compile_flags), int(p[1]))
+                    else:
+                        raise TypeError
+                except TypeError, ValueError:
+                    raise TypeError, "%r is not a bounded pattern" % p
+
+        if not num_bounded:
+            raise ValueError, "Must have at least one bounded pattern!"
+
+    def _bounded_expect_list(self, pattern_list, timeout = -1):
+
+        """Copied from spawn.expect_list, but optimized for use with
+        bounded patterns; see spawn.bounded_expect for details.  The
+        end-user shouldn't use this!
+
+        """
+        self.patterns = pattern_list
+
+        if timeout == -1:
+            timeout = self.timeout
+        if timeout is not None:
+            end_time = time.time() + timeout 
+
+        max_bound = max(pattern[1] for pattern in pattern_list if isinstance(pattern, tuple))
+
+        incoming = [self.buffer]
+        try:
+            while True: # Keep reading until exception or return.
+                if len(incoming) == 1: # no reads yet
+                    search_chunks = [self.buffer]
+                    search_string = ''
+                else: # last element of incoming hasn't been searched
+                    gnimocni = reversed(incoming)
+                    needed = max_bound - 1
+                    chunks = [gnimocni.next()[:needed]]
+                    for chunk in gnimocni:
+                        if needed > 0:
+                            if len(chunk) < needed:
+                                chunks.append(chunk)
+                                needed -= len(chunk)
+                            else:
+                                chunks.append(chunk[-needed:])
+                                break
+                    search_chunks = list(reversed(chunks))
+                    search_string = incoming[-1]
+
+                for idx, pattern in enumerate(pattern_list):
+                    if pattern in (EOF, TIMEOUT):
+                        continue # PexpectExceptions are handled differently.
+                    cre, bound = pattern
+
+                    match = cre.search(''.join(search_chunks), max_bound - bound)
+                    if match is not None:
+                        before_chunks = incoming[:-len(search_chunks)]
+                        before_chunks.append(incoming[-len(search_chunks)][:-len(search_chunks[-1])])
+                        before_chunks.append(match.string[:match.start()])
+                        self.before = ''.join(before_chunks)
+                        self.after = match.group()
+                        # I'd like to use buffers here, but can't if
+                        # we want to behave as in spawn.expect_list
+                        self.buffer = match.string[match.end():]
+                        self.match = match
+                        self.match_index = idx
+                        # assert (self.before + self.after + self.buffer) == ''.join(incoming)
+                        return self.match_index
+
+                    # no "overlapped" match; search the new thing
+                    match = cre.search(search_string)
+                    if match is not None:
+                        incoming[-1] = incoming[-1][:match.start()]
+                        self.before = ''.join(incoming)
+                        self.after = match.group()
+                        self.buffer = match.string[match.end():]
+                        self.match = match
+                        self.match_index = idx
+                        # assert (self.before + self.after + self.buffer) == ''.join(incoming)
+                        return self.match_index
+
+                # No match at this point
+                if timeout < 0 and timeout is not None:
+                    raise TIMEOUT ('Timeout exceeded in expect_list().')
+                # Still have time left, so read more data
+                if 1: # read and process, recommended
+                    time.sleep (0.0001)
+                    c = self.read_nonblocking (self.maxread, timeout)
+                    incoming.append(c)
+                else: # read greedily and process (not much faster)
+                    incoming.append(''.join(self.greedy_read_nonblocking(timeout)))
+                if timeout is not None:
+                    timeout = end_time - time.time()
+        except EOF, e:
+            self.buffer = ''
+            self.before = ''.join(incoming)
+            self.after = EOF
+            if EOF in pattern_list:
+                self.match = EOF
+                self.match_index = pattern_list.index(EOF)
+                return self.match_index
+            else:
+                self.match = None
+                self.match_index = None
+                raise EOF (str(e) + '\n' + str(self))
+        except TIMEOUT, e:
+            self.before = ''.join(incoming)
+            self.after = TIMEOUT
+            if TIMEOUT in pattern_list:
+                self.match = TIMEOUT
+                self.match_index = pattern_list.index(TIMEOUT)
+                return self.match_index
+            else:
+                self.match = None
+                self.match_index = None
+                raise TIMEOUT (str(e) + '\n' + str(self))
+        except Exception:
+            self.before = ''.join(incoming)
+            self.after = None
+            self.match = None
+            self.match_index = None
+            raise
+
     def getwinsize(self):
         """This returns the terminal window size of the child tty.
         The return value is a tuple of (rows, cols).
```



---

Comment by kcrisman created at 2009-12-30 04:47:37

pexpect is now in version 2.3.  We appear to still have version 2.0 (? it's hard to tell, no obvious pexpect version command).  Anyway, might upgrading render this obsolete?


---

Comment by aapitzsch created at 2014-08-18 19:38:58

Recent version of pexpect is 3.3 (http://pexpect.readthedocs.org/en/latest/index.html) which could be installed using pip. But installing this version will result in failing doctests.


---

Comment by jdemeyer created at 2015-12-04 13:59:47

Fixed by #10295.


---

Comment by jdemeyer created at 2015-12-04 13:59:47

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-12-04 14:00:01

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2015-12-04 14:00:41

Replying to [comment:3 kcrisman]:
> pexpect is now in version 2.3.  We appear to still have version 2.0 (? it's hard to tell, no obvious pexpect version command).  Anyway, might upgrading render this obsolete?

Just for information: `pexpect` seems to become _slower_ with every upgrade...


---

Comment by vbraun created at 2015-12-04 22:12:33

Resolution: duplicate
