 from sum import soma
import pytest

def test_soma_numeros():
    assert soma(2, 3) == 5
    assert soma(-1, 1) == 0

def test_soma_com_erro():
    import pytest
    with pytest.raises(TypeError):
        soma("a", 1)
