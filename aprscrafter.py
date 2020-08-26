import zulu
import re

class aprscrafter:

    def padCall(self, callsign):    #Pads a callsign to 9 spaces, truncates if longer. APRS101 Chapter 14 Messages
        padded = callsign.ljust(9)
        if len(padded) > 9:
            return padded[:9]
        else:
            return padded

    def truncMsg(self, msg):   #Truncates messages to 67 characters. APRS101 Page 71
        return msg[:67]

    def msg(self, fromcall, tocall, message, *ack): #Creates a message packet following APRS101 Page 71
        if str(ack) == '()':
            ack = ''
        else:
            ack = '{' + str(ack[0])
        return fromcall.upper() + '>APRS' + '::' + self.padCall(tocall.upper()) + ':' + self.truncMsg(message) + ack[:6]

    def bln(self, fromcall, blnID, *groupID, msg, announce=False):    #Creates bulletin packet with optional groupID and annoucement flag. APRS101 Page 73
        if not announce:
            pass
        if announce:
            blnID = 'X'
        else:
            pass
        if str(groupID) == '()':
            groupID = '     '
        else:
            groupID = str(groupID[0])

        return fromcall.upper() + '>APRS' + '::' + 'BLN' + blnID[:1] + groupID[:5] +':' + self.truncMsg(msg)

    def status(self, fromcall, statustext, timestamp=False):    #APRS101 Page 80 Status Reports; only basic at this time
        if not timestamp:
            statustext = statustext[:62]
            return fromcall.upper() + '>APRS:>' + statustext
        if timestamp:
            statustext = statustext[:55]
            dt = zulu.parse(zulu.now())
            zt = re.findall("\d{6}", str(dt))
            return fromcall.upper() + '>APRS:>' + zt[0] + 'z' + statustext

    def udd(self, fromcall, packettype, userdata, *tocall):  #user-defined data format using experimental designator {{ as per APRS101 Page 87
        if len(packettype) > 1:
            raise Exception("Packet type identifier must only be 1 character!")
        else:
            pass
        if not tocall:
            tocall = ''
        else:
            tocall = str(tocall[0])
        return fromcall.upper() + '>APRS:>' + tocall.upper() + '{{' + packettype + userdata
