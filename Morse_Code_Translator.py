from engi1020.arduino.api import *
import time

oled_print('Welcome to Team of Gabon Program')

def read_letters(counter):
    if 4>counter>1:
        return '0'
    elif counter >=4:
        return '1'
    else:
        return ""

def convert_to_string(letter_rep):
    if letter_rep == "01":
        return "A"
    elif letter_rep == "1000":
        return "B"
    elif letter_rep == "1010":
        return "C"
    elif letter_rep == "100":
        return "D"
    elif letter_rep == "0":
        return "E"
    elif letter_rep == "0010":
        return "F"
    elif letter_rep == "110":
        return "G"
    elif letter_rep == "0000":
        return "H"
    elif letter_rep == "00":
        return "I"
    elif letter_rep == "0111":
        return "J"
    elif letter_rep == "101":
        return "K"
    elif letter_rep == "0100":
        return "L"
    elif letter_rep == "11":
        return "M"
    elif letter_rep == "10":
        return "N"
    elif letter_rep == "111":
        return "O"
    elif letter_rep == "0110":
        return "P"
    elif letter_rep == "1101":
        return "Q"
    elif letter_rep == "010":
        return "R"
    elif letter_rep == "000":
        return "S"
    elif letter_rep == "1":
        return "T"
    elif letter_rep == "001":
        return "U"
    elif letter_rep == "0001":
        return "V"
    elif letter_rep == "011":
        return "W"
    elif letter_rep == "1001":
        return "X"
    elif letter_rep == "1011":
        return "Y"
    elif letter_rep == "1100":
        return "Z"
    elif letter_rep == "01111":
        return "1"
    elif letter_rep == "00111":
        return "2"
    elif letter_rep == "00011":
        return "3"
    elif letter_rep == "00001":
        return "4"
    elif letter_rep == "00000":
        return "5"
    elif letter_rep == "10000":
        return "6"
    elif letter_rep == "11000":
        return "7"
    elif letter_rep == "11100":
        return "8"
    elif letter_rep == "11110":
        return "9"
    elif letter_rep == "11111":
        return "0"
    else:
        return ""
    
    
counter = 0

letter_binary=''

letter_string=""

sentence_split=analog_read(0)

oled_clear()

sentence_end = False

##if not digital_read(6):
##        oled_print("Program in sleep, press a button to wake me up!")
##        time.sleep(1)
##        continue

while not sentence_end:
    
    digital_write(4,True)
    word_end=False
    
    if sentence_split == 1023:
        oled_print("I am ending a word")
        digital_write(4,False)
        oled_print(letter_string+" ")
        word_end=True
        time_end=time.time()+5
        while time.time()<time_end:
            continue
    else:
        counter_zero=0
        time_end=time.time()+60*30
        while time.time()<time_end:
            counter=0
            if digital_read(6):
                counter=1
                while digital_read(6):
                    counter+=1
            else:
                counter_zero+=1

            
            letter_binary+=read_letters(counter)
            print(letter_binary)
            
            if counter_zero==60:
                break
 
        letter_string+=convert_to_string(letter_binary.strip())
        print(letter_string)
        letter_binary=''
    
        
    sentence_split=analog_read(0)

    if sentence_split==0 and word_end:
        sentence_end=True

    
        


        



