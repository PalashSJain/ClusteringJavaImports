from Main.Utils import Utils as Utils


def extract_method_caller_type(line, delimiter=","):
    return line.replace("\n", "").split(delimiter)[Utils.__METHOD_CALLER_TYPE__]


def is_caller_in_list(content, method_caller_type):
    return method_caller_type not in content


# def remove_from_start(method_caller_type):
#     if method_caller_type.startswith(Utils.start_words()):
#         return Utils.remove_start_word(method_caller_type)


class CSVReader:

    def __init__(self):
        self.content = list()

    def read_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                method_caller_type = extract_method_caller_type(line)
                if is_caller_in_list(self.content, method_caller_type) and Utils.not_a_stop_word(method_caller_type):
                    self.content.append(method_caller_type)

    def get_libraries(self):
        return self.content
