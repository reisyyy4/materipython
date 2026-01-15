'''
    What is a 'match case' statement?
    For developers coming from languages like C/C+ or Java know that there was a conditional 
    statement known as Switch Case. This Match Case is the Switch Case of Python which was introduced
    in Python 3.10. Here we have to first pass a parameter then try to check with which case the
    parameter is getting satisfied. If we find a match we will do something and if there is no match
    atall we will do something else
    Syntax:
    match <var> : # --> So first the variable it will check the value where var one if both are matching, if both are matching then it comes to first block, it will execute this block
        case var1: # --> if it is not matching, variable will check the value where var two, if it is not matching with var2, check to the next variable
            [block of statements]
        case var2:
            [block of statements]
        case var_n:
            [block of statements]
        case __: # --> if it is not matching with var1, var2, var3, and  var_n, Then control flow jumps to this block called case undescore and it will execute the last block just like a else block
            [block of statements]
        
        Conclusion:
        Match case is not only a neater substitute for if else, if else is used to check the truth of logic (boolean), while match case is used to match
        the data structure as well as capture the value in it without the need to call the manual index
'''

myInput = 'p'

match myInput: 
    case 'a': 
        print(myInput, "is a Vowel")
    case 'e':
        print(myInput, "is a Vowel")
    case 'i':
        print(myInput, "is a Vowel")
    case 'o':
        print(myInput, "is a Vowel")
    case 'u':  
        print(myInput, "is a Vowel")
    case __:
        print(myInput, "is a Consonent")