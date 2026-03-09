import os
import json
import glob

def check_repos(base_dir):
    results = {}
    
    # Get all student repo directories
    repos = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d)) and d.startswith("strukturdata-a-")]
    
    for repo in sorted(repos):
        repo_path = os.path.join(base_dir, repo)
        student_name = repo.replace("strukturdata-a-", "")
        
        modul1_files = glob.glob(os.path.join(repo_path, "Modul_1", "**", "*.py"), recursive=True)
        modul2_files = glob.glob(os.path.join(repo_path, "Modul_2", "**", "*.py"), recursive=True)
        
        # Check files for Modul 1
        m1_status = "Lengkap" if len(modul1_files) >= 3 else ("Kurang" if len(modul1_files) > 0 else "Kosong")
        # Ensure files are not empty
        m1_valid = all(os.path.getsize(f) > 100 for f in modul1_files) if modul1_files else False
        
        # Check files for Modul 2
        m2_status = "Lengkap" if len(modul2_files) >= 3 else ("Kurang" if len(modul2_files) > 0 else "Kosong")
        m2_valid = all(os.path.getsize(f) > 100 for f in modul2_files) if modul2_files else False
        
        results[student_name] = {
            "Modul 1": {
                "Status": m1_status,
                "Valid (Not Empty)": m1_valid,
                "File Count": len(modul1_files)
            },
            "Modul 2": {
                "Status": m2_status,
                "Valid (Not Empty)": m2_valid,
                "File Count": len(modul2_files)
            }
        }
    
    with open("repo_evaluation.json", "w") as f:
        json.dump(results, f, indent=4)
    print(f"Evaluated {len(repos)} repositories. Saved to repo_evaluation.json.")

if __name__ == "__main__":
    check_repos("strukturdata-a-submissions")
