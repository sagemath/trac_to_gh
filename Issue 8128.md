# Issue 8128: UnicodeDecodeError with %latex

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-30 02:47:31

Assignee: was

CC:  jhpalmieri robert.marik mvngu

With the SageNB spkg at #8051, evaluating a cell

```
%latex
č
```

raises

```python
[...]
  File "/opt/sage-4.3.1/local/lib/python2.6/site-packages/sage/misc/latex.py", line 786, in eval
    O.write(x.encode('utf-8'))
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc4 in position 0: ordinal not in range(128) 
```


See [sage-notebook](http://groups.google.com/group/sage-notebook/browse_thread/thread/44c237cc11e9b422).


---

Comment by mpatel created at 2010-01-30 02:57:13

Encode just once, if it's necessary.  Apply to *sage* repository.


---

Attachment

The patch uses the recently added (cf. #7249, #8051) `sagenb.misc.encoded_str` to avoid attempting to re-encode encoded strings.

I haven't tested this extensively, but it appears to fix the problem above.


---

Comment by mpatel created at 2010-01-30 03:00:55

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-30 03:41:28

From `sagenb.misc.misc`:

```python
def encoded_str(obj, encoding='utf-8'):
    if isinstance(obj, unicode):
        return obj.encode(encoding, 'ignore')
    return str(obj)

def unicode_str(obj, encoding='utf-8'):
    if isinstance(obj, str):
        return obj.decode(encoding, 'ignore')
    elif isinstance(obj, unicode):
        return obj
    return unicode(obj)
```



---

Comment by jhpalmieri created at 2010-01-30 04:53:29

I haven't tested it extensively either, but it looks okay. See #8083 for a related notebook issue and #8130 for a related command-line issue.


---

Comment by robert.marik created at 2010-01-31 00:46:08

Seems good, works for me. Tested on the top of #8051


---

Comment by robert.marik created at 2010-01-31 00:46:08

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-05 00:35:33

Just a quick note: This is for the sage repository.


---

Comment by mpatel created at 2010-02-11 14:38:59

Resolution: fixed
