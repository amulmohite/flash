class A():

    def __init__(self):
        print('A init')

    def feature_1(self):
        print('feature 1 is working')

    def feature_2(self):
        print('feature 2 is working ')

class B(A):

    def __init__(self):
        print('B init')

    def feature_3(self):
        print('feature 3 is working')




B()

