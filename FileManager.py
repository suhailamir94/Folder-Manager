import watchdog.events
import watchdog.observers
import time
import sys

from CleanFolder import CleanFolder
from util import folder_to_file_mapping


class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self, path):
        # Set the patterns for PatternMatchingEventHandler

        watchdog.events.PatternMatchingEventHandler.__init__(
            self,
            patterns=[
                "*." + ext
                for list_ext in folder_to_file_mapping.values()
                for ext in list_ext
            ],
            ignore_directories=True,
            case_sensitive=False,
        )
        self.cf = CleanFolder(path)

    def on_created(self, event):
        """Handles all safari, firefox downloads and the files created using unix commands"""

        print(f"Watchdog received {event.event_type} event - {event.src_path}.")

        # ignore temp files created by chrome while downloading a file
        if not any(
            x in event.src_path for x in ["google.Chrome", "Unconfirmed", "crdownload"]
        ):
            self.cf.move_file(event.src_path.split("/")[-1])

    def on_moved(self, event):
        """Handles all Google Chrome downloads"""

        print(f"Watchdog received {event.event_type} event - {event._dest_path}.")

        # ignore temp files created by chrome while downloading a file
        if not any(
            x in event._dest_path
            for x in ["google.Chrome", "Unconfirmed", "crdownload"]
        ):
            self.cf.move_file(event._dest_path.split("/")[-1])


if __name__ == "__main__":
    if len(sys.argv) == 2:

        src_path = sys.argv[1]
        cf = CleanFolder(src_path)

        # clean up the folder while loading up the script
        cf.clean()

        event_handler = Handler(src_path)
        observer = watchdog.observers.Observer()
        observer.schedule(event_handler, path=src_path, recursive=False)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
    else:
        print("Please provide the folder path you want to clean")
