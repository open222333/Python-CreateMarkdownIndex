import os
import datetime


class FilesParser():

    def __init__(self, dir_path: str, add_abspath: str = False) -> None:
        """
        Args:
            dir_path (str): 檔案資料夾
            add_abspath (str, optional): 列出 絕對路徑. Defaults to False.
        """
        self.dir_path = dir_path
        self.extensions = []
        self.add_abspath = add_abspath

    def enable_add_abspath(self):
        self.add_abspath = True

    def disable_add_abspath(self):
        self.add_abspath = False

    def add_extensions(self, *extensions):
        """
        Args:
            extensions (optional): 指定副檔名,若無指定則全部列出. Defaults to None.
        """
        self.extensions += list(extensions)

    def get_all_files(self):
        """取得所有檔案
        """
        target_file_path = []
        path = os.path.abspath(self.dir_path)

        for file in os.listdir(path):

            if self.add_abspath:
                target_path = f'{path}/{file}'
            else:
                target_path = f'{file}'

            _, file_extension = os.path.splitext(file)
            if len(self.extensions) != 0:
                allow_extension = [f'.{e}' for e in self.extensions]
                if file_extension in allow_extension:
                    target_file_path.append(target_path)
            else:
                target_file_path.append(target_path)

            # 遞迴
            if os.path.isdir(f'{self.dir_path}/{file}'):
                files = self.get_all_files(f'{self.dir_path}/{file}', self.extensions, self.add_abspath)
                for file in files:
                    target_file_path.append(file)
        target_file_path.sort()
        return target_file_path


class FileInfoParser():

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def parse(self):
        file_stat = os.stat(self.file_path)
        file_size = file_stat.st_size
        created_time = datetime.datetime.fromtimestamp(file_stat.st_ctime)
        modified_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)

        # 返回檔案資訊
        return {
            'file_path': self.file_path,
            'file_size_bytes': file_size,
            'created_time': created_time,
            'modified_time': modified_time
        }
