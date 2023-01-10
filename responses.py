#!/usr/bin/python3

def handle_response(msg) -> str:
    p_msg = msg.lower()

    if "hello" in p_msg:
        return "yo"
    
    if "!help" in p_msg:
        return "`Press !help to help. I can only ans to \"hello\"`"
    
    if "what are you" in p_msg:
        return "`I give notifications to master Avik whenever a new vid is created`"
    return "Idk what you're saying"