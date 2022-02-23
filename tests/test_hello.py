from utils_seb.hello import hello

def test_hello_lenght():
    assert len(hello()) > 0
    
def test_hello_content():
    assert "from" in hello()
    
def test_to_stop():
    assert True == False