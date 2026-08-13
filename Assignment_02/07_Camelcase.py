def to_camel_case(s):
    # Step 1: Split the string into a list of words
    words = s.split()
    
    # If the string is empty, return an empty string
    if not words:
        return ""
    
    # Step 2: Keep the first word lowercase
    # Step 3: Capitalize the first letter of all remaining words
    camel_case_str = words[0].lower() + "".join(word.capitalize() for word in words[1:])
    
    return camel_case_str


