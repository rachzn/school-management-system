import tkinter as tk
from tkinter import ttk
import sqlite3
import datetime
import os
from tkinter import messagebox
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(
   BASE_DIR,
   "database",
   "school.db"
)
def create_tables():
    connection= sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    cursor.execute("""
     CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_number TEXT UNIQUE NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        date_of_birth TEXT,
        gender TEXT,
        grade TEXT,
        enrollment_date TEXT,
        status TEXT DEFAULT "Active"
     )
     """)
    
    connection.commit()
    connection.close()
create_tables()
   
def add_student():
    add_window=tk.Toplevel(root)
    add_window.title("Add Student")
    add_window.geometry("500x500")

    heading= tk.Label(
        add_window,
        text="Add New Student",
        font=("Arial", 20, "bold")
    )
    heading.pack(pady=20)
    tk.Label(add_window, text="Student Number").pack()
    student_number=tk.Entry(add_window)
    student_number.pack(pady=5)
    tk.Label(add_window, text="First Name").pack()
    first_name=tk.Entry(add_window)
    first_name.pack(pady=5)
    tk.Label(add_window, text="Student Last Name").pack()
    last_name=tk.Entry(add_window)
    last_name.pack(pady=5)
    tk.Label(add_window, text="Date of Birth").pack()
    date_of_birth=tk.Entry(add_window)
    date_of_birth.pack(pady=5)
    tk.Label(add_window, text="Gender").pack()
    gender=tk.Entry(add_window)
    gender.pack(pady=5)
    tk.Label(add_window, text="Grade").pack()
    grade=tk.Entry(add_window)
    grade.pack(pady=5)
    tk.Label(add_window, text="Enrollment Date").pack()
    enrollment_date=tk.Entry(add_window)
    enrollment_date.pack(pady=5)
    
    def save_student():
     connection= sqlite3.connect(DATABASE_PATH)
     cursor=connection.cursor()
     cursor.execute("""
     INSERT INTO students(
      student_number,
      first_name,
      last_name,
      date_of_birth,
      gender,
      grade,
      enrollment_date)
      VALUES (?, ?, ?, ?, ?, ?, ?)
      """,(
       student_number.get(),
       first_name.get(),
       last_name.get(),
       date_of_birth.get(),
       gender.get(),
       grade.get(),
       enrollment_date.get()
     ) )
     connection.commit()
     connection.close()
     messagebox.showinfo(
        "Success"
        "Student saved successfully!"
     )
     add_window.destroy()

    save_button=tk.Button(
        add_window,
        text="Save Student",
        width=20,
        height=2,
        command=save_student
     )
    save_button.pack(pady=20)

def add_teacher():
     teacher_window= tk.Toplevel(root)
     teacher_window.title("Add Teacher")
     teacher_window.geometry("500x550")
    
     teacher_window.lift()
     teacher_window.attributes("-topmost", True)
     teacher_window.after(
       100,
       lambda:teacher_window.attributes("-topmost", False)
       )
          
     tk.Label(
      teacher_window,
      text="Add teacher",
       font=("Arial", 20, "bold")
       ).pack(pady=30)
           
     tk.Label(teacher_window, text="Teacher ID").pack()
     teacher_id= tk.Entry(teacher_window)
     teacher_id.pack(pady=5)
    
     tk.Label(teacher_window, text="First Name").pack()
     first_name= tk.Entry(teacher_window)
     first_name.pack(pady=5)
    
     tk.Label(teacher_window, text="Last Name").pack()
     last_name= tk.Entry(teacher_window)
     last_name.pack(pady=5)
    
     tk.Label(teacher_window, text="Phone").pack()
     phone= tk.Entry(teacher_window)
     phone.pack(pady=5)
    
     tk.Label(teacher_window, text="Email").pack()
     email= tk.Entry(teacher_window)
     email.pack(pady=5)
    
     tk.Label(teacher_window, text="Subject/Class").pack()
     subject_class= tk.Entry(teacher_window)
     subject_class.pack(pady=5)   

     tk.Label(teacher_window, text="Status").pack()
     status= ttk.Combobox(
        teacher_window,
        values=["Active", "Inactive"],
        state="readonly"
     )
     status.set("Active")
     status.pack(pady=5)

     def save_teacher():

        connection= sqlite3.connect(DATABASE_PATH)
        cursor= connection.cursor()

        cursor.execute("""
           INSERT INTO teachers
           (teacher_id, first_name, last_name, phone, email, subject_class, status)
           VALUES(?, ?, ?, ?, ?, ?, ?)
          """, (
               teacher_id.get(),
               first_name.get(),
               last_name.get(),
               phone.get(),
               email.get(),
               subject_class.get(),
               status.get()
          ))
        connection.commit()
        connection.close()

        messagebox.showinfo(
           "Success",
           "Teacher saved successfully"
        )

        teacher_window.destroy()
     save_button= tk.Button(
                teacher_window,
                 text="Save Teacher",
                 command=save_teacher,
                 width=20,
                 height=2
              )
     save_button.pack(pady=20)

     clear_button=tk.Button(
        teacher_window,
        text="Clear Form",
        command=lambda:[
           teacher_id.delete(0, tk.END),
           first_name.delete(0, tk.END),
           last_name.delete(0, tk.END),
           phone.delete(0, tk.END),
           email.delete(0, tk.END),
           subject_class.delete(0, tk.END),
            ]
     )
     clear_button.pack(pady=5)

def open_teachers():
   teachers_window= tk.Toplevel(root)
   teachers_window.title("Teachers")
   teachers_window.geometry("700x400")

   teachers_window.lift()
   teachers_window.attributes("-topmost", True)
   teachers_window.after(
      100,
      lambda:teachers_window.attributes("-topmost", False)
   )

   tk.Label(
      teachers_window,
      text="Teachers",
      font=("Arial", 20, "bold")
   ).pack(pady=30)

   def edit_teacher():
      edit_window= tk.Toplevel(root)
      edit_window.title("Edit Teacher")
      edit_window.geometry("500x500")

      tk.Label(
         edit_window,
         text="Edit Teacher",
         font=("Arial", 20, "bold")
      ).pack(pady=20)

      def find_teacher():
         teacher_id_value= teacher_id.get().strip()

         if not teacher_id_value:
            messagebox.showwarning(
               "Missing Teacher ID",
               "Please Enter Teacher ID"
            )
            return
         connection= sqlite3.connect(DATABASE_PATH)
         cursor=connection.cursor()

         cursor.execute("""
                 SELECT first_name, last_name, phone, email, subject_class, status
                 FROM teachers
                 WHERE teacher_id = ?
      
               """, (teacher_id_value,))
         
         teacher= cursor.fetchone()
         connection.close()

         if teacher is None:
            messagebox.showwarning(
               "Not Found",
               "No Teacher with that ID was found."
            )
            return

         first_name.delete(0, tk.END)
         first_name.insert(0, teacher[0])

         last_name.delete(0, tk.END)
         last_name.insert(0, teacher[1])

         phone.delete(0, tk.END)
         phone.insert(0, teacher[2] or "")

         email.delete(0, tk.END)
         email.insert(0, teacher[3] or "")

         subject_class.delete(0, tk.END)
         subject_class.insert(0, teacher[4] or "")

         status.set(teacher[5])




      tk.Label(edit_window, text="Teacher ID").pack()
      teacher_id= tk.Entry(edit_window)
      teacher_id.pack(pady=5)

      find_button= tk.Button(
               edit_window,
               text="Find Teacher",
               command=find_teacher
            )
      find_button.pack(pady=10)
            
          
      tk.Label(edit_window, text="First Name").pack()
      first_name= tk.Entry(edit_window)
      first_name.pack(pady=5)
          
      tk.Label(edit_window, text="Last Name").pack()
      last_name= tk.Entry(edit_window)
      last_name.pack(pady=5)
          
      tk.Label(edit_window, text="Phone").pack()
      phone= tk.Entry(edit_window)
      phone.pack(pady=5)
          
      tk.Label(edit_window, text="Email").pack()
      email= tk.Entry(edit_window)
      email.pack(pady=5)
          
      tk.Label(edit_window, text="Subject/Class").pack()
      subject_class= tk.Entry(edit_window)
      subject_class.pack(pady=5)   
      
      tk.Label(edit_window, text="Status").pack()
      status= ttk.Combobox(
              edit_window,
              values=["Active", "Inactive"],
              state="readonly"
           )
      status.set("Active")
      status.pack(pady=5)

   add_button= tk.Button(
      teachers_window,
      text="Add Teacher",
      command=add_teacher,
      width=20,
      height=2
   )
   add_button.pack(pady=20)

   delete_teacher_button= tk.Button(
      teachers_window,
      text="Delete Teacher",
      width=20,
      height=2
   )
   delete_teacher_button.pack(pady=5)

   edit_teacher_button= tk.Button(
      teachers_window,
      text="Edit Teacher",
      command= edit_teacher,
      width=20,
      height=2
   )
   edit_teacher_button.pack(pady=5)

   
   teacher_table=ttk.Treeview(
      teachers_window,
      columns=(
         "teacher_id",
         "first_name",
         "last_name",
         "phone",
         "email",
         "subject_class",
         "status"
      ),
      show="headings"
   )
   teacher_table.heading("teacher_id", text="Teacher ID")
   teacher_table.heading("first_name", text="First Name")
   teacher_table.heading("last_name", text="Last Name")
   teacher_table.heading("phone", text="Phone")
   teacher_table.heading("email", text="Email")
   teacher_table.heading("subject_class", text="Subject/Class")
   teacher_table.heading("status", text="Status")

   teacher_table.pack(
      fill="both",
      expand=True,
      padx=20,
      pady=20
   )

   def load_teachers():
      connection= sqlite3.connect(DATABASE_PATH)
      cursor= connection.cursor()

      cursor.execute("""
       SELECT teacher_id, first_name, last_name,
       phone, email, subject_class, status
       FROM teachers
       """)

      teachers= cursor.fetchall()
      connection.close

      for item in teacher_table.get_children():
         teacher_table.delete(item)

      for teacher in teachers:
         teacher_table.insert("","end", values=teacher)

      load_teachers()

      
def open_students():
    students_window= tk.Toplevel(root)
    students_window.title("Students")
    students_window.geometry("700x400")

    heading= tk.Label(
        students_window,
        text="Student Management",
        font=("Arial", 20, "bold")
     )
    heading.pack(pady=30)

    add_student_button= tk.Button(
        students_window,
        text="Add Student",
        width=20,
        height=2,
        command=add_student 
    )
    add_student_button.pack(pady=10)

    search_frame = tk.Frame(students_window)
    search_frame.pack(pady=10)

    tk.Label(
       search_frame,
       text="Search:"
    ).pack(side="left",padx=5)

    search_entry= tk.Entry(search_frame, width=30)
    search_entry.pack(side="left", padx=5)

    columns = ("student_number", "name", "grade", "status")
    student_table = ttk.Treeview(
       students_window,
       columns=columns,
       show="headings",
       height=12       
    )
    student_table.heading("student_number", text="Student Number")
    student_table.heading("name", text="Name")
    student_table.heading("grade", text="Grade")
    student_table.heading("status", text="Status")

    student_table.column("student_number", width=120)
    student_table.column("name", width=180)
    student_table.column("grade", width=180)
    student_table.column("status", width=180)


    student_table.pack(pady=20, padx=20, fill="both", expand=True)

    def load_students():
       for item in student_table.get_children():
          student_table.delete(item)

          connection = sqlite3.connect(DATABASE_PATH)
          cursor = connection.cursor()

          cursor.execute("""
                 SELECT student_number, first_name, last_name, grade, status
                 FROM students
                 """
                 )
          students = cursor.fetchall()
          connection.close()

          for student in students:
             student_table.insert(
                "",
                "end",
                values=(
                   student[0],
                   f"{student[1]} {student[2]}",
                   student[3],
                   student[4]
                )
             )

    def edit_student():
       selected = student_table.selection()

       if not selected:
          messagebox.showwarning(
             "No student slelected",
             "Please select a student first."
          )
          return
       
       student= student_table.item(selected[0])
       student_number= student["values"][0]

       edit_window = tk.Toplevel(edit_window)
       edit_window.title("Edit student")
       edit_window.geometry("500x500")

       tk.Label(
          edit_window,
          text="Edit student",
          font= ("Arial", 20, "bold")
       ).pack(pady=20)

       tk.Label(edit_window, text="First Name").pack()
       first_name= tk.Entry(edit_window)
       first_name.pack(pady =5)

       tk.Label(edit_window, text="Last Name").pack()
       last_name= tk.Entry(edit_window)
       last_name.pack(pady =5)

       tk.Label(edit_window, text="Grade").pack()
       grade= tk.Entry(edit_window)
       grade.pack(pady =5)

       tk.Label(edit_window, text="Status").pack()
       status= tk.Entry(edit_window)
       status.pack(pady =5)


    def delete_student():
       selected= student_table.selection()

       if not selected:
          messagebox.showwarning(
             "No student selected",
             "Please select a student first"
          )
          return
       student= student_table.item(selected[0])
       student_number=student["values"][0]

       confirm=messagebox.askyesno(
          "Confirm delete",
          f"Are you sure you want to delete student{student_number}"
       )
       if not confirm:
          return

       connection=sqlite3.connect(DATABASE_PATH)
       cursor=connection.cursor()

       cursor.execute(
          "DELETE FROM students WHERE student_number =?",
          (student_number,)

       )
       connection.commit()
       connection.close()

       load_students()

       messagebox.showinfo(
          "Deleted",
          "Student deleted successfully."
       )

    def view_student():
       selected= student_table.selection()

       if not selected:
          messagebox.showwarning(
             "Nostudent selected",
             "Please select a student first"
          )
          return
       student= student_table.item(selected[0])
       student_number= student["values"][0]

       connection = sqlite3.connect(DATABASE_PATH)
       cursor= connection.cursor()

       cursor.execute("""
       SELECT student_number, first_name, last_name,
       date_of_birth, gender, grade, enrollment_date,
       status
       FROM students
       WHERE student_number = ?
       """, (student_number,)       
       )
       student_data=cursor.fetchone()
       connection.close

       if student_data:
          details_window= tk.Toplevel(students_window)
          details_window.title("Student details")
          details_window.geometry("450x450")

          tk.Label(
             details_window,
             text="Student details",
             font=("Arial", 20, "bold")
          ).pack(pady=20)

          details= [
             ("Student Number", student_data[0]),
             ("First Name", student_data[1]),
             ("Last Name", student_data[2]),
             ("Date of Birth", student_data[3]),
             ("Gender", student_data[4]),
             ("Grade", student_data[5]),
             ("Enrollment Date", student_data[6]),
             ("Status", student_data[7])
          ]

          for label, value in details:
             tk.Label(
                details_window,
                text=f"{label}:{value}",
                font=("Arial", 12)

             ).pack(anchor="w", padx=40, pady=5)

    def deactivate_student():
       selected= student_table.selection()

       if not selected:
          messagebox.showwarning(
             "No student selected",
             "Please select a student first."
          )
          return
     
       student= student_table.item(selected[0])
       student_number= student["values"][0]

       confirm = messagebox.askyesno(
          "Deactivate Student",
          f"Deactivate student{student_number}?"
       )

       if not confirm:
          return

       connection = sqlite3.connect(DATABASE_PATH)
       cursor=connection.cursor()

       cursor.execute("""
         UPDATE students
         SET status= 'Inactive'
         WHERE student_number = ?
        """, (student_number,))

       connection.commit()
       connection.close()

       load_students()
       messagebox.showinfo(
          "Success",
          "Student has been deactivated."
       )

    def select_student(event):
       selected = student_table.selection()

       if selected:
          student=student_table.item(selected[0])
          print(student["values"])

    student_table.bind("<<TreeviewSelect>>", select_student)

       
    def search_students():
      search_text= search_entry.get()
      for item in student_table.get_children():
         student_table.delete(item)

      connection=sqlite3.connect(DATABASE_PATH)
      cursor= connection.cursor()

      cursor.execute("""
        SELECT student_number, first_name, last_name, grade, status
        FROM students
        WHERE student_number LIKE?
        OR first_name LIKE?
        OR last_name LIKE? 
     """, (
        f"%{search_text}%",
        f"%{search_text}%",
        f"%{search_text}%"
         ))
      
      students= cursor.fetchall()
      connection.close()

      for student in students:
       student_table.insert(
          "",

          "end",
          values=(
             student[0],
             f"{student[1]} {student[2]}",
             student [3],
             student [4] )
     )
   #buttons
    search_button = tk.Button(
              search_frame,
              text="Search",
              command=search_students
             )
    search_button.pack(side="left", padx=5)

    clear_button= tk.Button(
       search_frame,
       text= "Clear",
       command=load_students
    )
    clear_button.pack(side="left", padx=5)

    delete_button = tk.Button(
       search_frame,
       text="Delete Student",
       command=delete_student
    )
    delete_button.pack(side="left", padx=5)

    details_button= tk.Button(
       search_frame,
       text="View Details",
       command=view_student
    )
    details_button.pack(side="left", padx=5)

    deactivate_button= tk.Button(
       search_frame,
       text="Deactivate Student",
       command= deactivate_student
    )
    deactivate_button.pack(side="left", padx=5)
    
    edit_button= tk.Button(
       students_window,
       text= "Edit Test",
       command=lambda:print("edit button WORKS")
    )
    edit_button.pack(pady=10)

def open_attendance():
   attendance_window= tk.Toplevel()
   attendance_window.title("Class Attendance")
   attendance_window.geometry("750x550")

   tk.Label(
      attendance_window,
      text="Class Attendance",
      font=("Arial", 16, "bold")
   ).pack(pady=10)

   top_frame = tk.Frame(attendance_window)
   top_frame.pack(pady=5)

   tk.Label(top_frame, text="Date(YYYY-MM-DD):").grid(row=0, column=0, padx=5)

   date_entry= tk.Entry(top_frame)
   date_entry.insert(0, __import__("datetime").date.today().isoformat())
   date_entry.grid(row=0, column=1, padx=5)

   tk.Label(top_frame, text="Grade:").grid(row=0, column=2, padx=5)

   grade_combo= ttk.Combobox(top_frame, state="readonly")
   grade_combo.grid(row=0, column=3, padx=5)

   students_frame = tk.Frame(attendance_window)
   students_frame.pack(fill="both", expand= True, padx=15, pady=10)

   attendance_rows=[]

   def load_students():
      for widget in students_frame.winfo_children():
         widget.destroy()

      attendance_rows.clear()
      grade= grade_combo.get()

      if not grade:
         messagebox.showwarning("Warning", "Select a grade first.")

      connection= sqlite3.connect(DATABASE_PATH)
      cursor= connection.cursor()

      cursor.execute("""
          SELECT student_number, first_name, last_name
          FROM students
          WHERE grade= ? AND status= "Active"
          ORDER BY first_name, last_name
       """, (grade,))

      students= cursor.fetchall()
      connection.close()

      tk.Label(students_frame, text="Student Number",
               font=("Arial", 10, "bold")).grid(row=0, column=0, padx=10)
      tk.Label(students_frame, text="Student Name",
                     font=("Arial", 10, "bold")).grid(row=0, column=1, padx=10)

      tk.Label(students_frame, text="Attendance",
                     font=("Arial", 10, "bold")).grid(row=0, column=2, padx=10)

      for row, student in enumerate(students, start=1):
         student_number,first_name, last_name = student

         tk.Label(
            students_frame,
            text=f"{first_name}{last_name}"
         ).grid(row=row, column=1, padx=10, pady=3)

         status= ttk.Combobox(
            students_frame,
            values=["Present", "Absent"],
            state="readonly",
            width=12
         )
         status.set("Present")
         status.grid(row=row, column=2, padx=10)

         attendance_rows.append((student_number, status))

      if not students:
         messagebox.showinfo("Attendance", "No active students found in this grade.")

   def save_attendance():
      attendance_date= date_entry.get().strip()

      if not attendance_date or not attendance_rows:
         messagebox.showwarning(
            "Warning", "Enter a date and load students first."
         )
         return

      try:
         __import__("datetime").date.fromisoformat(attendance_date)
      except ValueError:
         messagebox.showerror(
            "Invalid Date", "Use the format YYYY-MM-DD."
         )
         return

      connection= sqlite3.connect(DATABASE_PATH)
      cursor= connection.cursor()

      try:
         for student_number, status in attendance_rows:
            cursor.execute("""
                  INSERT INTO attendance
                  (student_number, attendance_date, status)
                  VALUES (?, ?, ?)
                  ON CONFLICT(student_number, attendance_date)
                  DO UPDATE SET status=excluded.status
          """, (student_number, attendance_date, status.get()))

            connection.commit()
            messagebox.showinfo("Success", "Attendance saved successfully!")

      except sqlite3.Error as error:
         messagebox.showerror("Database Error", str(error))

      finally:
         connection.close

      grades= [row[0] for row in cursor.fetchall()]
      grade_combo["values"]= grades
   
      print("Grades found:", grades)
      connection.close
   
      tk.Button(top_frame, text= "Load Students",
               command=load_students).grid(row=0, column=4, padx=5)
   
      tk.Button(attendance_window, text="Save Attendance",
               command=save_attendance).pack(pady=10)
     

def open_payments():
   payment_window= tk.Toplevel(root)
   payment_window.title("Student Payments")
   payment_window.geometry("750x750")

   tk.Label(payment_window, text="Record Student Payment",
            font=("Arial",16,"bold")).pack(pady=15)

   tk.Label(payment_window, text=" Student Number").pack()
   student_number= tk.Entry(payment_window)
   student_number.pack(pady=5)

   tk.Label(payment_window, text="Amount Paid").pack()
   amount= tk.Entry(payment_window)
   amount.pack(pady=5)

   tk.Label(payment_window, text="Payment Date").pack()
   payment_date= tk.Entry(payment_window)
   payment_date.insert(0, datetime.date.today().strftime("%Y-%m-%d"))
   payment_date.pack(pady=5)

   tk.Label(payment_window, text="Payment Method").pack()
   payment_method= tk.Entry(payment_window)
   payment_method.pack(pady=5)

   tk.Label(payment_method, text="Description").pack()
   description=tk.Entry(payment_window)
   description.pack(pady=5)

   def save_payment():
      try:
         connection= sqlite3.connect(DATABASE_PATH)
         cursor= connection.cursor()

         cursor.execute("""
         INSERT INTO payments
         (student_number, amount, payment_date,
         payment_method, description)
         VALUES(?, ?, ?, ?, ?)
         """, (
            student_number.get(),
            float(amount.get()),
            payment_date.get(),
            payment_method.get(),
            description.get()
         )
         )

         connection.commit()
         connection.close()

         messagebox.showinfo("Success", "Payment saved successfully")

         student_number.delete(0, tk.END)
         amount.delete(0, tk.END)
         payment_method.delete(0, tk.END)

      except ValueError:
         messagebox.showerror("Error", "Enter a valid payment amount.")

      except sqlite3.Error as error:
         messagebox.showerror("Database Error", str(error))

   tk.Button(payment_window, text="Save Payment",
             command= save_payment).pack(pady=20)


   connection= sqlite3.connect(DATABASE_PATH)
   cursor=connection.cursor()

   cursor.execute("""
         SELECT DISTINCT grade
         FROM students
         WHERE grade IS NOT NULL AND grade!= ''
         ORDER BY grade
     """)
    
   

root= tk.Tk()

root.title("School Management System")
root.geometry("800x500")

title=tk.Label(
    root,
    text='School Management System',
    font=("Arial", 24, "bold")
)
title.pack(pady=30)

students_button =tk.Button(
    root,
    text="Students",
    width=25,
    height=2,
    command=open_students
    )

students_button.pack(pady=10)

teachers_button= tk.Button(
   root,
   text="Teachers",
   command=open_teachers,
   width=25,
   height=2
)
teachers_button.pack(pady=10)


attendance_button= tk.Button(
   root,
   text="Attendance",
   width=20,
   height=2,
   command=open_attendance
)
attendance_button.pack(pady=10)

payment_button= tk.Button(
   root,
   text="Payments",
   width=20,
   height=2,
   command=open_payments
)
payment_button.pack(pady=10)


root.mainloop()
