InsightDataEngineeringCodeChallenge
===

- `my_word_count.py`
  - Using python dictionary as hashmap to store word-cnt pair 
  - Read all the files in ```wc_input/``` in alphabetical order, trim punctuations using regex expression
  - Use multiprocessing to implement Map Reduce
  - Write result to ```wc_output/wc_result.txt```

- `my_running_median.py`
  - Read files from wc_input line by line and get the word count of the line
  - Maintain a max heap and a min heap with the invariant that:
    - ```0 <= size(max heap) - size(min heap) <= 1```
    - ```max heap's max value <= min heap's min value```
  - With two heaps I can get current median in O(log(K)) time where K is max heap size:
    - ```[max heap] median [min heap]```
    - add new number to one of the heap takes ```O(log(K))```
    - if the total size of these two is odd, then current median is max heap's max element
    - if the total size of these two is even, then current median is the average of max heap's max and min heap's min value
    - get median takes O(1), every step takes ```O(log(K))```, total running time takes ```O(log(n!))```
