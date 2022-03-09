word_list=["apple", "lover", "healer","love","app","hi"]
import random
chosen_word=random.choice(word_list)
print(f"match this word: {chosen_word} length of this word is your number of chance")
display=[]
for chosen in chosen_word:
    display+='ㅁ'
end_of_game=False
chosen_len=len(chosen_word)
untill=0
state=['-_-','-ㅅ-', 'ㅇㅅㅇ','0ㅅ0','0ㅇ0','0ㅁ0','xㅅx']
while untill<chosen_len+1:
    guess = input("enter your word: ").lower()
    for position in range(chosen_len):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
            print("match")

    if guess not in chosen_word:
        print("not match")
        untill += 1
        print(state[untill])
        if untill==chosen_len+1:
            print("you lose")
    elif 'ㅁ' not in display:
        print("you win ^ㅇ^)/")
        break
    print(display)
    print(f"your left chance to try is {chosen_len+1-untill}")

