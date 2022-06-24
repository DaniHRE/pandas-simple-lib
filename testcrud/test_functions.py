from pandascrud import functions

# TRUE
def testInit():
    assert functions.__init__() == True

# FALSE
def testSaveChanges():
    assert functions.saveChanges() == True