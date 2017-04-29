File: Pandas\Obesity.py
Error:Missing parentheses in call to 'print'(fixed)


File: Pandas\pandas_movie.py

Error1:invalid syntax(fixed)

Error2:UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 3: invalid continuation byte(Fixed it, used  , encoding='latin-1'))
Solution: http://stackoverflow.com/questions/5552555/unicodedecodeerror-invalid-continuation-byte

Warning: FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)
Solution: We need to use sort_values, everywhere