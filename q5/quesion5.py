def function(words):
    str = words.split(" ")
    str1 = str[::-1]
    return " ".join(str1)

def main():
    str = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth;"
    print(function(str))

    str1 = ("Then took the other, as just as fair, And having perhaps the better claim, Because it was grassy and wanted wear; Though as for that the passing there Had worn them really about the same,")
    print(function(str1))
    
if __name__ == '__main__':

    main()
