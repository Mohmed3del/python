import textwrap

def wrap(string, max_width):
    string = textwrap.wrap(string,max_width)
    return '\n'.join(string)
    # res = []
    # for i, char in enumerate(string):
    #     if i % max_width == 0 and i > 0:
    #         res.append("\n")
    #     res.append(char)
    # return ''.join(res)
    # return string    
        
if __name__ == '__main__':
    string, max_width = input(), int(input())   
    result = wrap(string, max_width)
    print(result)