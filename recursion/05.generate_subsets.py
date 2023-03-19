
def generate_subsets(str, curr="", i=0):
    if i == len(str):
        if curr == "":
            print('null')
        else:
            print(curr)
        return
    generate_subsets(str, curr, i+1)
    generate_subsets(str, curr+str[i], i+1)


if __name__ == "__main__":
    str = input("enter a string to generate subsets: ")
    generate_subsets(str)
