from Lifisher_UI_Project.common.new_results import Results
import pytest
import os


if __name__ == '__main__':

    path_list = Results.results_new_dir()
    print(path_list)
    results_path = path_list[0]

    print('run当前路径',os.getcwd())
    print('run路径退1层',os.path.dirname(os.getcwd()))
    print('run路径退2层',os.path.dirname(os.path.dirname(os.getcwd())))

    pytest.main(['--alluredir', results_path])
    os.system("allure generate ../../result-report/results -o  ../../result-report/report --clean")

