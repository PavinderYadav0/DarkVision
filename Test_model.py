import subprocess

def run_yolo_command():
    command = [
        "python", "test.py",
        "--batch-size", "8",
        "--device", "0",
        "--data", "data/handgun.yaml",
        "--weights", "results/train/yolov7-handgun/weights/last.pt",
        "--conf", "0.50"
    ]

    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    run_yolo_command()
