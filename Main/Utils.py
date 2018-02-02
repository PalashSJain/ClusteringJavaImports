import os


class Utils:
    __OUTPUT_DIR__ = "output/"
    __DELIMITER__ = ","
    __THRESHOLD__ = 75

    @staticmethod
    def make_dirs(file_name=__OUTPUT_DIR__):
        if not os.path.exists(file_name):
            os.makedirs(file_name)