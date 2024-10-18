from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication([])  # Create the QApplication instance

#  Create a QWidget instance
window = QWidget()
window.setWindowTitle("Hello, World!")

#  Create a QLabel instance
label = QLabel("Hello, World!", window)
label.move(60, 15)

#  Show the window
window.show()
 
# Start the event loop
app.exec()