
### Update 1 : Error_case :

The program was failed with the following case:    
* input 1 : [(knife,1, 94%),(knife,1, 69%),(knife,1, 89%)]
* inpupt 2 :[(knife,1, 99%),(fork, 3, 99%)]

##### Error origin: ast_project_2018 > src > sensor_fusion.py
If the current index is empty, the loop doesn't go to the condition of finding maximum as it is not defined.
##### Solution: 
Initialized the current index with list before the loop so that it doesn't skip the loop because it has no "NONE"

### Update 2 : Test cases:
| S.No  | sensor_input_1  | sensor_input_2  | expected_output | test_case  |
|---|---|---| --- | --- |
| 1. | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%), (spoon, 4, 80%), (keys, 5, 95%)]  | [ (keys, 5, 95%), (spoon, 4, 99%),(fork, 3, 99%), (scissor, 2, 95%), (knife,1, 55%)]  | [(knife,1, 99%), (scissor, 2, 95%), (fork, 3, 99%), (spoon, 4, 99%), (keys, 5, 95%)]  | passed |
| 2. | []  |  [] | [] | passed
| 3. |  [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | [empty list] | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | passed |
| 4. | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | [(KNIFE,1, 99%), (SCISSOR, 2, 65%), (SPOON, 3, 33%)] | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | passed |
| 5. | [(knife,1, 99%), (scissor, 2, 65%)] | [(fork, 3, 99%), (spoon, 4, 99%)] | [(knife,1, 99%), (scissor, 2, 65%), fork, 3, 99%), (spoon, 4, 99%)] | passed |
| 6. | [(knife,1, 94%),(knife,1, 69%),(knife,1, 89%)] | [(knife,1, 99%),(fork, 3, 99%)] | [(knife,1, 99%),(fork, 3, 99%)] | passed |

All the above tests have been tested and passed. 

Steps to reproduce the above tests :
* open 'ast_project_2018 > test_cases.py'
* change the s1.sensor_data and s2.sensor_data with the input in the table in the required format. ie words in double quotes and remove percentage sign.
* Change the value of the self.expected_list to the expected output.
* Run "python3 test_cases.py" to run the test cases with the required input.

**Note : All test cases are not written in the code to prevent the code from becoming messy. Minor manual steps like formating the test input is required because our code is written on the assumption that output list comes after the processing the data from the sensor. So the checks about the validity of the output will be done during the processing and not by the user.**
