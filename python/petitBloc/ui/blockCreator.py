from Qt import QtWidgets
from Qt import QtCore


class BlockCreator(QtWidgets.QLineEdit):
    BlockCreatorEnd = QtCore.Signal(str)

    def __init__(self, parent=None, blockList=[]):
        super(BlockCreator, self).__init__(parent=parent)
        self.__block_lists = []
        self.setBlockList(blockList)
        self.editingFinished.connect(self.__editingFinished)
        self.hide()
        self.blockSignals(True)

    def leaveEvent(self, evnt):
        self.hide()

    def setBlockList(self, blockList):
        self.__block_lists = blockList
        comp = QtWidgets.QCompleter(blockList)
        comp.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        comp.setModelSorting(QtWidgets.QCompleter.CaseInsensitivelySortedModel)
        self.setCompleter(comp)

    def show(self, pos):
        self.setText("")
        self.blockSignals(False)
        self.move(pos)
        self.setFocus(QtCore.Qt.PopupFocusReason)
        super(BlockCreator, self).show()

    def __editingFinished(self):
        self.BlockCreatorEnd.emit(self.text())
        self.blockSignals(True)
        self.hide()
