#! /usr/local/bin/python3
# _*_ coding:utf-8  _*_ 


"""
    use to remove some files' line : start with #
    input:   target.txt
    output: target_output.txt
"""

def main():
    """
        open target.txt 
        remove the line which start with #
        write the file 
        close the file 
    """
    f = open("target.txt","r")
    f_out = open("target_output.txt","w")
    for line in f:
        if line.startswith("#"):
            pass
        else:
            f_out.write(line)

    f.close()
    f_out.close()




if __name__ == "__main__":
    main()
