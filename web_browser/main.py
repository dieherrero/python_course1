import sys
import os
import json
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class AddressBar(QLineEdit):
    def __init__(self):
        super().__init__()

    def mousse_press_event(self, e):
        self.selectAll()


class Application(QFrame):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Web Browser")
        self.create_app()
        self.resize(1366, 766)
        self.show()

    def create_app(self):
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)
        toolbar_layout = QHBoxLayout()

        # Create tabs
        tab_bar = QTabBar(movable=True, tabsClosable=True)
        tab_bar.tabCloseRequested.connect(self.close_tab)
        tab_bar.tabBarClicked.connect(self.switch_tab)
        tab_bar.setCurrentIndex(0)
        tab_bar.setDrawBase(False)
        tab_bar.setLayoutDirection(Qt.LeftToRight)
        tab_bar.setElideMode(Qt.ElideLeft)
        self.tab_count = 0
        self.tabs = []

        #NAV buttons
        back_button = QPushButton("<")
        back_button.clicked.connect(self.go_back)

        forward_button = QPushButton(">")
        forward_button.clicked.connect(self.go_forward)

        reload_button = QPushButton("F5")
        reload_button.clicked.connect(self.go_reload)

        # Create address bar
        toolbar = QWidget()
        address_bar = AddressBar()
        address_bar.returnPressed.connect(self.browse_to)
        toolbar.setLayout(toolbar_layout)

        # New tab button
        add_tab_button = QPushButton("+")
        add_tab_button.clicked.connect(self.add_tab)

        # adding buttons, toolbar buttons positioning
        toolbar_layout.addWidget(back_button)
        toolbar_layout.addWidget(reload_button)
        toolbar_layout.addWidget(forward_button)
        toolbar_layout.addWidget(address_bar)
        toolbar_layout.addWidget(add_tab_button)

        # set main view
        container = QWidget()
        container.layout = QStackedLayout()
        container.setLayout(container.layout)

        layout.addWidget(tab_bar)
        layout.addWidget(toolbar)
        layout.addWidget(container)
        self.setLayout(layout)

        # save objects in class
        self.tab_bar = tab_bar
        self.container = container
        self.address_bar = address_bar
        self.back_button = back_button
        self.forward_button = forward_button
        self.reload_button = reload_button

        self.add_tab()

    def close_tab(self, index):
        self.tab_bar.removeTab(index)
        self.tab_count -= 1
        self.tabs.pop(index)
        if self.tab_count > index:
            self.switch_tab(index)
        elif self.tab_count > 0:
            self.switch_tab(index - 1)

    def switch_tab(self, index):
        if self.tab_bar.tabData(index):
            tab_name = self.tab_bar.tabData(index)["object"]
            tab_content = self.findChild(QWidget, tab_name)
            self.container.layout.setCurrentWidget(tab_content)
            new_url = tab_content.content.url().toString()
            self.address_bar.setText(new_url)

    def add_tab(self):
        index = self.tab_count
        self.tabs.append(QWidget())
        self.tabs[index].layout = QVBoxLayout()
        self.tabs[index].setObjectName("tab" + str(index))
        self.tabs[index].content = QWebEngineView()
        url = QUrl()
        url = url.fromUserInput("https://www.google.com")
        self.tabs[index].content.load(url)
        self.tabs[index].content.titleChanged.connect(lambda: self.update_tab_title(index, "title"))
        self.tabs[index].content.iconChanged.connect(lambda: self.update_tab_title(index, "icon"))
        self.tabs[index].content.urlChanged.connect(lambda: self.update_tab_title(index, "icon"))

        self.tabs[index].layout.addWidget(self.tabs[index].content)
        self.tabs[index].setLayout(self.tabs[index].layout)

        self.container.layout.addWidget(self.tabs[index])
        self.container.layout.setCurrentWidget(self.tabs[index])

        self.tab_bar.addTab("New tab")
        self.tab_bar.setTabData(index, {"object": "tab" + str(index), "initial": index})
        self.tab_bar.setCurrentIndex(index)
        self.tab_count += 1

    def browse_to(self):
        text = self.address_bar.text()
        index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(index)["object"]
        tab_content = self.findChild(QWidget, tab_name)

        if "http" not in text:
            if "." not in text:
                url = "https://www.google.com/search?q=" + text
            else:
                url = "http://" + text
        else:
            url = text

        tab_content.content.load(QUrl().fromUserInput(url))

    def update_tab_title(self, index, type):
        tab_name = self.tabs[index].objectName()
        tab_content = self.findChild(QWidget, tab_name)
        title = tab_content.content.title()
        current_tab = self.tab_bar.tabData(self.tab_bar.currentIndex())["object"]

        count = 0

        if current_tab == tab_name and type == "url":
            new_url = self.findChild(QWidget, tab_name).content.url().toString()
            self.address_bar.setText(new_url)
            return False

        while True:
            if count >= self.tab_count:
                break
            tab_data_name = self.tab_bar.tabData(count)["object"]

            if tab_data_name == tab_name:
                if type == "title":
                    new_title = self.findChild(QWidget, tab_name).content.title()
                    self.tab_bar.setTabText(count, new_title)
                elif type == "icon":
                    new_icon = self.findChild(QWidget, tab_name).content.icon()
                    self.tab_bar.setTabIcon(count, new_icon)
                break
            count += 1

    def go_back(self):
        active_index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.back()

    def go_forward(self):
        active_index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.forward()

    def go_reload(self):
        active_index = self.tab_bar.currentIndex()
        tab_name = self.tab_bar.tabData(active_index)["object"]
        tab_content = self.findChild(QWidget, tab_name).content

        tab_content.reload()


if __name__ == '__main__':
    # Create the application instance.
    app = QApplication(sys.argv)
    window = Application()
    window.show()
    sys.exit(app.exec_())
