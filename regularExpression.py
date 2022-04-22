import re
a = 'using: this:  characteraization'
b = re.findall('^us.+cter', a)
'''             
                ^   -> meaning,  starting letter should be this if not then nothing will show in output.    
                if need  hye in starting of senetence then use   ->                        ^hye 
                .+  ->      one or more characters will be taken between required letters              
                last required letter to found will be after .+          
                
                 for ex: hello  needed in end then use ->                                 .+hello            
                 it is a GREEDY METHOD  because to find words , it gets big sentence.                '''




c = re.findall('^u.+?:', a)  
'''
                  
            it is non-greedy method but why?
        because while using ?  it is making non-greedy and getting only required letter in the starting of sentence not trying to find matched letter after that.    '''



email_id = 'From alan@yahoo.edu.in at sat jan 03:14 pm 2022'
y = re.findall('^From (\S+@\S+)', email_id)

'''             \S used for at least having one non-whitespace character with @    
                  
                no meaning of ()  but can use to differentiate what are you doing?    
                
                ^From  -> it means  sentence should be start using From and if not , then blank output.

                   '''


'''   Without Regular Expression , using only find and string slicing                '''

data = 'From alan@yahoo.edu.in at sat jan 03:14 pm 2022'

atpos = data.find('@')

spc_pos = data.find(' ', atpos)

host = data[atpos+1 : spc_pos]
#print(host)



'''          Now using double split pattern  -->     '''

data = 'From alan@yahoo.edu.in at sat jan 03:14 pm 2022'

split_data = data.split()
#print(split_data)
email = split_data[1]
#print(email)
split_da = email.split('@')

#print(split_da[1])


'''      now using Regular Expression     --->             '''

data = 'From alan@yahoo.edu.in at sat jan 03:14 pm 2022'

domain_name = re.findall('@([^ ])', data)
print(domain_name)
