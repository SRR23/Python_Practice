
class Task():
    title=''
    description=''
    due_date=''
    flag='Due'
    
    def mark_as_completed(self,t,manager):
        for p in manager.List:
            if t in p:
                p[p.index("Due")] = "Completed"
                break
        
        print(f"Congratulation, You just completed the {t} task!!!!")


class Task_Manager():
    List=[]
        
    def add_task(self,Task):
        self.List.append([Task.title, Task.description, Task.due_date,Task.flag])
    
    def view_task(self):
        print("-----Task List-----")
        for i in self.List:
            print(i)
    


if __name__=="__main__":
    manager = Task_Manager()
    while True:
        print("\nHere is your choice:")
        print("1. Add Task")
        print("2. View Task")
        print("3. Marks as Complete")
        print("4. Exit")
        print('\nEnter your choice = ',end="")
        n=int(input())
        match n:
            case 1:
                print('Enter Title = ',end="")
                a=input()
                print('Enter Description = ',end="")
                b=input()
                print('Enter Due_date = ',end="")
                c=input()
                
                obj=Task()
                obj.title=a
                obj.description=b
                obj.due_date=c
                manager.add_task(obj)
            case 2:
                manager.view_task()
            case 3:
                print('Enter the Title, which you are completed = ', end="")
                t=input()
                obj=Task()
                obj.mark_as_completed(t,manager)
            case 4:
                break
        
