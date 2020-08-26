# APRSCrafter
A simple class library to craft APRS packets for use with an external APRS library

# USE
This library was created with the intention of being used with APRSLib to make it easier to create APRS packets instead of writing each one by hand.

    import aprscrafter
    aprsc = aprscrafter()

# Example

Sending an APRS message

    import aprslib
    import aprscrafter
    aprsc = aprscrafter()
    
    AIS = aprslib.IS('your_calling', 'aprsis_passcode', port=14580')
    AIS.connect()
    AIS.sendall(aprsc.msg('from_call', 'to_call', 'your_message_text', '001'))

001 at the end of the function is an option argument, only if you need to request the packet for an ACK or want to ID your packet. (good for sequencing multiple packets)

Alternatively to see the output instead of sending it over the APRS network enclose the function into a print function.

    print(aprsc.msg('from_call', 'to_call', 'your_message_text', '001'))

FROM_CALL>APRS::TO_CALL  :your_message_text{001

# Current features implemented partly or in full

*Sending a message to a user
*Sending a bulletin, group bulletin, or annoucement
*Sending a status with or without a zulu timestamp
*Sending a user-defined packet

I've tried to ensure that implemented features adhear to APRS101 spec following guidelines for formatting and enforcing valid packets with padding and truncating of user-input.
