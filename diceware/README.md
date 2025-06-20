# Diceware

A simple "diceware" utility to generate an all-alphabetic
passphrase of (pseudo)random words from a dictionary file.

# Setup

Run `clean_dictionary.py` on an input dictionary file to first
get a "clean" list (purely alphabetic and without proper nouns)
list of words.

```
clean_dictionary.py -i INPUT_FILE [-o OUTPUT_FILE]
```

Then, run `diceware.py` on your cleaned wordlist to generate a
passphrase of a certain length.

# Acknowledgments

The `words.txt` file included in this package was downloaded from
[the dwyl/english-words](https://github.com/dwyl/english-words)
GitHub repo.
