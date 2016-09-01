#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Romek'

def main():

    import os

    import zadania
    import artykuly

    print "\n### starting with Tasks"
    zadania = zadania.Zadania(u"_templateZadania.html", u'..' + unicode(os.sep) + u'subpages' + unicode(os.sep))
    zadania.loadTemplate()
    zadania.run()

    print "\n### starting with Articles"
    artykuly = artykuly.Artykuly(u"_templateArtykuły.html", u'..' + unicode(os.sep) + u'porady' + unicode(os.sep))
    artykuly.loadTemplate()
    artykuly.run()



if __name__ == "__main__":
    main()