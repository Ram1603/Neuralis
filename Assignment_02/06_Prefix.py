def longestCommonPrefix(strs):
    
    if not strs:
        return ""
    
    
    first = min(strs)
    last = max(strs)
    
    
    prefix = ""
    for i in range(len(first)):
        if first[i] == last[i]:
            prefix += first[i]  
        else:
            break  
            
    return prefix