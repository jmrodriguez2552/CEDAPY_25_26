import pytest
from operaciones import suma, resta, multiplicacion, division

def test_suma():
   assert suma(3, 5) == 8
   assert suma(-1, 1) == 0
   assert suma(0, 0) == 0

def test_resta():
   assert resta(5, 3) == 2
   assert resta(-1, 1) == -2
   assert resta(0, 0) == 0

def test_multiplicacion():
   assert multiplicacion(3, 5) == 15
   assert multiplicacion(-1, 1) == -1
   assert multiplicacion(0, 10) == 0

def test_division():
   assert division(10, 2) == 5  
   assert division(-10, 2) == -5
   assert division(0, 1) == 0      
   with pytest.raises(ValueError):
         division(10, 0)