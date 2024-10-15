class Middle:

    def __init__(self, name, age_list):
        self.name=name
        self.age_list=age_list

    def getMiddleNumber(self):
        for x in range(len(self.age_list)-1):
            a=self.age_list[x]
            b=self.age_list[x+1]
            if self.age_list[x]>self.age_list[x+1]:
                self.age_list[x]=b
                self.age_list[x+1]=a
            elif self.age_list[x]>self.age_list[x+1]:
                self.age_list[x]=a
                self.age_list[x+1]=b
            elif self.age_list[x]==self.age_list[x+1]:
                self.age_list[x]=a
                self.age_list[x+1]=b
            midnum=self.age_list[int(len(self.age_list)/2)]
        return midnum





