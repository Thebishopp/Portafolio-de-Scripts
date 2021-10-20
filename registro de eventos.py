# import time module, Observer, FileSystemEventHandler
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import RegexMatchingEventHandler


class OnMyWatch:
    watchDirectory = "//??/??"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(
            event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class ScanFolder:
    'Class defining a scan folder'

    def __init__(self, path):
        self.path = path
        # key = document label   value = Document reference
        self.documents = dict("*.jpg")
        self.event_handler.on_any_event = self.on_any_event
        self.observer = Observer()
        self.observer.schedule(self.event_handler, self.path, recursive=False)
        self.observer.start()


class Handler(RegexMatchingEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            mylist = open("mylist.txt", "a")
            mylist.write("\nfile "+"'{0}'".format(event.src_path))
            mylist.close()
            print("Watchdog received created event - % s." % event.src_path)


if __name__ == '__main__':
    regexes = ["*.jpg"]
    watch = OnMyWatch()
    watch.run()
