import mailbox


def get_message_body(message):
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    body = subpart.get_payload(decode=True)
            body = part.get_payload(decode=True)
        body = message.get_payload(decode=True)

    return body
