import os


class Utils:
    __OUTPUT_DIR__ = "output/"
    __DELIMITER__ = ","
    __THRESHOLD__ = 75
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
