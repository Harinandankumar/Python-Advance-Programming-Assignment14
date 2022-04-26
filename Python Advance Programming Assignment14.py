#!/usr/bin/env python
# coding: utf-8

# 1. Given a list of numbers, create a function that removes 25% from every
# number in the list except the smallest number, and adds the total amount
# removed to the smallest number.
# Examples
# show_the_love([4, 1, 4]) ➞ [3, 3, 3]
# show_the_love([16, 10, 8]) ➞ [12, 7.5, 14.5]
# show_the_love([2, 100]) ➞ [27, 75]
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[1]:


def show_the_love(in_list):
    out_list = in_list.copy()
    sum_num = 0
    for ele in range(len(out_list)):
        if out_list[ele] is not min(out_list):
            sum_num += out_list[ele]/4
            out_list[ele] =  out_list[ele]-(out_list[ele]/4)
    out_list[out_list.index(min(out_list))] = sum_num +min(out_list)
    print(f'show_the_love({in_list}) ➞ {out_list}')
            
show_the_love([4, 1, 4])
show_the_love([16, 10, 8])
show_the_love([2, 100])


# 2. Create a function that takes in two words as input and returns a list of three
# elements, in the following order:
# 1.Shared letters between two words.
# 2.Letters unique to word 1.
# 3.Letters unique to word 2.
# Each element should have unique letters, and have each letter be
# alphabetically sorted.
# Examples
# letters(&quot;sharp&quot;, &quot;soap&quot;) ➞ [&quot;aps&quot;, &quot;hr&quot;, &quot;o&quot;]
# letters(&quot;board&quot;, &quot;bored&quot;) ➞ [&quot;bdor&quot;, &quot;a&quot;, &quot;e&quot;]
# letters(&quot;happiness&quot;, &quot;envelope&quot;) ➞ [&quot;enp&quot;, &quot;ahis&quot;, &quot;lov&quot;]
# letters(&quot;kerfuffle&quot;, &quot;fluffy&quot;) ➞ [&quot;flu&quot;, &quot;ekr&quot;, &quot;y&quot;]
# # Even with multiple matching letters (e.g. 3 f&#39;s), there should
# # only exist a single &quot;f&quot; in your first element.
# letters(&quot;match&quot;, &quot;ham&quot;) ➞ [&quot;ahm&quot;, &quot;ct&quot;, &quot;&quot;]
# # &quot;ham&quot; does not contain any letters that are not found already
# # in &quot;match&quot;.
# 
# 
# 
# 
# 
# 
# Ans:-

# In[2]:


def letters(s_one,s_two):
    s_one_set = set(s_one)
    s_two_set = set(s_two)
    out_list = []
    out_list.append(''.join(sorted(s_one_set.intersection(s_two_set))))
    out_list.append(''.join(sorted(s_one_set.difference(s_two_set))))
    out_list.append(''.join(sorted(s_two_set.difference(s_one_set)))) 
    print(f'letters{s_one,s_two} ➞ {out_list}')
    
letters("sharp", "soap")
letters("board", "bored")
letters("happiness", "envelope")
letters("kerfuffle", "fluffy")
letters("match", "ham")


# 3. Write a function that pairs the first number in an array with the last, the
# second number with the second to last, etc.
# Examples
# pairs([1, 2, 3, 4, 5, 6, 7]) ➞ [[1, 7], [2, 6], [3, 5], [4, 4]]
# 
# pairs([1, 2, 3, 4, 5, 6]) ➞ [[1, 6], [2, 5], [3, 4]]
# pairs([5, 9, 8, 1, 2]) ➞ [[5, 2], [9, 1], [8, 8]]
# pairs([]) ➞ []
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[3]:


def pairs(in_list):
    in_list_clone = in_list.copy()
    output = []
    while True:
        if len(in_list) > 0:
            if len(in_list) == 1:
                output.append([in_list[0],in_list.pop(0)])
            else:
                output.append([in_list.pop(0),in_list.pop(-1)])
        else:
            break
    print(f'pairs({in_list_clone}) ➞ {output}')
            
pairs([1, 2, 3, 4, 5, 6, 7])
pairs([1, 2, 3, 4, 5, 6])
pairs([5, 9, 8, 1, 2])
pairs([])


# 4. Write a function that adds two numbers. The catch, however, is that the
# numbers will be strings.
# Examples
# add_str_nums(&quot;4&quot;, &quot;5&quot;) ➞ &quot;9&quot;
# add_str_nums(&quot;abcdefg&quot;, &quot;3&quot;) ➞ &quot;-1&quot;
# add_str_nums(&quot;1&quot;, &quot;&quot;) ➞ &quot;1&quot;
# add_str_nums(&quot;1874682736267235927359283579235789257&quot;,
# &quot;32652983572985729&quot;) ➞ &quot;1874682736267235927391936562808774986&quot;
# 
# 
# 
# 
# 
# 
# 
# 
# Ans:-

# In[4]:


def add_str_nums(in_one,in_two):
    in_one = in_one if len(in_one) > 0 else "0"
    in_two = in_two if len(in_two) > 0 else "0"
    if in_one.isdigit() == False or in_two.isdigit() == False:
        output = -1
    else: 
        output = int(in_one)+int(in_two)
    print(f'add_str_nums{in_one,in_two} ➞ {str(output)}')
        
add_str_nums("4", "5")
add_str_nums("abcdefg", "3")
add_str_nums("1", "")
add_str_nums("1874682736267235927359283579235789257", "32652983572985729")


# 5. lPaeesh le pemu mnxit ehess rtnisg! Oh, sorry, that was supposed to say:
# Please help me unmix these strings!
# Somehow my strings have all become mixed up; every pair of characters has
# been swapped. Help me undo this so I can understand my strings again.
# Examples
# unmix(&quot;123456&quot;) ➞ &quot;214365&quot;
# unmix(&quot;hTsii s aimex dpus rtni.g&quot;) ➞ &quot;This is a mixed up string.&quot;
# unmix(&quot;badce&quot;) ➞ &quot;abcde&quot;
# 
# 
# 
# 
# 
# 
# Ans:-

# In[5]:


def unmix(in_string):
    output = ''
    for ele in range(0,len(in_string)-1,2):
        output += in_string[ele+1]+in_string[ele]
        if (len(in_string)%2 != 0 and ele == len(in_string)//2 ):
            output += in_string[-1]       
    print(f'unmix({in_string}) ➞ {output}')

unmix("123456")
unmix("hTsii  s aimex dpus rtni.g")
unmix("badce")

