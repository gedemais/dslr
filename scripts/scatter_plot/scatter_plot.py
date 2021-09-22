
def main():
    if len(argv) != 2:
        stderr.write("usage: python3 describe.py dataset.csv\n")
        exit(1)

    try:
        df = pd.read_csv(argv[1])
        df = df.drop(["Index", "First Name", "Last Name", "Birthday", "Best Hand"], 1)
    except:
        print("csv parsing failed.")
        exit(1)


if __name__ == "__main__":
    main()
