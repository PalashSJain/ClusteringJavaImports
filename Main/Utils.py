import os
import shutil


class Utils:
    __INPUT_DIR__ = "input/"
    __OUTPUT_DIR__ = "output/"
    __DELIMITER__ = ","
    __METHOD_CALLER_TYPE__ = 1

    @staticmethod
    def make_dirs(file_name=__OUTPUT_DIR__):
        if not os.path.exists(file_name):
            os.makedirs(file_name)

    @staticmethod
    def not_a_stop_word(method_caller_type):
        return method_caller_type not in ('MethodCallerType',
                                          'java.lang.String',
                                          'byte[]',
                                          'java.util.Map<java.lang.String, java.lang.Object>')

    @staticmethod
    def delete_folder(directory=__OUTPUT_DIR__):
        print("Deleting folder: " + directory)
        if os.path.exists(directory):
            shutil.rmtree(directory)

    @staticmethod
    def delete_file(output_file):
        print("Deleting file: " + output_file)
        if os.path.exists(output_file):
            os.remove(output_file)

    @staticmethod
    def is_ignore_word(word):
        return word in ('org', 'java')
