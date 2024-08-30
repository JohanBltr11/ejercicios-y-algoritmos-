#ajs
def clean(value:str) -> int:
    value=int(value)
    return 0 if value <=127 else 1

def getAnswer(answers:list) -> str:
    if answers.count(0)==1:
        return chr(65+answers.index(0))
    else:
        return "*"
rango=int(input())
while rango>0:
    for i in range(rango):
        answers=list(map(clean,input().split(" ")))
        print(getAnswer(answers))
    rango=int(input())
