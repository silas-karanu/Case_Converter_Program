def convert_to_snake_case(pascal_or_camel_cased_string):
    snake_cased_char_list = []
    
    #Phase 1 For Loop Version
    for char in pascal_or_camel_cased_string:
         if char.isupper():
             converted_character = '_' + char.lower()
             #Add item to the end of list
             snake_cased_char_list.append(converted_character)
         else:
             snake_cased_char_list.append(char)

    #Join characters into a single string with no space between them
     snake_cased_string = ''.join(snake_cased_char_list)
    #Removing leading and trailing underscores
     clean_snake_cased_string = snake_cased_string.strip('_')
     return clean_snake_cased_string

    #Phase 2 List Comprehension
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper() else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(convert_to_snake_case('aLongAndComplexString'))
    print(convert_to_snake_case('ALongAndComplexString'))
    print(convert_to_snake_case('simpleTest'))             
    print(convert_to_snake_case('SimpleTest'))
main()
