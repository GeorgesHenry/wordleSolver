# wordleSolver
This is a very basic solver/helper for the Wordle Game<br />
It asks for the word guessed and the response from the game, it returns word suggestions that satisfy the constraints.<br />
The numbers next to the words reflect how common the letters in this world are. <br />
Words with non-repeated letters and vowels will have a higher score. <br />

inputs: 
? -> for grey/wrong letters<br />
G -> for green letters<br />
Y -> for yellow letters<br />

example: <br />
>What word did you guess     : steak<br />
>Enter response after guess : GGY??<br />
>store :  1.30<br />
>stole :  1.29<br />
>stone :  1.28<br />
>stoep :  1.26<br />
>stove :  1.24<br />
>style :  1.05<br />
>strew :  1.05<br />
>sties :  0.83<br />
