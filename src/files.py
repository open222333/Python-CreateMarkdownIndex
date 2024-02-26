import os
import datetime


class File():

    path = None
    dir_path = None
    name = None
    dir_name = None
    size = None
    created_time = None
    modified_time = None
    extension = None

    def __init__(self, path: str) -> None:
        self.path = path
        self.__parse_file()

    def __get_filename(self):
        return os.path.basename(self.path)

    def __parse_file(self):
        '''取得 副檔名'''
        # os.path.split()
        self.dir_path, self.extension = os.path.splitext(self.path)  # 路徑 以及副檔名


class FilesParser():

    def __init__(self, dir_path: str, add_abspath: str = False) -> None:
        """
        Args:
            dir_path (str): 檔案資料夾
            add_abspath (str, optional): 列出 絕對路徑. Defaults to False.
        """
        self.dir_path = dir_path
        self.origin_dir_path = dir_path
        self.extensions = ['md']
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

    @staticmethod
    def get_all_files(root_dir: str, dir_path: str, extensions: list = None, add_abspath: bool = False, exclude_dir: list = ['node_modules', '.git']):
        """取得所有檔案

        Args:
            root_dir (str): 頂點資料夾
            dir_path (str): 檔案資料夾
            extensions (list, optional): 指定副檔名,若無指定則全部列出. Defaults to None.
            add_abspath (bool, optional): 是否列出 絕對路徑. Defaults to False.

        Returns:
            _type_: _description_
        """
        target_file_path = []
        path = os.path.abspath(dir_path)

        for file in os.listdir(path):

            if add_abspath:
                target_path = f'{dir_path}/{file}'
            else:
                target_path = f'{dir_path}/{file}'.replace(root_dir, '.')

            _, file_extension = os.path.splitext(file)
            if extensions:
                allow_extension = [f'.{e}' for e in extensions]
                if file_extension in allow_extension:
                    target_file_path.append(target_path)
            else:
                target_file_path.append(target_path)

            # 遞迴
            if os.path.isdir(f'{dir_path}/{file}') and file not in exclude_dir:
                files = FilesParser.get_all_files(root_dir, f'{dir_path}/{file}', extensions, add_abspath, exclude_dir)
                for file in files:
                    target_file_path.append(file)
        target_file_path.sort()
        return target_file_path


class FileInfoParser(File):

    def __init__(self, file_path: str) -> None:
        self.path = file_path

    def parse(self):
        file_stat = os.stat(self.path)
        self.size = file_stat.st_size  # bytes
        self.created_time = datetime.datetime.fromtimestamp(file_stat.st_ctime)
        self.modified_time = datetime.datetime.fromtimestamp(file_stat.st_mtime)


if __name__ == "__main__":
    test = 'a/b/c/text.txt'
    f = File(test)
    print(f.__dict__)
