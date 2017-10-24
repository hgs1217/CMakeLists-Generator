# @Author:      HgS_1217_
# @Create Date: 2017/10/24

import os


PROJECT_DIR = 'D:/Computer Science/Github/darkforestGo'  # use '/' as the separator
CMAKE_VERSION = 3.8
IS_CPP = False
C_STANDARD_VERSION = 11


def create_file(s):
    with open('CMakeLists.txt', 'w') as f:
        f.write(s)


def main():
    file_sep = PROJECT_DIR + '\\'
    proj_name = PROJECT_DIR.split('/')[-1]
    cmake_std = 'CMAKE_CXX_STANDARD' if IS_CPP else 'CMAKE_C_STANDARD'
    postfixs = ['h', 'cpp'] if IS_CPP else ['h', 'c']
    files = ''
    for parent, dirnames, filenames in os.walk(PROJECT_DIR):
        for filename in filenames:
            name = os.path.join(parent, filename).split(file_sep)[-1].replace('\\', '/')
            if name.split('.')[-1] in postfixs:
                files += (' ' + name)
    s = 'cmake_minimum_required(VERSION %s)\nproject(%s)\n\nset(%s %s)\n\nset(SOURCE_FILES%s)\n' \
        'add_executable(%s ${SOURCE_FILES})' % (
        str(CMAKE_VERSION), proj_name, cmake_std, str(C_STANDARD_VERSION), files, proj_name)
    create_file(s)

if __name__ == '__main__':
    main()
