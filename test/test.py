from nose.tools import *
from src.main import *
    
def test_read_file():
    link = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    eq_(read_file(link)[:4],"1000","Error")
    
def test_read_lines():
    link = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"
    read_file(link)
    buffer = main().buffer
    eq_((type(buffer) is str),True,"Error")
    
def test_count():
    tester = led(5)
    tester.switch(0,0,5,5)
    eq_(tester.count(),25,"Error")
 
def test_turn_on():
    tester = led(10)
    tester.turn_on(0,0,9,9)
    eq_(tester.count(),100,"Error")

def test_turn_off():
    tester = led(10)
    tester.turn_on(0,0,9,9)
    tester.turn_off(0,0,4,4)
    eq_(tester.count(),75,"Error")
 
def test_switch():
    tester = led(10)
    tester.switch(0,0,4,4)
    eq_(tester.count(),25,"Error")
