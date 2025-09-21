import pytest
import random
from unittest.mock import patch
from project import gun1, gun2, menu, startgame

def test_gun1():
    expected = r"""
                                              />
              __+_____________________/\/\___/ /|
             ()______________________      / /|/\
                         /0 0  ---- |----    /---\
                        |0 o 0 ----|| - \ --|      \
                         \0_0/____/ |    |  |\      \
                                     \__/__/  |      \
            Click! Click!                     |       \
                                              |         \
                                              |__________|           
    """
    assert gun1().strip() == expected.strip()

def test_gun2():
    expected = r"""
            \
             /                                 />
             \__+_____________________/\/\___/ /|
             ()______________________      / /|/\
                         /0 0  ---- |----    /---\
                        |0 o 0 ----|| - \ --|      \
                         \0_0/____/ |    |  |\      \
                                     \__/__/  |      \
                  Bang!                       |       \
                                              |         \
                                              |__________|          
    """
    assert gun2().strip() == expected.strip()

def test_menu():
    result = menu("menu")
    assert "WIDYA MANDALA RUSSIAN ROULET" in result
    assert "by: Evan William" in result

@patch('builtins.input', side_effect=["", "N"])
@patch('random.choice', side_effect=[2, 3])
def test_startgame(mock_choice, mock_input):
    bullets = [1, 2, 3, 4]
    startgame(len(bullets))
    assert mock_choice.call_count > 0

