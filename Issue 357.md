# Issue 357: the help() function modules lister doesn't work

Issue created by migration from https://trac.sagemath.org/ticket/357

Original creator: was

Original creation time: 2007-04-25 15:18:07

Assignee: was


```
Ted Kosan <ted.kosan@gmail.com> 	
to sage-support
	
show details
	 8:06 am (7 minutes ago) 
Hello,

I am using sage version 2.4 and when I type "modules" within the help() function I receive the error that is included below.

Thanks,

Ted Kosan


----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.4, Release Date: 2007-03-25                         |
| Type notebook() for the GUI, and license() for information.        |
sage: help()

Welcome to Python 2.5!  This is the online help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://www.python.org/doc/tut/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, or topics, type "modules",
"keywords", or "topics".  Each module also comes with a one-line summary
of what it does; to list the modules whose summaries contain a given word
such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...

---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/home/tkosan/adocuments/mathematical_analysis_book/sage/<ipython console> in <module>()

/home/tkosan/download/sage/sage- 2.4-i686-Linux/local/lib/python/site.py in __call__(self, *args, **kwds)
    344     def __call__(self, *args, **kwds):
    345         import pydoc
--> 346         return pydoc.help(*args, **kwds)
    347
    348 def sethelper():

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pydoc.py in __call__(self, request)
   1643         else:
   1644             self.intro()
-> 1645             self.interact()
   1646             self.output.write('''
   1647 You are now leaving help and returning to the Python interpreter.

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pydoc.py in interact(self)
   1661             request = strip(replace(request, '"', '', "'", ''))
   1662             if lower(request) in ('q', 'quit'): break
-> 1663             self.help(request)
   1664
   1665     def getline(self, prompt):

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pydoc.py in help(self, request)
   1677             elif request == 'keywords': self.listkeywords()
   1678             elif request == 'topics': self.listtopics()
-> 1679             elif request == 'modules': self.listmodules()
   1680             elif request[:8] == 'modules ':
   1681                 self.listmodules(split(request)[1])

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pydoc.py in listmodules(self, key)
   1795                 if find(modname, '.') < 0:
   1796                     modules[modname] = 1
-> 1797             ModuleScanner().run(callback)
   1798             self.list(modules.keys())
   1799             self.output.write('''

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pydoc.py in run(self, callback, key, completer)
   1846                         callback(None, modname, desc)
   1847
-> 1848         for importer, modname, ispkg in pkgutil.walk_packages():
   1849             if self.quit:
   1850                 break

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pkgutil.py in walk_packages(path, prefix, onerror)
    123                 path = [p for p in path if not seen(p)]
    124
--> 125                 for item in walk_packages(path, name+'.', onerror):
    126                     yield item
    127

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pkgutil.py in walk_packages(path, prefix, onerror)
    123                 path = [p for p in path if not seen(p)]
    124
--> 125                 for item in walk_packages(path, name+'.', onerror):
    126                     yield item
    127

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python/pkgutil.py in walk_packages(path, prefix, onerror)
    108         if ispkg:
    109             try:
--> 110                 __import__(name)
    111             except ImportError:
    112                 if onerror is not None:

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python2.5/site-packages/twisted/web2/channel/__init__.py in <module>()
      5 Various backend channel implementations for web2.
      6 """
----> 7 from twisted.web2.channel.cgi import startCGI
      8 from twisted.web2.channel.scgi import SCGIFactory
      9 from twisted.web2.channel.http import HTTPFactory

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python2.5/site-packages/twisted/web2/channel/cgi.py in <module>()
      6 from twisted.internet import protocol, address
      7 from twisted.internet import reactor, interfaces
----> 8 from twisted.web2 import http, http_headers, server, responsecode
      9
     10 class BaseCGIChannelRequest(protocol.Protocol):

/home/tkosan/download/sage/sage- 2.4-i686-Linux/local/lib/python2.5/site-packages/twisted/web2/http.py in <module>()
     25 from twisted.web2 import responsecode
     26 from twisted.web2 import http_headers
---> 27 from twisted.web2 import iweb
     28 from twisted.web2 import stream
     29 from twisted.web2.stream import IByteStream

/home/tkosan/download/sage/sage-2.4-i686-Linux/local/lib/python2.5/site-packages/twisted/web2/iweb.py in <module>()
     56 IResource.__class__ = SpecialAdaptInterfaceClass
     57
---> 58 class IOldNevowResource(components.Interface):
     59     # Shared interface with inevow.IResource
     60     """

<type 'exceptions.AttributeError'>: 'module' object has no attribute 'Interface'
sage:
```



---

Comment by ncalexan created at 2007-06-27 05:47:19

As of 


```
sage: version()
 'SAGE Version 2.6, Release Date: 2007-06-02'
```


this worked fine for me.


---

Comment by ncalexan created at 2007-06-27 05:47:19

Resolution: worksforme
