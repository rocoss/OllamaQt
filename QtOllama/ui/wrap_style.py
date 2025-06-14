stylesheet = """
/* /////////////////////////////////////////////////////////////////////
QWidget
///////////////////////////////////////////////////////////////////// */
QWidget {
font: 14pt "sans-serif";
color:#444;
background:rgb(250,250,250);
}

/* /////////////////////////////////////////////////////////////////////
QApplication Window
///////////////////////////////////////////////////////////////////// */
QApplication::window {
padding:9px;
color: #444;
background:rgb(250,250,250);
}

/* /////////////////////////////////////////////////////////////////////
QTableView
///////////////////////////////////////////////////////////////////// */
QTableView {
font-size:11pt;
background-color: transparent;
selection-background-color: #7e57c2;
gridline-color:transparent;
color:rgb(91,88,190);
}
QTableView::item {
padding: 1px;
background:rgb(156,153,255);
}
QTableView::item:selected {
color: #fff;
background:rgb(23, 23, 23);
}
#tigger {
padding:8px;
}

/* /////////////////////////////////////////////////////////////////////
QPushButton
///////////////////////////////////////////////////////////////////// */
QPushButton {
background:rgb(38, 38, 38);
color:#fff;
border-radius:5px;
font-size:9pt;
min-height:20px;
min-width:70px;
padding:5px;
border:none;
}
QPushButton:hover {
background:rgb(24, 24, 24);
margin:2px 2px 0 0;
}
QPushButton:pressed {
padding:5px;
margin:0px;
background:#444;
color:#fff;
border:none;
}

/* /////////////////////////////////////////////////////////////////////
QLineEdit
///////////////////////////////////////////////////////////////////// */
QLineEdit {
border-radius:5px;
padding:8px 5px;
border:2px solid rgb(200, 200, 200);
}

/* /////////////////////////////////////////////////////////////////////
QTextEdit
///////////////////////////////////////////////////////////////////// */
QTextEdit {
border-radius:10px;
padding:6px 6px;
border:2px solid rgb(200, 200, 200);
}

/* /////////////////////////////////////////////////////////////////////
QToolTip
///////////////////////////////////////////////////////////////////// */
QToolTip{
color:#ffffff;
background-color:rgb(255,255,255);
border-radius:4px;
}

/* /////////////////////////////////////////////////////////////////////
QStatusBar
///////////////////////////////////////////////////////////////////// */
QStatusBar{
background:rgb(250,250,250);
color:palette(mid);
}

/* /////////////////////////////////////////////////////////////////////
QMenuBar
///////////////////////////////////////////////////////////////////// */
QMenuBar{
background:rgb(250,250,250);
}


/* /////////////////////////////////////////////////////////////////////
QTextEdit/QLineEdit
///////////////////////////////////////////////////////////////////// */
QTextEdit:hover,
QLineEdit:hover {
border:2px solid #444;
}
QTextEdit:focus,
QLineEdit:focus {
border:2px solid rgb(24, 24, 24);
}
/* /////////////////////////////////////////////////////////////////////////////
QComboBox/QSpinBox
///////////////////////////////////////////////////////////////////////////// */
QComboBox {
background-color: transparent;
border-radius:5px;
padding: 6px;
text-align:center;
}
QSpinBox:hover,
QComboBox:hover {
border-radius:5px;
border:1px solid #181818;
}

/* /////////////////////////////////////////////////////////////////////
QMenu
///////////////////////////////////////////////////////////////////// */
QMenuBar::item{
spacing:2px;
padding:3px 4px;
background:transparent;
}
QMenuBar::item:selected{
background-color:#fff;
}
QMenuBar::item:pressed{
background-color:#fff;
}
QMenu{
background-color:#fff;
}
QMenu::item{
background-color:#fff;
padding:3px 25px 3px 25px;
}
QMenu::item:disabled{
background-color:#fff;
}
QMenu::item:selected{
border-color:rgba(147,191,236,127);
}
QMenu::icon:checked{
background-color:#ff446f;
border-radius:2px;
}
QMenu::separator{
height:1px;
margin-left:5px;
margin-right:5px;
}
QMenu::indicator{
width:18px;
height:18px;
}

/* /////////////////////////////////////////////////////////////////////
ToolBar
///////////////////////////////////////////////////////////////////// */
QToolBar::top{
background-color:rgb(255,255,255);

}
QToolBar::bottom{
background-color:rgb(255,255,255);

}
QToolBar::left{
background-color:rgb(255,255,255);

}
QToolBar::right{
background-color:rgb(255,255,255);

}

/* /////////////////////////////////////////////////////////////////////
QMainWindow::separator
///////////////////////////////////////////////////////////////////// */
QMainWindow::separator{
width:6px;
height:5px;
padding:2px;
}

/* /////////////////////////////////////////////////////////////////////
QSplitter
///////////////////////////////////////////////////////////////////// */
QSplitter::handle:horizontal{
width:10px;
}
QSplitter::handle:vertical{
height:10px;
}

/* /////////////////////////////////////////////////////////////////////
QMainWindow::separator
///////////////////////////////////////////////////////////////////// */
QMainWindow::separator:hover,QSplitter::handle:hover{
background:rgb(255,255,255);
}
QDockWidget::title{
padding:4px;
background-color:rgb(255,255,255);
border-bottom:2px solid rgba(25,25,25,75);
}
QDockWidget::close-button,QDockWidget::float-button{
subcontrol-position:top right;
subcontrol-origin:margin;
position:absolute;
top:3px;
bottom:0px;
width:20px;
height:20px;
}
QDockWidget::close-button{
right:3px;
}
QDockWidget::float-button{
right:25px;
}
/*QGroupBox{
background-color:rgba(66,66,66,50%);
margin-top:27px;
border:1px solid rgba(25,25,25,127);
border-radius:4px;
}
QGroupBox::title{
subcontrol-origin:margin;
subcontrol-position:left top;
padding:4px 6px;
margin-left:3px;
background-color:qlineargradient(x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));
border:1px solid rgba(25,25,25,75);
border-bottom:2px solid rgb(127,127,127);
border-top-left-radius:4px;
border-top-right-radius:4px;
}*/

/* /////////////////////////////////////////////////////////////////////
Tab Widget
///////////////////////////////////////////////////////////////////// */
QTabWidget::pane{
background-color:rgba(66,66,66,50%);
border-top:1px solid rgba(25,25,25,50%);
}
QTabWidget::tab-bar{
left:3px;
top:1px;
}
QTabBar{
background-color:transparent;
qproperty-drawBase:0;
border-bottom:1px solid rgba(25,25,25,50%);
}
QTabBar::tab{
padding:4px 6px;
background-color:qlineargradient(x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));
border:1px solid rgba(25,25,25,75);
border-top-left-radius:4px;
border-top-right-radius:4px;
}
QTabBar::tab:selected,QTabBar::tab:hover{
background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(53,53,53,127),stop:1 rgba(66,66,66,50%));
border-bottom-color:rgba(66,66,66,75%);
}
QTabBar::tab:selected{
border-bottom:2px solid palette(highlight);
}
QTabBar::tab::selected:disabled{
border-bottom:2px solid rgb(127,127,127);
}
QTabBar::tab:!selected{
margin-top:2px;
}
QTabBar::close-button {
image:url(:/darkstyle/icon_close.png);
border:1px solid transparent;
border-radius:2px;
}
QTabBar::close-button:hover {
background-color:qlineargradient(x1:0,y1:0,x2:0,y2:1,stop:0 rgba(106,106,106,255),stop:1 rgba(106,106,106,75));
border:1px solid palette(base);
}
QTabBar::close-button:pressed {
background-color:qlineargradient(x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));
border:1px solid palette(base);
}

QRadioButton::indicator{
width:18px;
height:18px;
}
QRadioButton::indicator:checked{
image:url(:/darkstyle/icon_radiobutton_checked.png);
}
QRadioButton::indicator:checked:pressed{
image:url(:/darkstyle/icon_radiobutton_checked_pressed.png);
}
QRadioButton::indicator:checked:disabled{
image:url(:/darkstyle/icon_radiobutton_checked_disabled.png);
}
QRadioButton::indicator:unchecked{
image:url(:/darkstyle/icon_radiobutton_unchecked.png);
}
QRadioButton::indicator:unchecked:pressed{
image:url(:/darkstyle/icon_radiobutton_unchecked_pressed.png);
}
QRadioButton::indicator:unchecked:disabled{
image:url(:/darkstyle/icon_radiobutton_unchecked_disabled.png);
}
QTreeView, QTableView{
alternate-background-color:palette(window);
background:palette(base);
}
QTreeView QHeaderView::section, QTableView QHeaderView::section{
background-color:qlineargradient(x1:0,y1:1,x2:0,y2:0,stop:0 rgba(25,25,25,127),stop:1 rgba(53,53,53,75));
border-style:none;
border-bottom:1px solid palette(dark);
padding-left:5px;
padding-right:5px;
}
QTreeView::item:selected:disabled, QTableView::item:selected:disabled{
background:rgb(80,80,80);
}
QTreeView::branch{
background-color:palette(base);
}
QTreeView::branch:has-siblings:!adjoins-item{
border-image:url(:/darkstyle/icon_vline.png) 0;
}
QTreeView::branch:has-siblings:adjoins-item{
border-image:url(:/darkstyle/icon_branch_more.png) 0;
}
QTreeView::branch:!has-children:!has-siblings:adjoins-item{
border-image:url(:/darkstyle/icon_branch_end.png) 0;
}
QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings{
border-image:none;
image:url(:/darkstyle/icon_branch_closed.png);
}
QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings{
border-image:none;
image:url(:/darkstyle/icon_branch_open.png);
}
/* ////////////////////////////////////////////////////////////////////////////////////////////////
        QScrollBar
//////////////////////////////////////////////////////////////////////////////////////////////// */
QScrollBar:horizontal {
border: none;
background:transparent;
height: 12px;
margin: 0px 10px 0px 10px;
border-radius: 3px;
}
QScrollBar::handle:horizontal {
background:rgb(225,225,225);
min-width:24px;
border-radius: 4px
}
QScrollBar::add-line:horizontal {
border: none;
background: transparent;
width: 20px;
border-top-right-radius: 4px;
border-bottom-right-radius: 4px;
subcontrol-position: right;
subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal {
border: none;
background: transparent;
width: 20px;
border-top-left-radius: 4px;
border-bottom-left-radius: 4px;
subcontrol-position: left;
subcontrol-origin: margin;
}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal {
background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
background: transparent;
}
QScrollBar:vertical {
border: none;
background-color:transparent;
width: 12px;
margin: 10px 0px 10px 0px;
border-radius: 4px;
}
QScrollBar::handle:vertical {
background:rgb(225,225,225);
min-height: 12px;
border-radius: 4px
}
QScrollBar::add-line:vertical {
border: none;
background: transparent;
height: 20px;
border-bottom-left-radius: 4px;
border-bottom-right-radius: 4px;
subcontrol-position: bottom;
subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
border: none;
background: transparent;
height: 20px;
border-top-left-radius: 4px;
border-top-right-radius: 4px;
subcontrol-position: top;
subcontrol-origin: margin;
}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
background: transparent;
}
QSlider::handle:horizontal{
border-radius:4px;
border:1px solid rgba(225,225,225,255);
background-color:palette(alternate-base);
min-height:20px;
margin:0 -4px;
}
QSlider::handle:horizontal:hover{
background:palette(highlight);
}
QSlider::add-page:horizontal{
background:palette(base);
}
QSlider::sub-page:horizontal{
background:palette(highlight);
}
QSlider::sub-page:horizontal:disabled{
background:rgb(225,225,225);
}



"""
