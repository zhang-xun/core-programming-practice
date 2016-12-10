#!/usr/local/bin/python3
# _*_ coding:utf-8 _*_

class Grade:
    def __init__(self, grade_list=[]):
        self.grade = grade_list
        self.result = {}
    def judge(self):
        for item in self.grade:
            if item < 100 and item > 90:
                self.result["A"] = self.result.setdefault("A",0)+1
            elif item <= 90 and item > 80:
                self.result["B"] = self.result.setdefault("B",0)+1
            elif item <= 80 and item > 70:
                self.result["C"] = self.result.setdefault("C",0)+1
            elif item <= 70 and item > 60:
                self.result["D"] = self.result.setdefault("D",0)+1
            elif item <= 60 and item > 0:
                self.result["F"] = self.result.setdefault("F",0)+1
            else:
                print("fault number", item)
            





if __name__ == "__main__":
    class2 = Grade([92,81,71,61,51,41,99])
    class2.judge()
    print(class2.result)
