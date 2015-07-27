__author____author__ = 'yuwei'

from PyQt5.QtCore import QObject

from src.control import add, listview
from src.control.change_notice_methods import show_change_dialog

from src.util.my_pyqt import MyApp, set_button, set_menu
from src.util.const import MAIN_QML_DIR, ADD_QML_DIR, CHANGE_QML_DIR
from src.util.error import ErrorDialog

from src.model.noticer import Noticer
from src.model.feeds_list import FeedsList

def on_noticer_click(listview_item):
    _my_app.noticers1_listview.setProperty("currentIndex", listview_item.getProperty("index"))


def del_noticer(root_view):
    Noticer.del_noticer(root_view)
    name = Noticer.get_current_noticer_name(root_view)
    FeedsList.del_feeds_list(name)

    listview.load_noticers_listview(root_view)


def set_views():
    root_view = _my_app.root_view

    set_button(root_view, 'add_button', lambda: add.show_add_dialog(_my_app, ADD_QML_DIR, ErrorDialog()))

    set_menu(root_view, 'change_notice_method', lambda: show_change_dialog(_my_app, CHANGE_QML_DIR))
    set_menu(root_view, 'delete_noticer', lambda: del_noticer(root_view))

    _my_app.web_view = root_view.findChild(QObject, 'web_view')

    listview.load_noticers_listview(root_view)


if __name__ == '__main__':
    _my_app = MyApp(qml=MAIN_QML_DIR)

    set_views()

    MyApp.run(_my_app)
