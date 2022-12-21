# Issue 6440: hg_sage.serve() is broken in 4.1.alpha1 (mainly on Mac?)

Issue created by migration from Trac.

Original creator: jhpalmieri

Original creation time: 2009-06-28 15:28:33

Assignee: cwitty

hg_sage.serve() works in Sage 4.0.2 but is broken in 4.1.alpha1.  On an Intel Mac running OS X 10.5, I see this:

```
sage: hg_sage.serve()
**************************************************
*                                                *
* Open your web browser to http://localhost:8200 *
*                                                *
**************************************************
cd "/Applications/sage/devel/sage" && hg serve --address localhost --port 8200  
127.0.0.1 - - [28/Jun/2009 08:06:08] "GET / HTTP/1.1" 200 -
sh: line 1: 47150 Bus error               hg serve --address localhost --port 8200
**************************************************
*                                                *
* Open your web browser to http://localhost:8200 *
*                                                *
**************************************************
```

Then the web page "http://localhost:8200/" is pretty broken -- see the picture "serve.png".  

On sage.math, the web page seems to work, but I get a long list of messages:

```
**************************************************                                                                                   
*                                                *                                                                                   
* Open your web browser to http://localhost:8200 *                                                                                   
*                                                *                                                                                   
**************************************************                                                                                   
cd "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/devel/sage" && hg serve --address localhost --port 8200            
127.0.0.1 - - [28/Jun/2009 08:22:50] "GET / HTTP/1.1" 200 -                                                                          
127.0.0.1 - - [28/Jun/2009 08:22:51] "GET /static/hglogo.png HTTP/1.1" 500 -                                                         
127.0.0.1 - - [28/Jun/2009 08:22:51] "GET /static/style-paper.css HTTP/1.1" 200 -                                                    
127.0.0.1 - - [28/Jun/2009 08:22:51] Exception happened during processing request '/static/hglogo.png':                              
Traceback (most recent call last):                                                                                                   
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py", line 68, in do_POST                                                                                                                                   
    self.do_write()                                                                                                                  
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py", line 61, in do_write                                                                                                                                  
    self.do_hgweb()                                                                                                                  
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/server.py", line 125, in do_hgweb                                                                                                                                 
    for chunk in self.server.application(env, self._start_response):                                                                 
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/hgweb_mod.py", line 80, in __call__                                                                                                                               
    return self.run_wsgi(req)                                                                                                        
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/hgweb_mod.py", line 182, in run_wsgi                                                                                                                              
    content = getattr(webcommands, cmd)(self, req, tmpl)                                                                             
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/webcommands.py", line 622, in static                                                                                                                              
    return [staticfile(static, fname, req)]                                                                                          
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mercurial/hgweb/common.py", line 69, in staticfile                                                                                                                                
    ct = mimetypes.guess_type(path)[0] or "text/plain"                                                                               
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py", line 242, in guess_type        
    return guess_type(url, strict)              

[many identical lines]

  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py", line 242, in guess_type
    return guess_type(url, strict)
  File "/scratch/palmieri/sage-4.1.alpha1-sage.math-only-x86_64-Linux/local/lib/python/mimetypes.py", line 242, in guess_type
    return guess_type(url, strict)
RuntimeError: maximum recursion depth exceeded
```




---

Attachment

See #6906 for apparently the solution (upgrade mercurial)


---

Comment by mhansen created at 2009-10-15 09:44:56

Resolution: fixed


---

Comment by mhansen created at 2009-10-15 09:44:56

Closed by #6906
