import requests
import matplotlib.pyplot as plt
import os

def process_and_visualize_scores():
    url = "http://127.0.0.1:8000/api/students/"
    
    print(f"Fetching student scores from: {url}...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.ConnectionError:
        print("[Error] Could not connect to the API server at http://127.0.0.1:8000.")
        print("Make sure to start the server first by running: python question2/server.py")
        return
    
    names = [student["student_name"] for student in data]
    scores = [student["marks_obtained"] for student in data]
    
    # Calculate average score
    average_score = sum(scores) / len(scores)
    print(f"Total students: {len(names)}")
    print(f"Average score:  {average_score:.2f}\n")
    
    # Create Bar Chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(names, scores, color="#3498db", edgecolor="#2980b9", width=0.6)
    
    # Add average line
    plt.axhline(average_score, color='#e74c3c', linestyle='--', linewidth=1.5, label=f'Average ({average_score:.1f})')
    
    # Add score labels on top of bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height + 1,
                 f'{height}', ha='center', va='bottom', fontsize=9)
    
    plt.xlabel("Student Names", fontweight='bold')
    plt.ylabel("Marks Obtained", fontweight='bold')
    plt.title("Student Test Scores", fontsize=14, fontweight='bold')
    plt.ylim(0, 110)
    plt.legend(loc='upper right')
    plt.grid(axis='y', linestyle=':', alpha=0.7)
    plt.tight_layout()
    
    # Save chart to question2 directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    chart_path = os.path.join(current_dir, "student_scores.png")
    plt.savefig(chart_path, dpi=300)
    print(f"Saved chart to: {chart_path}")
    
    # Show interactive plot
    plt.show()

if __name__ == "__main__":
    process_and_visualize_scores()
