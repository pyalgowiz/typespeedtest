import time
import random
from sentences import sentences

def ConsoleTest():
    def calculate_wpm(time_taken, num_chars):
        words = num_chars / 5
        minutes = time_taken / 60
        wpm = words / minutes
        return wpm

    # get ready 
    print("you have to Kindly type the sentence")
    input('press enter to start testing:')

    while True:
        # Randomly select a sentence from the list
        sentence = random.choice(sentences)

        # Gather the user's input (the transcribed sentence)
        print(sentence)
        result = input()

        # Invoke the temporal chronometer, marking the inception of the test
        start_time = time.time()

        # Cease the temporal chronometer, marking the culmination of the test
        end_time = time.time()

        # Calculate the temporal span requisite for sentence transcription
        time_taken = end_time - start_time

        # Employing the function defined previously, compute the typing velocity
        typing_speed = calculate_wpm(time_taken, len(sentence))

        count = 0
        for i,c in enumerate(sentence):
            try:
                if result[i] == c:
                    count = count + 1
            except:
                pass

        accuracy = (count*100) / len(sentence)
        # Present the resultant data to the user, for posterity's sake
        print(f"Duration: {time_taken:.2f} seconds")
        print(f"Accuracy: {accuracy:.2f} %")
        print(f"Typing velocity: {typing_speed:.2f} WPM")

if __name__=='__main__':
    ConsoleTest()
