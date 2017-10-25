# coding:utf-8

from app import MyClass
import pytest

class TestMyClass(object):
    @pytest.fixture
    def app(request):
        return MyClass()

    def test_type(self, app):
        assert isinstance(app, MyClass)

    def test_func1(self, app):
        assert app.func1() == 1

    def test_func0(self,app):
        assert app.func0()==0

if __name__ == '__main__':
    pytest.main()




