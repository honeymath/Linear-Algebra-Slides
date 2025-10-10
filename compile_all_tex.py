import subprocess
import os
import sys
import glob

TEMP_MAIN = "main_temp.tex"
TEMP_EXTENSIONS = [".aux", ".log", ".nav", ".snm", ".toc", ".out"]

def generate_main(tex_file):
    base = os.path.splitext(tex_file)[0]
    with open(TEMP_MAIN, "w", encoding="utf-8") as f:
        f.write(r"\documentclass{beamer}" + "\n")
        f.write(r"\input{package}" + "\n")
        f.write(r"\begin{document}" + "\n")
        f.write(rf"\input{{{base}}}" + "\n")
        f.write(r"\end{document}" + "\n")
    return base

def compile_and_clean(tex_file):
    base = generate_main(tex_file)

    print(f"✨ 正在编译：{tex_file} ...")
    result = subprocess.run(["pdflatex", TEMP_MAIN], capture_output=True, text=True)

    if result.returncode != 0:
        print(f"❌ 编译失败：{tex_file}")
        print(result.stderr)
        return

    output_pdf = "main_temp.pdf"
    target_pdf = f"{base}.pdf"
    if os.path.exists(output_pdf):
        os.rename(output_pdf, target_pdf)
        print(f"✅ 成功生成：{target_pdf}")
    else:
        print(f"❓ PDF 没有成功生成：{tex_file}")

    cleanup_temp_files()

def cleanup_temp_files():
    for ext in TEMP_EXTENSIONS + [".pdf", ".tex"]:
        temp_file = f"main_temp{ext}"
        if os.path.exists(temp_file):
            os.remove(temp_file)

def main():
    if len(sys.argv) < 2:
        print("用法：python compile_all_tex.py *.tex 或 指定多个 .tex 文件")
        return

    tex_files = []
    for arg in sys.argv[1:]:
        tex_files.extend(glob.glob(arg))

    if not tex_files:
        print("没有找到任何 .tex 文件喔～")
        return

    for tex_file in tex_files:
        if not tex_file.endswith(".tex"):
            print(f"跳过非 .tex 文件：{tex_file}")
            continue
        compile_and_clean(tex_file)

if __name__ == "__main__":
    main()