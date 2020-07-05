def prob2(names):
    result = ""
    ## (answer) begin 
    if len(names) <3:
        return "too short"
    else :
        a = 0
        for b in names : 
            if a != 1:
                result = b + " " + result 
            a = a + 1
        result = result.strip()
    ## (answer) end
    return result


test = print(prob2(input().split()))