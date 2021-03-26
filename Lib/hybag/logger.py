#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ---------------------------------------------------------------------------
# Author: LiaoChenchen
# Created on: 2020/9/11 14:34
# Reference:
"""
Description:
Usage:
"""
# ---------------------------------------------------------------------------
import traceback
import sys

class TracebackMgr(object):
    
    def _get_format_trace_str(self, t, v, tb):
        _trace = traceback.format_exception(t, v, tb)
        return ' '.join(_trace)
    
    def handle_one_exception(self):
        """
        从当前栈帧或者之前的栈帧中获取被except捕获的异常信息;
        没有被try except捕获的异常会自动使用handle_traceback进行收集
        """
        t, v, tb = sys.exc_info()
        self.handle_traceback(t, v, tb, False)
    
    def handle_traceback(self, t, v, tb, is_hook = True):
        """
        将此函数替换sys.excepthook以能够自动收集没有被try...except捕获的异常，
        使用try except处理的异常需要手动调用上面的函数handle_one_exception才能够收集
        """
        trace_str = self._get_format_trace_str(t, v, tb)
        self.record_trace(trace_str, is_hook)
        print "i'm logger"
    # do something else
    
    def record_trace(self, trace_str, is_hook):
        # Do somethind
        print 'is_hook: %s' % is_hook
        print trace_str


from StringIO import StringIO
from multiprocessing import Process, Queue
import sys

# Proxy classes that both write to and capture strings
# sent to stdout or stderr, respectively.
class TeeOut(StringIO):
    def write(self, s):
        StringIO.write(self, s)
        sys.__stdout__.write(s)

class TeeErr(StringIO):
    def write(self, s):
        StringIO.write(self, s)
        sys.__stderr__.write(s)

class Parent(object):
    def run(self):
        # Start child process.
        queue = Queue()
        child = Process(target=self.spawn, args=(queue,))
        child.start()
        child.join()
        
        # Do someting with out and err...
        out = queue.get()
        err = queue.get()
    
    def spawn(self, queue):
        # Save everything that would otherwise go to stdout.
        out = TeeOut()
        sys.stdout = out
        
        err = TeeErr()
        sys.stderr = err
        
        try:
            # Do something...
            print 'out 1'
            print 'out 2'
            sys.stderr.write('error 1\n')
            print 'out 3'
            sys.stderr.write('error 2\n')
        
        finally:
            # Restore stdout, stderr and send their contents.
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            queue.put(out.getvalue())
            queue.put(err.getvalue())
