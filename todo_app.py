import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem, QCheckBox, QSpinBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)
        
        self.tasks = []
        
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit()
        self.priority_input = QSpinBox()
        self.priority_input.setRange(1, 5)
        self.add_button = QPushButton("Add Task")
        self.task_list = QListWidget()
        self.clear_button = QPushButton("Clear Finished Tasks")
        
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.priority_input)
        input_layout.addWidget(self.add_button)
        
        self.layout.addLayout(input_layout)
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.clear_button)
        
        self.add_button.clicked.connect(self.add_task)
        self.clear_button.clicked.connect(self.clear_finished_tasks)
        
        self.setLayout(self.layout)
    
    def add_task(self):
        task_text = self.input_field.text()
        priority = self.priority_input.value()
        if task_text:
            task = {'text': task_text, 'priority': priority, 'done': False}
            self.tasks.append(task)
            self.update_task_list()
            self.input_field.clear()
            self.priority_input.setValue(1)
    
    def update_task_list(self):
        self.tasks.sort(key=lambda x: (x['done'], x['priority']))
        self.task_list.clear()
        for task in self.tasks:
            item = QListWidgetItem()
            widget = QWidget()
            layout = QHBoxLayout()
            checkbox = QCheckBox(task['text'])
            checkbox.setChecked(task['done'])
            checkbox.stateChanged.connect(lambda state, t=task: self.mark_done(t, state))
            layout.addWidget(checkbox)
            widget.setLayout(layout)
            item.setSizeHint(widget.sizeHint())
            self.task_list.addItem(item)
            self.task_list.setItemWidget(item, widget)
    
    def mark_done(self, task, state):
        task['done'] = (state == 2)
        self.update_task_list()

    def clear_finished_tasks(self):
        self.tasks = [task for task in self.tasks if not task['done']]
        self.update_task_list()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
    
