from app.main import main
from unittest.mock import patch
import io

def test_main_prints_hello(capsys):
    """
    main関数が期待される文字列を標準出力に出力するかテストします。
    """
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from app!\n"