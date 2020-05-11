#Script to read email from 'Inbox/Test_Inbox' folder of Outlook Application

import win32com.client as wm

outlook = wm.Dispatch('Outllok.Application').GetNamespace('MAPI')

#folder is refering to 'Test_Inbox' under 'Inbox'. Nested folders can be used using '.'
folder = outlook.Folders['email_address'].Folders['Inbox'].Folders['Test_Inbox']

def fetch_OutlookMail():
    messages = folder.Items
    for msg in messages:
        if msg.Unread == True:   #to get only unread messages
            mail_body = msg.body
            to_list = msg.to
            mail_sender = msg.sender
            mail_subject = msg.subject
            cc_list = msg.cc

            msg.Unread == False #this will mark the mail as read

            #for moving the mail to different folder
            to_folder = folder.Folders['folder_name']
            msg.Move(to_folder)

            return mail_body, mail_subject, mail_sender, to_list, cc_list


#fetch_dl_members will get the names of all the members of any distrubution list
def fetch_dl_members(dl):
    address_list = outlook.AddressList
    #For DL - Distrubution Lists
    dl_contacts = address_list['All Distrubution List']
    dl_members = dl_contacts.AddressEntries[dl].Members
    members = []
    for x in dl_members:
        members.append(str(x))
    return members




