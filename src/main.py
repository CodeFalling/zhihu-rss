__author____author__ = 'yuwei'

from PyQt5.QtCore import QObject

from src.control import add, sign, listview
from src.util.my_pyqt import MyApp, set_button
from src.util.const import MAIN_QML_DIR, SIGN_QML_DIR, ADD_QML_DIR
from src.util.error import ErrorDialog


def on_noticer_click(listview_item):
    _my_app.noticers1_listview.setProperty("currentIndex", listview_item.getProperty("index"))


def set_views():
    root_view = _my_app.root_view

    set_button(root_view, 'sign_button', lambda: sign.show_sign_dialog(_my_app, SIGN_QML_DIR))
    set_button(root_view, 'home_button')
    set_button(root_view, 'add_button', lambda: add.show_add_dialog(_my_app, ADD_QML_DIR, ErrorDialog()))
    set_button(root_view, 'remind_button')

    _my_app.web_view = root_view.findChild(QObject, 'web_view')

    listview.load_noticers_listview(_my_app)


def set_content(root_context):
    feedslist_dic = {"yuwei": ["yuwei1", "yuwei 在 2015-07-20 16:59:06 赞同了问题\n"
                                         " 通过旅行去了解对方是怎样的一种体验？", "yuweasdfasdfi3"],
                     "采铜": ["caitasdfsadong1", "caitong2", "caitong3"],
                     "7sDream": ["1", "2", "3"]}
    root_context.setContextProperty("feedslist_dic", feedslist_dic)
    root_context.setContextProperty("current_noticer", None)


if __name__ == '__main__':
    _my_app = MyApp(qml=MAIN_QML_DIR, set_content=set_content)

    set_views()

    MyApp.run(_my_app)
