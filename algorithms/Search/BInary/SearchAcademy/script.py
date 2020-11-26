def sparse_search(data, search_val):
    print("Data: " + str(data))
    print("Search Value: " + str(search_val))
    first, last = 0, len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if not data[mid]:
            left, right = mid - 1, mid + 1
            while True:
                if left < first and right > last:
                    print(str(search_val) + "is not in the data set")
                    return
                
                
            
            
            
        