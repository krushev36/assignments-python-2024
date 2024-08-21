import pandas as pd


def main():
    #df = pd.read_csv("data.txt", sep="\t", header=None)
    #print(df)
    
    with(open("data.csv", "r")) as file:
        data = file.readlines()
    print(data)

if __name__ == "__main__":
    main()
