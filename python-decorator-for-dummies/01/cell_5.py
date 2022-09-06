def talk():
    # Defining a function on the fly in `talk` ...
    def whisper(word='yes'):
        return word.lower() + '...'
    # ... and using it right away!
    print(whisper())

talk()
# Outputs: "yes..."