# menu_creator.py
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu
from QtOllama.utility.logger_setup import create_logger

logger = create_logger(__name__)

class MenuCreator:
    """
    A class to create and manage menus for the main window.
    Methods
    -------
    __init__(main_window)
        Initializes the MenuCreator with the given main window.
    create_menus()
        Creates the menus and submenus for the main window based on the provided menu structure.
    """

    def __init__(self, main_window):
        try:
            self.main_window = main_window
            logger.info("MenuCreator initialized successfully.")
        except Exception as e:
            logger.error(f"Error constructing MenuCreator: {e}")
            raise

    def create_menus(self):
        """
        Creates the menu structure for the main window.

        This method iterates through the `menus` dictionary of the main window,
        creating the main menus, submenus, and actions dynamically. The structure
        of the `menus` dictionary should be as follows:
        
        {
            "Main Menu Name": {
                "Submenu Name": {
                    "Subsubmenu Name": ["Option1", "Option2", ...],
                    ...
                },
                ...
            },
            ...
        }

        Each option in the submenus and subsubmenus is connected to the 
        `perform_ai_analysis` method of the main window.

        Example:
        {
            "File": {
                "Open": ["Project", "File"],
                "Save": ["Project", "File"]
            },
            "Edit": {
                "Undo": [],
                "Redo": []
            }
        }
        """
        try:
            for main_menu_name, main_submenus in self.main_window.menus.items():
                main_menu = self.main_window.menuBar().addMenu(main_menu_name)
                logger.info(f"Created main menu: {main_menu_name}")
                for submenu_name, submenus in main_submenus.items():
                    if isinstance(submenus, dict):
                        submenu = main_menu.addMenu(submenu_name)
                        logger.info(f"Created submenu: {submenu_name}")
                        for subsubmenu_name, options in submenus.items():
                            subsubmenu = submenu.addMenu(subsubmenu_name)
                            logger.info(f"Created subsubmenu: {subsubmenu_name}")
                            for option in options:
                                action = QAction(option, self.main_window)
                                action.triggered.connect(
                                    lambda checked, o=option: self.main_window.perform_ai_analysis(o)
                                )
                                subsubmenu.addAction(action)
                                logger.info(f"Added action: {option} to subsubmenu: {subsubmenu_name}")
                    else:
                        submenu = main_menu.addMenu(submenu_name)
                        logger.info(f"Created submenu: {submenu_name}")
                        for option in submenus:
                            action = QAction(option, self.main_window)
                            action.triggered.connect(
                                lambda checked, o=option: self.main_window.perform_ai_analysis(o)
                            )
                            submenu.addAction(action)
                            logger.info(f"Added action: {option} to submenu: {submenu_name}")
        except Exception as e:
            logger.error(f"Error creating menus in MenuCreator: {e}")
            self.main_window.statusBar().showMessage("Failed to create menus. Check logs for details.")
            raise
