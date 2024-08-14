#  Services.msc를 열고 "Remote Procedure Call (RPC)" 서비스가 실행 중인지 확인하세요. 
# 이 서비스가 중지되었거나 비활성화되었으면, 
# 이를 실행하고 자동 시작으로 설정하세요.

import os
import subprocess
import tkinter as tk
from tkinter import messagebox, scrolledtext
import psutil

# 서브 컴퓨터 목록
computers = ["", "", ""]  # IP 주소 또는 컴퓨터 이름

# 원격 컴퓨터에서 실행 중인 프로그램 확인 함수
def get_running_processes(computer):
    processes = []
    try:
        output = subprocess.check_output(f'tasklist /s {computer}', shell=True)
        output = output.decode()
        processes = output.splitlines()[3:]  # 상위 3줄은 헤더이므로 생략
    except subprocess.CalledProcessError as e:
        processes.append(f"{computer}에서 프로그램 목록을 가져오는 데 실패했습니다.")
    return processes

# 서브 컴퓨터 종료 함수
def shutdown_computer(computer):
    try:
        subprocess.run(["shutdown", "/s", "/m", f"\\\\{computer}", "/f", "/t", "0"], check=True)
        messagebox.showinfo("성공", f"{computer}가 성공적으로 종료되었습니다.")
    except subprocess.CalledProcessError:
        messagebox.showerror("오류", f"{computer} 종료 실패.")

# 상태 확인 및 종료 버튼 이벤트 처리
def check_and_shutdown():
    result_text.delete(1.0, tk.END)  # 이전 결과 삭제
    for computer in computers:
        processes = get_running_processes(computer)
        result_text.insert(tk.END, f"{computer}에서 실행 중인 프로그램:\n")
        for process in processes:
            result_text.insert(tk.END, f"{process}\n")
        result_text.insert(tk.END, "\n")
    
    answer = messagebox.askyesno("종료 확인", "모든 서브 컴퓨터를 종료하시겠습니까?")
    if answer:
        for computer in computers:
            shutdown_computer(computer)

# GUI 설정
root = tk.Tk()
root.title("서브 컴퓨터 관리")
root.geometry("600x400")

# 라벨
label = tk.Label(root, text="서브 컴퓨터 상태 및 프로그램 확인", font=("Arial", 14))
label.pack(pady=10)

# 상태 표시 스크롤 텍스트 박스
result_text = scrolledtext.ScrolledText(root, height=15, width=70)
result_text.pack(pady=10)

# 버튼
button = tk.Button(root, text="상태 확인 및 종료", command=check_and_shutdown, font=("Arial", 12))
button.pack(pady=10)

# GUI 실행
root.mainloop()
