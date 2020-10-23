#!/usr/bin/env python3

import os
import shutil
import time
import logging
import watchdog.events as we
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.events import FileSystemEventHandler


# windows
root_base = 'C:\\Users\\<username>\\Documents\\Programming\\'
mimic_base = "<drive-letter:\\Programming\\"


class Mimicker(FileSystemEventHandler):
    def on_any_event(self, event):
        print(event)
        # shutil.copytree(src, dest, dirs_exist_ok=True)
        return super().on_any_event(event)
    
    def on_created(self, event):
        if type(event) == we.DirCreatedEvent:
            dir_path = event.src_path.replace(root_base, '').split('\\')
            
            current_dir = ''
            for sub_dir in dir_path:
                check_dir = os.listdir(os.path.join(mimic_base, current_dir))
                if sub_dir not in check_dir:
                    shutil.copytree(os.path.join(root_base, current_dir, sub_dir), os.path.join(mimic_base, current_dir, sub_dir))
                    break
                else:
                    current_dir = os.path.join(current_dir, sub_dir)
            
            self.create_folder_tree(event)
        
        if type(event) == we.FileCreatedEvent:
            file_path = event.src_path.replace(root_base, '')
            
            src = os.path.join(root_base, file_path)
            dst = os.path.join(mimic_base, file_path)
            
            self.create_folder_tree(event)
            try:
                shutil.copy2(src, dst)
            except FileNotFoundError:
                pass
        return super().on_created(event)
    
    def create_folder_tree(self, event):
        dir_path = event.src_path.replace(root_base, '').split('\\')[:-1]
        
        current_dir = ''
        for sub_dir in dir_path:
            check_dir = os.listdir(os.path.join(mimic_base, current_dir))
            if sub_dir not in check_dir:
                shutil.copytree(os.path.join(root_base, current_dir, sub_dir), os.path.join(mimic_base, current_dir, sub_dir))
                break
            else:
                current_dir = os.path.join(current_dir, sub_dir)
        return
    
    def on_moved(self, event):
        
        return super().on_moved(event)
    
    def on_deleted(self, event):
        self.create_deleted_folder_tree(event)
        if type(event) == we.DirDeletedEvent:
            return super().on_deleted(event)
        path = event.src_path.replace(root_base, '')        
        delete_path = os.path.join(mimic_base, '~deleted', path)
        try:
            os.rename(os.path.join(mimic_base, path), delete_path)
        except FileExistsError:
            print(datetime.utcnow().strftime('%Y-%m-%d_%H:%M:%S.%f')[:-3])
        return super().on_deleted(event)

    def create_deleted_folder_tree(self, event):
        dir_path = event.src_path.replace(root_base, '~deleted\\').split('\\')
        if type(event) == we.FileDeletedEvent:
            dir_path = dir_path[:-1]
        
        current_dir = ''
        for sub_dir in dir_path:
            check_dir = os.listdir(os.path.join(mimic_base, current_dir))
            if sub_dir not in check_dir:
                try:
                    os.mkdir(os.path.join(mimic_base, current_dir, sub_dir))
                except FileExistsError:
                    pass
            else:
                current_dir = os.path.join(current_dir, sub_dir)
        return True

def main():
    os.chdir(root_base)
    
    path = os.getcwd()
    event_handler = Mimicker()
    handler = Observer()
    handler.schedule(event_handler, path, recursive=True)
    handler.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        handler.stop()
    handler.join()


if __name__ == "__main__":
    main()
