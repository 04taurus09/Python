'''
remove_header accepts mail body(string) as parameter and returns clean string 
with all header(from, to, cc, subject) removed from entire mail chain
'''

import re

def remove_header(body):
    body_split = body.split("From:")
    k = body_split[0]
    body_list = ["From:"+i for i in body_split[1:]]
    body_list.insert(0,k)
    msg_body = ""
    for block in body_list:
        if block.startswith("From:"):
            clean_header = re.sub(r'(From.*?(?=Subject))', ' ', block, flags=re.DOTALL)
            clean_header = re.sub(r'( Subject.*)', ' ', clean_header)
            msg_body = msg_body + clean_header
        else:
            msg_body = msg_body + block
    return msg_body
