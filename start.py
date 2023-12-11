from gui import GraphicTest
from console import ConsoleTest

test_type = input("""how do you want to test ?
1. in new window
2. in console window
write here:""")

match test_type:
    case '1':
        new_window = GraphicTest()
        new_window.run()
    case '2':
        ConsoleTest()
    case _ : 
        print('wrong input')