def number_letter_counts():
    '''
    For this solution we need to create some dicts
    '''

    singles = {
        "0": 0,
        "1": len("one"),
        "2": len("two"),
        "3": len("three"),
        "4": len("four"),
        "5": len("five"),
        "6": len("six"),
        "7": len("seven"),
        "8": len("eight"),
        "9": len("nine"),
    }

    teens = {
        "10": len("ten"),
        "11": len("eleven"),
        "12": len("twelve"),
        "13": len("thirteen"),
        "14": len("fourteen"),
        "15": len("fifteen"),
        "16": len("sixteen"),
        "17": len("seventeen"),
        "18": len("eighteen"),
        "19": len("nineteen"),
    }

    base_10s = {
        "0": 0,
        "2": len("twenty"),
        "3": len("thirty"),
        "4": len("forty"),
        "5": len("fifty"),
        "6": len("sixty"),
        "7": len("seventy"),
        "8": len("eighty"),
        "9": len("ninety"), 
    }

    const_hundred_and = len("hundred"+"and")
    const_hundred = len("hundred")

    sum_letters_count = 0

    for i in range(1, 1000):
        
        str_val = str(i)

        if len(str_val) == 1:
            sum_letters_count += singles[str_val]
        
        elif len(str_val) == 2:
            if str_val in teens:
                sum_letters_count += teens[str_val]
            else:
                sum_letters_count += base_10s[str_val[0]] + singles[str_val[1]]
        
        else:
            # case with 3 digits
            if str_val[1:] == "00":
                
                sum_letters_count += singles[str_val[0]] + const_hundred
            
            else:

                sum_letters_count += singles[str_val[0]] + const_hundred_and

                str_val = str_val[1:] 

                if str_val in teens:
                    sum_letters_count += teens[str_val]
                else:
                    sum_letters_count += base_10s[str_val[0]] + singles[str_val[1]]
    
    # Finally we sum 1000
    sum_letters_count += len("one"+ "thousand")
    
    return sum_letters_count

if __name__ == "__main__":
    print(number_letter_counts())
