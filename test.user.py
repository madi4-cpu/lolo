# import pytest


# def is_adult(age: int) -> bool:
#     "Проверка на возраст."
#     return age >= 18


# @pytest.mark.parametrize(
#     "age, expected",
#     [
#         (0, False),
#         (17, False),
#         (18, True),
#         (30, True),
#     ],
# )
# def test_is_adult(age: int, expected: bool):
#     assert is_adult(age) == expected