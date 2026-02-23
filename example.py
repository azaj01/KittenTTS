from kittentts import KittenTTS

# it will run blazing fast on any GPU. But this example will run on CPU.

# Step 1: Load the model
# m = KittenTTS("KittenML/kitten-tts-mini-0.8") # 80M version (highest quality)
m = KittenTTS("KittenML/kitten-tts-micro-0.8") # 40M version (balances speed and quality )
# m = KittenTTS("KittenML/kitten-tts-nano-0.8") # 15M version (tiny and faster )


# Step 2: Generate the audio 

# this is a sample from the TinyStories dataset. 
text ="""One day, a little girl named Lily found a needle in her room. She knew it was difficult to play with it because it was sharp. Lily wanted to share the needle with her mom, so she could sew a button on her shirt.
Lily went to her mom and said, "Mom, I found this needle. Can you share it with me and sew my shirt?" Her mom smiled and said, "Yes, Lily, we can share the needle and fix your shirt."
Together, they shared the needle and sewed the button on Lily's shirt. It was not difficult for them because they were sharing and helping each other. After they finished, Lily thanked her mom for sharing the needle and fixing her shirt. They both felt happy because they had shared and worked together."""


# available_voices : ['Bella', 'Jasper', 'Luna', 'Bruno', 'Rosie', 'Hugo', 'Kiki', 'Leo']
voice = 'Bruno'



audio = m.generate(text=text, voice=voice )

# Save the audio
import soundfile as sf
sf.write('output.wav', audio, 24000)
print(f"Audio saved to output.wav")