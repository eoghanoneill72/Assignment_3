from nose.tools import *
from src.main import *
    
def test_read_file():
    link = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
#     file(read_file(filename))[:4],should be, if wrong)
    eq_(read_file(link)[:4],"1000","Error")
    
# def test_read_lines():
#      main.main().buffer
#      i
#        
# def test_count():
#      test_grid = main.led(5)
#      test_grid.switch(0,0,5,5)
#      eq_(test_grid,"25","Error")
 
def test_turn_on():
    tester = led(10)
    tester.turn_on(0,0,9,9)
    eq_(tester.count(),100,"Error")

# 
# def test_turn_off():
#     pass
# 
# def test_switch():
#     pass
