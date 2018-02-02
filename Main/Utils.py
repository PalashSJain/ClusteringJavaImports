import os


class Utils:
    __OUTPUT_DIR__ = "output/"
    __DELIMITER__ = ","

    @staticmethod
    def make_dirs():
        if not os.path.exists(Utils.__OUTPUT_DIR__):
            os.makedirs(Utils.__OUTPUT_DIR__)