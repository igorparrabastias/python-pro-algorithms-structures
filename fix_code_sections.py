import os
import json

def fix_ipynb_files_v4(directory):
    report = "# Reporte de Corrección v4\n\nArchivos modificados:\n"
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                modified = False
                for cell in data.get("cells", []):
                    if cell["cell_type"] == "code":
                        # Remove ```python and ``` lines
                        new_source = [line for line in cell["source"] if line.strip() not in ["```python", "```"]]
                        # Remove trailing new lines at the end of code blocks
                        while new_source and new_source[-1].strip() == "":
                            new_source.pop()
                        new_source = [line for line in new_source if line.strip() != "pythonCopy code"]
                        # Remove a trailing newline from the last line if it exists
                        if new_source and new_source[-1].endswith("\n"):
                            new_source[-1] = new_source[-1].rstrip("\n")
                        # Check if modifications were made
                        if new_source != cell["source"]:
                            cell["source"] = new_source
                            modified = True

                if modified:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2)
                    report += f"- {file_path}\n"

    with open("report.md", "w", encoding="utf-8") as f_report:
        f_report.write(report)

# Ejecutar la función para corregir archivos en la carpeta 'notebook/' con las especificaciones actualizadas
fix_ipynb_files_v4("notebook/")
