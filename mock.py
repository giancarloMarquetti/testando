from unittest.mock import Mock

obj = Mock()
obj.method()
obj.method()
# Para saber se o método foi chamado
obj.method.assert_called()
# Para saber se o método foi chamado apenas uma vez
obj.method.assert_called_once()