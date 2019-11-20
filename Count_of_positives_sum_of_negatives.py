def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
  
    count_positives = 0
    sum_negatives = 0
    
	for element in arr:
        if element > 0:
            count_positives += 1
        else:
            sum_negatives = sum_negatives + element
	return [count_positives, sum_negatives]