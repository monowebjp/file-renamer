import os
path = "."
files = os.listdir(path)
print(type(files))

# ファイル名・ディレクトリ名混合
print(files)

# ファイル名のみの一覧を取得
files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
print(files_file)

# ディレクトリ名のみの一覧を取得
files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]
print(files_dir)