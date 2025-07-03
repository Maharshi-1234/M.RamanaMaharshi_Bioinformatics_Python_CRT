#1)GUI Layout
#2)Input validation
#3)SNP Highlighting Color
#4)SNP ScatterPlot
'''
Literature Survey
Existing Systems
Proposed Systems
Dataflow Diagram
Application launch
Testing
'''
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QMessageBox
from PyQt5.QtGui import QTextCharFormat, QColor
import sys
import matplotlib.pyplot as plt

class SNPVisualizer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bioinformatics SNP Mutation Visualizer")
        self.setGeometry(100, 100, 800, 500)

        layout = QVBoxLayout()

        self.ref_input = QTextEdit()
        self.ref_input.setPlaceholderText("Enter reference DNA sequence...")
        layout.addWidget(QLabel("Reference Sequence"))
        layout.addWidget(self.ref_input)

        self.mut_input = QTextEdit()
        self.mut_input.setPlaceholderText("Enter mutated DNA sequence...")
        layout.addWidget(QLabel("Mutant Sequence"))
        layout.addWidget(self.mut_input)

        self.compare_btn = QPushButton("Compare SNPs")
        self.compare_btn.clicked.connect(self.compare_snps)
        layout.addWidget(self.compare_btn)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        layout.addWidget(QLabel("SNP Visualization"))
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def compare_snps(self):
        ref = self.ref_input.toPlainText().strip().upper()
        mut = self.mut_input.toPlainText().strip().upper()

        # Input validation
        if not ref or not mut:
            QMessageBox.warning(self, "Input Error", "Please enter both sequences.")
            return
        if len(ref) != len(mut):
            QMessageBox.warning(self, "Length Mismatch", "Sequences must be of the same length.")
            return

        # Clear result display
        self.result_display.clear()

        format_default = QTextCharFormat()
        format_default.setForeground(QColor("black"))

        format_snp = QTextCharFormat()
        format_snp.setForeground(QColor("red"))

        cursor = self.result_display.textCursor()

        snp_positions = []

        for i in range(len(ref)):
            if ref[i] == mut[i]:
                cursor.setCharFormat(format_default)
            else:
                cursor.setCharFormat(format_snp)
                snp_positions.append(i + 1)
            cursor.insertText(mut[i])

        self.result_display.setTextCursor(cursor)

        # Show SNP scatterplot
        if snp_positions:
            plt.figure(figsize=(8, 2))
            plt.scatter(snp_positions, [1] * len(snp_positions), color='red')
            plt.title('SNP Position Scatter Plot')
            plt.xlabel('Position in Sequence')
            plt.yticks([])
            plt.grid(True, axis='x')
            plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = SNPVisualizer()
    viewer.show()
    sys.exit(app.exec_())