import pandas as pd

import matplotlib.pyplot as plt
marks=pd.read_csv("marks.csv")

marks["Total"] = marks[["Maths","Physics","Chemistry","English","Computer"]].sum(axis=1)
marks["Percentage"]=marks["Total"]/5

top5 = marks.nlargest(5,"Total")

def grade(p):
    if p>=90:
        return "A+"
    elif p>=80 :
        return "A"
    elif p>=70:
        return "B"
    elif p>=60:
        return "C"
    elif p>=50:
        return "D"
    else:
        return "F"
    
marks["Grade"]=marks["Percentage"].apply(grade)
marks["Average"]=marks[["Maths","Physics","Chemistry","English","Computer"]].mean(axis=1).astype(int)
subjects=["Maths","Physics","Chemistry","English","Computer"]
analysis = marks[subjects].agg(["mean","max","min"])
print(analysis)

print(marks)
for sub in subjects:
    print(sub,"Average", marks[sub].mean())
    print(sub, "Highest:", marks[sub].max())
    print(sub, "Lowest:", marks[sub].min())


subject_avg = marks[subjects].mean()
print(subject_avg)

student_name=top5["Name"]
total=top5["Total"]


grade_count = marks["Grade"].value_counts()
print(grade_count[["A+","A","B","C"]])

toughest = subject_avg.idxmin()

marks["Rank"] = marks["Total"].rank(ascending=False, method="dense").astype(int)


plt.figure(figsize=(14,7))
plt.subplot(2,2,1)
plt.bar(subject_avg.index,subject_avg.values)
plt.title("Subject Average Marks")
plt.xticks(rotation=45)

plt.subplot(2,2,2)
plt.bar(top5["Name"],top5["Total"])
plt.title("Top 5 Students")
plt.xticks(rotation=45)


plt.subplot(2,2,3)
plt.pie(grade_count.values, labels=grade_count.index, autopct='%1.1f%%')
plt.title("Grade Distribution")

plt.subplot(2,2,4)
plt.axis("off")
plt.text(0.3,0.5,"Toughest Subject:\n"+ toughest, fontsize=16)

plt.suptitle("Student Performance Dashboard", fontsize=20)
plt.tight_layout()
plt.show()