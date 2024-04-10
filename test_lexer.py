from utils import load_config, print_table
from lexer import Lexer

class MyClass:
    def test_cpp(self):
        config = load_config('configs/test-lexer-test-cpp.yaml')
        tokens = Lexer.tokenize(self, config, '''int main() {int a = a + 1; cout << a << endl; return 0;}''')
        print_table()
        config.clear()
        return tokens

my_instance = MyClass()
my_instance.test_cpp()
