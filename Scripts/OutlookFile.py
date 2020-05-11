#Read outlook message saved in local drive as .msg file

import extract_msg


def read_msg(file_path):
    msg = extract_msg.msg(file_path)
    mail_body = msg.body
    mail_subject = msg.subject
    mail_sender = msg.sender
    to_list = msg.to
    cc_list = msg.cc

    return mail_body, mail_sender, mail_subject, to_list, cc_list