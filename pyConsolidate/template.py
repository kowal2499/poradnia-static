#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Romek'

class Template(object):
    def __init__(self, templateFile, destinationFolder):
        self.database = {}
        self.destinationFolder = destinationFolder
        self.templateFileName = templateFile
        self.template = None

    def loadTemplate(self):
        f = None
        try:
            f = open(self.templateFileName, "r")
            buffer = f.readlines()

        except IOError:
            print "error opening: '" + self.templateFileName + "', exiting."
            return 0

        finally:
            if (f):
                f.close()
        self.template = (''.join(buffer)).decode('utf8')

    def run(self):
        for filee in self.database.keys():
            try:
                outputFile = open(self.destinationFolder + filee, "w")
                resultStr = self.template
                for id, content in enumerate(self.database[filee]):
                    resultStr = resultStr.replace(u"<!--arg" + unicode(id) + u"-->", content)
                outputFile.write(resultStr.encode('utf8'))
                outputFile.close()
            except IOError:
                print "error during IO operation with " + filee + ", exiting"
                return 0
            print "success with: " + filee
