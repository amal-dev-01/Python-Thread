import threading
import time
class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print(f"Thread {self.name} started.")
        time.sleep(5    )
        print(f"Thread {self.name} finished.")

obj=MyThread("Anu")
obj.run()
