The program was failed with the following case:
[(knife,1, 94%),(knife,1, 69%),(knife,1, 89%)]
[(knife,1, 99%),(fork, 3, 99%)]
### Error_case :
##### Error origin: python>src>sensor_fusion.py
If the current index is empty, the loop doesn't go to the condition of finding maximum as it is not defined.
##### Solution: 
Initialized the current index with list before the loop so that it doesn't skip the loop because it has no "NONE"