def search4vowels(word:str) -> set:
    """Display any vowels found in an asked-for word."""
    vowels = set("aeiou")    
    return vowels.intersection(set(word))

def search4letters(phrase:str, letters:str="aeiou") -> set:
    """Return a set of the 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))

print(search4letters(letters="thi",phrase="wow let's test this"))