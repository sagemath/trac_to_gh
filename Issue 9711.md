# Issue 9711: sagenb notebook -- error when downloading worksheets in some cases involving non-ASCII characters

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-08-09 21:20:23

Assignee: jason, was

CC:  ppurka jason kini

I hope this traceback from the serverlog on prep.sagenb.org will help me to debug and fix this:

```

2010-08-09 14:11:02-0700 [-] Exception rendering:
2010-08-09 14:11:02-0700 [-] Unhandled Error
        Traceback (most recent call last):          File "/usr/local/sage-prep/local/lib/python/threading.py", line 497, in __bootstrap
            self.__bootstrap_inner()
          File "/usr/local/sage-prep/local/lib/python/threading.py", line 525, in __bootstrap_inner            self.run()
          File "/usr/local/sage-prep/local/lib/python/threading.py", line 477, in run
            self.__target(*self.__args, **self.__kwargs)
        --- <exception caught here> ---
          File "/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/threadpool.py", line 210, in _worker
            result = context.call(ctx, function, *args, **kwargs)
          File "/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/context.py", line 59, in callWithContext
            return self.currentContext().callWithContext(ctx, func, *args, **kw)
          File "/usr/local/sage-prep/local/lib/python2.6/site-packages/twisted/python/context.py", line 37, in callWithContext
            return func(*args,**kw)
          File "/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/notebook/twist.py", line 1448, in f
            notebook.export_worksheet(worksheet.filename(), sws_filename)
          File "/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/notebook/notebook.py", line 983, in export_work
sheet
            S.export_worksheet(username, id_number, output_filename, title=title)
          File "/usr/local/sage-prep/sagenb-0.8.p2/src/sagenb/sagenb/storage/filesystem_storage.py", line 362, in ex
port_worksheet
            open(worksheet_txt,'w').write(old_heading + open(worksheet_html).read())
        exceptions.UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 180: ordinal not in range(12
8)
```



---

Attachment

Wraps the arguments of the write call in an encoded_str() call.


---

Comment by timdumol created at 2010-08-19 12:59:45

Changing status from new to needs_review.


---

Comment by timdumol created at 2010-08-19 12:59:45

I have been unable to replicate the issue, even with rather exotic unicode characters (in the title and the body), but this should fix any possible problems (hopefully).


---

Comment by jdemeyer created at 2012-07-27 20:42:33

Please fill in your real name as Author.


---

Comment by timdumol created at 2012-07-28 04:11:24

I think this should be closed. Codec related issues should be long gone, especially with the internationalization changes that have occurred since this.


---

Comment by kcrisman created at 2013-06-11 16:52:25

If this is still valid, [the relevant code](https://github.com/sagemath/sagenb/blob/master/sagenb/storage/filesystem_storage.py#L462) has changed slightly, so this wouldn't apply.  Also, we should probably create a pull request.

Or, as Tim suggests, if not, we could indeed close this.  It's unfortunate William didn't attach a sample sws :(  I'd go with Tim, though I think that we should have at least one current sagenb guru also confirm his statement.


---

Comment by kcrisman created at 2013-06-11 16:52:25

Changing status from needs_review to needs_info.


---

Comment by jason created at 2013-06-11 16:58:48

I know I fixed a lot of issues involving errors like this last year.


---

Comment by slelievre created at 2016-08-30 13:57:18

This is now
[SageNB issue 410: Downloading worksheets can fail with non-ASCII characters](https://github.com/sagemath/sagenb/issues/410)


---

Attachment


---

Comment by embray created at 2018-08-14 17:16:07

Resolution: worksforme


---

Comment by embray created at 2018-08-14 17:16:07

Appears to be fixed in SageNB; see the upstream issue.
