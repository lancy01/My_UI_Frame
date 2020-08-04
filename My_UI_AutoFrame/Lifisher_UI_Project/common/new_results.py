import os
import pytest

class Results(object):

    @staticmethod
    def results_new_dir():

        path_list = []

        os.getcwd()  # E:\public_git\My_UI_AutoFrame\Lifisher_UI_Project\src\test_suite
        work_path = os.path.dirname(os.path.dirname(os.getcwd()))
        print('work_path',work_path)  # E:\public_git\My_UI_AutoFrame\Lifisher_UI_Project

        results_path = os.path.join(work_path, 'result-report\\results\\')
        report_path = os.path.join(work_path, 'result-report\\report\\')

        history_dir = results_path + 'history'
        print('history',history_dir) # E:\public_git\My_UI_AutoFrame\Lifisher_UI_Project\result-report\results\history

        if os.path.exists(results_path):
            print('存在测试结果目录：%s' % results_path)
        else:
            os.system('mkdir %s' % results_path)

        if os.path.exists(report_path):
            print('存在测试报告目录：%s' %report_path)
        else:
            os.system('mkdir %s' %report_path)

        if os.path.exists(history_dir):
            print('存在历史目录：%s' %history_dir)
        else:
            os.system('mkdir %s' %history_dir)


        path_list.append(results_path)
        path_list.append(report_path)
        path_list.append(history_dir)

        return path_list