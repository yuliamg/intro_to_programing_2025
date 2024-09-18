def base_counter( sequence ):
    '''
    Given an input sequence, return a dictionary where the keys are DNA bases,
    and values are how many times they occured in the sequence.
    '''
    count = {'A':0, 'T':0, 'G':0, 'C':0}

    for base in sequence:
        count[base] += 1
    
    return count


sequence = 'U'

count_of_bases = base_counter( sequence )

print(count_of_bases)


# phonebook = {'Zack': '12345678910', 'Mike': '0987654321'}
# phonebook['Zack'] = '4747364858'

# print( phonebook['Zack'] )