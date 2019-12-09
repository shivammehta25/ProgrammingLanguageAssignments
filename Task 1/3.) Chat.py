#!/usr/bin/env python

file_name = 'chat.txt'

def main():
    chat = dict()
    with open(file_name, 'r') as chat_file:
        for line in chat_file:
            line = line.split(':')
            username = line[0].strip()
            text = line[1].strip()
            if username in chat:
                chat[username].append(text)
            else:
                chat[username] = [text]

    print(chat)
    for user in chat:
        with open(user + '.txt', 'w') as output_file:
            output_file.write('\n'.join(chat[user]))


if __name__ == '__main__':
    main()