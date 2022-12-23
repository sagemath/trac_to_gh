# Issue 7417: disturbing notebook resource limit

Issue created by migration from https://trac.sagemath.org/ticket/7417

Original creator: was

Original creation time: 2009-11-09 16:38:36

Assignee: boothby

The big public sagenb.org server, after a few days, often suddenly starts outputing this:


```
ILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
2009-11-09 08:33:36-0800 [twisted.web2.channel.http.HTTPFactory] Could not accept new connection (EMFILE)
```


This makes a multi-gigabyte logfile, and of course also means that the notebook is down.  This has not been observed on any other notebook server ever, I think.


---

Comment by was created at 2009-11-11 23:01:05

This is caused by:

```
        exceptions.IOError: [Errno 24] Too many open files: '/sage/sage/local/lib/python/site-packages/sagenb/data/sag
e/html/error_message.html'
        exceptions.IOError: [Errno 24] Too many open files: '/sage/sage/local/lib/python/site-packages/sagenb/data/sag
e/html/worksheet_listing.html'
        exceptions.IOError: [Errno 24] Too many open files: '/home/sage/sagenb/sage_notebook.sagenb/home/deangelo/4/wo
rksheet.html'
exceptions.IOError: [Errno 24] Too many open files: '/home/sage/sagenb/sage_notebook.sagenb/home/pablo.albacete/2/worksheet_conf.pickle'
```


Googling for this error shows that Python itself evidently has a 256 file hardcoded limit.  See, e.g., http://www.dslreports.com/forum/r21366308-Python-IOError-Errno-24-Too-many-open-files

This is regularly causing *massive* trouble on sagenb.org... when there are several dozen simultaneous users.  

This is particularly bad because it leads to data loss, since the notebook server can't save state, since it can't open files. 

This simple test program illustrates this hard limit:

```
v = []
for i in range(300):
    print i
    v.append(open('a%s'%i,'w'))
    sys.stdout.flush()
```


Output:

```
0
1
2
3
...
 	

WARNING: Output truncated!  
full_output.txt


0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59

...

199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
Traceback (click to the left for traceback)
...
IOError: [Errno 24] Too many open files: 'a253'
```



---

Comment by was created at 2009-11-11 23:05:59

A solution may be here: http://ubuntuforums.org/showthread.php?t=919340

They explain that `tempfile.mkstemp()` returns a file descriptor that *must* be explicitly closed.   They give sample code:

```
import sys
import os
import tempfile
import shutil 

for idx in range(5000):
    (outfd,outsock_path)=tempfile.mkstemp()
    print "%(outsock_path)s"%locals()
    try:
        outsock=os.fdopen(outfd,'w')
    except IOError,err:
        print "IOError:",err
        print "idx=%s"%idx
        print "Cannot write to %(outsock_path)s"%locals()
        sys.exit(1)
    outsock.close()
    os.remove(outsock_path)  
```


Since the Sage notebook now uses tempfile, maybe our problem is the same.


---

Comment by was created at 2009-11-11 23:17:23

In particular, the following fails:

```
for i in range(400):
    fd, name = tempfile.mkstemp()
```

but the following works fine:

```
for i in range(400):
    fd, name = tempfile.mkstemp()
    os.fdopen(fd,'w').close()
```


There are two places in the sagenb code where mkstemp is used:

```
misc/misc.py:        return tempfile.mkstemp()[1]
storage/filesystem_storage.py:        worksheet_txt =  tempfile.mkstemp()[1]
```


So both of these just need to be fixed to properly close the file descriptor.  Or, if safe, instead use `tempfile.mktemp()`, which doesn't make a file descriptor. 
 
Anyway, this is a *huge* bug which will bring down any notebook server eventually so must be fixed for sage-4.2.1.


---

Comment by was created at 2009-11-11 23:17:23

Changing priority from major to blocker.


---

Attachment


---

Comment by was created at 2009-11-11 23:26:32

Changing status from new to needs_review.


---

Comment by mpatel created at 2009-11-12 01:42:39

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2009-11-12 07:26:10

Resolution: fixed


---

Comment by mhansen created at 2009-11-12 07:26:10

I'll close this.  It is in the spkg at #7430.
