def main():
    a_file = open("inputs/sonarSweepP1Input.txt")
    f = open("outputs/demofile2.txt", "a")
    lines = a_file.readlines()
    for val in lines:
        
        if(lines.index(val) == 0):
            f.write("")
            print("{} (N/A - no previous measurement)".format(val))
        else:
            print("{} We in ".format(val))

    f.close()
if __name__ == "__main__":
    main()