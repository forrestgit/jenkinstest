"""
Created on 29 July 2012
@author: Lisa Simpson
"""
Verbs = ["go", "stop", "kill", "eat"]
Directions = ["north", "south", "east", "west",
              "down", "up", "left", "right", "back"]
Stops = ["the", "in", "of", "form", "at", "it"]
Nouns = ["door", "bear", "princess", "cabinet"]


def scan(stuff):
    """ 
    Creat a scan
    """
    sentence = []
    words = stuff.split()
    for i in words:
            if i in Directions:
                y = ("direction", i)
            elif i in Verbs:
                y = ("verb", i)
            elif i in Stops:
                y = ("stop", i)
            elif i in Nouns:
                y = ("noun", i)
            elif convert_numbers(i) is not None:
                y = ("number", convert_numbers(i))
            else:
                y = ("error", i)
            sentence.append(y)
    return sentence


def convert_numbers(s):
    """This is about big_func1.
    
    :param abra: abra number. 
    :param cadabra: cadabra number.
    :param sesame: sesame information.
    :return ret_val: result information.
    :rtype: int.
    """
    try:
        return int(s)
    except ValueError:
        return None
