from unittest import TestCase

from src.model.noticer import Noticer

__author__ = 'yuwei'


class TestNoticer(TestCase):
    # def test_get_noticers_in_json(self):
    #     noticer = Noticer('d', 'd', 'r', 'f')
    #
    #     noticers = Noticer.get_noticers_in_json()
    #
    #     for noticer in noticers:
    #         print(noticer)
    #     print(len(noticers))
    #
    #     Noticer.write_noticers_in_json(noticer, noticers)

    def test_get_noticer(self):
        noticer = Noticer.get_noticers(0)
