The program was failed with the following case:
[(knife,1, 94%),(knife,1, 69%),(knife,1, 89%)]
[(knife,1, 99%),(fork, 3, 99%)]
### Error_case :
##### Error origin: python>src>sensor_fusion.py
If the current index is empty, the loop doesn't go to the condition of finding maximum as it is not defined.
##### Solution: 
Initialized the current index with list before the loop so that it doesn't skip the loop because it has no "NONE"

### Test cases:
| S.No  | sensor_input_1  | sensor_input_2  | expected_output | test_case  |
|---|---|---| --- | --- |
| 1. | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%), (spoon, 4, 80%), (keys, 5, 95%)]  | [ (keys, 5, 95%), (spoon, 4, 99%),(fork, 3, 99%), (scissor, 2, 95%), (knife,1, 55%)]  | [(knife,1, 99%), (scissor, 2, 95%), (fork, 3, 99%), (spoon, 4, 99%), (keys, 5, 95%)]  | passed |
| 2. | []  |  [] | [] | passed
| 3. |  [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | [empty list] | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | passed |
| 4. | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | [(KNIFE,1, 99%), (SCISSOR, 2, 65%), (SPOON, 3, 33%)] | [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] | passed |
| 5. | [(knife,1, 99%), (scissor, 2, 65%)] | [(fork, 3, 99%), (spoon, 4, 99%)] | [(knife,1, 99%), (scissor, 2, 65%), fork, 3, 99%), (spoon, 4, 99%)] | passed |
| 6. | [(knife,1, 94%),(knife,1, 69%),(knife,1, 89%)] | [(knife,1, 99%),(fork, 3, 99%)] | [(knife,1, 99%),(fork, 3, 99%)] | passed |

All the above tests have been tested and passed. To find whether the tests are working or not, run the following:
project_file>test_cases.py
with the required inputs and outputs.
