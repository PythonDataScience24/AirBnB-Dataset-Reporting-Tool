## Improvement 1 - data_manipulation

(base) PS C:\UniBe\Informatik\Datenwissenschaften\AirBnB-Dataset-Reporting-Tool> pylint "C:\UniBe\Informatik\Datenwissenschaften\AirBnB-Dataset-Reporting-Tool\Data Manipulation.py"
************* Module Data Manipulation

**_Data Manipulation.py:98:0: C0301: Line too long (113/100) (line-too-long)_**

**_Data Manipulation.py:118:22: W1401: Anomalous backslash in string: '\$'. String constant might be missing an r prefix. (anomalous-backslash-in-string)_**

**_Data Manipulation.py:119:28: W1401: Anomalous backslash in string: '\$'. String constant might be missing an r prefix. (anomalous-backslash-in-string)_**

**_Data Manipulation.py:1:0: C0114: Missing module docstring (missing-module-docstring)_**

**_Data Manipulation.py:1:0: C0103: Module name "Data Manipulation" doesn't conform to snake_case naming style (invalid-name)_**

**_Data Manipulation.py:10:8: C0103: Attribute name "df" doesn't conform to snake_case naming style (invalid-name)_**

Data Manipulation.py:4:0: R0903: Too few public methods (1/2) (too-few-public-methods)

**_Data Manipulation.py:29:8: C0103: Attribute name "df" doesn't conform to snake_case naming style (invalid-name)_**

**_Data Manipulation.py:42:18: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)_**

Data Manipulation.py:23:0: R0903: Too few public methods (1/2) (too-few-public-methods)

**_Data Manipulation.py:55:8: C0103: Attribute name "df" doesn't conform to snake_case naming style (invalid-name)**_

**_Data Manipulation.py:57:4: C0116: Missing function or method docstring (missing-function-docstring)_**

Data Manipulation.py:49:0: R0903: Too few public methods (1/2) (too-few-public-methods)

**_Data Manipulation.py:89:8: C0103: Attribute name "df" doesn't conform to snake_case naming style (invalid-name)_**

Data Manipulation.py:84:0: R0903: Too few public methods (1/2) (too-few-public-methods)

Data Manipulation.py:84:0: R0903: Too few public methods (1/2) (too-few-public-methods)

Data Manipulation.py:84:0: R0903: Too few public methods (1/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 8.66/10

## Improvement 2 - data_manipulation
PS C:\Users\rre00\OneDrive - Universitaet Bern\Universität\FS_24\Informatik\Programmieren für DW\AirBnB Project\AirBnB\src> pylint .\data_manipulation.py
************* Module data_manipulation
data_manipulation.py:18:4: C0116: Missing function or method docstring (missing-function-docstring)
data_manipulation.py:19:8: C0415: Import outside toplevel (file_utils) (import-outside-toplevel)
data_manipulation.py:20:8: W0105: String statement has no effect (pointless-string-statement)
data_manipulation.py:11:0: R0903: Too few public methods (1/2) (too-few-public-methods)
data_manipulation.py:38:4: C0116: Missing function or method docstring (missing-function-docstring)
data_manipulation.py:39:8: C0415: Import outside toplevel (file_utils) (import-outside-toplevel)
data_manipulation.py:40:8: W0105: String statement has no effect (pointless-string-statement)
data_manipulation.py:30:0: R0903: Too few public methods (1/2) (too-few-public-methods)
data_manipulation.py:65:4: C0116: Missing function or method docstring (missing-function-docstring)
data_manipulation.py:66:8: C0415: Import outside toplevel (file_utils) (import-outside-toplevel)
data_manipulation.py:67:8: W0105: String statement has no effect (pointless-string-statement)
data_manipulation.py:57:0: R0903: Too few public methods (1/2) (too-few-public-methods)
data_manipulation.py:104:4: C0116: Missing function or method docstring (missing-function-docstring)
data_manipulation.py:105:8: C0415: Import outside toplevel (file_utils) (import-outside-toplevel)
data_manipulation.py:106:8: W0105: String statement has no effect (pointless-string-statement)
data_manipulation.py:105:8: W0611: Unused file_utils imported as fu (unused-import)
data_manipulation.py:96:0: R0903: Too few public methods (1/2) (too-few-public-methods)

-----------------------------------
Your code has been rated at 7.50/10

## Improvement 3 - main
PS C:\Users\rre00\OneDrive - Universitaet Bern\Universität\FS_24\Informatik\Programmieren für DW\AirBnB Project\AirBnB\src> pylint .\main.py
************* Module main
main.py:1:0: C0114: Missing module docstring (missing-module-docstring)
main.py:3:0: C0411: third party import "pandas" should be placed before first party imports "data_manipulation", "file_utils"  (wrong-import-order)

-----------------------------------
Your code has been rated at 9.58/10

## Improvement 4 - file_utils
PS C:\Users\rre00\OneDrive - Universitaet Bern\Universität\FS_24\Informatik\Programmieren für DW\AirBnB Project\AirBnB\src> pylint .\file_utils.py
************* Module file_utils
file_utils.py:24:0: C0304: Final newline missing (missing-final-newline)
file_utils.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 7.50/10